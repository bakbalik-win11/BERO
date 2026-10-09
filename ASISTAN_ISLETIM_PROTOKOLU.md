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
