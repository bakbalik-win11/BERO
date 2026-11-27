# PREBERO — Güncel durum ve devam noktası

> Bu dosya PREBERO için tek güncel çalışma noktasıdır. Oturuma yeniden başlarken önce burayı oku; ayrıntılı deney verilerini ilgili görev veya donanım kaydından aç. Bu dosyada yalnızca son karar, mevcut aşama, kısa geçmiş ve bir sonraki somut adım tutulur.

## Güncel durum — 2026-11-27

- **Aktif modül/görev:** Modül 2 / MOD2-GRV002 — BERO için pratik PF ölçümü ve PF etkili akım düzeltmesi.
- **MOD2-GRV001:** Kapalı. V1.6 EXP/K(x) modeli ve YAML korunur.
- **Kullanıcının seçtiği ilk yöntem:** ZMPT101B hazır kartını tanı; güvenlik ön kontrolünden sonra trimpotla yaklaşık 220–230 V AC gerilim okumasını PZEM'e yaklaştır; ardından SCT013 ile faz/PF ilişkisini dene.
- **PF deneyi:** Sabit ampul yükünü dimmerin farklı ayarlarında çalıştır; her kararlı pencerede PZEM V/I/P/PF değerlerini BERO'nun ham ve hesaplanan sonuçlarıyla karşılaştır. Dimmer ayarı PF yanında akımı ve dalga şeklini de değiştirebilir.
- **Akım formülü:** BERO PF bilgisiyle yeni PF etkili akım düzeltme adayı geliştirilebilir. Gerilim genlik ayarı, PHASE_CORRECTION ve akım düzeltmesi birbirinden ayrı tutulur. V1.6'ya dokunulmaz; yeni model MOD2-GRV002'de tutulur.
- **PZEM:** Geliştirme/karşılaştırma referansıdır; mutlak doğru kabul edilmez ve son BERO hattı için zorunlu değildir.
- **Araştırma notları:** Diğer yapay zekâların karşılaştırmalı özeti, metodoloji ve dış kaynak incelemeleri isteğe bağlı başvurudur. Güncel deney sırasının yerine geçmez.
- **Kanıt durumu:** Bu yeni yöntem için fiziksel deney, PF katsayısı ve firmware doğrulaması henüz yoktur.

## Bir sonraki somut adım

ZMPT101B kartının ön/arka yüzünü ve revizyon/pin işaretlerini kaydet; trimpotun etkisini ve güvenli ön test düzenini belirle. Kartın giriş devresi, yalıtım/mesafe, terminal koruması ve kapalı test düzeneği kontrol edilmeden 220–230 V bağlantısına geçme. Osiloskop ground klipslerini şebekeye bağlama.

## Modül gelişim hikâyesi ve mevcut aşamalar

### Modül 1 — Şebeke karakterini koruyan bias

Önce genel bias orta nokta yapısı tanımlandı; 3,30 V kutu çıkışından iki eşit dirençle yaklaşık 1,65 V orta nokta ölçüldü. Taşınabilir bias güç kutusu fiziksel olarak üretildi, kapalı kutu ve soketli bağlantı olarak kaydedildi. Şebeke karakterinin SCT013 ölçüm sinyaline aktarılması, izolasyon ve güvenlik doğrulaması tamamlanmış sayılmaz. Modül 1 kayıtları [burada](MODUL-1-BIAS-TRAFOSU/TARIHCE.md); imalat bilgisi [burada](MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md).

### Modül 2 — Masaüstü akım ve PF geliştirme

İlk masaüstü çalışmalarında SCT013 biaslı/biassız karşılaştırmaları ve farklı yük denemeleri yapıldı; bu sırada çamaşır makinesi saha kayıtları da alındı. Bias ölçüm ortalamasını bazı çalışma noktalarında etkiledi, ancak genel veri kalitesindeki iyileşme ek donanım ve bağlantı karmaşıklığını haklı çıkaracak kadar büyük görülmedi. Bu nedenle basit biassız ölçüm yolu tercih edildi. V1.6 EXP/K(x) akım modeli mevcut akım hedefi için referans kabul edildi; MOD2-GRV001 kapatıldı ve modeli değiştirmeme kararı alındı. Bias deneyi geçmişi ve teknik sonuçlar [Modül 2 tarihçesinde](MODUL-2-AKIM-TESTLERI/TARIHCE.md), akım modeli kanıtı GRV001 kayıtlarında; saha kaydı ise [Modül 3 tarihçesinde](MODUL-3-CAMASIR-MAKINESI/TARIHCE.md) bulunur.

Şimdi MOD2-GRV002’de ZMPT101B’yi tanıma, trimpotla gerilim okumasını PZEM’e yaklaştırma, SCT013 ile PF denemesi yapma ve işe yararsa PF bilgisini yeni akım düzeltmesine katma planı var. İlk pratik sıra ve sonraki adım yukarıdaki güncel durum bölümündedir. Bu aşamada fiziksel PF deneyi veya yeni katsayı yoktur. V1.6 korunur; ayrıntılar [MOD2-GRV002 görevinde](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md).

### Modül 3 — Çamaşır makinesi

Modül 2’den gelen V1.6 akım ölçüm yolu ile çamaşır makinesinin uzun pamuklu programında yaklaşık 78 dakikalık saha kaydı alındı. Isıtma bölümünde PZEM akımıyla yakın takip; sonraki düşük akım bölümlerinde pozitif fark gözlendi. Farkın PF kaynaklı olduğu kanıtlanmadı. MOD3-AKM001 saha kaydı hedefini tamamlayıp kapandı; ses/titreşim ve nihai modül mimarisi bu görevde tamamlanmadı. Tarihçe [burada](MODUL-3-CAMASIR-MAKINESI/TARIHCE.md), görev [burada](MODUL-3-CAMASIR-MAKINESI/GOREVLER/MOD3-AKM001/GOREV.md).

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

Ayrıntılı teknik geçmiş Modül 2 [TARIHCE.md](MODUL-2-AKIM-TESTLERI/TARIHCE.md), MOD2-GRV002 [görev kaydı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md) ve ilgili donanım kayıtlarındadır. Oturum sonunda önce ilgili tarihçe/görev kanıtını, sonra bu dosyadaki güncel durum ve sıradaki adımı yenile.
