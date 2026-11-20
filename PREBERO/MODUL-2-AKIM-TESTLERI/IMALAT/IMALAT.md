# Modül 2 – Masaüstü 4 Kanal / Akım Testleri – İmalat Dosyası

> **Kayıt durumu: İMALAT PLANLANDI**
>
> Masaüstü deney düzeneği ESP32-D geliştirme kartı, ESP32 shield, SCT013 30A/1V akım sensörü ve ADS1115 ara entegresi kullanılarak imal edilecektir. Paylaşılan ESP32 + shield görseli yalnızca temsili yerleşim görselidir; kesin kart modeli, pinout veya kablo bağlantısı kanıtı değildir. Gerçek donanım incelenmeden bağlantı bilgisi uydurulmaz.

## 1. Modülün amacı ve kapsamı

- **Amaç:** SCT013 30A/1V sensöründen gelen akım sinyalini ADS1115 üzerinden okuyup ESP32-D tabanlı masaüstü düzende incelemek; deneysel ölçüm katsayılarını belirlemek.
- **Fiziksel kapsam:** ESP32-D geliştirme kartı, ESP32 shield, SCT013 30A/1V sensörü ve ADS1115 ara entegresi.
- **Çalışma prensibi:** SCT013 sensör sinyali ADS1115 girişine aktarılacak; ADS1115 sayısal ölçüm verisini ESP32-D kartına iletecek. Gerçek analog bağlantı, bias düzeni, besleme ve haberleşme ayrıntıları donanım üzerinde doğrulanarak kaydedilecek.

## 2. Donanım ve malzeme listesi

| Sıra | Parça / model | Adet | Görevi | Kayıt / doğrulama |
|---|---|---:|---|---|
| 1 | ESP32-D geliştirme kartı | 1 | Ana kontrol ve ölçüm kartı | Kullanılacak fiziksel kartın tam modeli henüz doğrulanmadı |
| 2 | ESP32 shield | 1 | Kart pinlerini bağlantı terminallerine taşımak | Shield'ın tam modeli ve pin eşleşmesi henüz doğrulanmadı |
| 3 | SCT013 30A/1V | Belirlenecek | Akım algılama ve analog sinyal üretimi | Kullanıcı tarafından belirtilen sensör modeli |
| 4 | ADS1115 | Belirlenecek | Harici ADC / ara entegre; sensör sinyalini sayısal okumaya dönüştürmek | Kullanıcı tarafından belirtilen entegre |
 
Ortak donanım ve envanter kayıtları ana depodaki `DONANIM/` ve `ENVANTER/` altında tutulur; burada yalnızca bu modülde fiilen kullanılan parçalar ve ilgili envanter referansları belirtilir.

## 3. Elektriksel bağlantılar

- **ESP32-D – shield bağlantısı:** Kart shield üzerine takılacak; gerçek kart ve shield üzerindeki işaretler kontrol edilerek doğrulanacak.
- **SCT013 – ADS1115 analog bağlantısı:** Gerçek sensör çıkışı ve gerekli bias/analog giriş düzeni doğrulandıktan sonra pin bazında kaydedilecek.
- **ADS1115 – ESP32-D haberleşmesi:** I²C bağlantısı olarak planlanmaktadır; SDA/SCL GPIO eşleşmeleri gerçek kart ve yazılım yapılandırmasıyla doğrulanmadan kesinleştirilmeyecek.
- **GPIO / pin eşleşmeleri:** Henüz doğrulanmadı; temsili görselden pinout çıkarılmayacak.
- **Besleme gerilimi ve akım gereksinimi:** ADS1115 ve gerçek kartların teknik gereksinimleri üzerinden belirlenecek.
- **GND / ortak referans:** Gerçek bağlantı topolojisine göre doğrulanacak.
- **İzolasyon ve koruma:** Deney bağlantıları belirlenmeden doğrulanmış kabul edilmeyecek.

### Bağlantı tablosu

| Kaynak / pin | Hedef / pin | Sinyal veya işlev | Kablo bilgisi | Doğrulama |
|---|---|---|---|---|
| ESP32-D | ESP32 shield | Kartın shield üzerine takılması | Kartın pin başlıkları | Fiziksel kurulumda kontrol edilecek |
| SCT013 30A/1V | ADS1115 analog giriş | Akım sensörü analog sinyali | Gerçek kablo/konnektör belirlenecek | Henüz pin bazında doğrulanmadı |
| ADS1115 | ESP32-D | I²C veri haberleşmesi | SDA, SCL, besleme ve GND | GPIO eşleşmeleri henüz doğrulanmadı |

## 4. Fiziksel yerleşim ve montaj

- **Ana yerleşim:** ESP32-D geliştirme kartı shield üzerine takılacak.
- **Sinyal zinciri:** SCT013 30A/1V → ADS1115 → ESP32-D.
- **Görsel referans:** Kullanıcının paylaştığı ESP32 ve shield fotoğrafı temsili görseldir; gerçek kartın fotoğrafı/ölçüsü değildir.
- **Kutu / montaj biçimi:** Henüz belirlenmedi.
- **Kablo güzergâhı ve sabitleme:** Gerçek montaj sırasında kaydedilecek.
- **Sökme / yeniden kurma notları:** Fiziksel imalat sonrasında eklenecek.

## 5. ESP ve yazılım eşleştirmesi

- **Kart ailesi / çalışma tanımı:** ESP32-D.
- **Shield:** ESP32 shield.
- **Harici ADC:** ADS1115.
- **Akım sensörü:** SCT013 30A/1V.
- **Fiziksel ESP envanter kimliği:** Kullanılacak fiziksel kart seçilip envantere eşleştirildiğinde yazılacak.
- **Sabit ESPHome cihaz adı:** Gerçek cihaz adı belirlendiğinde yazılacak.
- **İlgili görev:** `MOD2-GRV001`.
- **Not:** Fiziksel ESP kimliği, görev kimliği ve kod sürümü birbirinden bağımsızdır.

## 6. Fotoğraflar ve şemalar

Gerçek montaj ve bağlantı fotoğrafları `FOTOGRAFLAR/`, çizimler ve şemalar `SEMALAR/` altında saklanır. Paylaşılan görsel temsili ESP32/shield yerleşim referansıdır; gerçek montaj fotoğrafı olarak değerlendirilmez.

| Dosya | Açıklama | Revizyon / tarih | Durum |
|---|---|---|---|
| Kullanıcının paylaştığı ESP32 + shield görseli | Temsili kart/shield yerleşimi | 2026-11-21 | Referans; gerçek donanım fotoğrafı değil |

## 7. Montaj ve devreye alma sırası

1. Kullanılacak ESP32-D kartının ve shield'ın tam modellerini fiziksel olarak doğrula.
2. SCT013 30A/1V sensörünün uç/konnektör yapısını ve ADS1115 kartının girişlerini doğrula.
3. ADS1115 besleme ve I²C pinlerini gerçek kart üzerinden belirle.
4. SCT013 analog sinyalinin ADS1115 girişine güvenli ve uygun bias düzeniyle aktarılmasını planla.
5. Kartı shield üzerine yerleştir; pin sırası ve oturuşunu enerjisiz durumda kontrol et.
6. Besleme, polarite, ortak referans ve gerekli izolasyon kontrollerini yap.
7. İlgili görevde tanımlanan kod sürümünü ve cihaz eşleştirmesini doğrula.
8. İlk enerjilendirme ve işlev testini kontrollü şekilde gerçekleştir.
9. Gerçek fotoğrafları, bağlantı tablosunu ve sonuçları bu dosyaya ve ilgili sürümün LOG/RAPOR klasörüne kaydet.

## 8. Güvenlik ve sınırlamalar

- SCT013 akım trafosu sensörünün ölçtüğü iletken ve bağlantı düzeni, sensörün üretici talimatlarına uygun olmalıdır.
- Shield üzerindeki terminal bloklarının bulunması, bağlı devrelerin şebekeden izole olduğu anlamına gelmez.
- Şebeke gerilimi içeren deney bağlantıları için uygun izolasyon ve koruma doğrulanmadan bağlantı yapılmaz.
- Bağlantı kurma/değiştirme enerjisiz durumda yapılır.
- Temsili görsel, güvenli bağlantı veya pin eşleşmesi kanıtı değildir.

## 9. İmalat revizyon kayıtları

| Tarih | Değişiklik | Gerekçe | İlgili görev / kanıt |
|---|---|---|---|
| 2026-11-21 | İmalat yaklaşımı ESP32-D + ESP32 shield olarak tanımlandı | Kullanıcının donanım tanımı ve temsili görseli | `MOD2-GRV001/GOREV.md` |
| 2026-11-21 | SCT013 30A/1V sensör ve ADS1115 ara entegresi donanım zincirine eklendi | Kullanıcının donanım tanımı | `MOD2-GRV001/GOREV.md` |

## 10. Yeniden kurulum kontrolü

- [ ] ESP32-D kartının tam modeli doğrulandı.
- [ ] Shield modeli ve pin eşleşmeleri doğrulandı.
- [ ] SCT013 30A/1V sensör modeli ve bağlantısı doğrulandı.
- [ ] ADS1115 kartı, beslemesi ve I²C bağlantısı doğrulandı.
- [ ] Fiziksel ESP envanter kimliği kaydedildi.
- [ ] Bağlantı şeması gerçek montajla eşleşiyor.
- [ ] Kablolar ve pin eşleşmeleri kontrol edildi.
- [ ] Besleme ve güvenlik kontrolleri yapıldı.
- [ ] İlgili kod sürümü ve test durumu kontrol edildi.
- [ ] İlk çalıştırma logu ve sonuç raporu kaydedildi.
- [ ] Gerçek montaj fotoğrafları ve şemalar eklendi.

**Not:** İmalat planlanmıştır; fiziksel kurulum ve doğrulama tamamlanmış değildir.
