# Hesaplama-3 — Kalibrasyon ve örnekleme

## Kalibrasyon planı
1. Akım yokken ADC raw ve bias dağılımını kaydet.
2. Düşük, bilinen AC akımda dalga biçiminin kırpılmadığını kontrol et.
3. Referans True-RMS ampermetre ile birkaç akım noktasında ölçüm al.
4. ADC VREF, burden değeri, analog kazanç ve RMS penceresini kaydet.
5. Hesaplanan akımla referansı karşılaştır; düzeltme katsayısını ölçüm verisinden çıkar.
6. Tek noktadaki kalibrasyonu tüm aralık için doğruluk kanıtı sayma.

## Örnek sayısı ve süre
N=1000, pencerede 1000 örnek demektir; 1000 örnek/saniye demek değildir. 1 ms aralık yaklaşık 1 saniye, 100 µs aralık yaklaşık 100 ms sürer. 50 Hz'de periyot 20 ms'dir; pencerenin kaç periyot kapsadığını gerçek zaman damgalarıyla hesapla.

Düzensiz örnekleme, aliasing, ADC kırpılması ve analog filtre RMS sonucunu etkiler.

## Çıplak CT ve modül ayrımı
Bu hesaplar çıplak ZMCT103C + bilinen burden için geçerlidir. OP07 op-amp/potansiyometre içeren modülün OUT pininde aynı gerilim-akım oranı garanti değildir. Modül çıkışını referans akımla kalibre et.