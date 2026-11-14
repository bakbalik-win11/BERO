# BERO 12 Kanallı Ölçüm Modülü — RT-209 Mekanik Adayı

## DURUM
**FİKİR / TASLAK — İMALAT KARARI DEĞİL.** Bu belge, 2026-11-15 tarihli kullanıcı görüşmesinde ortaya çıkan mekanik ve elektriksel yerleşim fikirlerini toplar. Kutu satın alınmadı; ölçülü yerleşim, devre şeması, kablo planı, firmware, üretim ve test yapılmadı.

## AMAÇ
BERO için iki aynı ölçüm düğümünü tek, servis edilebilir bir ana modül muhafazasında toplamak. Hedef sistem 12 SCT akım girişidir.

## ANA KUTU ADAYI
- Üretici/model: Altınkaya RT-209 DIN ray muhafazası.
- Kullanıcı kararı: RT-209, BERO ana modül kutusu olmaya aday olarak seçildi; henüz kesin satın alma/imalat kararı değildir.
- Kaynak çizim: kullanıcı tarafından sağlanan `RT-209-drawing.PDF`.
- Çizimdeki alt taşıyıcı PCB alanı yaklaşık 150 × 85,5 mm; üst panel ayrı parçadır. Gerçek montaj payı ve kullanılabilir iç hacim, üretici ölçüleri ve fiziksel numune üzerinden doğrulanmalıdır.
- Yeşil klemensli hazır taşıyıcı yapı kullanılmayacak; iç elektronik taşıyıcı kullanıcı tarafından delikli board/pertinaks ile hazırlanacak.

## HEDEF DONANIM — FİKİR
- 2 adet ESP32-WROOM-32D geliştirme kartı.
- Kullanıcıda bulunan 2 adet ESP32 vidalı klemensli terminal shield/adapter kartı; ESP32'ler soketli ve sökülebilir olacak.
- Toplam 6 adet ADS1115; her ESP32 başına 3 ADC ve 6 SCT girişi hedefi.
- Toplam 12 SCT girişi.
- 2 adet RS485 dönüştürücü; düğümler arası/merkez haberleşme topolojisi daha sonra tasarlanacak.
- Kullanıcıda yeterli sayıda bulunduğu bildirilen dişi SCT jack'ları; dış bağlantı paneline yerleştirme fikri.
- RESET-A ve RESET-B: her ESP32'nin EN/reset hattını ayrı ayrı donanımsal olarak resetleyecek iki dış erişimli buton. Ortak reset butonu düşünülmüyor.
- Besleme, koruma, topraklama/ortak referans ve servis bağlantıları henüz tasarlanmadı.

## MEKANİK YERLEŞİM FİKRİ
1. RT-209 üst/ön panelinde 12 SCT dişi jack ve kanal etiketleri.
2. İki ayrı dış erişimli reset butonu: RESET-A ve RESET-B.
3. İç tabanda iki ESP32 terminal shield'ı; ESP32 kartları soketli, sökülebilir.
4. Altı ADS1115 küçük modülünün delikli board üzerinde sabitlenmesi veya soketli bağlanması.
5. RS485, besleme ve diğer dağıtım bağlantılarının servis edilebilir şekilde yerleştirilmesi.
6. Jack'lar panelde; jack'lardan ADC ön uçlarına giden kablolar içeride sabit ve etiketli olacak.
7. İç taşıyıcı ile dış jack paneli işlevsel olarak ayrılacak; jack arızasında tüm elektronik taşıyıcının sökülmesi gerekmemesi hedefleniyor.

## HABERLEŞME VE KANAL MİMARİSİ — DOĞRULANMAMIŞ HEDEF
- Her ADS1115 için ayrı SDA/SCL çifti kullanılması tercih ediliyor.
- İlk inceleme basamağı: bir ESP32 üzerinde iki ADS1115'in iki ayrı donanımsal I²C hattıyla yönetilmesini test etmek.
- Üçüncü ADS1115 hattı için yazılımsal I²C veya başka çözümün ESPHome/framework ve gerçek kart üzerinde uygulanabilirliği henüz doğrulanmadı.
- Klasik ESP32'de iki donanımsal I²C kontrolcüsü olduğu için üç ayrı donanımsal I²C kontrolcüsü varmış gibi tasarım yapılmayacak.
- 12 SCT hedefi: 2 ESP32 × (3 ADS1115 + 6 SCT). Bu bir tasarım hedefidir; kanal tarama hızı, bus yöntemi ve uzun süreli kararlılık henüz kanıtlanmadı.

## SCT JACK VE ANALOG GİRİŞ GÜVENLİĞİ
- Jack tipi, pin dizilimi ve panel delik çapı mevcut SCT fişleri fiziksel olarak ölçüldükten sonra seçilecek.
- Her girişin iki iletkeni ve analog ön uç bağlantısı kanal bazında çizilecek.
- CT sekonderi, primer akım varken açık devre kalmamalı; jack çıkarıldığında sekonderin açık kalma riski için uygun kısa-devreli/önce-bağlanır çözüm veya giriş devresi değerlendirilmelidir.
- Burden, bias/common-mode, giriş koruması ve ADS1115 mutlak giriş sınırları doğrulanmadan enerjili SCT bağlantısı yapılmayacak.
- Jack metal gövdesi/şase bağlantısı ve kanal ortak uçları varsayılmayacak; devre şemasında tanımlanacak.

## İMALAT ÖNCESİ AÇIK İŞLER
- RT-209 gerçek iç ölçülerini, panel geometrisini, delik/slot konumlarını ve taşıyıcı taban ölçülerini çizimden doğrula.
- İki terminal shield, altı ADS1115, iki RS485 modülü, jack gövdeleri ve kablo bükülme yarıçaplarıyla ölçekli yerleşim çiz.
- 12 jack'ın hangi yüzeye kaç sıra yerleşeceğini belirle; paneldeki mevcut delik/slotlarla çakışmayı kontrol et.
- RESET-A/B butonlarının panel konumu ve EN bağlantı şemasını belirle.
- Delikli board ölçüsü, sabitleme, ara mesafe, izolasyon ve servis erişimini belirle.
- Her kanal için jack → koruma/burden/bias → ADS1115 giriş bağlantı şemasını çiz.
- ESP32 başına 3 ADS1115 bağlantı yöntemini gerçek donanımda doğrula; ilk iki ayrı I²C hattı testi ve üçüncü hat kararı E24 ile ilişkilendir.
- Besleme gerilimi/akım bütçesi, regülasyon, sigorta/koruma, RS485 topolojisi ve kablo girişlerini belirle.
- Kutuya delik açmadan önce 1:1 panel şablonu ve fiziksel prova hazırla.

## KANIT VE DURUM SINIRI
- **KULLANICI BİLDİRİMİ:** İki ESP32-WROOM-32D kart ve iki vidalı terminal shield mevcut; yeterli sayıda dişi jack bulunduğu bildirildi.
- **KULLANICI SAĞLADIĞI ÇİZİM:** RT-209 teknik PDF'si; alt taşıyıcı PCB alanı çizimde yaklaşık 150 × 85,5 mm gösteriliyor.
- **FİKİR:** Tek RT-209 kutuda 2 ESP32 + 6 ADS1115 + 12 SCT + 2 RS485 yerleşimi.
- **HENÜZ YAPILMADI:** Kutu satın alma, ölçülü CAD yerleşimi, delikli board imalatı, jack paneli, kablolama, devre/firmware, derleme, donanım testi ve RS485 testi.
