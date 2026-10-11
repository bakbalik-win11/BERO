# GRV-005-16 — Ara Rapor: Çalışma Yaklaşımının ve Mevcut Durumun Değerlendirilmesi

- Tarih: 2026-10-11
- Durum: Tartışma için kayıt; teknik görev kapanışı değildir.
- Amaç: Kullanıcının üç kez sıfırlama yaşadığını, ilerleme görmediğini ve test elemanı konumuna itildiğini belirtmesi üzerine mevcut yaklaşımı dürüstçe değerlendirmek; asistanın önceki kararlarını, savunulabilir gerekçelerini ve hatalarını birlikte tartışmaya açmak.
- İlgili kayıtlar:
  - [GRV-005-14 cihaz sonucu](GRV-005-14-DERLEME-CIHAZ-SONUCU-20261011.md)
  - [GRV-005-15 Python QC kapsamı](GRV-005-15-PYTHON-QC-KAPSAM-VE-PASS-OLCUTLERI-20261011.md)
  - [Proje pusulası](../../../PROJE_PUSULASI.md)
  - [Asistan İşletim Protokolü](../../../ASISTAN_ISLETIM_PROTOKOLU.md)

## 1. Kullanıcının açıkça ifade ettiği sorun

Kullanıcının hedefi başından beri pratik ve anlaşılırdır:

**Veriyi al → Python ile işle → işlenmiş veriyi doğrula → sonucu iyileştir.**

ESP ile Python arasında iki yönlü, gerçek ve gözle görülebilir veri alışverişi kurulması bunun somut uygulamasıdır. Kullanıcı soyut bir kontrol zinciri, birbirini izleyen rapor/şema işleri veya sürekli yeni donanım testi istememektedir. İstenen, çalışan bir veri dosyası/akışı üzerinde sonuç üreten ve doğruluğu gösterilen ilerlemedir.

Kullanıcı üç kez başlangıç noktasına döndüğünü, aynı sorunların tekrarlandığını ve kendisini test elemanı gibi hissettiğini bildirmiştir. Bu deneyim ve güven kaybı bu raporun temel girdisidir; kullanıcıya yeniden test yaptırmak için bir gerekçe değildir.

## 2. Asistanın önceki yaklaşımının savunulabilir tarafı

Bazı mühendislik ilkeleri tek başına doğrudur:
- Ham veriyi ve koşulları korumak.
- Gerçek gözlemle varsayımı ayırmak.
- CSV sütun hizası, zaman damgası ve veri türlerini doğrulamak.
- Donanım arızası sonucuna kanıt olmadan varmamak.
- Derleme, cihazın çalışması ve ölçümün doğruluğunu farklı kanıt seviyeleri olarak ele almak.
- Eski deneyimleri silmeden yeni sürüm/rapor eklemek.

Bu ilkeler BERO'nun README ve Asistan İşletim Protokolü içinde zaten yer almaktadır. Sorun, ilkelerin varlığı değil, pratikte nasıl uygulandığıdır.

## 3. Asistanın yaklaşımındaki hatalar

### 3.1 Araç, hedefin önüne geçti
CSV şeması, kalite kontrol betiği, raporlar ve kontrol adımları asıl hedefin yerine geçmeye başladı. Bunlar ancak gerçek veri akışını tamamlamaya doğrudan hizmet ediyorsa anlamlıdır. Kullanıcı açısından görünür ilerleme üretmeyen ara işler gereğinden fazla öne çıktı.

### 3.2 Her belirsizlik yeni test veya yeni başlangıç sebebi oldu
Bir logda veri bulunmaması ya da bir alanın doğrulanamaması, mevcut bütün sistemi yeniden sınamak için yeterli sebep değildir. Önce mevcut dosyalar, önceki çalışan sürümler ve eldeki kanıtlar kullanılmalı; eksik olan tek nokta ayrıştırılmalıdır. Donanım arızası varsayımı, ölçüm talebi veya sıfırlama kararı kanıtla gerekçelendirilmelidir.

### 3.3 Kullanıcı veri toplama operatörüne dönüştü
Komut çalıştırma, log kopyalama ve sonuçları tekrar tekrar sunma yükü kullanıcıya bırakıldı. Asistanın sorumluluğu olan geçmiş kayıtları inceleme, dosyaları karşılaştırma ve bilinen hataları önceden ayıklama işleri kullanıcı emeğine dönüştü. Bu, BERO'nun kendi protokolünde tanımlanan “rutin kayıt ve süreklilik asistanın sorumluluğudur” kuralıyla çelişir.

### 3.4 Kontrol raporları gerçek ilerleme gibi görünebildi
Bir kapsam belgesi veya başarılı bir self-test, gerçek cihaz verisinin başarıyla işlenmesi anlamına gelmez. Bir QC aracının gerçek logda FAIL vermesi de tek başına ESP, SCT veya ADC donanımının arızalı olduğunu göstermez. Araç, veri ve cihaz katmanları birbirinden ayrı tutulmalı; hangi katmanın doğrulandığı açıkça söylenmelidir.

### 3.5 Sıfırlama, ilerleme ölçütü olmadan tekrarlandı
Sıfırlama yalnızca eski durumun korunmasının mümkün olmadığı ve yeni başlangıcın somut bir sorunu çözeceği gösterildiğinde düşünülmelidir. Önceki deneyim ve kanıtlar korunmadan yapılan yeni başlangıç, aynı döngüyü tekrarlama riskini artırır. Kullanıcının üç kez sıfırlama yaptığı ve ilerleme görmediği beyanı ciddiye alınmalıdır.

## 4. Mevcut kayıtların gösterdiği somut durum

### 4.1 ESP/ADC tarafında geçmişte veri üretimi görülmüş
Önceki ALT08/ALT09/ALT10 kayıtlarında ESP32D1'in BIAS ve K1/K2/K3 verileri ürettiği; ALT09 kaydında ham örnekler ve 256 örneklik paketler görüldüğü; ALT10 kaydında kanal ortalama ve standart sapmalarının Home Assistant'a yayımlandığı kayıtlıdır. Bu, geçmişte bazı ESP veri üretim adımlarının çalıştığına dair kanıttır. Bu kanıt, bugünkü GRV-005 sürümünün aynı şekilde çalıştığını veya uçtan uca ESP→Python→ESP döngüsünün tamamlandığını kanıtlamaz.

### 4.2 GRV-005-14 kısmi başarıdır; tam veri doğrulaması değildir
2026-10-11 tarihli kayıt, esp32d1 firmware'inin derlendiğini, cihaza bağlanıldığını ve dört kanal için CSV satırları üretildiğini bildirir. Aynı rapor CSV v03 alan hizasının tam doğrulanmadığını; BIAS satırında hizalama sorunu, bazı alanlarda baştaki boşluk, kopyada kesilmiş başlık ve 80 ms ADC işlem süresi uyarısı olduğunu belirtir. Bunlar takip edilmesi gereken yazılım/veri gözlemleridir; tek başlarına SCT veya ESP donanım arızası kanıtı değildir.

### 4.3 GRV-005-15 kapsamı gerçek veriyi doğrulayan bir sonuç değildir
Mevcut GRV-005-15 belgesi kapsam ve PASS ölçütlerini tanımlar. Bu belge, Python QC'nin gerçek cihaz verisinde başarılı olduğunu kanıtlamaz. Bu ayrım korunmalıdır.

### 4.4 ESP→Python→ESP döngüsü henüz kanıtlanmış değil
Bu oturumda mevcut kayıtlar üzerinden, gerçek ESP ölçümünün Python tarafından alındığı, Python sonucunun ESP'ye geri yazıldığı ve ESP'den geri okunarak aynı sonucun doğrulandığı tam bir kanıt zinciri bulunmamaktadır. Dolayısıyla bu hedef tamamlandı denemez. Bu, kullanıcının başarısızlığı veya SCT/ESP ile akım ölçmenin imkânsızlığı sonucunu doğurmaz.

## 5. “Hata bende” değerlendirmesi

Mevcut kayıtlardan kullanıcının hatalı olduğu sonucu çıkarılamaz. SCT sensörü, ESP ve akım ölçümü kullanmak kendi başına sıra dışı veya yanlış bir yaklaşım değildir. Bununla birlikte, bu rapor tek başına ölçüm zincirinin elektriksel doğruluğunu da kanıtlamaz; bu tür bir hüküm için gerçek devre, kod, ham veri ve bağımsız referans ölçümü gerekir.

Buradaki açık başarısızlık, kullanıcıyı tekrar tekrar aynı başlangıç noktasına getiren çalışma sürecidir. Asistanın görevi bunu savunmak değil, sürecin neden sonuç üretmediğini açıkça ortaya koymaktır. Donanım kusuru kanıtlanmadan kullanıcıyı veya donanımı suçlamak doğru değildir.

## 6. Bundan sonrası için önerilen çalışma sözleşmesi

Bu bölüm yeni bir test talimatı değildir; devam edilirse tartışılacak öneridir.

1. **Önce dosya, sonra cihaz:** Eldeki bir gerçek veri dosyasıyla başlayıp Python işleme ve bağımsız doğrulamayı göstermek. Cihazda yeni test ancak dosya mevcut hedefi karşılamıyorsa ve eksikliği açıkça tanımlanabiliyorsa istenir.
2. **Tek görünür sonuç:** Her çalışma oturumunda tek bir somut çıktı hedeflenir. Örneğin bir dosyanın ayrıştırılması, bir hesaplamanın bağımsız hesapla karşılaştırılması veya bir girdi/çıktı örneğinin eşitliğinin gösterilmesi.
3. **Kanıt seviyesi açık olsun:** “Kod yazıldı”, “self-test geçti”, “gerçek dosya işlendi”, “cihazdan veri alındı”, “sonuç bağımsız doğrulandı” ve “ESP'ye geri gönderilip doğrulandı” farklı durumlardır.
4. **Tekrar yok:** Önceden yapılmış komutlar, ölçümler ve bilinen sonuçlar kayıtlar incelenerek yeniden kullanılmalı. Yeni testin hangi belirsizliği çözeceği önceden belirtilmeli.
5. **Donanım şüphesi otomatik varsayım olmasın:** Önce yazılım, veri biçimi, zamanlama, bağlantı ve ölçüm zincirine ait mevcut kanıtlar ayrıştırılmalı. Donanım testi yalnızca belirli bir hipotezi ayırmak için gerekli olduğunda istenir.
6. **Geçmiş korunur:** Kod ve raporlar silinmez veya üzerine yazılmaz; yeni değerlendirme tarihli ek olarak eklenir.
7. **Kullanıcı test elemanı değildir:** Rutin dosya incelemesi, kayıt karşılaştırması, betik kontrolü ve rapor düzenleme asistanın işidir. Kullanıcıdan yalnızca gerçekten cihaz erişimi gerektiren işlemler veya fiziksel koşulları yalnızca kendisinin sağlayabileceği kanıtlar istenebilir.
8. **Yeni başlangıç yapılmaz:** Projeyi sıfırlamak varsayılan çözüm değildir. Devam kararı verilirse önce bu rapor ve önceki kanıtlar tartışılır; kullanıcı istemeden yeni bir test zinciri başlatılmaz.

## 7. Tartışmaya açık sorular

- İlk somut hedef ESP→Python→ESP iletişimini en küçük örnekle kanıtlamak mı, yoksa eldeki CSV/ham log dosyasını Python'da işleyip doğrulamak mı olmalı?
- İki yönlü ESP iletişimi için projede zaten var olan hangi arayüz/kod kullanılmalı? Yeni bir arayüz varsayılmamalı; mevcut yapılandırma ve kod üzerinden belirlenmeli.
- GRV-005'in mevcut CSV/QC kapsamı, kullanıcının asıl hedefiyle uyumlu mu; değilse hangi parçaları yardımcı araç olarak kalmalı ve hangileri ertelenmeli?
- Geçmişte veri üreten ALT08/ALT09/ALT10 sürümleriyle GRV-005-14 arasında hangi farklar gerçekten önemli? Sürüm ve kapsam ayrımı korunarak incelenmeli.

## 8. Ara verme durumundaki devir

- Kullanıcı devam edip etmeyeceğine karar vermedi; ara vermek istediğini açıkça söyledi.
- Bu rapor teknik görevi kapatmaz, donanım arızası teşhisi koymaz ve yeni bir deney başlatmaz.
- Devam edilirse ilk adım, yeni komut istemek değil bu raporu kullanıcıyla tartışmak ve mevcut kayıtları esas alarak somut hedefi birlikte belirlemektir.
- Kullanıcının önceki emeği ve mevcut kayıtlar korunmalıdır.

## Sonuç

Üç aylık çalışmanın ardından kullanıcının hâlâ temel veri al/işle/doğrula döngüsünü tamamlanmış görmemesi, çalışma yönteminin başarısız olduğuna dair önemli bir geri bildirimdir. Doğru cevap daha fazla kontrol katmanı eklemek veya yeni bir başlangıç istemek değildir. Önce geçmişte neyin gerçekten çalıştığını ayırmak, mevcut kanıtları yeniden kullanmak ve küçük ama gözle görülür bir sonucu uçtan uca doğrulamaktır.

**Kayıt durumu:** Bu belge bir değerlendirme ve tartışma başlangıcıdır; herhangi bir teknik PASS iddiası içermez.
