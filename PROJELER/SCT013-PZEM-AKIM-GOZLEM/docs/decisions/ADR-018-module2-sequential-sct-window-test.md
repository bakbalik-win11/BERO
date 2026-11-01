# ADR-018 — Modül 2 üç SCT kanalında sıralı ölçüm pencereleri

- **Tarih:** 2026-11-01
- **Durum:** KABUL EDİLDİ — sıralı firmware kullanıcı bildirimiyle derlendi ve çalıştı; nicel log doğrulaması bekliyor
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
