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
- Kararlılık penceresi ve doğrulama süresi.
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
