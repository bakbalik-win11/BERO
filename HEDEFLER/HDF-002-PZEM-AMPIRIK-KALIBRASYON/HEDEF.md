# HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak

**Durum:** Açık — yeni araştırma yaklaşımı tanımlandı; deney sonuçları henüz üretilmiş sayılmaz.  
**Güncelleme:** 2026-10-12  
**Ana ilke:** Önce her ölçüm zincirinden bağımsız olarak mümkün olan en yüksek kaliteli ham veriyi al ve ölçüm karakterini öğren; fiziksel olarak desteklenen bölgeler arasında ilişki kur; donanım sadeleştirmesi ve paket optimizasyonunu daha sonraki aşamaya bırak.

> **Geçmişi koruma:** Bu hedefin önceki sürümleri ve kararları Git geçmişinde korunur. Bu yeni sürüm, eski mimariyi sessizce silmek yerine aktif araştırma yönünü değiştirir. Önceki test kayıtları, kodlar ve ölçümler tarihsel kanıt olarak kalır.

## 1. Hedef

Her ölçüm zincirinin fiziksel olaylara verdiği karakteristik cevabı öğrenmek. Aynı fiziksel olayı temsil eden iki ayrı veri akışındaki kararlı veya anlamlı kısa bölgeleri eşleştirmek, eşleştirilmiş veri kümesi oluşturmak ve Python ile veriler arasındaki en güçlü, doğrulanabilir ilişkiyi araştırmak.

Evrensel tek bir `k` katsayısı varsayılmaz. Aday ilişki önce `I = f(X)`, veriler katkı gösterirse `I = f(X, Bias, V, PF)` gibi daha geniş biçimde sınanabilir. Amaç en karmaşık modeli değil, yeni ve bağımsız verilerde de çalışan en sade ilişkiyi bulmaktır.

## 2. Aşama 1 — Ölçüm karakterini öğrenmek

### 2.1 Ham veri ve ölçüm kaynakları

İlk deneylerde kapsam küçük tutulur: **bias ve bir veya iki sensör kanalı**. Ham sensör verileri ile PZEM referans ölçümleri ayrı kaynaklardan toplanır; ham kayıtlar değiştirilmeden korunur.

**Öncelik, sensörleri aynı ESP'de toplamak değil, her ölçüm zincirinin kendi ham verisini en yüksek kalitede elde etmektir.** Aşama 1'de sensör kanallarını tek ESP'de birleştirmeye çalışmayız. Dört kanal gereksinimi, dört kanalın aynı ESP'de okunması gerektiği anlamına gelmez; bir zincirde kanal sayısı ölçüm hızını gereksiz düşürüyorsa kanallar/zincirler bağımsız sınanır. Donanım sadeleştirmesi, birleştirme ve paket optimizasyonu Aşama 1'in işi değildir.

**Okuma hızı ilk önceliktir:** Dört kanal okunacak diye ölçüm döngüsünün gereksiz yere yavaşlamasına izin verilmez. Seçilen kanalların her biri mümkün olan en yüksek *sağlıklı ve sürdürülebilir* örnekleme hızında okunmaya çalışılır. Dört kanalı birlikte okumak hızı düşürüyorsa, kanalların veya ESP'lerin ayrı ayrı çalıştırıldığı deneyler de yapılır. Kanal başına ve toplam örnekleme hızı, zamanlama kararlılığı ve örnek kaybı ölçülür; hız varsayılmaz, ölçülür. Gerekirse ESP'ler teker teker sınanır. Bu, doğrulanmış mevcut performans değil, test edilecek hedef gereksinimidir.

PZEM okuması sensör örnekleme yolunu yavaşlatmamak veya etkilememek için ayrı yürütülür. Bunun için ayrı bir ESP veya başka bir bağımsız okuma yolu kullanılabilir. Kaç ESP kullanılacağı şimdiden sabitlenmez; birden fazla mini ESP'nin aynı sensöre bakması da deney tasarımına göre değerlendirilebilir.

Mac'e doğrudan bağlantı sayısı pratik bir sınır oluşturabilir. Gerekirse veriler Home Assistant'a aktarılır, saklanır ve daha sonra Python/Mac tarafında birleştirilip eşleştirilir. **Mac'in gerçek zamanlı eşleştirme noktası olması şart değildir.** Home Assistant ile Mac arasındaki nihai veri taşıma mimarisi henüz kesinleşmiş değildir.

Her ölçüm zinciri ilk olarak kendi başına en yüksek sağlıklı okuma hızına ulaşmaya çalışır. Birden fazla kanalı/ESP'yi birlikte çalıştırmanın ölçüm hızını düşürüp düşürmediği ayrıca test edilir; dört kanalı okuma uğruna örnekleme yolunu yavaşlatmak kabul edilen bir varsayım değildir. Gerekirse ölçüm zincirleri teker teker çalıştırılır ve bağımsız ham kayıtlar toplanır.

Paket senkronizasyonu ve milisaniye düzeyinde saat eşitlemesi bu aşamanın hedefi değildir. Kayıt zamanı varsa korunur; fakat eşleştirme aynı fiziksel olayı temsil etme kanıtına ve deney bağlamına dayanır. Bölgelerin sürelerinin eşit olması gerekmez. Eşleşme güvenilir biçimde kurulamıyorsa veri zorla eşleştirilmez.

### 2.2 Deney sınıfları

- **Kısa, kontrollü deney:** Örneğin 150 W akkor lamba tek başına çalışır.
- **Uzun deney:** Örneğin Fan 1 bir gece boyunca çalışır; uzun dönemli kararlı bölgeler ve zaman içindeki değişimler gözlenir.
- **Karma deney:** Akkor lamba ve fan birlikte çalışır; karma yük davranışı ayrı etiketlenir.

Bunlar planlanan deney örnekleridir; tamamlanmış veya başarılı deneyler olarak kabul edilmez. Her deneyin fiziksel koşulu, kaynak cihazı/kanalı ve mevcut kayıt bilgileri saklanır. Ham veriler, temizlenmiş veriler ve eşleştirilmiş bölgeler ayrı tutulur. Tekil yük verileri karma yük davranışının basit toplamı olarak önceden varsayılmaz.

### 2.3 Eşleştirme ve etiketleme

İki akışın ilk işlemesi ayrı yürütülür:

- **PZEM akışı:** Kararlı/anlamlı bölgeler belirlenir ve uygun bölgelere ölçülen akım değeri etiketi verilir.
- **SCT akışı:** Ham örüntüler ve karakteristik özellikler çıkarılır; bu aşamada PZEM etiketi varsayılmaz.
- **Python korelasyonu:** PZEM etiketli bölgeler ile SCT karakter bölgeleri, aynı fiziksel durumu temsil ettiklerine dair deney koşulları ve kayıtlarla destek varsa ilişkilendirilir. Böylece PZEM akım etiketi, desteklenen SCT karakter bölgesine aktarılabilir ve aday `I = f(X)` ilişkisi öğrenilebilir.

**Öncelik paket/zaman senkronizasyonu değil, karakter ve bölge korelasyonudur.** Bununla birlikte zaman bilgisi yardımcı kanıt olarak korunabilir; sayısal benzerlik tek başına aynı fiziksel durumu kanıtlamaz. Fiziksel eşleşme yeterince desteklenmiyorsa etiket zorla aktarılmaz.

Mühendislik tarafı fiziksel olayı seçer, deney koşullarını kaydeder, veriyi temizler ve aynı fiziksel olayı temsil ettiği desteklenen bölgeleri etiketler.

Python tarafı:
- İki veri akışında karşılık gelen bölgeleri arar.
- Korelasyonu ve anlamlı özellikleri inceler.
- Bias, gerilim ve PF gibi aday parametrelerin katkısını değerlendirir.
- Aday fonksiyonları karşılaştırır.
- Eğitim/model seçimi için kullanılan verilerden ayrı tutulan örneklerle bağımsız doğrulama yapar.

Örnek olarak PZEM'de 1,50 A civarında bir bölge ve sensör akışında belirli bir ham örüntü görülebilir. Bunların aynı fiziksel duruma ait olduğu deney bağlamıyla desteklenmelidir; örnek değerler açıklama amaçlıdır, BERO ölçüm sonucu değildir.

PZEM, eğitim ve doğrulama aşamasında referanstır. Nihai amaç, doğrulanmış bir modelin çalışma sırasında sensör verisinden akım tahmin edebilmesidir.

## 3. Aşama 2 — Ölçüm hızı, donanım sadeleştirmesi ve paketlemeyle gerçek hayatı yakalamak

Aşama 1'de her zincirin ham veri kalitesi ve karakteri anlaşılmadan donanım sadeleştirmesi/birleştirmesi yapılmaz. **Paketleme ve paket optimizasyonu da birinci aşamanın kapsamı değildir.** İkinci aşamada, fiziksel olayları kaçırmadan yakalamaya uygun ölçüm hızı ve veriyi güvenilir taşıyacak paketleme yöntemi deneylerle seçilir.

- **Ölçüm hızı:** Kısa süreli değişimleri ve uzun süreli davranışı yeterince yakalayacak örnekleme hızını bul.
- **Paket boyutu/yöntemi:** Sabit boyutlu ve değişime duyarlı seçenekleri karşılaştır.
- **Aktarım:** Veri kaybı, aktarım süresi/throughput, bellek ve işlemci yükünü ölç.
- **Gerçek hayat temsili:** Kısa geçişlerin ve uzun kararlı bölgelerin seçilen hız ve paketleme ile korunup korunmadığını değerlendir.

Ölçüm hızı örneklerin hangi sıklıkta alındığını; paketleme ise alınan örneklerin nasıl gruplanıp taşındığını belirler. İki değişken ayrı ayrı incelenir ve sonra birlikte doğrulanır. En yüksek hız veya en büyük paket kendiliğinden en iyi seçenek sayılmaz.

## 4. Veri koruma

Ham kaynak kayıtları üzerine yazılmaz. Temizlenmiş veriler, eşleştirilmiş bölgeler, özellikler, modeller ve raporlar ayrı saklanır. Kayıtlar mümkün olduğunca deney kimliği, yük sınıfı, kaynak cihaz/kanal, bölge kimliği ve mevcut zaman bilgisiyle izlenebilir olmalıdır.

Önerilen arşiv düzeni:

```text
BERO_DATA/
  raw/
  features/
  models/
  reports/
  archive/
```

Bu, önerilen klasör düzenidir; belgenin yazılması Mac üzerinde klasörlerin oluşturulduğu veya veri aktarımının doğrulandığı anlamına gelmez. Kaynak veriler aktarım bütünlüğü doğrulanmadan silinmez.

## 5. Tamamlanma ölçütleri

**Aşama 1:** Ham veriler ve deney bağlamı korunmuş; aynı fiziksel olayı temsil eden bölgeler gerekçeli biçimde eşleştirilmiş; yeniden kullanılabilir eşleştirilmiş veri kümesi oluşturulmuş; aday fonksiyon bağımsız verilerle sınanmış olmalıdır.

**Aşama 2:** Kısa ve uzun süreli fiziksel davranışlar yeterince yakalanmış; veri aktarımı ve kayıp ölçülmüş; ölçüm hızı ile paketleme seçenekleri karşılaştırılarak uygun yapı seçilmiş olmalıdır.

Ölçüm veya doğrulama kanıtı olmadan hiçbir test başarılı ilan edilmez.

## 6. Çalışma sırası

1. PZEM referansını ayrı ve sensör örneklemesini etkilemeyecek şekilde kaydet; PZEM kararlı bölgelerini akım etiketiyle işaretle.
2. Bias ve seçilen sensör kanallarından, her ölçüm zincirini ilk aşamada bağımsız tutarak ham veri topla; her kanalın mümkün olan en yüksek sağlıklı hızını ölç. Dört kanalın birlikte okunmasının hızı düşürüp düşürmediğini, gerekirse kanal/ESP'leri teker teker çalıştırarak karşılaştır.
3. Kanal başına ve toplam örnekleme hızını, zamanlama kararlılığını ve örnek kaybını kaydet; hızın doğrulandığına dair ölçüm olmadan iddiada bulunma.
4. Veriyi uygun yerde biriktir (Mac veya Home Assistant üzerinden); ham kaynakları koru.
5. Aynı fiziksel olayı temsil eden bölgeleri Python ile eşleştir; geçerli eşleşmeleri etiketle.
6. Eşleştirilmiş veri kümesinden özellikleri ve aday `f(X)` ilişkilerini araştır; bağımsız verilerle doğrula.
7. Aşama 1 tamamlanıp ölçüm karakteri anlaşıldıktan sonra donanım sadeleştirmesi/birleştirmesini ayrıca değerlendir.
8. Daha sonra ölçüm hızı ve paketleme yöntemini gerçek hayatı yakalama, veri kaybı ve kaynak kullanımı açısından karşılaştır; ilk aşamada ölçülen ham okuma hızı sonuçlarını temel al.

## 7. Kısa yön özeti

**Önce her ölçüm zincirinden bağımsız, kaliteli ham veri al; PZEM bölgelerini akım etiketiyle, SCT bölgelerini sinyal karakteriyle tanımla; fiziksel olarak desteklenen karakter/bölgeleri korele ederek `I = f(X)` ilişkisini araştır. Sonra donanımı sadeleştir ve ölçüm hızı/paketlemeyi seç.** Paket senkronizasyonu olay korelasyonunun ön koşulu değildir; paketleme ikinci aşamanın araştırma konusudur.
