# ACS712 20A — akım hesaplama

- [Hesaplama-1 — raw → volt → amper](HESAPLAMA-1.md)
- [Hesaplama-2 — DC akım ve ofset](HESAPLAMA-2.md)
- [Hesaplama-3 — AC RMS ve kalibrasyon](HESAPLAMA-3.md)

Model: ±20 A; tipik hassasiyet **0.100 V/A**.

1. Gerçek sıfır akım V0'ı ölç.
2. ADC VREF ve giriş bölücü/kazanç oranını belirle.
3. Raw örnekleri ADC voltajına, ardından gerçek VIOUT'a dönüştür.
4. DC için ortalama akımı, AC için ofseti çıkarılmış RMS'i hesapla.
5. Referans ampermetreyle çok noktalı kalibrasyon yap.

Ratiometrik çıkış VCC ile değişir; 5 V besleme ile ADC VREF farklıysa drift'i hesaba kat. ADC kırpılması, gürültü, filtre ve düzensiz örnekleme ölçümü etkiler.
