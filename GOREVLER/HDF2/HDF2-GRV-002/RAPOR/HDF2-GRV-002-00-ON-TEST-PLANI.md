# HDF2-GRV-002 — Veri Motoru Ön Test Planı

**Tarih:** 2026-10-16 (görev adı/kapsam konumu güncellendi; planın ilk kayıt tarihi 2026-10-13)  
**Durum:** PLAN KAYDI — fiziksel test ve derleme henüz doğrulanmadı  
**Amaç:** ESP32-WROOM dahili ADC ile ham örnek yakalama altyapısını sınamak. Bu kayıt, sonraki dalga çizimi ve optimum hız adımlarından önceki ön test kapsamıdır.

## 1. Kapsam

Hedef 2 GRV-002 Veri Motoru ön testinde yalnızca ham veri yakalama ve aktarım davranışı değerlendirilecektir.

- Çift tampon mimarisi: Buffer A / Buffer B
- ADC örneklemesi USB aktarımını beklememeli.
- USB aktarımı ADC örneklemesini durdurmamalı.
- Ham örnekler önceliklidir; sıra ve örnek sayısı korunmalıdır.
- Hesaplama, filtreleme veya sinyal yorumu yapılmayacaktır.

## 2. İlk dalga yakalama hedefi

| Parametre | Hedef |
|---|---:|
| Şebeke frekansı | 50 Hz |
| Dalga sayısı | 5 tam periyot |
| Toplam kayıt süresi | 100 ms |
| Hedef örnekleme hızı | 10 kHz |
| Hedef örnek aralığı | 100 µs |
| Hedef örnek sayısı | 1.000 |
| ADC | ESP32-WROOM dahili ADC |
| Sinyal zinciri | SCT sinyali + mevcut BIAS devresi |
| ADC veri aktarımı | Örnekleme/kayıt tamamlandıktan sonra USB |
| MCP3208 | Kullanılmayacak |

**Not:** 10 kHz ve 100 µs hedef parametrelerdir; gerçekleşen örnekleme zamanlaması test verisinden doğrulanacaktır. Kodda hedef hızın tanımlanması tek başına zamanlama kanıtı sayılmaz.

## 3. Çift tampon ilkesi

1. ADC/DMA bir tampona örnek yazar.
2. Tampon tamamlandığında veri sahipliği güvenli biçimde diğer tampona aktarılır.
3. ADC diğer tampona devam ederken tamamlanan tampon USB aktarımına verilebilir.
4. USB aktarımı bitmeden ilgili tampon ADC tarafından yeniden kullanılmaz.
5. Tampon taşması, örnek kaybı veya aktarım hatası sessizce yok sayılmaz; sayaç/durum bilgisiyle görünür kılınır.

Çift tampon kullanımı tek başına kayıpsız çalışmayı garanti etmez. Tampon boyutu, üretim hızı, aktarım hızı ve tampon sahipliği birlikte doğrulanmalıdır.

## 4. Ön test kontrolleri

- [ ] Kaynak kod ESP32-WROOM hedefi için derleniyor.
- [ ] Kayıt sırasında seri/USB çıktı örnekleme döngüsünü bloke etmiyor.
- [ ] İstenen sayıda ham örnek alınıyor.
- [ ] Örneklerin sırası korunuyor.
- [ ] Tampon dolma/değişim olayları doğru yönetiliyor.
- [ ] USB aktarımı sırasında ADC örneklemesi sürüyor (çift tampon testi yapılırsa).
- [ ] Tampon taşması ve kayıp göstergeleri izleniyor.
- [ ] Gerçek örnek sayısı ve zamanlama kaydı mevcut.
- [ ] Aktarılan ham kayıt Mac'te yeniden okunarak bütünlük kontrolünden geçiyor.

Kontroller henüz çalıştırılmış veya başarılı olarak işaretlenmiş değildir.

## 5. Bu aşamada yapılmayacaklar

- RMS, ortalama, Peak veya Peak-Peak hesabı
- BIAS çıkarma
- Filtreleme veya dalga biçimi yorumlama
- Akım hesabı veya kalibrasyon
- Model / f(x) oluşturma
- 1T, 2T ve 4T kayıtlarını eşzamanlama
- MCP3208 kullanımı

## 6. Sonraki adımlar

1. Mevcut ve doğrulanabilir ADC sürekli örnekleme uygulamasını ESP32-WROOM hedefi için incele.
2. İlk testte 1.000 ham örneğin güvenilir biçimde alınıp USB ile aktarılmasını doğrula.
3. Ham kayıt doğrulandıktan sonra BIAS, SCT ve SCT−BIAS grafiklerini ayrı bir analiz adımında üret.
4. 10 kHz başlangıç referansını gerçek kayıtlarla doğrula; sonra 5 kHz, 2 kHz, 1 kHz ve 500 Hz adaylarını karşılaştırarak dalgayı yeterince temsil eden en düşük güvenli hızı seç.

## 7. Kanıt ve kayıt ilkesi

Bu belge bir plan ve ön test kontrol listesidir; fiziksel test, derleme başarısı veya veri kayıpsızlığı kanıtı değildir. Sonuçlar, kullanılan kod sürümü ve gerçek loglarla ayrı bir tarihli raporda tutulacaktır. Önceki görev ve deney kayıtları değiştirilmez.

**Sabit kapsam:** Bu görev, yalnızca Hedef 2 GRV-002 Veri Motoru ön testidir. 1T/2T/4T eşzamanlama ayrı bir step olarak kalır.

## 8. Python 3 — Masaüstü İlişki Atlası (ara rapor / öneri)

**Durum:** PLAN / ARAŞTIRMA ÖNERİSİ — uygulama ve veri doğrulaması yapılmadı.

**Numaralandırma kararı:** Bu çalışma Python 3 olarak konumlandırılır: masaüstünde çalıştırılacak **İlişki Atlası**. Model eğitimi bu görevin kapsamına alınmaz; ayrı sonraki aşama olarak Python 4'te kalır. Amaç, SCT'den çıkarılan her özelliğin PZEM etiketleriyle nasıl ilişkili olduğunu görsel olarak incelemek ve tek bir f(X) varsayımını peşinen kabul etmemektir.

### İlk grafikler

- SCT RMS → PZEM akım
- SCT Peak → PZEM akım
- SCT Peak-Peak → PZEM akım
- SCT StdDev → PZEM akım
- BIAS → ölçüm hatası (hata tanımı ve işareti ayrıca belgelenir)
- Veri mevcut olduğunda SCT özellikleri → PZEM PF, güç ve gerilim etiketleri

Her grafik üzerinde, veri yeterliyse:
- gözlenen veri noktaları;
- Pearson korelasyonu (r);
- doğrusal uyum için R²;
- trend çizgisi.

Doğrusal olmayan ilişki ihtimali görülürse, uygun trend eğrileri sonraki aşamada ayrıca karşılaştırılır. R² ve korelasyon tek başına nedensellik veya modelin genelleme başarısını kanıtlamaz. Aynı veriyle hem ilişki keşfi hem de nihai başarı iddiası yapılmamalıdır.

### Veri ilkeleri

- Ham kayıtlar değiştirilmez; özellik tabloları ve grafikler ayrı çıktılardır.
- PZEM ve SCT sabit alan kırpıcılarından gelen aralıklar zaman bilgisiyle eşleştirilir.
- Eşleştirme, kararlı alanların zaman örtüşmesi ve PZEM güncelleme gecikmesi dikkate alınarak yapılır.
- Her noktanın kaynak kayıt/çerçeve kimliği korunur; 55 saniye açık + 5 saniye kapalı deney çerçeveleri birbirine karıştırılmaz.
- İlişki Atlası model eğitmez; yalnızca veriyi görünür kılar ve sonraki modelleme kararlarına dayanak oluşturur.

### Olası ayrı ilişkiler

- Akım = f(SCT özellikleri)
- PF = g(dalga biçimi özellikleri)
- Güç = h(akım, PF, gerilim)

Bunlar doğrulanmış sonuç değil, veriyle sınanacak hipotezlerdir. Masaüstü Python uygulamasının kapsamı, mevcut CSV/özellik verileri ve zaman eşleştirmesi netleştikten sonra ayrı alt görevde belirlenecektir.



## 9. GRV-008 Freeze-1 kaydından alınan teknik katkılar

**Kaynak:** HDF2-GRV-003 içindeki `GRV-008-FREEZE-1-AKSAM-TEST-RAPORU.md` (2026-10-13). Bu bölüm yalnızca GRV-002 ön testine doğrudan katkı veren ham yakalama/aktarım ayrıntılarını devralır. Kaynak raporun tüm kapsamı GRV-002'ye taşınmış sayılmaz.

### 9.1 Donanım ve ham kayıt çerçevesi

- ESP32-WROOM dahili ADC kullanılacak; MCP3208 bu deneyin dışında.
- Aday girişler: GPIO34 / ADC1_CH6 = SCT, GPIO35 / ADC1_CH7 = BIAS. Fiziksel kablolama test öncesinde doğrulanmalı.
- Hedef: her kanal için 10 kHz; her frame 1.000 SCT + 1.000 BIAS örneği.
- Ham veriye bu aşamada RMS, BIAS çıkarma, filtreleme, kalibrasyon veya akım hesabı uygulanmaz.
- 1T/2T/4T eşzamanlama bu görevin kapsamı dışındadır.

### 9.2 Binary frame bütünlüğü

Kaynak raporda tanımlanan aday protokol: 9 adet uint32 başlık (36 bayt) + 2.000 adet uint16 örnek (4.000 bayt) + uint32 bitiş işareti (4 bayt) = toplam **4.040 bayt**. Python alıcısı toplam boyu ve son `0xCAFEBABE` marker'ını doğrulamalıdır. Seri akışta başlangıç marker'ı parçalı gelebileceği için marker aramasında son 3 bayt korunmalıdır.

Bu protokol GRV-002 için devralınan tasarım referansıdır; firmware derlemesi ve gerçek cihazdan aktarım doğrulanmadan çalışıyor kabul edilmez.

### 9.3 Tampon sahipliği ve kayıp göstergeleri

- ADC/DMA yazma tamponu ile USB aktarımına verilen tamponun sahipliği ayrılmalı; aktarım bitmeden aynı tampon yeniden kullanılmamalıdır.
- Ham tampon havuzu/kuyrukları ve frame kuyruğu kullanılıyorsa kuyruk taşmaları sessizce yok sayılmamalı; DMA overflow, ham kuyruk taşması ve frame kuyruğu taşması ayrı sayaçlarla raporlanmalıdır.
- Örnek indeksi, SCT ve BIAS örnek çiftinin ikisi de hazır olduğunda ilerlemelidir.
- Çift tampon tasarımı tek başına kayıpsızlığı kanıtlamaz; örnek sayısı, sıra, frame marker'ı ve taşma sayaçları gerçek kayıtta kontrol edilmelidir.

### 9.4 Zamanlama konusunda kritik sınır

DMA callback başlangıç/bitiş zamanları, ilk ve son fiziksel ADC örneğinin zaman damgası ile aynı şey değildir. Bu yüzden yalnızca callback zamanlarından hesaplanan frame süresi, 10 kHz örnek aralığını veya 100 ms gerçek kayıt süresini kanıtlamaz. Hedef hız tanımlanmış olması da ölçüm kanıtı değildir. Zamanlama ayrı ve güvenilir bir yöntemle doğrulanana kadar sonuç **bekliyor** kalır.

### 9.5 Test sırası ve kanıt

1. Önce sensör bağlı, yük yok koşulunda 100 frame almayı hedefle.
2. Frame sayısı/ID, marker, örnek sayısı ve sıra, frame süresi, BIAS ham değer istatistikleri ve taşma sayaçlarını kaydet.
3. Ham CSV'yi Mac üzerinde yeniden okuyup bütünlüğünü kontrol et; ilk beş frame grafiğini yalnızca ham ADC count olarak üret.
4. Sonraki yük testlerini ancak güvenli bağlantı ve temel ham kayıt doğrulandıktan sonra ayrı test adımları olarak uygula.

**Durum notu:** Kaynak raporda derleme, ESP'ye yükleme, 100 frame yakalama, fiziksel sensör testi, CSV ve grafik sonuçları beklemede olarak işaretlenmişti. Bu plan güncellemesi bu testlerin yapıldığını iddia etmez.

