# DS3231 — Resmî Veri Sayfası

> **Proje referans kopyası:** BERO kaynağı [`DONANIM/DS3231/datasheets/README.md`](../../../../DONANIM/DS3231/datasheets/README.md).

Üretici: Analog Devices (eski Maxim Integrated).

Resmî PDF: https://www.analog.com/media/en/technical-documentation/data-sheets/ds3231.pdf

Kaynak BERO deposunda PDF'nin kendisi bulunmuyor; bu Markdown dosyası üreticinin resmî PDF bağlantısını ve kaynak kaydını proje içinde erişilebilir kılmak için oluşturuldu.

Önemli özellik özeti:
- I²C arabirimi, 400 kHz'e kadar
- VCC çalışma aralığı 2,3–5,5 V; 3,3 V çalışma desteği
- RTC takvim kayıtları ve 2100'e kadar artık yıl düzeltmesi
- Ana besleme kesildiğinde VBAT üzerinden saat tutma
- ±2 ppm (0–40 °C), ±3,5 ppm (-40…+85 °C) doğruluk belirtimi
- İki alarm, INT/SQW ve 32,768 kHz çıkış

Kesin elektriksel sınırlar, timing grafikleri ve pin tanımları için resmî PDF kullanılmalıdır.
