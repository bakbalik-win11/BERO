# DERS 001 – FNIRSI Dahili Jeneratörüyle İlk Kare Dalga

- Durum: Hazır; henüz uygulanmadı.
- Süre: Yaklaşık 20 dakika.
- Amaç: Ekranda kararlı bir kare dalga oluşturmak; dikey ölçek, zaman ölçeği ve trigger kavramlarını ilk kez görmek.

## 1. İlk dersin sınırı

Bu derste yalnızca FNIRSI 2D15P'nin kendi jeneratörü ve CH1 kullanılacak. Harici NE555, SCT013 ve şebeke bağlantısı kullanılmayacak. Ayar isimlerinin cihaz yazılımındaki karşılıkları farklıysa ekrandaki menüye göre birlikte netleştirilecek.

## 2. Başlangıç sinyali

| Parametre | Başlangıç değeri |
|---|---:|
| Waveform | Square |
| Frequency | 1 kHz |
| Amplitude | 1,0 Vpp |
| Duty cycle | %50 |
| Offset | 0 V (menü sunuyorsa) |

FNIRSI'nin kendi jeneratör çıkışı, cihaz üzerindeki GEN/OUTPUT soketinden CH1 girişine üreticinin uygun kablosu/bağlantısı ile verilecek. Bağlantı tipini uygulama öncesi cihazın fotoğrafından kontrol edeceğiz; soket ve kablo uçları tahmin edilmeyecek.

## 3. Osiloskop başlangıç ayarları

| Ayar | Başlangıç değeri |
|---|---:|
| Kanal | CH1 |
| Coupling | DC |
| Prob oranı | Fiziksel prob ayarıyla aynı (ilk aşamada x1, eğer prob bunu destekliyorsa) |
| VOLTS/DIV | 200 mV/div |
| TIME/DIV | 200 µs/div |
| Trigger | Auto |
| Trigger edge | Rising |
| Trigger source | CH1 |

Bu ayarlar 1 Vpp sinyali ekranda yaklaşık 5 dikey bölüme ve 1 kHz sinyalin 1 ms periyodunu yatayda yaklaşık 5 bölüme yerleştirmeyi hedefler. Ekran görünümüne göre küçük ayar yapılabilir.

## 4. Bağlantı ve güvenlik

1. Jeneratör çıkışı kapalıyken kabloyu bağla.
2. CH1 prob ucu sinyal çıkışına; prob GND klipsi yalnızca aynı jeneratörün GND/COM noktasına bağlanır. Cihazın kendi kablo düzeni ortak GND bağlantısını farklı biçimde sağlıyorsa önce cihaz ekranı ve kablosunu inceleyeceğiz.
3. Sinyal kaynağı yalnızca FNIRSI'nin kendi dahili jeneratörüdür.
4. Şebeke prizine, canlı faz/nötr hattına veya şebekeye bağlı herhangi bir devreye bağlantı yapılmaz.
5. Bağlantı belirsizse jeneratör açılmaz; önce fotoğraf üzerinden birlikte kontrol edilir.

## 5. Bu derste öğrenilecek üç ayar

- VOLTS/DIV: Dikey eksende her karenin kaç volt temsil ettiğini belirler. Dalga yüksekliğini ekranda büyütüp küçültür.
- TIME/DIV: Yatay eksende her karenin kaç saniye temsil ettiğini belirler. Periyodun ekranda ne kadar yer kapladığını değiştirir.
- TRIGGER: Dalganın ekranda kaymasını azaltıp sabit görünmesini sağlar. İlk derste Auto ve Rising yeterlidir.

## 6. Ders sonunda cevaplanacak sorular

1. Kare dalganın yüksekliği ekranda kaç dikey bölme?
2. Bir tam periyot yatayda kaç bölme?
3. Ekranda dalga sabit mi, kayıyor mu?
4. VOLTS/DIV bir kademe değiştirilince ne değişti?
5. TIME/DIV bir kademe değiştirilince ne değişti?

İlk derste sayısal sonuçları ezberlemek zorunlu değil. Önce ekrandaki şekli ve düğmelerin etkisini tanımak hedeflenir.

## 7. Kapanış kaydı

Ders ancak uygulama yapılıp ekran fotoğrafı/ölçüm notu alındıktan sonra "tamamlandı" olarak işaretlenir. Uygulama öncesi durum: **HAZIR**.
