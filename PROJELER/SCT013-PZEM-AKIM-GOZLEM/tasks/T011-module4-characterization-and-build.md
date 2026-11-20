# T011 — Modül 4 teknik inceleme, tasarım ve imalat kapısı

- **Durum:** PLANLANDI — ilk adım aktif sıradaki iş
- **Öncelik:** PREBERO Modül 5/6/7'nin ön koşulu
- **Bağlayıcı mimari karar:** [ADR-035](../docs/decisions/ADR-035-module4-design-gate-before-prebero.md)

## Amaç

Masaüstünde geçici olarak çalışan ESP32D2 + ADS1115 + SCT düzeneğini teknik olarak anlamak, bias ve giriş yapısı hakkında kanıta dayalı karar vermek, Modül 4'ün fiziksel tasarımını belirlemek ve sabit donanım olarak imal edip doğrulamak.

Modül 4 tamamlanmadan PREBERO Modül 5/6/7 imalatına başlanmaz.

## Kapsam ve yaklaşım

Çalışma hobi düzeyinde tutulur. Amaç ADS1115 hakkında akademik/laboratuvar düzeyinde karakterizasyon yapmak değil, BERO'da doğru ve güvenli kullanım için gereken özellikleri anlamaktır. Üreticinin elektriksel sınırları mutlaka dikkate alınır.

## Aşamalar ve kabul koşulları

### 1. ADS1115 donanım raporu

- ADS1115'in temel çalışma mantığı ve delta-sigma ADC kavramı.
- 16 bit çözünürlüğün pratik anlamı.
- Single-ended ve diferansiyel giriş.
- PGA kazanç aralıkları ve seçilen aralığın ölçüm çözünürlüğüne etkisi.
- Örnekleme hızları ve BERO kullanımına etkisi.
- Besleme gerilimi, analog giriş pinlerinin izin verilen gerilim aralığı ve mutlak maksimum sınırlar.
- SCT sinyalinin ölçülmesinde negatif diferansiyel sonuç ile bir giriş pininin GND altına inmesi arasındaki fark.
- BERO için pratik sonuçlar ve kısa terimler sözlüğü.

**Kabul:** Üretici veri sayfasına dayanan, kaynakları belirtilmiş ve BERO kullanımına bağlanmış anlaşılır bir rapor. Laboratuvar karakterizasyonu veya tüm hata parametrelerinin ayrıntılı analizi gerekmiyor.

### 2. Masaüstü bağlantı incelemesi

- SCT modelini ve fiziksel bağlantısını doğrula.
- Burden/ön uç yapısını ve varsa bias bağlantısını fiziksel olarak belirle.
- ADS1115 beslemesini, GND ortaklığını, AIN0/AIN1 bağlantılarını ve I²C bağlantısını kaydet.
- Mevcut ESPHome/firmware ayarlarını gerçek cihazla eşleştir.
- Bilinmeyen veya fotoğrafla doğrulanamayan noktaları açık bırak.

**Kabul:** Gerçek bağlantıyı gösteren açıklamalı şema/fotoğraf ve ayar listesi.

### 3. Biaslı/bias'sız ölçüm karşılaştırması

- Aynı SCT ve ADS1115 ölçüm zincirini kullan.
- Test yükü ve koşulları mümkün olduğunca aynı tut.
- Her iki bağlantı için ölçüm logu ve deney koşullarını sakla.
- Sonuçları gözlem olarak yaz; tek deneyden genelleme yapma.

**Kabul:** Karşılaştırılabilir iki kayıt ve kısa yorum.

### 4. Osiloskopla sinyal gözlemi

- Önce bias'sız, sonra bias'lı düzeni gözlemle.
- AIN0-GND, AIN1-GND ve AIN0-AIN1 dalga biçimlerini incele.
- DC çalışma noktası, salınım, olası kırpılma ve gürültüyü gözlemle.
- Ekran görüntülerini zaman tabanı, volt/div ve prob ayarıyla sakla.
- Yalnız uygun ve izole edilmiş düşük gerilimli ölçüm tarafında çalış; şebeke iletkenlerine doğrudan prob bağlama.

**Kabul:** İki yapıya ait açıklamalı osiloskop görüntüleri ve gözlem notu. Osiloskop görüntüsü tek başına doğruluk sertifikası değildir.

### 5. Modül 4 tasarım kararı

Aşağıdaki başlıkları deney kanıtına göre kararlaştır:
- SCT ve ADS1115 giriş bağlantı topolojisi.
- Bias gerekliliği ve gerekiyorsa bias üretim yöntemi.
- ADS1115 besleme ve referans/GND düzeni.
- ESP32 ile I²C ve güç bağlantıları.
- Kablo, konektör, montaj ve kutu/yerleşim.
- Modülün bakım ve erişim gereksinimleri.

**Kabul:** İmalata esas alınabilecek bağlantı şeması, parça listesi ve kısa tasarım gerekçesi. Kanıtı olmayan seçimler açık karar olarak bırakılır.

### 6. Modül 4 imalatı ve doğrulaması

- Tasarım kararına göre sabit fiziksel modülü kur.
- Gerçek pin/kablo/konektör bağlantılarını imalat kaydına işle.
- Firmware yapılandırmasını ve kullanılan sürümleri kaydet.
- Uygun düşük gerilim kontrollerini ve gerçek SCT ölçüm testini yap.
- Başarılı log/çıktı ile teknik yorumunu sakla.

**Kabul:** Fiziksel modül, doğrulanmış bağlantı kaydı ve gerçek donanım çalışma kanıtı. Yalnız masaüstü prototipin çalışması imalatın tamamlandığı anlamına gelmez.

### 7. PREBERO geçiş kapısı

Modül 4 kabul koşulları karşılandıktan sonra:
- Modül 5: çamaşır makinesi gözlemi.
- Modül 6: bulaşık makinesi gözlemi.
- Modül 7: ana hat + PZEM gözlemi.

Bu üç modülün tamamı PREBERO kapsamındadır. Her modülün kendi imalat ve doğrulama kaydı ayrıca tutulur.

## Şu anki gerçek durum

- Masaüstü ESP32D2 + ADS1115 + SCT düzeneği mevcut ve daha önce akım okumak için kullanıldı.
- Kullanıcı, bias'sız denemede olumlu gözlem ve iki çamaşır makinesi tam program kaydı bildirdi. Bu bildirimler mevcut gözlemdir; teknik rapor ve tasarım kararı yerine geçmez.
- ADS1115 teknik raporu henüz hazırlanmadı.
- Güncel masaüstü bağlantısının tüm ayrıntıları bu görev kapsamında yeniden doğrulanmadı.
- Bias karşılaştırması ve osiloskop gözlemi henüz bu görev kapsamında tamamlanmadı.
- Modül 4 henüz sabit fiziksel modül olarak imal edilmiş ve kabul edilmiş değildir.
- PREBERO Modül 5/6/7 imalatı bu kapı tamamlanana kadar beklemededir.

## Kayıt düzeni

Her aşamada:
- HEDEF
- GERÇEK BAĞLANTI / KOŞUL
- LOG / FOTOĞRAF / OSİLOSKOP GÖRÜNTÜSÜ
- YORUM
- SONUÇ ve açık kalan sorular

Ham kayıtlar korunur; yorumlar ölçümden ayrılır. Başarılı kod, gerçek çıktı/log ve yorum birlikte depolanır.
