# FNIRSI 2D15P – Bağımsız Osiloskop Öğrenme

- Başlangıç tarihi: 2026-11-22
- Çalışma biçimi: Geceleri yaklaşık 20 dakika
- Durum: Öğrenme alanı açıldı; ilk ders henüz uygulanmadı.
- Kapsam: BERO teknik testlerinden ve veri analizi öğreniminden ayrı, cihaz kullanım eğitimi.

## Amaç

FNIRSI 2D15P osiloskopu sıfırdan öğrenmek. İlk aşamada cihazın kendi sinyal jeneratörünü kullanarak dalga biçimini ekranda göstermek; VOLTS/DIV, TIME/DIV, TRIGGER ve SINGLE ayarlarını anlamak; ardından dalganın temel büyüklüklerini teker teker okumayı öğrenmek.

Her derste tek bir kavram ele alınacak. Kavram önce günlük bir dille açıklanacak, sonra FNIRSI ekranında gösterilecek ve kullanıcıya ekrandan ölçtürülecek. RMS gibi kavramlar yalnızca formül ezberletilerek değil, sinyalin şekliyle ilişkilendirilerek anlatılacak.

Bu çalışma ticari ölçüm cihazı geliştirme veya laboratuvar kalibrasyonu değildir. Amaç cihazı temel düzeyde güvenli ve bilinçli kullanabilmektir.

## Kullanılacak ekipman

| Ekipman | Rol |
|---|---|
| FNIRSI 2D15P | Osiloskop ve ilk aşamada dahili sinyal jeneratörü |
| Cihazla gelen prob | CH1 üzerinden sinyal görüntüleme |
| SANEC NE555 kare dalga jeneratörü | İlerleyen derslerde harici kaynak olarak karşılaştırma |

İlk derslerde yalnızca FNIRSI'nin kendi jeneratörü kullanılacak. NE555 sonraya bırakıldı.

## Cihaz için başlangıç bilgileri

FNIRSI 2D15P üretici sayfasında listelenen başlıca özellikler:
- İki kanallı osiloskop.
- Tek kanal kullanımında 100 MHz bant genişliği.
- 500 MSa/s örnekleme hızı.
- Dikey ölçek: 10 mV/div – 10 V/div.
- Zaman tabanı: 5 ns/div – 50 s/div.
- Dahili DDS jeneratörü: 0–10 MHz.
- Jeneratör genliği: 0,1–3,0 Vpp.
- Duty cycle ayarı.

Üretici sayfası: https://www.fnirsi.com/products/2d15p

10 mV/div, en hassas dikey ölçek kademesidir; ölçülebilecek en küçük sinyalin mutlak alt sınırı değildir. Prob fiziksel olarak x1/x10 konumuna sahipse cihaz menüsündeki prob oranı da aynı seçilmelidir.

## 20 dakikalık oturum yöntemi

| Süre | İçerik |
|---:|---|
| 0–3 dk | Önceki dersin tekrarı ve bağlantı kontrolü |
| 3–8 dk | Tek yeni kavram veya ayar |
| 8–15 dk | Dahili jeneratörle uygulama |
| 15–18 dk | Ekrandaki sinyali okuma |
| 18–20 dk | Fotoğraf ve oturum notu |

Bir konu anlaşılmadan yenisine geçilmez. Gerekirse aynı ders tekrarlanır. Bir akşamda birden fazla yeni terim yüklenmez.

## Dalga üzerinde teker teker öğrenilecek kavramlar

| Sıra | Kavram | Öğreneceğimiz şey |
|---:|---|---|
| 1 | Dalga biçimi ve eksenler | Yatay eksen zaman, dikey eksen gerilimdir |
| 2 | Sıfır çizgisi ve DC offset | Dalganın referans seviyesi ve sıfırdan kayması |
| 3 | Tepe değer (Vp) | Dalganın merkezden en yüksek uzaklığı |
| 4 | Tepe-tepe (Vpp) | En üst ve en alt noktalar arasındaki fark |
| 5 | Periyot (T) | Bir tam tekrarın süresi |
| 6 | Frekans (f) | Saniyedeki tekrar sayısı; periyotla ilişkisi |
| 7 | Ortalama değer (Vavg) | Dalganın bir periyottaki ortalaması |
| 8 | RMS (Vrms) | Aynı dirençte eşdeğer ısı etkisi oluşturan etkin gerilim |
| 9 | Duty cycle | Kare dalgada yüksek seviyede geçen zamanın oranı |
| 10 | Faz farkı | İki periyodik sinyalin zaman bakımından kayması |
| 11 | Gürültü | İstenen dalganın üzerine binen istenmeyen değişimler |
| 12 | Harmonik ve dalga şekli bozulması | Sinüs dışı şeklin frekans bileşenleri |
| 13 | Örnekleme ve sample rate | Sürekli dalgadan sayısal örneklerin alınması |
| 14 | Trigger ve Single | Görüntüyü aynı olaydan başlatmak ve tek kare yakalamak |
| 15 | Prob x1/x10, AC/DC coupling | Ölçüm bağlantısı ve girişin gösterdiği bileşen |
| 16 | Otomatik ölçüm ve cursor | Cihazın hesapladığı değerleri okumak ve elle ölçmek |
| 17 | İki kanal | İki sinyali aynı zaman ekseninde karşılaştırmak |

RMS anlatımında sinyal türü mutlaka dikkate alınacak. Sinüs, simetrik kare ve farklı duty cycle değerleri aynı RMS ilişkisine sahip değildir; her örneğin hesabı kendi dalga şekli üzerinden yapılacaktır.

## Ders sırası

1. Ekran, eksenler, dalga biçimi ve sıfır seviyesi.
2. Dahili jeneratörle 1 kHz kare dalga.
3. VOLTS/DIV ve sinyal genliği.
4. TIME/DIV, periyot ve frekans.
5. TRIGGER ve SINGLE: canlı görüntü ile tek yakalama farkı.
6. Vp ve Vpp.
7. Ortalama değer ve DC offset.
8. RMS (Vrms).
9. Kare, sinüs ve üçgen dalga karşılaştırması.
10. Duty cycle.
11. Faz farkı ve iki kanal.
12. Gürültü ve dalga biçimi kararlılığı.
13. Örnekleme, sample rate ve aliasing.
14. Prob x1/x10, AC/DC coupling.
15. Otomatik ölçümler ve cursor.
16. SANEC NE555 harici jeneratörü.
17. İsteğe bağlı SCT013 gözlemi (eğitim uygulaması; BERO görevi değildir).

## Gelecek kişisel çalışma: ESP tabanlı dalga verisi toplayıcı

FNIRSI ekran görüntüsü, ekrandaki dalganın görsel kaydıdır; kullanıcının şu anki kullanımında sayısal örnekleri doğrudan PC'ye aktaran bir veri çıkışı bulunmamaktadır. Gelecekte ESP tabanlı, düşük frekanslı sinyalleri örnekleyip sayısal veriyi bilgisayara gönderen basit bir dalga verisi toplayıcı geliştirmek istiyoruz.

İlk hedef, FNIRSI'nin yerini alan profesyonel bir osiloskop yapmak değildir. Hedef:
- Analog sinyalden zaman sıralı sayısal örnekler toplamak.
- Örnekleme aralığını veya zaman bilgisini kaydetmek.
- Veriyi USB seri veya uygun başka bir yerel aktarım yöntemiyle PC'ye göndermek.
- Bilgisayarda dalga grafiği çizmek.
- CSV olarak saklamak ve daha sonra Python ile analiz etmek.
- İleride RMS, tepe, Vpp, periyot, frekans ve gürültü ölçümlerini bu veriden hesaplamak.

Olası veri zinciri:
1. Güvenli analog giriş ve sinyal koşullandırma (bias, kazanç, giriş koruması, uygun filtre).
2. ESP32 ve uygun ADC ile örnekleme.
3. Örneklerin zaman bilgisiyle RAM tamponunda tutulması.
4. USB seri veya yerel ağ üzerinden PC'ye aktarım.
5. Python ile grafik ve CSV üretimi.

ADC seçimi ve örnekleme hızı henüz belirlenmedi. Önce osiloskopta örnekleme, frekans, RMS ve dalga şekli kavramlarını öğreneceğiz; sonra hedef sinyal frekansı ve gerekli dalga biçimi ayrıntısına göre ESP32'nin dahili ADC'si mi yoksa harici ADC mi kullanılacağına karar vereceğiz. Bu çalışma BERO ana ölçüm zincirinden ve PREBERO görevlerinden bağımsız bir öğrenme/kişisel elektronik projesi olarak kalacaktır.

Ayrıntılı fikir notu: `IDE-001-ESP32-DALGA-VERI-TOPLAYICI.md`

## Güvenlik sınırı

İlk dersler yalnızca osiloskopun kendi düşük gerilimli jeneratörüyle yapılacaktır. İlk bağlantıdan önce prob tipi, jeneratör çıkışı ve cihaz üzerindeki soketler birlikte kontrol edilecektir.

Osiloskopun pilde çalışması, şebeke ölçümünde girişlerinin güvenli veya izole olduğu anlamına gelmez. Prob GND klipsi şebeke fazına, nötrüne veya şebekeye bağlı devreye bağlanmayacaktır. Bu eğitimde şebeke ölçümü yapılmayacaktır. İleride ESP veri toplayıcı için de şebeke sinyali doğrudan ESP/ADC girişine bağlanmayacaktır; uygun izolasyon ve analog ön uç olmadan böyle bir deney yapılmaz.

## Kayıtlar

- İlk ders: `DERS-001-ILK-KARE-DALGA.md`
- Her gece için: `OTURUM-LOG.md`
- Gelecek ESP dalga verisi toplayıcı fikri: `IDE-001-ESP32-DALGA-VERI-TOPLAYICI.md`

Yapılmamış ders tamamlandı olarak işaretlenmez. Fotoğraf/log, ancak gerçekten uygulandıktan sonra kaydedilir.

## BERO'dan ayrım

Bu klasör bağımsız öğrenme içindir. BERO'nun PREBERO görevlerini, kalibrasyon kararlarını veya firmware'ini değiştirmez. Öğrenme sırasında elde edilen bir gözlem BERO için teknik kanıt niteliğindeyse ayrıca ilgili BERO görevinin altında kaydedilir.
