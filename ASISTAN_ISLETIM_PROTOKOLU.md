# BERO Asistan İşletim Protokolü

Bu belge, ChatGPT'nin Proje BERO çalışmasında kendi uygulaması gereken iş akışını tanımlar. Kullanıcının her seferinde adımları hatırlatmasına gerek bırakmamak için komutlar tetikleyici olarak ele alınır.

## Ana kural

Kullanıcı yalnızca teknik soruların yanıtlanmasını değil, projenin sürekliliğinin de korunmasını bekler. Bu nedenle aşağıdaki komutlardan biri verildiğinde ilgili kontrol listesi kendiliğinden uygulanır. Yapılmayan işlem yapılmış, doğrulanmayan sonuç doğrulanmış gibi gösterilmez.

## TODO fikir havuzu kullanımı

TODO listesi [TODO/README.md](TODO/README.md) dosyasında tutulur. Bu liste resmî görevlerin yerine geçmez; henüz görev açılmamış fikirleri ve küçük yapılacakları yakalar.

- Kullanıcı açıkça bir fikri TODO'ya eklememizi istediğinde maddeyi listeye kaydet.
- Kullanıcı “bunu TODO'ya at”, “aklımıza yaz” veya benzer net bir kayıt isteği verdiğinde fikir maddesini ekle.
- Her yeni maddeyi **Açık fikirler** bölümünün en üstüne ekle; ilk kayıt tarihini koru.
- Her bölüm kendi içinde yeniden eskiye değil, **yeniden eskiye sıralanır**: en yeni kayıt bölümün en üstündedir.
- Madde durumunu açıkça yönet: `Bekliyor`, `Göreve dönüştü — görev açık`, `Tamamlandı`, `Vazgeçildi` veya `Görev tamamlandı`.
- `[ ]` sonuçlanmamış madde demektir; `[x]` fikir kaydının sonucu belli olup kapandığını gösterir. Tikin anlamı teknik başarı değildir; sonuç ayrıca yazılır.
- Normal fikir tamamlandığında `[x]`, sonuç ve sonuç tarihi eklenir; madde **Sonuçlananlar** bölümünün en üstüne taşınır.
- Fikirden vazgeçilirse madde silinmez: `[x]`, `Sonuç: Vazgeçildi`, tarih ve gerekçe eklenir; **Sonuçlananlar** bölümünün en üstüne taşınır.
- Fikir resmî göreve dönüştürülünce görev kimliği ve bağlantısını ekle, maddeyi **Göreve dönüşenler — açık görevler** bölümüne taşı; ancak `[ ]` bırak. “Göreve dönüştü” bir ara durumdur, kapanış değildir.
- **Göreve dönüşen TODO maddesi, bağlı resmî görev tamamlanana kadar açık kalır.** Görev tamamlandığı doğrulanınca `[x]`, `Sonuç: Görev tamamlandı` ve sonuç tarihi eklenir; ardından **Sonuçlananlar** bölümüne taşınır.
- Görev açılması tek başına tamamlanma kanıtı değildir. Görev bağlantısı veya tamamlanma durumu bilinmiyorsa tahmin etme; açık bırak ve sor.
- İlk kayıt tarihi hiçbir zaman değiştirilmez. Tarih güvenilir biçimde bilinmiyorsa uydurma.
- Fikir konuşmada geçti diye otomatik olarak göreve dönüştürme; kullanıcı açıkça TODO'ya kayıt talep etmediyse bağlama göre karar ver veya gerektiğinde sor.
- Ara rapor ve günü kapa sırasında bu oturumda eklenen, tamamlanan, vazgeçilen veya göreve dönüşen maddeleri kontrol et; durumlarını ve bağlantılarını doğru kaydet.

## Günlük kontrol listesi — zorunlu takip

Günlük tik listesi `GUNLUK/YYYY/YYYY-MM-DD.md` altında tutulur; dizin ve otomatik günlük dosyası oluşturma kuralı [GUNLUK/README.md](GUNLUK/README.md) içindedir.

- “Ara rapor” ve “günü kapa” tetiklenince bugünün günlük kontrol listesini aç/oluştur ve kontrol et.
- Yalnızca gerçekten tamamlanan adımları `[x]` yap. Yapılmayan, atlanan veya doğrulanamayan adımlar `[ ]` kalır; kullanıcıya yapılmış gibi sunulmaz.
- Fikir göreve dönüştüğünde aynı iş akışında TODO kaydını “Göreve dönüşenler — açık görevler” bölümüne taşı, `[ ]` olarak bırak, görev kimliği/linki ekle; günlük listede fikir→görev kaydı kutusunu ancak bu kayıtlar yazılıp doğrulandıktan sonra işaretle.
- Ara rapor/günü kapa sırasında HISTORY girdisi, görev raporu eki, pusula ve TODO durumu kontrol edilir. İlgili günlük kutuları ancak her bir kayıt başarıyla yazılıp geri okunarak doğrulanınca işaretlenir.
- Gün sonu listesi teknik görevin kapandığı anlamına gelmez. Teknik deney yapılmadıysa deney kutusu açık kalır; teknik sonuç yoksa özet bunu açıkça söyler.
- Günlük dosyaları eklemeli korunur; var olan aynı tarihli dosyanın üzerine otomasyonla yazılmaz.
- Rutin takip asistanın sorumluluğudur: günlük dosyayı açmak/oluşturmak, yeni tarihli dosyanın indeks bağlantısını kontrol etmek, TODO→görev geçişini kaydetmek, kutuları yalnızca doğrulanmış işlemler için işaretlemek ve GitHub yazımlarını geri okumak.
- Kullanıcıdan yalnızca teknik kanıt/karar gerekir: gerçek deney koşulları ve ham ölçümler/loglar, derleme sonucu, gerektiğinde donanım veya çalışan yapılandırma değişikliği için açık onay. Kullanıcıdan günlük kayıtları elle yönetmesi veya her adımı hatırlatması beklenmez.
- Otomasyonun dosyası repoda bulunması çalıştığının kanıtı değildir. İlk başarılı Actions çalıştırması görülene kadar durum “kuruldu, çalışması bekleniyor” olarak belirtilir.

## Tetikleyici: "ara rapor"

Kullanıcı "ara rapor" dediğinde, o ana kadarki çalışmanın ara durum kaydı hazırlanır.

1. Mevcut konuşma ve ilgili GitHub kayıtlarından en son durumu belirle.
2. Bu oturumda yapılan gerçek işlemleri, commitleri ve bağlantıları ayırarak kaydet.
3. Teknik olarak doğrulananları; yalnızca önerilen, varsayılan veya henüz test edilmemiş olanlardan ayır.
4. Aktif ana hedefi ve görevi belirle; hedef/görev durumunu güncel kayıtlarla karşılaştır.
5. Yeni kararları, gözlemleri ve öğrenilenleri eski kayıtların üzerine yazmadan ekle.
6. HISTORY/YYYY/YYYY-MM-DD.md dosyasını kontrol et; yoksa oluştur, varsa önceki kayıtları koruyarak yeni saatli bir ara rapor girdisi ekle.
7. İlgili görev raporuna gerekli tarihli ek kaydı ekle; var olan deney raporunu sessizce değiştirme.
8. Proje pusulasındaki güncel durum, son doğrulanmış sonuç, açık sorular ve sıradaki somut adım alanlarını güncelle.
9. Kod üretildiyse, kod sürümünü ve eşlik eden Markdown belgesini kontrol et. Kullanıcı başarılı derlemeyi onaylamadan kodu görev klasörüne taşıma.
10. Sonuçta kısa bir ara rapor ver: yapılanlar, günlük kayıt bağlantısı, doğrulanmış durum, açık konular ve sıradaki adım.

Ara rapor bir kapanış değildir; iş devam edebilir. Yeni bir test sonucu yoksa bunu açıkça belirt.

## Tetikleyici: "günü kapa"

Kullanıcı "günü kapa" dediğinde, gün sonu devri yapılır. Bu komut, "ara rapor" kontrol listesinin tamamını da içerir ve ek olarak aşağıdaki adımları zorunlu kılar:

1. Gün içindeki çalışma izini toparla: hangi hedef/görev üzerinde çalışıldı, hangi dosyalar değişti ve hangi commitler oluştu?
2. Ana hedefin ve aktif görevin durumunu güncelle; görev tamamlanmadıysa tamamlanmış gibi işaretleme.
3. O gün alınan önemli kararları tarihli karar kronolojisine ekle. Önceki kararları silme veya sessizce yeniden yazma.
4. Öğrenilenleri, başarısız denemeleri ve belirsizlikleri kaydet; başarısız testleri de bilgi olarak koru.
5. Proje pusulasındaki "son tamamlanan iş", "son doğrulanmış durum", "açık soru" ve "sıradaki tek adım" alanlarını yeni oturuma hazır hale getir.
6. HISTORY/YYYY/YYYY-MM-DD.md dosyasına gün sonu girdisi ekle. Dosya varsa önceki girdileri silme veya yeniden yazma; aynı günün yeni kapanışını yeni saatli bölüm olarak ekle.
7. Proje pusulasındaki devir alanlarını güncelle ve günlük geçmiş dosyasına bağlantı ver.
8. Yapılan dosya değişikliklerini GitHub'dan doğrula ve linklerini kaydet. Araç hatası veya başarısız kayıt varsa bunu açıkça bildir; kaydedilmiş gibi davranma.
9. Kapanış özetini ver: günün kazanımı, doğrulananlar, açık kalanlar, en son güvenilir durum, günlük kayıt bağlantısı ve bir sonraki oturumun ilk adımı.

"Günü kapa" komutu teknik hedefi otomatik olarak kapatmaz; yalnızca çalışma gününü ve oturum devrini kapatır. Ana hedef/görev ancak kendi başarı ölçütleri ve kanıtlarıyla kapatılır.

## Kayıt ve sürümleme güvenceleri

- Deney raporları, ham loglar, ölçümler ve kod sürümleri üzerine sessizce yazılmaz.
- Yeni sonuçlar tarihli ek kayıt veya yeni sürüm olarak eklenir.
- Yapısal README/politika belgeleri, yapıyı açıklamak için güncellenebilir.
- Kodun her sürümünün yanında, hedefi, donanımı, sürüm işlevini, test koşullarını, doğrulananları, loglardan öğrenilenleri, doğrulanmamış noktaları ve sonraki adımı açıklayan bir .md belgesi bulunur.
- Kullanıcının kimlik/isim ve çalışan donanım yapılandırması onay olmadan değiştirilmez.
- Ölçüm kanıtı olmayan teknik başarı iddia edilmez.
- Kod derleme gerektiriyorsa, kullanıcının derleme başarısı onaylanmadan görev arşivine taşınmaz.
- Pusula bir özet/indeks; ayrıntılı görev raporları ve kod belgeleri ise kaynak kayıtlardır. Pusula kaynak kayıtların yerine geçmez.

## Tetikleyici eşleştirmesi

Aşağıdaki ifadeler aynı iş akışını başlatır:

- **Ara rapor:** "ara rapor", "ara durum", "buraya kadar raporla".
- **Günü kapa:** "günü kapa", "bugünlük kapatalım", "oturumu kapat".

Kullanıcı açıkça daha dar bir kapsam belirtirse, o kapsam uygulanır; ancak kayıtları koruma ve doğruluk kuralları değişmez.

## Zorunlu tarihli geçmiş kaydı

**"Ara rapor" ve "günü kapa" komutlarının ikisinde de HISTORY günlüğüne yazmak zorunludur.** Bu işlem yalnızca pusulayı güncellemekle karşılanmış sayılmaz. Her girdide tarih/saat (saat güvenilir biçimde bilinmiyorsa yalnızca tarih), hedef/görev kimliği, yapılan iş, değişen dosyalar ve commit bağlantıları, doğrulananlar, açık kalanlar ve sıradaki adım bulunur. Günlük dosyası yoksa oluşturulur; varsa eski içerik korunur ve yeni bölüm eklenir. Günlük kaydı GitHub'a başarıyla yazılamazsa kullanıcıya açıkça söylenir.

## HISTORY sıralama kuralı

HISTORY günlüklerinde **en yeni kayıt en üstte** olmalıdır. Ara rapor veya gün sonu kaydı eklendiğinde yeni bölüm mevcut dosyanın başına eklenir; önceki kayıtlar aşağıda ve değişmeden kalır. HISTORY/README.md içindeki günlük listesi de en yeni tarihten eskiye doğru sıralanır. Kullanıcı geçmişe gitmek isterse aşağı doğru ilerler; güncel kaydı bulmak için dosyanın sonuna inmek zorunda kalmaz.

## Kalıcı ilkeleri yakalama ve uygulama — zorunlu

Sohbette yeni bir çalışma ilkesi, karar veya tekrar kullanılabilir teknik ders ortaya çıktığında, bunu yalnızca konuşmada bırakma.

1. **Sınıflandır:** Genel ve kalıcı çalışma ilkesi ise `README.md` içindeki BERO çalışma prensiplerine; kayıt/sürümleme kuralı ise `KAYIT_VE_SUREKLILIK.md` dosyasına; asistanın yapacağı iş akışı ise bu protokole; tarihsel karar ise `HISTORY/YYYY/YYYY-MM-DD.md` dosyasına işle. Aynı ilkeyi gereksiz yere her belgeye kopyalama; ana kuralı bir yerde tanımla ve diğer belgelerden bağlantı ver.
2. **Operasyonelleştir:** İlkeyi uygulamak için hangi somut adımın gerektiğini ve hangi kanıtla tamamlandığını yaz. Yalnızca “dikkat et” gibi soyut bir notla yetinme.
3. **Bağlantı kur:** İlgili ana hedef, görev raporu, deney kaydı, donanım/sensör notu ve kod sürümü arasında bağlantı ver.
4. **Eski kaydı koru:** Tarihsel kayıtların üzerine yazma. Yapısal/politika belgeleri güncellenebilir; geçmiş deney, karar ve kanıtlar tarihli ek kayıtlarla korunur.
5. **Doğrula:** GitHub'a yazdıktan sonra ilgili dosyayı geri oku; yazım doğrulanmadan işi tamamlandı diye bildirme.
6. **Özetle:** Kullanıcıya yeni ilkenin hangi kalıcı kayda işlendiğini ve uygulamada neyi değiştireceğini kısaca bildir.

## Görev basamakları, teknik dersler ve donanım kütüphanesi

- Büyük görev içindeki anlamlı basamaklar görev raporunda tarihli ve kronolojik olarak izlenir. Her küçük işlem ayrı resmî görev olmak zorunda değildir.
- Basamak değiştiğinde önceki basamağın sonucu, kanıtı, kullanılan kod sürümü ve açık soruları kaybolmadan rapora eklenir.
- Görevde öğrenilen ve başka görevlerde de işe yarayabilecek donanım/sensör bilgisi, ilgili donanımın kalıcı Markdown notuna aktarılır; görev raporu kaynak deney ve kanıta bağlantı verir.
- Donanım notuna aktarılmış olmak, bilginin otomatik olarak doğrulanmış olduğu anlamına gelmez. Her bilgi `öneri`, `gözlem`, `koşullu doğrulandı` veya `doğrulandı` gibi açık durum ve koşullarla etiketlenir.
- Doğrulanmış kodlar tek bir “son kod” dosyasında birleştirilmez. Her sürüm kendi kodu, eşlik eden MD belgesi, donanım/yazılım koşulları, test kanıtı ve sınırlarıyla ayrı saklanır. Önceki sürüm korunur.
- Derleme doğrulaması, gerçek donanım testi ve ölçüm doğrulaması ayrı kanıt türleridir; biri diğerinin yerine geçmez.
- Bir teknik kural başka donanım/model için de geçerli görünüyorsa, kapsamı ayrı test edilene kadar genelleme yapma. Örneğin ortak yazılım bileşeni kullanılması iki ADC'nin tüm davranışlarının aynı olduğunu kanıtlamaz.

## Tetikleyici: işe başlama veya aradan sonra depoya dönüş — zorunlu

Kullanıcı yeni bir çalışma gününe başlarken, aynı gün içinde ara verip geri döndüğünde veya yeni sohbet/oturumda BERO işine devam ettiğinde, teknik işe geçmeden önce bu başlangıç zincirini uygula. Kullanıcının “başlayalım”, “devam edelim”, “depoya döndüm” gibi ifadeleri tetikleyicidir; açıkça “önceki kayıtlara bakma” derse bu istek kapsamı değiştirebilir.

1. [Proje Pusulası](PROJE_PUSULASI.md) dosyasını oku: son tamamlanan iş, son doğrulanmış durum, açık sorular ve sıradaki somut adım.
2. [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) içinden çalışılacak konuya uygulanacak kuralları kontrol et.
3. Aktif ana hedefi ve görev raporunu oku; son görev basamağını, açık işleri ve varsa tarihli ek kayıtları kontrol et.
4. İlgili kod/MD, donanım veya sensör notları, deney raporları ve son HISTORY kayıtlarını oku. Yeni teknik konuya geçiliyorsa ilgili bileşenin kalıcı bilgisini de ara.
5. Günlük kontrol listesini kontrol et; gün değiştiyse doğru tarihli dosyayı ve indeksini doğrula. Otomasyonun gerçekten çalıştığı kanıtlanmadıysa çalışıyor varsayma.
6. Konuşmada daha önce kabul edilmiş ama henüz kalıcı kayda işlenmemiş ilke/karar varsa, uygun belgeye işle; gerekiyorsa kullanıcıdan kararın kapsamını netleştir.
7. Kayıtlar arasında çelişki varsa sessizce seçim yapma: çelişkiyi belirt, daha yeni ve doğrulanmış kanıtı ayırt et, gerekiyorsa kullanıcıya sor.
8. Kullanıcıya kısa bir “devam bağlamı” sun: mevcut basamak, son doğrulanmış sonuç, açık soru ve sıradaki tek somut adım. Sonra teknik çalışmaya başla.

**Bu zincir yalnızca yeni gün açılışında değil, her ara dönüşte de uygulanır.** Önceki oturumun bağlamı otomatik olarak hâlâ geçerli varsayılmaz. Bu prosedürün amacı, kayıtları okumadan ileri atlama ve daha önce belirlenmiş ilkeleri unutma riskini azaltmaktır.

