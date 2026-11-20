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
