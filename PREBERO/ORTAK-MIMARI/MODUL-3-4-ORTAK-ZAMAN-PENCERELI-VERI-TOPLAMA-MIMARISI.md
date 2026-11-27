# Modül 3 ve 4 – Ortak zaman pencereli çoklu sensör veri toplama mimarisi

- **Karar tarihi:** 2026-11-22
- **Durum:** TASLAK MİMARİ KARAR / İMALAT ÖNCESİ TASARIM
- **Kapsam:** PREBERO Modül 3 (çamaşır makinesi), Modül 4 (bulaşık makinesi) ve Modül 2 ile araştırma veri alışverişi

## 1. Amaç

Akım, ses, titreşim ve deneyle doğrulanırsa gerilim/PF gibi farklı fiziksel büyüklükleri, sensörlerin kendi uygun örnekleme hızlarını koruyarak ortak bir zaman ekseninde karşılaştırılabilir hale getirmek. Modül 3 ve Modül 4'te mümkün olduğunca aynı veri şeması ve zamanlama yaklaşımı kullanılacaktır.

**Önemli sıra kararı:** Mimari fikirler, sensör seçimi, örnekleme gereksinimleri, bağlantılar, işlem yükü ve veri şeması yeterince netleşmeden donanım imalatına geçilmeyecektir. Bu belge tek başına imalat izni değildir.

## 2. Çalışma sırası – geçici deney düzeneği ve sonradan modülleşme

Kullanıcı kararı (2026-11-22): Modül 3 Step 1 akım okuma tamamlandı. Step 2'de ses ve titreşim verileri, çamaşır makinesinin yanına yerleştirilecek **ayrı/geçici bir ESP** ile toplanacaktır. Bu aşamada ses ve titreşim donanımı nihai Modül 3 kartına entegre edilmeyecek; Modül 3 fiziksel olarak imal edilmeyecektir.

- Geçici ESP, ses ve titreşim ölçümlerini kendi örnekleme gereksinimlerine göre alacaktır.
- Veriler, PZEM uygulamasında kullanılan yayın yaklaşımına benzer biçimde dışarı aktarılacaktır.
- Her yayın/kayıt zaman bilgisi ve ortak zaman dilimi/slice numarası taşıyacaktır. Alan adları ve zaman diliminin kesin tanımı deney tasarımında belirlenecektir.
- Akım ölçümünden gelen kayıtlarla ses/titreşim kayıtları zaman damgası ve dilim numarası üzerinden eşleştirilecektir.
- Deneylerle örnekleme, yayın sürekliliği, zaman hizası ve özelliklerin makine davranışını ayırt etme yeterliliği gözlemlenecektir.
- Ses/titreşim ve akım tarafı deneylerle kararlı ve birleştirilebilir hale geldiğinde, doğrulanmış donanım/yazılım tek Modül 3 yapısında toplanacaktır. Modül 4 için de ortak mimari ilkeleri korunacak; cihaz özelindeki doğrulamalar ayrıca yapılacaktır.

Bu nedenle Step 2'nin çıktısı nihai modül değil, **bağımsız ses/titreşim veri toplama ve yayın deney düzeneği** olacaktır.

## 3. Önerilen mimari

Her sensör kendi fiziksel ölçüm ihtiyacına uygun hızda örnekleme yapar. Sensörlerin ham örnekleme hızlarının aynı olması zorunlu değildir. Her sensör, ortak 1 saniyelik zaman penceresine ait özellikleri/özetleri üretir. Pencere kimliği ve zaman damgası ortak zaman tabanından alınır.

- **Akım – SCT013:** Modül 2'den devralınan SCT013 + ADS1115 + ESP32D2 ve V1.6 ölçüm yolu başlangıç referansıdır. Mevcut ct_clamp yaklaşımındaki 200 ms RMS penceresi korunacak; ilgili 1 saniyelik slota ait akım özeti üretilecektir. V1.6 kalibrasyonu bu mimari not nedeniyle değişmez.
- **Ses – MAX4466 (öneri):** Analog ses örneklemesi kendi uygun örnekleme hızıyla yapılır. DC orta nokta/bias bileşeni ayrıldıktan sonra pencere bazında ses RMS ve peak; uygun görülürse ZCR hesaplanabilir. MAX4466 kalibreli dB ölçer olarak kabul edilmeyecek; ilk hedef göreceli akustik özellikleri kaydetmektir.
- **Titreşim – MPU6050 (öneri):** Sensör kendi ODR/örnekleme hızında üç eksenli ivme verisi sağlar. Yerçekimi/statik bileşeni uygun filtreyle ayırma yaklaşımı tasarımda belirlenecek. Pencere bazında eksen RMS/peak özellikleri değerlendirilebilir. Sadece vektör büyüklüğünden sabit 1 g çıkarmanın her durumda yeterli olduğu varsayılmayacaktır.

## 4. Zaman senkronizasyonu

- Tek bir ortak monoton zaman tabanı ve 1 saniyelik slot kimliği (ör. `tick_id` / `epoch_s`) kullanılacaktır.
- Sensörlerin örnekleme döngüleri birbirini bloke etmeyecek; her biri kendi hızında çalışacaktır.
- Slot sınırında, her sensörün aynı zaman aralığına ait özeti birleştirilerek tek kayıt oluşturulacaktır.
- Zaman damgası üretimi, slot sınırları, sensör gecikmeleri, eksik pencere davranışı ve yeniden başlatma sonrası zaman eşlemesi tasarım aşamasında tanımlanacaktır.
- Ortak slot kullanımı tek başına donanım seviyesinde eşzamanlı örnekleme veya sıfır zaman kayması garantisi vermez. Gerekirse gecikme ve hizalama ölçülüp raporlanacaktır.

## 5. Önerilen veri şeması

İlk taslak alanlar:

`timestamp, tick_id, current_rms_a, sound_rms, sound_peak, sound_zcr, vib_x_rms, vib_y_rms, vib_z_rms`

Gerekirse tepe ivme, sensör durum bayrakları, pencere örnek sayıları, veri geçerlilik bayrakları ve cihaz/modül kimliği eklenir. Alan adları ve birimler imalat/yazılım tasarımında kesinleştirilecektir.

## 6. Nihai modül imalatı öncesinde netleştirilecekler

1. ESP32 kart modeli, ADC/I²C kaynakları ve pin planı.
2. SCT013/ADS1115 ölçüm yolunun diğer sensörlerle kaynak paylaşımı.
3. MAX4466 analog çıkışının hangi ADC ile, hangi örnekleme hızı ve çözünürlükte okunacağı.
4. MPU6050 ODR, arayüz, filtre ve üç eksenli veri işleme yaklaşımı.
5. 1 saniyelik slotun kesin sınırları ve sensör pencerelerinin slotla ilişkisi.
6. Birleşik kayıt biçimi, Home Assistant aktarımı, yerel tamponlama ve veri kaybı davranışı.
7. ESP32 CPU/RAM/ADC/I²C yükü ve uzun süreli çalışma kararlılığı.
8. Besleme, topraklama, analog gürültü, kablo ve sensör montaj konumları.
9. Modül 3 ve 4'te ortak tutulacak alanlar ile cihaza özgü alanlar.

## 7. Nihai modül imalatına geçiş kapısı

Geçici deney düzeneği, nihai modül imalatı anlamına gelmez. Nihai imalat başlamadan önce bağlantı/pin planı, sensör listesi, veri şeması, örnekleme/zamanlama planı, yayın/taşıma yöntemi ve yazılım iş akışı deney sonuçlarıyla gözden geçirilip onaylanmalıdır. Açık teknik sorular varken nihai modül imalatı başlatılmaz.

## 8. Modül 2 ile PF/dalga biçimi araştırma ilişkisi

- Modül 2'nin MOD2-GRV001 masaüstü akım ölçüm görevi kapanmıştır. V1.6 akım ölçüm yolu referans olarak korunur.
- Modül 2'nin ayrı ileri araştırma yönü, SCT013 akım dalga biçimi ile ZMPT101B gerilim dalga biçimini incelemek; dalga istatistikleri ve PF koşullarının akım ölçüm sapmasıyla ilişkisini araştırmaktır.
- Modül 3 ve 4'ün saha deneyleri, farklı cihaz evreleri ve yük davranışlarından veri sağlayarak bu araştırmaya katkıda bulunabilir. PF'nin ölçüm sapmasına neden olduğu henüz kanıtlanmış değildir.
- ZMPT101B nihai Modül 3/4 donanımında koşullu bileşendir: Modül 2 araştırmasında yararlı sonuç üretir, Modül 3/4 saha deneyleriyle doğrulanır ve kaynak yükü uygun bulunursa eklenir. Başlangıçta zorunlu değildir.
- ZMPT101B tek başına PF ölçmez. PF incelemesi için gerilim ve akım dalga biçimleri uygun zaman eşlemesiyle örneklenmelidir.
- Mevcut ESP32 üzerinde işlemci, bellek, örnekleme ve yayın yükü ölçülür. Yetersiz kalırsa ESP32-P4 değerlendirilir; kesin kart seçimi daha sonra yapılır.

## 9. Açık tasarım kararları

- Otomatik program/aşama sınıflandırma algoritması bu mimari notla tanımlanmış değildir.
- Ses için desibel kalibrasyonu taahhüt edilmemiştir.
- Örnekleme hızları ve özellik hesaplama parametreleri henüz kesinleştirilmemiştir.
- PF kanalı ve ZMPT101B'nin kesin devre/örnekleme entegrasyonu deney sonuçlarına bağlıdır.


## Dağıtık ESP düzeni ve paket yayınlama yaklaşımı

Kullanıcı kararı (2026-11-22): Nihai Modül 3/4 donanımı oluşana kadar sensörler tek kartta toplanmayacaktır. Deney aşamasında birden fazla bağımsız/geçici ESP, kendi sensör kanalını okuyup ölçüm özetlerini paket halinde yayınlayabilir. Bu dağıtık düzende PZEM ile kurulan paket yayınlama tecrübesi temel alınacaktır.

- Her ESP kendi ölçümünü ve sensör özelliklerini üretir; yayın paketinde cihaz/kanal kimliği, zaman damgası ve ortak zaman dilimi numarası bulunması tasarım gereğidir.
- Paket biçimi, yayın aralığı, taşıma protokolü, alıcı tarafın eşleştirmesi ve kayıp/tekrar davranışı PZEM uygulamasındaki mevcut kod ve loglar incelenerek netleştirilecektir; mevcut protokol ayrıntıları görülmeden alan adları veya paket yapısı varsayılmayacaktır.
- Ayrı ESP'lerden gelen paketler merkezi alıcıda zaman damgası ve ortak dilim numarasıyla bir araya getirilecektir. Aynı dilim numarası tek başına örneklerin fiziksel olarak eşzamanlı alındığını kanıtlamaz; pencere başlangıç/bitişleri ve saat hizası ayrıca doğrulanacaktır.
- Dağıtık yapı geçici deney mimarisidir. Sensörler, örnekleme ve yayın davranışı deneylerle doğrulanınca gerekli kanallar nihai Modül 3/4 donanımında birleştirilecektir.
- Bu yaklaşım, nihai modül imalatını öne çekmez; tersine, imalat öncesi yazılım ve veri akışını gerçek koşullarda sınamak için kullanılır.

## Paket yayınlama için doğrulama başlıkları

1. PZEM'de kullanılan mevcut paket/mesaj yapısını ve yayın kodunu depodaki kaynaklardan tespit etmek.
2. Sensör ESP'leri için ortak zorunlu alanları belirlemek: cihaz kimliği, sensör/kanal kimliği, timestamp, tick_id/slice_no, pencere başlangıç-bitiş bilgisi ve veri geçerlilik durumu.
3. PZEM'den gelen ölçüm paketleriyle ses/titreşim ESP paketlerinin aynı zaman/dilim sözleşmesine nasıl uyacağını tanımlamak.
4. Alıcıda eksik paket, yinelenen paket, sıra dışı geliş, ESP yeniden başlatma ve saat eşitleme davranışlarını test etmek.
5. Paket kaybı ve gecikme ölçümlerini loglamak; yalnızca başarılı yayın örneklerini değil, hata/eksik veri durumlarını da raporlamak.

Bu maddeler tasarım ve test gereksinimidir; henüz doğrulanmış uygulama sonucu değildir.


## PF araştırması – sayısal hesaplama ve istatistik
PF/dalga biçimi araştırmasında amaç yalnızca analog dalgayı görselleştirmek değildir. SCT013 akım ve ZMPT101B gerilim örneklerinden pencere bazında aktif güç, RMS, görünür güç ve gerçek PF hesaplanacak; pencere geçerliliği ve istatistiksel dağılım da saklanacaktır.
- Metodoloji: [DONANIM/ZMPT101B/PF-SAYISAL-HESAPLAMA-VE-ISTATISTIK-METODOLOJISI.md](../../DONANIM/ZMPT101B/REFERANS/PF-ARASTIRMA/PF-SAYISAL-HESAPLAMA-VE-ISTATISTIK-METODOLOJISI.md)
- Örneklerin ortak zaman tabanında eşleştirilmesi zorunludur; ortak slot numarası tek başına eşzamanlı örnekleme garantisi vermez.
- ADS1115'in kanal gecikmesi ve gerçek dönüşüm zamanları ölçülmeden PF hesaplaması doğrulanmış kabul edilmeyecektir.
- Düşük akım/görünür güç, eksik örnek, kırpılma ve zamanlama hatası içeren pencereler geçerlilik bayraklarıyla işaretlenecektir.
