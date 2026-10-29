# Görev kartları

Görev kartları yol haritasındaki işi küçük, kabul ölçütü belli adımlara böler. **ROADMAP.md** genel fazları, **STATUS.md** ise güncel durumu gösterir.

## Çalışma kuralı
- Bir oturumda STATUS.md içindeki tek aktif göreve odaklan.
- Yeni bir fikir çıkarsa mevcut görevi bölme; açık soruya veya uygun sonraki göreve not et.
- Bir kartın durumu, kanıtın gösterdiği seviyeyi aşamaz.
- Kullanıcıdan teknik ayrıntıları kendi başına değerlendirmesini bekleme. Gerekli kanıtı asistan bulmalı veya hangi fiziksel kanıtın gerektiğini açıkça söylemeli.
- Fiziksel olarak görülmeyen bileşen doğrulandı sayılmaz. Bilinmeyen alanları tahminle doldurma.
- 220–240 V AC tarafında çalışma ve güvenlik onayı yetkin kişi sorumluluğundadır. Güvenlik kontrolü bitmeden şebeke bağlantısı/deneyi başlatılmaz.

## Durum sözlüğü
- **PLANLANDI:** hedef ve kabul koşulu belirlendi.
- **HAZIRLANDI:** taslak veya plan hazır.
- **UYGULANDI:** çıktı hedef dosyaya/ortama işlendi.
- **DOĞRULANDI:** ilgili kontroller ve kanıt gözden geçirildi.
- **TAMAMLANDI:** kabul ölçütlerinin tamamı kanıtla karşılandı.
- **ENGELLENDİ:** gereken erişim, donanım, karar veya test eksik.
- **DEVAM EDİYOR:** iş başladı ancak kabul ölçütlerinin tamamı karşılanmadı.

Bir kart, yalnızca doküman dolduruldu diye otomatik olarak TAMAMLANDI olmaz.

## Sıra ve bağımlılıklar

| ID | Görev | Faz | Durum | Bağımlılık |
|---|---|---:|---|---|
| T001 | Fiziksel donanım envanteri | 0.1 | TAMAMLANDI — kullanıcı beyanındaki stok, kart rolleri ve bias devresi kaydedildi; kalan analog tasarım ayrıntıları sonraki görevlere ait | — |
| T002 | Güvenlik kontrolü | 0.2 | TAMAMLANDI — kullanıcı tüm kontrol maddelerini tamamladığını beyan etti; fiziksel durum bağımsız doğrulanmadı | T001 |
| T003 | PZEM tabanlı model hata hedefi | 0.3 | TAMAMLANDI — ±%4 bağıl sapma; Python'da geçerli örnekler için OK kararı | T001 |
| T004 | Analog ön uç | 1.1 | TAMAMLANDI — SCT jack/bias devresi ve dahili ADC yaklaşımı belgelendi; laboratuvar düzeyinde ölçüm şartı yok | T002, T003 |
| T005 | ADC temel okumaları ve E01 gürültü tabanı | 1.2 | PLANLANDI — önce SCT bağlı değilken ham ADC ve mV API'leri; sonra SCT bağlı ve akım yok; uzun E01 kaydı daha sonra | T004 |
| T006 | SCT kalibrasyonu | 1.3 | PLANLANDI | T005 |
| T007 | Python program mimarisini kullanıcı hedeflerine göre tanımla | 3–7 | DEVAM EDİYOR — ayrı mimari belgesi açıldı; program sayısı ve sorumluluklar sonraki açıklamalarla doldurulacak | HA→PC aktarım hedefi, PZEM/SCT analiz ve etiketleme hedefi |

## Kart açma
Yeni görev için _template.md dosyasını kopyala; bir sonraki T numarasını kullan, bağımlılıkları ve ölçülebilir kabul koşulunu yaz. Yeni kart eklendiğinde bu tabloyu, ROADMAP.md ve gerekiyorsa STATUS.md'yi güncelle.

## Fikir havuzu
Henüz göreve dönüştürülmemiş veya önceliği değişebilecek fikirler [IDEA_BACKLOG.md](../IDEA_BACKLOG.md) içinde tutulur. Fikirler bu listede korunur; yalnızca seçilip uygulanmaya hazır olduğunda görev listesine alınır. Fikir ID'si görev açıldıktan sonra da korunur.

## 2026-10-29 — Paketleme öncesi E00A ham sinyal gözlemi eklendi

Kullanıcı kararıyla E00A, mevcut E00/E01 ve veri paketleme kararından önce gelecek şekilde eklendi. Amaç ham ADC dalgasını bias-only, SCT yüksüz ve 100 W ampul koşullarında farklı örnekleme hızlarında kaydetmek; PC'de yavaş oynatmak ve ortalama/min/max/peak-to-peak/standart sapma gibi temel istatistikleri karşılaştırmak. İlk aşamada çift buffer, DMA veya laboratuvar düzeyinde veri kaybı analizi zorunlu değil. E00A sonuçları basit aktarımın yeterli olup olmadığına karar vermek için kullanılacak. Henüz ölçüm yapılmadı.

## 2026-10-29 — İlk ADC öğrenme testi eklendi

E00, SCT bağlı olmadan bias orta noktasını dahili ADC ile okuyan ilk adım olarak eklendi. Aynı örnek döngüsünde `analogRead()` ham sayısı ve `analogReadMilliVolts()` çıktısı karşılaştırılacak. Ardından SCT bağlı fakat akım yok durumu, daha sonra uzun E01 gürültü kaydı gelecek. Henüz fiziksel test yapılmadı.

## 2026-10-29 — Kaynak raporu incelemesi

SCT013-030 raporu ve CT satürasyonu notu genel teknik referans olarak değerlendirildi. Bu belge incelemesi T005 durumunu değiştirmez; fiziksel ölçüm yapılmadı. Aktif görev T005/E01 olarak kalır.


## 2026-10-29 — E08 planı

E08, görev indeksinde aktif görevin yerini almaz. T005/E00-E01 yüksüz temel ölçüm hazırlığı tamamlanmadan E08 uygulamasına geçilmeyecek. E08'in amacı ve aşamaları [E08 genel açıklamasında](../experiments/E08-sct-characterization/README.md) yer alır. Fiziksel ölçüm yapılmadığı için E08 sonuçları tamamlandı olarak işaretlenmez.
