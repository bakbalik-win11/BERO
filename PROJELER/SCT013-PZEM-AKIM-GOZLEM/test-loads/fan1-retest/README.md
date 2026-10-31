# FAN-1-RETEST-001 — FAN-1 yeniden gözlem oturumu

**Durum:** AÇIK — yeni fiziksel ölçüm ve log bekleniyor.

## Amaç
FAN-1 fan kademesini Modül 2 / ESP32D1 / SCT-1 hattında yeniden gözlemlemek. Bu, daha önce kapatılmış FAN-1 ısınma/deneme oturumunun üzerine yazmaz; ayrı test kimliği ve ayrı log kullanır. Düşük akım için ayrılmış eğitim/veri sınıfına katkı sağlayacak gözlem toplamaktır.

## Sabit düzenek
- Kart/modül: ESP32D1 / Modül 2.
- SCT-1 sarı sinyal: GPIO32 / ADC1_CH4.
- Ortak bias turuncu: GPIO35 / ADC1_CH7.
- Mevcut SCT013-030 (30A/1V).
- Firmware: `firmware/esp32d1.yaml`; FAN-3-3T-001 kapanışında kullanılan snapshot ile aynı aktif YAML içeriği.
- ESPHome 2026.10.1; ADC 12 dB / 1 s; ct_clamp 200 ms / 2 s.
- K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.
- Başlangıçta tek primer tur kabul edilir; tur sayısı farklıysa log başlığı ve analiz metadata'sında açıkça yazılır.

## Referans ve değerlendirme
- FAN-1 için son UNIT bildirimi 0,093 A; önceki 0,097 A ve 0,096 A bildirimleri tarihsel nottur.
- 0,30 A altında ±%4 kabul/ret uygulanmaz. UNIT değeri yalnız kaynak türü belirtilmiş karşılaştırma bilgisi olarak saklanır.
- PZEM akımı ve PF mevcutsa ayrı alanlarda kaydedilir; UNIT ve PZEM birbirine karıştırılmaz.
- SCT toplam hat akımını gözlemler; SCT'den PF hesaplanmaz.

## Ölçüm protokolü
1. Fan kapalı başlangıç tabanını kaydet.
2. FAN-1 açılma anını saat/olay notuyla işaretle.
3. Kararlı FAN-1 penceresini yeterli süre kaydet.
4. FAN-1 kapanış anını işaretle ve fan kapalı son taban penceresini kaydet.
5. Varsa UNIT/PZEM ölçümlerini aynı kararlı pencereye bağla.
6. Ham log, firmware akım, Raw AC, bias, SCT ADC ve SPS verilerini koru. Geçiş verisini kararlı veriyle karıştırma.

## Kapanış koşulları
- Ham log ve kaynak SHA-256 kaydedilecek.
- Analiz raporu gerçek logdan üretilecek; ölçülmeyen veri tamamlanmış gibi yazılmayacak.
- Test kapatılırken kullanılan son YAML snapshot arşivlenecek ve log/analiz ona bağlanacak.
- Arşiv dosyaları GitHub'da tekrar okunup doğrulanmadan test kapatılmayacak.

## Tarihsel FAN-1 kaydı
Önceki FAN-1 oturumu 0,093 A UNIT bildirimiyle düşük akım gözlemi olarak kapatılmıştır. Eski ham log, analiz ve kapanış YAML dosyaları değiştirilmeyecektir. Bu yeni test ayrı oturumdur.
