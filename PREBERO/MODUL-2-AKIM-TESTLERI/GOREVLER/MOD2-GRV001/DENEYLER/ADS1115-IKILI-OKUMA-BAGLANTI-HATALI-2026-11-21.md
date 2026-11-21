# MOD2-GRV001 – ADS1115 iki kanal okuma denemesi / bağlantı sorunu

**Tarih:** 2026-11-21  
**Fiziksel ADC:** ADS1115 No.10  
**Kontrol kartı:** ESP32D2  
**ESPHome:** 2026.11.0  
**I²C:** 0x48, SDA GPIO21, SCL GPIO22  
**Durum:** GEÇERSİZ DENEME – bağlantı sorunu nedeniyle baştan kurulacak

## 1. Amaç

A0-A1 ve A2-A3 diferansiyel girişlerinde yapılan iki kanallı okumayı gözlemlemek. Bu kayıt, kullanıcının bağlantı sorunu bildirmesi üzerine başarısız/ geçersiz denemenin izini korumak için oluşturulmuştur.

## 2. Logda doğrulanan yapı

- ESP32D2, 192.168.0.82 adresinden ESPHome API üzerinden bağlandı.
- I²C taramasında ADS1115 0x48 bulundu.
- Logda iki ADS1115 sensör tanımı vardı: A0-A1 ve A2-A3.
- Her iki kanal için ayrı `ct_clamp` bileşeni ve 200 ms örnekleme penceresi raporlandı.
- Logda örnekleme hızı alanı `7` olarak gösterildi; ESPHome logu bunu bu yapılandırmada ADS1115'in sample-rate enum değeri olarak yazdırıyor. Bu satır tek başına gerçek örnekleme performansını doğrulamaz.

## 3. Logdan seçilmiş çıktılar

```text
[21:18:43.075] Found device at address 0x48
[21:18:43.127] 'BERO Akim Sensoru' - Raw AC Value: 0.016A after 17 different samples (85 SPS)
[21:18:43.147] 'BERO Akim Sensoru A2-A3' - Raw AC Value: 0.033A after 17 different samples (85 SPS)
[21:18:43.250] 'BERO Akim Sensoru' >> 0.447 A
[21:18:43.250] 'BERO Akim Sensoru A2-A3' >> 0.897 A
[21:18:44.104] 'BERO Akim Sensoru' - Raw AC Value: 0.017A after 25 different samples (125 SPS)
[21:18:44.104] 'BERO Akim Sensoru A2-A3' - Raw AC Value: 0.018A after 25 different samples (125 SPS)
[21:18:44.215] 'BERO Akim Sensoru' >> 0.464 A
[21:18:44.215] 'BERO Akim Sensoru A2-A3' >> 0.494 A
[21:18:56.217] 'BERO Akim Sensoru' >> 0.456 A
[21:18:56.217] 'BERO Akim Sensoru A2-A3' >> 1.158 A
[21:18:57.216] 'BERO Akim Sensoru' >> 0.462 A
[21:18:57.216] 'BERO Akim Sensoru A2-A3' >> 1.357 A
```

## 4. Gözlem ve yorum

- İlk açılışta yayınlanan 0.447 A ve 0.897 A değerleri kararlı pencere değildir; başlangıç geçişi olarak değerlendirilmelidir.
- Sonraki A0-A1 değerleri yaklaşık 0.45–0.50 A çevresinde kalırken A2-A3 değeri 0.494 A civarından yükselerek 1.357 A'ya ulaşmıştır.
- Kullanıcı bağlantı sorunu bulunduğunu bildirmiş ve deneyi baştan başlatma kararı vermiştir.
- Bu nedenle bu log biaslı/biassız performans karşılaştırması olarak kullanılamaz.
- Bu kayıt, sorunun kesin olarak bias devresinden, SCT'den, ADS1115 kanal geçişinden veya yazılım mimarisinden kaynaklandığını kanıtlamaz.
- K=27.59 dahil hiçbir kalibrasyon katsayısı bu logdan türetilmeyecek veya güncellenmeyecektir.

## 5. Karar

1. Bu deneme geçersiz kabul edildi.
2. Bağlantı düzeni baştan kurulacak ve deney yeniden yürütülecek.
3. Mevcut çalışan tek kanallı V1.1 YAML korunacak.
4. Bu iki kanallı denemede kullanılan tam YAML kaynak dosyası bu log ekinde bulunmuyor. Bu nedenle kaynak kod, logdan tahmin edilerek oluşturulmadı. Gerçek YAML dosyası sağlandığında ayrı kod sürümü olarak arşivlenecek.
5. Bu kurulumdaki fiziksel ADC kimliği ADS1115 No.10'dur. Görev belgelerindeki önceki No.1 atıfları bu deneme için kullanılmayacaktır.

## 6. İlgili kaynaklar

- Korunan tek kanallı kod: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/V1.1/MOD2-GRV001_V1.1.yaml`
- Görev: `PREBERO/MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV001/GOREV.md`
- Modül tarihçesi: `PREBERO/MODUL-2-AKIM-TESTLERI/TARIHCE.md`
