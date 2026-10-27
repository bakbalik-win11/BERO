# Proje donanım referansları

Bu klasör, önceki BERO donanım çalışmalarındaki teknik Markdown belgelerinin bu projede doğrudan kullanılabilmesi için hazırlanmış kopyalarını içerir.

- [SCT013-100A-1V — 100 A / 1 V](SCT013-100A-1V.md)
- [SCT013-30A-1V — 30 A / 1 V](SCT013-30A-1V.md)
- [PZEM-004T V3.0 — AC ölçüm modülü](PZEM-004T-V3.0.md)
- [SSR — donanım referansı](SSR.md)
- [SSR — ürün sayfası ve model eşleştirme notu](SSR-datasheet-candidate.md)
- [DS3231 — RTC donanım referansı](DS3231.md)
- [DS3231 — resmî veri sayfası bağlantısı](DS3231-datasheet.md)

## Kaynak belgeler
- [`DONANIM/SCT013-100A-1V/README.md`](../../../../DONANIM/SCT013-100A-1V/README.md)
- [`DONANIM/SCT013-30A-1V/README.md`](../../../../DONANIM/SCT013-30A-1V/README.md)
- [`DONANIM/PZEM-004T/README.md`](../../../../DONANIM/PZEM-004T/README.md)
- [`DONANIM/SSR/README.md`](../../../../DONANIM/SSR/README.md)
- [`DONANIM/SSR/datasheets/README.md`](../../../../DONANIM/SSR/datasheets/README.md)
- [`DONANIM/DS3231/README.md`](../../../../DONANIM/DS3231/README.md)
- [`DONANIM/DS3231/datasheets/README.md`](../../../../DONANIM/DS3231/datasheets/README.md)

Kaynak belgeler asıl kayıttır. Kopyalar önceki bilgileri proje içinde erişilebilir yapar; kopyanın varlığı fiziksel seçimi, yeni deney veya kalibrasyon sonucunu doğrulamaz. Kaynak metinler değişirse kopyalar eşitlenmelidir.

**SSR notu:** Kullanıcının satın alma bağlantısı 5 V, 2 kanallı SAMM Market kartını tanımlar (tedarikçi kodu İzmo9659, SKU MP02637). Ürün sayfası özellikleri envantere kaydedildi. Kart üzerindeki gerçek SSR entegrenin tam model kodu doğrulanmadığından Omron G3MB veri sayfası yalnız karşılaştırma kaynağıdır; kesin parça eşleşmesi değildir.

**DS3231 notu:** Teknik referans önceki BERO donanım belgesinden kopyalandı ve Analog Devices resmî veri sayfasıyla desteklendi. Önceki ESP32-C3 SDA/SCL pinleri bu projeye otomatik taşınmaz; yeni pin planı ve breakout pil/pull-up devresi ayrıca doğrulanmalıdır.
