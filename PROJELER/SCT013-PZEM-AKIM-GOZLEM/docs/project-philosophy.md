# BERO proje felsefesi: kişisel veri kümesi, öğrenme ve kabul edilebilir sınırlar

## Amaç

BERO, piyasaya sürülecek evrensel bir akım ölçer veya laboratuvar referans cihazı geliştirme projesi değildir. Amaç, evde bulunan sınırlı sayıdaki elektrikli aygıt ve karşılaşılan yüklerden zaman içinde veri toplayarak bu veri kümesine giderek daha iyi uyum sağlayan bir model geliştirmektir.

Modelin öncelikli kullanım alanı, projenin gözlemlediği ev içi aygıtlar ve koşullardır. Her olası yükte çalışması, tüm akım aralığını kapsaması veya hiç görülmemiş yüklerde genelleme garantisi vermesi proje hedefi değildir.

## Birleşik ve büyüyen veri kümesi

Yeni kayıtlar geldikçe veri kümesi büyür. Önceki ham kayıtlar, etiketler, analiz sonuçları ve model sürümleri izlenebilir biçimde korunur. Yeni veriler mevcut veri kümesine eklenebilir; model yeniden eğitilebilir ve yeni katsayılar/model sürümleri üretilebilir.

Modelin kendi eğitim kümesinde çok iyi, hatta kusursuza yakın sonuç vermesi tek başına bir kusur sayılmaz. Bu projede aşırı öğrenme (overfitting), ticari bir ürün için olduğu gibi otomatik bir başarısızlık ölçütü değildir. Modelin gözlenen ev içi veri kümesini iyi öğrenmesi istenen bir sonuç olabilir.

Bununla birlikte raporlar neyin ölçüldüğünü açıkça ayırmalıdır:
- **Eğitim kümesi sonucu:** Modelin öğrendiği etiketli kayıtlarla ne kadar uyumlu olduğu.
- **Birleşik veri kümesi sonucu:** Belirtilen model sürümünün mevcut etiketli kayıtların tümündeki sonucu.
- **Yeni/ayrılmış kayıt sonucu:** Eğitimde kullanılmamış kayıt varsa, modelin bu kayıtlar üzerindeki sonucu.
- **Etiketsiz kayıt incelemesi:** Model davranışının gözlemlenmesi; referans etiketi yoksa sayısal doğruluk kanıtı değildir.

Bu ayrımlar modeli evrensel bir ölçer olarak sertifikalandırmak için değil, modelin kendi veri kümesinde nasıl geliştiğini dürüstçe izlemek içindir. Eğitimde çok iyi sonuç alınması, henüz görülmemiş aygıtlarda da aynı performansın olacağını iddia etmemize yol açmaz; fakat bu belirsizlik projenin ana hedefini değiştirmez.

## Referans etiketleri ve katsayılar

PZEM okumaları, proje kapsamındaki SCT verilerini etiketlemek ve modelin tahminleriyle karşılaştırmak için referans akıştır; kusursuz veya bağımsız laboratuvar gerçeği olarak kabul edilmez. Python araçları zaman içinde:
1. kayıtları toplar, denetler ve ilişkilendirir;
2. kararlı bölgeleri ve kullanılabilir etiketleri belirler;
3. SCT ham örneklerinden özellikler çıkarır;
4. etiketli veriden model/katsayılar öğrenir;
5. modeli etiketli kayıtlarla karşılaştırır ve sonuçları geçmiş sürümlerle raporlar.

Modelin akım tahmini şu an ESP üzerinde yapılmıyor. İlk basamakta yalnız ESP32 dahili ADC ham verisinin okunması, kaydedilmesi ve bilgisayarda görselleştirilmesi hedefleniyor. Model ve katsayı üretimi, veri edinimi ve etiketleme için yeterli kanıt oluştuktan sonraki aşamadır.

## Ölçüm sınırları başarısızlık değildir

Evde bir tamirat sırasında kaynak makinesi gibi yüksek akım çeken veya daha önce gözlenmemiş bir yük kullanılabilir. SCT/analog ön uç/ESP32 ADC aralığı aşılır, örnekler tavana veya tabana vurur ya da model anlamlı tahmin üretemezse bu tek başına proje başarısızlığı değildir. Her yükü ölçmek zorunlu değildir.

Böyle bir kayıt yine de işe yarayabilir: ADC değerlerinin sınıra dayanması, dalga biçiminin bozulması, verinin eksik kalması veya modelin tahmin üretememesi raporlanabilir. Kayıt, kapsam dışı veya doygunluk içeren örnek olarak işaretlenebilir. Ölçülmeyen akım için uydurma değer üretilmez ve başarısız tahmin başarılı ölçüm gibi sunulmaz.

Hedef, her koşulda bir sayı üretmek değil; mevcut ev içi aygıtlar için toplanan veriyi zamanla daha iyi açıklamak ve sistemin ne zaman sınırına geldiğini kayıtlardan anlayabilmektir.

## Değişim raporu ve geçmiş

Yeni modelin sonuçları önceki model sürümüyle karşılaştırılır. Rapor, kullanılan veri kümesi sürümünü, etiketleri, özellikleri, modeli/katsayıları ve karşılaştırma kapsamını belirtir. İyileşme, gerileme veya karşılaştırılamayan durumlar ayrı yazılır. Eski sonuçlar sessizce silinmez veya üzerine yazılmaz.

## Çalışma ilkesi

BERO küçük ve aşamalı ilerler. İlk hedef ham ADC verisini görmek ve bilgisayarda görselleştirmektir. Sonraki kararlar gözlenen veriye göre verilir; model, katsayı, karmaşık aktarım veya ilave donanım ilk adıma peşinen eklenmez.

Bu belge proje yaklaşımını açıklar; model eğitimi, akım hesaplama, fiziksel ölçüm veya doğrulama yapıldığı anlamına gelmez.
