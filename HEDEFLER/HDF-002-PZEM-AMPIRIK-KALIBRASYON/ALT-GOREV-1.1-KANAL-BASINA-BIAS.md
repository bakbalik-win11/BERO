# HDF-002 — Alt Görev 1.1
## Kanal başına BIAS ölçümü ve prototip modifikasyonu

Her SCT kanalının BIAS değerini kendi ölçüm zincirinde ayrıca ölçmek, mevcut prototipte yapılacak yeni bir tasarım değişikliğidir. Bu nedenle ayrı bir donanım modifikasyonu ve doğrulama alt görevi olarak izlenecektir.

- Üç SCT kanalının her biri için ayrı BIAS ölçüm yolunun tasarımı yapılır.
- Kullanıcı gerekli fiziksel modifikasyonları yapacaktır; modifikasyon öncesi ve sonrası donanım/bağlantı durumu kaydedilir.
- Her kanalın SCT verisi kendi BIAS ölçümüyle ilişkilendirilir; kanalların BIAS değerleri birbirinin yerine kullanılmaz.
- BIAS ölçümünün SCT örnekleme düzenine ve veri kaybına etkisi kayıtlarla incelenir; etkisiz olduğu baştan varsayılmaz.
- Eski kodlar ve deney kayıtları korunur. Donanım ve yazılım değişiklikleri ayrı sürüm/deneme kaydıyla eklenir.

**Alt görev çıktısı:** Üç SCT kanalı için SCT + kendi BIAS ölçüm yolunu gösteren güncel bağlantı kaydı, fiziksel modifikasyon notları ve doğrulama soruları.

**Kanıt sınırı:** Bu alt görev planlanmıştır. Modifikasyonun yapıldığı veya üç kanalda BIAS ölçümünün çalıştığı henüz iddia edilmez.
