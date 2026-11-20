# MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları

## Amaç

Masaüstü 4 kanal düzeninde elde edilen akım okumasının sinyal davranışını anlamak, testleri sürdürmek ve ölçüm katsayılarını deneysel gözlemlerle belirlemek.

## Çalışma donanımı

- Ana kontrol kartı: ESP32-D geliştirme kartı.
- Taşıyıcı/bağlantı kartı: ESP32 shield.
- ESP32-D kartı shield üzerine takılarak masaüstü deney düzeneği imal edilecektir.
- Paylaşılan ürün görseli temsili yerleşim görselidir. Görsel, kullanılacak ESP32-D kartının kesin varyantını, GPIO eşleşmelerini veya shield üzerindeki terminal bağlantılarını doğrulamaz.
- Fiziksel kartın tam modeli, shield modeli, pin bağlantıları, besleme ve çevre modülleri gerçek donanım üzerinden doğrulanınca imalat kaydına işlenecektir.

## Çalışma kapsamı

1. ESP32-D ve shield masaüstü düzeneğini imal etmek.
2. Gerçek kart ve shield üzerindeki pinleri doğrulayıp bağlantı şemasını hazırlamak.
3. Üretilen/ölçülen sinyali osiloskopta gözlemlemek.
4. Gerekli görülen koşullarda biaslı ve biassız sinyali karşılaştırmak.
5. Test koşullarını ve ölçüm sonuçlarını kaydetmek.
6. Katsayıları ancak test sonuçları yeterli olduğunda belirlemek.
7. Her testin logunu ve yorumunu bu görev altında saklamak.

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
- **Fiziksel ESP envanter kimliği:** İmal edilecek/kullanılacak fiziksel kart seçilip envantere eşleştirildiğinde yazılacak.
- **ESPHome / Home Assistant cihaz adı:** Gerçek cihaz ve sabit ad doğrulandığında yazılacak.
- **Not:** Paylaşılan görsel temsildir; kesin kart modeli veya pinout kanıtı değildir. Kimlik veya cihaz adı tahmin edilmeyecektir.

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
