# GRV-007 — Veri Motoru Ön Test Planı

**Tarih:** 2026-10-13  
**Durum:** PLAN KAYDI — fiziksel test ve derleme henüz doğrulanmadı  
**Amaç:** ESP32-WROOM dahili ADC ile ham örnek yakalama altyapısını sınamak. Bu kayıt, sonraki dalga çizimi ve optimum hız adımlarından önceki ön test kapsamıdır.

## 1. Kapsam

GRV Veri Motoru ön testinde yalnızca ham veri yakalama ve aktarım davranışı değerlendirilecektir.

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

**Sabit kapsam:** Bu görev, yalnızca GRV Veri Motoru ön testidir. 1T/2T/4T eşzamanlama ayrı bir step olarak kalır.

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

