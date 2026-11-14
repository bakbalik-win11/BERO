# 2026-11-14 — E19 ADS1115 yüksüz sıçramaları: kullanıcı açıklaması ve yeni karşılaştırma planı

## Kullanıcıdan gelen fiziksel kurulum açıklaması
- Kullanıcı açıkça bildirdi: ADS1115'in gözlem yaptığı hatta aç/kapa yapılmıyor.
- Aç/kapa rölesi gözlenen hatta bağlı değil.
- Anahtarlama başka bir ESP tarafından yürütülüyor; ADS1115'in bulunduğu ESP ile aynı ESP değil.
- Buna rağmen ADS1115 ölçümünde tekrarlayan yüksek sıçramalar görülüyor.
- Kullanıcı, anahtarlama sesini duyduğunu ve sıçramalardan şüphelendiğini belirtti. Ses/işitsel gözlem kullanıcı bildirimi olarak kaydedilir; elektriksel kuplajın tek başına kanıtı değildir.

## Önceki istatistik raporuna düzeltme
Önceki rapordaki 72 yüksek örneğin 57'sinin HA switch state geçişlerine 10 saniye içinde denk gelmesi yalnızca zaman korelasyonudur. Yeni fiziksel kurulum bilgisiyle bu ilişki, ölçülen hattın anahtarlanması veya doğrudan röle etkisi şeklinde yorumlanamaz.

**Güncel yorum:** Ayrı bir ESP'deki anahtarlama olayı ile ADS1115 ölçüm zincirindeki sapmalar arasında olası parazit/kuplaj ilişkisi araştırılacaktır. Bu henüz hipotezdir; nedensellik veya fiziksel mekanizma kanıtlanmış değildir. Önceki rapordaki zaman yakınlığı sayıları değişmez; yalnızca fiziksel yorumları bu ek kayıtla sınırlandırılır.

## Sayısal referans — önceki E19 kaydı
- 1.669 sayısal ADS1115 state kaydı.
- 0.005 A ve altı 1.592 kayıt (%95.39); ortalama 0.00122955 A, medyan 0.00128425 A, örnek SD 0.00028426 A.
- 0.040 A ve üzeri 72 kayıt (%4.31); medyan 0.046599 A, ortalama 0.051456 A.
- En yüksek tek örnek 0.353055 A.
- Bu değerler yeni testin karşılaştırma tabanıdır; filtre veya eşik olarak uygulanmayacaktır.

## 2026-11-14 için kullanıcı tarafından bildirilen sonraki işlem
- Aç/kapa mekanizması/kodları mevcut düzenekten çıkarılacak.
- Kodlar yenilenecek ve yeni modül oluşturulacak.
- Yeni modülün bu akşam uzun süreli kaydı alınacak.
- Yeni kayıt, önceki E19 ADS1115 yüksüz gözlem istatistikleriyle karşılaştırılacak.

## Yeni kayıt için karşılaştırma ilkeleri
1. Yeni modülün fiziksel bağlantısı, sensör, ADC ayarları, firmware sürümü ve YAML/commit kimliği kayıt altına alınmalı.
2. Ölçülen hatta aç/kapa yapılmadığı ve rölenin o hatta bağlı olmadığı test koşulu olarak açıkça yazılmalı.
3. Yeni CSV'de ADS1115 akım state'leri, unavailable aralıkları ve zaman damgaları korunmalı.
4. Önceki kayıtla aynı istatistikler hesaplanmalı: n, ortalama, medyan, örnek SD, min/max, P95/P99, 0.005 A altı taban grubu, 0.040 A ve üzeri sapma sayısı/dağılımı.
5. Yeni kayıt için yalnızca toplam sıçrama sayısı değil, mümkünse olayların genliği, zaman aralığı ve süreyi belirlemeye yetecek ham örnekleme kaydı tutulmalı. Home Assistant state-change CSV'si darbe süresini tek başına göstermeyebilir.
6. Önceki ve yeni kayıt farklı donanım/firmware veya ADS ayarları kullanıyorsa bu farklar açıkça belirtilmeli; ham ortalamalar doğrudan eşdeğer koşul gibi kıyaslanmamalı.
7. Yeni modülde sıçramalar belirgin azalırsa bu, eski kurulumla ilişkili bir farkı destekler; tek başına sebebi kesinleştirmez. Sıçramalar sürerse ortak çevre/tesisat, güç, toprak, kablo ve giriş devresi gibi olasılıklar sonraki kontrollü testlerle ayrıştırılır.

## Durum
- Önceki E19 yüksüz gözlem testi: istatistiksel rapor olarak kapalı.
- Sıçramaların fiziksel nedeni: AÇIK / TEŞHİS EDİLMEDİ.
- Yeni modül uzun kayıt karşılaştırması: PLANLANDI; kayıt ve analiz henüz yapılmadı.
- Bu belge dokümantasyon düzeltmesidir; firmware/YAML değişikliği veya fiziksel test yapıldığı anlamına gelmez.
