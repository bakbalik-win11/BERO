# Örnek Kod-3 — UART/Modbus teşhis notları

## Fiziksel seri ayarları

PZEM-004T V3.0 dokümanı UART-TTL için 9600 baud, 8 veri biti, parity yok, 1 stop biti (9600 8N1) belirtir. Uygulama katmanı Modbus-RTU benzeri protokol kullanır.

## Okuma başarısızsa sırayla kontrol et

1. Modülün tam sürümü ve protokol uyumu.
2. PZEM TTL tarafında 5V ve GND bağlantılarının ikisi de mevcut mu?
3. TX/RX çapraz mı bağlandı? Gerekirse enerjisizken bağlantıyı doğrula.
4. ESP32 UART pinleri doğru mu ve başka log çıktısıyla çakışıyor mu?
5. 9600 8N1 ayarı doğru mu?
6. Modülün AC ölçüm beslemesi/gerilim bağlantısı üretici şemasına göre doğru ve güvenli mi?
7. Varsayılan cihaz adresi ve kütüphane varsayımları uyumlu mu? Çoklu cihazda her cihaza uygun benzersiz adres gerekebilir.

## Kayda geçir

- Modül model/revizyonu
- Kütüphane ve ESPHome sürümü
- UART pinleri ve ayarlar
- Ham hata mesajı / NaN durumu
- Beklenen ve ölçülen V, A, W, PF, Hz ve kWh
- Referans ölçüm cihazı ve yük

Kaynaklar:
- https://github.com/mandulaj/PZEM-004T-v30
- https://esphome.io/components/sensor/pzemac/

Bu sayfa bir teşhis kontrol listesidir; herhangi bir bağlantı veya yazılım çözümü test edilmiş sonuç olarak sunulmamaktadır.