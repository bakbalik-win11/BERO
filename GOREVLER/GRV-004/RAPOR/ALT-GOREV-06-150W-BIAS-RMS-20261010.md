# GRV-004 — ALT GÖREV 06: 150 W Yük ve Bias Referanslı Akım Hesabı
Tarih: 2026-10-10
Cihaz: esp32d1 @ 192.168.0.8
Kaynak log: esp32d1-logs (13).txt
Durum: 150 W nominal yük testi loglandı; sıradaki çalışma bias referanslı RMS akım hesabı.

## 1. Deney sonucu
TUR=38–51 arasında PZEM yaklaşık 147.2–148.9 W, 226.9–228.6 V ve 0.650–0.653 A gösteriyor. TUR=52'de değerler 1.7 W / 0.028 A seviyesine dönüyor. Böylece yükün devrede olduğu pencere ve yük kaldırıldıktan sonraki durum logda görülüyor.

## 2. Yük altındaki gözlem
- BIAS STD yaklaşık 0.0240–0.0258 V.
- K1 STD yaklaşık 0.0471–0.0493 V.
- K2 STD yaklaşık 0.0717–0.0731 V.
- K3 STD yaklaşık 0.0044–0.0080 V.
- Kanal ortalamaları yük sırasında da yaklaşık 1.66 V civarında kalıyor. AVG tek başına akım hesabı için uygun değil; yük etkisi özellikle K1/K2 STD alanlarında belirgin.

## 3. Sonraki adım: bias'ı her örnekten çıkar
Mevcut log yalnızca istatistikleri içeriyor, ham eşzamanlı örnek çiftlerini içermiyor. Bu nedenle bias çıkarılmış RMS geçmiş logdan doğru biçimde yeniden hesaplanamaz.

Yeni ve ayrı kod sürümünde:
1. Her örnekleme anında BIAS ile SCT kanal örneği eşleştirilecek.
2. Her örnek için x_ac = x_sct - bias hesaplanacak.
3. Bu farkların RMS değeri sqrt(mean(x_ac * x_ac)) olarak hesaplanacak.
4. Kanal başına örnek sayısı ve pencere süresi loglanacak.
5. Aynı yöntem yüksüz ve 150 W koşullarında çalıştırılacak; PZEM akımı referans alınarak dönüşüm katsayısı daha sonra değerlendirilecek.

BIAS kanalının STD değerini SCT kanalının STD değerinden doğrudan çıkarmayacağız. Örnek bazında bias çıkarımı, eşzamanlı ölçüm gerektirir.

## 4. Kayıt disiplini
Mevcut YAML ve mevcut log korunacak. Bias çıkarma + RMS hesabı yeni tarihli YAML ve ayrı rapor olacak. Önce derleme kontrolü, ardından donanım testi yapılacak.

## Sonuç
150 W nominal yük testinde PZEM yaklaşık 148 W ve 0.65 A gösteriyor. Bir sonraki teknik hedef, bias'ı örnek bazında çıkarıp AC bileşenin RMS değerini hesaplamak.
