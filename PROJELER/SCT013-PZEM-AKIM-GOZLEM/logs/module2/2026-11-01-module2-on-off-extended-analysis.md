# 2026-11-01 — Modül 2/3 uzun ON/OFF olay aktarımı incelemesi

## HEDEF
Modül 3'ün SSR ON/OFF olaylarının UDP 4210 üzerinden Modül 2'ye ulaşıp ulaşmadığını, Modül 2'nin alanları HA'ya yayınlayıp yayınlamadığını ve HA History ekranındaki iki modül olaylarının tutarlılığını incelemek.

## KAYNAK
- Kullanıcı logu: `esp32d1-logs (74).txt`
- Boyut: 145.178 bayt; 1.809 satır.
- SHA-256: `e125e3d471a70abb63407d1ee9c6db82336780fbd93bc26e6f9481681e24dece`
- ESPHome 2026.10.1; Modül 2 `esp32d1`, IP `192.168.0.33`; Modül 3 kaynak IP `192.168.0.70`.
- BOOT_ID: `53A14E04372DEB0E67FA07270AC69561`.
- Ek kanıt: Kullanıcının 1 Kasım 2026 HA History ekran görüntüsü; bu görüntü dosya olarak GitHub'a eklenmedi, gözlemi bu raporda yazılı olarak korundu.

## Modül 2 cihaz logunda görülen UDP alımları
| Saat | EVENT_ID | STATE | UDP alımı | HA yayın çağrısı |
|---|---:|---|---|---|
| 19:18:07.736 | 59 | ON | Var | Var |
| 19:19:07.796 | 61 | ON | Var | Var |
| 19:19:47.706 | 62 | OFF | Var | Var |
| 19:20:47.706 | 64 | OFF | Var | Var |

Dört paketin her biri için `UDP_EVENT_RECEIVED` ve `HA_EVENT_PUBLISHED` logları bulunuyor. Kaynak BOOT_ID dört olayda da aynı.

## Olay dizisi ve kayıp sınırı
Log zaman aralığında olay numaraları 59, 61, 62 ve 64 olarak görüldü. 60 ve 63 numaralı olaylar bu Modül 2 logunda görünmüyor. Bu nedenle:
- Modül 2 logu, 59–64 aralığındaki tüm olayların eksiksiz alındığını göstermiyor.
- 60 ve 63'ün Modül 3'te üretilmediği mi, UDP'de kaybolduğu mu, yoksa Modül 2 logunda başka nedenle görünmediği mi bu dosyadan belirlenemez.
- 61 ON → 62 OFF arası yaklaşık 40 s; 62 OFF → 64 OFF arası 60 s. Eksik 63 numarası, beklenen 20 s sonraki ON geçişiyle uyumlu bir boşluk oluşturuyor; ancak 63'ün durumu bu logla kanıtlanmış değildir.

## Home Assistant History ekran görüntüsü
Ekran görüntüsünde:
- 19:23:07'de Modül 2 EVENT_ID 69 görülüyor; STATE ve ham paket satırı ekran kesitinde görünmüyor.
- 19:23:47'de Modül 2 STATE OFF, EVENT_ID 70 ve ham OFF olayı; Modül 3 ham OFF olayı; SSR entity durumu Kapalı görülüyor.
- 19:24:07'de Modül 2 STATE ON, EVENT_ID 71 ve ham ON olayı; Modül 3 ham ON olayı; SSR entity durumu Açık görülüyor.
- 70 OFF → 71 ON aralığı 20 s. 69 → 70 aralığı 40 s; 69'un STATE değeri ekranda görünmediğinden ON olarak kesin kaydedilmedi.

Bu ekran görüntüsü, en azından 70 OFF ve 71 ON olaylarının iki modülün HA geçmişinde göründüğünü destekler. Modül 2'nin 59–64 logundaki eksik 60/63 olaylarını geriye dönük olarak açıklamaz; ayrı zaman kesitidir.

## Modül 2 SCT ve çalışma durumu
- Log boyunca üç SCT kanalı sıralı okunuyor; 200 ms ct_clamp pencereleri ve yaklaşık 2 s çevrim sürüyor.
- Bu kayıt için yük koşulu ve PZEM eşzamanlı karşılaştırma değeri tanımlanmadığından SCT akım doğruluğu veya kalibrasyon sonucu çıkarılmadı.
- Bir adet 70 ms safe_mode operation uyarısı var; tekil uyarı olarak takip notu. Bu kesitte ERROR, UDP_RECV_FAILED, UDP_INVALID_PACKET veya UDP_BIND_FAILED satırı görülmedi.
- Başlangıçta validated config cache kullanıldığı yazıyor; bu, o açılışta config validation'ın atlandığı anlamına gelir.

## SONUÇ
- **DOĞRULANDI:** Modül 2, aynı BOOT_ID altında 59 ON, 61 ON, 62 OFF ve 64 OFF olaylarını UDP ile aldı ve HA yayın çağrısı yaptı.
- **HA HISTORY İLE DESTEKLENDİ:** Ayrı ekran görüntüsünde EVENT_ID 70 OFF ve 71 ON olayları Modül 2 ve Modül 3 entity'lerinde; SSR entity mantıksal durumu da Kapalı/Açık olarak görülüyor.
- **DOĞRULANMADI:** Bütün UDP olaylarının kayıpsız teslimi. 60 ve 63 bu cihaz logunda yok.
- **DOĞRULANMADI:** SSR'nin fiziksel kontak/yük anahtarlaması. HA switch durumu, ESPHome mantıksal durum/yayın bilgisidir; fiziksel yükte gerilim/akım kesilmesini tek başına kanıtlamaz.
- **DOĞRULANMADI:** Recorder veritabanının kalıcı saklama/yeniden başlatma sonrası geçmiş bütünlüğü. Ekran görüntüsü HA History görünümünü gösterir; bağımsız DB denetimi değildir.
- **DOĞRULANMADI:** Python paketleme/eşleştirme hattı; bu aşamada yalnız ESP/HA olay aktarımı gözlendi.

## KOD / DEPO SINIRI
Bu log çalışan Modül 2 binary'sindeki UDP alımını doğrular; ancak başlangıçta config cache doğrulaması atlandığı ve kaynak YAML ile binary'nin byte-byte eşitliği gösterilmediği için depodaki YAML için bağımsız config check/derleme/OTA kanıtı sayılmaz. Modül 3 kaynak YAML'ı da test loguyla birebir eşit kabul edilmemelidir.

## SONRAKİ TEKNİK KAPI
Yeni kod değişikliği yapmadan önce 60 ve 63 gibi eksik olayları Modül 3 gönderim logu ile aynı BOOT_ID/EVENT_ID üzerinden karşılaştır. Gerekirse Modül 2 alıcı döngüsü/HA publish gecikmesi ve Wi-Fi/UDP kayıp olasılığı ayrı incelensin. Mevcut kanıt, tüm olaylar kayıpsızdır demek için yeterli değildir.
