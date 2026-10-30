# SCT–PZEM Kararlılık Alanı Etiketleme ve Kalibrasyon Hedefi

**Durum:** Kullanıcı tarafından açıklanmış hedef mimari; uygulama/firmware ve deneyler henüz tamamlanmadı.  
**Kapsam:** T001 sırasında aktarılan mimariyi ve gelecekteki veri/modelleme akışını koruyan proje notu. Bu belge uygulanmış yazılım veya deney sonucu iddiası değildir.

## Ana hedef

Üç ayrı SCT örnekleme düğümünden ham/anlık sensör gerilimi örneklerini mümkün olduğunca az kayıpla toplamak. PZEM ve SCT'nin kararlı olduğu **alanları/dönemleri**, SSR olay paketleri ve geliştirilecek kararlılık algoritmaları/istatistikleriyle belirleyip etiketlemek. Python'da etiketlenmiş SCT verisi oluşturmak; bu veriyle her SCT için kalibrasyon katsayısı ve (f(x)) modelini çıkarmak. Ardından bulunan fonksiyonu çok sayıda paket/olay içeren ham veri üzerinde sınamak ve sonuçlara göre gerekirse modeli/algoritmayı iyileştirmek.

**Temel tasarım vurgusu:** Kullanıcının tarif ettiği yöntem salt zaman damgası veya olaydan sonra sabit bir süre sayarak etiketleme değildir. Esas yaklaşım **paket bağlamı + PZEM/SCT kararlı alanlarının belirlenmesi**dir. Zaman ve istek/yanıt bilgileri kayıtların izlenebilirliği ve inceleme için yararlı olabilir; fakat kararlılık etiketinin yerine geçmez. Sabit bir geçiş süresi (ör. eski teknik raporlardaki yaklaşık 3 s başlangıç maskesi) nihai etiketleme kuralı olarak varsayılmamalı; ancak deneylerde karşılaştırılacak başlangıç hipotezi olabilir.

## Hedef iş bölümü

- **ESP32-C3 SuperMini:** SSR anahtarlama ve zamanlama düğümü; ON/OFF olaylarını paket bilgisiyle yayımlar. Mevcut paket biçimi: `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF`.
- **SCT örnekleme düğümleri:** 2 × ESP32-WROOM-32D ve 1 × ESP32-WROOM-32E. Her düğüm SCT sinyalinin ham/anlık gerilim örneklerini hızlı ve düşük kayıpla toplar ve veriyi Home Assistant'a aktarır. İlk aşamada ESP düğümlerinin akım/RMS hesabı yapması hedeflenmiyor.
- **PZEM düğümü:** PZEM'in raporladığı ölçüm alanları ve paket/olay bağlamı, PZEM'in kararlı olduğu alanları belirlemek ve SCT kararlılığıyla ilişkilendirmek için kullanılır. PZEM kusursuz/altın standart kabul edilmez; alanların aynı yanıtta gelmesi içeride eşzamanlı yenilendiklerini kanıtlamaz.
- **Home Assistant:** ESP düğümlerinden gelen verilerin aktarılacağı hedef sistem.
- **Python (Mac Mini/PC):** Veri birleştirme, kararlılık algoritmaları ve istatistikleri geliştirme, alan etiketleme, kalibrasyon katsayısı/(f(x)) modelini çıkarma, modelin ham veri üzerinde doğrulanması ve iteratif iyileştirme. Temel hesaplama/modelleme ESP'lerde veya Home Assistant'ta değil Python tarafında yapılır.

## İlk eğitim aşaması — ortak kararlı alan etiketleme kuralı

Bu bölüm, BERO'nun ilk eğitim aşamasında uygulanacak temel etiketleme yöntemini tanımlar.

1. SSR yükü açar veya kapatır. SSR'nin `BOOT_ID`, `EVENT_ID` ve `STATE=ON|OFF` bilgisi ilgili test olayını ve ON/OFF penceresini tanımlar.
2. Aynı olay penceresindeki PZEM akım kayıtları Python'da incelenir; PZEM'in kararlı olduğu alan/alanlar belirlenir.
3. Aynı olay penceresindeki SCT ham verisinden çıkarılan pencere istatistikleri ayrıca incelenir; SCT'nin kararlı olduğu alan/alanlar bağımsız olarak belirlenir.
4. Python, PZEM kararlı alanı ile SCT kararlı alanının **aynı SSR olay penceresi içinde örtüştüğü ortak aralığı** bulur. Eğitim için kabul edilen bölüm yalnızca bu ortak kararlı aralıktır. Yalnız PZEM'in veya yalnız SCT'nin kararlı olması yeterli değildir.
5. Ortak kararlı aralıkta yer alan SCT verisi, o aralığa karşılık gelen geçerli PZEM akım değeriyle etiketlenir. Etiket, PZEM'in proje içi referans değerini temsil eder; PZEM kusursuz veya bağımsız mutlak standart kabul edilmez.
6. Aynı işlem hem SSR ON (yük açma) penceresi hem de SSR OFF (yük kapama) penceresi için uygulanır. Böylece açma ve kapama davranışlarından ortak kararlı alan örnekleri elde edilir.
7. Geçiş, yerleşme ve kararlı olmayan alanlar eğitim etiketi olarak kullanılmaz; ihtiyaç halinde analiz amacıyla ayrı sınıflandırılıp korunabilir.

**Zaman yaklaşımı:** Burada amaç her SCT örneğini PZEM okumasıyla milisaniye hassasiyetinde eşleştirmek değildir. İki taraftaki kararlılık ayrı ayrı bulunur ve aynı SSR olay penceresindeki örtüşen alan seçilir. Zaman damgaları ile PZEM istek/yanıt zamanları bu alanların sırasını, örtüşmesini ve PZEM güncelleme gecikmesini incelemek için kullanılır. Olaydan sonra sabit N saniye beklemek, ortak kararlı alanı bulmanın yerine geçmez.

**Kararlılık ölçütleri:** PZEM ve SCT için eşikler, pencere sayıları ve algoritmalar önceden uydurulmaz; ilgili deney verileriyle belirlenir. Bu kurallar belirlenip uygulanana ve fiziksel veriyle sınanana kadar yöntem hedef tasarımdır, doğrulanmış sonuç değildir.

## Kalibrasyon ve model doğrulama döngüsü

1. Kararlı alanlardan seçilen, PZEM bağlamı ve mümkünse bağımsız referans ölçümle desteklenen etiketli veriyi hazırla.
2. Python'da SCT başına kalibrasyon katsayısı ve/veya (f(x)) ilişkisini modelle.
3. Bulunan fonksiyonu yalnızca modelin çıkarıldığı kararlı örneklerde değil, çok sayıda paket ve olay içeren ham veri akışında da dene.
4. Hataları, yanlış etiketleri, geçiş davranışını ve veri kalitesini incele; gerekirse kararlılık algoritmasını, istatistiksel eşikleri veya fonksiyon biçimini iyileştir.
5. Sonuçları ayrı doğrulama verisi ve açık hata ölçütleriyle raporla. Deney yapılmadan model başarısı veya doğruluk iddia etme.
6. **Kabul hedefi (T003):** Python'da model tahmini geçerli PZEM akımından en fazla ±%4 bağıl sapıyorsa `OK` sayılır (`abs(prediction - pzem_current) / abs(pzem_current) <= 0.04`). Tam %4 sınır içindedir. Geçersiz PZEM okumaları ve sıfır referans akımı yüzdeyle sınıflandırılmaz; ayrı geçersiz/hesaplanamaz durum olarak tutulur.

## Sarım deneyleri

Aynı iletkenin SCT içinden geçirilme sayısı ayrı deneylerde 1 sarım, 2 sarım ve 4 sarım olarak değiştirilecektir. Bu deneylerden elde edilen etiketli örnekler sensör davranışını modellemek için kullanılacaktır. Her deneyde sensör/kanal kimliği, sarım sayısı ve kalibrasyon/model sürümü korunmalıdır. Henüz deney verisi veya doğrulanmış model yoktur.

## Geçmiş belgelerle ilişki ve dikkat

- Önceki teknik raporlar ve ADR'ler yaklaşık 1 s PZEM sorgusu, zaman kayıtları ve olay sonrası yaklaşık 3 s geçiş maskesi gibi başlangıç önerileri içeriyor. Bunlar daha önce hazırlanmış önerilerdir; kullanıcının burada açıkladığı **kararlı alan bazlı etiketleme** hedefiyle aynı şey değildir.
- ADR-003 ve ADR-006 mevcut durumlarıyla otomatik olarak değiştirilmiş sayılmaz. Uygulama öncesinde bu belgeler, paket bilgisinin SCT/PZEM tarafında nasıl erişilebilir olacağı ve etiketlerin nasıl üretileceği açısından açıkça gözden geçirilmelidir.
- Zaman damgaları yardımcı metadata olabilir; zaman bazlı eşleştirme veya sabit zaman maskesi, kararlılık alanını belirleyen esas ölçüt olarak varsayılmamalıdır.

## Açık kalanlar

1. Paket bilgisinin PZEM ve SCT verileriyle nasıl ilişkilendirileceği ve hangi düğümlerin paketi doğrudan alacağı.
2. Kararlılık alanı tanımı, algoritması, istatistiksel eşikler ve etiket şeması.
3. Home Assistant'a aktarım şeması, örnekleme hızı, tamponlama ve kayıp ölçüm yöntemi.
4. Kalibrasyonda kullanılacak referans, (f(x)) model biçimi, eğitim/doğrulama ayrımı ve hata ölçütleri.
5. Ham veride modelin çok paketli/olaylı koşullarda nasıl değerlendirileceği ve iyileştirme ölçütleri.

## Kayıt ilkesi

Bu belge kullanıcının açıkladığı hedefi kaydeder. Henüz yazılmamış SCT firmware'ini, yapılmamış deneyleri, belirlenmemiş algoritmaları veya doğrulanmamış kalibrasyon sonuçlarını mevcutmuş gibi göstermez.

## HA'dan PC'ye veri aktarımı

Veriler Home Assistant'ta toplandıktan sonra ayrı bir Python aktarım programı HA'dan kayıtları alıp PC'de saklayacaktır. Kararlılık analizi ve etiketleme de PC üzerinde çalışan Python programlarında yapılacaktır. PZEM akışı ile üç SCT kanalının kararlılık analizi ayrı yürütülecek; deneylerle geliştirilen kriterler kullanılarak etiketler üretilecektir. Aç/kapa olay paketleri verilerle ilişkilendirilecektir.

Bu bölüm hedef mimariyi tanımlar; aktarım ve analiz kodlarının uygulandığı anlamına gelmez.
