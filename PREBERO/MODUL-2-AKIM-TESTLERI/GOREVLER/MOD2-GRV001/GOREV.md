# MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları

## Amaç

Masaüstü 4 kanal düzeninde elde edilen akım okumasının sinyal davranışını anlamak, testleri sürdürmek ve ölçüm katsayılarını deneysel gözlemlerle belirlemek.

## Çalışma kapsamı

1. Üretilen/ölçülen sinyali osiloskopta gözlemlemek.
2. Gerekli görülen koşullarda biaslı ve biassız sinyali karşılaştırmak.
3. Test koşullarını ve ölçüm sonuçlarını kaydetmek.
4. Katsayıları ancak test sonuçları yeterli olduğunda belirlemek.
5. Her testin logunu ve yorumunu bu görev altında saklamak.

## Çıktılar

- Her kod sürümünün YAML dosyası, logları ve raporları aynı görev klasörünün altındaki kendi sürüm klasöründe tutulur.
- Test verileri görev klasöründeki ortak `VERI/` alanında saklanır.
- Bir sürümün test kanıtları başka bir sürümün kayıtlarıyla karıştırılmaz.

## Tamamlanma ölçütü

Sinyal davranışı yeterince anlaşılmış, katsayılar ölçüm sonuçlarıyla gerekçelendirilmiş ve test çıktıları bu görev içinde kayıt altına alınmış olmalıdır.

Bu görev henüz tamamlanmış değildir.

## Kullanılan fiziksel ESP

- **Fiziksel ESP envanter kimliği:** Henüz bu görev için atanmadı.
- **ESPHome / Home Assistant cihaz adı:** Fiziksel cihaz seçilip envanter kaydıyla eşleştirildiğinde buraya yazılacak.
- **Kimlik kuralı:** ESP kimliği cihaza aittir ve görev/kod sürümünden bağımsızdır. Aynı ESP başka görevde kullanılırsa fiziksel kimliği ve sabit cihaz adı değişmez.
- **Atama notu:** Gerçek cihaz seçilmeden ESP kimliği veya cihaz adı tahmin edilerek yazılmayacak.

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
