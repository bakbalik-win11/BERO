# ZMPT101B – AC Gerilim Algılama

## Amaç
BERO kapsamında şebeke geriliminin anlık dalga şeklini güvenli bir ölçüm zinciri üzerinden örneklemek; SCT013 akım dalga şekliyle zaman hizalı veriler elde ederek aktif güç (P), görünür güç (S) ve gerçek güç faktörü (PF) araştırmasına veri sağlamak.

Bu donanım kaydı bir imalat/onay belgesi değildir. Önce sensör, analog ön uç, ADC ve zamanlama deneyleri doğrulanacaktır.

## Parça kimliği
- Model: ZMPT101B
- Üretici: Qingxian Zeming Langxi Electronic Devices Co., Ltd. (ZEMING)
- Tip: Akım çıkışlı minyatür gerilim ölçü trafosu
- Sarım oranı: 1000:1000 (1:1)
- Nominal primer akımı: 2 mA
- Nominal sekonder akımı: 2 mA
- Üretici sayfasında belirtilen faz açısı hatası: 100 Ω örnekleme direnci ve 2 mA giriş koşulunda ≤20 yay-dakika
- Doğrusallık: ≤0,2% (belirtilen çalışma aralığında)
- İzolasyon gerilimi: 4000 V (üretici veri sayfası değeri; tamamlanmış devrenin güvenlik onayı değildir)
- Çalışma sıcaklığı: -40 °C … +60 °C

## Üretici belgeleri
- [Üretici ürün sayfası](https://www.micro-transformer.com/2ma-2ma-voltage-transformer-ZMPT101B.html)
- [Üretici PDF veri sayfası](https://makerselectronics.com/wp-content/uploads/2020/11/ZMPT101B-specification.pdf)

## Bağlantı ve analog ön uç – henüz tasarım kararı değil
ZMPT101B çıplak transformatör elemanıdır. Primerde akım sınırlama direnci, sekonderde uygun örnekleme direnci ve ADC girişine uygun analog koşullandırma gerekir. Yaygın potansiyometreli ZMPT101B modülü ile çıplak transformatör aynı donanım değildir; kart üzerindeki op-amp ve ayar devresi ayrıca değerlendirilmelidir.

ESP32/ADC girişine uygulanacak sinyal, ADC'nin izin verilen aralığında kalmalı ve negatif gerilim içermemelidir. Bunun için uygun AC kuplaj/bias ve gerekiyorsa koruma/filtreleme tasarlanmalıdır. Direnç değerleri, şebeke gerilimi ve kullanılacak tam devre doğrulanmadan bağlantı yapılmayacaktır.

## BERO'daki kullanım yaklaşımı
- SCT013 akım dalga şekli ile ZMPT101B gerilim dalga şekli aynı zaman tabanında örneklenmelidir.
- Her örnek için eşleşmiş v[n] ve i[n] değerleri kullanılmalıdır.
- P = mean(v[n] × i[n])
- Vrms = sqrt(mean(v[n]²))
- Irms = sqrt(mean(i[n]²))
- S = Vrms × Irms
- Gerçek PF = P / S

Sinüzoidal olmayan yüklerde yalnızca faz açısı üzerinden cos(phi) hesaplamak gerçek PF değildir. Gerçek PF, aktif gücün görünür güce oranıdır ve dalga şekli bozulmasını da kapsar.

## Önemli ölçüm kısıtı
ADS1115'in 860 SPS azami dönüşüm hızı iki kanala bölündüğünde kanal başına yaklaşık 430 örnek/saniye düzeyine iner; 50 Hz için bu yaklaşık 8,6 örnek/döngüdür. Ayrıca ADS1115 kanalları eşzamanlı örneklemez. Bu nedenle ADS1115, faz ve gerçek PF ölçümü için ilk tercih olarak kabul edilmeyecektir. Daha hızlı ve zaman hizalı iki kanal örneklemesi sağlayan ADC/örnekleme mimarisi araştırılacaktır.

## Güvenlik
Bu eleman şebeke gerilimi ölçümünde kullanılacaktır. Primer tarafında ölümcül gerilim bulunabilir. Açık breadboard üzerinde şebeke bağlantısı yapılmayacaktır. Uygun izolasyon mesafeleri, muhafaza, sigorta/akım sınırlama, terminal koruması ve ölçüm ekipmanı güvenliği tasarımın zorunlu parçalarıdır. 4000 V izolasyon değeri tek başına kurulmuş devrenin güvenli olduğunu göstermez.

## Durum
- Veri sayfası bulundu.
- Donanım klasörü açıldı.
- Elektriksel bağlantı ve ADC seçimi: araştırma aşamasında.
- PF ölçümü: henüz uygulanmadı ve doğrulanmadı.
