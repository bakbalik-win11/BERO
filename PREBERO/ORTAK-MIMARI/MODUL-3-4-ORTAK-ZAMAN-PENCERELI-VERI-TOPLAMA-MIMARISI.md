# Modül 3 ve 4 – Ortak zaman pencereli çoklu sensör veri toplama mimarisi

- **Karar tarihi:** 2026-11-22
- **Durum:** TASLAK MİMARİ KARAR / İMALAT ÖNCESİ TASARIM
- **Kapsam:** PREBERO Modül 3 (çamaşır makinesi) ve Modül 4 (bulaşık makinesi)

## 1. Amaç

Akım, ses ve titreşim gibi farklı fiziksel büyüklükleri, sensörlerin kendi uygun örnekleme hızlarını koruyarak ortak bir zaman ekseninde karşılaştırılabilir hale getirmek. Modül 3 ve Modül 4'te mümkün olduğunca aynı veri şeması ve zamanlama yaklaşımı kullanılacaktır.

**Önemli sıra kararı:** Mimari fikirler, sensör seçimi, örnekleme gereksinimleri, bağlantılar, işlem yükü ve veri şeması yeterince netleşmeden donanım imalatına geçilmeyecektir. Bu belge tek başına imalat izni değildir.

## 2. Önerilen mimari

Her sensör kendi fiziksel ölçüm ihtiyacına uygun hızda örnekleme yapar. Sensörlerin ham örnekleme hızlarının aynı olması zorunlu değildir. Her sensör, ortak 1 saniyelik zaman penceresine ait özellikleri/özetleri üretir. Pencere kimliği ve zaman damgası ortak zaman tabanından alınır.

- **Akım – SCT013:** Modül 2'den devralınan SCT013 + ADS1115 + ESP32D2 ve V1.6 ölçüm yolu başlangıç referansıdır. Mevcut ct_clamp yaklaşımındaki 200 ms RMS penceresi korunacak; ilgili 1 saniyelik slota ait akım özeti üretilecektir. V1.6 kalibrasyonu bu mimari not nedeniyle değişmez.
- **Ses – MAX4466 (öneri):** Analog ses örneklemesi kendi uygun örnekleme hızıyla yapılır. DC orta nokta/bias bileşeni ayrıldıktan sonra pencere bazında ses RMS ve peak; uygun görülürse ZCR hesaplanabilir. MAX4466 kalibreli dB ölçer olarak kabul edilmeyecek; ilk hedef göreceli akustik özellikleri kaydetmektir.
- **Titreşim – MPU6050 (öneri):** Sensör kendi ODR/örnekleme hızında üç eksenli ivme verisi sağlar. Yerçekimi/statik bileşeni uygun filtreyle ayırma yaklaşımı tasarımda belirlenecek. Pencere bazında eksen RMS/peak özellikleri değerlendirilebilir. Sadece vektör büyüklüğünden sabit 1 g çıkarmanın her durumda yeterli olduğu varsayılmayacaktır.

## 3. Zaman senkronizasyonu

- Tek bir ortak monoton zaman tabanı ve 1 saniyelik slot kimliği (ör. `tick_id` / `epoch_s`) kullanılacaktır.
- Sensörlerin örnekleme döngüleri birbirini bloke etmeyecek; her biri kendi hızında çalışacaktır.
- Slot sınırında, her sensörün aynı zaman aralığına ait özeti birleştirilerek tek kayıt oluşturulacaktır.
- Zaman damgası üretimi, slot sınırları, sensör gecikmeleri, eksik pencere davranışı ve yeniden başlatma sonrası zaman eşlemesi tasarım aşamasında tanımlanacaktır.
- Ortak slot kullanımı tek başına donanım seviyesinde eşzamanlı örnekleme veya sıfır zaman kayması garantisi vermez. Gerekirse gecikme ve hizalama ölçülüp raporlanacaktır.

## 4. Önerilen veri şeması

İlk taslak alanlar:

`timestamp, tick_id, current_rms_a, sound_rms, sound_peak, sound_zcr, vib_x_rms, vib_y_rms, vib_z_rms`

Gerekirse tepe ivme, sensör durum bayrakları, pencere örnek sayıları, veri geçerlilik bayrakları ve cihaz/modül kimliği eklenir. Alan adları ve birimler imalat/yazılım tasarımında kesinleştirilecektir.

## 5. İmalat öncesi netleştirilecekler

1. ESP32 kart modeli, ADC/I²C kaynakları ve pin planı.
2. SCT013/ADS1115 ölçüm yolunun diğer sensörlerle kaynak paylaşımı.
3. MAX4466 analog çıkışının hangi ADC ile, hangi örnekleme hızı ve çözünürlükte okunacağı.
4. MPU6050 ODR, arayüz, filtre ve üç eksenli veri işleme yaklaşımı.
5. 1 saniyelik slotun kesin sınırları ve sensör pencerelerinin slotla ilişkisi.
6. Birleşik kayıt biçimi, Home Assistant aktarımı, yerel tamponlama ve veri kaybı davranışı.
7. ESP32 CPU/RAM/ADC/I²C yükü ve uzun süreli çalışma kararlılığı.
8. Besleme, topraklama, analog gürültü, kablo ve sensör montaj konumları.
9. Modül 3 ve 4'te ortak tutulacak alanlar ile cihaza özgü alanlar.

## 6. İmalata geçiş kapısı

İmalat başlamadan önce yukarıdaki kararlar bir bağlantı/pin planı, sensör listesi, veri şeması, örnekleme/zamanlama planı ve yazılım iş akışı halinde gözden geçirilip onaylanmalıdır. Açık teknik sorular varken imalat başlatılmaz.

## 7. Kapsam dışı / henüz karar verilmemiş

- Otomatik program/aşama sınıflandırma algoritması bu mimari notla tanımlanmış değildir.
- Ses için desibel kalibrasyonu taahhüt edilmemiştir.
- PF ölçümü bu mimarinin zorunlu parçası değildir.
- ZMPT101B eklenmesi yalnızca kullanıcı tarafından dile getirilmiş ileriye dönük bir fikir/araştırma seçeneğidir; sensör listesine veya imalat kapsamına alınmamıştır.
- Örnekleme hızları ve özellik hesaplama parametreleri henüz kesinleştirilmemiştir.
