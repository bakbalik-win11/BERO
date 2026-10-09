# Örnek Kod-3 — UART haberleşme hata ayıklama

## Kontrol listesi

1. PZEM sürümünü doğrula: V1/V2/V3 kütüphane uyumluluğunu varsayma.
2. PZEM'in AC ölçüm kısmı doğru şebeke bağlantısını gerektirir; yalnızca 5 V UART beslemesi ölçüm yapması için yeterli olmayabilir.
3. GND ve TX/RX çapraz bağlantısını doğrula.
4. UART 9600, 8N1 ayarını V3.0 dokümanıyla karşılaştır.
5. Kütüphanenin hata/NaN çıktısını kaydet; besleme, kablo, adres ve model uyumluluğunu sırayla kontrol et.
6. TTL sinyallerini analizörle gözlemleyeceksen yalnızca düşük gerilimli UART tarafını kullan; ortak GND ve lojik seviyelerini doğrula.
7. Şebeke bağlantısı gerektiren testlerde açık kart üzerinde çalışma; uygun muhafaza ve izolasyon kullan.

## Lojik analizör kanal önerisi

- CH0: ESP32 TX → PZEM RX
- CH1: PZEM TX → ESP32 RX
- GND: yalnızca düşük gerilimli UART tarafının ortak referansı

PZEM'in AC giriş terminallerine veya şebeke tarafına lojik analizör probu/GND bağlama.

V3.0 kaynakları Modbus-RTU benzeri çerçeve ve CRC16 kullanır. Ham baytları yorumlarken PZEM sürümüne uygun protokol belgesini kullan.

Kaynak: https://github.com/mandulaj/PZEM-004T-v30