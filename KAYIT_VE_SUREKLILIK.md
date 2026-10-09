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

## İlkelerin ve teknik tecrübenin kalıcılaştırılması

Sohbette ortaya çıkan kalıcı çalışma ilkeleri yalnızca sohbet geçmişinde bırakılmaz. İlkenin türüne göre ana kayıt yeri seçilir:
- Genel BERO çalışma ilkeleri: `README.md`
- Kayıt, kod sürümü ve deney geçmişi politikası: bu dosya
- Asistanın takip edeceği adımlar: `ASISTAN_ISLETIM_PROTOKOLU.md`
- Güncel durum ve sıradaki adım: `PROJE_PUSULASI.md`
- Tarihsel karar ve o günkü çalışma izi: `HISTORY/YYYY/YYYY-MM-DD.md`
- Görev basamakları, deney ve sonuç: ilgili `GOREVLER/GRV-NNN/RAPOR/`
- Donanıma/sensöre ait yeniden kullanılabilir teknik bilgi: ilgili `DONANIM/` altındaki Markdown notu
- Belirli doğrulanmış uygulama: koşulları ve test belgesiyle birlikte ilgili donanım kod kütüphanesi

### Basamak ve kod kütüphanesi kuralları

1. Büyük görev içindeki anlamlı basamaklar görev raporunda tarihli/kronolojik olarak izlenir; her küçük işlem için ayrı resmî görev açmak gerekmez.
2. Her basamak değişiminde ne değiştiği, neden geçildiği, hangi kanıtın elde edildiği, hangi sürümün korunduğu ve hangi soruların açık kaldığı kaydedilir.
3. Görevde edinilen tekrar kullanılabilir teknik tecrübe ilgili donanım/sensör MD notuna aktarılır ve kaynak görev/deney bağlantısı korunur.
4. Bir bilginin donanım notunda yer alması onu tek başına doğrulanmış yapmaz. Durum ve kapsam açıkça etiketlenir: öneri, gözlem, koşullu doğrulandı veya doğrulandı.
5. Her doğrulanmış kod sürümü ayrı ve değişmez bir sürüm olarak tutulur; kodun yanında aynı sürüme ait MD belgesi, test koşulları, kanıt, sınırlar ve kaynak görev bulunur. Yeni sürüm eskisinin üzerine yazmaz.
6. Derleme, gerçek donanımda çalışma ve ölçüm sonucu ayrı doğrulama seviyeleridir. Yalnızca eldeki kanıtın desteklediği seviye işaretlenir.
7. Bir modelde veya koşulda doğrulanan kural, test edilmeden diğer modellere/koşullara genellenmez.

Bu kayıt düzeni bir sohbetten diğerine aktarılabilmelidir; uygulamanın doğruluğu yalnızca asistanın hatırlamasına bağlı olmamalıdır.

