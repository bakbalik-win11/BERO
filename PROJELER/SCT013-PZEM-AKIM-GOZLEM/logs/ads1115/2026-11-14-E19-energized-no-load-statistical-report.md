# 2026-11-14 — E19 ADS1115 enerjili-yüksüz hat gözlemi: istatistiksel sonuç ve kapanış

## Durum
**KAPATILDI — CSV incelendi, istatistiksel rapor ve olay örnekleri kaydedildi.**

Bu kapanış yalnızca 13–14 Kasım gecesi yapılan **hat enerjili / ölçülen iletkende yük bulunmayan ADS1115 gözlem oturumuna** aittir. Ayrı planlanan enerjisiz hat taban testi bu kayıtla yapılmış veya kapatılmış sayılmaz.

## HEDEF
ESP32D2 + ADS1115 + SCT ölçüm zincirinin, hat enerjiliyken ölçülen iletkende yük/akım yok koşulundaki uzun dönem davranışını incelemek; normal taban dağılımını, yüksek sapmaları ve mevcut PZEM/SSR durum kayıtlarıyla zamansal ilişkisini belirlemek.

## KAYNAK VERİ VE BÜTÜNLÜK
- Kullanıcı dosyası: `uzun 1115 boşta .csv`
- Boyut: **1,414,838 bayt**
- SHA-256: `3494db19c69a54b6488389b9cac89bd970a9b37ca72c2ad61a4d5ddbebc31202`
- CSV toplamı: **16,260 satır**, 3 sütun: `entity_id`, `state`, `last_changed`.
- Zaman damgaları CSV'de UTC (`Z`) biçiminde; bu raporda Türkiye yerel saati **UTC+03:00** olarak gösterilir.
- Genel dosya aralığı: **2026-11-13 22:00:00 – 2026-11-14 08:34:30 (+03:00)**.
- ADS1115 akım entity'si: `sensor.esp32d2_bero_akim_sensoru`.
- Akım entity aralığı: **2026-11-13 22:00:00 – 2026-11-14 08:31:39.713 (+03:00)**; geçen süre **10 saat 31 dakika 39.713 saniye**.
- Akım entity'si: 1,679 state satırı; **1,669 sayısal**, **10 unavailable**. Sayısal kayıtlar 1,379 farklı değer içerir.
- Kaynak CSV bu raporla birlikte Git'e ham dosya olarak eklenmedi. Kaynak dosyanın kimliği/bütünlüğü SHA-256 ile sabitlendi; analizde kullanılan 0.005 A üzerindeki 77 olay satırı ayrı CSV olarak kaydedildi. Bu olay dökümü ham CSV'nin yerine geçmez.

## TEST KOŞULU VE BAĞLAM
- Önceki cihaz/OTA kaydında ESP32D2, ESPHome 2026.10.2, ADS1115 I²C 0x48, A0–A1 diferansiyel giriş, gain 2.048, 860 SPS, continuous mode, 200 ms ct_clamp penceresi, 1 s yayın ve K=27.60 kaydedilmişti. Bu uzun CSV'nin her satırında firmware/binary kimliği bulunmadığından, bu ayarların CSV boyunca kesintisiz aynı kaldığı yalnız CSV ile bağımsız doğrulanamaz.
- Kullanıcı test koşulunu hat enerjili, ölçülen iletkende yük/akım yok olarak bildirdi.
- PZEM akım entity'sinde yalnızca 3 state vardır: başlangıçta 0.0 A, 2026-11-14 00:53:19.139 (+03:00) anında unavailable, 00:53:19.333 (+03:00) anında yeniden 0.0 A. Bu nedenle PZEM'in tüm 10.5 saat boyunca kesintisiz sıfır ölçtüğü söylenemez.
- SSR kontrol entity'sinde 633 `on`, 633 `off` ve 1 `unavailable` state kaydı vardır. Bunlar Home Assistant switch entity durumlarıdır; fiziksel SSR kontaklarının veya yük akımının doğrudan kanıtı değildir.
- PZEM gerilim entity'sinde 5,508 sayısal kayıt: ortalama 231.970 V, SD 1.919 V, min 223.1 V, max 234.6 V.
- PZEM frekans entity'sinde 849 sayısal kayıt: ortalama 49.9501 Hz, min 49.9 Hz, max 50.0 Hz.

## ADS1115 AKIM İSTATİSTİKLERİ

### Tüm sayısal kayıtlar
| İstatistik | Sonuç |
|---|---:|
| n | 1,669 |
| Ortalama | 0.003427 A |
| Medyan | 0.0012877 A |
| Standart sapma (örnek SD) | 0.012668 A |
| Minimum | 0.000000 A |
| P95 | 0.0015657 A |
| P97.5 | 0.0463483 A |
| P99 | 0.0483364 A |
| Maksimum | 0.3530546 A |

Tüm veri ortalaması ve standart sapması, yüksek sapma grubundan güçlü biçimde etkilenmektedir. Bu nedenle normal tabanı temsil etmek için tüm kayıtların ortalaması tek başına kullanılmamalıdır.

### 0.005 A ve altındaki taban grubu
Bu eşik yalnızca **istatistiksel gruplama** içindir; firmware'e eşik veya filtre eklenmesi anlamına gelmez.

| İstatistik | Sonuç |
|---|---:|
| Kayıt sayısı | 1,592 (%95.39) |
| Ortalama | 0.00122955 A |
| Medyan | 0.00128425 A |
| Standart sapma (örnek SD) | 0.00028426 A |
| Minimum | 0.000000 A |
| Maksimum | 0.00168470 A |
| CV (SD/ortalama) | %23.12 |
| Tam sıfır kayıt | 76 |

Taban grubundaki CV, ortalamanın çok küçük olması ve 76 adet tam sıfır kaydı nedeniyle göreli olarak büyüktür. Mutlak standart sapma **0.000284 A (0.284 mA)** düzeyindedir. Taban değerleri yaklaşık 1.2–1.3 mA çevresinde yoğunlaşmıştır.

### Yüksek değer / sapma grubu
| Aralık | Kayıt |
|---|---:|
| 0.005–0.010 A | 3 |
| 0.010–0.040 A | 2 |
| 0.040–0.060 A | 70 |
| 0.060–0.100 A | 1 |
| 0.100 A üzeri | 1 |
| **0.040 A ve üzeri toplam** | **72 (%4.31)** |

- 0.040 A ve üzerindeki 72 kaydın medyanı **0.046599 A**; ortalaması **0.051456 A**.
- Tekil yüksek örneklerden biri **0.072691 A** (2026-11-14 05:09:00.594 +03:00).
- En yüksek örnek **0.353055 A** (2026-11-14 06:03:45.924 +03:00). Bu değer, 0.040 A üzerindeki grubun medyanının yaklaşık 7.58 katıdır.
- 0.353055 A değeri dağılımın geri kalanından belirgin biçimde ayrılır; tek örnekten kalıcı akım, gerçek yük veya sensör arızası sonucu çıkarılamaz.

## SSR DURUM GEÇİŞLERİYLE ZAMANSAL KARŞILAŞTIRMA
Yüksek sapma grubu olarak tanımlanan 0.040 A ve üzerindeki 72 örnek, HA switch entity'sinin en yakın `on/off` state değişimiyle karşılaştırıldı:

| En yakın switch state değişimine uzaklık | Örnek sayısı |
|---|---:|
| 1 saniye veya daha az | 20 / 72 (%27.78) |
| 5 saniye veya daha az | 35 / 72 (%48.61) |
| 10 saniye veya daha az | 57 / 72 (%79.17) |

Bu sonuç zamansal yakınlık gösterir. SSR state değişimleri düzenli ve tekrarlıdır; dolayısıyla bu karşılaştırma tek başına nedensellik kanıtı değildir. Ayrıca HA switch entity durumu fiziksel kontak hareketini doğrulamaz. Bulguyu **SSR kontrol geçişleriyle ilişkili olabilecek sapmalar — hipotez** olarak kaydediyoruz. Olası elektriksel kuplaj, ortak besleme/toprak etkisi, giriş devresi davranışı veya başka bir etken bu CSV ile birbirinden ayrılamaz.

## ZAMAN SERİSİ / KAYIT KALİTESİ
- Ardışık akım state timestamp farklarının medyanı **1.000 s**; 10 saniyeyi aşmayan pozitif aralıkların %95 persentili **1.078 s**.
- Bununla birlikte 10 saniyeden uzun kayıt aralıkları ve 10 adet `unavailable` durumu vardır; en uzun iki ardışık sayısal state aralığı 1,936 s ve 1,850 s düzeyindedir.
- Home Assistant CSV'si yalnız state değişimlerini taşıyor olabilir; aynı değerin tekrar yayımlandığı fakat state değişmediği aralıklar bu dışa aktarımda görünmeyebilir. Bu nedenle bu satır sayısı kesintisiz 1 Hz örnek sayısı olarak yorumlanmamalıdır.
- Yüksek değerlerin gerçek darbe genişliği, süresi veya her darbenin kaç saniye sürdüğü bu CSV'den belirlenemez.

## SONUÇ
1. **ÖLÇÜLDÜ / CSV İLE DESTEKLENDİ:** Sayısal ADS1115 kayıtlarının %95.39'u 0.005 A veya altındadır. Bu grubun ortalaması 0.001230 A, medyanı 0.001284 A ve örnek SD'si 0.000284 A'dır.
2. **ÖLÇÜLDÜ / CSV İLE DESTEKLENDİ:** 0.040 A ve üzerindeki 72 örnek, taban grubundan açıkça ayrılan ikinci bir değer kümesi oluşturur. En yüksek örnek 0.353055 A'dır.
3. **ÖLÇÜLDÜ / CSV İLE DESTEKLENDİ:** 0.040 A üzerindeki örneklerin 57/72'si en yakın HA switch state geçişinden 10 saniye içinde görülmüştür. Bu, geçişlerle zamansal yakınlıktır; sebep kanıtı değildir.
4. **SINIR:** PZEM akım entity'si uzun kayıt boyunca yalnızca üç state içerir. PZEM'in tüm süre boyunca 0.000 A gösterdiği iddiası CSV ile doğrulanamaz; yalnızca mevcut iki sayısal state 0.0 A'dır.
5. **SINIR:** CSV, sıçramaların fiziksel kaynağını, analog girişteki gerçek gerilimi veya ADS1115'in güvenli ortak-mod aralığında kaldığını kanıtlamaz.
6. **KOD KARARI KORUNDU:** Alt eşik, ortalama veya spike filtresi eklenmedi. Ham ölçüm yaklaşımı değiştirilmedi; bu rapor firmware değişikliği değildir.

## TEST KAPANIŞI
- **Durum:** KAPATILDI — enerjili hat / yüksüz iletken uzun süreli gözlemi analiz edildi.
- **Kapanış gerekçesi:** İstenen uzun dönem CSV istatistikleri çıkarıldı; taban dağılımı, sapma sayısı/büyüklüğü ve SSR state geçişlerine zamansal yakınlık kaydedildi.
- **Açık kalan teknik konu:** Sapmaların fiziksel nedeni teşhis edilmedi.
- **Ayrı test:** Enerjisiz hat taban gözlemi bu testin kapsamında değildir; yapılmış sayılmaz.
- **Güvenlik kapısı:** ADS1115 A0/A1 ortak-mod ve GND–VDD giriş sınırlarının fiziksel doğrulaması hâlâ açık. Bu rapor enerjili test için güvenlik onayı değildir; doğrulama olmadan yeni enerjili test başlatılmamalıdır.

## İLGİLİ KAYITLAR
- [Önceki OTA / 1 s log raporu](2026-11-13-E19-energized-no-load-1s-raw-log-report.md)
- [Bu analizdeki 0.005 A üzeri olay örnekleri](2026-11-14-E19-energized-no-load-event-samples.csv)
- [Özet istatistik CSV](2026-11-14-E19-energized-no-load-statistics.csv)
