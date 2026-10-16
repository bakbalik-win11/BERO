// PROJE BERO — GRV-008.2 CANDIDATE
// Hedef: ESP32-WROOM ADC1 CH6(GPIO34=SCT), CH7(GPIO35=BIAS) ham çift örneklerini
// ADC continuous/DMA ile toplamak ve 1000 çift örneği binary frame olarak seri aktarmak.
// Donanım: ESP32-WROOM-32, mevcut SCT/BIAS analog devresi, USB veri kablosu.
// NOT: Bu kod adaydır; Arduino-ESP32 sürümüyle derleme ve osiloskop/ham veri testi yapılmadı.

#include <Arduino.h>
#include <string.h>
#include <soc/soc_caps.h>
#include <esp_adc/adc_continuous.h>

#define SAMPLE_RATE_HZ       10000U       // Her kanal için hedef
#define SAMPLE_COUNT         1000U        // Her frame'de 1000 SCT + 1000 BIAS
#define CHANNEL_COUNT        2U
#define RAW_POOL_SIZE        4U
#define FRAME_POOL_SIZE      4U
#define ADC_ITEM_SIZE        sizeof(adc_digi_output_data_t)
#define SAMPLES_PER_DMA_BLOCK 100U      // 10 blok/frame; zaman aralığını ölçebilmek için
#define ADC_CONVERSIONS_PER_BLOCK (SAMPLES_PER_DMA_BLOCK * CHANNEL_COUNT)
#define DMA_BLOCK_SIZE       (ADC_CONVERSIONS_PER_BLOCK * ADC_ITEM_SIZE)
#define SERIAL_BAUD          921600

static constexpr uint32_t FRAME_START_MARKER = 0xDEADBEEF;
static constexpr uint32_t FRAME_END_MARKER   = 0xCAFEBABE;

struct __attribute__((packed)) SamplePair {
  uint16_t sct;
  uint16_t bias;
};

struct __attribute__((packed)) DataFrame {
  uint32_t startMarker;
  uint32_t frameId;
  uint32_t sampleRateHz;
  uint32_t sampleCount;
  uint32_t startMicros;
  uint32_t endMicros;
  uint32_t dmaOverflows;
  uint32_t rawQueueOverflows;
  uint32_t frameQueueOverflows;
  SamplePair samples[SAMPLE_COUNT];
  uint32_t endMarker;
};

struct RawBlockMessage {
  uint32_t poolIndex;
  uint32_t size;
  uint32_t callbackMicros;
};

static uint8_t rawPool[RAW_POOL_SIZE][DMA_BLOCK_SIZE];
static DataFrame framePool[FRAME_POOL_SIZE];
static QueueHandle_t rawFreeQueue = nullptr;   // index: processing task -> callback
static QueueHandle_t rawReadyQueue = nullptr;  // index+size+time: callback -> processing task
static QueueHandle_t frameFreeQueue = nullptr; // index: USB task -> processing task
static QueueHandle_t frameReadyQueue = nullptr; // completed frame index -> USB task
static adc_continuous_handle_t adcHandle = nullptr;

static volatile uint32_t dmaOverflowCount = 0;
static volatile uint32_t rawQueueOverflowCount = 0;
static volatile uint32_t frameQueueOverflowCount = 0;
static uint32_t nextFrameId = 0;

static bool IRAM_ATTR onConversionDone(adc_continuous_handle_t,
                                      const adc_continuous_evt_data_t *edata,
                                      void *) {
  BaseType_t taskWoken = pdFALSE;
  if (edata == nullptr || edata->conv_frame_buffer == nullptr || edata->size == 0) {
    return false;
  }

  uint32_t poolIndex;
  if (xQueueReceiveFromISR(rawFreeQueue, &poolIndex, &taskWoken) != pdTRUE) {
    rawQueueOverflowCount++;
    return taskWoken == pdTRUE;
  }

  if (edata->size > DMA_BLOCK_SIZE) {
    rawQueueOverflowCount++;
    xQueueSendFromISR(rawFreeQueue, &poolIndex, &taskWoken);
    return taskWoken == pdTRUE;
  }

  memcpy(rawPool[poolIndex], edata->conv_frame_buffer, edata->size);
  RawBlockMessage msg;
  msg.poolIndex = poolIndex;
  msg.size = edata->size;
  msg.callbackMicros = micros();

  if (xQueueSendFromISR(rawReadyQueue, &msg, &taskWoken) != pdTRUE) {
    rawQueueOverflowCount++;
    xQueueSendFromISR(rawFreeQueue, &poolIndex, &taskWoken);
  }
  return taskWoken == pdTRUE;
}

static bool IRAM_ATTR onPoolOverflow(adc_continuous_handle_t,
                                     const adc_continuous_evt_data_t *,
                                     void *) {
  dmaOverflowCount++;
  return false;
}

static void adcProcessingTask(void *) {
  RawBlockMessage msg;
  uint32_t sampleIndex = 0;
  uint32_t frameStartMicros = 0;
  uint16_t pendingSct = 0, pendingBias = 0;
  bool haveSct = false, haveBias = false;
  int32_t activeFrameIndex = -1;

  for (;;) {
    if (xQueueReceive(rawReadyQueue, &msg, portMAX_DELAY) != pdTRUE) continue;

    if (sampleIndex == 0 && activeFrameIndex < 0) {
      uint32_t idx;
      if (xQueueReceive(frameFreeQueue, &idx, 0) != pdTRUE) {
        frameQueueOverflowCount++;
        xQueueSend(rawFreeQueue, &msg.poolIndex, 0);
        continue;
      }
      activeFrameIndex = (int32_t)idx;
      frameStartMicros = msg.callbackMicros;
      haveSct = false;
      haveBias = false;
    }

    const uint32_t itemCount = msg.size / ADC_ITEM_SIZE;
    for (uint32_t i = 0; i < itemCount; ++i) {
      const adc_digi_output_data_t *p =
        reinterpret_cast<const adc_digi_output_data_t *>(&rawPool[msg.poolIndex][i * ADC_ITEM_SIZE]);
      const uint32_t channel = p->type2.channel;
      const uint16_t value = p->type2.data;

      if (channel == ADC_CHANNEL_6) {
        pendingSct = value;
        haveSct = true;
      } else if (channel == ADC_CHANNEL_7) {
        pendingBias = value;
        haveBias = true;
      } else {
        continue;
      }

      // Kanal sırasına varsayım yapma: yalnızca CH6 ve CH7 birlikte geldiyse bir çift yaz.
      if (haveSct && haveBias && activeFrameIndex >= 0 && sampleIndex < SAMPLE_COUNT) {
        framePool[activeFrameIndex].samples[sampleIndex].sct = pendingSct;
        framePool[activeFrameIndex].samples[sampleIndex].bias = pendingBias;
        sampleIndex++;
        haveSct = false;
        haveBias = false;

        if (sampleIndex == SAMPLE_COUNT) {
          DataFrame &f = framePool[activeFrameIndex];
          f.startMarker = FRAME_START_MARKER;
          f.frameId = nextFrameId++;
          f.sampleRateHz = SAMPLE_RATE_HZ;
          f.sampleCount = SAMPLE_COUNT;
          f.startMicros = frameStartMicros;
          f.endMicros = msg.callbackMicros;
          f.dmaOverflows = dmaOverflowCount;
          f.rawQueueOverflows = rawQueueOverflowCount;
          f.frameQueueOverflows = frameQueueOverflowCount;
          f.endMarker = FRAME_END_MARKER;

          const uint32_t completedIndex = (uint32_t)activeFrameIndex;
          if (xQueueSend(frameReadyQueue, &completedIndex, 0) != pdTRUE) {
            frameQueueOverflowCount++;
            xQueueSend(frameFreeQueue, &completedIndex, 0);
          }
          activeFrameIndex = -1;
          sampleIndex = 0;
          haveSct = false;
          haveBias = false;
        }
      }
    }

    // Raw block is returned only after every item in it has been parsed.
    xQueueSend(rawFreeQueue, &msg.poolIndex, portMAX_DELAY);
  }
}

static void usbBinaryTask(void *) {
  uint32_t frameIndex;
  for (;;) {
    if (xQueueReceive(frameReadyQueue, &frameIndex, portMAX_DELAY) != pdTRUE) continue;
    const uint8_t *bytes = reinterpret_cast<const uint8_t *>(&framePool[frameIndex]);
    size_t remaining = sizeof(DataFrame);
    while (remaining > 0) {
      const size_t written = Serial.write(bytes, remaining);
      if (written == 0) { vTaskDelay(1); continue; }
      bytes += written;
      remaining -= written;
    }
    xQueueSend(frameFreeQueue, &frameIndex, portMAX_DELAY);
  }
}

static void initAdcContinuous() {
  adc_continuous_handle_cfg_t handleConfig = {};
  handleConfig.max_store_buf_size = DMA_BLOCK_SIZE * RAW_POOL_SIZE;
  handleConfig.conv_frame_size = DMA_BLOCK_SIZE;
  ESP_ERROR_CHECK(adc_continuous_new_handle(&handleConfig, &adcHandle));

  adc_digi_pattern_config_t pattern[CHANNEL_COUNT] = {};
  pattern[0].atten = ADC_ATTEN_DB_12;
  pattern[0].channel = ADC_CHANNEL_6; // GPIO34 / ADC1_CH6
  pattern[0].unit = ADC_UNIT_1;
  pattern[0].bit_width = SOC_ADC_DIGI_MIN_BITWIDTH;
  pattern[1].atten = ADC_ATTEN_DB_12;
  pattern[1].channel = ADC_CHANNEL_7; // GPIO35 / ADC1_CH7
  pattern[1].unit = ADC_UNIT_1;
  pattern[1].bit_width = SOC_ADC_DIGI_MIN_BITWIDTH;

  adc_continuous_config_t config = {};
  config.sample_freq_hz = SAMPLE_RATE_HZ * CHANNEL_COUNT;
  config.conv_mode = ADC_CONV_SINGLE_UNIT_1;
  config.format = ADC_DIGI_OUTPUT_FORMAT_TYPE2;
  config.pattern_num = CHANNEL_COUNT;
  config.adc_pattern = pattern;
  ESP_ERROR_CHECK(adc_continuous_config(adcHandle, &config));

  adc_continuous_evt_cbs_t callbacks = {};
  callbacks.on_conv_done = onConversionDone;
  callbacks.on_pool_overflow = onPoolOverflow;
  ESP_ERROR_CHECK(adc_continuous_register_event_callbacks(adcHandle, &callbacks, nullptr));
  ESP_ERROR_CHECK(adc_continuous_start(adcHandle));
}

void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(1000);

  rawFreeQueue = xQueueCreate(RAW_POOL_SIZE, sizeof(uint32_t));
  rawReadyQueue = xQueueCreate(RAW_POOL_SIZE, sizeof(RawBlockMessage));
  frameFreeQueue = xQueueCreate(FRAME_POOL_SIZE, sizeof(uint32_t));
  frameReadyQueue = xQueueCreate(FRAME_POOL_SIZE, sizeof(uint32_t));
  if (!rawFreeQueue || !rawReadyQueue || !frameFreeQueue || !frameReadyQueue) {
    while (true) delay(1000);
  }
  for (uint32_t i = 0; i < RAW_POOL_SIZE; ++i) xQueueSend(rawFreeQueue, &i, 0);
  for (uint32_t i = 0; i < FRAME_POOL_SIZE; ++i) xQueueSend(frameFreeQueue, &i, 0);

  xTaskCreatePinnedToCore(adcProcessingTask, "ADC_Process", 6144, nullptr, 3, nullptr, 0);
  xTaskCreatePinnedToCore(usbBinaryTask, "USB_Binary", 4096, nullptr, 1, nullptr, 1);
  initAdcContinuous();
}

void loop() { vTaskDelay(pdMS_TO_TICKS(1000)); }