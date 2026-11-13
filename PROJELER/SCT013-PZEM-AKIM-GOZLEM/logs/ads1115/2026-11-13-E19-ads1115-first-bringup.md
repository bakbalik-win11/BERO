# E19 — ADS1115 ilk donanım okuma kayıtları

Tarih: 2026-11-13. Kaynak: Kullanıcının bu oturumda paylaştığı ESP32D2 ADS1115 ve ESP32D1 Modül 2 logları.
Kanıt türü: ÖLÇÜLDÜ / LOG İLE DESTEKLENDİ. Tam ham log dosyası bu kayda eklenmedi; aşağıdaki değerler paylaşılan loglardan özetlendi.

## 1. I2C ve yüksüz diferansiyel okuma — ESP32D2
- I2C taraması ADS1115'i 0x48 adresinde buldu.
- Bağlantı bildirimi: GPIO21=SDA, GPIO22=SCL, 3.3 V besleme, ADDR=GND; SCT uçları A0 ve A1.
- Önceki test ayarı: A0_A1, gain 0.256 V, 7 SPS; sensör güncellemesi yaklaşık 1 s.
- Akım olmayan koşulda diferansiyel okumalar: 23, 23, 31, 39, 31, 16, 8, 8, 16, 8 µV.
- Yorum: I2C haberleşmesi ve diferansiyel sayısal okuma çalıştı. Bu, RMS akım ölçümünün doğrulandığı anlamına gelmez.

## 2. Yük bağlıyken diferansiyel gözlem — ESP32D2 + PZEM
- Kullanıcı yaklaşık 57 W nominal akkor yükü devreye aldı.
- PZEM Modül 3: 17:23:38'de 228.1 V, 0.264 A, 60.20 W; 17:23:42'de 227.8 V, 0.264 A, 60.00 W; 50 Hz, PF=1.00.
- Önceki düşük hızlı ADS logunda A0-A1 değerleri yaklaşık -12.8 mV ile +13.1 mV arasında değişti.
- Logda örnekler yaklaşık saniyede bir yayımlandı; ADS ayarı 7 SPS idi.
- Yorum: 50 Hz sinyalin seyrek örneklenmesi aliasing benzeri yavaş işaret değişimi oluşturabilir. Bu kayıt dalga şeklini, RMS akımı veya katsayıyı ölçmüş değildir; yalnız giriş sayısının yükle değiştiğini gösterir.

## 3. Mevcut ESP32D1 zinciri — karşılaştırma tabanı
- Ham ct_clamp: yaklaşık 0.13757–0.13954 A.
- K uygulanmış sensör: yaklaşık 3.332–3.380 A.
- Her pencerede 1,340–1,384 farklı örnek; loglanan hız 6,700–6,920 SPS.
- Bu log kesitinde eşzamanlı PZEM ölçümü yoktur.
- Yorum: Mevcut zincir ham ct_clamp değerine yaklaşık 24.22 katsayısını uyguluyor. Aynı zamanlı PZEM olmadan 3.35 A gerçek akım kabul edilemez.

## 4. Sınırlar
- I2C ve diferansiyel sayısal okuma gözlendi; RMS akım ve kalibrasyon doğrulanmadı.
- Önceki düşük hızlı ölçüm 7 SPS/1 s güncelleme ile yapıldı. Yeni 860 SPS + ct_clamp YAML henüz derlenip fiziksel olarak test edilmedi.
- AIN pinlerinin mutlak gerilim/common-mode güvenliği diferansiyel çıktılardan kanıtlanamaz.
- 100 W katsayı deneyi henüz yapılmadı; katsayı veya ±%4 başarı sonucu yok.