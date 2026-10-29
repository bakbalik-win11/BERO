# Deney ve karar izleme defteri

> **Bu dosyanın amacı:** Deney kodunu, deneyin neden yapıldığını, alınan kararları ve kanıtlanan sonucu birbirinden koparmamak. Bu dosya bir navigasyon/özet defteridir; ayrıntılı protokol, kod ve sonuç kayıtlarının yerine geçmez.

## Her basamakta korunacak kayıt

Her deney veya teknik adım için şu sorular cevaplanır:

1. **Neden?** Hangi belirsizliği veya pratik sorunu çözmeye çalışıyoruz?
2. **Soru ve hipotez:** Deney hangi soruya cevap verecek; beklenti varsa bunun hipotez olduğu açık mı?
3. **Karar ve gerekçe:** Neyi seçtik, hangi alternatifleri neden şimdilik seçmedik?
4. **Uygulama:** Gerçekte kullanılan kart, pin, devre, firmware/kod sürümü ve ayarlar neler?
5. **Kanıt:** Ham dosya, log, hesap veya gözlem nerede? Yapılmayan kontroller açıkça yazılmış mı?
6. **Sonuç:** Kanıt neyi destekliyor, neyi desteklemiyor?
7. **Sonraki basamak:** Sonuç nedeniyle hangi adım seçildi ve neden?

**Kural:** Kod/protokol dosyasının depoda bulunması, kodun çalıştığı veya deneyin yapıldığı anlamına gelmez. “Planlandı”, “kodlandı”, “derlendi”, “kartta çalıştırıldı”, “ölçüldü” ve “sonuç yorumlandı” ayrı durumlar olarak kaydedilir. Sonuç çıkmadıysa bu da açıkça yazılır.

## Kod ile açıklama arasındaki bağ

- Deneyin **sorusu, gerekçesi ve adımları**: ilgili deneyin `README.md` / `protocol.md` dosyaları.
- Deneyin **kısa kimliği ve planlanan koşulları**: ilgili `metadata.yaml` ve varsa `experiment.yaml`. YAML dosyalarının firmware tarafından otomatik okunduğu varsayılmaz.
- Deneyin **gerçek uygulama kodu**: kod gerçekten oluşturulduğunda firmware/yazılım dosyasının tam depo yolu bu deftere ve deneyin protokolüne eklenir. Kod henüz yoksa “uygulama kodu henüz oluşturulmadı” denir; dosya yolu uydurulmaz.
- Deneyin **gerçek uygulama kaydı ve sonuçları**: ilgili deneyin `results.md`; ham veri varsa yerel `data/raw/` yolunda tutulur ve varsayılan olarak Git'e eklenmez.
- Deneyin **karar gerekçesi**: değişmeyen tasarım kararıysa ilgili ADR; yalnızca o deneye özgü seçimse deney protokolü ve oturum günlüğü.
- Depodaki **son durum ve sıradaki tek adım**: `STATUS.md`; büyük resim ve gezinme için `PROGRESS_TREE.md`.

## Basamak defteri

| Basamak | Neden yapılıyor? | Karar / gerekçe | Uygulama ve kanıt durumu | Sonraki karar kapısı |
|---|---|---|---|---|
| Hazırlık: envanter ve kapsam | Eldeki donanımı ve projenin sınırlarını bilmek; yanlış varsayımla kod yazmamak | İlk aşamada ESP32 dahili ADC; MCP3208 sonraya. Proje enerji/güç kalitesi analizörü değil | Donanım ve kararlar belgelenmiş; bazı bilgiler kullanıcı beyanına dayanır. Bağımsız fiziksel doğrulama olduğu varsayılmaz | Gerçek kart ve ADC pinini fiziksel pinout ile eşleştir |
| E00A — ham ADC gözlemi | SCT bağlanınca ham ADC dağılımının bias-only ve yüksüz duruma, ardından 100 W akkor yük koşuluna göre değişip değişmediğini görmek | İlk geçişte tek ESP32, 2 kS/s hedefi ve yaklaşık 1 s/koşul; önce temel istatistikler, grafik yalnız gerektiğinde | **PLANLANDI.** Firmware/uygulama kodu, kayıt ve fiziksel ölçüm henüz yapılmadı. Protokol: [E00A](experiments/E00A-raw-waveform-observation/README.md). CSV planı ve yerel yollar protokolde | Kart/GPIO pinout'u ve fiziksel bias düzeni doğrulandıktan sonra ilk ham kayıt |
| E00 — bias ADC API karşılaştırması | SCT bağlı değilken ham ADC sayısı ile mV API'sinin ne gösterdiğini anlamak | Temel, anlaşılır bir okuma; SCT'li koşuldan ayrı tut | **PLANLANDI.** Kod ve ölçüm henüz yok. [Protokol](experiments/E00-bias-adc-baseline/protocol.md) | E00A gözlemi ve fiziksel hazırlık sonrası gerçek okumaları kaydet |
| T005 / E01 — yüksüz temel okuma ve gürültü | Yüksüz sinyalin zaman içindeki davranışını görmek | Uzun kayıt, ilk kısa gözlemlerden sonra; gereksiz analiz eklememek | **PLANLANDI.** Fiziksel ölçüm yok. [T005](tasks/T005-noise-floor.md) | E00/E00A kanıtı temel kayıt planını destekliyor mu? |
| E08 — SCT karakterizasyonu | Önceki temel adımların ardından yük, kablo turu ve örnekleme hızı değişimlerinin etkisini incelemek | Temel hazırlıklar tamamlanmadan öne alınmayacak; E07 eski/uygulanmamış plan olarak kalır | **PLANLANDI.** Ölçüm yok. [E08](experiments/E08-sct-characterization/README.md) | Yalnız önceki sonuçlar ihtiyaç gösterirse uygulanır |

## Deney kodu eklendiğinde zorunlu bağlantı

Her yeni kod dosyası için:
- Dosya yolu ve ilgili commit/sürüm kaydedilir.
- Kodun hangi deney adımını gerçekleştirdiği belirtilir.
- Derleme kontrolü ile fiziksel çalıştırma birbirinden ayrılır.
- Kullanılan gerçek kart/GPIO ve ayarlar deney LOG'una yazılır.
- Sonuçlar ham veri veya log ile ilişkilendirilir.
- Sonraki kararın hangi bulguya dayandığı belirtilir.

## Kanıt ve durum dili

- **PLANLANDI:** soru, gerekçe ve kabul koşulu belirlendi; uygulama yapılmış demek değildir.
- **KODLANDI:** kod depoda mevcut; derlendiği veya çalıştığı anlamına gelmez.
- **DERLENDİ:** belirtilen ortamda derleme sonucu kaydedildi.
- **UYGULANDI:** hedef dosya/değişiklik depoya işlendi; fiziksel deney yapıldığı anlamına gelmez.
- **ÇALIŞTIRILDI:** kodun belirtilen donanım/yazılım ortamında çalıştırıldığına dair kayıt var.
- **ÖLÇÜLDÜ:** protokol, koşul ve veri/log ile gözlem kaydedildi.
- **YORUMLANDI:** sonuç ve sınırlamalar kanıta dayalı olarak yazıldı.

Bu durumlar birbirinin yerine kullanılamaz. Önceki kararlar silinmez; karar değişirse eski gerekçe ve değişiklik nedeni tarihçede korunur.
