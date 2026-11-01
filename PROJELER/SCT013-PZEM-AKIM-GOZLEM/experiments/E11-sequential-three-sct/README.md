

## 2026-11-01 — E11 Log 66 / 100 W UNIT karşılaştırması (kullanıcı yük teyidi)

- Deney 100 W akkor ampul yüküyle başlatıldı; Log 66 aynı deney oturumunun uzun kaydıdır.
- Tarihsel UNIT referansı 0,427 A; eşzamanlı UNIT ölçümü yoktur. ±%4 bandı 0,40992–0,44408 A.
- 396 kararlı çevrim ortalamaları: SCT1 0,423884 A (−%0,730), SCT2 0,424328 A (−%0,626), SCT3 0,425828 A (−%0,274).
- Üç kanalın ortalaması da tarihsel UNIT referansına göre ±%4 içindedir. Üç sensör aynı deney oturumunda kullanılmıştır; firmware ADC pencerelerini eşzamanlı değil SCT1 → SCT2 → SCT3 sırasıyla çalıştırır. Bu oturum için yeni sıralı kod başarılı kabul edilir; sonuç eşzamanlı UNIT doğrulaması veya genel kalibrasyon garantisi değildir.
- SCT2'nin kabul edilmiş örnek sayısı yaklaşık %5 düşüktür; 42/396 çevrimde en az bir script geçiş işareti 200–300 ms tanısal aralığın dışındadır. Gerçek pencere sınırları callback ile doğrulanmadığından 50 ms pay azaltılmaz.
- K=24.22 değişmedi. Ayrıntı: [Log 66 uzatılmış analiz](../../logs/module2/2026-11-01-e11-three-sct-sequential-extended-analysis.md).
# E11 — Üç SCT kanalında sıralı CT Clamp okuması

- **Tarih:** 2026-11-01
- **Görev:** [T010](../../tasks/T010-module2-triple-sct-bringup.md)
- **Karar:** [ADR-018](../../docs/decisions/ADR-018-module2-sequential-sct-window-test.md)
- **Durum:** KULLANICI BİLDİRİMİYLE DERLENDİ VE ÇALIŞTI; nicel log analizi bekliyor.

## Amaç

Aynı 100 W akkor ampulü fiziksel olarak gözleyen üç SCT kanalının, ESP32 üzerinde ölçüm pencereleri sırayla çalıştırıldığında ayrı ayrı okuma ürettiğini denemek. Önceki eşzamanlı yazılım okuma denemesinde sağlıklı sonuç alınmadığı için her çevrimde tek bir `ct_clamp` penceresi etkin tutulur.

## Donanım ve bağlantılar

| Kanal | Kablo | ESP32D1 pini |
|---|---|---|
| SCT-1 | Sarı sinyal | GPIO32 / ADC1_CH4 |
| SCT-2 | Yeşil sinyal | GPIO33 / ADC1_CH5 |
| SCT-3 | Mavi sinyal | GPIO34 / ADC1_CH6 |
| Ortak bias | Turuncu | GPIO35 / ADC1_CH7 |

Üç SCT sinyal yolu bağımsızdır; bias tek ortak devre ve tek ortak dağıtım hattıdır.

## Uygulama

- ESPHome: 2026.10.1
- Framework: ESP-IDF
- ADC attenuation: 12 dB
- Her `ct_clamp` penceresi: 200 ms
- Her kanal slotu: 250 ms (200 ms pencere + 50 ms bekleme payı)
- Kanal sırası: SCT-1 → SCT-2 → SCT-3
- Ortak bias: üç kanal çevriminden sonra bir kez okunur.
- Çevrim tetikleme aralığı: 2 saniye
- Script modu: `single`
- Akım katsayısı: K=24.22 (değiştirilmedi; bu test kalibrasyon değildir).

## Kullanıcı tarafından bildirilen sonuç

Kullanıcı 2026-11-01 tarihinde bu YAML'ın **derlendiğini ve cihazda çalıştığını** bildirdi. Bu, derleme ve çalışma için birinci el kullanıcı raporudur.

Bu aşamada ham cihaz logu, kanal başına ölçüm örnekleri, ölçüm dağılımları veya gerçek zaman damgaları bu kayıtla birlikte sunulmadı. Bu nedenle:
- Üç kanalın firmware'de etkinleşip çalıştığına dair kullanıcı bildirimi kaydedilmiştir.
- Kanal başına doğruluk, tekrarlanabilirlik ve ölçüm farkı hakkında nicel sonuç çıkarılmamıştır.
- Pencere çakışmadığı ve gerçek merkez-zaman farkının tam 500 ms olduğu log zaman damgalarıyla henüz ölçülmüş değildir.
- 50 ms geçiş payının optimum olduğu iddia edilmez.

## Zamanlama hesabı — tasarım değerleri

| Kanal | Başlangıç | 200 ms pencere bitişi | Sonraki başlangıca kadar pay |
|---|---:|---:|---:|
| SCT-1 | 0 ms | 200 ms | 50 ms |
| SCT-2 | 250 ms | 450 ms | 50 ms |
| SCT-3 | 500 ms | 700 ms | 50 ms |

İlk ve son kanal ölçüm pencerelerinin nominal merkezleri arasında 500 ms vardır. Üç kanal slotu toplam 750 ms sürer. Bunlar YAML zamanlama değerlerinden hesaplanan nominal değerlerdir; logla ölçülmüş gerçek zamanlar değildir.

## Sonraki test aşaması

1. Cihaz logunu al ve SCT1/2/3 START/COMPLETE sırasını doğrula.
2. Her kanalın Raw AC ve akım yayınlarını ayrı ayrı incele.
3. Aynı yük ve aynı çevrimlerde kanal bazında ortalama, medyan, min-maks ve dağılımı karşılaştır.
4. Log zaman damgalarından gerçek başlangıç/bitiş ve merkez-zaman farklarını hesapla.
5. Pencere çakışması olmadığını doğrula; ardından 50 ms geçiş payının azaltılabilirliğini dene.
6. Log örneği ve analizi bu klasöre ekle.

## Kayıt sınırı

Bu kayıt kodun kullanıcı bildirimiyle derlenip çalıştığını belgelemektedir. Henüz kanal karşılaştırma analizi, senkron kayması ölçümü veya kalibrasyon/doğruluk onayı değildir.


## 2026-11-01 — İlk üç kanallı log analizi

- Kaynak: `esp32d1-logs (64).txt`; 2.795 satır / 208.718 bayt; SHA-256 `97a36071b8319625df5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.
- [Maskelenmiş tam log](../../logs/module2/2026-11-01-e11-three-sct-sequential-full-sanitized.txt); [analiz](../../logs/module2/2026-11-01-e11-three-sct-sequential-analysis.md); [kanıt satırları](../../logs/module2/2026-11-01-e11-three-sct-sequential-evidence.txt).
- 176 çevrimde üç kanalın 176'şar akım ve Raw AC yayını, ayrıca 176 bias yayını görüldü. İlk çevrim açılış verisi olarak ayrıldı; kararlı istatistikler sonraki 175 çevrimden hesaplandı.
- SCT1 ortalama 0.42141 A / CV %1.98; SCT2 0.42283 A / CV %2.36; SCT3 0.42686 A / CV %2.09. Bias ortalaması 1.66022 V.
- 12:01:07 çevriminde sıra işaretleri 16/454/392 ms aralıkları gösterdi. İşaretler ve debug örnek sayıları çeliştiği için gerçek pencere çakışmasızlığı kesin doğrulanmadı; 50 ms geçiş payı azaltılmayacak.
- PZEM yoktur; 0.427 A geçici UNIT beklentisidir. Kalibrasyon veya ±%4 kabul sonucu çıkarılmadı. T010 aktif kalır.


## 2026-11-01 — Uzatılmış üç SCT logu (Log 66)

- **KAYNAK:** [Log 66 tam arşiv](../../logs/module2/2026-11-01-e11-three-sct-sequential-log66-full-overlap.txt); 5.000 satır / 378.656 bayt. SHA-256: `b1bad3f1a8ef010d4ff5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.
- **ÖRTÜŞME:** Log 66'nın ilk 1.678 satırı Log 64'ün son 1.678 satırıyla birebir aynıdır; analizde bir kez sayıldı.
- **ANALİZ:** [Uzatılmış analiz](../../logs/module2/2026-11-01-e11-three-sct-sequential-extended-analysis.md); [seçilmiş kanıt](../../logs/module2/2026-11-01-e11-three-sct-sequential-extended-evidence.txt).
- **KAPSAM:** Birleştirilmiş zaman çizgisinde 397 tamamlanmış çevrim vardır. İlk açılış çevrimi ve son yarım çevrim dışarıda bırakılarak 396 kararlı çevrim/kanal incelendi.
- **AKIM ORTALAMALARI:** SCT1 0.423884 A (CV %2.646), SCT2 0.424328 A (CV %2.810), SCT3 0.425828 A (CV %2.215). Bias ortalaması 1.660866 V.
- **ÖRNEK SAYISI:** Ortalama farklı örnekler/200 ms: SCT1 3401.9, SCT2 3235.5, SCT3 3414.9. SCT2 yaklaşık %5 düşük kabul edilmiş örnek sayısıyla önceki logdaki davranışı tekrarladı.
- **ZAMANLAMA:** 42/396 çevrimde en az bir script geçiş işareti 200–300 ms tanısal aralığının dışındadır. 12:01:07.174 çevriminde 16/454/392 ms; 12:06:06.849 çevriminde 309/393/392 ms görüldü.
- **KANIT SINIRI:** START/COMPLETE işaretleri doğrudan pencere callback'i değildir; COMPLETE işareti sabit 250 ms delay sonrasında yazılır. Gerçek pencere çakışmasızlığı kesin doğrulanmadı. İki Wi-Fi roaming scan olayı zamanlama sapmalarına yakın görünür; nedensellik kanıtlanmadı.
- **REFERANS:** PZEM/UNIT kaydı yok; fiziksel yük ve besleme metadata'sı açıkça tanımlı değil. Kalibrasyon veya ±4% kabulü çıkarılmadı.
- **DURUM:** YAML ve K=24.22 değişmedi. 50 ms geçiş payı azaltılmayacak. T010 AKTİF.


## 2026-11-01 — T010 kapatıldı / SCT2-SCT3 soket değişimi gözlem planı

- T010 kapatıldı; E11 üç-SCT okuma kodu 100 W akkor ampul oturumunda üç kanaldan veri üretti.
- **PLANLANAN SON KANAL GÖZLEMİ:** SCT-2 ve SCT-3 fiziksel fişleri/soketleri yer değiştirilecek; ardından aynı 100 W ampulle kısa bir log alınacak. Yalnız kanal davranışı izlenecek.
- **Amaç:** Önceki logda SCT2'de görülen yaklaşık %5 düşük kabul edilmiş örnek sayısı sensörle mi, yoksa kanal/GPIO okuma yoluyla mı birlikte hareket ediyor sorusuna gözlemsel veri sağlamak.
- **Kontrollü sabitler:** YAML/firmware, K=24.22, GPIO32/33/34 eşlemesi, okuma sırası, 200 ms pencere, 250 ms slot ve 2 s çevrim değiştirilmez. Yalnız fiziksel 2 ve 3 numaralı soketlerdeki SCT fişleri yer değiştirilir.
- **Kapsam dışı:** UNIT/PZEM doğruluk kıyası, ±%4 kabul kararı, katsayı ayarı veya yeni yük karakterizasyonu yapılmayacak.
- **Güvenli işlem:** Yük kapalı ve düzenek enerjisizken SCT fişlerini değiştir; bağlantılar kontrol edildikten sonra 100 W deneyi başlat.
- **Durum:** PLANLANDI; fiziksel değişim ve yeni log bekleniyor.
