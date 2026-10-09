# BERO TODO — Fikirler ve Bekleyenler

> Burası, resmî görev açmadan önce akla gelen fikirleri ve küçük yapılacakları yakaladığımız ortak listedir. Liste, Home Assistant'taki yapılacaklar mantığıyla kolayca takip edilir; fikirlerin sonucu ve geçmişi de korunur.

## İşleyiş kuralları

- **Her bölümde en yeni kayıt en üsttedir.** Yeni fikirler “Açık fikirler” bölümünün en üstüne eklenir. Bölüm değiştirilen kayıt, hedef bölümün en üstüne taşınır.
- Her madde ilk kayıt tarihini taşır: `Eklenme: YYYY-MM-DD`. İlk kayıt tarihi hiçbir zaman sonradan değiştirilmez.
- `[ ]` = sonuçlanmamış/açık; `[x]` = sonucu belli olup kapanmış madde. Tikin anlamı teknik başarı değil, fikir kaydının kapanmış olmasıdır; sonucu ayrıca yazılır.
- Her kapanan maddede sonuç ve tarih açıkça bulunur: `Tamamlandı`, `Vazgeçildi` veya `Görev tamamlandı`. Vazgeçildiyse gerekçe yazılır.
- Fikir resmî göreve dönüşürse sonuç hemen kapanmaz. Madde **“Göreve dönüştü — görev açık”** durumuna geçer, `[ ]` kalır ve görev kimliği/linki eklenir. Bağlı resmî görev tamamlanana kadar TODO maddesi açık kalır.
- Bağlı görev tamamlandığında görev sonucu doğrulanır; madde `[x]` yapılır, `Sonuç: Görev tamamlandı` ve tamamlanma tarihi eklenir, sonra “Sonuçlananlar” bölümüne taşınır.
- Tamamlanan veya vazgeçilen fikirler silinmez; “Sonuçlananlar” bölümünün en üstüne taşınır. İlk kayıt tarihi korunur.
- Tarih güvenilir biçimde bilinmiyorsa tarih uydurulmaz.
- TODO maddesi resmî görev değildir. Görev açılınca `GOREVLER/GRV-...` altında ayrı kayıt oluşturulur ve bağlantısı burada tutulur.
- HISTORY günlük olay akışını; TODO ise fikirlerin mevcut durumunu ve sonucunu gösterir.

## 1. Açık fikirler — en yeni en üstte

_Yeni fikirleri bu satırın hemen altına ekle. Henüz sonuçlanmamış maddeler burada kalır._

## 2. Göreve dönüşenler — açık görevler

_Bu bölümdeki maddeler **açık kalır**. Görev oluşturulmuş olması fikrin tamamlandığı anlamına gelmez. İlgili resmî görev tamamlanana kadar `[ ]` kalır. En yeni dönüşüm en üstte._

## 3. Sonuçlananlar — en yeni sonuç en üstte

_Tamamlanan, vazgeçilen veya bağlı görevi tamamlanan maddeler buraya taşınır. Her maddede sonuç, sonuç tarihi ve gerekirse gerekçe/bağlantı bulunur._

### Madde şablonları

**Yeni fikir**
- [ ] **Fikir başlığı**
  - Eklenme: YYYY-MM-DD
  - Açıklama:
  - Sonuç: Bekliyor

**Göreve dönüştü — hâlâ açık**
- [ ] **Fikir başlığı**
  - Eklenme: YYYY-MM-DD
  - Sonuç: Göreve dönüştü — görev açık
  - Görev: [GRV-XXX](../GOREVLER/GRV-XXX/RAPOR/README.md)
  - Görev durumu: Açık

**Sonuçlandı**
- [x] **Fikir başlığı**
  - Eklenme: YYYY-MM-DD
  - Sonuç: Tamamlandı / Vazgeçildi / Görev tamamlandı
  - Sonuç tarihi: YYYY-MM-DD
  - Gerekçe veya sonuç:
