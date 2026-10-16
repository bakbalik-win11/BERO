# STEP-002 — GRV-008.3 kod inceleme kaydı
**Tarih:** 2026-10-16  
**Durum:** AÇIK — kod adayı depoya eklendi; derleme ve donanım testi yapılmadı.

## Hedef
ESP32D1 / ESP32-WROOM dahili ADC1 üzerinden GPIO34 (ADC1_CH6, SCT) ve GPIO35 (ADC1_CH7, BIAS) okumak; kanal başına 10 kHz hedefiyle 1000 örnek çifti bir binary frame olarak Mac'e aktarmak. Bu deneyde MCP3208 kullanılmaz.

## Bu oturumda yapılan
- Mevcut `GRV-008.2_candidate.ino` incelendi; orijinal dosya değiştirilmedi.
- Yeni aday eklendi: [`GRV-008.3_candidate_safety_patch.ino`](../KOD/GRV-008.3_candidate_safety_patch.ino).
- Callback alanı `on_pool_overflow` yerine ESP-IDF ADC Continuous API'deki `on_pool_ovf` olarak düzeltildi.
- DMA pool veya raw-queue taşması sayaçları değiştiğinde, eksik veri üzerinden devam eden kısmi frame atılacak şekilde işlem döngüsüne koruma eklendi.
- Değişiklik commit'i: `1e9b6a09d829efc818636fe776b78f7268b0b3d0`.

## Önemli sınırlar
- Bu kod henüz derlenmedi; bu nedenle API uyumu ve derlenebilirliği kanıtlanmış değildir.
- Donanımda flash, örnekleme hızı, sinyal doğruluğu, frame aktarımı veya Python alıcısıyla test yapılmadı.
- Callback içinde ham veriyi kopyalama, kanal sırası/örnek çifti eşleştirmesi, frame sürekliliği ve sürüm uyumu ayrıca derleme/test aşamasında kontrol edilmelidir.
- Binary frame mevcut protokol düzenini korumayı hedefler; Python alıcısı bu adayla birlikte doğrulanmadan veri toplama başlatılmamalıdır.

## Sıradaki işler
1. Hedef Arduino-ESP32 ve ESP-IDF sürümlerini belirle.
2. `GRV-008.3_candidate_safety_patch.ino` dosyasını gerçek hedef ortamında derle ve tam çıktıyı kaydet.
3. Derleme hatalarını kanıtına göre düzelt; eski adayı koru.
4. Derleme başarılı olursa USB seri portu ve frame alıcısını doğrula.
5. Fiziksel testte frame ID, marker, sampleCount, taşma sayaçları ve CSV örnek sayılarını kontrol et.

## Kapanış ölçütü
STEP-002 ancak hedef ortamda başarılı derleme kaydıyla derleme aşaması için tamamlanır. Donanım doğrulaması ayrı test kaydı gerektirir.
