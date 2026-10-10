#pragma once

#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "esp_err.h"
#include "esp_log.h"
#include "esp_timer.h"
#include "esp_adc/adc_oneshot.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

// GRV-004 raw ADC capture.
// GPIO32=BIAS/ADC1_CHANNEL_4; GPIO33=1T/ADC1_CHANNEL_5;
// GPIO34=2T/ADC1_CHANNEL_6; GPIO35=3T/ADC1_CHANNEL_7.
// Each speed captures 1000 scans of all four channels.
// Raw counts and relative timestamps are exported for computer analysis.

class ADCCharacterTest {
 public:
  void start() {
    if (task_handle_ != nullptr) {
      ESP_LOGW(TAG, "ADC characterization task is already running");
      return;
    }

    const BaseType_t created = xTaskCreatePinnedToCore(
        &ADCCharacterTest::task_entry, "adc_char_test", 8192,
        this, 1, &task_handle_, 1);

    if (created != pdPASS) {
      task_handle_ = nullptr;
      ESP_LOGE(TAG, "Could not create ADC characterization task");
    }
  }

 private:
  static constexpr uint32_t CHANNEL_COUNT = 4;
  static constexpr uint32_t SAMPLE_COUNT = 1000;
  static constexpr uint32_t LOG_CHUNK = 50;
  static constexpr const char *TAG = "ADC_CHARACTER";

  int16_t raw_[CHANNEL_COUNT][SAMPLE_COUNT];
  uint32_t sample_offset_us_[SAMPLE_COUNT];
  TaskHandle_t task_handle_ = nullptr;

  static void task_entry(void *argument) {
    auto *self = static_cast<ADCCharacterTest *>(argument);
    self->run();
    self->task_handle_ = nullptr;
    vTaskDelete(nullptr);
  }

  static const char *channel_name(uint32_t channel) {
    switch (channel) {
      case 0: return "BIAS";
      case 1: return "1T";
      case 2: return "2T";
      case 3: return "3T";
      default: return "UNKNOWN";
    }
  }

  void run() {
    const uint32_t speeds_ms[] = {1, 2, 5, 10};
    const adc_channel_t channels[CHANNEL_COUNT] = {
        ADC_CHANNEL_4, ADC_CHANNEL_5, ADC_CHANNEL_6, ADC_CHANNEL_7};

    adc_oneshot_unit_handle_t adc_handle = nullptr;
    adc_oneshot_unit_init_cfg_t unit_config = {};
    unit_config.unit_id = ADC_UNIT_1;
    unit_config.ulp_mode = ADC_ULP_MODE_DISABLE;

    esp_err_t error = adc_oneshot_new_unit(&unit_config, &adc_handle);
    if (error != ESP_OK) {
      ESP_LOGE(TAG, "adc_oneshot_new_unit failed: %s", esp_err_to_name(error));
      return;
    }

    adc_oneshot_chan_cfg_t channel_config = {};
    channel_config.atten = ADC_ATTEN_DB_12;
    channel_config.bitwidth = ADC_BITWIDTH_DEFAULT;

    for (uint32_t channel = 0; channel < CHANNEL_COUNT; ++channel) {
      error = adc_oneshot_config_channel(
          adc_handle, channels[channel], &channel_config);
      if (error != ESP_OK) {
        ESP_LOGE(TAG, "ADC channel setup failed ch=%u: %s",
                 static_cast<unsigned>(channel), esp_err_to_name(error));
        adc_oneshot_del_unit(adc_handle);
        return;
      }
    }

    ESP_LOGI(TAG, "START | channels=4 | samples/channel/speed=1000 | speeds=1,2,5,10ms");

    for (uint32_t speed_index = 0; speed_index < 4; ++speed_index) {
      const uint32_t target_ms = speeds_ms[speed_index];
      TickType_t period_ticks = pdMS_TO_TICKS(target_ms);
      if (period_ticks == 0) {
        period_ticks = 1;
      }

      uint32_t read_errors = 0;
      const int64_t run_start_us = esp_timer_get_time();
      TickType_t last_wake = xTaskGetTickCount();

      for (uint32_t sample = 0; sample < SAMPLE_COUNT; ++sample) {
        const int64_t scan_start_us = esp_timer_get_time();
        sample_offset_us_[sample] =
            static_cast<uint32_t>(scan_start_us - run_start_us);

        for (uint32_t channel = 0; channel < CHANNEL_COUNT; ++channel) {
          int raw_value = 0;
          error = adc_oneshot_read(adc_handle, channels[channel], &raw_value);
          if (error == ESP_OK) {
            raw_[channel][sample] = static_cast<int16_t>(raw_value);
          } else {
            raw_[channel][sample] = -1;
            ++read_errors;
          }
        }

        // Yield to ESPHome, Wi-Fi, API and PZEM tasks on every scan.
        // Timestamp deltas are calculated later on the computer.
        vTaskDelayUntil(&last_wake, period_ticks);
      }

      const int64_t total_us = esp_timer_get_time() - run_start_us;
      ESP_LOGI(TAG,
               "HIZ=%ums | ornek/kanal=%u | toplam=%.3fms | hatali_okuma=%u",
               static_cast<unsigned>(target_ms),
               static_cast<unsigned>(SAMPLE_COUNT),
               static_cast<double>(total_us) / 1000.0,
               static_cast<unsigned>(read_errors));

      dump_raw(target_ms);
      dump_timestamps(target_ms);
      ESP_LOGI(TAG, "HIZ_TAMAMLANDI | hiz=%ums", static_cast<unsigned>(target_ms));
      vTaskDelay(pdMS_TO_TICKS(100));
    }

    const esp_err_t delete_error = adc_oneshot_del_unit(adc_handle);
    if (delete_error != ESP_OK) {
      ESP_LOGW(TAG, "adc_oneshot_del_unit returned: %s", esp_err_to_name(delete_error));
    }
    ESP_LOGI(TAG, "ALL_SPEEDS_COMPLETE");
  }

  void dump_raw(uint32_t target_ms) {
    for (uint32_t channel = 0; channel < CHANNEL_COUNT; ++channel) {
      for (uint32_t base = 0; base < SAMPLE_COUNT; base += LOG_CHUNK) {
        char line[384] = {};
        size_t used = 0;
        const uint32_t end =
            (base + LOG_CHUNK < SAMPLE_COUNT) ? base + LOG_CHUNK : SAMPLE_COUNT;

        for (uint32_t index = base; index < end; ++index) {
          const int written = snprintf(
              line + used, sizeof(line) - used, "%s%d",
              index == base ? "" : ",",
              static_cast<int>(raw_[channel][index]));
          if (written < 0 || static_cast<size_t>(written) >= sizeof(line) - used) {
            break;
          }
          used += static_cast<size_t>(written);
        }

        ESP_LOGI(TAG, "RAW,%ums,%s,%u:%s",
                 static_cast<unsigned>(target_ms), channel_name(channel),
                 static_cast<unsigned>(base), line);
        vTaskDelay(pdMS_TO_TICKS(2));
      }
    }
  }

  void dump_timestamps(uint32_t target_ms) {
    for (uint32_t base = 0; base < SAMPLE_COUNT; base += LOG_CHUNK) {
      char line[384] = {};
      size_t used = 0;
      const uint32_t end =
          (base + LOG_CHUNK < SAMPLE_COUNT) ? base + LOG_CHUNK : SAMPLE_COUNT;

      for (uint32_t index = base; index < end; ++index) {
        const int written = snprintf(
            line + used, sizeof(line) - used, "%s%lu",
            index == base ? "" : ",",
            static_cast<unsigned long>(sample_offset_us_[index]));
        if (written < 0 || static_cast<size_t>(written) >= sizeof(line) - used) {
          break;
        }
        used += static_cast<size_t>(written);
      }

      ESP_LOGI(TAG, "TS_US,%ums,%u:%s",
               static_cast<unsigned>(target_ms),
               static_cast<unsigned>(base), line);
      vTaskDelay(pdMS_TO_TICKS(2));
    }
  }
};

ADCCharacterTest adc_char_test;
