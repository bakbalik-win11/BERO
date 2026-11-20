# Modül 1 – Şebeke Karakterini Koruyan Bias – İmalat Dosyası

> **Kayıt durumu: ŞABLON / FİZİKSEL İMALAT BİLGİLERİ HENÜZ DOLDURULMADI**
>
> Bu dosya, modülün fiziksel kurulumu gerçek donanım üzerinde incelenip doğrulandıkça doldurulur. Aşağıdaki başlıklar bir kontrol listesidir; boş alanlar hakkında tahmin yürütülmez.

## 1. Modülün amacı ve kapsamı

- **İmalat amacı:** Şebeke karakterini SCT013 akım trafosunun ölçüm sinyaline yansıtacak bias yapısını oluşturmak. Amaç, SCT013'ten gelen şebeke ile ilişkili AC sinyalin karakterinin bias uygulaması sonrasında korunup korunmadığını deneysel olarak incelemektir. Bu, tasarım hedefidir; henüz doğrulanmış sonuç değildir.
- **Ana yaklaşım:** Modül 1'in imal amacı, şebeke karakterini SCT013 akım trafosunun sinyaline yansıtmaktır. Bias yapısının SCT013 sinyaline etkisi ve sinyal karakterini koruyup korumadığı deneyle incelenecektir. Bu aşamada hedef tanımlanmıştır; sonuç henüz doğrulanmamıştır.
- **Karşılaştırma yaklaşımı:** ESP'nin 3,3 V beslemesinden oluşturulan bias ayrı bir yöntemdir. Bu yöntem şebeke sinyalini taşımaz; ADC için DC çalışma noktası/referansı oluşturur.
- **1,65 V seviyesi:** Bias yapısının tanımı değildir. 1,65 V seviyesinin hangi ara işlemle elde edildiği, devrenin bileşen standardından ayrı bir uygulama süreci olarak açıklanacaktır.
- **Bias yapısı standardı:** Gerçek devrede kullanılan dirençler ve kondansatör(ler), değerleri, toleransları ve bağlantı biçimleri doğrulandıktan sonra yeniden kurulabilir bir standart olarak tanımlanacaktır.
- **Fiziksel kapsam:** Kullanıcı breadboard üzerinde kurulduğunu bildirdi; gerçek yerleşim ve bağlantılar henüz kaydedilmedi.
- **ESP kullanımı:** ESP kaynaklı bias karşılaştırma yaklaşımıdır. ESP'nin modüle kalıcı atanması henüz belirlenmedi.

## 2. Donanım ve malzeme listesi

| Sıra | Parça / model | Adet | Görevi | Kayıt / doğrulama |
|---|---|---:|---|---|
| 1 | RN130421, 6 V / 2.0 VA PCB tipi trafo | Belirtilmedi | Modülde bulunduğu kullanıcı tarafından bildirildi; devredeki görevi/bağlantısı doğrulanmadı | [Ürün sayfası](https://www.motorobit.com/rn130421-6v-20va-pcb-tipi-trafo-transformator) |
| 2 | KBU610 / kullanıcı yazımı: KBU610VETH | Belirtilmedi | Köprü doğrultucu olduğu bildirildi; tam model ve bağlantı doğrulanmadı | Kullanıcı bildirimi |
| 3 | 2200 / 35 V kondansatör | Belirtilmedi | Kapasite birimi µF olarak anlaşılmıştır; üzerindeki işaretleme doğrulanmalı | Kullanıcı bildirimi |
| 4 | L78L33, TO-92 | Belirtilmedi | 3,3 V regülatör; devredeki kullanım ve bağlantı doğrulanmadı | Kullanıcı bildirimi |
| 5 | İki adet direnç | 2 | Genel bias orta nokta yapısında seri gerilim bölücü | Her iki direnç devreden ayrılarak 9,82 kΩ ölçüldü; nominal 10 kΩ sınıfıyla uyumlu |
| 6 | Seramik kondansatör, işaretleme: 104 | 1 | Bias devresinde kullanılıyor; kesin bağlantı işlevi henüz doğrulanmadı | 104 kodu 100 nF (0,1 µF) anlamına gelir |
| 7 | Elektrolitik kondansatör, kullanıcı bildirimi: “10 50V” | 1 | Bias devresinde kullanılıyor; kesin bağlantı işlevi henüz doğrulanmadı | 10 µF / 50 V olduğu henüz teyit edilmedi |
| 8 | Breadboard | Belirtilmedi | Kurulumun breadboard üzerinde yapıldığı bildirildi | Kullanıcı bildirimi |
| 9 | ESP | Belirtilmedi | ESP kaynaklı bias karşılaştırmasında kullanılıyor; model/pin/bağlantı kaydedilmedi | Kullanıcı bildirimi |


Ortak donanım ve envanter kayıtları ana depodaki `DONANIM/` ve `ENVANTER/` altında tutulur; burada yalnızca bu modülde fiilen kullanılan parçalar ve ilgili envanter referansları belirtilir.

## 3. Elektriksel bağlantılar

- **Bağlantı şeması:** Henüz eklenmedi. Breadboard fotoğrafları dirençlerin orta nokta düzenini gösteriyor; delik/satır bazında kesin bağlantı şeması henüz çıkarılmadı.
- **Trafo sekonderi, doğrultucu, filtre ve L78L33 bağlantıları:** Henüz doğrulanmadı.
- **Genel bias orta nokta yapısı:** İki eşit direnç seri gerilim bölücü olarak kullanılır; bias çıkışı iki direncin birleşim noktasından alınır. Yapı belirli bir trafoya özgü değildir ve uygun DC kaynakla uygulanabilir. İdeal/yüksüz durumda orta nokta kaynak geriliminin yaklaşık yarısıdır; kaynak gerilimi değişirse bias gerilimi de değişir.
- **Bu modülde ölçülen dirençler:** Her iki direnç devreden ayrılarak 9,82 kΩ ölçüldü. İki ölçüm de aynı değerdedir; 10 kΩ nominal sınıfıyla uyumludur.
- **Bu modülde gözlenen bağlantı ve gerilimler:** Modül 1 çıkışı (3,31 V), genel bias orta nokta yapısının girişine bağlandı. Genel bias devresindeki iki eşit dirençli bölücünün birleşim noktasından 1,65 V bias alındı. Yani Modül 1, 3,31 V kaynağı sağlar; 1,65 V orta nokta ise Modül 1'in kendi başına sabit çıkışı değil, ona bağlanan genel bias yapısının sonucudur.
- **Kondansatörler:** 104 işaretli seramik kondansatör (100 nF / 0,1 µF) ve üzerinde “10 50V” olarak bildirilen elektrolitik kondansatör devrede bulunuyor. Elektrolitik kondansatörün 10 µF olduğu henüz teyit edilmedi. Her iki kondansatörün kesin bağlantı noktaları ve işlevleri şemayla doğrulanmadı.
- **Önemli sınır:** 1,65 V değeri, 3,3 V civarındaki bir kaynağın iki eşit dirençle bölünmesinden elde edilir. Bu orta nokta yapısı kaynaktan/trafo modelinden bağımsız bir genel yöntemdir; ancak çıkış gerilimi kaynak geriliminin yarısına bağlıdır.
- **ESP bias bağlantısı:** ESP modeli, çıkış pini, direnç ağı ve ortak referans henüz kaydedilmedi.
- **Besleme gerilimi ve akım gereksinimi:** Henüz doğrulanmadı.
- **GND / ortak referans:** Henüz doğrulanmadı.
- **İzolasyon ve koruma:** Henüz doğrulanmadı. Trafo kullanılması tek başına tüm devrenin galvanik izolasyonunu kanıtlamaz; izolasyon, sinyal karakterinin korunmasından ayrı değerlendirilir.

### Bağlantı tablosu

| Kaynak / pin | Hedef / pin | Sinyal veya işlev | Kablo bilgisi | Doğrulama |
|---|---|---|---|---|
| Henüz kaydedilmedi | Henüz kaydedilmedi | — | — | — |

## 4. Fiziksel yerleşim ve montaj

- **Kartların ve bileşenlerin yerleşimi:** Henüz kaydedilmedi.
- **Kutu / montaj biçimi:** Henüz kaydedilmedi.
- **Kablo güzergâhı ve sabitleme:** Henüz kaydedilmedi.
- **Sökme / yeniden kurma notları:** Henüz kaydedilmedi.

## 5. ESP ve yazılım eşleştirmesi

- **Fiziksel ESP envanter kimliği:** Atanmadı / doğrulanmadı.
- **Sabit ESPHome cihaz adı:** Atanmadı / doğrulanmadı.
- **İlgili görev ve kod sürümü:** İlgili görev kayıtlarından eklenecek.
- **Not:** Fiziksel ESP kimliği, görev kimliği ve kod sürümü birbirinden bağımsızdır.

## 6. Fotoğraflar ve şemalar

Gerçek montaj ve bağlantı fotoğrafları `FOTOGRAFLAR/`, çizimler ve şemalar `SEMALAR/` altında saklanır. Dosyalar burada açıklayıcı adları ve revizyon/tarih bilgileriyle referanslanır.

| Dosya | Açıklama | Revizyon / tarih | Durum |
|---|---|---|---|
| Henüz eklenmedi | — | — | — |

## 7. Montaj ve devreye alma sırası

1. Malzeme ve fiziksel ESP kimliğini envanterden doğrula.
2. Bağlantı şemasını ve parça modellerini kontrol et.
3. Enerjisiz durumda kablolamayı yap.
4. Besleme, polarite, ortak referans ve izolasyon kontrollerini gerçekleştir.
5. İlgili görevde kayıtlı kod sürümünü ve cihaz eşleştirmesini doğrula.
6. İlk enerjilendirme ve işlev testini ilgili görev test prosedürüne göre yap.
7. Sonuçları ilgili sürümün LOG/RAPOR klasörüne kaydet; imalat dosyasındaki gerçekleşmiş yapıyı güncelle.

## 8. Güvenlik ve sınırlamalar

Henüz modüle özgü doğrulanmış güvenlik bilgisi kaydedilmedi. Şebeke gerilimi veya tehlikeli enerji içeren bağlantılar için uygun izolasyon, koruma ve enerjisiz çalışma prosedürü belirlenmeden montaj yapılmaz.

## 9. İmalat revizyon kayıtları

| Tarih | Değişiklik | Gerekçe | İlgili görev / kanıt |
|---|---|---|---|
| 2026-11-20 | Modül adı ve amacı “Şebeke Karakterini Koruyan Bias” olarak tanımlandı; 1,65 V üretiminin ayrı ara süreç olduğu kaydedildi | Bias yapısı ile 1,65 V elde etme yöntemini ayırmak | PREBERO karar kaydı |
| 2026-11-20 | Trafo, doğrultucu, kondansatör, regülatör, breadboard ve ESP bias karşılaştırması ön envantere işlendi | Kullanıcı tarafından bildirilen mevcut parçaları kaybetmemek | Fiziksel inceleme bekliyor |
| 2026-11-20 | Genel bias orta nokta yapısı iki eşit dirençli gerilim bölücü olarak kaydedildi. İki direnç ayrı ayrı 9,82 kΩ ölçüldü; 3,31 V kaynakta orta nokta 1,65 V gözlendi | Bias yapısının Modül 1 trafosundan bağımsız genel yöntem olduğunun ayrıştırılması | Kullanıcı ölçümleri ve breadboard fotoğrafları; kondansatör bağlantıları henüz doğrulanmadı |

## 10. Yeniden kurulum kontrolü

- [ ] Parça modelleri ve adetleri doğrulandı.
- [ ] Fiziksel ESP envanter kimliği doğrulandı.
- [ ] Bağlantı şeması gerçek montajla eşleşiyor.
- [ ] Kablolar ve pin eşleşmeleri kontrol edildi.
- [ ] Besleme ve güvenlik kontrolleri yapıldı.
- [ ] İlgili kod sürümü ve test durumu kontrol edildi.
- [ ] İlk çalıştırma logu ve sonuç raporu kaydedildi.
- [ ] Fotoğraf ve şemalar güncel.

**Not:** Bu kontrol listesi tamamlanmadan modülün yeniden imalatı veya doğrulanmış devreye alımı tamamlandı kabul edilmez.
