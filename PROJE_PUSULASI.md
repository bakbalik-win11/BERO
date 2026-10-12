# Proje BERO — Ana Pusula ve Süreklilik Kaydı

> Bu belge, günlük deney ayrıntılarının yerine geçmez. Projenin genel yönünü, nereden geldiğimizi, şu anda nerede olduğumuzu ve sıradaki adımı takip eden ana çerçevedir.

## 1. Bu belgenin görevi

Bu dosya, yeni bir çalışma oturumuna veya sohbete geçildiğinde BERO'nun bağlamını yeniden kurmak için ilk bakılacak yönlendirme kaydıdır.

- **Ana çerçeve burada:** proje amacı, ana mimari, aktif hedef, güncel durum ve sıradaki adım.
- **Görev ayrıntıları GOREVLER altında:** test planı, kod sürümleri, ölçümler, loglar ve görev deneyimi.
- **Ana hedefler HEDEFLER altında:** hedef tanımı, hedefe bağlı görev silsilesi ve hedefin sonuçlandırılması.
- **Fikir havuzu TODO altında:** henüz resmî göreve dönüşmemiş fikirler ve küçük yapılacaklar.
- **Kalıcı kararlar ve süreklilik ilkeleri** kendi belgelerinde korunur.
- Bu belge ayrıntılı kayıtların yerine geçmez; ilgili kayıtlara yönlendirir.

## 2. BERO'nun genel yönü

Proje BERO, ev otomasyonu ve ölçüm/denetim sistemini modüler, ölçülebilir, doğrulanabilir ve zaman içinde sürdürülebilir biçimde kurmayı hedefler.

Bilinen ana mimari çerçeve:
- **Home Assistant:** üst seviye otomasyon ve karar katmanı.
- **Aqara ve mevcut akıllı ev cihazları:** yaşam otomasyonunun mevcut bileşenleri.
- **ESP32 düğümleri:** özel ölçüm, sensör ve yerel kontrol işleri.
- **Saha I/O ve haberleşme:** RS485/Modbus ve Ethernet tabanlı modüler bağlantıların araştırılması.
- **Mini Node yaklaşımı:** işlevleri ayrıştırılmış ve bağımsız doğrulanabilir modüller.
- **Ölçüm disiplini:** ham veriyi, test koşullarını, yorumu ve doğrulanmış sonucu birbirinden ayırmak.

Bu bölüm ana resmi özetler. Ayrıntılı elektrik, HVAC, donanım ve bağlantı kararları kendi kayıtlarında tutulmalıdır; bu dosya onların yerine geçmez.

## 3. Aktif ana hedef

**[HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md)**

**Aktif çalışma HDF-002'dir.** HDF-001/GRV-001 önceki çalışmanın geçmişidir; kullanıcı üç kez başa dönmek istemediği için yeni araştırma hedefi HDF-002 altında kuruldu. HDF-001'e geri dönülmeyecek veya eski görev geçmişi silinmeyecek; HDF-002 yeni aktif hedef olarak sürdürülecek.

HDF-002'nin odağı: ölçüm zincirlerinin davranışını ayrı ayrı anlamak, ham veriyi korumak ve PZEM paket yayın anını fiziksel ölçüm anı saymadan, deney koşullarıyla desteklenen bölgeler arasında ilişki araştırmak. V/PF bağlamı korunur; deneyle desteklenmeyen eşleştirme yapılmaz.

**Sıradaki iş:** HDF-002 araştırma çerçevesinde, mevcut gerçek donanım ve kod durumunu depodaki ilgili görev/kayıtlardan doğrula; sonra planlanan deneyde neyin gözleneceğini netleştir. MCP, mevcut aktif hedefin varsayılan başlangıç noktası değildir.

## 4. Şu anki kayıtlı durum

- Hedef/görev yapısı GitHub'da oluşturuldu.
- GRV-001'in adı ve kapsamı ESP32-D + SCT-013 akım okuması olarak düzeltildi.
- Görev klasörlerinde RAPOR ve KOD alanları tanımlandı.
- Kayıt, sürümleme ve süreklilik politikası oluşturuldu.
- TODO fikir havuzu oluşturuldu. İlk fikir — ESP32-D ile SCT-013 30A/1V akım okuma — GRV-001 görevine dönüştürüldü ve TODO'da “Göreve dönüşenler — açık görevler” bölümünde açık `[ ]` olarak tutuluyor. Durum akışı açık fikir → göreve dönüşen açık kayıt → sonuçlanan kayıt biçiminde işliyor.
- **Deney sonucu veya derleme başarısı bu dosyada varsayılmayacak.** İlgili test kaydı ve kullanıcı doğrulaması bulunmadan kod başarılı/çalışıyor kabul edilmeyecek.
- GRV-001 henüz sonuçlandırılmış sayılmıyor.

Bu durum bölümü, yeni kanıt elde edildiğinde güncellenebilir bir anlık görüntüdür. Değişiklik önemli bir karar veya önceki durumu etkiliyorsa aşağıdaki kronolojiye ayrıca kayıt eklenir.

## 5. Sıradaki adım

1. **HDF-002'de kal; hedefi yeniden HDF-001'e döndürme ve projeyi sıfırlama.**
2. HDF-002'nin kayıtlı araştırma yönünü uygula: ölçüm zincirlerini kendi davranışları açısından ayır, ham veriyi ve koşulları koru.
3. PZEM paket yayın zamanını fiziksel ölçüm anı sayma; zaman bilgisi varsa yardımcı bağlam olarak tut.
4. PZEM tarafında akım etiketiyle birlikte V ve PF koşullarını koru; bölgeleri ancak fiziksel/deneysel bağlam destekliyorsa ilişkilendir.
5. Bu akşamki somut deney adımını mevcut donanım/kod kaydını doğruladıktan sonra seç. MCP veya sıfır sorunu varmış gibi varsayma; kullanıcı son mesajında MCP sıfırları olmadığını açıkça belirtti.
6. Sonuçları kanıtla kaydet; doğrulanmamış hipotezleri sonuç gibi yazma.

Bu liste HDF-002'nin devamını sağlar; önceki görev geçmişini silmez ve projeyi baştan başlatmaz.

## 6. Oturum devri — en son nerede kaldık?

Yeni bir oturuma geçerken bu bölümü kısa ve somut biçimde güncelle:
- **Son tamamlanan iş:** Hangi belge, kod veya deney tamamlandı?
- **Son doğrulanmış durum:** Hangi sonuç kullanıcı/ölçüm/log tarafından doğrulandı?
- **Açık soru:** Hangi belirsizlik hâlâ çözülmedi?
- **Sıradaki tek adım:** Devam etmek için ilk yapılacak somut işlem nedir?
- **İlgili kayıtlar:** Görev raporu, kod sürümü, log veya karar bağlantıları.

Bir sonuç doğrulanmadıysa “bekliyor” yaz; tahminle doldurma.

### Mevcut devir notu

- **Son tamamlanan işler:** GRV-005-15 QC v02, kullanıcının Mac mini bilgisayarında v06 CSV üzerinde çalıştırıldı; görünür Terminal çıktısı `RESULT: PASS (14/14 checks)` gösterdi. Ardından GRV-006-01 ilk dosya akışı asistan ortamında gerçekten çalıştırıldı.
- **GRV-006-01 kanıtı:** Sentetik ham CSV dosyası yazıldı ve yeniden okundu; üç satır Python ile dönüştürülerek ayrı çıktı dosyasına yazıldı ve yeniden okundu. Bağımsız hesaplanan toplam 120, çıktı dosyasından okunan toplam 120 ile eşleşti.
- **Kanıt sınırı:** GRV-005 Terminal çıktısında exit code ayrıca kaydedilmedi; QC yapısal uygunluğu gösterir, fiziksel ölçüm doğruluğunu kanıtlamaz. GRV-006-01 sentetik veri kullandı; ESP haberleşmesi henüz yapılmadı.
- **Sıradaki tek adım:** Depodaki mevcut ESP kodu ve haberleşme arayüzünü inceleyerek Python→ESP→geri okuma yolunu belirlemek; yeni haberleşme yöntemi varsaymamak.
- **İlgili kayıtlar:** [GRV-005 doğrudan QC sonucu](GOREVLER/GRV-005/RAPOR/GRV-005-15-QC-v02-GRV-005-14-v06-DOGRUDAN-CALISTIRMA-SONUCU-20261011.md), [GRV-006 Python kodu](GOREVLER/GRV-006/KOD/GRV-006-01-file-roundtrip-v01.py), [GRV-006 sonuç MD](GOREVLER/GRV-006/KOD/GRV-006-01-file-roundtrip-v01.md), [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md), [HISTORY](HISTORY/2026/2026-10-11.md).
- **Çalışma sınırı:** v06 ve önceki kayıtların üzerine yazma; kullanıcı ESP adı tercihini koru: `esp32d1`.


## 7. Önemli kararların kronolojisi

Bu bölüm **eklemeli kayıt** içindir. Yeni kararlar yeni tarihli maddeler olarak eklenir; eski maddeler sessizce değiştirilmez.

- **2026-10-09:** Ana hedef/görev ilişkisi kuruldu. HDF-001 “Akımı Okuma”; GRV-001 “ESP32-D ile SCT-013 Akım Okuması” olarak tanımlandı.
- **2026-10-09:** Geçmiş deneyimin üzerine yazmama, kod sürümlerini ve raporları koruma, her kod için eşlik eden Markdown belgesi bulundurma ve doğrulanmamış sonuçları doğrulanmış gibi sunmama ilkeleri kayıt altına alındı.
- **2026-10-09:** Henüz resmî göreve dönüşmemiş fikirler ve küçük yapılacaklar için tarihli, tamamlanma tikli ve yeni maddeleri üstte tutan TODO listesi oluşturuldu.
- **2026-10-09:** TODO sonuç durumları tanımlandı: “Tamamlandı”, “Vazgeçildi” ve “Göreve dönüştü”. Göreve dönüşen fikir, bağlı resmî görev tamamlanana kadar açık kalacak; sonuçlanmış maddeler ayrı bölüme taşınacak.

Yeni karar kaydında tarih, karar, gerekçe ve etkilediği dosyalar belirtilir.

- **2026-10-09:** Yeni süreklilik ilkesi: anlamlı görev basamakları görev raporunda tarihli izlenecek; tekrar kullanılabilir donanım/sensör tecrübesi kaynak görev ve kanıt bağlantısıyla donanımın Markdown notuna aktarılacak; doğrulanmış kod sürümleri koşulları ve test belgeleriyle ayrı korunacak. İlkenin uygulama ayrıntıları [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) içindedir.


- **2026-10-09:** Depoya dönüş/oturum başlatma kuralı: her yeni gün, ara sonrası veya yeni sohbetten devam ederken teknik işe başlamadan önce pusula, protokol, kayıt politikası, aktif görev, ilgili kod/MD ve HISTORY okunacak; günlük kontrol edilecek; çelişkiler açıklanacak ve kısa devam bağlamı çıkarılacak. Ayrıntı: [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md).

- **2026-10-11:** GRV-006 ayrı görev olarak açıldı. Amaç, gerçek veri üretme/yazma/okuma kanıtından başlayarak HA→Mac aktarımı, Python işlemesi, bağımsız teyit ve gerekirse tek iyileştirme turudur. Görev tanımı: [GRV-006](GOREVLER/GRV-006/RAPOR/README.md). Eski görev kayıtları değiştirilmez.

## 2026-10-12 — PZEM V/PF koşullu etiketleme ek kararı

- PZEM verisinde aynı/benzer gerilim ve PF koşullarındaki bölgeler önce işaretlenip gruplanacak.
- Akım etiketi bağlamından ayrılmayacak: `(I, V, PF)`. SCT karakterine aktarımda V/PF koşulları da korunacak.
- Benzer V/PF grupları daha basit bir aday `k` incelemesi sağlar; `k` sabit varsayılmayacak ve bağımsız veride sınanacak.
- V/PF benzerliği tek başına aynı fiziksel olay kanıtı değildir; deney bağlamı ve SCT karakteriyle desteklenmesi gerekir.
- Ayrıntı: [HDF-002 hedefi](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md) · [12 Ekim HISTORY](HISTORY/2026/2026-10-12.md).

## 2026-10-12 — HDF-002 yöntem kararı ve oturum devri

- **Olgunlaşan yöntem:** Her ölçüm zincirinden önce bağımsız olarak en yüksek kaliteli ham veriyi al; sensörleri Aşama 1'de aynı ESP'de toplamaya çalışma.
- **PZEM/SCT ayrımı:** PZEM kararlı bölgeleri akım etiketi alır; SCT bölgeleri sinyal karakteriyle tanımlanır. Python, deney bağlamının aynı fiziksel durumu desteklediği bölgeleri korele eder ve etiketi uygun SCT karakter bölgesine aktararak aday `I = f(X)` ilişkisini araştırır.
- **Eşleştirme sınırı:** Paket/zaman senkronizasyonu ön koşul değil; zaman yardımcı kanıt olabilir. Sayısal benzerlik tek başına eşleşme değildir. Ham kayıtlar ve deney metadatası korunur.
- **Aşama sınırı:** Donanım sadeleştirmesi/birleştirmesi ve paket optimizasyonu, bağımsız ham verinin karakteri anlaşıldıktan sonraki aşamadır.
- **Doğrulanmış durum:** Bu bir yöntem kararıdır; yeni deney veya performans doğrulaması değildir.
- **Sıradaki ilk adım:** Bağımsız ölçüm zincirlerinin ham veri ve kayıt yollarını belirlemek; PZEM okumasını sensör örneklemesinden ayırmak.
- **Ayrıntı:** [HDF-002 hedefi](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md) · [2026-10-12 gün sonu kaydı](HISTORY/2026/2026-10-12.md).

## 8. Süreklilik ilkesi

**Bir sonraki adımı bulurken önceki adımları kaybetme.** Yeni oturumda önce bu pusula, sonra ilgili ana hedef, sonra aktif görev raporu ve en son kod/log kayıtları okunur.

Ayrıntılı kayıt politikası: [KAYIT_VE_SUREKLILIK.md](KAYIT_VE_SUREKLILIK.md).

## 9. Asistanın komut tetikleyicileri

- **“Ara rapor”** verildiğinde [ASISTAN_ISLETIM_PROTOKOLU.md](ASISTAN_ISLETIM_PROTOKOLU.md) içindeki ara rapor kontrol listesi otomatik uygulanır.
- **“Günü kapa”** verildiğinde ara rapor adımlarına ek olarak gün sonu kaydı ve yeni oturum devri hazırlanır.
- Bu komutlar yalnızca sohbet yanıtı üretmek anlamına gelmez: uygun olduğunda kaynak kayıtlar ve bu pusula güncellenir; başarısız araç işlemleri açıkça bildirilir.

Komutların ayrıntılı kontrol listesi: [ASISTAN_ISLETIM_PROTOKOLU.md](ASISTAN_ISLETIM_PROTOKOLU.md).

## 10. Tarihli proje geçmişi

Projenin nereden nereye ilerlediğini tarih sırasıyla görmek için [HISTORY/](HISTORY/README.md) günlüğü kullanılır. “Ara rapor” ve “günü kapa” komutlarında yalnızca bu pusula güncellenmez; ilgili tarihin HISTORY dosyasına da yeni bir kayıt eklenir. Günlük geçmiş eklemeli tutulur ve eski girdiler silinmez.

## 11. TODO — fikir havuzu

[TODO/README.md](TODO/README.md), henüz resmî göreve dönüşmemiş fikirlerin ve küçük yapılacakların ortak listesidir. Yeni fikirler bölümün en üstüne eklenir; ilk kayıt tarihi korunur. Tamamlanan veya vazgeçilen fikirler silinmez, sonuç ve tarihleriyle “Sonuçlananlar” bölümüne taşınır. Bir fikir resmî göreve dönüşürse “Göreve dönüşenler — açık görevler” bölümüne alınır ve bağlı görev tamamlanana kadar açık kalır. Görev tamamlandığında sonuç “Görev tamamlandı” olarak kaydedilir.


## 12. Günlük kontrol listesi ve süreklilik

[GUNLUK/README.md](GUNLUK/README.md) günlük tik listesinin dizinidir. Her gün için `GUNLUK/YYYY/YYYY-MM-DD.md` dosyası tutulur; [GitHub Actions iş akışı](.github/workflows/daily-bero-checklist.yml) Türkiye saatiyle yaklaşık 03.05'te yeni günlük dosyası oluşturmaya ayarlanmıştır.

- “Ara rapor” ve “günü kapa” sırasında günlük kontrol listesi, TODO yaşam döngüsü, HISTORY, aktif görev raporu ve bu pusula birlikte gözden geçirilir.
- Kutular yalnızca ilgili işlem tamamlanıp GitHub kaydı geri okunarak doğrulandığında işaretlenir.
- Günlük otomasyonun zamanlanmış ilk çalışması henüz doğrulanmış değildir.


## 13. Süreklilik denetimi — 2026-10-09

- **Denetim bulgusu:** Günlük otomasyonun yeni dosyayı `GUNLUK/README.md` indeksine eklememesi düzeltildi.
- **Asistan sorumluluğu:** Günlük liste, TODO yaşam döngüsü, HISTORY, görev raporu, pusula, bağlantılar ve GitHub geri-okuma doğrulaması.
- **Kullanıcı sorumluluğu:** Yalnızca teknik kanıt ve kararlar — deney koşulları/ham loglar, derleme sonucu, gerektiğinde donanım veya çalışan yapılandırma değişikliği onayı.
- **Henüz doğrulanmayan:** GitHub Actions iş akışının gerçek çalıştırması. İlk başarılı çalıştırma görülene kadar günlük otomasyonun çalıştığı varsayılmayacak.
- **Sıradaki adım:** GitHub Actions durumunu doğrulamak; ardından GRV-001 için mevcut kod, bağlantı ve test koşullarını belirlemek.
- **Ayrıntılı kayıt:** [HISTORY Kayıt 007](HISTORY/2026/2026-10-09.md).


## 2026-10-10 güncellemesi — GRV-004 ADC deneyi

- **Son kayıt:** [GRV-004 ara raporu](GOREVLER/GRV-004/RAPOR/ALT-GOREV-03-ARA-RAPOR-20261010.md)
- **Son doğrulanmış teknik durum:** ESP32D1 API bağlantısı başarılı; GPIO32 BIAS, GPIO33 1T, GPIO34 2T ve GPIO35 3T canlı voltaj yayınlıyor. Son yüklenen log bölümünde PZEM satırı görünmüyor.
- **Aktif deney hedefi:** PZEM olmadan dört kanalda 1000'er okuma; her kanal için MIN, MAX ve ORTALAMA değerlerini tek satırda üretmek.
- **Açık noktalar:** Gerçek örnekleme hızı; 1000 okumanın tamamlanması; istatistik satırının üretilmesi; nihai YAML'ın derleme sonucu.
- **Sıradaki tek adım:** Ara rapor üzerinden hızlı okuma yöntemini ve sade kodu tartışarak netleştirmek.
- **Durum:** GRV-004 açık; bu güncelleme görev kapanışı veya teknik doğrulama değildir.


## 2026-10-11 — Ara sonrası devam notu

- **Kullanıcı durumu:** Üç kez sıfırlama sonrası ilerleme göremediğini ve devam edip etmeyeceğinden emin olmadığını belirterek ara verdi. Kullanıcıdan yeni test, komut veya sıfırlama istenmeyecek.
- **Asıl hedefin yeniden ifadesi:** Veri al → Python ile işle → sonucu doğrula → iyileştir. Hedef, soyut bir kontrol zinciri kurmak değil, görünür ve kanıtlanabilir veri işleme sonucudur.
- **Asistan yaklaşımının değerlendirmesi:** [GRV-005-16 ara raporu](GOREVLER/GRV-005/RAPOR/GRV-005-16-ARA-RAPOR-YAKLASIM-DEGERLENDIRMESI-20261011.md) okunmadan yeni teknik işe başlanmamalıdır.
- **Son teknik durum:** GRV-005-14 cihazın CSV satırları üretmesini kısmen doğrulamıştır; CSV alan hizası ve ESP→Python→ESP uçtan uca döngüsü tamamlanmış değildir. Bu durum SCT/ESP donanımının arızalı olduğunu veya kullanıcının hatalı olduğunu kanıtlamaz.
- **Devam edilirse ilk adım:** Yeni test başlatmak değil, GRV-005-16 raporunu kullanıcıyla tartışmak ve mevcut dosya/kod/log kanıtları üzerinden tek bir somut çıktı hedefi seçmektir.
- **Süreklilik şartı:** Geçmiş deneyimler ve kod sürümleri korunacak; yeni bir sıfırlama varsayılan çözüm olarak kullanılmayacak.


## 2026-10-11 — GRV-006-03 derleme/API bağlantısı

- **Son doğrulanan:** Kullanıcı GRV-006-03 v01 aday YAML'ın derlendiğini bildirdi. Paylaşılan ESPHome 2026.9.1 logu firmware derleme zamanını (2026-10-11 18:19:09 +0300), ESP32 rev3.1 bilgisini ve `esp32d1 @ 192.168.0.9` için API bağlantısı/handshake başarısını gösteriyor.
- **Kayıt:** [GRV-006-03 cihaz logu](GOREVLER/GRV-006/RAPOR/GRV-006-03-v01-CIHAZ-LOGU-20261011.md); [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md); [aday YAML](GOREVLER/GRV-006/KOD/GRV-006-03-v01-ADAY.yaml).
- **Kanıt sınırı:** Log parçası kesik. Python'dan action çağrısı ve ESP'den geri okuma henüz kanıtlanmadı; bu nedenle GRV-006-03 uçtan uca PASS değildir.
- **Sıradaki tek adım:** Python istemcisini mevcut API ayarlarıyla çalıştırıp `SENT` ve `ECHOED` değerlerinin eşleşmesini doğrulamak. ESP adı `esp32d1` olarak korunur; GRV-005 geçmişi değişmez.


## 2026-10-11 — GRV-006-03 Python → ESP → Python echo sonucu

- **Son doğrulanan teknik sonuç:** Kullanıcının Mac mini çıktısı `CONNECTED: 192.168.0.9:6053`, `SENT: 120`, `ECHOED: 120.0`, `RESULT: PASS` gösterdi. Python'dan ESP'ye gönderilen değer ESP echo sensöründen geri okundu ve eşleşti.
- **Açık küçük düzeltme:** İlk çalıştırma sonunda `APIClient.disconnect` asenkron kapatma uyarısı çıktı. Depodaki Python istemcisi `await client.disconnect()` şeklinde düzeltildi; yeniden çalıştırma ile uyarısız kapanış henüz doğrulanmadı.
- **Kanıt sınırı:** API echo akışı doğrulandı; gerçek SCT verisi, ölçüm doğruluğu ve GRV-006'nın bütün aşamaları tamamlanmış sayılmaz.
- **Sıradaki tek adım:** Düzeltilmiş Python dosyasını bir kez daha çalıştırıp PASS sonucunu ve uyarısız kapanışı teyit etmek.
- **İlgili kayıtlar:** [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md), [Python istemcisi](GOREVLER/GRV-006/KOD/GRV-006-03-v01-python-api-echo.py), [günlük HISTORY](HISTORY/2026/2026-10-11.md).


## 2026-10-11 — GRV-006-03 kapanış düzeltmesi doğrulandı

- Kullanıcı düzeltilmiş Python API echo istemcisini yeniden çalıştırdı: `SENT: 120`, `ECHOED: 120.0`, `RESULT: PASS`.
- Önceki `APIClient.disconnect` RuntimeWarning'i yeni çıktıda yok; düzeltme kullanıcı çalıştırmasıyla doğrulandı.
- **GRV-006-03 alt sonucu:** Python → ESP → Python echo PASS.
- **Kanıt sınırı:** Bu, SCT akım ölçüm doğruluğunu veya GRV-006'nın bütün hedefinin tamamlandığını kanıtlamaz.
- **Sıradaki yön:** Echo yolunu sabit kabul et ve GRV-006'nın Python veri işleme/bağımsız doğrulama basamaklarına dön; aynı testi sebepsiz tekrarlama.
- **Kayıtlar:** [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md), [Python istemcisi](GOREVLER/GRV-006/KOD/GRV-006-03-v01-python-api-echo.py), [HISTORY](HISTORY/2026/2026-10-11.md).


## 2026-10-11 — GRV-006 CSV → Python → ESP echo sonucu

- **Son doğrulanan:** Kullanıcı Mac mini üzerinde CSV işleme betiğini çalıştırdı. CSV'den üç kanalın `adc_rms_ac` değerleri okundu ve toplam `37.085439` bulundu.
- ×1000 ve yuvarlama sonucu `37085`; bağımsız yeniden okuma hesabı da `37085` verdi.
- ESP `192.168.0.9:6053` üzerinden bağlandı; `SENT: 37085`, `ECHOED: 37085.0`; `RESULT: PASS — CSV processed value returned by ESP`.
- **Sonuç:** Bu örnek CSV için dosya okuma → Python işleme → bağımsız kontrol → ESP'ye gönderme → geri okuma zinciri PASS.
- **Kanıt sınırı:** Kullanılan CSV geçmişte kaydedilmiş örnek veridir; yeni canlı SCT ölçümü ve fiziksel doğruluk kanıtı değildir. `invalid_count=NOT_TRACKED`; GRV-006'nın bütün kapsamı tamamlanmış değildir.
- **Sıradaki tek adım:** Kullanıcının çalıştırdığı `grv006_csv_to_esp.py` betiğini depoya ve görev raporuna kaydet; aynı echo testini tekrarlama.
- **İlgili kayıt:** [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md), [HISTORY](HISTORY/2026/2026-10-11.md).


## GRV-006 — sonraki adım

- Kullanıcının çalıştırdığı CSV→Python→ESP echo betiği depoya ayrı dosya ve MD olarak eklendi: [Python](GOREVLER/GRV-006/KOD/GRV-006-04-csv-to-esp-v01.py), [MD](GOREVLER/GRV-006/KOD/GRV-006-04-csv-to-esp-v01.md).
- Önceki PASS, eski kaydedilmiş CSV'ye aittir.
- **Sıradaki tek adım:** Yeni canlı cihaz CSV'siyle aynı akışı çalıştırmak; eski örnek CSV'yi yeniden deneyerek vakit kaybetmemek.


## 2026-10-11 — GRV-006-05 ADC raporu logda görüldü

- Kullanıcı birleşik GRV-006-05 kodunun derlendiğini ve ESPHome cihaz logunu paylaştı.
- Firmware: ESPHome 2026.9.1, derleme 18:49:28 +0300; `esp32d1` API bağlantısı başarılı.
- Dört ADC satırı oluştu: CH0-1T, CH1-2T, CH2-3T, BIAS; her satırda 1000 örnek.
- AC RMS sonuçları: CH0 12.111068, CH1 14.469792, CH2 12.546252.
- **Doğrulanan:** ADC örnek toplama ve raporlama satırlarının loga çıkması.
- **Henüz doğrulanmayan:** CSV kolon hizasının QC kontrolü, yeni canlı CSV üzerinden Python→ESP→geri okuma ve fiziksel akım doğruluğu.
- **Sıradaki tek adım:** Yeni log satırlarını ayrı canlı CSV dosyasına kaydet ve mevcut CSV→Python→ESP echo betiğini bu dosyayla çalıştır. Eski CSV korunacak.
- **Kayıtlar:** [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md), [birleşik YAML](GOREVLER/GRV-006/KOD/GRV-006-05-v01-BIRLESTIRILMIS-ADAY.yaml).


## 2026-10-11 — GRV-006-05 canlı CSV ve sıradaki çalıştırma

- Yeni ayrı dosya: [canlı logdan türetilen CSV](GOREVLER/GRV-006/RAPOR/GRV-006-05-LIVE-CSV-20261011.csv); [köken notu](GOREVLER/GRV-006/RAPOR/GRV-006-05-LIVE-CSV-20261011.md).
- Kaynak, kullanıcı tarafından paylaşılan ESPHome logudur; ESP'nin doğrudan diske yazdığı özgün CSV değildir.
- Beklenen AC RMS toplamı 39.127112; gönderilecek tamsayı 39127.
- **Sıradaki tek iş:** Depo kök dizininden çalıştır: `GRV006_CSV="GOREVLER/GRV-006/RAPOR/GRV-006-05-LIVE-CSV-20261011.csv" python3 GOREVLER/GRV-006/KOD/GRV-006-04-csv-to-esp-v01.py`.
- Kullanıcı terminal sonucu paylaşana kadar yeni canlı veri zinciri PASS sayılmaz. Eski CSV ve GRV-005 deneyimleri değiştirilmez.


## 2026-10-11 — GRV-006 canlı CSV zinciri PASS

- Yeni canlı log türevli CSV okundu; üç kanal toplamı 39.127112, gönderim değeri 39127.
- Bağımsız hesap PASS; ESP `192.168.0.9:6053` üzerinden SENT 39127 ve ECHOED 39127.0.
- **Kanıtlanan:** CSV → Python → bağımsız hesap → ESP → echo zinciri.
- **Sınır:** CSV ESP'nin doğrudan yazdığı dosya değil, logdan türetildi. Fiziksel akım doğruluğu kanıtlanmadı; `invalid_count=NOT_TRACKED`.
- **Sıradaki tek iş:** Özgün cihaz/log kaydının otomatik dosyaya alınması yolunu belirle; echo testini tekrarlama.
- [GRV-006 raporu](GOREVLER/GRV-006/RAPOR/README.md).


## 2026-10-11 — GRV-006 USB canlı kayıt yolu hazırlandı

- USB seri log yakalama betiği ve kullanım notu eklendi: [Python](GOREVLER/GRV-006/KOD/GRV-006-06-USB-serial-capture-v01.py), [MD](GOREVLER/GRV-006/KOD/GRV-006-06-USB-serial-capture-v01.md).
- Amaç: ESP32D1 logunu Mac'te ham dosyaya kaydetmek ve CSV satırlarını otomatik ayırmak; elle kopyalamayı kaldırmak.
- **Durum:** Kod depoda hazır; fiziksel USB çalıştırması doğrulanmadı. Gerçek cihaz kanıtı olmadan PASS yazılmayacak.
- **Sıradaki tek iş:** USB seri portta yakalama yapıp CSV kolon hizasını doğrulamak; ESP echo testi tekrar edilmeyecek.


## GRV-006 — uygulama için en kısa USB yolu

- [Mac USB kayıt komutları](GOREVLER/GRV-006/KOD/GRV-006-07-MAC-USB-KAYIT-KOMUTU.md) eklendi; [yakalama betiği](GOREVLER/GRV-006/KOD/GRV-006-06-USB-serial-capture-v01.py) mevcut ESP firmware'ini değiştirmez.
- Sıradaki tek adım: ESP32D1 USB ile Mac'e bağlıyken belgelenen komutları çalıştırmak. Cihazı buradan fiziksel olarak test edemediğim için USB yakalama henüz PASS değildir.


## 2026-10-12 — Oturum devri: yayın zamanı ≠ fiziksel ölçüm zamanı

- **Yeni araştırma hipotezi (kanıtlanmadı):** Bazı tutarsızlıklar sensör arızasından değil, PZEM paket yayın zamanını SCT/MCP örnekleme zamanıyla aynı fiziksel anmış gibi eşitlemekten kaynaklanıyor olabilir.
- PZEM yayın anı, değerlerin temsil ettiği ölçüm aralığını veya fiziksel durumu tek başına açıklamaz. İç ölçüm/güncelleme davranışı henüz doğrulanmadı.
- **Sıradaki ilk iş:** Analizörle MCP sıfırlarını incele; sıfırların kaynağını ölçmeden arıza ilan etme.
- Önce SCT/MCP ve PZEM zincirlerini ayrı ayrı değerlendir; ardından deney koşullarıyla desteklenen kararlı bölgeleri ilişkilendir. Zaman bilgisi korunsun ama tek başına eşleşme kanıtı sayılmasın.
- PZEM etiketleri akım ile birlikte V ve PF bağlamını taşısın: (I, V, PF). Benzer V/PF aynı fiziksel olay veya aynı sinyal niteliği demek değildir.
- **Kanıt sınırı:** Bu oturumda yeni donanım deneyi yapılmadı. Sensörlerin sağlam olduğu, MCP sıfırlarının nedeni veya hipotezin doğruluğu kanıtlanmış değil.
- Ayrıntı: [2026-10-12 gün sonu kaydı](HISTORY/2026/2026-10-12.md); [Elma-armut yöntem notu](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/NOTLAR/YONTEM_NOTU-ELMA-ARMUT-SAYI-NITELIK.md).


## 2026-10-12 — Aktif hedef düzeltmesi

- Önceki pusula görüntüsünde HDF-001/GRV-001 hâlâ aktif hedef gibi görünüyordu; bu, güncel çalışma durumunu yanlış yönlendiriyordu.
- **Düzeltme:** Aktif hedef HDF-002'dir. HDF-001/GRV-001 önceki çalışma geçmişidir; tekrar başa dönülmeyecek. HDF-002, önceki saplanmayı ve sıfırlama döngüsünü tekrarlamadan ölçüm karakterini öğrenmek için açılmıştır.
- MCP sıfırları varmış gibi varsayılmayacak; kullanıcı açıkça “sıfır yok” dedi. Bu akşamın planı MCP etrafında kurulmayacak.
- Bir sonraki plan HDF-002'nin gerçek durumundan ve mevcut kod/donanım kayıtlarından türetilecek.


---

## 2026-10-12 — HDF-002 güncel süreç kararı

**Aktif hedef:** [HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md)

- HDF-001/GRV-001 geçmiş tecrübesi başlangıç noktasıdır; kod ve loglar kullanılacak, aynı testler gereksiz yere tekrarlanmayacaktır.
- SCT-ESP hızlı, düzenli ve dalgayı doğru temsil eden kaliteli ham veriyi okur; ESP analiz/formül üretmez. Bias bilgisi aynı SCT ölçüm zinciriyle doğru ilişkilendirilir.
- PZEM ayrı ESP'de kendi hızında çalışır; SCT örneklemesini yavaşlatmaz.
- Her iki akış HA'da birikir. Masaüstü Python veriyi alır, Mac'teki kalıcı kopyayı doğrular ve ancak sonra HA kopyasını siler.
- Ham arşiv değişmez. Ayrı Python süreçleri aktarım/doğrulama, eş bölge işaretleme/etiketleme ve birikimli model üretme görevlerini yürütür.
- Eşleştirme zaman damgalarının birebir eşitliği değil, aynı fiziksel yük durumunu temsil eden kararlı eş bölgelerdir. Eğitimde yük geçişleri kullanılmaz. PZEM etiketi (I, V, PF) bağlamını, SCT bölgesi kendi bias bilgisini korur.
- Doğru etiketlenmiş çok sayıda farklı akım seviyesi hedeflenir. Model/formül parametreleri incelenir; uygun model sınav ESP'sine yüklenir ve PZEM ile eş bölgelerde karşılaştırılır.
- Pratik hedef yaklaşık ±%4 bağıl akım sapmasıdır; sıfıra yakın akım için mutlak hata ölçütü gerekir.
- Önce mevcut arşivdeki veriler kullanılır. Yeni fiziksel test ancak gerekli kanıt mevcut kayıtlardan elde edilemiyorsa düşünülür.

**Sıradaki tek adım:** HDF-001'deki SCT okuma kodu/loglarını yeniden test yapmadan bulup mevcut kanıtı değerlendirmek; HDF-002 veri akışı için henüz yapılmamış kurulumları başarı gibi göstermemek.

**Durum:** Hedef ve süreç tanımı plan/mimari kararıdır; deney, model veya ±%4 performans doğrulaması değildir.


---

## 2026-10-12 — Güncel yöntem ayrımı: HDF-001 donduruldu, HDF-002 etiketli veri merkezli

Bu bölüm, pusuladaki eski yöntem özetleriyle çelişirse güncel karar olarak izlenir. Önceki kayıtlar silinmez.

- **HDF-001 durumu:** Donduruldu / yarım kaldı. ESP'nin veri okuma yetenekleri için yapılan işe yarar testler ve bunlardan öğrenilenler korunur; uygun olanlar HDF-002'de yeniden kullanılır.
- **Dondurma nedeni:** MCP/SCT ölçüm zincirinin entegre/işlenmiş çıktısı ham SCT davranışıyla aynı türden veri değildir. PZEM de kendi örnekleme ve hesaplama zincirinin çıktısını verir. Bu iki çıktıyı yalnızca zaman damgalarına göre eşleştirmek, aynı fiziksel akım olayını temsil ettiklerini kanıtlamaz. Son testlerde istatistiklerin beklenen şekilde tutturulamaması, eski F(x) yaklaşımının temel varsayımını sorgulattı. Başarısız olan bütün veri okuma deneyleri değil, bu verilerden F(x)'e geçmek için kullanılan zaman merkezli eşleştirme felsefesidir.
- **HDF-002 ilk kazanımı:** Aynı fiziksel akım alanını/olayını temsil eden SCT bölgelerini PZEM'in sabit `(I, V, PF)` alanları ve deney bağlamıyla etiketlenmiş veri kümesine dönüştürmek.
- **Yeni ara Python adımı:** Etiketli veri üzerinden optimum paket/pencere/okuma adayını seçmek; sonrasında paket testlerini etiketlenmiş veriyle yürütmek.
- **Yeni sıra:** Aynı akım alanını belirle ve etiketle → optimum paket adayı seç → etiketli veride paket testleri → F(x) hesapla → hatayı ölç → iyileştir.
- **Sınırlar:** V/PF benzerliği tek başına aynı fiziksel olay kanıtı değildir; zaman damgası tek başına eşleştirme değildir; etiket güvenilir değilse zorla atanmaz. Ham veri ve eski deney kayıtları korunur.
- **Kanıt durumu:** Bu, yöntem kararıdır. Etiketli veri kümesi, optimum paket, başarılı F(x) veya ±%4 doğruluk elde edildiği iddia edilmez.
- **Ayrıntı:** [HDF-001 dondurulma gerekçesi](HEDEFLER/HDF-001-AKIMI-OKUMA/HEDEF.md) · [HDF-002 güncel yöntem kararı](HEDEFLER/HDF-002-PZEM-AMPIRIK-KALIBRASYON/HEDEF.md) · [Günlük geçmiş](HISTORY/2026/2026-10-12.md)
