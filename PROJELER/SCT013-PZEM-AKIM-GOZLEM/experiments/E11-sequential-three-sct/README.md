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
