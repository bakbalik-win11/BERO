# Akım durum sınıflandırması — üç sonuçlu çıktı sözleşmesi

**Durum:** Tasarım kararı kaydedildi; karar eşikleri ve algoritma henüz doğrulanmadı.  
**Tarih:** 2026-11-06  
**Kapsam:** Ölçüm/izleme çıktısının fiziksel akım durumunu üç sınıftan biriyle ifade etmesi.

## 1. Amaç

BERO'nun kullanıcıya sunduğu sonuç yalnızca sayısal akım değeri değildir. Sistem, ölçümün hangi durumda olduğunu da dürüstçe bildirmelidir. Amaç her koşulda doğru amper değeri üretmek değil; fiziksel akım yok, akım var veya güvenilir karar/hesap üretilemiyor ayrımını yapabilmektir.

Bu sınıflandırma, ON eğitiminden K katsayısı üretme işleminden ayrıdır. K eğitimi sabit yük ON pencerelerindeki SCT/PZEM medyan çiftlerini kullanır. Üç durumlu sınıflandırma ise OFF referansını, yüklü dağılımları, zaman kararlılığını ve ölçüm çalışma sınırını birlikte değerlendirir.

## 2. Kullanıcı tarafından belirlenen üç çıktı

| Kod | Kullanıcıya gösterilecek ifade | Anlam |
|---|---|---|
| `CURRENT_PRESENT` | **AKIM VAR** | Akım varlığına yeterli kanıt vardır ve ölçüm mevcut çalışma koşullarında hesaplanabilir. |
| `NO_CURRENT` | **AKIM YOK** | Fiziksel akım olmadığına OFF referansıyla yeterli istatistiksel kanıt vardır. |
| `CURRENT_NOT_COMPUTABLE` | **AKIM HESAPLANAMADI** | Akım olabilir; fakat ölçüm kararsızdır, OFF/yüklü dağılımlar örtüşür veya çalışma noktası güvenilir ölçüm bölgesinin dışındadır. |

**Değişmez anlam:** AKIM HESAPLANAMADI, AKIM YOK anlamına gelmez. Belirsizlik zorla ikili karara çevrilmez.

## 3. İstatistiksel dayanak

### 3.1 OFF referansı

Fiziksel akımın olmadığı koşullarda toplanan I007 verisi ayrı referans dağılımıdır. En az şu ölçüler raporlanır:

- Medyan
- MAD ve 1.4826 × MAD
- P05, P95 ve P99
- Zaman dilimlerine göre medyan/MAD
- Örnek sayısı, gerçek timestamp aralığı ve eksik kayıtlar

Tek bir OFF medyanı veya tek bir üst yüzdelik otomatik karar eşiği değildir. 2026-11-06 CH1-1T oturumunda zamanla medyan ve MAD değişimi gözlendi; bu nedenle durağanlık varsayılmayacaktır.

### 3.2 Yüklü durum dağılımları

15 W ve diğer sabit yük seviyeleri ayrı veri gruplarıdır. Her yük grubu kendi medyanı, MAD'si, yüzdelikleri ve zaman içi kararlılığıyla değerlendirilir. Farklı yükler tek bir dağılımda birleştirilmez.

### 3.3 Dağılım örtüşmesi

OFF ve yüklü dağılımlar örtüşüyorsa tek bir ölçüm değerinden kesin fiziksel durum çıkarmak mümkün olmayabilir. Örtüşen alan, veri yetersizliği veya kararsızlık halinde çıktı `CURRENT_NOT_COMPUTABLE` olmalıdır. Örtüşme miktarı ve sınıflandırma performansı gerçek veri üzerinde ölçülmeden eşik belirlenmez.

### 3.4 Zaman koşulu

Tek bir örnekle durum değiştirilmez. Kararlılık penceresi, doğrulama süresi ve minimum örnek sayısı deneylerle seçilecektir. Kısa sıçramalar ve geçişler ham veride korunur; sınıflandırma için ayrı türetilmiş özellikler/işaretler üretilebilir.


## 3.5 Süre-temelli karar ilkesi — sıçrama tuzağına karşı zorunlu kural

**Kullanıcı tarafından açıkça belirlenen analiz ilkesi:** K=24.22 uygulanmış CH1 akım çıktısında 0.20 A sınırı değerlendirilirken tekil örneklerin eşik üstüne çıkması, tek başına akım varlığı veya OFF sınıflandırmasının başarısızlığı sayılmaz. Karar, eşik davranışının zaman içindeki süresine ve pencere kararlılığına dayanmalıdır.

Zorunlu uygulama kuralları:

1. Tekil yüksek örnekler ve kısa süreli sıçramalar ham veride aynen korunur; ancak tek başlarına CURRENT_PRESENT veya NO_CURRENT kararı verdirmez.
2. Her aday zaman penceresinde eşik üstünde kalma süresi, ardışık devam süresi ve pencere içindeki zaman oranı hesaplanır. Kayıt aralığı düzensizse süre, örnek adedinden değil timestamp farklarından türetilir.
3. Pencere medyanı, MAD ve zaman dilimli medyan değişimi birlikte incelenir. Tek bir eşik üstü örnek veya yalnızca eşik üstü örnek yüzdesi karar ölçütü değildir.
4. OFF, 15 W, 42 W, 57 W ve 57 W+15 W gibi her fiziksel koşul ayrı gruplar halinde ve aynı pencere yöntemiyle karşılaştırılır.
5. Kısa/uzun pencere karşılaştırmaları yapılır; pencere uzunluğu, minimum devam süresi, izin verilen kesinti ve zaman oranı henüz belirlenmiş değildir. Bu parametreler deneylerle belirlenecek ve ayrı kayıtlarda doğrulanacaktır.
6. Sıçramalar filtrelenerek ham kayıttan silinmez. Gerekirse türetilmiş analiz katmanında sıçrama olarak işaretlenir; karar algoritması süreklilik/kararlılık koşulunu uygular.

**0.20 A hipotezinin doğru yorumu:** Kullanıcının gözlemi, K uygulanmış CH1 çıktısının 0.20 A altındaki davranışının fiziksel OFF ile uyumlu olabileceğidir. Bu, tekil örnek bazında mutlak cutoff olarak değil, zaman penceresi ve süre koşuluyla sınanacak aday sınıflandırma kuralıdır. 0.20 A üzerinde kısa sıçrama görülmesi bu hipotezi tek başına çürütmez.

**Önceki değerlendirme düzeltmesi:** I007 raporundaki tekil örnek yüzdelikleri veya 0.20 A üstü örnek oranı, OFF sınıflandırmasının başarısızlığı şeklinde yorumlanamaz. I007 raporu K öncesi katsayısız ct_clamp verisini içerir; K=24.22 uygulanmış eşik değerlendirmesi için önce doğru ölçek dönüşümü yapılmalı, ardından süre-temelli analiz uygulanmalıdır. Tekil örnek oranı yalnız betimleyici bilgidir.

## 4. 0.3 A aday çalışma sınırı

Önceki deneylerde yaklaşık 0.3 A altındaki ölçüm bölgesi belirsiz/kararsız aday alan olarak tartışılmıştır. Bu değer:

- doğrulanmış evrensel eşik değildir;
- fiziksel akımın yok olduğu anlamına gelmez;
- bu bölgedeki akım ölçümünün güvenilir sayı üretmeyebileceğini ifade eden aday çalışma sınırıdır;
- gerektiğinde `CURRENT_NOT_COMPUTABLE` sonucuna götürebilir.

OFF/15 W dağılım ayrışması, düşük akımın varlığını tanımaya yardımcı olabilir; fakat tek başına doğru amper hesabını veya tüm aralıkta doğruluğu kanıtlamaz.

## 5. Karar sırası — taslak

1. Kaynak kayıtların geçerliliği, timestamp ve örnek sayısı kontrol edilir.
2. SCT ölçüm serisinin zaman kararlılığı değerlendirilir.
3. Ölçüm OFF referansıyla karşılaştırılır.
4. OFF ve yüklü dağılımlarının örtüşmesi ve karar kanıtı değerlendirilir.
5. Akım varlığına kanıt varsa ve çalışma bölgesi hesaplanabilir durumdaysa `CURRENT_PRESENT`.
6. OFF referansıyla fiziksel akım yokluğuna yeterli kanıt varsa `NO_CURRENT`.
7. Kararsızlık, örtüşme, yetersiz veri veya düşük akım çalışma sınırı varsa `CURRENT_NOT_COMPUTABLE`.

Bu sıra kavramsal taslaktır; henüz çalışan algoritma veya doğrulanmış karar ağacı değildir. Sınıf önceliği ve sayısal eşikler OFF ve yük deneyleri tamamlandıktan sonra belirlenmelidir.

## 6. K katsayısı eğitiminden ayrım

- K eğitim çifti: aynı ON çevriminin ortak kararlı penceresinden SCT medyanı ve PZEM medyanı.
- OFF referansı: fiziksel sıfır-akım koşulunun ayrı dağılımı; ON K eğitim çiftine katılmaz.
- Durum sınıflandırması: OFF ve yüklü dağılımları, kararlılık ve çalışma sınırlarını kullanır.
- Üç durumlu sınıflandırma, K katsayısını değiştirmez; K'nin hangi koşullarda kullanılabilir olduğunu ifade eden ayrı katmandır.

## 7. Açık kalan kararlar

- OFF dağılımından türetilecek karar eşiği/yöntemi.
- OFF referansının zamanla değişimini ele alma yöntemi.
- Dağılım örtüşmesini nicel ölçme yöntemi.
- Kararlılık penceresi, eşik üstü devam süresi, izin verilen kesinti ve doğrulama süresi (süre-temelli; henüz belirlenmedi).
- Minimum SCT/PZEM örnek sayıları.
- 0.3 A aday çalışma sınırının deneylerle doğrulanması.
- Üç sınıfın gerçek OFF, 15 W ve daha yüksek yük verilerindeki hata/karışıklık oranları.

Bu parametreler gerçek verilerden önce sonuçlara bakarak keyfî biçimde ayarlanmayacak; deney protokolünde tanımlanıp bağımsız kayıtlarla doğrulanacaktır.

## 8. İlk doğrulama sırası

1. I007 uzun OFF oturumlarını çoğalt ve zaman içi değişimi ölç.
2. 15 W ON verisini aynı CH1-1T ölçüm zinciriyle tamamla.
3. OFF ve 15 W dağılımlarının ayrışmasını/örtüşmesini hesapla.
4. 100 W ve diğer sabit yük seviyelerini ayrı gruplar olarak karşılaştır.
5. Eşik ve karar sürelerini belirle; farklı oturumlarda doğrula.

**Sonuç:** BERO üç çıktı üretmeyi hedefler: AKIM VAR, AKIM YOK, AKIM HESAPLANAMADI. Özellikle son sınıf, fiziksel akım yokluğu ile ölçüm yetersizliğini birbirine karıştırmamak için zorunludur.


## 6.1 İki istatistiksel hedefin ayrılması

Üç durumlu sınıflandırma geliştirilirken iki ayrı problem çözülmelidir:

**A. Fiziksel akım var/yok karar kanıtı:** `NO_CURRENT` ile `CURRENT_PRESENT` ayrımı. K=24.22 uygulanmış CH1 serisi, OFF referansı ve yük ON/OFF pencereleriyle karşılaştırılır. Kullanıcının 0.20 A gözlemi aday sınırdır; tekil örnek eşiği değildir. Süreklilik, eşik çevresinde kalma süresi, pencere medyanı/MAD ve tekrarlı çevrim tutarlılığı değerlendirilir.

**B. Hesaplanamayan alanın istatistiksel çerçevesi:** `CURRENT_NOT_COMPUTABLE` için ölçümün OFF referansına yakınlığı, dağılım genişliği, dalgalanması, zaman içi kararlılığı ve ON/OFF dağılım örtüşmesi nicel tarif edilir. Her pencerede medyan, OFF medyanından fark, MAD, IQR/P05/P95, tepe-tepe aralığı, eşik çevresinde kalınan süre, en uzun devam süresi, örnek sayısı, gerçek zaman kapsaması ve timestamp boşlukları kaydedilir.

Bu iki hedef birbirine karıştırılmaz: bir pencere akım varlığını gösterebilir ancak amper hesabı için kararsız/uygunsuz olabilir. Benzer şekilde OFF referansına yakınlık tek başına fiziksel akımın kesin yokluğunu kanıtlamaz; zaman sürekliliği ve referans dağılımı ile birlikte değerlendirilir.
