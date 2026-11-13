# Oturum kaydı — 2026-11-13 — E19 düşük akım çalışma sınırı

## HEDEF
E19'un mevcut aşamasının amacını netleştirmek: katsayı kalibrasyonu değil, ADS1115 + SCT ölçüm zincirinin mevcut ayar/katsayıyla düşük akımdaki çalışma davranışını ve gözlenen alt çalışma sınırını belirlemek.

## YAPILAN İŞ
- E19 README, protocol ve results dosyalarına deney amacı/sıra düzeltmesi eklendi.
- STATUS.md güncellendi.
- 57 W test kaydına kullanıcı bildirimi ve yorum sınırları eklendi.
- Eski SCT + ESP32 dahili ADC yolunun 100 W'ta kısa kalibre edilmiş olmasına rağmen düşük akımda kararlı/hassas sonuç vermediği bilgisi tarihsel karşılaştırma olarak kaydedildi.
- Katsayı belirleme/kalibrasyonun çalışma sınırı deneyi bittikten sonra ayrı aşama olacağı belirtildi.

## LOG / ÖN GÖZLEM
- 57 W sabit yük: PZEM 0,265 A; ADS1115 + SCT 0,270 A (KULLANICI BİLDİRİMİ).
- Kullanılan katsayı kaba/başlangıç katsayısıdır; kalibrasyon yapılmamıştır.
- Fark +0,005 A; PZEM'e göre yaklaşık +%1,89 (HESAP).
- Ham CSV ve ortak zaman penceresi istatistikleri bu kısa bildirime eşlik etmediğinden sonuç ön gözlem düzeyindedir.

## KARAR
- Mevcut ayarlar ve katsayı yük basamakları boyunca sabit tutulacak.
- Yük kademeli olarak aşağı indirilecek.
- Her basamakta PZEM aynı zaman aralığının karşılaştırma referansı olacak.
- Kararlılık/tekrarlanabilirlik, sıçrama/okuma kaybı, dağılım ve mevcut fark raporlanacak.
- Bu aşamada katsayı ayarı yapılmayacak; kalibrasyon daha sonra ayrı iş olacak.

## DOĞRULAMA / AÇIKLAR
- Beş mevcut doküman güncellendi; bu oturum kaydı ve PROGRESS_TREE bağlantısı ayrıca eklendi.
- 57 W ortak CSV/zaman serisi analizi bekliyor.
- ADS1115 A0/A1 giriş ortak-mod/bias ve ray sınırlarının fiziksel güvenlik doğrulaması açık ön koşuldur.
- Daha düşük yük basamakları henüz yapılmadı.
- Hiçbir kalibrasyon veya ±%4 genel doğrulaması ilan edilmedi.

## SONRAKİ TEK ADIM
Güvenlik ön koşulu doğrulandıktan sonra mevcut ayar/katsayıyı değiştirmeden bir alt sabit yük basamağının ortak PZEM + ADS/SCT kaydını almak.

## 2026-11-13 — 57 W oturumu kapandı (18:40) ve CSV ön analizi

- Kullanıcı bildirimi: 57 W nominal akkor yük oturumu **18:40 (+03:00)** itibarıyla kapatıldı.
- Kaynak CSV: `history (57).csv`; SHA-256: `5945b3731a86408db84426f140c6b71869dd5e43b885514aa060e8d9a892a78b`; 5.441 satır, 3 sütun. CSV zamanları UTC'den Europe/Istanbul'a çevrilerek incelendi.
- İncelenen oturum aralığı: 18:32:00–18:40:00 (+03:00). Kullanıcı yükü 57 W nominal olarak tanımladı; CSV'deki PZEM aktif güç bu aralıkta yaklaşık 60,1–61,0 W (18:32–18:40 ortalama 60,58 W) gösteriyor. Nominal lamba etiketi ile PZEM'in ölçtüğü aktif güç birbirinden ayrıdır.
- 18:35:00–18:40:00 ortak gözlem kesiti: ADS1115 + SCT n=150, ortalama 0,266212 A, örnek SD=0,000985 A, min–maks 0,263838–0,269036 A. PZEM akım n=18, ortalama 0,264500 A, örnek SD=0,000514 A, min–maks 0,264–0,265 A. Ortalama fark +0,001712 A; PZEM'e göre yaklaşık +%0,647 (**HESAP**).
- 18:32:00–18:40:00 tam kesitinde ADS1115 n=239, ortalama 0,266547 A, SD=0,001108 A; PZEM n=23, ortalama 0,264783 A, SD=0,000795 A. Ortalama fark +0,001764 A; yaklaşık +%0,666 (**HESAP**).
- Aynı 18:35–18:40 aralığında eski ESP32D1 dahili ADC CH1-1T serisi n=300, ortalama 0,305881 A, SD=0,021954 A, min–maks 0,277557–0,439324 A. Bu seri ADS1115'ten belirgin biçimde daha geniş dağılım gösteriyor; farklı ölçüm mimarileri ayrı tutulur.
- CSV'nin son ADS1115 örneği 18:39:59.927, son PZEM akım örneği 18:39:57.857; kullanıcının 18:40'ta kapatma bildirimiyle uyumlu kayıt sonu.
- **Yorum sınırı:** 18:35–18:40 ADS1115 serisi bu oturumda dar dağılımlı/kararlı gözüküyor ve PZEM ortalamasına yakın. Bu, 100 W'ta yapılan kaba referans ayarından sonra düşük akımda çalışma davranışına ilişkin gözlemdir; bağımsız kalibrasyon, ±%4 genel doğrulaması veya alt çalışma sınırının kesin belirlenmesi değildir. Daha düşük basamaklar ve tekrarlar gerekir.
- Bu aşamanın yöntemi: her ölçüm yapısı PZEM'e karşı yaklaşık 100 W noktasında kaba kalibre edilir; ardından katsayı değiştirilmeden daha düşük akım basamaklarında davranışı tanınır. Düşük akım aşamasında amaç yeniden kalibrasyon değil, kararlılık ve kullanılabilir alt sınırı bulmaktır. Kullanıcı bu yöntemi her ölçüm yapısı için geçerli olarak netleştirdi.
- Güvenlik ön koşulu (ADS1115 A0/A1 ortak-mod/bias ve giriş ray sınırlarının fiziksel doğrulaması) ayrıca açık kalır.

## 42 W basamağı açıldı
- 18:44 (+03:00), 42 W nominal yük: kullanıcı bildirimi.
- 57 W önceki basamak 18:40'ta kapatıldı.
- Katsayı ve ayarlar sabit; hedef düşük akım çalışma davranışını gözlemek, kalibrasyon yapmak değil.
- CSV, kapanış saati ve sonuç analizi bekleniyor.
- Test kaydı: [E19 42 W](../logs/ads1115/2026-11-13-E19-42w-test.md).


## 2026-11-13 — 42 W oturumu kapandı (18:50) ve CSV analizi

- Kullanıcı bildirimi: 42 W nominal yük oturumu 18:44'te başladı ve 18:50 (+03:00) itibarıyla kapatıldı.
- Kaynak CSV: `history (58).csv`; 19.183 satır, 3 sütun; SHA-256 `df278701f3dc4a317dd70716f0e192436c82cb334d6c1a6919f4a9e4af8811be`.
- Ortak analiz penceresi: 18:44:07–18:49:59 (+03:00). ADS1115 son örneği 18:49:57.913; PZEM akım son örneği 18:49:57.867.
- ADS1115 + SCT: n=176, ortalama 0.189236 A, örnek SD=0.001014 A, min–maks 0.186221–0.192013 A, CV=%0.536.
- PZEM akım: n=9, ortalama 0.189000 A, örnek SD=0.001000 A, min–maks 0.188–0.191 A, CV=%0.529.
- Ortalama fark +0.000236 A / PZEM'e göre yaklaşık +%0.125 (HESAP); PZEM örnek sayısı düşük ve örnekleme yoğunluğu ADS1115'ten farklıdır.
- PZEM aktif güç n=31, ortalama 43.452 W, SD=0.115 W, min–maks 43.3–43.8 W.
- Modül 2 CH1-1T n=352, ortalama 0.257694 A, SD=0.030760 A, min–maks 0.200736–0.418209 A, CV=%11.937. Bu farklı ölçüm mimarisinin aynı oturumdaki betimleyici karşılaştırmasıdır.
- CSV yeniden sayımında ADS örnek sayısı 176 bulundu; önceki sohbet ön özetindeki 177 sayısı düzeltilmiştir.
- **Sonuç:** 42 W basamağında ADS1115 + SCT yolu dar dağılım ve PZEM'e yakın ortalama gösterdi. Bu, düşük akım çalışma davranışı açısından olumlu gözlemdir; kalibrasyon, bağımsız doğruluk veya ±%4 genel kabulü değildir. Katsayı/ayar değiştirilmedi.
- Fiziksel düzen kullanıcı bildirimi: aynı SCT, bias devresi yok, harici transformatör yok. ADS1115 A0/A1 ortak-mod ve GND–VDD giriş güvenliği ayrıca doğrulanmalıdır.
- Ayrıntı: [42 W test raporu](../logs/ads1115/2026-11-13-E19-42w-test.md); [E19 sonuç defteri](../experiments/E19-ads1115-low-current-alternative/results.md).


## 2026-11-13 — 18 W sabit yük gözlemi kapatıldı; aç/kapa deneyine geçiş kararı

- Kaynak CSV: `history (59).csv`; 3.798 satır, 3 sütun; SHA-256 `64de1d73afa4f716eef93793d62911b247dd18dd4d2063efd8aec077da5c9b52`.
- CSV zamanları Europe/Istanbul'a çevrildi. Ortak karşılaştırma penceresi 18:54:17.903–19:00:02.859 (+03:00); PZEM akımın son ortak örneği 19:00:02.859.
- ADS1115 + SCT n=173, ortalama 0.078715 A, örnek SD=0.000373 A, min–maks 0.077580–0.079561 A.
- PZEM akım n=18, ortalama 0.079500 A, SD=0.000514 A, min–maks 0.079–0.080 A. PZEM aktif güç n=32, ortalama 18.269 W, SD=0.074 W.
- Ortalama akım farkı ADS1115−PZEM = −0.000785 A; PZEM'e göre yaklaşık −%0.99 (HESAP). Bu oturum ±%4 beklentisinin içindedir; genel kabul/kalibrasyon değildir.
- ADS1115 entity'sinde 4 adet 0.00 A yayını bulundu. 18W ortak kararlı pencerede ADS1115 sıfır yayını yoktur. Yük öncesi sıfırdan 18W'ta yaklaşık 0.0787 A'ya geçiş kaydedildi.
- Aynı SCT sensörü kullanıldı; kullanıcı teyidiyle ADS1115 yolunda harici bias ve harici transformatör yok.
- Eski Modül 2 CH1-1T: n=346, mean 0.185460 A, SD 0.042098 A. ADS1115 dağılımı bu oturumda belirgin biçimde daha dardır.
- **Veri kararı:** 18 W sabit yük baz kaydı tamamlandı. ADS1115 + SCT zinciri BERO için umut verici ana ölçüm adayı olarak değerlendirilecek. Katsayı, gain, filtre ve zaman ayarları değiştirilmedi.
- **Sonraki iş:** aç/kapa tepki deneyi. Fiziksel yük açılıp kapanması PZEM ve SCT akım/güç davranışıyla teyit edilecek. SSR/UDP olayı tek başına fiziksel ON/OFF kanıtı değildir; CSV'de SSR OFF olaylarından sonra PZEM 18 W seviyesinde kalmıştır.
- Güvenlik: ADS1115 A0/A1 ortak-mod ve GND–VDD giriş ray sınırlarının fiziksel doğrulaması hâlâ açık.
- Rapor: [E19 18 W test raporu](../logs/ads1115/2026-11-13-E19-18w-test.md).
