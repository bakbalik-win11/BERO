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
