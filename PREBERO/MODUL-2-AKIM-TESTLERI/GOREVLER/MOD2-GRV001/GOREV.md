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

- Kullanılan kodlar: KOD/
- Test verileri: VERI/
- Ham çalışma logları: LOG/
- Analiz ve sonuç raporları: RAPOR/

## Tamamlanma ölçütü

Sinyal davranışı yeterince anlaşılmış, katsayılar ölçüm sonuçlarıyla gerekçelendirilmiş ve test çıktıları bu görev içinde kayıt altına alınmış olmalıdır.

Bu görev henüz tamamlanmış değildir.

## Kullanılan fiziksel ESP

- **Fiziksel ESP envanter kimliği:** Henüz bu görev için atanmadı.
- **ESPHome / Home Assistant cihaz adı:** Fiziksel cihaz seçilip envanter kaydıyla eşleştirildiğinde buraya yazılacak.
- **Kimlik kuralı:** ESP kimliği cihaza aittir ve görev/kod sürümünden bağımsızdır. Aynı ESP başka görevde kullanılırsa fiziksel kimliği ve sabit cihaz adı değişmez.
- **Atama notu:** Gerçek cihaz seçilmeden ESP kimliği veya cihaz adı tahmin edilerek yazılmayacak.

## Bu görevin sürümlü çıktı düzeni

Her kod sürümünün kodu, logları ve raporları birbirine açıkça bağlanır. Örnek düzen:

```text
KOD/
└── MOD2-GRV001_V1.0.yaml

LOG/
└── MOD2-GRV001_V1.0/
    └── [bu sürümün gerçek çalışma logları]

RAPOR/
└── MOD2-GRV001_V1.0/
    └── [bu sürümün test sonucu ve teknik yorumu]
```

Yeni bir yama `V1.1` gibi yeni bir kod sürümü oluşturur. Önceki sürümün kodu, logları ve raporları değiştirilmeden korunur. Yeni sürümün test kayıtları kendi sürüm klasörüne yazılır.
