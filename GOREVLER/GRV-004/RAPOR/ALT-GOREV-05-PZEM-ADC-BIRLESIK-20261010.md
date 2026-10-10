# GRV-004 — ALT-GÖREV-05: Aynı koda PZEM ekleme

- Tarih: 2026-10-10
- Cihaz adı korunmuştur: `esp32d1` / `ESP32D1`
- Taban sürüm: [Dört kanal MIN/MAX/ORT/STD sürekli ADC YAML](KOD/esp32d1-4ch-1000-min-max-avg-std-continuous-20261010.yaml)
- Yeni aday: [PZEM eklenmiş dört kanal YAML](KOD/esp32d1-4ch-1000-min-max-avg-std-pzem-continuous-20261010.yaml)
- Durum: **Kod adayı oluşturuldu; derleme ve cihaz testi bekliyor.**

## Hedef

Mevcut dört ADC kanalının tur bazlı MIN, MAX, ortalama ve popülasyon standart sapması hesabını değiştirmeden aynı YAML'a PZEM telemetrisini eklemek.

## Korunan yapı

- GPIO32: BIAS
- GPIO33: 1T
- GPIO34: 2T
- GPIO35: 3T
- ADC güncelleme aralığı: 10 ms
- Her kanal için tur başına hedef: 1000 örnek
- Dört kanalın sonuçları tamamlanınca tek `ADC_TEST` satırı; sayaç ve istatistiklerin sıfırlanması
- ESP adı ve friendly name: `esp32d1` / `ESP32D1`

## Eklenen PZEM yapılandırması

- UART TX: GPIO16
- UART RX: GPIO17
- Baud: 9600
- Stop bit: 1
- ESPHome `modbus` bileşeni
- `pzemac` sensörleri: gerilim, akım, güç, enerji, frekans ve güç faktörü
- PZEM güncelleme aralığı: 5 saniye

## Doğrulama sınırları

- Bu kayıt bir YAML adayının oluşturulduğunu belirtir; derlemenin başarılı olduğu anlamına gelmez.
- Cihazda PZEM ve ADC işlevlerinin aynı anda çalıştığı henüz doğrulanmadı.
- PZEM telemetrisi ESPHome sensörleri olarak Home Assistant'a sunulacak. Mevcut `logger` ayarındaki `sensor: NONE`, sensörlerin rutin log çıktısını susturabilir; bu, API üzerinden sensör varlığını tek başına engellemez.
- Dört ADC kanalının 1000 örnek/tur şartı önceki loglarda doğrudan sayaçla kanıtlanmış değildi; bu görev bu doğrulama açığını kapatmış sayılmaz.
- Önceki STD'li ve STD'siz YAML snapshot'ları değiştirilmedi.

## Kabul adımları

- [ ] ESPHome derlemesi başarılı
- [ ] API bağlantısı başarılı
- [ ] PZEM gerilim/akım/güç/enerji/frekans/güç faktörü sensörleri görünür
- [ ] ADC_TEST tur satırları devam ediyor
- [ ] PZEM eklenmesinin ADC tur süresine etkisi log üzerinden gözleniyor
