# PREBERO — Güncel durum ve devam noktası

> Bu dosya PREBERO için tek güncel çalışma noktasıdır. Oturuma yeniden başlarken önce burayı oku; ayrıntılı deney verilerini ilgili görev veya donanım kaydından aç. Bu dosyada yalnızca son karar, mevcut aşama, kısa geçmiş ve bir sonraki somut adım tutulur.

## Güncel durum — 2026-11-28

- **Aktif modül/görev:** Modül 2 / MOD2-GRV002 — BERO için pratik PF ölçümü ve PF etkili akım düzeltmesi.
- **MOD2-GRV001:** Kapalı. V1.6 EXP/K(x) modeli ve YAML korunur.
- **Kullanıcının seçtiği ilk yöntem:** Hobi/prototip ölçeğinde kolay, pratik deneyi öne al. Güvenlik ön kontrolünden sonra ZMPT101B gerilim okumasını trimpotla PZEM'e yaklaştır; sabit lamba ve dimmer ayarlarında PZEM PF'yi referans alarak SCT013 + ZMPT101B PF okumasını dene.
- **PF ve akım düzeltmesi:** Çamaşır makinesi saha kaydının sonraki değerlendirmesinde akım sapmasının PF koşullarıyla ilişkili olduğu teyit edildi. Önce sabit yük/dimmer/PZEM karşılaştırmalarından pratik bir PF okuma ve akım düzeltme eğrisi, EXP/K(x) geliştirme yaklaşımına benzer biçimde aranacak. BERO'nun kendi SCT+gerilim sensörü PF'si girdiye dönüşecek. Kolay deney yeterli olmazsa daha ayrıntılı faz/zamanlama yöntemlerine geçilecek. V1.6'ya dokunulmaz; yeni model MOD2-GRV002'de tutulur.
- **PZEM:** Geliştirme/karşılaştırma referansıdır; mutlak doğru kabul edilmez ve son BERO hattı için zorunlu değildir.
- **Araştırma notları:** Diğer yapay zekâların karşılaştırmalı özeti, metodoloji ve dış kaynak incelemeleri isteğe bağlı başvurudur. Güncel deney sırasının yerine geçmez.
- **Kanıt durumu:** Bu yeni yöntem için fiziksel deney, PF katsayısı ve firmware doğrulaması henüz yoktur.

## Bir sonraki somut adım

Önce FNIRSI 2D15P'yi DMM modunda kullanarak SCT013-030 (30 A / 1 V) sensör çıkışını doğrudan ölç. İlk hedef, 0,05 A RMS primer akımına karşılık gelen yaklaşık 1,67 mV RMS AC değerin yüksüz tabandan ayırt edilip edilemediğini ve tekrarlandığında kararlı görünüp görünmediğini kontrol etmektir. Bu ilk deneyde ESP32, ADS1115, MCP3208, bias, harici burden veya yükselteç kullanma. Akımın gerçekten 0,05 A olduğu bağımsız ve güvenilir biçimde doğrulanamıyorsa sonucu yaklaşık yük denemesi olarak kaydet; kesin 0,05 A sonucu ilan etme. Ayrıntı: [FNIRSI 2D15P DMM – SCT013-030 deney planı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/DENEYLER/FNIRSI-2D15P-DMM-SCT013-030-005A-2026-11-28.md).

Bu ön testten sonra MOD2-GRV002'nin ZMPT101B kartını tanıma ve PF deneyi adımlarına devam et. Şebeke bağlantısı için kartın giriş devresi, yalıtım/mesafeler, terminal koruması ve kapalı test düzeneği ayrıca kontrol edilir. Osiloskop ground klipslerini şebekeye bağlama.

## Modül gelişim hikâyesi ve mevcut aşamalar

### Modül 1 — Şebeke karakterini koruyan bias

Önce genel bias orta nokta yapısı tanımlandı; 3,30 V kutu çıkışından iki eşit dirençle yaklaşık 1,65 V orta nokta ölçüldü. Taşınabilir bias güç kutusu fiziksel olarak üretildi, kapalı kutu ve soketli bağlantı olarak kaydedildi. Şebeke karakterinin SCT013 ölçüm sinyaline aktarılması, izolasyon ve güvenlik doğrulaması tamamlanmış sayılmaz. Modül 1 kayıtları [burada](MODUL-1-BIAS-TRAFOSU/TARIHCE.md); imalat bilgisi [burada](MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md).

### Modül 2 — Masaüstü akım ve PF geliştirme

Modül numarası burada geliştirme/deney alanını belirtir; her zaman tek bir kalıcı fiziksel cihaz demek değildir. Eski üç kanallı biaslı fiziksel Modül 2 imha edilmiştir. Bugünkü masaüstü ölçüm düzeneği ayrı varlık **MOD2-BENCH-01**'dir: ESP32-D2 + ADS1115 No.10 + SCT013 30 A / 1 V. Modül 1'in taşınabilir bias güç kutusu da bu düzeneğin kendisi değildir.

Bu masaüstü düzende SCT013 biaslı/biassız karşılaştırmaları ve farklı yük denemeleri yapıldı; bu sırada çamaşır makinesi saha kayıtları da alındı. Bias ölçüm ortalamasını bazı çalışma noktalarında etkiledi, ancak genel veri kalitesi iyileşmesi ek donanım ve bağlantı karmaşıklığını haklı çıkaracak kadar büyük görülmedi. Bu nedenle basit biassız ölçüm yolu tercih edildi. V1.6 EXP/K(x) akım modeli sabit yük deneylerinden geliştirildi ve korunmuş referans olarak MOD2-GRV001 kapatıldı. Çamaşır makinesi kaydının sonraki değerlendirmesinde PF koşullarının akım sapmasıyla ilişkisi teyit edildi; bu gözlem PF'yi yeni düzeltme denklemine katma gerekçesi oldu.

PZEM değerlerini yayınlayan ESP32-WROOM ise ayrı varlık **PZEM-REF-WROOM-01**'dir. Eski firmware adı `bero-modul3-wroom` olsa da güncel PREBERO Modül 3 (çamaşır makinesi) ile aynı kimlik değildir; MOD2 deneylerinde karşılaştırma referansı olarak kullanılabilir. Envanter ve cihaz eşlemesi [burada](../ENVANTER/README.md); bias/model kanıtı [Modül 2 tarihçesi](MODUL-2-AKIM-TESTLERI/TARIHCE.md) ve GRV001 kayıtlarında; çamaşır makinesi saha kaydı [Modül 3 tarihçesinde](MODUL-3-CAMASIR-MAKINESI/TARIHCE.md) bulunur.

Şimdi MOD2-GRV002’de önce basit sabit yük/dimmer deneyleriyle PZEM referanslı PF ve akım noktaları toplanacak; yeni ZMPT101B + SCT013 zincirinin PF okumasından pratik bir f(X) düzeltmesi aranacak. Bu yolla sonuç alınamazsa ayrıntılı faz/zamanlama yöntemleri yedek plandır. Henüz yeni katsayı bulunmadı veya fiziksel doğrulanmadı. V1.6 korunur; ayrıntılar [MOD2-GRV002 görevinde](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).

### Modül 3 — Çamaşır makinesi

Modül 2’den gelen V1.6 akım ölçüm yolu ile çamaşır makinesinin uzun pamuklu programında yaklaşık 78 dakikalık saha kaydı alındı. Isıtma bölümünde PZEM akımıyla yakın takip; sonraki düşük akım bölümlerinde pozitif fark görüldü. Kullanıcının kayıt üzerindeki sonraki değerlendirmesi, bu farkın PF koşullarıyla ilişkisini teyit etti ve PF'yi akım denklemine katma araştırmasını başlattı. MOD3-AKM001 saha kaydı hedefini tamamlayıp kapandı; ses/titreşim ve nihai modül mimarisi bu görevde tamamlanmadı. Tarihçe [burada](MODUL-3-CAMASIR-MAKINESI/TARIHCE.md), görev [burada](MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/GOREV.md).

### Modül 4 — Bulaşık makinesi

Modül 4 saha çalışması henüz başlamadı. Modül 3 ile ortak zaman pencereli akım, ses ve titreşim veri toplama fikri taslak olarak belirlendi; örnekleme, bağlantı ve veri birleştirme koşulları doğrulanmadan nihai imalata geçilmeyecek. Ortak taslak [burada](ORTAK-MIMARI/MODUL-3-4-ORTAK-ZAMAN-PENCERELI-VERI-TOPLAMA-MIMARISI.md), Modül 4 tarihçesi [burada](MODUL-4-BULASIK-MAKINESI/TARIHCE.md).

### Modül 5 — Ana pano

Ana pano izleme modülü bekliyor; görev ve saha çalışması henüz açılmadı. Amaç ve modül geçmişi netleştikçe kayıtlar [Modül 5 klasörüne](MODUL-5-ANA-PANO/) eklenecek.

## Bilginin modüller arasında ilerlemesi

Sensör tecrübesi ve tekrar kullanılabilir küçük kodlar sensörün DONANIM kaydında tutulur. Deney, kanıt ve olgunlaşma aktif PREBERO görevi içinde ilerler. Olgunlaşan sonuç uygun nihai modüle aktarılır ve kaynak kaydına bağlantı verilir. Fiziksel modül devreden çıksa veya imha edilse bile modülün amacı ve geçmiş kayıtları korunur; fiziksel durum ENVANTER'de güncellenir. Bu çalışma düzeninin kalıcı kuralı [ana README’de](../README.md) açıklanır.

## Kısa geçmiş

- **2026-11-21:** Biaslı/biassız SCT karşılaştırmaları yapıldı. Biaslı kolun ölçüm ortalamasına etkisi yaklaşık 0,47 A çalışma noktasında gözlendi; genel veri kalitesi kazancı ek donanım karmaşıklığını haklı çıkarmadığından biassız yol tercih edildi. Çamaşır makinesi kayıtları da bu masaüstü geliştirme dönemi boyunca ayrıca alındı; kontrollü bias karşılaştırmasıyla karıştırılmamalı.
- **2026-11-22:** MOD2-GRV001 için V1.6 tek fonksiyonlu EXP/K(x) modeli kabul edildi; görev kapatıldı ve referans korunuyor.
- **2026-11-24:** PF ve PF etkili akım araştırması için MOD2-GRV002 açıldı.
- **2026-11-27:** Kullanıcı, pratik ZMPT trimpot + PZEM gerilim karşılaştırmasıyla başlayıp SCT013/PF denemesine ve yeni akım düzeltme adayına ilerleme sırasını seçti. Henüz deney yapılmadı.
- **2026-11-28:** Kullanıcı, çamaşır makinesi kaydındaki PF/akım ilişkisini teyit etti ve hobi projesi için önce basit, sabit yükle yapılabilir deneylerden EXP/K(x) benzeri PF etkili f(X) aramayı; işe yaramazsa daha ayrıntılı yönteme geçmeyi seçti.
- **2026-11-28:** Donanım kimlikleri ayrıştırıldı: eski imha edilmiş fiziksel Modül 2 ile aktif masaüstü MOD2-BENCH-01 aynı şey değildir; PZEM yayımlayan WROOM ESP'nin de eski `bero-modul3-wroom` firmware adı kalırken bağımsız PZEM-REF-WROOM-01 varlığı olarak yaşadığı kullanıcı tarafından teyit edildi.
- **2026-11-28:** PF/ZMPT adımlarından önce sensör çıkışını bağımsız gözleme kararı alındı. FNIRSI 2D15P DMM ile SCT013-030'un 0,05 A karşılığı yaklaşık 1,67 mV RMS çıkışının okunabilirliği denenecek. Bu bir deney planıdır; fiziksel ölçüm veya sonuç henüz yoktur.

Ayrıntılı teknik geçmiş Modül 2 [TARIHCE.md](MODUL-2-AKIM-TESTLERI/TARIHCE.md), MOD2-GRV002 [görev kaydı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md) ve ilgili donanım kayıtlarındadır. Oturum sonunda önce ilgili tarihçe/görev kanıtını, sonra bu dosyadaki güncel durum ve sıradaki adımı yenile.
