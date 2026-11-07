# E16 — Yüksüz/düşük akım koşulunda SCT'nin ON/OFF davranışını gözlemleme

**Durum:** KAPATILDI — CH1 alt sınırı belirlendi; ayrı ON/OFF gözlemine gerek kalmadı  
**Tarih:** 2026-11-06  
**Faz:** Faz 2  
**İlişkili işler:** T007 (HA → PC), T008 (kararlılık/eşleştirme), E12 (SCT kararlılık ve tepki davranışı)

## Amaç

PZEM'in sıfır veya sıfıra yakın akım gösterdiği yüksüz koşulda, Modül 3'ün mevcut ON/OFF olay döngüsü sırasında SCT CH1 çıktısının nasıl davrandığını uzun süreli gözlemek. Ayrıca kullanıcının 18 W yükteki gözleminde SCT'nin akım seviyesini doğru okumak yerine açma-kapama değişimini algılıyor olabileceği hipotezini sonraki kontrollü tekrar için kaydetmek.

Bu deneyin ana sorusu: **SCT çıktısı fiziksel yük akımını temsil etmese bile ON/OFF olaylarıyla tekrarlanabilir biçimde değişiyor veya belirli seviyelere yerleşiyor mu?**

## Başlangıç gözlemi — HA grafiği

Kullanıcının 2026-11-06 tarihinde paylaştığı HA ekran görüntüsünde görülen anlık/ekran değerleri:
- PZEM gerilimi: 230,2 V.
- PZEM akımı: 0,000 A.
- Modül 2 CH1-1T Faz akım entity'si: 0,204 A.
- Aynı kanala ait Raw AC entity göstergesi: 0,00842 (ekran görüntüsünde birim açıkça doğrulanmadığından burada birim atanmamıştır).
- Zaman grafiğinde SCT akımı yaklaşık 0,18–0,30 A çevresinde basamaklı seyretmekte; daha yüksek tekil sıçramalar da görünmektedir. PZEM akımı sıfır çizgisindedir.

Bu değerler tek ekran görüntüsünden alınmış gözlem noktalarıdır; uzun dönem ortalaması veya deney sonucu değildir. Grafik, SCT'nin yüksüz koşulda kararlı bir ölçüm tabanı üretip üretmediğini tek başına kanıtlamaz.

## Kullanıcının 18 W gözlemi — hipotez

Kullanıcı, 18 W yükte SCT'nin gerçek akım seviyesini okumadığını; buna karşın yükün açılıp kapanmasını algılıyor gibi göründüğünü bildirdi.

Bu henüz tekrarlanmış/CSV ile doğrulanmış sonuç değildir. E16'nın gece boyu yüksüz kaydıyla karıştırılmayacak; 18 W koşulu daha sonra ayrı, kontrollü bir tekrar olarak ele alınacaktır. 18 W koşulunda PZEM'in eşzamanlı akım verisi ayrıca kontrol edilmelidir.

## Gece kaydı — ana koşul

- Home Assistant History üzerinden Modül 2 ve Modül 3'e ait ilgili kayıtlar birlikte dışa aktarılacak.
- PZEM gerilim ve akım entity'leri kayıtta tutulacak.
- SCT CH1 akım ve Raw AC entity'leri kayıtta tutulacak.
- Modül 3 ON/OFF olay işaretleri ile Modül 2'nin aldığı olay işaretleri kayıtta tutulacak.
- Ölçülen hatta yük bağlı değilse bu fiziksel koşul kayıt notuna açıkça yazılacak. Yük durumu farklıysa gerçek durum yazılacak; PZEM 0,000 A tek başına fiziksel yüksüzlüğün kanıtı sayılmayacak.
- Mevcut firmware, K, sample_duration, update_interval, pinler ve olay döngüsü bu gözlem için değiştirilmez. Değişiklik yapılmışsa gerçek ayarlar ayrıca kaydedilir.
- Gece boyunca kayıt alınır; sabah HA History dışa aktarımı CSV olarak korunur. Ham CSV değiştirilmez.

## İncelenecek sorular

1. Her ON/OFF çevriminde SCT CH1'de tekrarlanabilir bir değişim var mı?
2. SCT'nin ON ve OFF dönemlerindeki seviyeleri birbirinden ayrışıyor mu?
3. Olaydan sonra SCT çıktısı belirli bir banda yerleşiyor mu; yerleşme süresi çevrimler arasında benzer mi?
4. PZEM 0,000 A gösterirken SCT'nin 0,18–0,30 A çevresindeki çıktısı çevrimlerle ilişkili mi, yoksa benzer seviyede sürekli bir taban mı?
5. Modül 3'ün gönderdiği ve Modül 2'nin aldığı BOOT_ID/EVENT_ID/STATE işaretleri çevrimleri doğrulamaya yeterli mi?
6. Uzun kayıt boyunca tekil sıçramalar ve kalıcı seviye değişimleri birbirinden ayrılabiliyor mu?

## Analiz yöntemi ve sınırlar

- Önce ham CSV, gerçek kolon/entity adları, timestamp, birim ve kayıt aralığı doğrulanır.
- PZEM ve SCT akışları ayrı ayrı incelenir; olay işaretleri çevrimleri tanımlamak için kullanılır.
- Paket bütünlüğü mevcut ADR-024 kurallarına göre kontrol edilir.
- ON/OFF seviyeleri, dağılım, medyan, yüzdelikler, çevrimler arası tekrarlanabilirlik ve olay sonrası değişim raporlanır.
- Bu deneyde eğitim etiketi veya kalibrasyon katsayısı üretilmez.
- Yüksüz ON/OFF davranışı, yük akımının doğru ölçüldüğü anlamına gelmez. Olay değişimini algılama ile akım genliğini ölçme ayrı kabiliyetler olarak değerlendirilir.
- 18 W hakkındaki gözlem bu geceki yüksüz kayıtla doğrulanmış sayılmaz.

## Sabah teslim edilecek kaynaklar

- Modül 2 + Modül 3'ü kapsayan HA History CSV.
- Mümkünse aynı zaman aralığına ait ekran görüntüsü veya kısa not.
- Fiziksel koşul: hatta yük bağlı mıydı, 18 W yük var mıydı, başka değişiklik yapıldı mı?
- Kayıt boyunca firmware/ayar değişikliği yapıldıysa ayrıntısı.

Kaynak CSV ilk haliyle korunacak; dosya hash'i ve boyutu alım sırasında kaydedilecek.

## Kapanış — kullanıcı kararı

E16, CH1'in yüksüz/ölçülemeyen düşük akım bölgesini yeniden ON/OFF döngüsüyle araştırma ihtiyacı kalmadığı için kapatıldı. Projenin ihtiyacı sensörün olay değişimini ayrıca kanıtlamak değil, mevcut CH1 kurulumunun ölçüm alt sınırını ve bunun altındaki ölü/hesaplanmayan bölgeyi tanımlamaktır. Kullanıcı kararıyla bu sınır belirlenmiştir.

Bu kapanış, SCT'nin her düşük akımda genlik ölçebildiği veya tüm ON/OFF koşullarında sınıflandırma yaptığı anlamına gelmez. Alt sınır ve hesaplanmayan bölge yalnız mevcut CH1 kurulumuna aittir. Sonraki aşama Python veri analizi ve yük davranışlarının eğitim/sınıflandırma açısından incelenmesidir.

**SONUÇ:** KAPATILDI — tekrar deney planlanmayacak. Ham kayıt varsa kaynak niteliğini korur; yeni etiket veya kalibrasyon bu deneyden üretilmez.

## İlgili kararlar
- [ADR-024 — Python ON/OFF paket bütünlüğü](../../docs/decisions/ADR-024-python-packet-completeness-validation.md)
- [ADR-028 — Kararlı alan SCT ile kapanacak](../../docs/decisions/ADR-028-stable-window-sct-boundaries.md)
- [E12 — SCT kararlı alan tespiti ve PZEM örtüşmesi](../E12-sct-stability-window-and-response/README.md)
