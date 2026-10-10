# GRV-004 — ALT08 ADC Ham Veri Testi

**Tarih:** 2026-10-10  
**Durum:** Derleme başarılı (kullanıcı bildirimi); donanım/veri aktarım testi bekliyor.

## Hedef

ESP32-D1 üzerinden BIAS ve üç ADC kanalının ham sayısal değerlerini okumaya başlamak. Bu aşamada akım hesabı veya kalibrasyon yapılmaz.

## Donanım ve pinler

- ESP32 cihaz adı: `esp32d1`
- GPIO32: BIAS
- GPIO33: K1
- GPIO34: K2
- GPIO35: K3
- PZEM: Bu ALT08 deneme yapılandırmasında yok.

## Uygulama

- ESPHome yapılandırması: `GRV-004-ALT08-adc-ham-veri-test-20261010.yaml`
- Framework: Arduino
- Günlük seviyesi: INFO
- Okuma aralığı: 100 ms
- Her satırda örnek sıra numarası ve dört ADC okuması yazdırılır.

Örnek günlük biçimi:

```text
[ALT08_RAW] n=0,bias=...,k1=...,k2=...,k3=...
```

## Derleme sonucu

Kullanıcı 2026-10-10 tarihinde tam ALT08 YAML dosyasının derlendiğini bildirdi. Bu kayıt kullanıcı bildirimine dayanır; bağımsız derleme çalıştırması yapılmadı.

## Sınırlamalar ve sonraki adım

- Bu sürümün derlenmesi, ADC pinlerinden anlamlı ölçüm alındığını henüz kanıtlamaz.
- 100 ms aralık yaklaşık 10 kayıt/saniyedir; 50 Hz akım dalga biçiminin RMS analizi için yeterli değildir.
- Veriler henüz Mac'e aktarılmıyor ve CSV dosyası oluşturulmuyor.
- Bir sonraki adım: cihaz günlüklerinde `ALT08` başlangıç mesajını ve `ALT08_RAW` satırlarını doğrulamak. Ardından daha hızlı örnekleme ve ham verinin toplu aktarımı ayrı bir geliştirme olarak ele alınacak.

## Sürüm koruma

ALT08 ayrı deneydir. ALT06 ve ALT07 dosyaları bu kayıt kapsamında değiştirilmemiştir. Bu rapor, ALT08'in derlenebilir başlangıç aşamasını kaydeder; ölçüm doğrulaması veya kalibrasyon onayı değildir.
