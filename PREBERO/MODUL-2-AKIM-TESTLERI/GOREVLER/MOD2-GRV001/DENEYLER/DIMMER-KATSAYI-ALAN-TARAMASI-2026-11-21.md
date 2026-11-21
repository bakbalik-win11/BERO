# MOD2-GRV001 – Dimmer ile katsayı alanı taraması

**Deney tarihi:** 2026-11-21  
**Modül:** Modül 2 – ESP32D2 / ADS1115 fiziksel modül No.10 / SCT013 30A-1V  
**Karşılaştırma:** Modül 3 PZEM akım ölçümü  
**Yük:** 100 W akkor ampul  
**Yük kontrolü:** SANEC AC 220 V dimmer  
**Başlangıç firmware'i:** V1.1 – katsayı 27.59 (değiştirilmeyecek)  
**Durum:** Deney açıldı; ilk grafik gözlemi mevcut, sayısal kararlı pencere analizi bekleniyor.

## 1. Amaç

Dimmer kullanarak aynı akkor yükte akımı yüksekten düşüğe kademeli değiştirmek ve her kararlı akım aralığında PZEM ile SCT ölçümleri arasındaki sapmayı belirlemek.

Bu deneyin ilk amacı yeni katsayı belirlemek değildir. Önce mevcut V1.1 katsayısı 27.59 ile sapmanın hangi akım bölgelerinde kabul edilebilir kaldığı, hangi bölgelerde sistematik düşük/yüksek okuma oluştuğu haritalanacaktır.

## 2. Deney kapsamı ve ayrım

Dimmer faz kesmeli AC dalga biçimi oluşturur. Bu nedenle dimmerli sonuçlar saf şebeke sinüsüyle alınan V1.0/V1.1 kalibrasyon pencereleriyle aynı veri grubu sayılmayacaktır.

- Dimmerli ölçümler ayrı deney olarak tutulur.
- V1.1 YAML ve 27.59 katsayısı değiştirilmez.
- Bu deneyin sonuçları tek başına genel/nihai kalibrasyon kanıtı değildir.
- PZEM karşılaştırma referansıdır; kusursuz gerçek değer (ground truth) kabul edilmez.
- Yalnızca kararlı pencereler analiz edilir; potansiyel hareketi ve yük geçişleri pencere dışında bırakılır.

## 3. Donanım ve bağlantı bağlamı

- Yük: 100 W akkor ampul.
- Akım sensörü: SCT013 30A/1V.
- ADC: ADS1115 No.10, A0-A1 diferansiyel okuma.
- Ölçüm kartı: ESP32D2 / Modül 2.
- Karşılaştırma ölçümü: Modül 3 PZEM.
- Dimmer: SANEC AC 220 V, potansiyel kontrollü AC dimmer.

**Güvenlik notu:** Dimmerin klemens işlevleri ve koruyucu toprak düzeni yalnızca fotoğraf veya süreklilik sesiyle kesinleşmiş değildir. Bu deney kaydı, belirsiz klemenslere bağlantı talimatı değildir. Şebeke bağlantısı yalnızca bağlantı düzeni yetkin kişi tarafından doğrulanmış, kapalı ve dokunmaya karşı korumalı düzenekte yapılmalıdır.

## 4. Ölçüm yöntemi

1. V1.1 firmware'i ve 27.59 katsayısı sabit tutulur.
2. 100 W akkor ampul dimmer üzerinden çalıştırılır.
3. Dimmer ayarı yüksek akımdan düşük akıma doğru kademeli değiştirilir.
4. Her ayar değişikliğinden sonra ölçümlerin kararlı hale gelmesi beklenir.
5. Her kararlı noktada tercihen 30–60 saniye veri alınır.
6. Her pencerede PZEM için en az 5–6 geçerli örnek hedeflenir. Yetersiz örnekli pencere düşük güvenli olarak işaretlenir.
7. Mümkünse her akım bölgesi üç kez tekrarlanır.
8. Pencere ortalamaları aynı zaman aralığından ayrı ayrı hesaplanır; PZEM ve SCT örnek sayıları ayrıca raporlanır.

Akım kademeleri yük gücüne veya dimmer potansiyelinin açısına göre değil, ölçülen PZEM akımına göre adlandırılır.

## 5. İlk tarama hedefleri

Önce yüksekten düşüğe tarama yapılır. Hedefler yaklaşık PZEM akım aralıklarıdır; dimmer ayarının bu değerleri tam tutturması beklenmez.

| Sıra | PZEM hedef akım aralığı | Amaç |
|---:|---:|---|
| 1 | 0.80–1.00 A | Düşük bölgeye yaklaşım |
| 2 | 0.60–0.70 A | V1.1'de şüpheli alt sınır çevresi |
| 3 | 0.40–0.50 A | Düşük akım sapması |
| 4 | 0.25–0.30 A | Düşük akım sapması |
| 5 | 0.15–0.20 A | Alt ölçüm bölgesi |

İlk taramada bu aralıklar elde edilemezse gerçekleşen PZEM akımı kaydedilir; hedefe ulaşıldığı varsayılmaz. Daha yüksek akım noktaları, dimmer ve 100 W ampulün gerçek çalışma aralığı izin verirse ayrıca eklenebilir.

## 6. Hesaplamalar

Her kararlı pencere için:

- PZEM_ortalama_A
- SCT_ortalama_A
- PZEM_ornek_sayisi
- SCT_ornek_sayisi
- PZEM_std_A
- SCT_std_A
- Sapma_yuzde
- K_gerekli

Sapma:

Sapma (%) = ((SCT ortalama - PZEM ortalama) / PZEM ortalama) × 100

Pozitif değer SCT'nin PZEM'den yüksek, negatif değer düşük okuduğunu gösterir.

V1.1'deki 27.59 katsayısı altında pencereye karşılık gelen katsayı:

K_gerekli = 27.59 × (PZEM ortalama / SCT ortalama)

Bu hesaplanan katsayı yalnızca pencere bazlı analiz değeridir; firmware'e otomatik uygulanmayacaktır.

## 7. İlk grafik gözlemi – henüz sayısal sonuç değil

2026-11-21 tarihinde paylaşılan ilk grafikte:
- SCT çizgisi yük devreye girince yaklaşık 0.34 A seviyesine çıkmıştır.
- PZEM çizgisi ilk aşamada yaklaşık 0.20 A göstermiş, sonraki seviyede yaklaşık 0.43 A'ya yükselmiştir.
- Dimmer kapatıldığında SCT ölçümü sıfıra dönmüştür; PZEM de daha sonra sıfıra inmiştir.

Grafikten kesin ortalama, kararlı pencere veya sapma yüzdesi çıkarılmamıştır. CSV verisi ve zaman eşleştirmesi beklenmektedir.

## 8. Sonuçlandırma ölçütü

Deney tamamlandığında akım aralıkları aşağıdaki sınıflardan biriyle değerlendirilecektir:

- **27.59 destekleniyor:** Tekrarlı kararlı pencerelerde sapma kabul sınırı içinde.
- **27.59 düşük okuyor:** Tekrarlı pencerelerde SCT/PZEM sapması negatif ve sistematik.
- **27.59 yüksek okuyor:** Tekrarlı pencerelerde sapma pozitif ve sistematik.
- **Belirsiz:** PZEM örnek sayısı, kararlılık veya tekrar sayısı yetersiz.

Katsayı alanları ancak birden fazla kararlı pencere ve tekrar ile desteklenirse tanımlanacaktır. Bu deney tamamlanmadan yeni katsayı veya katsayı geçiş sınırı ilan edilmeyecektir.

## 9. Kayıt dosyaları

- Ham Home Assistant history CSV: deney tamamlandığında kaynak dosya olarak eklenecek.
- Kararlı pencere özeti: LOG/DIMMER-KARARLI-PENCERE-OZETI-2026-11-21.csv
- Sonuç raporu: RAPOR/DIMMER-KATSAYI-ALANLARI-2026-11-21.md

**Açılış kararı:** Deney protokolü oluşturuldu. İlk grafik gözlemi not edildi. Henüz sayısal sapma analizi yapılmadı ve deney tamamlanmadı.
