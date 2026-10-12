# HDF-002 — Alt Görev 1.2
## SCT kanal seçimi ve iki katmanlı prototip mimarisi

### Karar

Prototipte kullanılacak üç SCT kanalı:

- **ESP32D #1 → 1T SCT**
- **ESP32D #2 → 2T SCT**
- **ESP32E → 4T SCT**

3T SCT okumalarında yaşanan sorun nedeniyle mevcut prototipte 4T SCT kullanılacaktır. Bu, geçici seçim olarak değil, prototipin güncel sensör eşlemesi için alınmış yeni karar olarak kaydedilir. 3T ile ilgili geçmiş sorun ve deneyimler korunur; bu karar 3T sorununun çözüldüğü anlamına gelmez.

### İki katmanlı mimari

Bu düzen aynı zamanda iki katmanlı bir yapı oluşturur:

1. **Ölçüm katmanı:** Üç ayrı ESP kendi SCT sensörünü ve o kanala ait BIAS değerini okur. Ham kayıtlar sensör ve cihaz kimliğiyle korunur.
2. **Referans ve deney kontrol katmanı:** PZEM ESP yalnızca kendi PZEM cihazını okur; ayrı SSR kontrol ESP'si yükün deney döngüsünü yönetir. Bu işlevler SCT ESP'lerinin ölçüm görevini üstlenmez.

SSR için 55 saniye açık + 5 saniye kapalı döngüsü başlangıç zamanlama adayı olarak ayrıca kaydedilmiştir; optimum olduğu henüz doğrulanmış değildir.

### Kayıt ve kanıt sınırı

- 3T SCT'nin eski sorun kayıtları korunur ve 4T kayıtlarıyla karıştırılmaz.
- Her SCT kanalının kendi BIAS değerinin ölçülmesi yeni donanım modifikasyonu gerektirir; bu modifikasyon ayrı alt görevde takip edilir.
- Bu kayıt mimari ve sensör seçimi kararını tanımlar. Yeni düzenin kurulduğu veya üç sensörün başarıyla okunduğu iddia edilmez.

### Ek karar — kanal adı veride korunur, sarım sayısına göre ön bölme yapılmaz

- `1T`, `2T` ve `4T` etiketleri fiziksel kanal yapılandırmasını tanımlar; hesaplama öncesi bölme oranı değildir.
- Her veri kaydında `channel_id` (1T/2T/4T), `esp_id` ve ilgili `bias_id` korunur. Kalibrasyon parametresi aynı kanal kimliğiyle eşleştirilir.
- BIAS düzeltmesinden sonra veriler sarım sayısına göre önceden bölünmeden kalibrasyona girer. Ham kayıtlar korunur; dönüştürülmüş sonuçlar ayrı tutulur.
- Her kanal için ayrı (K) katsayısı deneysel aday olarak değerlendirilebilir. (K), en iyi sarım sayısını kanıtlamaz; yalnızca ampirik ilişki hakkında ipucu verir. Tek katsayının farklı akım seviyelerinde yeterliliği doğrulanmalıdır.
- (K) yeterli olmazsa daha genel kanal bazlı (F(x)) değerlendirilir. Hangi sarımın daha iyi olduğu; ham veri kalitesi, PZEM'e göre hata ve bağımsız doğrulama sonuçlarıyla değerlendirilir.
- Bu karar, ön bölmenin kesin olarak hataya neden olduğunun kanıtı değildir; amaç kalibrasyon öncesinde sarım oranı varsayımını veriye dayatmamaktır.

**İlgili aşamalar:** Alt Görev 1.1 (BIAS-kanal ilişkilendirmesi), P1 (kimlikleri koruyan arşiv), P2 (kanal bazlı olay eşlemesi/etiket), P3–P4 (ön bölmesiz ilk (F(x)) ve doğrulama), P5–P6 (aynı kanal/katsayı kimliğiyle paketleme ve canlı sınama).

**Kanıt sınırı:** Bu karar prototipin montajının, hesaplamanın veya kalibrasyonun tamamlandığını göstermez.

