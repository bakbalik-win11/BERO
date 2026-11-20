# MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları

## Amaç

SCT013 30A/1V akım sensöründen gelen sinyali ADS1115 ara entegresi üzerinden okuyarak ESP32-D tabanlı masaüstü düzende akım davranışını incelemek ve ölçüm katsayılarını deneysel gözlemlerle belirlemek.

## Çalışma donanımı

- Ana kontrol kartı: ESP32-D geliştirme kartı.
- Taşıyıcı/bağlantı kartı: ESP32 shield.
- Akım sensörü: SCT013 30A/1V.
- Ara entegre / harici ADC: ADS1115.
- Sinyal zinciri: SCT013 30A/1V → ADS1115 → ESP32-D.
- Kullanıcının paylaştığı fiziksel fotoğrafta ESP32-D kartının shield üzerine takılı olduğu ve ADS1115 modülünün kablolarla düzeneğe bağlandığı görülmektedir.
- SCT013 30A/1V sensör fotoğrafta görünmemektedir; model kullanıcı tarafından bildirilmiştir.
- Fotoğraf fiziksel yerleşimi gösterir; kabloların pin eşleşmelerini, elektriksel değerleri veya sistemin çalıştığını kanıtlamaz.

## Çalışma kapsamı

1. ESP32-D ve shield masaüstü düzeneğini imal etmek.
2. ADS1115 modülü ile ESP32-D arasındaki mevcut kabloların pin eşleşmelerini doğrulamak.
3. ADS1115 ile ESP32-D arasındaki I²C haberleşmesini doğrulamak.
4. SCT013 30A/1V sensör çıkışını ADS1115 analog girişine uygun şekilde bağlamak.
5. Bias, besleme ve ortak referans düzenini gerçek bağlantı üzerinden doğrulamak.
6. Üretilen/ölçülen sinyali osiloskopta gözlemlemek.
7. Test koşullarını ve ölçüm sonuçlarını kaydetmek.
8. Katsayıları ancak test sonuçları yeterli olduğunda belirlemek.
9. Her testin logunu ve yorumunu bu görev altında saklamak.

## Kullanıcı tarafından verilen pin yapısı ve ölçüm ayarları

Bu bölüm, kullanıcının sağladığı mevcut yapılandırma bilgisini kaydeder. Buradaki ayarlar deney sürümüne ait tanımdır; fiziksel bağlantı ve tüm elektriksel sınırlar ayrıca doğrulanmalıdır.

### Bağlantılar

| Kaynak | Hedef | İşlev |
|---|---|---|
| ESP32D2 GPIO21 | ADS1115 SDA | I²C veri |
| ESP32D2 GPIO22 | ADS1115 SCL | I²C saat |
| ESP32D2 3.3V | ADS1115 VDD | Besleme |
| ESP32D2 GND | ADS1115 GND | Ortak referans |
| ADS1115 ADDR | GND | I²C adresi 0x48 |
| SCT013 iki çıkış ucu | ADS1115 A0 ve A1 | Diferansiyel akım sinyali |

### Ölçüm ve yazılım ayarları

| Parametre | Değer |
|---|---|
| ADS1115 ölçüm modu | Diferansiyel A0-A1 |
| PGA gain | 2.048 V |
| Örnekleme hızı | 860 SPS |
| Çalışma modu | Continuous |
| ct_clamp RMS penceresi | 200 ms |
| Sensör güncelleme aralığı | 1 saniye |
| Kalibrasyon katsayısı | 27.60 |
| Alt akım eşiği | 0.005 A (5 mA) |
| Alt eşik davranışı | 5 mA altındaki ölçüm sıfırlanır |

### Ölçüm amacı ve eşik gerekçesi

ADS1115 üzerinden SCT013 akım trafosunun diferansiyel çıkışı okunur; ct_clamp ile 200 ms RMS akım hesabı yapılır. Bu sürümde 5 mA altındaki ölçümler sıfırlanır. Amaç, yüksüz durumda gözlenen yaklaşık 1–2 mA taban değerlerinin Home Assistant'a gereksiz veri üretmesini önlemektir.

### ADS1115 birim kimliği ve kalibrasyon kuralı

- Kullanımdaki ADS1115 modülleri fiziksel olarak **1–10** şeklinde numaralandırılmıştır.
- Her ADS1115 kendi birim numarasıyla izlenir ve **her modül için ayrı kalibrasyon yapılır**.
- Bir ADS1115 için bulunan kalibrasyon katsayısı diğer ADS1115 modüllerine aktarılmaz; bütün ADS1115'ler için ortak katsayı kabul edilmez.
- Bu görevde yapılacak testlerde kullanılacak ADS1115: **No. 1**.
- Test kayıtlarında ADS1115 birim numarası açıkça yazılır; katsayı yalnızca o numaralı modülün kalibrasyon kaydına bağlanır.

### Önceki kalibrasyon gözlemi

- Önceki katsayı: 30.00
- ADS1115 gözlemi: yaklaşık 0.513 A
- PZEM gözlemi: yaklaşık 0.472 A
- Hesaplanan katsayı: 30.00 × (0.472 / 0.513) = 27.60

27.60 değeri önceki tek karşılaştırmadan elde edilmiş gözlem katsayısıdır; tüm ADS1115 modülleri için geçerli değildir. Bu değerin ADS1115 No. 1'e ait olduğu ayrıca doğrulanmadıkça No. 1'in kalibrasyon katsayısı olarak atanmaz. Her birim farklı akım seviyelerinde ayrıca kalibre edilip doğrulanmalıdır. PZEM karşılaştırma referansıdır, kusursuz ground truth olarak kabul edilmez.

### Elektriksel sınır notu

ADS1115 girişleri GND − 0.3 V ile VDD + 0.3 V sınırları içinde kalmalıdır. PGA kazanç ayarı bu giriş sınırlarını değiştirmez. Diferansiyel okuma seçilmiş olması, her bir giriş pininin mutlak gerilim sınırlarını ortadan kaldırmaz.

### Doğrulama durumu

Bu bölüm kullanıcının verdiği bağlantı ve ayar tanımını kaydeder. Gerçek kablo uçları, A0/A1 üzerindeki mutlak gerilimlerin sınırlar içinde kalması ve sistemin bu ayarlarla çalıştığına ilişkin log henüz bu kayıtla tek başına kanıtlanmış sayılmaz.

## Çıktılar

- Her kod sürümünün YAML dosyası, logları ve raporları aynı görev klasörünün altındaki kendi sürüm klasöründe tutulur.
- Test verileri görev klasöründeki ortak `VERI/` alanında saklanır.
- Bir sürümün test kanıtları başka bir sürümün kayıtlarıyla karıştırılmaz.

## Tamamlanma ölçütü

Sinyal davranışı yeterince anlaşılmış, katsayılar ölçüm sonuçlarıyla gerekçelendirilmiş ve test çıktıları bu görev içinde kayıt altına alınmış olmalıdır.

Bu görev henüz tamamlanmış değildir.

## Kullanılan fiziksel ESP

- **Kart ailesi / çalışma tanımı:** ESP32-D.
- **Shield:** ESP32 shield.
- **Akım sensörü:** SCT013 30A/1V.
- **Ara entegre / harici ADC:** ADS1115.
- **Fiziksel kurulum kanıtı:** 2026-11-21 tarihli kullanıcı fotoğrafında ESP32-D + shield yerleşimi ve ADS1115 modülünün kabloları görülmektedir.
- **Fiziksel ESP envanter kimliği:** İlgili fiziksel kart envantere eşleştirildiğinde yazılacak.
- **ESPHome / Home Assistant cihaz adı:** Gerçek cihaz ve sabit ad doğrulandığında yazılacak.
- **Not:** Fotoğraf pinout veya çalışan sistem kanıtı değildir. Kimlik, pin ve elektriksel değer tahmin edilmeyecektir.

## Bu görevin sürümlü çıktı düzeni

YAML, LOG ve RAPOR her kod sürümü için tekrarlanan sürüm klasörlerinde birlikte tutulur:

```text
MOD2-GRV001/
├── GOREV.md
├── VERI/
├── V1.0/
│   ├── MOD2-GRV001_V1.0.yaml
│   ├── LOG/
│   │   └── [bu sürümün gerçek çalışma logları]
│   └── RAPOR/
│       └── [bu sürümün test sonucu ve teknik yorumu]
└── V1.1/
    ├── MOD2-GRV001_V1.1.yaml
    ├── LOG/
    └── RAPOR/
```

- Her yeni kod sürümü için görev klasörünün altında yeni bir sürüm klasörü açılır.
- YAML dosyası doğrudan sürüm klasöründe bulunur; LOG ve RAPOR alt klasörleri aynı sürüm klasörünün içindedir.
- `VERI/` görev genelindeki test verileri için ortak alandır.
- Önceki sürümün kodu, logları ve raporları değiştirilmeden korunur.
- Yeni sürümün test kayıtları yalnızca kendi sürüm klasörüne yazılır.
