# Fikir Havuzu ve Değişken Öncelikler

**Amaç:** Sohbet sırasında ortaya çıkan fikirleri, henüz görev olmadan kaybetmeden saklamak ve önceliklerini ihtiyaç değiştikçe güncelleyebilmek.

## Kullanım kuralları

- Yeni fikirler önce bu dosyaya girer; otomatik olarak aktif göreve dönüşmez.
- Her fikre kalıcı bir `I###` kimliği verilir. Durum veya öncelik değişse de kimlik değişmez.
- Öncelik sırası sabit değildir. Kullanıcı yeni bilgi verdiğinde sıralama güncellenir; değişiklik ve gerekçe karar geçmişine eklenir.
- Öncelik alanı boşsa henüz sıralama kararı verilmemiştir. Asistan kendi başına aciliyet varsaymaz.
- Bir fikir uygulanmaya hazır olduğunda görev listesine `T###` görevi olarak alınır; fikir kaydı silinmez, görev ID'sine bağlantı eklenir.
- Fikir ertelenirse veya önceliği düşerse silinmez. İptal edilirse nedenini kaydet.
- Bir fikir hakkında sohbet içinde yeni ayrıntı verilirse önce mevcut ID'li kaydı güncelle; aynı fikri tekrar tekrar yeni kayıt olarak açma.

## Alanlar

- **Öncelik:** P1 = şu an öne alınacak; P2 = sıradaki uygun fırsatta; P3 = düşük öncelik/ileride; boş = kararlaştırılmadı.
- **Durum:** FİKİR, DEĞERLENDİRİLİYOR, BEKLİYOR, GÖREVE ALINDI, ERTELENDİ, İPTAL.
- **Gerekçe / tetikleyici:** Önceliği değiştirebilecek ihtiyaç, bağımlılık veya yeni bilgi.
- **Görev bağlantısı:** Göreve dönüştürüldüyse ilgili T-ID.

## Fikirler

| Fikir ID | Fikir | Öncelik | Durum | Gerekçe / tetikleyici | Görev bağlantısı |
|---|---|---|---|---|---|
| I001 | Python programlarının sayısını, sorumluluklarını ve aralarındaki veri akışını ayrı mimaride tanımlamak | — | FİKİR | Kullanıcı programların nasıl oluşacağını aşamalı anlatacak; sayı ve görev dağılımı şimdiden sabitlenmeyecek. | T007 ile ilişkili |
| I002 | Home Assistant'taki verileri PC'ye taşıyacak Python aktarım akışını tanımlamak | — | FİKİR | Veri HA'da toplanacak, PC'ye aktarılacak ve PC'de işlenecek. Uygulama ayrıntıları sonraki açıklamalarla netleşecek. | T007 ile ilişkili |
| I003 | PZEM akışı ve üç SCT kanalının kararlı alanlarını deneylerle geliştirilecek kriterlerle Python'da etiketlemek | — | FİKİR | Kabul kriteri ve etikette tutulacak alanlar henüz kararlaştırılmadı. | — |

## Öncelik / karar geçmişi

Henüz kayıtlı bir öncelik değişikliği yok.

Yeni kararları şu biçimde ekle:
- Tarih — Fikir ID — eski öncelik/durum → yeni öncelik/durum — gerekçe — kullanıcı kararı mı, öneri mi?

## Gözden geçirme

Yeni fikirleri kaydet; yalnızca kullanıcı öncelik belirlediğinde veya yeni bilgi sıralamayı değiştirmeyi gerektirdiğinde öncelikleri değiştir. Aktif görev sayısını şişirme. Bu dosya fikirlerin geçmişini korur; `tasks/README.md` uygulanacak işlerin listesidir.
