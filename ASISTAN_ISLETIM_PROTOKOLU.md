# BERO Asistan İşletim Protokolü

Bu belge, ChatGPT'nin Proje BERO çalışmasında kendi uygulaması gereken iş akışını tanımlar. Kullanıcının her seferinde adımları hatırlatmasına gerek bırakmamak için komutlar tetikleyici olarak ele alınır.

## Ana kural

Kullanıcı yalnızca teknik soruların yanıtlanmasını değil, projenin sürekliliğinin de korunmasını bekler. Bu nedenle aşağıdaki komutlardan biri verildiğinde ilgili kontrol listesi kendiliğinden uygulanır. Yapılmayan işlem yapılmış, doğrulanmayan sonuç doğrulanmış gibi gösterilmez.

## Tetikleyici: "ara rapor"

Kullanıcı "ara rapor" dediğinde, o ana kadarki çalışmanın ara durum kaydı hazırlanır.

1. Mevcut konuşma ve ilgili GitHub kayıtlarından en son durumu belirle.
2. Bu oturumda yapılan gerçek işlemleri, commitleri ve bağlantıları ayırarak kaydet.
3. Teknik olarak doğrulananları; yalnızca önerilen, varsayılan veya henüz test edilmemiş olanlardan ayır.
4. Aktif ana hedefi ve görevi belirle; hedef/görev durumunu güncel kayıtlarla karşılaştır.
5. Yeni kararları, gözlemleri ve öğrenilenleri eski kayıtların üzerine yazmadan ekle.
6. Gerekliyse ilgili görev raporuna tarihli ek kayıt ekle. Var olan deney raporunu sessizce değiştirme.
7. Proje pusulasındaki güncel durum, son doğrulanmış sonuç, açık sorular ve sıradaki somut adım alanlarını güncelle.
8. Kod üretildiyse, kodun sürümünü ve eşlik eden Markdown belgesini kontrol et. Kullanıcı başarılı derlemeyi onaylamadan kodu görev klasörüne taşıma.
9. Sonuçta kısa bir ara rapor ver: yapılanlar, kanıt/bağlantılar, doğrulanmış durum, açık konular ve sıradaki adım.

Ara rapor bir kapanış değildir; iş devam edebilir. Yeni bir test sonucu yoksa bunu açıkça belirt.

## Tetikleyici: "günü kapa"

Kullanıcı "günü kapa" dediğinde, gün sonu devri yapılır. Bu komut, "ara rapor" kontrol listesinin tamamını da içerir ve ek olarak aşağıdaki adımları zorunlu kılar:

1. Gün içindeki çalışma izini toparla: hangi hedef/görev üzerinde çalışıldı, hangi dosyalar değişti ve hangi commitler oluştu?
2. Ana hedefin ve aktif görevin durumunu güncelle; görev tamamlanmadıysa tamamlanmış gibi işaretleme.
3. O gün alınan önemli kararları tarihli karar kronolojisine ekle. Önceki kararları silme veya sessizce yeniden yazma.
4. Öğrenilenleri, başarısız denemeleri ve belirsizlikleri kaydet; başarısız testleri de bilgi olarak koru.
5. Proje pusulasındaki "son tamamlanan iş", "son doğrulanmış durum", "açık soru" ve "sıradaki tek adım" alanlarını yeni oturuma hazır hale getir.
6. Günlük kayıt klasörü/formatı zaten tanımlıysa oraya tarihli kayıt ekle; tanımlı değilse yeni bir günlük yapı icat etmek yerine ana pusulanın kronolojisine ve ilgili görev raporuna ekle.
7. Yapılan dosya değişikliklerini GitHub'dan doğrula ve linklerini kaydet. Araç hatası veya başarısız kayıt varsa bunu açıkça bildir; kaydedilmiş gibi davranma.
8. Kapanış özetini ver: günün kazanımı, doğrulananlar, açık kalanlar, en son güvenilir durum ve bir sonraki oturumun ilk adımı.

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
