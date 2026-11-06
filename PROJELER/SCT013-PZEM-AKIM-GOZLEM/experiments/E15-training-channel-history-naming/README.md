# E15 — Eğitim işaretli kanal adlarının Home Assistant History doğrulaması

**Durum:** PLANLANDI — kod değişikliği ve fiziksel doğrulama bekliyor  
**Planlama tarihi:** 2026-11-06  
**Faz:** Faz 2  
**İlişkili karar:** [ADR-027 — tek kanallı eğitim veri setleri ve History adlandırması](../../docs/decisions/ADR-027-single-channel-training-datasets.md)  
**İlişkili görevler:** T007 (HA History dışa aktarımı), T008 (ileride eğitim verisi hazırlama)  
**İlişkili deneyler:** E12 (kararlı alan gözlemi), E14 (tek kanal 2 Hz denemesi)

## 1. Amaç

Günlük deneylerde kullanılan genel kanal adlarından, yalnız eğitim verisi toplanmasına karar verildiğinde kullanılacak eğitim işaretli kanal adlarına küçük bir kod değişikliğiyle geçilebildiğini gerçek ESPHome → Home Assistant → History zincirinde doğrulamak.

Bu deneyin doğruladığı konu ölçüm doğruluğu, kararlılık veya örnekleme hızı değildir. Yalnızca kanal adlandırmasının koddan HA'ya doğru taşınması, History'de ayırt edilebilir olması ve dışa aktarılan CSV'de doğru kaynak olarak görünmesidir.

## 2. Kabul edilen adlandırma

| Fiziksel kanal | Genel deney adı | Eğitim amaçlı History adı |
|---|---|---|
| CH1 | `CH1` | `CH1-E` |
| CH2 | `CH2` | `CH2-E` |
| CH3 | `CH3` | `CH3-E` |

`-E` eki yalnız eğitim amacıyla yayınlanan History akışını işaretler. Sarım sayısı, katsayı veya hesaplama yöntemi adın parçası değildir.

## 3. Deney sınırı

- Mevcut üç kanallı Modül 2 okuma düzeni korunur.
- Üç kanalın fiziksel pinleri, SCT bağlantıları, bias bağlantısı, sarım sayıları, K katsayısı, sample_duration, update_interval, okuma sırası ve ölçüm hesaplaması değiştirilmez.
- Yalnız kanalın HA'da görünen adını/kimliğini eğitim işaretli hale getirmek için gereken en küçük kod alanları değiştirilir.
- Çalışan YAML doğrudan üzerine yazılmaz. Önce depodaki gerçek çalışan dosya bulunur, kopyası alınır ve deney sürümü ayrı dosyada tutulur.
- Deney sırasında alınan kayıtlar henüz eğitim veri seti ilan edilmez; bu bir adlandırma ve History doğrulama denemesidir.
- Firmware yükleme/OTA öncesinde kullanıcıyla dosya, kart ve geri dönüş sürümü doğrulanır.

## 4. Ön koşullar

1. Modül 2'nin o anda çalışan YAML dosyasını depodan bul ve tam içeriğini oku.
2. Çalışan dosyanın Git commit/blob SHA bilgisini deney notuna yaz.
3. Home Assistant'taki mevcut üç kanalın gerçek `entity_id`, görünen ad ve mevcut History kayıtlarını not et.
4. Üç kanalın fiziksel eşlemesini test öncesi doğrula:
   - CH1: sarı / GPIO32
   - CH2: yeşil / GPIO33
   - CH3: mavi / GPIO34
   - Ortak bias: GPIO35
5. Fiziksel sarım/geçiş sayıları o anki gerçek bağlantıya göre not edilir; eski 1/4/3 değerleri varsayılmaz.
6. Deney YAML'ı ayrı dosyaya kopyalanır. Orijinal çalışan YAML korunur.

## 5. Uygulama yöntemi

### A — Başlangıç kaydı

- Mevcut firmware ile kısa bir History kaydı al.
- Üç kanalın HA'daki gerçek entity_id ve görünen adlarını dışa aktarım veya ekran kaydıyla not et.
- Başlangıçta ölçüm ayarlarını ve kod sürümünü kaydet.

### B — Yalnız adlandırma değişikliği

- Deney YAML'ında CH1, CH2, CH3 kanallarının HA'ya sunulan adlarını sırasıyla `CH1-E`, `CH2-E`, `CH3-E` yap.
- ESPHome `name`, `id`, `unique_id`, entity registry ve `entity_id` ilişkisini dosyanın gerçek yapısına göre incele. Sırf görünen adı değiştirmek entity_id'nin de değişeceğini varsayma.
- Ölçüm hesabına, pinlere, filtreye, katsayıya, örnekleme/çağrı sürelerine veya olay protokolüne dokunma.
- YAML doğrulaması/derlemesi yap; derleme çıktısını kaydet.
- OTA/kurulum öncesi kullanıcı onayı al ve geri dönüş dosyasını hazır tut.

### C — Home Assistant doğrulaması

- Deney firmware'ini yükle.
- HA cihaz/entity sayfasında üç kanalın görünen adlarını ve gerçek `entity_id` değerlerini kontrol et.
- History'de üç eğitim işaretli akışın ayrı ayrı oluştuğunu doğrula.
- Eğer HA entity registry eski `entity_id` değerini korursa, bunu deney sonucu olarak kaydet. Entity kimliğini değiştirmek için ayrıca ve kontrollü bir işlem gerekebilir; bu deney sırasında otomatik veya varsayımla registry müdahalesi yapılmaz.

### D — Kısa kayıt ve CSV kontrolü

- Uygun, güvenli ve sabit bir test yüküyle kısa kayıt al; yük ve fiziksel test koşulu kullanıcı tarafından belirlenir.
- Üç kanalda yeni kayıtların geldiğini, timestamp'lerin ilerlediğini ve doğru kanal adına yazıldığını kontrol et.
- HA History'den CSV dışa aktar.
- CSV içinde `entity_id` alanında beklenen eğitim akışlarının bulunup bulunmadığını kontrol et. Görünen ad ile gerçek entity_id ayrı ayrı raporlanır.
- Kaynak CSV değiştirilmeden arşivlenir; test için kopya/özet ayrı tutulur.

### E — Geri dönüş

- Test tamamlandığında kullanıcı kararıyla önceki çalışan YAML'a dön veya deney YAML'ını koru.
- Geri dönüş sonrası genel deney adlarının tekrar çalıştığını doğrula.
- Hangi firmware sürümünün cihazda kaldığını STATUS'a yaz.

## 6. Kaydedilecek göstergeler

- Önceki YAML yolu, Git commit ve blob SHA.
- Deney YAML yolu ve değişen satırlar.
- ESPHome doğrulama/derleme sonucu ve gerçek log.
- OTA/kurulum sonucu (yapıldıysa).
- Her kanal için önceki ve sonraki görünen ad.
- Her kanal için önceki ve sonraki gerçek `entity_id`.
- HA History'de kayıt oluşup oluşmadığı.
- CSV'deki gerçek `entity_id` değerleri ve satır sayıları.
- Test yükü, test zamanı ve fiziksel kanal/sarım yapılandırması.
- Geri dönüş yapıldıysa sonucu.

## 7. Kabul ölçütleri

Deney yalnız aşağıdaki koşulların tümü doğrulanırsa adlandırma testi başarılı sayılır:

1. Üç fiziksel kanalın ölçüm davranışını değiştiren hiçbir ayar veya hesaplama değiştirilmemiş olmalı.
2. HA'da CH1, CH2, CH3 akışları eğitim işaretli adlarıyla açıkça ayırt edilebilmeli.
3. Gerçek entity_id değerleri kaydedilmiş ve CSV dışa aktarımında doğrulanmış olmalı.
4. History'deki kayıtlar doğru fiziksel kanalla eşleşmeli; kanal karışması olmamalı.
5. Ham dışa aktarım dosyası değiştirilmeden korunmalı.
6. Orijinal çalışan YAML'a geri dönüş yolu korunmuş olmalı.

Görünen ad değişmiş ama CSV'deki entity_id beklenen şekilde ayrışmamışsa deney kısmen başarılıdır; Python seçim kuralı kesinleştirilmeden önce entity registry davranışı ayrıca çözülür.

## 8. Bu deneyin kanıtlamadığı konular

- SCT ölçüm doğruluğu veya ±%4 kabulü.
- Kararlılık penceresi ya da PZEM/SCT eşleşmesi.
- Python-1 veya Python-2'nin çalışır durumda olması.
- Eğitim veri setinin hazır olması.
- Üç kanalın aynı modelde birleştirilebileceği.
- Yeni entity adlarının geçmişteki eski History kayıtlarını geriye dönük yeniden adlandıracağı.

## 9. LOG / SONUÇ

Henüz uygulanmadı. Kod kopyası, YAML değişikliği, derleme, OTA, HA History ve CSV doğrulaması yapılmadı. Sonuç alanı gerçek deneyden sonra doldurulacaktır.

## 10. Kontrol listesi

- [ ] Depodaki gerçek çalışan Modül 2 YAML dosyasını bul ve oku.
- [ ] Çalışan YAML'ın commit/blob SHA bilgisini kaydet.
- [ ] HA'daki mevcut görünen adları ve entity_id değerlerini kaydet.
- [ ] Ayrı E15 YAML kopyasını oluştur.
- [ ] Yalnız CH1-E / CH2-E / CH3-E adlandırma değişikliğini yap.
- [ ] YAML doğrulaması ve derleme yap.
- [ ] Kullanıcı onayıyla firmware yükle.
- [ ] HA cihaz/entity ekranında adları ve entity_id değerlerini doğrula.
- [ ] Kısa History kaydı al ve CSV dışa aktar.
- [ ] CSV entity_id alanlarını doğrula.
- [ ] Ham CSV, gerçek log ve sonuç yorumunu kaydet.
- [ ] Geri dönüş durumunu doğrula ve STATUS'u güncelle.
