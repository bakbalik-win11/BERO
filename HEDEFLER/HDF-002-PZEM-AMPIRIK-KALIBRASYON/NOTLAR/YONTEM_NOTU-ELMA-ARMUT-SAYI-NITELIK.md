# BERO — Araştırma ve Yöntem Notu
# Elma ile Armut: Sayısal İşlem, Fiziksel Anlam ve Ölçüm Niteliği

**Tarih:** 2026-10-12  
**Bağlantılı hedef:** HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak  
**Kayıt türü:** Yöntemsel düşünce / araştırma ilkesi  
**Durum:** Kavramsal not; deneysel sonuç veya doğrulanmış fizik modeli değildir.

---

## 1. Çıkış noktası

Matematiğe güvenmek güzeldir. Matematik, açıkça tanımlanmış nicelikler üzerinde tutarlı işlemler yapmamızı sağlar. Fakat bir işlemin matematiksel olarak yapılabilir olması, sonucunun fiziksel açıdan anlamlı olduğunu tek başına garanti etmez.

Elma ile armudu düşünelim. Elma sayısı ile armut sayısını toplamak mümkündür. Sonuç, toplam meyve adedini verir. Ancak bu toplam, kaç elma ve kaç armut olduğunu artık ayrı ayrı söylemez. Eğer sorumuz toplam meyve sayısıysa işlem anlamlıdır; eğer elmaların ve armutların ayrı özelliklerini araştırıyorsak, tür ayrımını kaybetmek bilgi kaybıdır.

Demek ki mesele yalnızca “toplanabilir mi?” değildir. **Hangi soruya cevap arıyoruz ve işlem sırasında hangi niteliği korumamız gerekiyor?**

Bazı durumlarda nicelikleri toplamak tam olarak aradığımız şeydir. Bazı durumlarda ise toplama, karşılaştırma veya tek bir katsayıya indirgeme, önemli farklılıkları görünmez hâle getirir. Nitelik önemliyse, bu farkları salt sayıya dönüştürüp sonra yok sayamayız.

Bu ayrım BERO'daki ölçüm araştırması için önemlidir.

## 2. Sayı, temsil ve fiziksel anlam aynı şey değildir

Bir ölçüm sistemi bize sayı verir. Fakat sayı tek başına, o değerin hangi fiziksel süreci temsil ettiğini bütün ayrıntılarıyla anlatmaz.

Bir veri noktasını yorumlayabilmek için en azından şu sorular sorulmalıdır:

- Hangi sensör veya ölçüm zinciri bu değeri üretti?
- Değer ham bir örnek mi, dönüştürülmüş bir ölçüm mü, yoksa hesaplanmış bir özellik mi?
- Hangi fiziksel büyüklüğü temsil ediyor?
- Ölçek, birim, ofset ve referans koşulları biliniyor mu?
- Hangi yük ve deney koşullarında üretildi?
- Bu değer başka bir değerle karşılaştırılabilir mi? Karşılaştırılabiliyorsa hangi koşullarda?
- İşlem yapılırken korunması gereken bir sinyal karakteri veya sınıf farkı var mı?

Örneğin bir ADC'nin verdiği ham sayısal örnek ile içinde ölçüm/işleme entegresi bulunan bir modülün dışarıya verdiği sonuç aynı biçimde sayıya çevrilebilir. Ancak bunlar otomatik olarak aynı türden veri olmaz. ADC örneği analog girişin belirli andaki sayısal karşılığı olabilir; entegreli modülün çıkışı ise kendi donanım yapısının, ölçüm zincirinin veya iç işleme yönteminin etkisini zaten taşıyor olabilir.

Her iki değer de sayısal olduğu için onları aynı sütuna yazmak mümkün olabilir. Fakat bu, aralarındaki temsil farkının ortadan kalktığı anlamına gelmez.

**Veriyi ortak bir biçimde saklamak ile verileri aynı fiziksel anlamı taşıyormuş gibi kullanmak farklı kararlardır.**

## 3. Matematiksel işlem doğru, yorum yanlış olabilir

Bir işlem sayılar üzerinde kusursuz uygulanabilir ama kullanılan sayılar araştırma sorusu için uygun olmayabilir.

Örneğin iki sensörün ham çıktılarını topladığımızı düşünelim. Çıktılar aynı birime sahip değilse veya farklı dönüşüm zincirlerinden geliyorsa, toplamın doğrudan fiziksel anlamı olmayabilir. Önce kalibrasyon, ölçek, birim ve temsil ilişkilerinin anlaşılması gerekir.

Benzer şekilde, iki akım değerini toplamak bazı elektriksel sorular için anlamlı olabilir. Fakat iki yükün akımlarını yalnızca aritmetik olarak toplamak, bütün koşullarda toplam akımın doğru fiziksel temsilini elde ettiğimizi garanti etmez. Faz ilişkisi, dalga biçimi, ölçümün RMS mi anlık değer mi olduğu ve hangi noktada ölçüm yapıldığı gibi ayrıntılar sorunun niteliğine göre önemli olabilir.

Buradaki amaç her işlemi karmaşıklaştırmak değildir. Tam tersine, işlemden önce hangi bilgilerin gerekli olduğunu belirlemektir. Sorunun cevabı toplam nicelikse uygun koşullarda toplamak gerekir. Sorunun cevabı sensör karakterleri arasındaki farksa bu karakterleri tek bir toplamda eritmemek gerekir.

## 4. Nitelik neden önemlidir?

Nitelik, aynı sayısal büyüklükteki iki olayın ölçüm açısından farklı davranabileceğini anlatır.

İki yük benzer akım çekebilir ama dalga biçimleri farklı olabilir. İki sensör aynı fiziksel büyüklüğü ölçmeyi amaçlayabilir ama farklı iç yapılara, bant genişliklerine, ölçeklere veya işleme davranışlarına sahip olabilir. İki kayıt benzer sayılar içerebilir ama farklı deney koşullarında üretilmiş olabilir.

Böyle durumlarda sayısal benzerlik tek başına eşdeğerlik kanıtı değildir.

BERO açısından bu şu anlama gelir:

- Ham verinin kaynağı korunmalıdır.
- Ölçüm zincirinin kimliği kaybolmamalıdır.
- Deney koşulları ve yük türü kaydedilmelidir.
- Ham sinyal ile ondan çıkarılan özellikler birbirinden ayrılmalıdır.
- Birbirine benzeyen bölgeler otomatik olarak aynı fiziksel olaya ait kabul edilmemelidir.
- Eşleştirme için yalnızca sayısal benzerlik değil, deney bağlamı da aranmalıdır.

Bu ilkeler, daha sonra verileri bir tabloda birleştirmeye veya matematiksel bir model kurmaya engel değildir. Tam tersine, böyle birleştirmelerin hangi koşullarda savunulabilir olduğunu belirlemeye yardım eder.

## 5. Voltaj ve PF etiketleri neyi çözer, neyi çözmez?

HDF-002'de geliştirilen yöntemle PZEM bölgeleri, voltaj (`V`) ve güç faktörü (`PF`) bakımından aynı veya deney toleransı içinde benzer olan gruplara ayrılabilir. Bu gruplarda akım etiketi tek başına değil, `(I, V, PF)` bağlamıyla saklanır.

Bu yaklaşımın faydası, akım etiketinin hangi elektriksel koşullarda gözlendiğini unutmamaktır. Benzer V/PF koşullarında farklı akımların ve SCT karakterlerinin nasıl ilişkili olduğu daha kontrollü biçimde incelenebilir. Böylece belirli bir koşul grubunda daha sade bir ilişki veya aday `k` katsayısı araştırılabilir.

Ama bu etiketleme elma ile armudu otomatik olarak aynı meyve yapmaz.

Aynı voltaj ve benzer PF, iki yükün aynı dalga biçimine sahip olduğunu veya aynı fiziksel olayı temsil ettiğini kanıtlamaz. Yük türü, sinyal karakteri ve sensörün kendi davranışı hâlâ önemlidir. PF de dalga biçiminin bütün ayrıntılarını tek başına tarif etmez.

Dolayısıyla V/PF etiketleri bir **koşul tanımlama ve kontrollü karşılaştırma aracı** olarak görülmelidir; bütün nitelik farklarını ortadan kaldıran bir eşitleme işlemi olarak değil.

## 6. SCT ve entegreli sensörler: Aynı araştırma disiplini, farklı ölçüm karakterleri

SCT-013 gibi bir akım trafosu ile içinde ölçüm veya sinyal işleme entegresi bulunan bir sensör/modül aynı ölçüm zinciri değildir. Birinin ham analog davranışını örnekleyebiliriz; diğerinin dışarı verdiği değer, entegre ve çevresindeki devrenin davranışını da içeriyor olabilir.

Her iki sistemi aynı araştırma disipliniyle incelemek mümkündür: ham çıktıyı korumak, deney koşullarını kaydetmek, referans ölçümle ilişki aramak ve doğrulamayı bağımsız veride yapmak. Ancak bir sistemden öğrenilen dönüşüm veya katsayı, gerekçe ve kanıt olmadan diğer sisteme taşınmamalıdır.

Sensör türü, model/entegre bilgisi biliniyorsa parça kimliği, bağlantı, ölçüm aralığı, çıktı türü, ölçek ve mevcut dokümantasyon kayıtla birlikte tutulmalıdır. Bilinmeyen özellikler tahminle doldurulmamalı; açık soru olarak kalmalıdır.

Böylece ileride farklı sensörler incelendiğinde, hepsinin çıktısını aynı tabloya yazabilsek bile her değerin hangi zincire ait olduğu ve neyi temsil ettiği korunur.

## 7. Bir katsayı veya model ne zaman anlamlı olur?

Tek bir `k` katsayısı, doğrusal ilişki veya daha karmaşık bir fonksiyon baştan doğru kabul edilmemelidir. Önce hangi verilerin karşılaştırılabilir olduğu ve hangi koşullar altında ilişki arandığı belirlenmelidir.

Araştırma sırası şu şekilde düşünülebilir:

1. Ölçüm kaynağını, ham veri türünü ve fiziksel anlamı tanımla.
2. Deney koşullarını ve referans etiketlerini kaydet.
3. Fiziksel olarak desteklenen, karşılaştırılabilir bölgeleri seç.
4. Bu bölgelerde ham sinyal ve özellikler arasındaki ilişkiyi incele.
5. Basit bir tablo veya katsayının yeterli olup olmadığını sınayarak değerlendir.
6. Gerekirse daha kapsamlı bir fonksiyon araştır.
7. Aday ilişkiyi bağımsız deneylerde doğrula ve hangi koşullarda geçerli olduğunu açıkça belirt.

Eğer bir katsayı yalnızca dar bir voltaj/PF grubunda çalışıyorsa, bunu evrensel katsayı diye sunmak yerine o grubun koşullu ilişkisi olarak kaydetmek gerekir. Farklı yük türleri veya sensörler farklı davranıyorsa, ayrı tablolar veya modeller gerekebilir. Bunların gerçekten gerekli olup olmadığı deney verisiyle belirlenecektir.

**Modelin sadeliği değerlidir; ama sadelik, önemli fiziksel ayrımları silerek elde edilmemelidir.**

## 8. BERO için yöntem ilkesi

Bu düşünceden çıkan çalışma ilkesi şudur:

> Önce ölçümün neyi temsil ettiğini ve hangi nitelikleri taşıdığını öğren. Sonra hangi verilerin hangi koşullarda karşılaştırılabileceğine karar ver. Matematiksel işlemi ve modeli bu karardan sonra seç.

Bu ilke, verileri asla birleştirmemek anlamına gelmez. Birleştirmek, toplamak, normalize etmek, katsayı bulmak ve model kurmak araştırmanın doğal araçlarıdır. Ancak her aracın hangi soruyu cevapladığı bilinmelidir.

Bir tabloda ayrı sütunlarda tutulan iki nicelik, gerektiğinde ortak bir sonuç üretmek için birleştirilebilir. Fakat kaynak, birim, fiziksel anlam ve koşul bilgisi erken aşamada atılırsa daha sonra hangi verinin neden uyumlu veya uyumsuz olduğu anlaşılamayabilir.

Bu nedenle ham kayıtlar korunur; dönüşümler açıkça belgelenir; eşleştirmeler gerekçelendirilir; deney sonucu ile yorum birbirinden ayrılır. Önceki sonuçlar ve başarısız denemeler de silinmez. Yeni kanıt eski yorumu değiştirirse, geçmişi yok etmek yerine yeni kararın gerekçesi kaydedilir.

## 9. Açık kalan sorular

- Hangi sensör ve modüllerin çıktıları aynı fiziksel büyüklüğü hangi biçimde temsil ediyor?
- Her cihazın ölçüm zinciri, ölçeği ve iç işleme davranışı ne kadar biliniyor?
- V/PF koşulları içinde hangi ek nitelikler veya yük sınıfları ayrım gerektiriyor?
- Hangi bölgelerde basit tablo veya katsayı yeterli; hangi bölgelerde ayrı ilişki/model gerekiyor?
- Bir ilişki bağımsız deneylerde ne kadar iyi korunuyor?

Bu sorular henüz cevaplanmış sayılmaz. Bu belge sonuç ilan etmek için değil, araştırma sırasında kavramsal ayrımı unutmamak için saklanmaktadır.

---

## Kısa sonuç

Elma ile armut sayıca toplanabilir; toplam meyve adedini arıyorsak bu doğru ve yararlı bir işlemdir. Ama meyve türlerini, tatlarını veya özelliklerini araştırıyorsak toplam sayı bu ayrımları korumaz. Hangi bilginin önemli olduğu, hangi işlemin anlamlı olduğunu belirler.

Ölçümlerde de salt sayı her zaman yeterli değildir. Sayının kaynağı, fiziksel temsil ettiği büyüklük, ölçüm zinciri, nitelikleri ve deney koşulları korunmalıdır.

**Matematik hesaplar; fiziksel anlamı ise doğru tanımlanmış ölçüm, deney ve koşullar birlikte kurar.**
