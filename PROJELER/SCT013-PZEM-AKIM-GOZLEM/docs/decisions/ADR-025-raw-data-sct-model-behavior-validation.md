# ADR-025 — Ham verinin PZEM geçiş okumalarından bağımsız SCT model değerlendirmesi

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — kullanıcı mimari açıklaması
- **İlişkili kararlar:** ADR-010, ADR-022, ADR-024
- **Kapsam:** Kararlı yük verisiyle katsayı/model öğrenimi ve aynı deneyin ham kaydında bağımsız SCT davranış değerlendirmesi

## Bağlam

Eğitim aşamasında sabit yük deneylerinden elde edilen PZEM ve SCT kayıtları kullanılır. Her iki akış kendi içinde değerlendirilir; **yalnız ON (yük açık) dönemindeki uygun kararlı alanlar** eşleştirilerek PZEM akımı SCT eğitim penceresine referans etiketi olur. **OFF/kapalı alanlar hiçbir zaman eğitim verisi veya SCT–PZEM eşleştirme adayı değildir.** OFF olayı ON paketini kapatır; ilk aşamada OFF durumu sıfır/kapalı kabul edilir. Bu aşama katsayı veya katsayı/alan modeli üretmek içindir.

Ancak deneyin ham kaydı yalnızca eğitimde seçilen kararlı alanlardan ibaret değildir. Açılma, kapanma ve geçiş bölgeleri de dahil olmak üzere ham veri korunur. PZEM, yük geçişlerinde kendi güncelleme/ölçüm davranışı nedeniyle örneğin 0,8 → 0,6 → 0,8 → 1,0 A gibi değişken okumalar gösterebilir. Bu geçiş okumaları, her anın kesin akım gerçeği veya SCT modelini değerlendirmek için noktasal referans kabul edilmez.

## Karar

1. **Ham kayıt korunur.** Eğitim için kararlı alanlar seçilse bile deneyin geri kalan ham verisi silinmez veya eğitim dışı diye değersiz sayılmaz. Ancak ham kaydın korunması, OFF alanlarının eğitim verisine alınacağı anlamına gelmez.
2. **Öğrenme ve tam kayıt değerlendirmesi ayrı işlemlerdir.** Önce eşleştirilmiş kararlı SCT/PZEM alanlarından katsayı veya alan bazlı model öğrenilir. Daha sonra öğrenilmiş model aynı deneyin tam ham SCT kaydına, açılma/kapanma/geçişler dahil uygulanarak incelenir.
3. **Tam kayıt değerlendirmesinde PZEM geçiş örnekleri noktasal doğruluk referansı değildir.** PZEM'in geçişteki anlık/ardışık okumalarıyla SCT'nin her örneğini birebir karşılaştırıp hata veya başarı puanı üretmek, PZEM'in geçiş davranışını doğruluk ölçütü haline getirir; bu yöntem kabul edilmez.
4. **Python'a deneyin bilinen yük koşulu verilir.** Öğrenilmiş modelin tam ham kayıtta ON/OFF davranışı ve geçişleri incelenebilir. Bu, OFF alanlarını eğitim örneği yapmaz: eğitim yalnız ON içindeki kararlı SCT/PZEM örtüşmesinden oluşur; OFF yalnız olay paketini kapatır ve ilk aşamada sıfır/kapalı kabul edilir. Tam kayıt değerlendirmesinde modelin OFF tepkisi, ON algısı ve geçiş davranışı gözlenebilir. Bu değerlendirme PZEM'in geçiş okumalarını yeniden referans yapmaz.
5. **Bilinen deney koşulu, örnek başına gerçek akım dalga şekli anlamına gelmez.** Yükün açık/kapalı bilgisi veya nominal/önceden belirlenmiş akım aralığı, her ara örneğin kesin amper değerini vermez. Python raporu bu sınırı korur; bilinmeyen ara akım değerlerini uydurmaz.
6. **PZEM'in rolü ortadan kalkmaz.** PZEM, öğrenme için eşleştirilmiş kararlı alanlarda proje referansıdır. Yalnızca sonradan tam ham kayıt üzerinde yapılan geçiş/ON-OFF davranış değerlendirmesinde PZEM'in geçiş okumaları doğruluk hakemi olarak tekrar kullanılmaz.
7. **Model alanları veriden seçilebilir.** Tek katsayı veya birden fazla akım alanı/katsayı kullanımı (ör. düşük, orta, yüksek aralıklar) önceden sabitlenmez. Python, yeterli veri ve ayrılmış değerlendirme sonuçlarıyla alan ihtiyacını inceleyebilir; alan sınırları kanıt olmadan belirlenmez.
8. **Başarım dili doğru seçilir.** Bu tam kayıt incelemesi, bilinen deney koşullarına karşı SCT modelinin davranış/tutarlılık değerlendirmesidir. Örnek başına bağımsız, izlenebilir akım referansı bulunmadıkça mutlak doğruluk veya gerçek dalga şekli doğrulaması olarak adlandırılmaz.

## OFF verisinin gelecekteki ayrı kullanım alanı — gürültü/kapalı durum modeli

OFF örnekleri ON akım kalibrasyonuna veya PZEM–SCT kararlı yük eşleştirmesine katılmaz. Bununla birlikte, farklı deneylerde zaman içinde biriken OFF okumaları kaybolmayacak; ayrı etiketli bir OFF/yüksüz veri havuzunda birleştirilebilir. Bu havuz ileride gürültü tabanını tanımlamak ve "bu aralık gürültü/kapalı durumdur" sınıflandırması için eşik veya ayrı bir model geliştirmek amacıyla kullanılabilir.

Gerekirse bu amaç için ayrıca aç-kapa döngüsü çalıştırmadan, ölçülen hatta yük bağlı değilken uzun süreli yüksüz kayıt alınır. Böylece doğal yüksüz taban dağılımı daha temiz incelenebilir. Bu, ilk aşamanın hedefi değildir ve ON akım doğruluğu çalışmasının yerine geçmez.

İleriye dönük mimari fikir: Python tarafında biriken verilerle geliştirilen model/eşik, ileride ölçümü sahada yapan ve sınıflandırma/akım hesabı gerçekleştiren ESP'ye aktarılabilir. ESP'nin model yükleme, güncelleme ve çalışma biçimi henüz tasarlanmış veya uygulanmış değildir; bu bir gelecek hedefidir.

## Örnek

Nominal olarak yaklaşık 1 A çeken sabit bir yükün açılıp kapatıldığı bir deneyde:
- PZEM/SCT kararlı alan eşleşmeleri katsayı öğrenmek için kullanılır.
- Öğrenilen katsayı/model tam SCT ham kaydına uygulanır.
- Python, deneyin kapalı/açık durumlarını ve bilinen 0–yaklaşık 1 A yük aralığını kullanarak SCT'nin OFF tabanını, ON seviyesini ve geçiş davranışını inceler.
- PZEM'in geçiş sırasında verdiği 0,8 / 0,6 / 0,8 / 1,0 A gibi ardışık okumalar SCT'nin her örneği için referans kabul edilmez.

## Kapsam dışı / henüz kararlaştırılmayanlar

- Python algoritması, regresyon/en küçük kareler yöntemi, hata fonksiyonu veya kabul eşikleri bu ADR ile seçilmemiştir.
- Katsayıların tek model mi, alan bazlı modeller mi olacağı gerçek veri analizine bırakılmıştır.
- Modül 4 olarak eğitilmiş modeli ayrı SCT üzerinde çalıştırma fikri olası sonraki aşamadır; bu ADR ile donanım görevi veya kabul kararı haline getirilmemiştir.
- Bu kayıt Python kodunun yazıldığı, model üretildiği veya deney sonucunun doğrulandığı anlamına gelmez.

## Uygulama ve doğrulama durumu

Bu ADR mimari/değerlendirme kuralını kaydeder. Python uygulaması, gerçek ham kayıt üzerinde model çalıştırma, örnek çıktı/log ve başarı ölçütü henüz oluşturulmamıştır.


## 2026-11-05 — Ayrı yüksüz/gürültü veri havuzu için kullanıcı talimatı

Bir sonraki çalışma oturumunun **ilk adımı**, kullanıcıdan bu gece alınan sistem yüksüz Home Assistant History CSV kaydını istemektir. Kullanıcı dosyayı sağlayacaktır. Bu kayıt, ON akım kalibrasyonundan ayrı bir yüksüz/gürültü veri havuzunun ilk girdisi olarak analiz edilecektir. Her yeni yüksüz kayıt ayrı ayrı değerlendirilecek, sonuçlar zaman içinde aynı havuzda biriktirilerek gürültü dağılımının oturumlar arası değişimi izlenecektir.

### Kanal ve fiziksel tur bilgisi
- SCT1 / sarı / GPIO32: fiziksel tek geçiş (1T); YAML/entity adında 2T ifadesi kalmış olabilir.
- SCT2 / yeşil / GPIO33: nötr hattında 4 geçiş (4T).
- SCT3 / mavi / GPIO34: faz hattında 3 geçiş (3T).
- GPIO35: ortak bias.

Tur sayısına bölerek yaklaşık normalize edilmiş bir gürültü karşılaştırması yapılabilir; ancak bu işlem kesin eşdeğerlik sağlamaz. Kanalın fiziksel yerleşimi, hat/faz-nötr konumu, sensör ve analog yol kazancı, K katsayısı ve örnekleme etkileri farklı olabilir. Bu nedenle her raporda ham kanal dağılımı (medyan, üst yüzdelikler/P95-P99, maksimum, saçılım ve zaman davranışı) korunmalı; tur-normalize değer yalnız ek karşılaştırma olarak sunulmalıdır. Bir kanaldaki en yüksek okumanın tek başına eşik seçimi için yeterli olmadığı, tekrar eden oturumların dağılımıyla birlikte değerlendirilmesi gerektiği not edilir.

Bu havuz ON kararlı alan kalibrasyonuna veya PZEM–SCT ON eşleştirmesine katılmaz. Hedef, sistem yüksüzken görülen taban/gürültü alanını ve oturumlar arası değişimini tanımak; daha sonra kapalı durum eşiği veya ayrı OFF sınıflandırıcısı için veri sağlamaktır. Henüz eşik/model belirlenmemiştir.
