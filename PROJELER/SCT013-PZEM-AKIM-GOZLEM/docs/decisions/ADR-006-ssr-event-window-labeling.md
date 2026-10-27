# BERO — SSR Olay Pencereleriyle PZEM/SCT Kararlılık Etiketleme Raporu

**Durum:** Tasarım yaklaşımı kayda alındı; doğrulama logları kullanıcı tarafından mevcut olarak bildirildi, rapora henüz eklenmedi.  
**Kapsam:** SSR ile yükün açılıp kapatılması, olay pencerelerinin kimliklendirilmesi ve bu pencerelerdeki PZEM/SCT ölçümlerinin etiketlenerek ileride eğitim/karşılaştırma amacıyla kullanılması.

## 1. Amaç

BERO'nun bu kolunda yük, ESP32-C3 SuperMini üzerinden kontrol edilen SSR ile planlı biçimde açılıp kapatılır. Yükün ON/OFF durum geçişleri ağ üzerinden olay mesajları olarak yayınlanır ve olaylara kimlik verilir. Bu olay kimlikleri, diğer ESP üzerindeki PZEM ölçümlerini ve SCT akım sensörlerinden elde edilecek verileri ortak deney pencerelerinde ilişkilendirmek için kullanılacaktır.

Hedef, yalnızca “yük açık/kapalı” ayrımı yapmak değildir. Amaç, belirli yük durumları içinde **kararlı ölçüm aralıklarını belirlemek**, bu aralıklara güvenilir etiketler atamak ve farklı sarım/ölçüm düzenlerine ait SCT verilerini aynı deney bağlamında eğitime ve karşılaştırmaya hazırlamaktır.

## 2. Bildirilen donanım ve yazılım düzeni

### 2.1 SSR kontrol ESP'si

- Denetleyici: ESP32-C3 SuperMini.
- Saat: DS3231 RTC ve NTP eşitleme yaklaşımı.
- Yük kontrolü: SAMM Market 5 V, iki kanallı SSR kartı.
- Planlanan çevrim: 40 saniye ON, 20 saniye OFF.
- Olay yayını: UDP broadcast, port 4210.
- Olay mesajı biçimi:
  `BERO_EVT,BOOT_ID=XXXXXXXX,EVENT_ID=N,STATE=ON|OFF`
- `BOOT_ID`, cihazın açılış oturumunu; `EVENT_ID`, o oturum içindeki olay sırasını ayırt etmeye yardımcı olur.

### 2.2 PZEM ölçüm ESP'si

- Kart: ESP32 tabanlı ayrı ölçüm düğümü.
- Ölçüm cihazı: PZEM-004T.
- UART: TX GPIO17, RX GPIO16, 9600 baud.
- Bildirilen ölçümler: gerilim, akım, güç, enerji, frekans ve güç faktörü.
- PZEM sensör güncelleme aralığı kodda 5 saniye olarak tanımlanmış.
- UDP alıcısı port 4210 üzerinden olay mesajlarını alacak şekilde yapılandırılmış.

### 2.3 Doğrulama durumu

Kullanıcı, iki kodun da ESP cihazlarında çalıştığını, haberleşmenin görüldüğünü ve doğrulama loglarının bulunduğunu bildirdi. İlgili loglar daha sonra paylaşılacak. Donanımın deney düzeneğinden sökülmüş olması, geçmişte alınan çalışma/haberleşme loglarının varlığını ortadan kaldırmaz; ancak bu raporda log içeriği görülmediği için test ayrıntıları, ölçülen zamanlama sapmaları ve kabul sonuçları bağımsız olarak doğrulanmış sayılmıyor.

## 3. Olay penceresi mantığı

SSR denetleyicisi her durum geçişini olay mesajıyla bildirir. `BOOT_ID + EVENT_ID + STATE` birleşimi, olayları yeniden başlatmalar arasında ayırt etmeye ve sıralamaya yarayan temel anahtardır. Zaman damgası ve PZEM örnekleriyle birlikte ele alındığında, yükün ON ve OFF olduğu dönemler oluşturulabilir.

40 s ON / 20 s OFF çevrimi tasarımda tanımlıdır. Analizde yalnızca planlanan zamanlamaya güvenmek yerine, alınan olay mesajı, yerel zaman damgaları ve ölçüm kayıtları birbiriyle eşleştirilmelidir. UDP yayınları tek başına her mesajın kesin teslim edildiğini garanti etmez; kayıp, tekrar veya sıra dışı gecikme olasılıkları veri işleme aşamasında göz önünde tutulmalıdır.

## 4. Kararlılık pencereleri ve etiketleme

Her ON/OFF dönemi, tek parça ve otomatik olarak “kararlı” kabul edilmeyecektir. Yük geçişinden hemen sonraki geçici rejim, PZEM'in ölçüm güncelleme gecikmesi ve SCT sinyalinin yerleşmesi nedeniyle kararlı bölgeden ayrı tutulmalıdır.

Önerilen veri işleme sırası:

1. Olay mesajlarını `BOOT_ID`, `EVENT_ID`, `STATE` ve zaman bilgisiyle kaydet.
2. PZEM ölçümlerini kendi zaman damgalarıyla kaydet.
3. SCT örneklerini ve/veya pencere özelliklerini aynı saat tabanına bağla.
4. Olay geçişlerine göre ON/OFF dönemlerini oluştur.
5. Geçiş sonrası yerleşme süresini ve kararlılık ölçütlerini deney protokolünde tanımla.
6. Ölçütleri sağlayan alt aralıkları “kararlı” olarak etiketle; geçiş, eksik veri veya tutarsız zaman bilgisi içeren aralıkları ayrı işaretle.
7. Aynı kararlı aralığa ait PZEM referans değerlerini ve farklı SCT sarım/konfigürasyonlarından gelen örnekleri ortak pencere kimliğiyle ilişkilendir.

Kararlılık eşiği ve geçiş sonrası dışlama süresi bu raporda sabitlenmemiştir; bunlar ölçüm sıklığı, yük türü ve gerçek loglar incelendikten sonra deney protokolünde belirlenecektir.

## 5. SCT sarım varyantlarıyla eğitim

Farklı sarım sayısı veya farklı SCT düzeniyle alınan ölçümler, hangi sensör/konfigürasyona ait oldukları açıkça belirtilerek etiketlenmelidir. Aynı ON/OFF olayı içinde bulunmaları tek başına aynı akım ölçeğine sahip oldukları anlamına gelmez.

Her veri penceresi için mümkün olduğunda şu alanlar korunmalıdır:

- Deney/oturum kimliği
- `BOOT_ID` ve `EVENT_ID`
- Olay durumu: ON veya OFF
- Pencerenin başlangıç ve bitiş zamanları
- Kararlılık etiketi ve etiketleme gerekçesi
- PZEM ölçümleri ve geçerlilik durumu
- SCT sensör kimliği, sarım/bağlantı konfigürasyonu ve örnekleme ayarları
- SCT penceresinden çıkarılan özellikler
- Eksik, geç, yinelenmiş veya şüpheli veri göstergeleri

Eğitim/karşılaştırma için kullanılacak hedef etiketin ne olduğu ayrıca tanımlanmalıdır: örneğin PZEM akımıyla kalibre edilmiş değer tahmini, ON/OFF sınıflandırması veya kararlı durumdaki SCT özelliklerinin modellenmesi. Bunlar birbirinden farklı görevlerdir ve aynı veri kümesinde karıştırılmamalıdır.

## 6. Mevcut koddan anlaşılan sınır

Paylaşılan PZEM alıcı kodunda UDP olaylarının alınıp loglanması tariflidir; bu sürümde olay ve PZEM ölçümlerini birleştiren kalıcı CSV/veri kümesi kaydı bulunmuyor. Bu nedenle olay mesajının alınması, tek başına eğitim için eşlenmiş bir veri kümesinin oluşturulduğu anlamına gelmez. Kalıcı kayıt ve eşleme adımı, sonraki geliştirme aşamasının parçasıdır.

## 7. Sonraki adımlar

1. Kullanıcının belirttiği SSR ve PZEM ESP doğrulama loglarını bu rapora kanıt bağlantıları olarak eklemek.
2. Loglardan olay teslimini, olay kimliklerinin sıralanmasını, RTC/NTP zaman damgalarını ve gerçek ON/OFF geçişlerini doğrulamak.
3. PZEM ölçümlerinin zaman damgası ve gerçek güncelleme davranışını doğrulamak.
4. SCT tarafının örnekleme, pencereleme ve sarım varyantı metaverisini tanımlamak.
5. Kararlılık ölçütü, geçiş sonrası dışlama süresi ve pencere etiket şemasını deney protokolünde kesinleştirmek.
6. Olaylar, PZEM ölçümleri ve SCT pencere özelliklerini ortak anahtarla kalıcı biçimde kaydetmek.

## 8. Sonuç

BERO için SSR kontrollü yük durumu, olay mesajları ve olay kimlikleri; PZEM ile SCT ölçümlerini deney pencereleri içinde hizalamaya yönelik temel zaman/olay iskeletini sağlar. Bir sonraki aşama, bu iskeleti loglarla belgelemek ve kararlılık kuralları tanımlanmış, sensör/konfigürasyon metaverisi korunmuş bir veri kümesine dönüştürmektir. Doğrulama logları paylaşılana kadar çalışma durumu “kullanıcı tarafından çalıştırıldığı ve haberleşmenin görüldüğü bildirildi; log incelemesi bekleniyor” olarak tutulacaktır.
