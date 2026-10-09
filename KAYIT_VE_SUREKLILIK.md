# Kayıt, Sürümleme ve Süreklilik Politikası

## Temel taahhüt

**Geçmiş deneyim kayıtlarının üzerine yazılmaz.** Proje BERO'da süreklilik; önceki kodu, raporu, logu, ölçümü ve alınmış kararı kaybetmeden yeni bir sürüm veya yeni bir görev üzerinden ilerlemek demektir.

## Uygulama kuralları

1. **Deneyim kayıtları eklemeli ilerler.** Bir test raporu veya sonuç kaydı yayımlandıktan sonra yeni bulgu eski metni sessizce değiştirmez. Düzeltme ve yeni yorumlar tarih/sürüm belirtilerek eklenir; gerektiğinde EK-NNN veya yeni bir rapor dosyası açılır.
2. **Kod sürümleri korunur.** Yeni deneme, önceki kodun üstüne yazmak yerine yeni sürüm adıyla kaydedilir. Örneğin akim_test_v01, akim_test_v02. Git geçmişi ek koruma sağlar; fakat tek başına anlaşılır sürüm adlandırmasının yerini tutmaz.
3. **Çalışan sürüm ayrı tutulur.** Kullanıcının derleme başarısını doğruladığı kod, açık onay olmadan değiştirilmez veya görev klasörüne taşınmaz. Yeni denemeler ayrı dosya/sürüm üzerinden yürütülür.
4. **Yanlış veya eksik kayıt silinerek düzeltilmez.** Hata varsa düzeltme notu eklenir; neyin yanlış olduğu, neden düzeltildiği ve hangi yeni kanıtın bulunduğu belirtilir.
5. **Her kodun eşlik eden belgesi vardır.** Aynı sürüm adıyla bir .md dosyası; amaç, donanım, sürüm, test koşulları, doğrulananlar, loglardan çıkarılan dersler, bilinmeyenler ve sonraki adımı kaydeder.
6. **Kanıt ile yorum ayrıdır.** Ham ölçüm/log ve test koşulları mümkün olduğunca değiştirilmeden korunur. Yorumlar, ölçümün kendisiymiş gibi sunulmaz.
7. **Görev kapanışı geçmişi korur.** Görev tamamlanırken rapor kapanış özeti eklenir; sonraki görev yeni klasörde başlar. Yeni görev eski görev klasörünü yeniden kullanmaz.
8. **Ana hedef kapanışı yeni başlangıca köprü olur.** Hedefin sonuç raporu, doğrulanmış sonuçları ve açık noktaları toplar. Sonraki hedef ayrı bir kimlikle açılır; önceki hedefin kayıtları arşiv niteliğinde korunur.
9. **Belirsizlik açıkça işaretlenir.** Derlenmemiş, çalıştırılmamış veya ölçümle doğrulanmamış kod ve sonuçlar doğrulanmış olarak etiketlenmez.
10. **Yapısal belgeler güncellenebilir; tarihsel kayıtlar sessizce yeniden yazılamaz.** README ve klasör politikaları yapıyı açıklamak için değiştirilebilir. Deney raporları, sonuçlar, loglar ve sürümlenmiş kod ise eklemeli/değişmez geçmiş yaklaşımıyla yönetilir.

## Görev ve hedef adlandırma

- Ana hedef: HDF-NNN-KISA-AD/
- Görev: GRV-NNN/
- Görev raporları: RAPOR/
- Göreve ait deney kodları ve her kodun .md belgesi: KOD/

Her görev raporunda bağlı ana hedef belirtilir. Ana hedef dosyası görev sırasını, durumları ve sonuç bağlantılarını izler.

## Bu politikanın amacı

Bir süre ara verilse, yeni bir sohbet açılsa veya başka bir çalışma oturumuna geçilse bile proje; mevcut durum, son doğrulanmış sürüm, yapılan deneyler, elde edilen kanıtlar ve sıradaki adım üzerinden yeniden devam edilebilir olmalıdır.
