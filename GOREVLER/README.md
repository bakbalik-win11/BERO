# GÖREVLER

Bu klasör, Proje BERO'nun ana hedeflerine bağlı görevleri ve görev bazında biriken deneyimi tutar. Görevler, üst düzey hedefleri somut ve doğrulanabilir çalışma adımlarına dönüştürür.

## Hedeflerle ilişki

Her görev, katkı sağladığı ana hedefle ilişkilendirilir. Ana hedeflerin tanımı ve hedefe bağlı görev silsilesi HEDEFLER/ altında tutulur.

- Ana hedef: HDF-NNN — istenen üst düzey sonuç ve tamamlanma ölçütleri.
- Görev: GRV-NNN — o sonuca katkı sağlayan sınırlı çalışma ve doğrulama adımı.
- Görev sırası, elde edilen bulgulara göre planlanır; yeni bir ana hedefe geçiş mevcut hedefin sonucu değerlendirildikten sonra ayrıca kararlaştırılır.

## Görev düzeni

Her görev kendi klasöründe yer alır: GRV-NNN/.

Her görev klasöründe:
- RAPOR/: görev hedefi, bağlı ana hedef, test planı, bağlantılar, gözlemler, sonuçlar, kararlar ve öğrenilenler.
- KOD/: göreve ait deney kodları ve her kod sürümünün yanında bulunan .md teknik kaydı.

Göreve ait tecrübe ve deney kodu burada tutulur. Sensöre veya donanıma özel kalıcı uygulama kodları, ilgili donanım/sensör klasörlerinde tutulmaya devam eder. Görev klasörü deney ve doğrulama geçmişini korur; kalıcı kodun asıl yerini kendiliğinden değiştirmez.

## Geçmişi koruma

- Kapanmış bir görevin raporu ve kod sürümleri üzerine yeni deney yazılmaz.
- Yeni deney, yeni dosya/sürüm veya yeni görev olarak kaydedilir.
- Düzeltmeler eski kaydı sessizce değiştirmek yerine ek notla belgelenir.
- Derleme gerektiren kod, kullanıcı derlemenin başarılı olduğunu doğrulamadan görev klasörüne taşınmaz.
- Ölçüm ve logların göstermediği sonuçlar doğrulanmış gibi yazılmaz.
- Ayrıntılı kural: [Kayıt, Sürümleme ve Süreklilik Politikası](../KAYIT_VE_SUREKLILIK.md).

## İlk görev

- [GRV-001 — ESP32-D ile SCT-013 Akım Okuması](GRV-001/RAPOR/README.md)
- Bağlı ana hedef: [HDF-001 — Akımı Okuma](../HEDEFLER/HDF-001-AKIMI-OKUMA/HEDEF.md)

Görev numaraları sıralı ilerler: GRV-001, GRV-002, ...

## İkinci görev

- [GRV-002 — ESP32D1 + PZEM-004T V3.0](GRV-002/RAPOR/README.md)
- Amaç: ESP32D1 üzerinde PZEM-004T V3.0 UART/Modbus yapılandırmasını ve log kanıtını görev bazında saklamak.
