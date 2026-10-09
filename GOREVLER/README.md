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
- KOD/: göreve ait deney kodu ve test araçları.

Göreve ait tecrübe ve deney kodu burada tutulur. Sensöre veya donanıma özel kalıcı uygulama kodları, ilgili donanım/sensör klasörlerinde tutulmaya devam eder. Görev klasörü deney ve doğrulama geçmişini korur; kalıcı kodun asıl yerini kendiliğinden değiştirmez.

## Kod doğrulama kuralları

- Derleme gerektiren kod, kullanıcı derlemenin başarılı olduğunu doğrulamadan görev klasörüne taşınmaz.
- Her kod sürümünün yanında, hedefi, donanımı, sürümün işlevini, doğrulananları, test koşullarını/sonuçlarını, loglardan öğrenilenleri, hataları, doğrulanmamış noktaları ve sonraki adımı açıklayan bir .md dosyası bulunur.
- Ölçüm ve logların göstermediği sonuçlar doğrulanmış gibi yazılmaz.

## İlk görev

- [GRV-001 — ESP32-D ile SCT-013 Akım Okuması](GRV-001/RAPOR/README.md)
- Bağlı ana hedef: [HDF-001 — Akımı Okuma](../HEDEFLER/HDF-001-AKIMI-OKUMA/HEDEF.md)

Görev numaraları sıralı ilerler: GRV-001, GRV-002, ...
