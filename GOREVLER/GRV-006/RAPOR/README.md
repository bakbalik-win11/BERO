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
