# Hesaplama-2 — DC akım, işaret ve ofset (5A)

Örneklerin ortalama sensör çıkış gerilimi:

Vmean = sum(VIOUT[i]) / N

Sıfır akım ofseti V0, akım yokken ölçülür.

I_DC ≈ (Vmean − V0) / 0.185 A

Örnek: V0=2,500 V ve Vmean=2.870 V ise yaklaşık +2 A; akım yönü tersse işaret negatiftir.

**Hata uyarısı:** Ölçüm penceresinin ortalamasını her seferinde ofset kabul edip çıkarmak gerçek DC akımı sıfırlar. DC akım için **ayrı ölçülmüş V0** kullan. Sıcaklık ve VCC değişirse V0 kayabilir; kalibrasyon stratejisi gereklidir.

ACS712 çift yönlü Hall sensörüdür; SCT013 gibi yalnız AC ölçmez.
