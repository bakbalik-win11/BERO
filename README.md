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



12. **Basamakları görünür tut.** Büyük görev içindeki anlamlı basamakları görev raporunda tarihli olarak izle; her küçük adımı ayrı resmî görev yapmak zorunda değilsin.
13. **Tecrübeyi kaynağından donanıma taşı.** Görevde edinilen tekrar kullanılabilir teknik bilgiyi ilgili donanım/sensör Markdown notuna aktar ve kaynak görev/deney bağlantısını koru.
14. **Doğrulanmış kod tek dosyadan ibaret değildir.** Her sürümü kendi koşulları, test belgesi, kanıtları ve sınırlarıyla ayrı sakla. Derleme, donanım testi ve ölçüm doğrulamasını birbirinden ayır.
15. **İlkeyi sohbet içinde bırakma.** Kalıcı bir ilke ortaya çıktığında uygun ana belgeye kaydet, uygulama adımını tanımla ve yazımı geri okuyarak doğrula. Ayrıntılar için [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) dosyalarına bak.


16. **Depoya her dönüşte önce bağlamı oku.** Yeni gün, ara sonrası veya yeni sohbet fark etmez: pusula, aktif görev, ilgili teknik kayıtlar ve uygulanacak ilkeler okunmadan işe dalma. Zorunlu sıra [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) içindedir.

**Temel ilke:** Önce doğru ölçüm, sonra doğru yorum, en son sistemin tamamlanması.

*BERO'da hedef yalnızca çalışması değil, neden doğru çalıştığının da bilinmesidir.*

Kayıtların nasıl korunacağı ve projenin oturumlar arasında nasıl sürdürüleceği için [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) dosyasına bak.

## Fikirden tecrübeye ve tekrar kullanıma akış

```text
TODO / Fikir
    ↓
Ana hedef
    ↓
Görev
    ↓
Alt görevler ve alt görev raporları (gerektiğinde)
    ↓
Görev ana raporu: kronolojik basamaklar, deneyler, kanıtlar, sonuçlar ve açık sorular
    ↓
Tekrar kullanılabilir teknik tecrübe → ilgili DONANIM / Sensör kaydı
                                  ↘ kaynak hedef + görev + ilgili alt görev/rapor atfı
```

- **Görev raporu**, tecrübenin nasıl ve hangi basamaklarda edinildiğinin kaynak izini korur.
- **DONANIM / Sensör kaydı**, aynı bileşen hakkında farklı hedeflerde biriken ayarları, kod parçalarını, sınırları ve kullanım tecrübelerini bir araya getirir; her kayıt kaynak hedefe ve göreve atıf verir.
- **Hedefler değişse de teknik kayıtlar birbirinin yerine geçmez.** Farklı hedeflerde oluşan kodlar ve ayarlar ayrı sürüm/kayıt olarak korunur; yeni bilgi eskisini ezmez. Her sürümün koşulu ve doğrulama durumu belirtilir.
- **Tecrübeyi yeniden kullanırken atfı izle:** donanım/sensör kaydından kaynak hedefe, göreve ve gerekiyorsa alt görev raporuna git; ilgili basamakları okuyup koşulları kontrol et.
- Bir donanım/sensör kaydında bulunması tek başına doğrulama sayılmaz. Gözlem, öneri, koşullu doğrulama ve doğrulama durumu birbirinden ayrılır.

Ayrıntılı uygulama adımları için [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) dosyalarına bak.

## Gelecek aşama: İngilizce sensör sayfaları

BERO'nun Türkçe donanım/sensör kayıtlarında biriken, kaynağı ve koşulları izlenebilir teknik tecrübe olgunlaştıkça İngilizce sensör sayfalarına aktarılacaktır. Amaç yalnızca çeviri değil, başka kişilerin inceleyip yeniden deneyebileceği güvenilir ve evrensel bir teknik bilgi katkısı oluşturmaktır.

- İngilizce sayfalar yalnızca tekrar kullanılabilir ve paylaşılmaya yeterince hazır bilgiyi kapsar.
- Her bilgi kaynağı olan Türkçe sensör/donanım kaydına ve oradan ilgili hedef, görev ve rapor basamaklarına geri izlenebilir.
- Farklı hedeflerdeki kod ve ayar varyantları ayrı korunur; birbirinin üzerine yazılmaz.
- Koşullar, kanıtlar, sınırlar ve doğrulama durumu açıkça belirtilir. Olgunlaşmamış bilgi evrensel gerçek gibi yayımlanmaz.
- İngilizce sensör sayfaları aylık olarak gözden geçirilir; yeni aktarılabilir bilgi yoksa sırf değişiklik olsun diye güncelleme yapılmaz.

Uygulama sorumluluğu ve kontrol akışı [Asistan İşletim Protokolü](ASISTAN_ISLETIM_PROTOKOLU.md) ve [Kayıt, Sürümleme ve Süreklilik Politikası](KAYIT_VE_SUREKLILIK.md) içindedir.

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
