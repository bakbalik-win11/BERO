# GÖREVLER

Bu klasör, Proje BERO'nun ana hedeflerine bağlı görevleri ve görev bazında biriken deneyimi tutar. Görevler, üst düzey hedefleri somut ve doğrulanabilir çalışma adımlarına dönüştürür.

## Hedeflerle ilişki

- Ana hedef: HDF-NNN — istenen üst düzey sonuç ve tamamlanma ölçütleri.
- Görev: GRV-NNN — o sonuca katkı sağlayan sınırlı çalışma ve doğrulama adımı.
- Görev numaraları kronolojik olarak artar; bu görünümde yeni/açık çalışmalar üstte, tamamlanan görevler altta gösterilir.

## Görev düzeni

Her görev kendi klasöründe yer alır: GRV-NNN/.

- RAPOR/: görev hedefi, bağlı ana hedef, test planı, bağlantılar, gözlemler, sonuçlar, kararlar ve öğrenilenler.
- KOD/: göreve ait deney kodları ve her kod sürümünün yanında bulunan .md teknik kaydı.

Göreve ait tecrübe ve deney kodu burada tutulur. Sensöre veya donanıma özel kalıcı uygulama kodları, ilgili donanım/sensör klasörlerinde tutulmaya devam eder. Görev klasörü deney ve doğrulama geçmişini korur; kalıcı kodun asıl yerini kendiliğinden değiştirmez.

## Açık / çalışma sırasındaki görevler

### GRV-004 — ESP32D1 + PZEM + SCT013-1T/2T/3T

- [Görev raporu](GRV-004/RAPOR/README.md)
- Amaç: Bias yapısı ayrı görevde ele alındıktan sonra PZEM ve üç SCT013'ü aynı ESP32D1 deneyinde bir araya getirmek.
- [Alt Görev 2 — Fiziksel Okuma Notu](GRV-004/RAPOR/ALT-GOREV-02-FIZIKSEL-OKUMA.md)

### GRV-002 — ESP32D1 + PZEM-004T V3.0

- [Görev raporu](GRV-002/RAPOR/README.md)
- Amaç: ESP32D1 üzerinde PZEM-004T V3.0 UART/Modbus yapılandırmasını ve log kanıtını görev bazında saklamak.

### GRV-001 — ESP32-D ile SCT-013 Akım Okuması

- [Görev raporu](GRV-001/RAPOR/README.md)
- Bağlı ana hedef: [HDF-001 — Akımı Okuma](../HEDEFLER/HDF-001-AKIMI-OKUMA/HEDEF.md)
- Not: Bu dizinde GRV-001 için tamamlanma durumu ayrıca işaretlenmemiştir.

## Tamamlanan görevler

### GRV-003 — Trafo Bias Yapısının Kurulması ve Doğrulanması

- [Tamamlanan görev raporu](GRV-003/RAPOR/README.md)
- Sonuç: Ayrı ve taşınabilir güç kutusu kuruldu; regüle çıkış fiziksel olarak 3.30 V ölçüldü. GPIO32/33/34 üzerindeki 1.65 V okumaları da rapora kaydedildi.

## Görev sırası neden değişti?

GRV-003 ilk olarak birleşik PZEM + SCT013 deneyi olarak düşünülmüştü. SCT013 ölçümünün dayandığı trafo bias yapısının önce ayrı bir görevde açıklanması gerektiği görüldü. Bu nedenle bias çalışması GRV-003 oldu; birleşik sensör deneyi GRV-004'e kaydırıldı. Önceki ölçüm bilgileri silinmedi; yeni görev numarası altında korunarak ilişkilendirildi.

## Geçmişi koruma

- Kapanmış bir görevin raporu ve kod sürümleri üzerine yeni deney yazılmaz.
- Yeni deney, yeni dosya/sürüm veya yeni görev olarak kaydedilir.
- Düzeltmeler eski kaydı sessizce değiştirmek yerine ek notla belgelenir.
- Derleme gerektiren kod, kullanıcı derlemenin başarılı olduğunu doğrulamadan görev klasörüne taşınmaz.
- Ölçüm ve logların göstermediği sonuçlar doğrulanmış gibi yazılmaz.
- Ayrıntılı kural: [Kayıt, Sürümleme ve Süreklilik Politikası](../KAYIT_VE_SUREKLILIK.md).

## Yapının çalışma mantığı

- **GOREVLER/README.md:** Görevlerin sırasını ve birbirleriyle ilişkilerini gösteren ana dizin.
- **GRV-NNN/RAPOR/:** Görevin amacı, alt görevleri, fiziksel test notları, sonuçları ve kararları.
- **GRV-NNN/KOD/:** O göreve ait deney kodları ve kod sürümüne bağlı teknik kayıtlar.
- **DONANIM / KOD klasörleri:** Donanımın kalıcı referans bilgileri ve yeniden kullanılabilir örnekler; görev klasörleri ise belirli deneyin geçmişini tutar.
