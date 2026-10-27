# Python Program Mimarisi

**Durum:** TASLAK — kullanıcı açıklamalarına göre aşamalı olarak doldurulacak.  
**Kural:** Program sayısı, dosya/modül sınırları ve her programın sorumlulukları kullanıcı sonraki parçaları anlattıkça kaydedilecek. Şimdilik bunlar hakkında karar verilmiş sayılmaz.

## Bilinen hedef

- Home Assistant'taki kayıtları PC'ye taşıyan Python kodu olacak.
- Veriler PC'de işlenecek.
- PZEM akışının ve üç SCT kanalının kararlı alanlarını bulma ve etiketleme işlemleri Python tarafında yapılacak.
- Kararlılık kabul kriterleri deneylerle geliştirilecek; etiket şeması da değerlendirilecek.

## Henüz belirlenmedi

- Kaç Python programı / çalıştırılabilir süreç olacağı.
- Programların dosya/modül yapısı ve sorumluluk sınırları.
- HA'dan veri aktarım yöntemi, kayıt biçimi ve aktarım sıklığı.
- Analiz adımlarının birbirinden ayrılma biçimi ve aralarındaki veri sözleşmeleri.
- Hangi ara çıktılar ve nihai veri dosyalarının üretileceği.

## Çalışma yöntemi

Kullanıcının sohbet sırasında açıkladığı her yeni hedef veya görev, uygun mimari belgesine ya da görev kartına işlenecek. Belirsiz ayrıntılar varsayımla doldurulmayacak. Depoya yapılan her değişiklikten sonra ilgili dosya yeniden okunarak doğrulanacak.

Bu belge yalnızca hedef ve açık kararları kaydeder; kodun yazıldığını veya akışın çalıştığını iddia etmez.

## Parçalar ve ilerleme durumu

| ID | Parça | Kaydedilen hedef | Gerçekleşen | Bekleyen | Görev |
|---|---|---|---|---|---|
| PY-01 | HA'dan PC'ye veri aktarımı | HA kayıtlarını PC'ye taşıyan Python kodu | Hedef mimariye yazıldı | Aktarım yöntemi ve kod | T007 ile ilişkili |
| PY-02 | PZEM verisini işleme | PC'de PZEM kararlı alanlarını bulma | Hedef mimariye yazıldı | Algoritma ve deney kriterleri | Henüz ayrılmadı |
| PY-03 | Üç SCT kanalını işleme | Her SCT kanalının kararlı alanlarını PC'de ayrı belirleme | Hedef mimariye yazıldı | Algoritma ve deney kriterleri | Henüz ayrılmadı |
| PY-04 | Etiketleme | Kararlı alanları etiketleme | Hedef mimariye yazıldı | Etiket alanları ve kabul kriterleri | Henüz ayrılmadı |

## İlerleme güncelleme kuralı

- Yeni parça geldikçe PY kimliğiyle bu belgeye eklenir.
- Bir parça uygulandığında yalnızca o satırın gerçekleşen ve bekleyen alanları güncellenir.
- Yapılacak somut işler görev listesine T-ID ile eklenir; ilgili bağlantı burada tutulur.
- Deney sonuçları, öğrenilenler ve başarısız denemeler uygun Markdown (.md) dosyasına yazılır.
- Program sayısı, dosya sınırları ve görev dağılımı kullanıcı açıklamaları geldikçe belirlenir; şimdiden varsayılmaz.
- Fikir havuzu [IDEA_BACKLOG.md](../../IDEA_BACKLOG.md) içinde, Python parça durumları bu belgede tutulur.

Bu tablo hedefleri ve ilerleme durumunu izler; kodun yazıldığı anlamına gelmez.
