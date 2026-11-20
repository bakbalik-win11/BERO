# ADR-033 — BERO modül kimlikleri: masaüstü ölçüm, cihaz gözlem ve PreBERO ana hat

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ — modül numaralandırması ve işlev ayrımı
- **Karar sahibi:** Kullanıcı

## Bağlam

Önceki dokümanlarda E22 deney fikri yanlışlıkla ayrı bir 100 A / 1 V ölçüm modülü gibi tanımlanmış; çamaşır ve bulaşık makinesi gözlem modülleri de Modül 4/5 olarak numaralandırılmıştı. Kullanıcı gerçek yapıyı düzeltti. E22 kapsamında 100 A / 1 V SCT ile hiçbir ölçüm alınmadı ve bu amaçla ayrı bir modül imal edilmedi.

## Kabul edilen modül envanteri

| Kimlik | Tanım | İşlev / durum |
|---|---|---|
| Modül 1 | Bağımsız bias trafosu / güç kutusu | Korunacak mevcut donanım |
| Modül 2 | Eski üçlü SCT okuma modülü | İmha edildi; firmware ve kayıtlar tarihsel arşiv |
| Modül 3 | Eski PZEM + SSR olay modülü | İmha edildi; firmware ve kayıtlar tarihsel arşiv |
| **Modül 4** | Günlük masaüstü ESP32D2 + ADS1115 + SCT ölçüm düzeneği | Mevcut çalışma düzeneği ve günlük ölçüm baseline'ı |
| **Modül 5** | Çamaşır makinesi gözlem modülü | İmal edilecek |
| **Modül 6** | Bulaşık makinesi gözlem modülü | İmal edilecek |
| **Modül 7 / PreBERO** | Ana hat gözlem düzeneği | Ana hattı PZEM ile birlikte okumak için hedef; tasarım/test bekliyor |

## Modül 4 ve E22 ilişkisi

- Modül 4, mevcut günlük masaüstü ESP32D2 + ADS1115 + SCT ölçüm düzeneğidir.
- E22 bir cihaz/modül kimliği değildir; deney numarasıdır.
- Modül 4'ün mevcut ölçüm zinciri başarılı ve kararlı çalıştıktan sonra 100 A / 1 V SCT'yi aynı ölçüm yaklaşımında deneme fikri vardır.
- Görüşülen olası karşılaştırma: bir kanalda 30 A / 1 V, diğer kanalda 100 A / 1 V SCT. İki kanalın fiziksel bağlantısı ve aynı anda/ayrı oturumda ölçüm yöntemi henüz kararlaştırılmamıştır.
- E22 kapsamında bugüne kadar 100 A SCT bağlantısı, firmware, derleme, OTA, ölçüm veya analiz yapılmamıştır. Sonuç/katsayı/başarı iddiası yoktur.
- Mevcut 30 A / 1 V ölçüm firmware'i korunur; 100 A sensör için değişiklik gerekirse deney snapshot'ı ayrı tutulur.

## Modül 5 ve 6 ilişkisi

Modül 5 çamaşır, Modül 6 bulaşık makinesi gözlem modülüdür. Aynı elektronik tasarımın iki fiziksel kopyasıdır. Donanım listesi ve I²C ayrımı ADR-032'de tanımlıdır; ADR-032'deki eski Modül 4/5 numaraları bu ADR ile 5/6 olarak düzeltilmiştir. Fiziksel imalat ve doğrulama henüz yapılmamıştır.

## Modül 7 / PreBERO

Modül 7'nin amacı PreBERO çalışmaları sırasında ana hattı PZEM ile birlikte okumaktır. Bu karar yalnızca modülün kimliğini ve üst düzey amacını belirler. CT modeli, PZEM topolojisi, ESP kartı, bağlantılar, haberleşme, firmware, muhafaza ve test sırası ayrıca tasarlanıp doğrulanacaktır.

## Tarihçe ve geçerlilik

- 2026-11-13 tarihli eski kayıtlarda 100 A / 1 V SCT + ADS1115 + PZEM fikri Modül 4 olarak adlandırılmıştı. Bu, o tarihteki planlama kaydıdır; fiziksel olarak kurulmuş modül/ölçüm kanıtı değildir.
- 2026-11-20 tarihli önceki Modül 4/5 çamaşır/bulaşık ataması da bu karar ile güncellenmiştir.
- Eski kayıtlar silinmez; güncel modül kimlikleri için bu ADR esas alınır.

## İlgili kayıtlar

- [Modül 5 — Çamaşır makinesi](../devices/washing-machine/README.md)
- [Modül 6 — Bulaşık makinesi](../devices/dishwasher/README.md)
- [E22 — 30 A / 1 V ve 100 A / 1 V karşılaştırma fikri](../../experiments/E22-sct100a-1v-ads1115-characterization/README.md)
- [ADR-032 — İkiz sensör modülleri](ADR-032-washing-dishwasher-twin-sensor-modules.md)
