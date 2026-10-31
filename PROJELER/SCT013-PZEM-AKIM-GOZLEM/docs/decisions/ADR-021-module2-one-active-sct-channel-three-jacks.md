# ADR-021 — Modül 2: tek aktif SCT kanalı, üç fiziksel giriş

- **Tarih:** 2026-10-31
- **Durum:** KULLANICI KARARI / TEST MİMARİSİ; güç kaynağı tekrarlı gözlemi bekliyor
- **İlgili görev:** T010
- **İlgili kayıt:** [LOAD-100W-004 uzun test analizi](../../logs/module2/2026-10-31-load-100w-004-sct1-desktop-power-extended-analysis.md)

## Bağlam ve gözlem

LOAD-100W-003 tek kanallı yazılım ve önceki besleme koşulunda 0,55 A üzerinde sıçramalar içeriyordu. LOAD-100W-004 ise ESP32D1 masaüstü harici besleme koşulunda yaklaşık 7 dakika boyunca 215 akım yayını verdi; medyan 0,423 A, ortalama 0,425 A, min–maks 0,401–0,480 A ve 0,55 A üzeri yayın yoktu.

Kullanıcı, 0,427 A UNIT değerine göre son kod çıktısını mevcut aşamada oldukça uyumlu buluyor. Bu kıyas geçici kullanıcı referansıdır; eşzamanlı PZEM doğrulaması değildir. LOAD-100W-004 logu 5 V girişini veya ESP32 3,3 V rayını doğrudan ölçmediğinden güç kaynağının etkisi henüz kesin neden olarak atanamaz.

## Karar

1. **Bir ESP düğümü aynı anda yalnız bir SCT akım kanalını okuyacak.**
2. Modül 2 üzerindeki üç fiziksel SCT jack girişi korunacak:
   - SCT-1 sarı sinyal → GPIO32 / ADC1_CH4
   - SCT-2 yeşil sinyal → GPIO33 / ADC1_CH5
   - SCT-3 mavi sinyal → GPIO34 / ADC1_CH6
   - Ortak bias izleme → GPIO35 / ADC1_CH7
3. Test sırasında SCT jack'i seçilen girişe takılacak; firmware yalnız o giriş için tek ct_clamp akım sensörü çalıştıracak. Bir, iki veya dört primer tur gibi farklı tur düzenleri ayrı test koşulları olabilir; her koşulda aynı anda tek CT/tek aktif okuma kanalı kullanılacak.
4. Üç jack'in bulunması üç kanalın eşzamanlı okunacağı anlamına gelmez. Amaç, test düzeneğini söküp yeniden kablolamadan farklı kanalları farklı zamanlarda seçebilmek ve aynı kutuyu tekrar tekrar kullanabilmektir.
5. Güç kaynağı tekrar gözlemlenecek. Harici masaüstü 5 V besleme mevcut iyi sonuçla ilişkili bir koşuldur; tek başına nedensellik kanıtı değildir. Mümkünse 5 V giriş ve 3,3 V rayı multimetreyle yük altında kontrol edilecek; aynı firmware, CT, yük ve tur koşulları korunarak yeterli süreli tekrar alınacak.
6. K katsayısı, mevcut loglar ve UNIT kıyası nedeniyle değiştirilmez. PZEM ile eşzamanlı kararlı pencere karşılaştırması ayrı doğrulama adımıdır.

## Gerekçe

Tek aktif kanal, yazılım/örnekleme yolunu sadeleştirir ve kanallar arası eşzamanlılık/iş yükü belirsizliğini test mimarisinden çıkarır. Üç fiziksel girişin korunması ise jack değiştirerek kanal seçme esnekliği sağlar. Böylece fiziksel düzenek sabit kalırken ölçüm sırası yazılımla ve jack seçimiyle yönetilir.

## Kanıt sınırları

- LOAD-100W-004 kararlı logu **ölçülmüş gözlemdir**.
- 0,427 A UNIT beklentisi **kullanıcı bildirimidir**, PZEM sonucu değildir.
- Harici beslemenin iyileşmenin nedeni olduğu iddiası **hipotezdir**.
- Bir ESP/tek aktif kanal tercihi **kullanıcı mimari kararıdır**; üç kanalın aynı ESP'de teknik olarak çalışamayacağı kanıtlanmış değildir.
- Yeni güç ölçümü, 150 W testi ve seçilen diğer jack kanallarının fiziksel testi henüz yapılmamıştır.

## Sonraki doğrulama

Aynı tek-kanal firmware yaklaşımıyla SCT-1 / 100 W koşusunu harici beslemede tekrarla; 5 V ve 3,3 V raylarını kaydet. Ardından jack değiştirilerek SCT-2 ve SCT-3 ayrı oturumlarda sınanır. Her oturumda CT modeli, primer tur sayısı, yük, besleme, firmware ve log aralığı kaydedilir.
