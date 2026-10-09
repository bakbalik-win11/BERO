# Örnek Kod-2 — ESP32 + RS485 UART

PZEM-014 RS485 hattı, ESP32 GPIO'larına doğrudan bağlanmaz; uygun RS485 transceiver gerekir.

## Fiziksel katman
- PZEM A/B → transceiver A/B
- Transceiver RO → ESP32 UART RX
- ESP32 UART TX → transceiver DI
- DE/RE → uygun GPIO veya otomatik yön kontrollü transceiver
- GND/reference bağlantısı transceiver ve PZEM dokümanına göre yapılmalı.

USB–RS485 adaptörü ve MCU transceiver'ı farklı kullanım seçenekleridir. İkisi aynı anda bağlanacaksa bus topolojisi doğru tasarlanmalıdır.

## Ayar taslağı
- Baud: 9600
- Data bits: 8
- Parity: None
- Stop bits: 1
- Slave address: kılavuza göre doğrula; örneklerde genellikle 0x01.

## Test sırası
1. A/B ve UART yönlerini enerjisizken doğrula.
2. 9600 8N1 ayarını kullan.
3. Önce Input Register okuma isteği gönder.
4. Yanıt süresini, CRC hatalarını ve register sayısını kaydet.
5. Değerleri kılavuz ölçekleriyle yorumla; doğrulamadan register yazma.

Şebeke tarafı ile düşük gerilim kontrol tarafını ayır. İzolasyonlu RS485 transceiver kullanımı sistem risk değerlendirmesine bağlıdır. Bu sayfa derlenmiş/test edilmiş firmware değildir.