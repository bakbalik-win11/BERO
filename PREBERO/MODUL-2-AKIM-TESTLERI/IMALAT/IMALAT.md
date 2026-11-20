# Modül 2 – Masaüstü 4 Kanal / Akım Testleri – İmalat Dosyası

> **Kayıt durumu: FİZİKSEL KURULUM DEVAM EDİYOR**
>
> ESP32-D geliştirme kartı shield üzerine yerleştirilmiştir. ADS1115 modülü kablolarla düzeneğe bağlanmış olarak kullanıcı fotoğrafında görülmektedir. SCT013 30A/1V sensör bu fotoğrafta görünmemektedir; sensör modeli kullanıcı tarafından bildirilmiştir. Tüm sistemin imalatı ve elektriksel bağlantıları doğrulanmış değildir.

## 1. Modülün amacı ve kapsamı

- **Amaç:** SCT013 30A/1V sensöründen gelen akım sinyalini ADS1115 üzerinden okuyup ESP32-D tabanlı masaüstü düzende incelemek; deneysel ölçüm katsayılarını belirlemek.
- **Fiziksel kapsam:** ESP32-D geliştirme kartı, ESP32 shield, ADS1115 ara entegresi ve SCT013 30A/1V akım sensörü.
- **Sinyal zinciri:** SCT013 30A/1V → ADS1115 → ESP32-D.
- **Çalışma prensibi:** SCT013 sensör sinyali ADS1115 analog girişine aktarılır; ADS1115 sayısal ölçüm verisini I²C üzerinden ESP32-D kartına iletir. Gerçek analog bağlantı, bias düzeni, besleme ve haberleşme ayrıntıları ölçülerek/doğrulanarak kaydedilecektir.

## 2. Donanım ve malzeme listesi

| Sıra | Parça / model | Adet | Görevi | Kayıt / doğrulama |
|---|---|---:|---|---|
| 1 | ESP32-D geliştirme kartı | 1 | Ana kontrol ve ölçüm kartı | Kullanıcı fotoğrafında shield üzerine takılı görülüyor; kartın tam ürün varyantı ayrıca doğrulanacak |
| 2 | ESP32 shield | 1 | Kart pinlerini bağlantı terminallerine taşımak | Kullanıcı fotoğrafında ESP32-D kartıyla birlikte görülüyor; shield'ın tam modeli ayrıca doğrulanacak |
| 3 | ADS1115 modülü | 1 | Harici ADC / ara entegre | Kullanıcı fotoğrafında kablolarla düzeneğe bağlanmış görülüyor; pin eşleşmeleri henüz doğrulanmadı |
| 4 | SCT013 30A/1V | 1 | Akım algılama ve analog sinyal üretimi | Kullanıcı tarafından model olarak bildirildi; bu fotoğrafta görünmüyor |

Ortak donanım ve envanter kayıtları ana depodaki `DONANIM/` ve `ENVANTER/` altında tutulur; burada yalnızca bu modülde fiilen kullanılan parçalar ve ilgili envanter referansları belirtilir.

## 3. Elektriksel bağlantılar

- **ESP32-D – shield bağlantısı:** Fotoğrafta kart shield üzerine takılmış durumda.
- **ADS1115 – ESP32-D bağlantısı:** Fotoğrafta ADS1115 modülünden shield'a kablolar uzanıyor. Kablo renkleri görülse de tek başına renklerden SDA, SCL, besleme ve GND eşleşmesi kesinleştirilmeyecek.
- **SCT013 – ADS1115 analog bağlantısı:** Sensörün gerçek çıkışı ve gerekli bias/analog giriş düzeni doğrulandıktan sonra pin bazında kaydedilecek.
- **GPIO / I²C pin eşleşmeleri:** Henüz kesinleştirilmedi.
- **Besleme gerilimi ve akım gereksinimi:** Gerçek kart ve modül üzerindeki etiket/doküman ve ölçümle doğrulanacak.
- **GND / ortak referans:** Gerçek bağlantı topolojisine göre doğrulanacak.
- **İzolasyon ve koruma:** Deney bağlantıları belirlenmeden doğrulanmış kabul edilmeyecek.

### Bağlantı tablosu

| Kaynak / pin | Hedef / pin | Sinyal veya işlev | Kablo bilgisi | Doğrulama |
|---|---|---|---|---|
| ESP32-D | ESP32 shield | Kartın shield üzerine takılması | Kartın pin başlıkları | Fotoğrafta fiziksel yerleşim görülüyor |
| ADS1115 modülü | ESP32 shield | Besleme ve I²C bağlantıları | Fotoğrafta kırmızı, siyah, mavi ve yeşil kablolar görülüyor | Pin eşleşmeleri henüz doğrulanmadı; renklerden işlev çıkarılmadı |
| SCT013 30A/1V | ADS1115 analog giriş | Akım sensörü analog sinyali | Henüz kaydedilmedi | Henüz doğrulanmadı |

## 3.1. Kullanıcı tarafından bildirilen pin yapısı ve ölçüm ayarları

Bu bağlantı/ayar tanımı MOD2-GRV001 çalışmasına aittir. Fiziksel pinlerin ve elektriksel sınırların doğrulanması ayrıca yapılacaktır.

### Bağlantılar

| Kaynak | Hedef | İşlev |
|---|---|---|
| ESP32D2 GPIO21 | ADS1115 SDA | I²C veri |
| ESP32D2 GPIO22 | ADS1115 SCL | I²C saat |
| ESP32D2 3.3V | ADS1115 VDD | Besleme |
| ESP32D2 GND | ADS1115 GND | Ortak referans |
| ADS1115 ADDR | GND | I²C adresi 0x48 |
| SCT013 iki çıkış ucu | ADS1115 A0 ve A1 | Diferansiyel ölçüm girişi |

### Ölçüm ayarları

| Parametre | Değer |
|---|---|
| ADS1115 modu | Diferansiyel A0-A1 |
| PGA gain | 2.048 V |
| Sample rate | 860 SPS |
| Continuous mode | true |
| ct_clamp örnekleme penceresi | 200 ms |
| Sensör güncelleme aralığı | 1 saniye |
| Kalibrasyon katsayısı | 27.60 |
| Alt eşik | 0.005 A (5 mA) |

5 mA altındaki ölçümler bu sürümde sıfırlanır. Amaç, yüksüz durumda gözlenen yaklaşık 1–2 mA taban değerlerinin Home Assistant'a gereksiz veri üretmesini önlemektir.

### Kalibrasyon kaydı

- Önceki katsayı: 30.00
- ADS1115 gözlemi: yaklaşık 0.513 A
- PZEM gözlemi: yaklaşık 0.472 A
- Hesap: 30.00 × (0.472 / 0.513) = 27.60

Katsayı tek karşılaştırmadan türetilmiştir ve farklı akım seviyelerinde tekrar doğrulanmalıdır. PZEM referans karşılaştırma aracıdır; kusursuz ground truth değildir.

### ADS1115 giriş sınırı

ADS1115 girişleri GND − 0.3 V ile VDD + 0.3 V sınırları içinde kalmalıdır. PGA kazanç ayarı bu mutlak giriş sınırlarını değiştirmez. Diferansiyel ölçüm, A0 ve A1 pinlerinin mutlak giriş sınırlarını ortadan kaldırmaz.

**Kayıt notu:** Yukarıdaki pin ve ayarlar kullanıcı tarafından bildirilen yapılandırmadır. Kabloların fiziksel uçtan uca doğrulaması, A0/A1 mutlak gerilimlerinin sınırlar içinde olduğunun ölçümü ve çalışma logu ayrıca kaydedilecektir.

## 4. Fiziksel yerleşim ve montaj

- **Ana yerleşim:** ESP32-D geliştirme kartı shield üzerine takılmıştır.
- **ADS1115:** Ayrı modül olarak kablolarla shield üzerindeki bağlantılara bağlanmış görünmektedir.
- **SCT013:** Bu fotoğrafta görünmemektedir; sensör modeli kullanıcı tarafından SCT013 30A/1V olarak bildirilmiştir.
- **Kutu / montaj biçimi:** Henüz belirlenmedi.
- **Kablo güzergâhı ve sabitleme:** Mevcut fotoğraftaki geçici kablolama nihai montaj kabul edilmez.
- **Sökme / yeniden kurma notları:** Bağlantılar doğrulandıktan sonra eklenecek.

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

Gerçek montaj ve bağlantı fotoğrafları `FOTOGRAFLAR/`, çizimler ve şemalar `SEMALAR/` altında saklanır.

| Dosya | Açıklama | Revizyon / tarih | Durum |
|---|---|---|---|
| ESP32-D + shield + ADS1115 kullanıcı fotoğrafı | Fiziksel kart/shield yerleşimi ve ADS1115'e giden kabloları gösterir | 2026-11-21 | Kullanıcı fotoğrafıyla gözlendi; pin eşleşmelerini doğrulamaz |
| SCT013 30A/1V | Akım sensörü | — | Model kullanıcı tarafından bildirildi; bu fotoğrafta görünmüyor |

## 7. Montaj ve devreye alma sırası

1. ESP32-D kartının ve shield'ın tam modellerini fiziksel olarak doğrula.
2. ADS1115 modülünün pin etiketlerini ve besleme gereksinimini doğrula.
3. Mevcut kabloların iki uçtaki pin eşleşmelerini tek tek kontrol et.
4. ADS1115 ile ESP32-D arasındaki I²C bağlantısını doğrula.
5. SCT013 30A/1V sensör çıkışını ADS1115 analog girişine uygun bias ve koruma düzeniyle bağla.
6. Besleme, polarite, ortak referans ve gerekli izolasyon kontrollerini yap.
7. İlgili görevde tanımlanan kod sürümünü ve cihaz eşleştirmesini doğrula.
8. İlk enerjilendirme ve I²C iletişim testini kontrollü şekilde gerçekleştir.
9. Sensör sinyalini osiloskop ve ADS1115 okumalarıyla incele.
10. Gerçek bağlantı şemasını, fotoğrafları, logları ve sonuçları ilgili dosyalara kaydet.

## 8. Güvenlik ve sınırlamalar

- SCT013 akım trafosu sensörünün ölçtüğü iletken ve bağlantı düzeni, sensörün üretici talimatlarına uygun olmalıdır.
- Shield üzerindeki terminal bloklarının bulunması, bağlı devrelerin şebekeden izole olduğu anlamına gelmez.
- Şebeke gerilimi içeren deney bağlantıları için uygun izolasyon ve koruma doğrulanmadan bağlantı yapılmaz.
- Bağlantı kurma/değiştirme enerjisiz durumda yapılır.
- Fotoğraf fiziksel yerleşimi gösterir; elektriksel pin eşleşmesi veya güvenli bağlantı kanıtı değildir.

## 9. İmalat revizyon kayıtları

| Tarih | Değişiklik | Gerekçe | İlgili görev / kanıt |
|---|---|---|---|
| 2026-11-21 | ESP32-D + ESP32 shield imalat yaklaşımı tanımlandı | Kullanıcının donanım tanımı | `MOD2-GRV001/GOREV.md` |
| 2026-11-21 | SCT013 30A/1V ve ADS1115 sinyal zincirine eklendi | Kullanıcının donanım bildirimi | `MOD2-GRV001/GOREV.md` |
| 2026-11-21 | ESP32-D kartının shield üzerinde ve ADS1115 modülünün kablolarla bağlı olduğu fotoğrafla kaydedildi | Kullanıcının paylaştığı fiziksel kurulum fotoğrafı | Bu dosyanın 6. bölümü |

## 10. Yeniden kurulum kontrolü

- [ ] ESP32-D kartının tam modeli doğrulandı.
- [ ] Shield modeli ve pin eşleşmeleri doğrulandı.
- [ ] ADS1115 modül modeli, beslemesi ve I²C bağlantısı doğrulandı.
- [ ] SCT013 30A/1V sensör bağlantısı doğrulandı.
- [ ] Fiziksel ESP envanter kimliği kaydedildi.
- [ ] Bağlantı şeması gerçek montajla eşleşiyor.
- [ ] Kablolar ve pin eşleşmeleri kontrol edildi.
- [ ] Besleme ve güvenlik kontrolleri yapıldı.
- [ ] İlgili kod sürümü ve test durumu kontrol edildi.
- [ ] İlk çalıştırma logu ve sonuç raporu kaydedildi.
- [ ] Gerçek montaj fotoğrafları ve şemalar eklendi.

**Not:** ESP32-D/shield yerleşimi ve ADS1115 kablolaması fotoğrafta görülmektedir. SCT013 bağlantısı, pin eşleşmeleri ve bütün sistemin çalışması henüz doğrulanmış değildir.
