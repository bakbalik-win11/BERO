# MOD2-GRV001 – Kod 0 İlk Ölçüm ve Katsayı Değerlendirme Raporu

**Tarih:** 2026-11-21  
**Modül:** Modül 2 – Masaüstü akım test düzeneği  
**Görev:** MOD2-GRV001  
**Kod:** Kod 0  
**Kullanılan ADC:** ADS1115 fiziksel modül No.10  
**Durum:** İlk ölçüm ve katsayı değerlendirmesi tamamlandı; V1.0 katsayı denemesine geçildi.

## 1. Deneyin amacı

Kod 0 ile SCT013 30A/1V sensöründen gelen akım sinyali ADS1115 No.10 üzerinden okundu. İlk ölçümde kodda bulunan **27.60** kalibrasyon katsayısı kullanıldı.

Amaç, 100 W ve 150 W yüklerde Kod 0'ın verdiği SCT akım sonuçlarını aynı zaman aralıklarındaki PZEM akım sonuçlarıyla karşılaştırmak ve katsayının yeterliliğini değerlendirmekti.

PZEM bu çalışmada karşılaştırma/etiketleme referansıdır; kusursuz gerçek değer (ground truth) olarak kabul edilmez.

## 2. Kod 0 ölçüm düzeni

- SCT013 30A/1V → ADS1115 No.10 A0-A1 diferansiyel giriş
- ADS1115 I²C adresi: 0x48
- ESP32-D GPIO21: SDA
- ESP32-D GPIO22: SCL
- ADS1115 PGA: 2.048 V
- ADS1115 örnekleme hızı: 860 SPS
- Çalışma modu: Continuous
- ct_clamp RMS penceresi: 200 ms
- Home Assistant güncelleme aralığı: 1 saniye
- Kod 0 kalibrasyon katsayısı: **27.60**

## 3. history.csv kararlı pencere sonuçları

Kaynak: Kullanıcının deney sırasında sağladığı `history.csv` verisi. Yük geçişleri, sıfır durumları ve geçiş sıçramaları kararlı ortalamalara dahil edilmedi.

| Yük | Kararlı zaman aralığı | PZEM akım ortalaması | SCT akım ortalaması (Kod 0) | Hesaplanan katsayı |
|---|---|---:|---:|---:|
| 150 W | 15:57:00–15:57:38 | 0.65050 A | 0.58537 A | 30.67 |
| 150 W | 15:58:33–15:59:58 | 0.65043 A | 0.58507 A | 30.68 |
| 100 W | 16:00:53–16:02:35 | 0.47450 A | 0.42759 A | 30.63 |

Katsayı hesabı:

`K_yeni = K_mevcut × (I_PZEM / I_SCT)`

`K_yeni = 27.60 × (I_PZEM / I_SCT)`

Üç kararlı pencerenin hesaplanan katsayılarının aritmetik ortalaması yaklaşık **30.6607** olup iki ondalık basamakla **30.66** olarak alınmıştır.

## 4. Kod 0 değerlendirmesi

Kod 0, akım okuma zincirini çalıştırmış ve 100 W ile 150 W yüklerde kararlı ölçüm verisi üretmiştir. Bununla birlikte 27.60 katsayısı kullanıldığında SCT sonuçları, karşılaştırılan kararlı pencerelerde PZEM sonuçlarından düşük kalmıştır.

Üç pencereden hesaplanan katsayıların 30.63–30.68 aralığında birbirine yakın çıkması, ADS1115 No.10 için 27.60 yerine daha yüksek bir katsayının denenmesini gerektirmiştir.

Bu sonuç, Kod 0'ın akım okuma işlevinin başarısız olduğu anlamına gelmez. Tespit edilen konu, bu ADS1115 No.10 ve kullanılan ölçüm zinciri için mevcut 27.60 katsayısının karşılaştırma sonuçlarıyla uyuşmamasıdır.

## 5. V1.0'a geçiş kararı

Kod 0'ın YAML dosyası ve bu ilk deneyin sonuçları temel kayıt olarak korunacaktır. Kod 0 geriye dönük olarak değiştirilmeyecek; 30.66 katsayısı Kod 0'a yazılmayacaktır.

Bu ölçüm değerlendirmesinin ardından ayrı bir deneme sürümü olan **V1.0** hazırlanmıştır:

- ADS1115 fiziksel modül: No.10
- V1.0 katsayısı: **30.66**
- Diğer ölçüm ayarları Kod 0 ile aynı tutulmuştur.
- V1.0'ın amacı, bulunan 30.66 katsayısının yeni ölçümlerde sonuçları iyileştirip iyileştirmediğini sınamaktır.

## 6. Şu anki çalışma aşaması

Çalışma şu anda V1.0 katsayı doğrulama aşamasındadır.

V1.0 cihaza yüklendikten sonra 100 W ve 150 W yüklerde yeniden kararlı ölçüm pencereleri alınacaktır. Yeni PZEM ve SCT sonuçları ayrı log/rapor olarak V1.0 klasöründe saklanacak ve Kod 0'ın ilk ölçümleriyle karşılaştırılacaktır.

**30.66 katsayısı henüz doğrulanmış veya nihai katsayı değildir.** Başarı kararı, V1.0 ile alınacak yeni ölçüm sonuçlarından sonra verilecektir.

## 7. Kayıt ve sürüm koruma

- Kod 0 YAML: `KOD/MOD2-GRV001_KOD-0.yaml`
- Kod 0 ilk ölçüm raporu: `KOD/MOD2-GRV001_KOD-0_RAPOR.md`
- V1.0 YAML: `V1.0/MOD2-GRV001_V1.0.yaml`
- V1.0 yeni ölçüm logları ve değerlendirmesi: `V1.0/LOG/` ve `V1.0/RAPOR/`

Kod 0'ın ilk ölçüm kayıtları ile V1.0 doğrulama kayıtları birbirine karıştırılmayacaktır.
