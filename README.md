# Proje BERO

## BERO ÇALIŞMA PRENSİPLERİ

Proje BERO, yalnızca çalışan bir sistem üretmeyi değil, ölçülebilir, doğrulanabilir ve sürdürülebilir bir sistem kurmayı hedefler.

1. **Ölçmeden varsayım yapma.** Bir değerin doğru görünmesi, ölçüm zincirinin doğru çalıştığını kanıtlamaz.
2. **Tek seferde tek değişken.** Donanım, yazılım, zamanlama ve algoritma değişikliklerini birbirinden ayır.
3. **Çalışan durumu koru.** Her test öncesinde mevcut durumu kaydet; doğrulanmış çalışan kodu koru.
4. **Kanıtla ilerle.** Beklenen sonuçla gerçek ölçümü karşılaştır; her deney bir varsayımı doğrulasın veya eleyebilsin.
5. **Sorunun kaynağını bul.** Belirtiyi geçici olarak gidermek yerine nedenini belirle.
6. **Doğrulamadan sonraki aşamaya geçme.** Her katmanı bağımsız test et ve sonuçlarını kaydet.
7. **Başarısız test de veridir.** Sonucu, koşulları ve çıkarımları kayıt altına al; aynı belirsizliği yeniden üretme.
8. **Geçmiş deneyimin üzerine yazma.** Rapor, log, ölçüm ve kod sürümlerini koru; yeni bulguları yeni sürüm veya tarihli ek kayıt olarak ekle.
9. **Her kodun bir belgesi olsun.** Kodun yanında test koşullarını, doğrulananları, loglardan öğrenilenleri ve açık kalan noktaları anlatan bir .md dosyası tut.
10. **Doğrulanmış ile varsayılanı ayır.** Derleme, çalışma ve ölçüm kanıtı yoksa sonucu doğrulanmış gibi sunma.
11. **Yeni görev, yeni kayıt alanı.** Bir görev kapandıktan sonra sonraki görev yeni kimlik ve klasörle başlar; eski görev geçmişi referans olarak kalır.

**Temel ilke:** Önce doğru ölçüm, sonra doğru yorum, en son sistemin tamamlanması.

*BERO'da hedef yalnızca çalışması değil, neden doğru çalıştığının da bilinmesidir.*

Kayıtların nasıl korunacağı ve projenin oturumlar arasında nasıl sürdürüleceği için [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) dosyasına bak.

## Proje pusulası

Projenin genel çerçevesi, aktif ana hedefi, güncel durumu ve oturumlar arası devam notu için [PROJE_PUSULASI.md](PROJE_PUSULASI.md) dosyasını başlangıç noktası olarak kullan.

## TODO — fikirler ve bekleyenler

Henüz resmî görev açmaya gerek olmayan fikirleri [TODO/README.md](TODO/README.md) listesinde takip et. Yeni fikirler üstte; tamamlanan veya vazgeçilen fikirler neden/sonuç bilgisiyle sonuçlananlar bölümüne taşınır. Göreve dönüşen fikir, bağlı görev tamamlanana kadar açık kalır.
## Asistanın çalışma komutları

“Ara rapor” ve “günü kapa” komutlarında uygulanacak kontrol listesi [ASISTAN_ISLETIM_PROTOKOLU.md](ASISTAN_ISLETIM_PROTOKOLU.md) dosyasında tanımlıdır.

## Çalışma geçmişi

Projenin tarih sıralı ilerleyişi için [HISTORY/](HISTORY/README.md) klasörünü kullan. “Ara rapor” ve “günü kapa” komutlarında tarihli günlük kaydı zorunludur.

## Günlük kontrol listesi

Günlük yapılacaklar, ara rapor ve gün sonu adımları tiklenebilir biçimde [GUNLUK/](GUNLUK/README.md) altında izlenir. Yeni günlük dosyası GitHub Actions ile her gün Türkiye saatiyle yaklaşık 03.05'te otomatik oluşturulacak şekilde ayarlanmıştır.
