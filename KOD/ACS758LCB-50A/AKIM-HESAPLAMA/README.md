# ACS758LCB — Akım hesaplama yöntemleri

## Hesaplama sırası

1. Sensörün tam varyantını belirle: 050B çift yönlü 40 mV/A mı, 050U tek yönlü 60 mV/A mı?
2. Sıfır akımda VIOUT ofsetini ölç.
3. ADC raw kodunu gerçek giriş gerilimine dönüştür; VREF, bit çözünürlüğü ve giriş bölücü/kazanç oranını dahil et.
4. Ofseti çıkar.
5. DC akım için ortalama gerilim farkını; AC için ofset çıkarılmış RMS değerini hesapla.
6. Nominal hassasiyetle başlangıç amper değerini hesapla.
7. Birden çok noktada referans ampermetreyle kalibrasyon yap.

## Dosyalar

- [Hesaplama-1 — Ofset çıkarma ve RMS](HESAPLAMA-1.md)
- [Hesaplama-2 — Voltajdan amper](HESAPLAMA-2.md)
- [Hesaplama-3 — DC ortalama ve AC RMS ayrımı](HESAPLAMA-3.md)

## Genel formüller

050B için nominal duyarlılık (S=0.040\,V/A):
`I = (V_{OUT}-V_0)/S`

050U için nominal duyarlılık (S=0.060\,V/A):
`I = (V_{OUT}-V_0)/S`

Burada V0 gerçek sıfır akım ofsetidir; sabit olarak VCC/2 varsayılmamalıdır. Bu formül anlık/DC akım değerini temsil eder. AC RMS için önce ofset çıkarılmış örneklerin RMS'i hesaplanır.

ADC girişinde ölçülen voltaj, VIOUT voltajından farklıysa analog bölücü/kazanç tersine uygulanmalıdır. Nominal hassasiyet ilk tahmindir; kalibrasyon yerine geçmez.
