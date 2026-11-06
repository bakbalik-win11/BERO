# I007 — 2026-11-06 uzun OFF gözlemi / CH1-1T

## Oturum tanımı

- Oturum: `I007-2026-11-06-02`
- Kullanıcının bildirdiği fiziksel yük kesme zamanı: 16:14 (+03:00)
- İncelenen aralık: 16:14:00.752–16:34:59.754 (+03:00)
- Süre: yaklaşık 20 dakika 59 saniye
- Kaynak: kullanıcı tarafından sağlanan `history (49).csv`
- Kaynak CSV boyutu: 4,772,658 byte
- Kaynak CSV SHA-256: `235ad89116f3d0a36205acafbe4eec1f29baa9043567e59f71b3d12835c45e74`
- İncelenen entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_ham_akim`
- Kanal/donanım: CH1-1T, SCT013 30A/1V, GPIO32 / ADC1_CH4
- Analiz edilen değer: K çarpımı öncesi katsayısız ct_clamp çıktısı; bu değer ADC'nin tekil ham örneği değildir.
- Kullanıcı fiziksel yükün 16:14'te kapatıldığını bildirdi. Bu fiziksel durum bilgisi kullanıcı raporudur.

## Veri bütünlüğü ve sınırlamalar

- SCT serisinde 1,260 sayısal kayıt bulundu; eksik/sayısal olmayan SCT değeri yok.
- Gerçek timestamp aralığı medyan 1.000 s; ortalama 1.000 s. Bu dışa aktarımda gözlenen hız yaklaşık 1 Hz'dir. 500 ms / 2 Hz varsayılmamıştır.
- PZEM akım entity'sinin son kaydı 16:13:12.898'dir ve değeri 0.000 A'dır. 16:14 sonrası için PZEM akımında yeni kayıt yoktur. Bu nedenle PZEM'in tüm OFF penceresi boyunca sıfır kaldığı CSV ile doğrulanamaz; ekrandaki 0.000 A göstergesi son değer olarak kalmış olabilir.
- SSR ve UDP olayları 16:14 sonrasında da 40 s OFF / 20 s ON düzeninde devam etmektedir. Bu olaylar test sürücüsünün komutlarını gösterir; kullanıcının bildirdiği fiziksel yükün açılıp kapandığını kanıtlamaz.
- Ham CSV bu commit'e eklenmedi; kaynak dosya SHA-256 ile tanımlandı. Ham kaynak kullanıcı tarafından sağlanan dosya olarak korunmalıdır.

## Genel istatistikler — 16:14:00.752–16:34:59.754

| Ölçüt | Değer |
|---|---:|
| n | 1,260 |
| Medyan | 0.009918 A |
| MAD | 0.001950 A |
| 1.4826 × MAD | 0.002891 A |
| Ortalama (yalnız betimleyici) | 0.009308 A |
| Standart sapma (popülasyon) | 0.002874 A |
| P05 | 0.004407 A |
| P25 | 0.007156 A |
| P75 | 0.011237 A |
| P95 | 0.013439 A |
| P99 | 0.015288 A |
| IQR | 0.004081 A |
| Minimum | 0.000000 A |
| Maksimum | 0.017821 A |
| 0.015 A üzerindeki oran | %1.35 |
| Tam sıfır kayıt oranı | %0.40 |

Medyan ve MAD, OFF davranışını özetlemek için ana sağlam istatistiklerdir. Ortalama ve standart sapma yalnız betimleyici karşılaştırma amacıyla raporlanmıştır. 0.015 A değeri eşik olarak seçilmemiştir; yalnızca gözlenen örneklerin %1.35'inin bu değeri aştığı raporlanmıştır.

## Zaman içindeki değişim

İlk bölüm (16:14:00–16:21:59):
- n=479
- medyan=0.010574 A
- MAD=0.002364 A
- P05=0.004048 A
- P95=0.014383 A

İkinci bölüm (16:22:00–16:34:59):
- n=779
- medyan=0.009575 A
- MAD=0.001614 A
- P05=0.005043 A
- P95=0.012570 A

İkinci bölümde ilk bölüme göre medyan yaklaşık %9.4, MAD yaklaşık %31.7 daha düşüktür. Bu, gözlem aralığında merkez ve yayılımın sabit olmadığını; özellikle dağılımın daralma eğilimi gösterdiğini destekler. Bunun fiziksel nedeni bu CSV'den belirlenemez.

Dakika bazlı medyanlar yaklaşık 0.00787–0.01097 A, dakika bazlı MAD değerleri yaklaşık 0.00098–0.00282 A aralığındadır. Bu değişim, OFF referansını tek bir sabit sayı olarak ele almamamız gerektiğini gösterir.

## Yorum

1. Kullanıcının görsel gözlemiyle uyumlu olarak, yük kesildikten sonraki CH1-1T katsayısız çıktı sıfıra inmemiş; ayrı bir yüksüz dağılım oluşturmuştur.
2. Bu oturumun genel medyanı 0.009918 A ve MAD değeri 0.001950 A'dır. Bunlar bu oturumun betimleyici sonuçlarıdır; henüz cutoff eşiği veya evrensel sıfır tabanı değildir.
3. Zamanla bant daralması sayısal olarak da görülmektedir. İlk ve ikinci alt dönem MAD'leri farklıdır. Bu nedenle tek bir OFF medyanı/eşiği ile tüm zaman davranışını temsil etmek şimdilik zayıf bir varsayım olur.
4. Grafikteki periyodik yapı ve sıçramalar ham seride korunmuştur; aykırı değerler silinmemiştir.
5. Remanans, bias devresi, ADC, sıcaklık veya çevresel etki nedenlerinden hiçbiri bu oturumla kanıtlanmış değildir.

## 15 W karşılaştırma deneyi için çıkarımlar

- Aynı CH1-1T fiziksel yerleşimi ve aynı firmware/ölçüm ayarları korunmalı; deney sırasında parametre değiştirilmemeli.
- OFF karşılaştırma aralığı yaklaşık 21 dakika olduğundan, ilk karşılaştırma için 15 W ON kaydı da en az 21 dakika; tercihen 30 dakika alınabilir.
- PZEM akım entity'sinin ON deneyi boyunca yeni timestamp'lerle güncellendiği test öncesi doğrulanmalıdır. Bu OFF CSV'sinde PZEM akımı 16:13:12.898 sonrasında güncellenmemiştir.
- 15 W yükün gerçek türü ve etiketi deney kaydına yazılmalı; PZEM'in kararlı akım/güç değerleri ölçülmelidir.
- Karşılaştırma: medyan, MAD, P05/P95/P99, zaman dilimli medyan/MAD ve OFF/15 W dağılımlarının örtüşmesi.
- 15 W verisi ayrı yük profili/deneydir; I007 OFF havuzuna veya 100 W ON eğitim grubuna karıştırılmaz.

## Sonuç durumu

**OFF oturumu sayısal olarak işlendi ve kaydedildi.** Bu rapor tek oturumdur; sıfır eşiği belirlemek veya 15 W algılanabilirliği hakkında nihai hüküm vermek için yeterli değildir. I007'nin önceki çok kanallı 2026-11-05 oturumuyla doğrudan havuzlanmamalıdır; mevcut oturum CH1-1T tek kanal ölçümüdür.


## Sonradan eklenen yöntem düzeltmesi — 2026-11-06

Bu raporun önceki yorumunda tekil örnek dağılımı ve yüzdelikler, K uygulanmış 0.20 A sınırıyla doğrudan ilişkilendirilemez. Raporun ölçtüğü seri **K öncesi katsayısız ct_clamp çıktısıdır**. Ayrıca tekil örneklerin eşik üstünde görülmesi süreklilik kanıtı değildir. Bu nedenle rapordaki tekil yüzdelikler yalnızca katsayısız OFF dağılımının betimleyici istatistikleri olarak kalır; 0.20 A sınıflandırma kuralını doğrulamaz veya çürütmez.

İlerideki sınıflandırma değerlendirmesi için K dönüşümü doğru uygulanmalı ve eşik davranışı zaman pencereleri, eşik üstünde kalma süresi, devamlılık, medyan/MAD ve zaman kararlılığıyla analiz edilmelidir. Ham veri değişmez; kısa sıçramalar tek başına durum değişimi sayılmaz. Süre/pencere parametreleri henüz belirlenmemiştir.
