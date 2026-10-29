# Proje İlkeleri

## Mükemmel akım hedef değil

Bu projede hedef ilk günden kusursuz akım ölçümü değildir. Sistem zamanla, deneylerden ve kaydedilen sonuçlardan öğrenerek iyileştirilecektir.

- İlk sürüm yeterince işe yarıyorsa akım hesaplamaya ve sonuçları kaydetmeye devam et.
- Sistemin doğruluğunu henüz yeterli bulmamak, akım hesaplamayı veya gelişimi izlemeyi durdurma gerekçesi değildir.
- Her sürümde elde edilen ölçümleri, hata ve sınırlamaları açıkça kaydet; daha sonra karşılaştırılabilir bir başlangıç noktası bırak.
- İyileştirmeleri aşamalı yap. Kusursuzluk şartı uydurarak ilerlemeyi bloke etme.
- Sonuçları olduğundan iyi gösterme: mevcut doğruluk ve belirsizlik neyse onu belirt.

**Çalışma kuralı:** Akım hesapla, sonucu kaydet, mevcut sınırları belirt ve zaman içindeki gelişimi ölç. Mükemmellik değil, izlenebilir ilerleme hedeflenir.

## Kullanıcı beyanı ve tamamlanmış işler

Kullanıcı bir işi yaptığını, kontrol ettiğini veya test ettiğini açıkça söylüyorsa, proje kaydında o iş **yapılmış/tamamlanmış kabul edilir**. Her defasında kuşkucu bir dille “yalnızca beyan edildi” diye yazıp yapılmamış veya güvenilmezmiş izlenimi verme.

- Kullanıcının bildirdiği işin sonucu ve ilgili kapsam, uygun dosyaya doğrudan kaydedilir; tamamlanma durumu bu bilgiye göre güncellenir.
- Kullanıcının yaptığı işi asistanın bağımsız olarak ölçmediği veya görmediği durumlarda, bağımsız doğrulama yapıldığı da iddia edilmez. Bu ayrım, kullanıcının sözüne güvensizlik anlamına gelmez; yalnızca kimin hangi işlemi yaptığına dair doğru kayıt tutar.
- Ek doğrulama yalnız somut bir çelişki, güvenlik gereği veya görevin açık kabul ölçütü bunu gerektiriyorsa istenir. Kullanıcıdan aynı işi tekrar yapması rutin olarak istenmez.
- Kullanıcının açıkça tamamlandı dediği bir işi sırf asistanın kendi gözlemi yok diye yeniden açma.

**Kısa kural:** Kullanıcının açık beyanını esas al; işi tamamlanmış kaydet, yapılmamış bağımsız doğrulamayı ise yapılmış gibi gösterme.

## Her oturumda depoya kayıt

Bazı oturumlar fiziksel test ve ölçüm, bazıları mimari/yol belirleme, bazıları analiz veya sonuç değerlendirme için olabilir. Oturumun türü değişse de proje bilgisini depoda koruma işi devam eder.

- Test yapıldıysa: koşulları, elde edilen veriyi/sonucu, görülen sorunu ve öğrenileni kaydet.
- Yol veya mimari belirlendiyse: kararı, gerekçesini ve açık kalan noktaları kaydet.
- Bir fikir ortaya çıktıysa: fikir havuzuna ekle; önceliği kendiliğinden varsayma.
- Bir iş yapılacak hale geldiyse: görev listesine al ve durumunu doğru göster.
- Henüz uygulanmayan veya doğrulanmayan şeyi tamamlanmış gibi yazma.
- Her depoya yazma işleminden sonra dosyayı yeniden okuyarak kaydın gerçekten oluştuğunu kontrol et. Başarısız olursa bunu açıkça bildir; kaydedildiğini söyleme.

**Kısa kural:** Test günü de, planlama günü de, analiz günü de — ortaya çıkan bilgi depoya işlenir.

## Anlık kayıt ve gün sonu süreklilik kontrolü

Depoya kayıt yapmak için gün sonu beklenmez. Sohbette yeni bir hedef, karar, fikir, görev, test sonucu veya öğrenim ortaya çıktığında uygun depodaki kayıt aynı çalışma akışı içinde güncellenir.

- Anlık kayıt: yeni bilgi geldiğinde uygun mimari, fikir havuzu, görev kartı, durum veya sonuç belgesi güncellenir; yazma işlemi ardından dosya yeniden okunarak doğrulanır.
- Gün sonu kontrolü: anlık kayıtların yerine geçmez. Gün sonunda belgeler arası süreklilik gözden geçirilir; durumlar, görev bağlantıları, açık kalan işler ve sonuç kayıtları birbiriyle tutarlı hale getirilir.
- Kayıt başarısız olursa başarısızlık açıkça bildirilir; bilgi sessizce bekletilmez ve kaydedilmiş gibi gösterilmez.
- Kullanıcı, anlık kayıt için beklemeye razıdır; hız uğruna kayıt ve doğrulama adımları atlanmaz.

**Kısa kural:** Gelişme olur olmaz depoya işle; gün sonunda sürekliliği kontrol et.

## Öncelik: İstenen kaydı gerçekten yapmak

Kullanıcı bir bilginin depoya kaydedilmesini istediğinde, öncelik açıklama veya yeni kural yazmak değil, istenen kaydı fiilen yapmaktır.

- Bilgiyi uygun mevcut dosyaya ekle veya güncelle; gereksiz yeni belge ve süreç üretme.
- Yazma işleminden sonra dosyayı yeniden oku ve kaydın bulunduğunu doğrula.
- Başarısız olursa net biçimde bildir; kayıt yapılmış gibi konuşma.
- Kullanıcının güveni, uzun vaatlerle değil istenen kayıtların doğru ve doğrulanabilir biçimde yapılmasıyla kazanılır.


## Deney kodu koşulsuz açıklanmalı
BERO'da deney kodu/firmware'i, hangi deneyin hangi koşullarını uyguladığını kendi içinde açıklamalıdır. Her deneyin planlanan koşulları açıklamalı YAML dosyasında tutulur; kodun başında deney kimliği, amacı, bağlantı/koşul varsayımları ve kullanılan ayarlar belirtilir. Kod YAML dosyasını otomatik okumuyorsa bu açıkça yazılır. Planlanan ve gerçekten kullanılan değerler ayrılır; bilinmeyen değerler tahmin edilmez.

Her anlamlı adımda **HEDEF / LOG / SONUÇ** kaydı zorunludur. Bu kural kullanıcı tekrar hatırlatmasa da uygulanır. YAML, kod açıklamaları, protokol, sonuç kaydı ve oturum günlüğü birbiriyle tutarlı olmalı; değişiklik sonrası dosyalar yeniden okunarak doğrulanmalıdır. Bu gereklilik atlanmışsa iş tamamlanmış sayılmaz.
