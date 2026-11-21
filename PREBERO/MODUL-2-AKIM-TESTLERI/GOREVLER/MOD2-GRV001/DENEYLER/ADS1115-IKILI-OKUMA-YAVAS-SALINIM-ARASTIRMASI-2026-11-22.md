# ADS1115 İkili Okuma – Yavaş Salınım Araştırması
**Tarih:** 2026-11-22  
**Görev:** MOD2-GRV001  
**Durum:** AÇILDI – TEST BEKLİYOR  
**Kod durumu:** Mevcut çalışan YAML değiştirilmeyecek

## 1. Amaç

Aynı ADS1115 üzerindeki iki diferansiyel SCT kanalında gözlenen, birbirleriyle aynı periyotta olmayan yavaş akım salınımlarının kaynağını araştırmak.

Araştırılacak temel soru: Salınım iki kanalın birlikte okunması, ADS1115 dönüşüm sırası veya ESPHome ölçüm zamanlaması nedeniyle mi oluşuyor; yoksa SCT ve analog giriş kollarının kendi davranışlarından mı kaynaklanıyor?

Bu deneyin amacı katsayı belirlemek, filtre ayarlamak veya ölçüm dalgalanmasını yazılımla gizlemek değildir.

## 2. Gözlemin dayanağı

Kullanıcının paylaştığı Home Assistant grafiği:
- Zaman aralığı: yaklaşık 00:18:00–00:22:15.
- Yük: Kettle 1 + 100 W ampul.
- PZEM akımı: yaklaşık 1.163 A seviyesinde düz/kararlı görünmektedir.
- A0–A1 (sarı): yaklaşık 0.98–1.21 A aralığında belirgin yavaş salınım.
- A2–A3 (kırmızı): yaklaşık 1.05–1.19 A aralığında, sarı kanalla aynı periyotta olmayan salınım.
- Görselden çıkarılan periyotlar yaklaşık 45–60 saniye mertebesindedir; kesin periyot ham CSV zaman serisinden hesaplanmalıdır.

Bu grafik nitel gözlemdir. Tek başına ADS1115, ESPHome veya gerçek yük kaynaklı bir neden kanıtlamaz. PZEM'in daha yavaş örneklemesi de göz önünde tutulacaktır.

## 3. Donanım ve mevcut yapı

- ESP: ESP32D2
- ADC: ADS1115, I²C adresi 0x48
- SDA: GPIO21
- SCL: GPIO22
- Besleme: 3.3 V
- Ortak GND: ESP32D2–ADS1115
- Kanal 1: A0–A1, SCT013
- Kanal 2: A2–A3, ikinci SCT013
- Ölçüm yaklaşımı: ADS1115 diferansiyel kanal okuması ve ESPHome ct_clamp
- Bilinen önceki ayarlar: ADS1115 continuous, 860 SPS, PGA 2.048 V; ct_clamp penceresi 200 ms, sensör güncellemesi 1 s. Test öncesi çalışan iki kanallı YAML'dan gerçek değerler teyit edilecektir.

**Önemli:** Depoda görülen KOD-0 YAML yalnızca A0–A1 tek kanalını tanımlar. Bu dosya iki kanallı salınımı açıklamak için yeterli değildir. Deneyden önce sahada çalışan iki kanallı YAML ayrıca alınmalı ve değiştirilmeden incelenmelidir.

## 4. Hipotezler

1. İki diferansiyel kanalın ADS1115 üzerinde ardışık dönüşümle okunması ve dönüşüm zamanlarının farklılığı.
2. İki ct_clamp örnekleme penceresinin başlangıç/bitiş zamanlarının veya güncelleme fazlarının farklı olması.
3. A0–A1 ve A2–A3 analog kollarında bias, SCT, bağlantı veya ortak-mod davranışı farkı.
4. ESP32/ADS1115 besleme veya referans hattında yavaş değişim.
5. Yükün gerçek akımında PZEM'in örnekleme/güncelleme hızı nedeniyle grafikte görünmeyen değişim.

Bunlar test edilecek hipotezlerdir; şu aşamada hiçbiri doğrulanmış neden değildir.

## 5. Deney protokolü

### A. Mevcut çift kanal düzeni – referans kaydı
- Çalışan iki kanallı YAML aynen korunacak; deney için kopyası alınacak.
- Kettle 1 + 100 W ampul yükü ve aynı SCT yerleşimi korunacak.
- PZEM, A0–A1 ve A2–A3 aynı oturumda kaydedilecek.
- En az 5 dakika kesintisiz veri alınacak.
- Açılış/kapanış geçişleri kararlı pencere analizine katılmayacak.
- Ham CSV saklanacak; grafik tek başına veri kaynağı sayılmayacak.

### B. Tek kanal karşılaştırması
Güvenli ve mevcut çalışan yapıdan ayrı bir test kopyası hazırlanması halinde:
1. Yalnız A0–A1 okunarak aynı yükte en az 3 dakika kayıt alınacak.
2. Yalnız A2–A3 okunarak aynı yükte en az 3 dakika kayıt alınacak.
3. Her aşamada PZEM kaydı devam edecek.
4. Tek kanal testleri arasında SCT konumu, yönü, yük ve kablolama değiştirilmemeye çalışılacak.

Bu aşama için YAML değişikliği ancak mevcut iki kanallı dosya incelendikten ve kullanıcı onayladıktan sonra yapılacaktır. Çalışan YAML üzerine yazılmayacaktır.

### C. Zaman serisi karşılaştırması
Her kanal için örnek sayısı, zaman damgaları ve örnek aralığı; ortalama, medyan, standart sapma, minimum ve maksimum; trend çıkarıldıktan sonra tepe-çukur genliği; tepe zamanları ve yaklaşık periyot; iki kanal arasındaki gecikme/faz ilişkisi; PZEM ile zaman eşleştirilmiş fark hesaplanacaktır.

İki ADS1115 kanalının ardışık dönüşümleri eşzamanlı örnek kabul edilmeyecektir. Zaman damgaları gerçek ölçüm anını göstermiyorsa bu sınırlama rapora yazılacaktır.

## 6. Kontrol edilecek YAML/firmware alanları
- ADS1115 continuous_mode
- Her kanalın multiplexer, gain, sample_rate tanımı
- Sensörlerin update_interval değerleri
- ct_clamp sample_duration değerleri
- filters zinciri ve filtre sırası
- Sensörlerin güncelleme/başlatılma sırası
- I²C frekansı ve hata/yeniden deneme logları

Örnekleme penceresi veya filtreler ilk referans kaydı alınmadan değiştirilmeyecektir.

## 7. Güvenlik ve değişiklik kontrolü
- ADS1115 A0, A1, A2 ve A3 pinlerinin her birinin GND'ye göre mutlak gerilimi ADS1115 besleme sınırları içinde kalmalıdır.
- Diferansiyel ölçüm seçimi pinlerin mutlak giriş sınırlarını değiştirmez.
- SCT yalnızca yalıtımı sağlam tek bir iletkeni kavramalıdır.
- Şebeke bağlantılı devrede ESP32 GND doğrudan şebekeye bağlanmayacaktır.
- Osiloskop kullanılacaksa prob toprak bağlantısının koruma toprağıyla ilişkisi önceden doğrulanmalıdır.
- Mevcut çalışan YAML ve K=27.59 korunacaktır. Bu deneyde kalibrasyon katsayısı veya filtre değişikliği yapılmayacaktır.

## 8. Başarı ölçütü

Deney, salınımın kaynağını kesin olarak bulmuş sayılmak için değil, olası kaynakları birbirinden ayıracak kanıt üretmek için açılmıştır.

Başarılı çıktı: çalışan iki kanallı YAML'ın incelenmiş kopyası; ham CSV ve test koşulları; her iki kanalın salınım periyodu/genliği/zaman ilişkisi; tek kanal ve çift kanal kayıtlarının karşılaştırması; bulguların kanıt sınırlarıyla birlikte teknik yorumu.

## 9. Mevcut karar
- Deney açıldı; fiziksel test henüz yapılmadı.
- YAML henüz değiştirilmedi.
- Filtre genişletme veya update_interval değiştirme kararı verilmedi.
- K=27.59 ve mevcut V1.1 çalışma kodu korunuyor.
- İlk sonraki adım: sahada çalışan iki kanallı YAML dosyasını incelemek.