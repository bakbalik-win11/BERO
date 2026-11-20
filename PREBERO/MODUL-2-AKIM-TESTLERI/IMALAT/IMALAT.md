# Modül 2 – Masaüstü 4 Kanal / Akım Testleri – İmalat Dosyası

> **Kayıt durumu: İMALAT PLANLANDI**
>
> Bu modül ESP32-D geliştirme kartı ve ESP32 shield kullanılarak masaüstü deney düzeneği olarak imal edilecektir. Paylaşılan görsel yalnızca temsili yerleşim görselidir; kesin kart modeli, pinout veya kablo bağlantısı kanıtı değildir. Gerçek donanım incelenmeden bağlantı ve parça bilgisi uydurulmaz.

## 1. Modülün amacı ve kapsamı

- **Amaç:** ESP32-D ve shield tabanlı masaüstü düzende akım/sinyal davranışını incelemek ve deneysel ölçüm katsayılarını belirlemek.
- **Fiziksel kapsam:** ESP32-D geliştirme kartı, ESP32 shield ve görev deneyleri için gerekli çevre devreleri.
- **Çalışma prensibi:** Gerçek bağlantı ve deney yöntemi donanım kurulduktan ve doğrulandıktan sonra bu dosyaya işlenecek.

## 2. Donanım ve malzeme listesi

| Sıra | Parça / model | Adet | Görevi | Kayıt / doğrulama |
|---|---|---:|---|---|
| 1 | ESP32-D geliştirme kartı | 1 | Ana kontrol ve ölçüm kartı | Kullanılacak fiziksel kartın tam modeli henüz doğrulanmadı |
| 2 | ESP32 shield | 1 | Kart pinlerini bağlantı terminallerine taşımak | Shield'ın tam modeli ve pin eşleşmesi henüz doğrulanmadı |
| 3 | Deney çevre devreleri | — | İlgili test bağlantıları | Test planı ve gerçek donanıma göre kaydedilecek |

Ortak donanım ve envanter kayıtları ana depodaki `DONANIM/` ve `ENVANTER/` altında tutulur; burada yalnızca bu modülde fiilen kullanılan parçalar ve ilgili envanter referansları belirtilir.

## 3. Elektriksel bağlantılar

- **ESP32-D – shield bağlantısı:** Kart shield üzerine takılacak; gerçek kart ve shield üzerindeki işaretler kontrol edilerek doğrulanacak.
- **GPIO / pin eşleşmeleri:** Henüz doğrulanmadı; temsili görselden pinout çıkarılmayacak.
- **Besleme gerilimi ve akım gereksinimi:** Gerçek kart ve çevre devreleri belirlendiğinde kaydedilecek.
- **GND / ortak referans:** Gerçek bağlantı topolojisine göre doğrulanacak.
- **İzolasyon ve koruma:** Deney bağlantıları belirlenmeden doğrulanmış kabul edilmeyecek.

### Bağlantı tablosu

| Kaynak / pin | Hedef / pin | Sinyal veya işlev | Kablo bilgisi | Doğrulama |
|---|---|---|---|---|
| ESP32-D | ESP32 shield | Kartın shield üzerine takılması | Kartın pin başlıkları | Fiziksel kurulumda kontrol edilecek |
| Diğer bağlantılar | Henüz belirlenmedi | — | — | Henüz doğrulanmadı |

## 4. Fiziksel yerleşim ve montaj

- **Ana yerleşim:** ESP32-D geliştirme kartı shield üzerine takılacak.
- **Görsel referans:** Kullanıcının paylaştığı ESP32 ve shield fotoğrafı temsili görseldir; gerçek kartın fotoğrafı/ölçüsü değildir.
- **Kutu / montaj biçimi:** Henüz belirlenmedi.
- **Kablo güzergâhı ve sabitleme:** Gerçek montaj sırasında kaydedilecek.
- **Sökme / yeniden kurma notları:** Fiziksel imalat sonrasında eklenecek.

## 5. ESP ve yazılım eşleştirmesi

- **Kart ailesi / çalışma tanımı:** ESP32-D.
- **Shield:** ESP32 shield.
- **Fiziksel ESP envanter kimliği:** Kullanılacak fiziksel kart seçilip envantere eşleştirildiğinde yazılacak.
- **Sabit ESPHome cihaz adı:** Gerçek cihaz adı belirlendiğinde yazılacak.
- **İlgili görev:** `MOD2-GRV001`.
- **Not:** Fiziksel ESP kimliği, görev kimliği ve kod sürümü birbirinden bağımsızdır.

## 6. Fotoğraflar ve şemalar

Gerçek montaj ve bağlantı fotoğrafları `FOTOGRAFLAR/`, çizimler ve şemalar `SEMALAR/` altında saklanır. Paylaşılan görsel temsili yerleşim referansıdır; gerçek montaj fotoğrafı olarak değerlendirilmez.

| Dosya | Açıklama | Revizyon / tarih | Durum |
|---|---|---|---|
| Kullanıcının paylaştığı ESP32 + shield görseli | Temsili kart/shield yerleşimi | 2026-11-21 | Referans; gerçek donanım fotoğrafı değil |

## 7. Montaj ve devreye alma sırası

1. Kullanılacak ESP32-D kartının ve shield'ın tam modellerini fiziksel olarak doğrula.
2. Kartı shield üzerine yerleştir; pin sırası ve oturuşunu enerjisiz durumda kontrol et.
3. Shield üzerindeki terminal/pin etiketlerini gerçek kart pinleriyle karşılaştır.
4. Deney çevre devrelerinin bağlantı şemasını hazırla.
5. Besleme, polarite, ortak referans ve gerekli izolasyon kontrollerini yap.
6. İlgili görevde tanımlanan kod sürümünü ve cihaz eşleştirmesini doğrula.
7. İlk enerjilendirme ve işlev testini kontrollü şekilde gerçekleştir.
8. Gerçek fotoğrafları, bağlantı tablosunu ve sonuçları bu dosyaya ve ilgili sürümün LOG/RAPOR klasörüne kaydet.

## 8. Güvenlik ve sınırlamalar

- Shield üzerindeki terminal bloklarının bulunması, bağlı devrelerin şebekeden izole olduğu anlamına gelmez.
- Şebeke gerilimi içeren deney bağlantıları için uygun izolasyon ve koruma doğrulanmadan bağlantı yapılmaz.
- Bağlantı kurma/değiştirme enerjisiz durumda yapılır.
- Temsili görsel, güvenli bağlantı veya pin eşleşmesi kanıtı değildir.

## 9. İmalat revizyon kayıtları

| Tarih | Değişiklik | Gerekçe | İlgili görev / kanıt |
|---|---|---|---|
| 2026-11-21 | İmalat yaklaşımı ESP32-D + ESP32 shield olarak tanımlandı | Kullanıcının donanım tanımı ve temsili görseli | `MOD2-GRV001/GOREV.md` |

## 10. Yeniden kurulum kontrolü

- [ ] ESP32-D kartının tam modeli doğrulandı.
- [ ] Shield modeli ve pin eşleşmeleri doğrulandı.
- [ ] Fiziksel ESP envanter kimliği kaydedildi.
- [ ] Bağlantı şeması gerçek montajla eşleşiyor.
- [ ] Kablolar ve pin eşleşmeleri kontrol edildi.
- [ ] Besleme ve güvenlik kontrolleri yapıldı.
- [ ] İlgili kod sürümü ve test durumu kontrol edildi.
- [ ] İlk çalıştırma logu ve sonuç raporu kaydedildi.
- [ ] Gerçek montaj fotoğrafları ve şemalar eklendi.

**Not:** İmalat planlanmıştır; fiziksel kurulum ve doğrulama tamamlanmış değildir.
