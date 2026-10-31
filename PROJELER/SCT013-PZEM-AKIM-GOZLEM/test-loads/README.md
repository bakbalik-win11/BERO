# Test Yükleri ve Karşılaştırmalı Ölçüm Kayıtları

Bu bölüm, aynı fiziksel test yüküyle farklı ESP kartı, modül, SCT kanalı, firmware ve ölçüm yöntemi kullanılarak alınan sonuçları bir arada izlemek için açılmıştır.

## Kayıt düzeni

- Her fiziksel yük/senaryo için ayrı klasör ve ana kayıt dosyası oluşturulur.
- Her test oturumu için kullanılan firmware'in tam sürümü, kod bağlantısı ve mümkünse commit SHA'sı kaydedilir.
- Log, test tarih/saat aralığı, zaman dilimi, ilgili satırlar veya kayıt dosyası bağlantısı ile birlikte tutulur.
- Aynı yük için farklı donanım veya kodla yapılan her ölçüm ana yük tablosuna yeni satır olarak eklenir; eski satırlar değiştirilmez.
- Referans cihaz, referans değeri ve kaynak türü (log, fotoğraf, kullanıcı bildirimi) açıkça yazılır.
- Sapma yalnız eşleşen yük ve zaman pencereleri için hesaplanır. Referans değeri yoksa sapma hesaplanmaz.
- ±%4 kabulü bir test sonucu olarak işaretlenir; yalnızca gerçek ve karşılaştırılabilir referans verisi varsa değerlendirilir.
- Kod, log veya zaman aralığı mevcut değilse hücreye “mevcut değil / doğrulanmadı” yazılır; tahmin üretilmez.

## Yük kayıtları

| Yüksüz / boşta Modül 2 | [Yüksüz SCT-1 ölçüm kayıtları](idle-no-load/README.md) |

## 2026-10-31 — LOAD-IDLE-001 ilk yüksüz log

- Modül 2 / ESP32D1 / SCT-1 GPIO32 / ortak bias GPIO35; ESPHome 2026.10.1.
- 60 akım yayını, yaklaşık 1 dk 58 sn: ortalama 0,011267 A; medyan 0,000 A; min–maks 0,000–0,104 A.
- 48/60 (%80) yayın sıfır; 12/60 (%20) yayın 0,014–0,104 A.
- Raw AC ortalaması 0,0004657 V; bias ortalaması 1,663881 V; SCT-1 ADC ortalaması 1,662508 V.
- Yüksüz senaryo olduğu için UNIT referansı aranmadı. PZEM verisi yok.
- K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi. Tek kısa kayıt, ilk yüksüz taban gözlemidir.
- [Yüksüz test dosyası](idle-no-load/README.md); [analiz](../logs/module2/2026-10-31-load-idle-001-analysis.md); [seçilmiş log kanıtı](../logs/module2/2026-10-31-load-idle-001-evidence.txt).
- Kaynak dosya 36.687 bayt / 514 satır; SHA-256 `9ac3ece0770a85219e7ad6664f15f1ccc9db9b561d04f6195ef034d4e718e455`. Tam kaynak metin kullanıcı yüklemesinde korunmuştur; depoya seçilmiş gerçek satırlardan kanıt dökümü eklendi.


| Test yükü | Ana kayıt |
|---|---|
| 100 W akkor ampul | [100 W akkor — karşılaştırmalı ölçüm tablosu](100w-incandescent/README.md) |
| 150 W akkor ampul | [150 W akkor — karşılaştırmalı ölçüm tablosu](150w-incandescent/README.md) |

## Her ölçüm satırında tutulacak alanlar

1. Test ID ve tarih.
2. Başlangıç/bitiş saati ve log içindeki gerçek ölçüm aralığı.
3. Test yükü ve fiziksel koşul.
4. ESP/kart/modül ve SCT kanalı/GPIO.
5. Firmware dosyası, sürüm/commit ve kod bağlantısı.
6. Log dosyası bağlantısı ve log kaynağının niteliği.
7. Referans cihaz/değer ve kaynak türü.
8. Kodun kararlı bölüm sonucu (ör. ortalama, aralık, örnek sayısı).
9. Mutlak fark ve yüzde sapma.
10. ±%4 değerlendirmesi, teknik yorum ve açık kanıt eksikleri.

## Kanıt sınıfları

- **LOG:** Paylaşılan cihaz logundan doğrudan çıkarılmış veri.
- **KULLANICI BİLDİRİMİ:** Kullanıcının bildirdiği referans veya fiziksel test koşulu.
- **KOD KAYDI:** Depodaki firmware dosyası; tek başına çalıştığını kanıtlamaz.
- **HESAP:** Kaydedilmiş sayısal verilerden hesaplanan sonuç.
- **EKSİK KANIT:** İlgili ham log, zaman aralığı veya tam firmware sürümü mevcut değil.


## 2026-10-31 — LOAD-150W-001 sonucu

- 150 W akkor / ESP32D1 Modül 2 / SCT-1 GPIO32 / harici masaüstü besleme oturumu analiz edildi.
- UNIT kullanıcı bildirimleri 0,598 A ve 0,599 A; geçici ortalama 0,5985 A. ±%4 bandı 0,57456–0,62244 A.
- Uzun log 391 akım yayını içeriyor: ortalama 0,60821 A, medyan 0,608 A; ortalama sapma +%1,62; 388/391 (%99,23) yayın UNIT ±%4 bandında.
- PZEM bu logda yoktur; UNIT karşılaştırması PZEM doğrulaması olarak sunulmaz. K=24.22 değiştirilmedi.
- [150 W karşılaştırma kaydı](150w-incandescent/README.md); [uzun log analizi](../logs/module2/2026-10-31-load-150w-001-sct1-long-analysis.md).
- Ham kaynak dosya adı/boyutu/SHA-256 analizde tanımlandı; ham metnin GitHub'a tam aktarımı açık arşiv işidir.

## Test referans sırası kararı

Her test yükü için önce o yüke ait UNIT ölçümü alınır ve SCT sonucu bu UNIT değeriyle karşılaştırılır. PZEM sonraki aşamada eklenir. UNIT ve PZEM değerleri birbirinin yerine yazılmaz.


## 2026-10-31 — LOAD-IDLE-001 uzun yüksüz log güncellemesi

- Kaynak `esp32d1-logs (37).txt`; 110.590 bayt / 1.492 satır; SHA-256 `e4b229b45abce1f85e74f60260c0a7ed279e48c6b8f59d70ccbabaf23c8ee22f`.
- İlk kısa logdaki 60 akım yayını, uzun logun ilk 60 yayınıyla birebir aynı. Bu yeni test değil, aynı testin uzatılmış kaydı; 140 yeni yayın eklenmiştir.
- Toplam 200 akım yayını: ortalama 0,017130 A; medyan 0,000 A; aralık 0,000–0,144 A; 146/200 (%73) sıfır.
- Devam eden 140 yayında ortalama 0,019643 A; medyan 0,000 A; 98/140 (%70) sıfır.
- Raw AC ortalama 0,00070765 V; bias ortalama 1,664461 V; SCT-1 ADC ortalama 1,662461 V.
- ct_clamp log SPS ortalaması 17.990 (17.465–18.465).
- UNIT/PZEM referansı yok; yüksüz senaryoda UNIT aranmadı. K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.
- [Yüksüz test dosyası](idle-no-load/README.md); [uzun log analizi](../logs/module2/2026-10-31-load-idle-001-analysis.md); [tam ham log](../logs/module2/2026-10-31-load-idle-001-module2-sct1-no-load-full.txt).



| Fan | [Fan kademe test kayıtları](fan/README.md) |

## 2026-10-31 — FAN-1 uzun SCT-1 logu

- Kaynak `esp32d1-logs (39).txt`; özgün SHA-256 `ccc520db070555741d45f3fa67b5866011bec0dadc092c839eb52ff5502eba8e`.
- 97 akım yayını, 17:13:53.070–17:17:05.067 (+03:00); ortalama 0,14114 A, medyan 0,147 A, aralık 0,000–0,259 A.
- İlk açılışın çok kısa yüksüz olduğu kullanıcı tarafından bildirildi. Başlangıç/geçiş değerleri kararlı fan ölçümünden ayrı tutulur.
- FAN-1 UNIT son bildirimi 0,096 A (ilk bildirim 0,097 A); ±%4 aralığı 0,09216–0,09984 A. Logda fanın tam açılma/kararlı zaman işareti yok; kesin sapma kararı verilmedi.
- UNIT PF göstermiyor; PZEM ile sonraki aşamada netleştirilecek. K=24.22 ve yazılımsal sıfır eşiği kararı değişmedi.
- [Fan test kaydı](fan/README.md); [analiz](../logs/module2/2026-10-31-fan1-module2-sct1-analysis.md); [tam ham log](../logs/module2/2026-10-31-fan1-module2-sct1-extended-full.txt).
