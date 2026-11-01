# ADR-018 — Modül 2 üç SCT kanalında sıralı ölçüm pencereleri

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — sıralı firmware derlendi/çalıştı ve kanal logu analiz edildi; gerçek pencere çakışmasızlığı zamanlama anomalisi nedeniyle kesin doğrulanmadı
- **İlgili görev:** [T010](../../tasks/T010-module2-triple-sct-bringup.md)
- **İlgili firmware:** [esp32d1.yaml](../../firmware/esp32d1.yaml)

## Bağlam

Modül 2'de üç bağımsız SCT sinyal kanalı ve tek ortak bias hattı vardır. Kullanıcı, üç kanalın yazılımda birlikte örneklenmesi denemesinde sağlıklı sonuç alınmadığını bildirmiştir. Projenin ihtiyacı, üç sensörün aynı fiziksel yükü gözlemesi ve kanalların ölçüm çıktılarının birbirleriyle karşılaştırılmasıdır. Tam eşzamanlı ADC örneklemesi bu deneyin şartı değildir; ancak kanallar arası zaman kayması küçük tutulmalıdır.

## Karar

SCT'ler aynı 100 W akkor ampulü fiziksel olarak aynı anda gözler. ESP32 ölçüm pencereleri ise çakışmayacak şekilde sıralı tetiklenir:

1. SCT-1 / GPIO32
2. SCT-2 / GPIO33
3. SCT-3 / GPIO34
4. Üç kanal tamamlandıktan sonra ortak bias / GPIO35

Bir kanalın `ct_clamp` penceresi tamamlanmadan sonraki kanalın `component.update` çağrısı yapılmaz. Otomasyon tekil çalıştırma modunda tutulur; aynı çevrimden ikinci bir çevrimin üst üste başlaması engellenir.

## İlk zamanlama adayı ve senkron kayması

- `sample_duration`: 200 ms.
- İlk aday kanal slotu: 250 ms (200 ms pencere + 50 ms geçiş payı).
- Yaklaşık ölçüm merkezi farkı: komşu kanallar 250 ms; SCT-1 ile SCT-3 500 ms.
- İlk-son kanal ölçüm pencereleri toplamı yaklaşık 700 ms.

Bu süreler ilk firmware adayının tasarım değerleridir; ölçülmüş gerçek çalışma zamanı değildir. Kullanıcının küçük senkron kayması hedefi nedeniyle 50 ms payın gerekliliği log üzerinden değerlendirilecek. Pencere bitişi ile sonraki başlangıç arasındaki gerçek boşluk ölçülecek; çakışma olmadan güvenli olan en küçük pay seçilecek. `sample_duration` değerini veya örnekleme algoritmasını değiştirmek ayrı deney/karar gerektirir.

## Doğrulama ölçütleri

- Üç kanal ayrı ve geçerli çıktı üretir.
- Her kanalın çıktı etiketi doğru GPIO/SCT girişine karşılık gelir.
- Ölçüm pencereleri çakışmaz.
- START/COMPLETE zaman damgalarıyla gerçek kanal merkez-zaman farkı hesaplanabilir.
- Aynı 100 W yük koşulu korunur.
- Ortak bias yalnız kanal sıralaması tamamlandıktan sonra okunur.
- Tekrarlı çevrimlerde kanal davranışı karşılaştırılabilir olmalıdır.

## Güvenlik ve kapsam

Bu yöntem bir hobi düzeneğinde kanal davranışı gözlemidir; laboratuvar eşzamanlılığı, kalibrasyon veya ölçüm doğruluğu sertifikası değildir. SCT yalnızca tek yalıtılmış iletkeni çevrelemeli; SCT bağlantısı yük enerjisizken değiştirilmelidir. Şebeke tarafı kapalı/korumalı düzenekte kalmalıdır.

## Kayıt durumu

Bu ADR hedefi ve deney yöntemini sabitler. YAML derlemesi, OTA, fiziksel ölçüm ve log analizi henüz yapılmadı. Başarı iddiası yoktur.


## Uygulama durumu — 2026-11-01

Kullanıcı, bu ADR'ye dayalı üç kanallı sıralı YAML'ın derlendiğini ve cihazda çalıştığını bildirdi. Kod snapshot ve deney kaydı [E11 klasöründe](../../experiments/E11-sequential-three-sct/README.md) saklanır. Ham log ve kanal bazında sayısal analiz henüz eklenmediği için gerçek zaman kayması, pencere çakışmasızlığı ve kanal tekrarlanabilirliği nicel olarak doğrulanmış değildir. 50 ms geçiş payı ilk çalışan konfigürasyon değeridir; optimum olduğu kabul edilmez.


## Log doğrulaması — 2026-11-01

E11 üç kanal logunda 176 çevrim ve her kanal için 176 akım/Raw AC yayını görüldü. İlk çevrim hariç kanal ortalamaları SCT1 0.42141 A, SCT2 0.42283 A, SCT3 0.42686 A; bias ortalaması 1.66022 V'tur. Kanal dağılımları birbirine yakındır.

Bununla birlikte 12:01:07 çevrimindeki sıra işaretleri 16/454/392 ms aralıkları göstermiş, aynı çevrimin debug örnek sayılarıyla çelişmiştir. Dolayısıyla bu log, her çevrimde gerçek pencere çakışmasızlığını kesin kanıtlamaz. 50 ms geçiş payı azaltılmayacak; zamanlama anomalisinin tekrar logla incelenmesi gerekir. PZEM verisi bulunmadığından kalibrasyon veya ±%4 doğruluk sonucu çıkarılmaz.

Ayrıntı: [E11 log analizi](../../logs/module2/2026-11-01-e11-three-sct-sequential-analysis.md).


## Uzatılmış log doğrulaması — 2026-11-01

Log 64 ve Log 66 birleştirilirken Log 66'nın Log 64 ile birebir aynı olan 1.678 satırlık örtüşmesi tek kez sayıldı. Birleşik zaman çizgisinde 397 tamamlanmış çevrim vardır; ilk açılış çevrimi ve son yarım çevrim hariç 396 çevrim incelendi.

Kanal ortalamaları SCT1 0.423884 A, SCT2 0.424328 A, SCT3 0.425828 A; CV değerleri sırasıyla %2.646, %2.810 ve %2.215'tir. SCT2'nin ortalama kabul edilmiş farklı örnek sayısı 3235/200 ms olup SCT1 ve SCT3'ten yaklaşık %5 daha düşüktür.

200–300 ms tanısal aralığının dışında en az bir geçişi olan çevrim sayısı 42/396'dır. 12:01:07.174 ve 12:06:06.849 çevrimleri belirgin zamanlama sapmaları gösterir. İki Wi-Fi roaming scan kaydı bu sapma kümelerinin yakınındadır; olası etki olarak izlenir, neden kabul edilmez.

YAML'daki COMPLETE işaretleri gerçek pencere bitiş callback'inden değil sabit 250 ms delay sonrasından üretildiği için script işaretleri tek başına ADC pencerelerinin gerçek sınırını kanıtlamaz. 50 ms pay azaltılmaz; gerçek pencere başlangıç/bitişini cycle_id ile callback tabanlı kaydetmeden çakışmasızlık kabul edilmez.

Ayrıntı: [uzatılmış analiz](../../logs/module2/2026-11-01-e11-three-sct-sequential-extended-analysis.md), [Log 66 arşivi](../../logs/module2/2026-11-01-e11-three-sct-sequential-log66-full-overlap.txt), [seçilmiş kanıt](../../logs/module2/2026-11-01-e11-three-sct-sequential-extended-evidence.txt).

PZEM/UNIT karşılaştırması yoktur; yük ve besleme metadata'sı logda açıkça tanımlı değildir. K=24.22 ve firmware değişmemiştir. T010 AKTİF kalır.
