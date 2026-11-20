# Modül 1 – Şebeke Karakterini Koruyan Bias – Tarihçe

Bu dosya modülün görevleri boyunca edinilen tecrübeyi ve gelişim sürecini kronolojik olarak kaydeder.

## Kayıt standardı

Her kayıt aşağıdaki bilgileri içermelidir:

- **Tarih:**
- **Görev kimliği:**
- **Çalışma / deneme:**
- **Gözlenen sonuç:**
- **Edinilen tecrübe:**
- **Teknik karar:**
- **İlgili kayıtlar:** YAML sürümü, LOG ve RAPOR yolları

Başarısız, sonuçsuz veya henüz doğrulanmamış çalışmalar da kaydedilir. Sonuçlar olduğundan başarılı veya doğrulanmış gösterilmez. **Tarihçe, test loglarının veya raporların kopyası değildir.** Log ve raporların ne gösterdiğini, bunlardan ne öğrenildiğini ve hangi teknik sonuca/karara ulaşıldığını özetler. Ham loglar ve ayrıntılı raporlar kendi sürüm klasörlerinde korunur; tarihçe ilgili kayıtlara referans verir.

---

## Kronolojik kayıtlar

### 2026-11-20 – Modülün amacı ve bias standardının ayrıştırılması

- **Görev kimliği:** Henüz atanmadı.
- **Çalışma / deneme:** Modülün adı ve teknik kapsamı belirlendi. Kullanıcı; RN130421 6 V / 2.0 VA PCB tipi trafo, KBU610 (kullanıcı yazımı KBU610VETH), 2200 / 35 V kondansatör, L78L33 TO-92 regülatör ve breadboard kurulumunu mevcut parçalar olarak bildirdi. ESP üzerinden bias üretme yaklaşımının da bulunduğunu belirtti.
- **Gözlenen sonuç:** Bu oturumda devre bağlantısı veya elektriksel davranış testi yapılmadı. Parça adetleri, tam model işaretlemeleri, direnç/kondansatör değerleri ve bağlantılar henüz doğrulanmadı.
- **Edinilen tecrübe:** 1,65 V seviyesini elde etme yöntemi, bias devresinin yapısal tanımıyla aynı şey değildir; ayrı bir ara süreç olarak açıklanmalıdır. ESP beslemesinden üretilen bias, şebeke sinyalinin karakterini taşıyan yaklaşım değildir ve ayrı karşılaştırma yöntemi olarak ele alınmalıdır.
- **Teknik karar:** Modülün adı **“Modül 1 – Şebeke Karakterini Koruyan Bias”** olarak onaylandı. Bias devresinin standart tanımı, gerçek devrede kullanılan direnç ve kondansatörlerin değerleri, toleransları ve bağlantı biçimi üzerinden yapılacak. 1,65 V elde etme adımı bu standarttan ayrı belgelenerek anlatılacak. “Şebeke karakterini koruma” şimdilik tasarım hedefidir; doğrulanmış test sonucu değildir. Galvanik izolasyon ayrıca incelenecek.
- **İlgili kayıtlar:** `PREBERO/MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md`; görev, YAML, LOG ve RAPOR henüz oluşturulmadı.


### 2026-11-20 – Genel bias orta nokta yapısının ölçülmesi

- **Görev kimliği:** Henüz atanmadı.
- **Çalışma / deneme:** Breadboard üzerindeki iki dirençli bias orta nokta yapısı incelendi. İki direnç devreden ayrılarak ayrı ayrı ölçüldü. Kullanıcı, bias çıkışını iki direncin birleşim noktasından aldığını belirtti.
- **Gözlenen sonuç:** Birinci direnç 9,82 kΩ, ikinci direnç 9,82 kΩ ölçüldü. Kaynak/trafo çıkışı 3,31 V; dirençlerin orta noktasındaki bias 1,65 V olarak bildirildi. İki eşit dirençli bölücü için beklenen teorik orta nokta 1,655 V'tur; bildirilen 1,65 V ölçümle uyumludur.
- **Edinilen tecrübe:** Bias orta nokta yapısı Modül 1'in trafosuna özgü değildir. İki eşit direnç, uygun bir DC kaynağın yaklaşık yarı gerilimini orta noktada üretir. Kaynak gerilimi değişirse orta nokta gerilimi de değişir; 1,65 V sabit ve kaynaktan bağımsız bir çıktı değildir.
- **Teknik karar:** Bu yapı PREBERO README içinde genel bias orta nokta standardı olarak tanımlanacaktır. Modül 1 imalat dosyasında ise mevcut kurulumun ölçülmüş örneği olarak tutulacaktır. İki direnç 9,82 kΩ ölçülmüş değerleriyle kaydedildi; 10 kΩ nominal sınıfıyla uyumlu kabul edildi. 104 seramik kondansatör 100 nF olarak kaydedildi. Elektrolitik kondansatörün “10 50V” işaretlemesinin tam kapasite değeri ve kondansatörlerin bağlantı biçimleri henüz doğrulanmadı. Devrenin şebeke karakterini koruduğu veya galvanik izolasyon sağladığı bu ölçümlerle kanıtlanmış değildir.
- **İlgili kayıtlar:** `PREBERO/README.md`; `PREBERO/MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md`; 2026-11-20 oturum fotoğrafları ve kullanıcı tarafından bildirilen multimetre ölçümleri. Ayrı görev/YAML/LOG/RAPOR henüz oluşturulmadı.
