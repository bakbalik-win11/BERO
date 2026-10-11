# GRV-006 — Veri Al, Python ile İşle, ESP'ye Geri Gönder ve Teyit Et

**Durum:** Açık — hedef ve kabul ölçütleri netleştirildi; uçtan uca uygulama henüz kanıtlanmadı.  
**Açılış tarihi:** 2026-10-11  
**Kapsam düzeltmesi:** 2026-10-11  
**Öncelik:** Gerçek veri dosyasıyla görünür sonuç üretmek. Rapor, QC veya öz-test üretmek bu görevin teknik ilerlemesi sayılmaz.

## 1. Tek cümlelik hedef

**Veriyi al → dosyaya yaz → aynı dosyayı yeniden oku → Python ile işle → sonucu bağımsız doğrula → işlenmiş sonucu ESP'ye geri gönder → ESP'den geri okuyup teyit et.**

Bu görev, kullanıcının doğrudan ifade ettiği hedefi esas alır. GRV-005 geçmişini ve kayıtlarını değiştirmez. SCT/akım ölçümünün elektriksel doğruluğu bu veri alışverişi görevinin ilk kabul ölçütü değildir.

## 2. En küçük uygulanabilir akış

### Aşama 1 — Veriyi al ve dosyaya yaz
- Mevcut kayıtlarda bulunan gerçek ve kullanılabilir veri kaynağını önce incele.
- Veri kaynağı bu ilk prova için uygun değilse küçük, deterministik bir örnek veri kümesi kullanılabilir; bunun sentetik olduğu açıkça yazılır.
- Veriyi gerçek bir dosyaya yaz.
- Dosyanın varlığını, boyutunu ve içeriğini kontrol et.

**Kabul kanıtı:** Üretilmiş dosya ve dosyadan okunmuş gerçek içerik.

### Aşama 2 — Aynı dosyayı yeniden oku
- Aynı dosyayı yeniden aç; bellekteki ilk değişkeni tekrar göstermekle yetinme.
- Kayıt sayısını, alanları ve değerleri doğrula.
- Beklenen değerlerle okunan değerleri karşılaştır.

**Kabul kanıtı:** Dosyadan tekrar okunmuş veri ve açık eşleşme sonucu.

### Aşama 3 — Python ile işle
- Okunan veriye tek ve açıkça tanımlanmış bir işlem uygula.
- Ham dosyayı koru; işlenmiş sonucu ayrı bir dosyaya veya açık çıktıya yaz.
- İşlenmiş sonucu da yeniden oku.

**Kabul kanıtı:** Kaynak ve işlenmiş çıktı ayrı ayrı mevcut; işlem sonucu dosyadan yeniden okunabiliyor.

### Aşama 4 — Bağımsız doğrulama
- En az bir beklenen sonucu ana işleme fonksiyonundan bağımsız bir hesapla doğrula.
- Örneğin küçük veri kümesinde toplam, ortalama veya bilinen dönüşüm sonucu elle kontrol edilebilir.
- Yalnızca aynı kodun kendi PASS mesajını bağımsız doğrulama sayma.

**Kabul kanıtı:** Beklenen değer, Python sonucu ve bağımsız kontrol yan yana gösterilmiş; eşleşme veya fark açıkça kaydedilmiş.

### Aşama 5 — İşlenmiş sonucu ESP'ye geri gönder ve teyit et
- Projede hâlihazırda kullanılan ESP haberleşme arayüzünü ve kodunu mevcut depodan inceleyerek belirle; yeni arayüz varsayma.
- Python'dan işlenmiş sonucu ESP'ye gönder.
- ESP'nin aldığı değeri görünür biçimde geri yayımla veya yanıtla.
- Geri okunan değeri Python'ın gönderdiği değerle karşılaştır.

**Kabul kanıtı:** Gönderilen değer, ESP'nin geri bildirdiği değer ve karşılaştırma sonucu aynı kayıtta bulunur. Haberleşme yöntemi henüz mevcut koddan belirlenemiyorsa yalnızca bu belirsizlik raporlanır; kullanıcıya rastgele yeni testler yaptırılmaz.

## 3. Sıra ve kapsam sınırları

1. Önce dosya yazma/okuma ve Python işlemesi tamamlanır; ardından ESP'ye geri gönderme aşamasına geçilir.
2. Her aşamada yalnızca bir somut sonuç hedeflenir. Aşama kanıtlanmadan yeni kontrol katmanı eklenmez.
3. İlk prova için sentetik veri kullanılabilir; bu, gerçek SCT ölçümünün doğrulandığı anlamına gelmez.
4. Mevcut gerçek log ve kodlar önce depodan incelenir. Kullanıcıdan daha önce verdiği dosya, komut veya sonuçları tekrar isteme.
5. Home Assistant, veri aktarımının mevcut ESP arayüzünü kullanmak için gerçekten gerekli olduğu kanıtlanmadıkça bu görevin zorunlu ara durağı değildir. HA üzerinden kayıt, Mac'e kopyalama, geçici kopya silme gibi işler asıl hedefi geciktirecekse bu görevden çıkarılır.
6. Paket kontrolü, QC öz-testi, ek şema veya rapor tek başına ilerleme değildir. Yalnızca gerçek veri akışındaki belirli bir hatayı teşhis etmek için gerekiyorsa kullanılır.
7. Kod veya dosya üretilmeden, gerçek çıktı okunmadan ve karşılaştırılmadan PASS denmez.
8. Geçmiş görevler, kodlar, loglar ve deneyimler silinmez veya üzerine yazılmaz.

## 4. Kabul ölçütleri

- [ ] Veri kaynağı belirlenmiş ve kaynağın gerçek mi sentetik mi olduğu açıklanmış.
- [ ] Gerçek bir veri dosyası oluşturulmuş.
- [ ] Aynı dosya yeniden açılıp içeriği doğrulanmış.
- [ ] Python işlemesi uygulanmış; ham ve işlenmiş çıktılar ayrı korunmuş.
- [ ] İşlenmiş çıktı yeniden okunmuş.
- [ ] En az bir sonuç bağımsız yöntemle doğrulanmış.
- [ ] Python'dan işlenmiş sonuç ESP'ye gönderilmiş.
- [ ] ESP'nin geri bildirdiği sonuç okunmuş ve gönderilen değerle karşılaştırılmış.
- [ ] Her kabul maddesinin kanıtı dosya/çıktı/log bağlantısıyla kaydedilmiş.

Bir madde yalnızca planlandıysa veya kod yazıldıysa işaretlenmez. Bu dosyanın güncellenmesi görev başarısı değildir.

## 5. Alt görev sırası

### GRV-006-01 — Dosya yazma, yeniden okuma ve Python işleme
Tek küçük veri kümesiyle dosyayı oluştur, aynı dosyayı tekrar aç, Python ile işle ve işlenmiş sonucu yeniden oku. Bağımsız beklenen sonucu önceden tanımla.

### GRV-006-02 — Bağımsız sonuç doğrulaması
Python sonucunu ikinci ve basit bir hesapla karşılaştır. Fark varsa yalnızca farkın kaynağını mevcut dosya ve kod üzerinden incele.

### GRV-006-03 — Python → ESP → geri okuma
Depodaki mevcut ESP arayüzünü incele; Python'dan sonucu gönder, ESP'den geri oku ve eşitliği kanıtla. Yeni haberleşme katmanı ancak mevcut seçeneklerin uygun olmadığı gösterilirse değerlendirilir.

### GRV-006-04 — Sonuç ve tek gerekli iyileştirme
İlk uçtan uca sonuçları kaydet. Yalnızca açık hata veya ölçülebilir fayda varsa bir iyileştirme yap; yoksa dur.

## 6. İlk yapılacak somut iş

**Yeni komut veya cihaz testi istemeden, depodaki mevcut dosya/kod/logları incele ve ilk aşama için kullanılabilecek en küçük veri örneğini seç.** Ardından tek bir dosyaya yazıp aynı dosyadan okuyan ve sonucu görünür biçimde karşılaştıran tam, anlaşılır bir Python örneği hazırla.

İlk kanıt; dosyanın gerçekten yazılması, aynı dosyanın yeniden açılması ve beklenen değerlerin eşleşmesidir. Bu kanıt gösterilmeden HA taşıma zinciri, yeni QC altyapısı veya ek kontrol döngüsü başlatılmaz.

## 7. GRV-006-01 — ilk gerçek dosya akışı (2026-10-11)

**Durum:** İlk basamak için yerel çalıştırma kanıtı alındı; veri açıkça sentetiktir.

- Kod: [GRV-006-01 Python](../KOD/GRV-006-01-file-roundtrip-v01.py)
- Kod açıklaması ve çıktı: [GRV-006-01 MD](../KOD/GRV-006-01-file-roundtrip-v01.md)
- Ham CSV: [ham veri](../KOD/GRV-006-01-ham-veri.csv)
- İşlenmiş CSV: [işlenmiş veri](../KOD/GRV-006-01-islenmis-veri.csv)
- Kanıt: dosya yazıldı; aynı dosya yeniden açıldı; üç satır okundu; her değer ikiyle çarpılarak ayrı dosyaya yazıldı; işlenmiş dosya yeniden açıldı; bağımsız beklenen toplam 120 ile okunan toplam 120 eşleşti.
- **Sonuç:** GRV-006-01'in dosya yazma/okuma ve Python işleme alt basamağı PASS.
- **Sınır:** Sentetik örnek veridir. ESP'ye veri gönderimi/geri okuma, sensör doğruluğu ve gerçek SCT verisi henüz kanıtlanmadı.
- **Sonraki tek adım:** Depodaki mevcut ESP kodu ve arayüzünü inceleyerek Python→ESP→geri okuma için mevcut ve uygun yolun ne olduğunu belirlemek; kullanıcıya rastgele yeni test yaptırmamak.

## 8. Başlangıç durumu ve geçmiş kapsam notu

Bu görev tanımı hedefe uygunluk için 2026-10-11 tarihinde netleştirilmiştir. Önceki sürümde HA'ya kaydetme, HA'dan Mac'e taşıma ve geçici kaydı silme adımları zorunlu tutulmuştu. Bunlar kullanıcının asıl hedefinin önüne geçen gereksiz ara adımlar olabileceğinden zorunlu kabul ölçütü olmaktan çıkarılmıştır. Eski karar HISTORY'de korunur; bu güncel görev tanımı onu sessizce yok saymaz, kapsamı açıkça düzeltir.

**Teknik başlangıç durumu:** Henüz uçtan uca başarı kanıtı yoktur. Dosya yazma/okuma, Python işleme, bağımsız doğrulama ve Python→ESP→geri okuma adımlarının hiçbiri bu kayıtla tamamlanmış sayılmaz.


## 9. GRV-006-03 — derleme ve cihaz API bağlantısı (2026-10-11)

**Durum:** Derleme kullanıcı tarafından doğrulandı; ESPHome API bağlantısı logda görüldü. Python → ESP → geri okuma henüz tamamlanmadı.

- Aday YAML: [GRV-006-03 v01](../KOD/GRV-006-03-v01-ADAY.yaml)
- Python istemcisi (aday): [GRV-006-03 Python API echo](../KOD/GRV-006-03-v01-python-api-echo.py)
- Kod notu: [GRV-006-03 aday MD](../KOD/GRV-006-03-v01-ADAY.md)
- Kullanıcının logu: [GRV-006-03 cihaz logu](GRV-006-03-v01-CIHAZ-LOGU-20261011.md)
- Görünen sonuç: ESPHome 2026.9.1; firmware compiled on 2026-10-11 18:19:09 +0300; ESP32 rev3.1; cihaz `esp32d1 @ 192.168.0.9`; API resolve, connect ve handshake başarılı.
- Logda görünen uyarılar: `minimum_chip_revision: "3.1"` ve `sram1_as_iram: true` önerileri. Bunlar görünen bölümde derleme hatası değil.
- Log metni kullanıcı tarafından `[18:23:17.784]` satırından sonra kesilmiş; devamı uydurulmadı.
- **Kabul edilmeyen sonuç:** Python eylem çağrısı ve echo geri okuması. `SENT`, `ECHOED` ve `RESULT: PASS` çıktıları henüz yok.
- **Sıradaki tek adım:** Python adayını, kullanılan API şifreleme ayarıyla çalıştırıp gönderilen değerin ESP'den geri okunduğunu kanıtlamak. Bu tamamlanana kadar alt görev uçtan uca PASS sayılmayacak.


## 10. GRV-006-03 — Python → ESP → Python echo PASS (2026-10-11)

**Durum:** Kullanıcının Mac mini Terminal çıktısında değer gönderme ve geri okuma eşleşti. İlk uçtan uca API echo denemesi PASS.

Kanıt:
- `CONNECTED: 192.168.0.9:6053`
- `SENT: 120`
- `ECHOED: 120.0`
- `RESULT: PASS — sent value equals ESP echo`

**Yorum:** Gönderilen tamsayı 120, ESP echo sensöründen 120.0 olarak geri okundu. Sayısal değerler eşit; gösterim biçiminin tam sayı/ondalıklı olması sonucu değiştirmiyor.

**Düzeltme notu:** İlk çalıştırma başarılı sonuçtan sonra `RuntimeWarning: coroutine 'APIClient.disconnect' was never awaited` verdi. Bu, veri eşleşmesinden ayrı bir kaynak kapatma uyarısıdır. Python istemci kodunda kapatma çağrısı `await client.disconnect()` olarak düzeltildi. Kullanıcı düzeltilmiş dosyayı yeniden çalıştırdı; aynı PASS çıktısı geldi ve bu kez RuntimeWarning görünmedi.

- Python istemcisi: [GRV-006-03 Python API echo](../KOD/GRV-006-03-v01-python-api-echo.py)
- Aday YAML: [GRV-006-03 v01](../KOD/GRV-006-03-v01-ADAY.yaml)

**Sınır:** Bu sonuç API üzerinden bir tamsayının ESP'ye gönderilip echo sensöründen geri okunmasını doğrular. SCT akım ölçüm doğruluğunu, gerçek sensör verisinin işlenmesini veya tüm GRV-006 hedefinin tamamlandığını kanıtlamaz.

**Yeniden çalıştırma sonucu (2026-10-11):** Kullanıcı düzeltilmiş dosyayı tekrar çalıştırdı ve `CONNECTED: 192.168.0.9:6053`, `SENT: 120`, `ECHOED: 120.0`, `RESULT: PASS` çıktısını aldı. `APIClient.disconnect` RuntimeWarning'i görünmedi.\n\n**GRV-006-03 alt sonucu:** Python → ESP → Python echo PASS; kapatma uyarısının düzeltildiği kullanıcı çıktısıyla doğrulandı. Bu sonuç yalnızca Native API echo yolunu doğrular; SCT ölçüm doğruluğunu veya GRV-006'nın tüm hedefinin tamamlandığını kanıtlamaz.\n\n**Sıradaki yön:** Echo deneyini sebepsiz yere tekrarlama; GRV-006'nın veri dosyası, Python işlemesi ve bağımsız doğrulama adımlarına dön.


## 11. GRV-006 — CSV işleme → ESP echo (2026-10-11)

**Durum:** Kullanıcının Mac mini Terminal çıktısında uçtan uca veri aktarımı PASS.

Kanıtlanan çıktı:
- `CSV_READ: PASS` — CSV'den 4 satır okundu.
- Kullanılan kanallar: CH0-1T=`15.038437`, CH1-2T=`9.631619`, CH2-3T=`12.415383`.
- `PROCESSED_SUM: 37.085439`.
- `SEND_INTEGER: 37085` — toplam × 1000, en yakın tamsayıya yuvarlandı.
- `INDEPENDENT_CHECK: PASS (37085)`.
- `CONNECTED: 192.168.0.9:6053`.
- `SENT: 37085`, `ECHOED: 37085.0`.
- `RESULT: PASS — CSV processed value returned by ESP`.

**Sonuç:** Bu çalıştırmada CSV dosyası okundu, üç kanalın `adc_rms_ac` değerleri Python ile toplandı, toplam 1000 ile çarpılarak tamsayıya dönüştürüldü, bağımsız yeniden okuma/hesapla kontrol edildi ve ESP'ye gönderilen değer geri okundu. Gönderilen ve dönen değer eşleşti.

**Kanıt sınırı:** CSV, daha önce kaydedilmiş GRV-005-14 v06 örnek verisidir; bu çalışma yeni bir canlı SCT ölçümü üretmez ve fiziksel akım doğruluğunu kanıtlamaz. `invalid_count` değeri `NOT_TRACKED` olduğundan geçersiz örnek sayısı bu veriden doğrulanamaz. Görev GRV-006'nın tüm kapsamı tamamlanmış sayılmaz; ancak CSV→Python işleme→bağımsız kontrol→ESP→geri okuma zinciri bu örnek için PASS.

- Python kodu: [CSV → ESP echo](../KOD/GRV-006-03-v01-python-api-echo.py) ve kullanıcıda çalıştırılan [GRV-006 CSV → ESP betiği](../KOD/GRV-006-CSV-ESP-BETIK.md) (çalıştırılan dosya depoya ayrıca kaydedilmelidir).
- Girdi: [GRV-005-14 v06 QC CSV](../../GRV-005/RAPOR/GRV-005-14-v06-QC-GIRDİSİ-20261011.csv).

**Sıradaki adım:** Çalıştırılan `grv006_csv_to_esp.py` betiğini ve bu sonuç kaydını depoya koy; ardından gerçek, yeni bir ölçüm CSV'si mevcut olduğunda aynı akışı ona uygula. Echo testini tekrar etmeye gerek yok.


## 12. Çalıştırılan betiğin depoya alınması ve sonraki adım

- Kullanıcının başarılı çalıştırdığı CSV→Python→ESP betiği yeni, ayrı dosya olarak kaydedildi: [GRV-006-04 Python](../KOD/GRV-006-04-csv-to-esp-v01.py).
- Açıklama: [GRV-006-04 MD](../KOD/GRV-006-04-csv-to-esp-v01.md).
- Önceki PASS sonucu korunur; betik depoya alındı diye yeni bir test yapılmış sayılmaz.
- **Sıradaki tek adım:** Aynı veri zincirini yeni bir canlı cihaz CSV'sinde çalıştırmak. Eski 2026-10-11 örnek CSV tekrar kullanılmayacak.


## 13. GRV-006-05 — birleşik ADC + API echo kodu derlendi (2026-10-11)

**Durum:** Kullanıcı derleme/cihaz logunu paylaştı; ADC rapor satırları gerçekten oluştu.

- Kod: [GRV-006-05 birleşik aday YAML](../KOD/GRV-006-05-v01-BIRLESTIRILMIS-ADAY.yaml)
- Kod notu: [GRV-006-05 MD](../KOD/GRV-006-05-v01-BIRLESTIRILMIS-ADAY.md)
- ESPHome: 2026.9.1
- Firmware derleme zamanı: 2026-10-11 18:49:28 +0300
- Cihaz: `esp32d1`, ESP32 rev3.1; API bağlantısı ve handshake başarılı.
- PZEM logu: yaklaşık 0.028 A, 1.5–1.8 W, PF 0.24–0.27 aralığında değişti.
- Dört ADC rapor satırı 18:54:07 civarında üretildi; her satır `sample_count=1000`, `invalid_count=NOT_TRACKED`.

Paylaşılan ADC özetleri:
- CH0-1T: mean 1863.755000, std 12.037520, min 1829, max 2097, raw RMS 1863.793834, AC RMS 12.111068.
- CH1-2T: mean 1861.695000, std 14.060500, min 1559, max 2032, raw RMS 1861.748042, AC RMS 14.469792.
- CH2-3T: mean 1855.842000, std 8.426627, min 1765, max 1905, raw RMS 1855.861112, AC RMS 12.546252.
- BIAS: mean 1865.141000, std 8.812422, min 1765, max 2023.

**Önemli sınır:** Logda CSV başlıkları ve dört satır görünmesi, ADC örnekleme/raporlama yolunun çalıştığını doğrular. Bu tek başına sensörün fiziksel akım doğruluğunu kanıtlamaz. Ayrıca paylaşılan log parçasında `grv006_set_value` çağrısı veya yeni ESP echo sonucu yok; bu nedenle birleşik kodun API echo bölümü bu logla ayrıca doğrulanmış sayılmaz. PZEM alanlarının CSV kolon hizası QC ile ayrıca kontrol edilmelidir.

**Sıradaki tek adım:** Bu dört satırı yeni ve ayrı bir GRV-006 canlı CSV dosyasına dönüştürüp Python→bağımsız kontrol→ESP echo betiğini bu yeni dosyayla çalıştırmak. Önceki tarihsel CSV korunacak.


## 14. GRV-006-05 — yeni canlı log CSV'si hazırlandı (2026-10-11)

- Ayrı CSV: [GRV-006-05 canlı CSV](GRV-006-05-LIVE-CSV-20261011.csv).
- Kaynak notu: [CSV köken ve durum notu](GRV-006-05-LIVE-CSV-20261011.md).
- Dosya, kullanıcının paylaştığı GRV-006-05 ESPHome logundan ayrıştırıldı; ESP'nin doğrudan yazdığı özgün dosya değildir.
- Python betiğinin okuması gereken alanlar doğrulandı: `channel_id` ve `adc_rms_ac`; BIAS satırının `adc_rms_ac` alanı boş bırakıldı.
- Beklenen kanal değerleri: CH0-1T=12.111068, CH1-2T=14.469792, CH2-3T=12.546252.
- Beklenen toplam=39.127112; ×1000 ve yuvarlama sonucu gönderilecek değer=39127.
- **Henüz PASS değil:** Bu yeni CSV ile Mac mini betik çıktısı ve ESP geri okuması henüz alınmadı.
- **Sıradaki tek adım:** Depo kök dizininde aşağıdaki komutu çalıştırıp çıktıyı kaydet:
  `GRV006_CSV="GOREVLER/GRV-006/RAPOR/GRV-006-05-LIVE-CSV-20261011.csv" python3 GOREVLER/GRV-006/KOD/GRV-006-04-csv-to-esp-v01.py`
- Tarihsel CSV ve önceki kodlar korunmuştur.


## 15. GRV-006-05 — yeni canlı CSV ile Python → ESP echo PASS (2026-10-11)

Kullanıcının Mac mini Terminal çıktısı:
- Yeni [canlı CSV](GRV-006-05-LIVE-CSV-20261011.csv) okundu; 4 satır bulundu.
- AC RMS: CH0-1T=12.111068, CH1-2T=14.469792, CH2-3T=12.546252.
- Toplam=39.127112; gönderilen tamsayı=39127.
- Bağımsız kontrol=PASS (39127).
- ESP 192.168.0.9:6053; SENT=39127; ECHOED=39127.0.
- Sonuç: PASS — CSV processed value returned by ESP.

Kanıt sınırı: CSV, kullanıcının paylaştığı cihaz logundan türetilmiştir; ESP'nin doğrudan yazdığı özgün dosya değildir. invalid_count=NOT_TRACKED. Bu sonuç fiziksel akım doğruluğunu veya GRV-006'nın tüm kapsamını kanıtlamaz.


## 15. GRV-006-05 — canlı log CSV → Python → ESP echo PASS (2026-10-11)

**Kullanıcı terminal kanıtı:**
- `CSV_READ: PASS` — yeni canlı logdan türetilen CSV'den 4 satır okundu.
- CH0-1T=12.111068, CH1-2T=14.469792, CH2-3T=12.546252.
- Toplam=39.127112; ölçeklenmiş/yuvarlanmış gönderim=39127.
- `INDEPENDENT_CHECK: PASS (39127)`.
- `CONNECTED: 192.168.0.9:6053`; `SENT: 39127`; `ECHOED: 39127.0`.
- `RESULT: PASS — CSV processed value returned by ESP`.

**Bu adımda kanıtlanan:** Yeni logdan ayrı CSV hazırlanması, Python'ın bu dosyayı okuması, üç kanal değerini işlemesi, dosyayı yeniden okuyarak sonucu bağımsız hesapla kontrol etmesi, ESP'ye göndermesi ve eşleşen değeri geri okuması.

**Sınırlar:** CSV, ESPHome logundan türetildi; ESP'nin kendisinin doğrudan dosyaya yazdığı özgün dosya değildir. `invalid_count=NOT_TRACKED`. Fiziksel SCT akım doğruluğu kanıtlanmadı.

**GRV-006 durumu:** Kısmi başarı; görev tamamen kapanmadı. Geriye kalan fark, ölçüm kaydının cihazdan otomatik ve özgün bir dosya olarak alınması/yazılmasıdır. Mevcut ESPHome YAML yalnızca loga CSV biçimli satırlar yazar; cihaz üzerinde dosyaya yazma özelliği yoktur. Bu nedenle bir sonraki iş, log satırlarını dosyaya kaydetme yolunu belirlemek ve dosya kökenini doğrulamaktır. Aynı Python→ESP echo testi tekrar edilmeyecek.

- Girdi: [canlı logdan türetilen CSV](GRV-006-05-LIVE-CSV-20261011.csv)
- Betik: [CSV → ESP Python](../KOD/GRV-006-04-csv-to-esp-v01.py)
- Köken notu: [CSV açıklaması](GRV-006-05-LIVE-CSV-20261011.md)
