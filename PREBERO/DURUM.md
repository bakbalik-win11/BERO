# PREBERO — Güncel durum ve devam noktası

> Bu dosya PREBERO için tek güncel çalışma noktasıdır. Oturuma yeniden başlarken önce burayı oku; ayrıntılı deney verilerini ilgili görev veya donanım kaydından aç. Bu dosyada yalnızca son karar, mevcut aşama, kısa geçmiş ve bir sonraki somut adım tutulur.

## Güncel durum — 2026-11-28

- **Ölçüm altyapısı kararı:** Sensör doğrulama sırası ve cihaz görevleri [Ölçüm Altyapısı Stratejisi V1.0](OLCUM-ALTYAPISI/OLCUM-STRATEJISI-V1.0.md) içinde sabitlendi. Önce sensörün ham çıkışı bağımsız DMM ile tanınacak; sonra dalga biçimi, ADC ve yazılım doğrulanacak.
- **Satın alma:** Tek planlanan yeni ölçüm cihazı UNI-T UT61E+ sipariş edildi (28.11.2026); teslim ve cihaz kontrolü bekleniyor. AD9833, AD9850, FYE050 veya XR2206 için şu aşamada yeni satın alma yapılmayacak. Mevcut FNIRSI 2D15P DDS, SG-002 DC simülatörü ve SANEC sinyal jeneratörü/lojik analizör mevcut görevleri için kullanılacak; doğrulanmayan işlevler deney öncesi teyit edilecek.

- **Aktif modül/görev:** Modül 2 / MOD2-GRV002 — BERO için pratik PF ölçümü ve PF etkili akım düzeltmesi.
- **Ana PF deney planı:** [MOD2-GRV002 — PF-DENEY-PLANI-V1.0](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/PF-DENEY-PLANI-V1.0.md) artık tek uygulama sırasıdır: ZMPT gerilim ölçeğini PZEM'e yaklaştır, PF≈1 SCT kalibrasyonunu koru, 1/2/3 LED → vantilatör → telefon şarjı → dimmerli akkor yükleri dene; PZEM kararlılığı ve veri kalite etiketlerini uygula. BERO bağımsız PF hesabı için ham zaman eşlemeli v[n]/i[n] ve ADC yeterliliği ayrıca doğrulanacak.
- **MOD2-GRV001:** Kapalı. V1.6 EXP/K(x) modeli ve YAML korunur.
- **Kullanıcının seçtiği yöntem:** Önce güvenli kart kontrolü ve sabit dirençli yükte ZMPT101B gerilim RMS ölçeğini trimpotla PZEM'e yaklaştır; ardından gerçek yüklerde 1/2/3 LED, vantilatör ve telefon şarjını, son olarak ayrı kontrollü deneyde dimmerli akkoru incele. PZEM PF karşılaştırma etiketidir; BERO'nun bağımsız PF hesabı ham zaman eşlemeli gerilim-akım örnekleri ve yeterli ADC örneklemesi gerektirir.

- **SCT/PF deney kararı (2026-11-28):** Kullanıcı, SCT013 akım kalibrasyonunun PF≈1 koşulunda daha önce başarıldığını teyit etti; bu kalibrasyon ve MOD2-GRV001 V1.6 korunacak, PF<1 deneyinde baştan ayarlanmayacak. ZMPT101B trimpotu yalnız gerilim RMS ölçeğini PZEM'e yaklaştıracak; PF çalışma noktası dimmerle seçilecek (ör. PZEM PF≈0,50) ve dimmer sabitlenecek. PF, yalnızca gerilim/akım RMS değerlerinden değil, zaman eşlemeli örneklerle (P=\operatorname{mean}(v[n]i[n])) ve (PF=P/(V_{RMS}I_{RMS})) hesabından üretilecek. SCT hatası yalnız sabit doğrusal genlik kazancıysa bu kazanç PF oranında sadeleşebilir; faz/frekans hatası, dalga bozulması, kırpılma, ofset/gürültü veya örnekleme zaman farkı PF'yi de bozabilir. Bu karar deney planıdır; henüz doğrulanmış PF sonucu/fonksiyon yoktur. Ayrıntı: [MOD2-GRV002 §16](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).


- **PF deney matrisi güncellemesi (2026-11-28):** Düzeltme yalnız PF'ye bağlanmayacak; PF, I_RMS, I_peak/crest factor, yük tipi/dalga biçimi ve örnekleme kimliği ayrı kaydedilecek. Dimmerli 100 W ve 8,5 W LED tarihsel verileri farklı, birbirine karıştırılmayacak çalışma koşullarıdır. PZEM-REF-WROOM-01 5 saniyelik yayın yaptığı için yük/dimmer geçişinden sonra kararlı plato beklenip aynı zaman sınırlarında pencere özeti karşılaştırılacak. Kritik sınır: mevcut ADS1115 ct_clamp kayıtları 200 ms RMS / 1 s yayın değeridir; ham v[n], i[n] örnek dizisi değildir. ADS1115 860 SPS ve MUX nedeniyle iki kanalı eşzamanlı örneklemez; gerçek PF/harmonik hesabından önce ham örnek hızı ve Δt ölçülmelidir. Detay: [MOD2-GRV002 §17](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).

- **PF ve akım düzeltmesi:** Modül 2 masaüstü platformuyla çamaşır makinesi gerçek yükünde alınan kaydın sonraki değerlendirmesinde akım sapmasının PF koşullarıyla ilişkili olduğu kullanıcı tarafından teyit edildi. Önce sabit yük/dimmer/PZEM karşılaştırmalarından pratik bir PF okuma ve akım düzeltme eğrisi, EXP/K(x) geliştirme yaklaşımına benzer biçimde aranacak. BERO'nun kendi SCT+gerilim sensörü PF'si girdiye dönüşecek. Kolay deney yeterli olmazsa daha ayrıntılı faz/zamanlama yöntemlerine geçilecek. V1.6'ya dokunulmaz; yeni model MOD2-GRV002'de tutulur.
- **PZEM:** Geliştirme/karşılaştırma referansıdır; mutlak doğru kabul edilmez ve son BERO hattı için zorunlu değildir.
- **Araştırma notları:** Diğer yapay zekâların karşılaştırmalı özeti, metodoloji ve dış kaynak incelemeleri isteğe bağlı başvurudur. Güncel deney sırasının yerine geçmez.
- **Kanıt durumu:** Bu yeni yöntem için fiziksel deney, PF katsayısı ve firmware doğrulaması henüz yoktur.


- **Deney logu pratik alanları (2026-11-28):** Her veri bloğunda `window_status=settling/steady/invalid`, yük değişim zamanı, PZEM yayın zamanı, gerçek ölçüm penceresi başlangıç/bitişi ve süresi, `ct_clamp_sample_duration_ms=200`, `ct_clamp_update_interval_ms=1000` ve logdan elde edilebiliyorsa gerçek kaynak örnek sayısı/efektif SPS ayrı tutulacak. ESPHome ct_clamp, her güncellemede bir 200 ms örnekleme fazı yürütür; 1 s update_interval saniyede beş adet 200 ms pencerenin birleştirildiği anlamına gelmez. PZEM'in 5 s yayın aralığı için geçişler `settling` olarak işaretlenir; önceden belirlenen ardışık yayın kararlılığı sağlanınca `steady` olur. Ayrıntı: [MOD2-GRV002 §17.6](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).


- **Veri kanıtı / ham kayıt ilkesi (2026-11-28):** `settling/steady/invalid` etiketleri geçiş, kararlı ve bozuk kayıtları ayırır; geçiş verisi silinmez. Zaman damgaları PZEM yayın zamanı ile BERO 200 ms ölçüm penceresinin ilişkisini incelemek içindir; PZEM'in iç ortalama penceresini kanıtlamaz. Gerçek kaynak örnek sayısı ve efektif SPS yalnız logdan alınır; yoksa tahmin edilmez. Ham ADS/PZEM kayıtları değişmeden saklanır; pencere seçimi, filtre, katsayı ve grafikler ayrı analiz çıktısında tutulur. Böylece aynı ham kayıt V1.6 ve PF araştırmasında farklı hipotezlerle yeniden incelenebilir; V1.6 kendi başına değiştirilmez. Detay: [MOD2-GRV002 §17.7](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).


- **Gerçek hayat PF yükleri (2026-11-28):** İlk ek deney serisi eldeki üç LED ampulle 1/2/3 ampul basamaklarıdır; her kademede PZEM kararlılığı yeniden beklenip V/I/P/PF ayrı kaydedilecek. Ampuller aynı model değilse model ve watt bilgileri tek tek etiketlenecek, kombinasyonlar aynı yük kabul edilmeyecek. Sonra vantilatörün sabit hız kademeleri; telefon şarjı ise uzun kararlı kalması beklenmeyen dinamik yük olarak incelenecek. Veri durumu settling/steady/dynamic/invalid olarak ayrılacak. Ayrıntı: [MOD2-GRV002 §17.8](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).


- **LED basamak deneyi uygulaması (2026-11-28):** Tek LED → iki LED → üç LED adımında her yük ekleme anı `load_change_timestamp` ile kaydedilecek; önceki pencere kapatılıp PZEM'in yeni değerleri kararlı hale gelene kadar `settling`, kararlılık şartı sağlanınca yeni `window_id` altında `steady` kullanılacak. Aynı model ampuller sürücü ailesini büyük ölçüde sabit tutar, ancak PF/crest factor/dalga biçiminin değişmeyeceği varsayılmaz; her basamakta ölçülür. Ayrıntı: [MOD2-GRV002 §17.9](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).

## Bir sonraki somut adım

Ana uygulama kaynağı [MOD2-GRV002 PF Deney Planı V1.0](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/PF-DENEY-PLANI-V1.0.md).

İlk olarak ZMPT101B kartının PCB/pin/besleme/OUT bilgilerini ve kapalı test düzeninin güvenliğini kontrol et. SCT013-030'un ham çıkışını FNIRSI 2D15P DMM ile kısa doğrudan ön gözlemden geçir; bu testin 0,05 A için hedefi yalnızca yaklaşık 1,67 mV RMS sinyalin görünürlüğü/kararlılığıdır. Ardından sabit dirençli yükte ZMPT gerilim RMS ölçeğini PZEM'e yaklaştır ve trimpot ayarını sabitle. Güvenlik kapısı tamamlanmadan şebeke tarafına bağlanma.

Sonraki gerçek yük serisi 1 → 2 → 3 LED, ardından vantilatör, telefon şarjı ve son olarak dimmerli akkor olacaktır. Her değişimde settling/steady/dynamic/invalid etiketlerini uygula; ham kayıtları koru. UT61E+ siparişi teslim edilip cihaz kontrolü yapılınca envanter durumu güncellenecek.

## Modül gelişim hikâyesi ve mevcut aşamalar

### Modül 1 – Ölçüm Destek ve Referans Birimleri

Modül 1, Modül 2 masaüstü deney platformunun kullandığı iki ayrı destek/referans birimini kapsayan üst gruptur. Tek bir birleşik fiziksel cihaz değildir. Genel indeks: [Modül 1 destek ve referans birimleri](MODUL-1-DESTEK-REFERANS/README.md).

#### Modül 1A – Bias Ünitesi

Önceki projeden devralınan fiziksel bias kaynağıdır. Kapalı kutu ve soketli bağlantılarla fiziksel imalatı tamamlanmıştır. Bu durum biasın işlevini, şebeke karakterini doğru aktardığını, galvanik izolasyonu veya elektriksel güvenliği kanıtlamaz. Ayrıntı: [hedefler](MODUL-1-BIAS-TRAFOSU/HEDEFLER.md), [imalat kaydı](MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md), [tarihçe](MODUL-1-BIAS-TRAFOSU/TARIHCE.md).

#### Modül 1B – PZEM Dış Referans Ünitesi

PZEM-004T V3.0 ve ESP32-WROOM yayıncısından oluşan dış karşılaştırma birimidir. Geçici fiziksel işlev etiketi **PZEM-REF-WROOM-01**'dir. Eski firmware adı `bero-modul3-wroom` tarihsel yazılım adıdır; güncel PREBERO Modül 3 ile aynı kimlik değildir. Modül 2 deneylerinde V/I/P/PF karşılaştırma ve etiket kaynağı olarak kullanılır; kalibrasyon standardı veya mutlak ground truth değildir. Ayrıntı: [Modül 1B kaydı](MODUL-1-DESTEK-REFERANS/MODUL-1B-PZEM-REFERANS.md).

### Modül 2 – Masaüstü Deney ve Altyapı Doğrulama Platformu

Modül 2, Modül 3 ve 4'te kullanılacak ölçüm altyapısının geliştirildiği ve denendiği masaüstü platformdur. Aktif düzenek **MOD2-BENCH-01**: ESP32-D2 + ADS1115 No.10 + SCT013 30 A / 1 V. Deney ihtiyacına göre Modül 1A bias ünitesi ve Modül 1B PZEM dış referans birimi kullanılır.

Akım okuma, sensör/ADC davranışı, kalibrasyon, örnekleme, veri zamanlaması, ham veri toplama ve PF araştırması Modül 2 kapsamındadır. Çamaşır makinesiyle daha önce alınan yaklaşık 78 dakikalık uzun program kaydı da Modül 2 altyapısının gerçek yükte sınanmasıdır. Makine bu deneyde **test yüküdür**; kayıt Modül 3'ün imal edildiği veya bütünleşik Modül 3 sisteminin çalıştığı anlamına gelmez. Eski `MOD3-AKM001` görev kimliği ve rapor yolu tarihsel çapraz referans olarak korunur; teknik sahiplik Modül 2'dir. Ayrıntı: [Modül 2 hedefleri](MODUL-2-AKIM-TESTLERI/HEDEFLER.md), [tarihçesi](MODUL-2-AKIM-TESTLERI/TARIHCE.md) ve [MOD2-GRV002 PF deney planı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/PF-DENEY-PLANI-V1.0.md).

### Modül 3 – Çamaşır Makinesi Nihai Modülü

**FİZİKSEL İMALAT YAPILMADI.** Modül 3, Modül 2'de geliştirilen ölçüm altyapısının ileride çamaşır makinesi için ses ve titreşim kanallarıyla bütünleştirileceği nihai hedeftir. Bugüne kadarki çamaşır makinesi akım/PZEM kayıtları Modül 2 platformunun gerçek yük testleridir ve Modül 3 tasarımına girdi bırakır. Eski `MOD3-AKM001` kaydı bu geçmişi izlemek için bağlantılı tutulur; Modül 3 imalatı veya bütünleşik sensör başarısı sayılmaz. Ayrıntı: [hedefler](MODUL-3-CAMASIR-MAKINESI/HEDEFLER.md), [tarihçe](MODUL-3-CAMASIR-MAKINESI/TARIHCE.md), [eski görev izi](MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/GOREV.md).

### Modül 4 – Bulaşık Makinesi Nihai Modülü

**FİZİKSEL İMALAT YAPILMADI.** Modül 4, Modül 2'de geliştirilecek ve doğrulanacak ölçüm altyapısının ileride bulaşık makinesine uyarlanacağı nihai hedeftir. Bulaşık makinesiyle Modül 2 kapsamında tamamlanmış saha deneyi bulunduğu varsayılmaz. Modül 3/4 ortak zaman pencereli akım, ses ve titreşim mimarisi taslaktır; imalat öncesi karar kapıları geçilmeden fiziksel modül yapılmayacaktır. Ayrıntı: [hedefler](MODUL-4-BULASIK-MAKINESI/HEDEFLER.md), [tarihçe](MODUL-4-BULASIK-MAKINESI/TARIHCE.md), [ortak mimari](ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md).

### Modül 5 — Ana pano

Ana pano izleme modülü bekliyor; görev ve saha çalışması henüz açılmadı. Amaç ve modül geçmişi netleştikçe kayıtlar [Modül 5 klasörüne](MODUL-5-ANA-PANO/) eklenecek.

## Bilginin modüller arasında ilerlemesi

Sensör tecrübesi ve tekrar kullanılabilir küçük kodlar sensörün DONANIM kaydında tutulur. Deney, kanıt ve olgunlaşma aktif PREBERO görevi içinde ilerler. Olgunlaşan sonuç uygun nihai modüle aktarılır ve kaynak kaydına bağlantı verilir. Fiziksel modül devreden çıksa veya imha edilse bile modülün amacı ve geçmiş kayıtları korunur; fiziksel durum ENVANTER'de güncellenir. Bu çalışma düzeninin kalıcı kuralı [ana README’de](../README.md) açıklanır.

## Kısa geçmiş

- **2026-11-21:** Biaslı/biassız SCT karşılaştırmaları Modül 2 masaüstü platformunda yapıldı. Biaslı kolun ortalama ölçüme etkisi yaklaşık 0,47 A noktasında gözlendi; genel veri kalitesi kazancı ek karmaşıklığı haklı çıkarmadığından basit biassız yol tercih edildi.
- **2026-11-22:** MOD2-GRV001 için V1.6 tek fonksiyonlu EXP/K(x) modeli kabul edildi. Aynı dönemde çamaşır makinesi gerçek yük kaydı da Modül 2 altyapı doğrulaması olarak üretildi; eski MOD3-AKM001 bağlantısı tarihsel iz için korundu.
- **2026-11-24:** PF ve PF etkili akım araştırması için MOD2-GRV002 açıldı.
- **2026-11-27:** Kullanıcı, pratik ZMPT trimpot + PZEM gerilim karşılaştırmasıyla başlayıp SCT013/PF denemesine ve yeni akım düzeltme adayına ilerleme sırasını seçti. Henüz deney yapılmadı.
- **2026-11-28:** Kullanıcı, çamaşır makinesi kaydındaki PF/akım ilişkisini teyit etti ve hobi projesi için önce basit, sabit yükle yapılabilir deneylerden EXP/K(x) benzeri PF etkili f(X) aramayı; işe yaramazsa daha ayrıntılı yönteme geçmeyi seçti.
- **2026-11-28:** Donanım kimlikleri ayrıştırıldı: eski imha edilmiş fiziksel Modül 2 ile aktif masaüstü MOD2-BENCH-01 aynı şey değildir; PZEM yayımlayan WROOM ESP'nin de eski `bero-modul3-wroom` firmware adı kalırken bağımsız PZEM-REF-WROOM-01 varlığı olarak yaşadığı kullanıcı tarafından teyit edildi.
- **2026-11-28:** PF/ZMPT adımlarından önce sensör çıkışını bağımsız gözleme kararı alındı. FNIRSI 2D15P DMM ile SCT013-030'un 0,05 A karşılığı yaklaşık 1,67 mV RMS çıkışının okunabilirliği denenecek. Bu bir deney planıdır; fiziksel ölçüm veya sonuç henüz yoktur.

Ayrıntılı teknik geçmiş Modül 2 [TARIHCE.md](MODUL-2-AKIM-TESTLERI/TARIHCE.md), MOD2-GRV002 [görev kaydı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md) ve ilgili donanım kayıtlarındadır. Oturum sonunda önce ilgili tarihçe/görev kanıtını, sonra bu dosyadaki güncel durum ve sıradaki adımı yenile.
