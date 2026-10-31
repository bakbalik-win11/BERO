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


## 2026-10-31 — FAN-1 uzun log istatistikleri ve kapanış sınıfı

- FAN-1, Modül 2 ısınma/deneme gözlemi olarak kapatıldı; ±%4 akım doğrulama testi olarak kabul edilmedi.
- Son UNIT bildirimi 0,093 A; ±%4 aritmetik bandı 0,08928–0,09672 A. 17:14:11.079 sonrası yaklaşık 247 yayın: ortalama 0,146757 A; medyan 0,147 A; aralık 0,064–0,259 A; SD 0,026064 A. 4/247 (%1,6) yayın UNIT bandında.
- UNIT PF göstermediğinden PF etkisi doğrulanamadı. FAN-1'in PZEM akım ve PF ile aynı kararlı pencerede yeniden değerlendirilmesi açık kalır.
- FAN-2 ve sonraki fan kademeleri için PZEM akım + PF kaydı gereklidir.
- [FAN-1 kayıt dosyası](fan/README.md); [uzun analiz](../logs/module2/2026-10-31-fan1-module2-sct1-long-analysis.md); [uzun ham log](../logs/module2/2026-10-31-fan1-module2-sct1-long-full.txt); [kapanış kod snapshot](../firmware/archive/FAN-1-2026-10-31-esp32d1-sct1.yaml).


## 2026-10-31 — Düşük akım bölgesi ve FAN-1 değerlendirme düzeltmesi

- **KURAL:** 0,30 A altındaki akım bölgesinde ±%4 kabul/ret ölçütü uygulanmaz. 0,30 A ve üzerindeki koşullarda ±%4 kriteri, eşleşmiş ve kararlı referans verisi mevcutsa kullanılabilir.
- Bu 0,30 A sınırı BERO deney sınıflandırmasıdır; SCT-013 üretici doğruluk garantisi veya fiziksel alt ölçüm sınırı değildir.
- **FAN-1:** UNIT bildirimi 0,093 A; düşük akım araştırma bölgesindedir. Önceki ±%4 bandı ve 4/247 sayımı tarihsel hesap olarak korunur, kabul/ret sonucu sayılmaz. 247 yayın ortalaması 0,146757 A ve medyanı 0,147 A istatistik olarak korunur.
- **FAN-2:** UNIT bildirimi 0,106 A; düşük akım araştırma bölgesindedir. Mevcut SCT logu ayrı gözlem olarak tutulur; ±%4 değerlendirmesi yapılmaz. PZEM akım + PF gereklidir.
- **AYRI DENEY:** [0,30 A altı düşük akım deney planı](low-current-below-0p30/README.md). Tek tur, 2 tur ve 4 tur koşulları planlanmıştır; henüz uygulanmış test değildir.


## 2026-10-31 — FAN-2 uzun SCT-1 logu ve kapanışı

- FAN-2 UNIT bildirimi 0,106 A; 0,30 A altı düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- Uzun log: `esp32d1-logs (42).txt`; 90.706 bayt; SHA-256 `e550d447b75b50e2b99581a70de23b8916caba576a8665240f44574e586a3dca`; 17:26:19.113–17:31:41.120; 162 yayın.
- SCT akım ortalaması 0,168969 A; medyan 0,1685 A; min–maks 0,108–0,257 A. 162 yayının tamamı 0,30 A altındadır.
- Raw AC ortalama 0,00697685 V; bias GPIO35 ortalama 1,663426 V; SCT-1 ADC GPIO32 ortalama 1,660537 V.
- FAN-2, düşük akım gözlem oturumu olarak kapatıldı; ±%4 doğrulaması değildir. PZEM akım + PF ile aynı kararlı pencerede ileri inceleme açık.
- [FAN kayıtları](fan/README.md); [analiz](../logs/module2/2026-10-31-fan2-module2-sct1-long-analysis.md); [tam log](../logs/module2/2026-10-31-fan2-module2-sct1-long-full.txt); [kapanış YAML](../firmware/archive/FAN-2-2026-10-31-esp32d1-sct1.yaml).


## 2026-10-31 — FAN-3 uzun SCT-1 logu ve kapanışı

- FAN-3 UNIT bildirimi 0,141 A; 0,30 A altı düşük akım bölgesinde ±%4 kabul/ret uygulanmaz.
- Uzun log: `esp32d1-logs (43).txt`; 139.575 bayt; SHA-256 `a4345c7af2b5dcc608b264e1dceed50dbe8ee5e40c5137d1eeff2583f9a53a9f`; 17:35:27.127–17:43:55.115; 255 yayın.
- SCT akım ortalaması 0,224612 A; medyan 0,223 A; min–maks 0,189–0,311 A; örnek SD 0,018657 A. 253/255 yayın 0,30 A altındadır.
- Raw AC ortalama 0,009273 V; bias GPIO35 ortalama 1,663387 V; SCT-1 ADC GPIO32 ortalama 1,661008 V.
- FAN-3, düşük akım gözlem oturumu olarak kapatıldı; ±%4 veya PF doğrulaması değildir. PZEM akım + PF ile eşleşmiş kararlı pencere ve olay işaretli açılma/kapanma deneyi açık araştırma işidir.
- [Fan kayıtları](fan/README.md); [FAN-3 analiz](../logs/module2/2026-10-31-fan3-module2-sct1-long-analysis.md); [tam ham log](../logs/module2/2026-10-31-fan3-module2-sct1-long-full.txt); [kapanış YAML](../firmware/archive/FAN-3-2026-10-31-esp32d1-sct1.yaml).


| Karma yük | [100 W akkor + FAN-3 test kaydı](mixed-load-100w-plus-fan3/README.md) |

## 2026-10-31 — MIXED-LOAD-001 açıldı: 100 W akkor + FAN-3

- **AMAÇ:** FAN-3 motor yükünü 100 W akkor dirençli yükle birlikte çalıştırarak toplam hat akımının ve karma yük davranışının SCT-1 tarafından gözlenmesini incelemek.
- **DENEY:** 100 W tek başına; FAN-3 tek başına; ikisi birlikte; 100 W açıkken FAN-3 açılma/kapanma geçişleri.
- **REFERANS:** Önceki ayrı testlerde 100 W için UNIT geçici bildirimi 0,427 A, FAN-3 için 0,141 A'dır. Bunlar karma yük referansı değildir. Yeni birlikte çalışma UNIT ölçümü ve eşzamanlı PZEM akım/PF kaydı alınacaktır.
- **KURAL:** 0,30 A ve üzeri kararlı pencerelerde eşleşmiş referans varsa ±%4 kıyası; 0,30 A altında ±%4 kabul/ret yok. SCT toplam hat akımını gözlemler; tek başına PF veya FAN-3 bileşen akımını ayrıştırmaz.
- **DURUM:** Test planı açıldı; fiziksel deney, yeni log ve sonuç henüz yoktur.
- **AYRINTI:** [MIXED-LOAD-001 test dosyası](mixed-load-100w-plus-fan3/README.md).
