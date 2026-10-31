# ct_clamp bileşeninin tasarım tarihçesi

**Alt başlık:** ESPHome ct_clamp – yazar, gerekçe ve tasarım niyeti araştırması

> Kaynak notu: Bu metin, kullanıcının sağladığı Claude açıklamasının Word belgesinden Markdown'a aktarımıdır. İçerik ve iddialar kaynak rapora aittir; bağımsız doğrulama veya BERO kararı olarak okunmamalıdır. Kaynak DOCX: 7.993 bayt; SHA-256: `0c7f56bd6056bd4709410778561641bc683ae8fa6359647323b4a4c2e6995dc2`.

Not: GitHub'da PR #559, PR #2283, PR #647, issue #457 ve resmi belgeyi okudum. Tam commit listesine (git log) ve her PR'ın bütün yorum dizisine ulaşamadım. Aşağıda "bulunamadı" dediğim yerlerde gerekçesi yazılı bir kaynak görmedim. Orada varsayım yapmadım.

## Kısa özet

| Soru | Cevap | Kanıt |
|---|---|---|
| 1. Kim yazdı? | Jesse Hills (jesserockz) PR'ı açtı. Otto Winter (OttoWinter) yapıyı yeniden düzenledi ve birleştirdi. | PR #559 |
| 2. İlk commit | PR #559, Mayıs 2019 sonu. Belge PR'ı 26 Mayıs'a, Otto'nun commit'i 29 Mayıs'a düşüyor, hedef sürüm 1.13. Tam ilk commit saatini doğrulayamadım. | PR #559 |
| 3–5. İhtiyaç / hedef | Genel amaçlı. SCT013'e özel değil. Herhangi bir gerilim örnekleyiciden (ADC, ADS1115) tek faz AC akım okumak. | Belge |
| 6. 200 ms | Belge gerekçeyi veriyor: 50 Hz'de 10 tam periyot. Kimin seçtiği bulunamadı. | Belge |
| 7. 60 s | Gerekçe bulunamadı. | – |
| 8–11. last_value_ == value | Doğruluk için. Performans veya bellek gerekçesi bulunamadı. | PR #2283 |
| 12. Tartışma | Evet, aşağıda. | Issue #457, PR #2283 |

## Kim, ne zaman, neden?

İlk PR (#559): Açıklaması kısa: CT (akım trafosu) kelepçeleri için sensör kodu ekliyor. Jesse test donanımını anlatıyor: D1 Mini A0 pinine bağlı bir CTL-10-CLS kelepçe, burden direnci ve direnç bölücülü devre, evin ana fazında, akıllı sayaçla uyumlu okumalar. Yani motivasyon, ev elektrik tüketimini ESPHome ile görmekti.

Etkileşim: Bir kullanıcı (digiblur) sonuçları EmonLib'le karşılaştırdı ve tutarsız okumalar bildirdi. Belgenin "See Also" kısmı da EmonLib ve OpenEnergyMonitor rehberine bağlanıyor. Bu, tasarımın o dünyadan etkilendiğine işaret ediyor. Kodu yazanların bunu söylediğini görmedim, çıkarımım.

Neden update() yalnızca başlatıyor, loop() örnekliyor? Bunun gerekçesi açık. Otto yorumunda, update() içinde birkaç AC fazı boyunca örneklemenin ana döngüyü yaklaşık 100 ms yavaşlattığını, oysa 20–30 ms civarının kabul edilebilir sayıldığını yazıyor. Bu yüzden kodu loop() tabanlı, eşzamansız hale getirdi. update() örneklemeyi başlatıyor, sample_duration sonunda bir zamanlayıcı sonucu yayınlıyor. Bugünkü yapı, ölçüm hassasiyeti için değil, ESPHome'u bloklamamak için doğdu.

## Genel amaçlı mı, SCT013'e özel mi?

Genel amaçlı. Belge bileşeni, CT kelepçeyi ADC gibi bir analog gerilim sensörüne bağlayıp tek faz AC akım ölçümüne çeviren bileşen olarak tanımlıyor. Kaynak, voltage_sampler arayüzüne bağlı (ADC veya ADS1115 olabilir). Belgede model adı veya burden/bias hesabı yok. İlk örnek ESP8266 A0 üzerinde.

## Hedef: hassas ölçüm mü, kaba izleme mi?

Belge hedef sınıfını açıkça söylemiyor. Okunabilen ipuçları:

- Kalibrasyon yöntemi bilinen bir yükle calibrate_linear kullanmak. Belgenin örneği 4,0 A yük, log'da 0,1333 gösteriyor.
- Belge sample_duration için daha yüksek değerlerin doğruluğu artırabileceğini söylüyor. Doğruluk ifadesi var, bir sayısal garanti yok.
- Düşük akım, bias, gürültü tabanı veya doğruluk sınıfı hakkında hiçbir ifade görmedim.

Sonuç: "Home Assistant'ta makul doğrulukta akım görmek" yönünde. Enerji analizörü veya metroloji hedefi için bir kanıt yok.

## sample_duration = 200 ms, update_interval = 60 s

- **200 ms:** Belge gerekçeyi veriyor: 50 Hz sistemde 10 tam çevrim. Kimin ve neden seçtiğine dair commit veya yorum bulamadım. Issue #457'de bir kullanıcı bunun uygun bir varsayılan olup olmadığını sorguluyor. Başka biri 300 ms'de daha doğru, 400 ms'de fark yok sonucunu bildiriyor (kullanıcı gözlemi, kontrollü ölçüm değil).
- **60 s:** Belgede yalnızca değer ve "sample_duration'dan büyük olmalı" kuralı var. Gerekçe bulunamadı. Aynı 60 s varsayılanı ESPHome'un başka sensör belgelerinde de görülüyor (ATM90E32 sayfasında da görüyorum), yani bileşene özgü bir seçim gibi görünmüyor. Bu bir gözlem, gerekçe değil.

## last_value_ == value filtresi

Kim, ne zaman: PR #2283, skasi7, 12 Ekim 2021'de jesserockz tarafından birleştirildi. Başlık: "Improves ct_clamp component accuracy".

Gerekçe (PR açıklaması): Doğruluğu artırmak için tekrarlanan örnekleri atlamak. ESPHome saniyede 1000'e kadar örnek isteyebilirken ADS1115 gibi ADC'ler nadiren 860 SPS'ten fazlasını veriyor. Değişiklik türü olarak Bugfix işaretli. Test ortamı: ESP8266 (ESP32 işaretli değil), örnek yapılandırmada ADS1115.

Cevaplar:

- Performans için mi? Hayır, böyle bir ifade yok.
- Bellek için mi? Hayır.
- ADC tekrarlarını azaltmak için mi? Evet, ama amaç aynı dönüşümü birden fazla örnek olarak toplamamak. Gerekçe doğruluk.

Önemli çıkarım (benim): Bu mantık, sample() çağrısının önceki dönüşümü tekrar döndürdüğü bir kaynak için kurulmuş (ADS1115, ESP8266). ESP32'nin adc kaynağında ise her sample() yeni bir adc_oneshot_read yapıyor (kodda gördüm). Yani filtrenin asıl gerekçesi ESP32 yerleşik ADC için geçerli değil. Gerçek tekrarlar da (aynı kod, yeni dönüşüm) atılıyor. PR'da düşük genlikte bunun etkisinin tartışıldığını görmedim.

## Diğer tarihçe: düzeltilen bir tasarım hatası

Issue #457 (Haziran 2019), sıfırdan başlayıp yavaşça inen okumaları bildiriyor. Otto neden olarak örneklenen gerilimin ofsetinin 0,5 V'tan başlamasını ve ofsete uygulanan alçak geçiren filtreyi gösteriyor. ESP8266 ADC'si için uygun, ADS1115'in yüksek kazançlarında uygun değil. Düzeltme PR #647 ("CT Clamp ADS1115 Improvements", 2 Temmuz 2019), PR açıklaması boş. Kodun bugünkü hali pencere ortalamasını kullanıyor. Yani ofset kestirimi sonradan değişti, ama değişikliği doğrudan PR metninden doğrulayamadım, çıkarımım. Header'daki last_value_ yorumunun hâlâ "The DC offset of the circuit" demesi, bu geçişten kalan eski bir yorum gibi duruyor (bunu 2026.10.1 API belgesinde gördüm).

Aynı konuşmada Otto şunu da söylüyor: ADS1115 tek atış modunda yavaş olduğundan sinüsün çok örneğini almak zor. Yani tasarım, örnek sayısının sınırlı olduğunu baştan biliyordu.

## BERO'ya çıkarım

- Bileşen, evde kaba-orta doğrulukta akım görmek için yazılmış. Düşük akım doğruluğu için tasarlanmamış.
- last_value_ filtresi ESP8266 + ADS1115 için eklenmiş. ESP32 yerleşik ADC'de bu gerekçe uygulanmıyor, ve yan etkisi (genliğe bağlı sapma) tartışılmamış.
- Sizin için pratik sonuç: hata, yanlış kullanım değil, tasarım varsayımlarının sizin donanımınıza uymaması. Bu, ayrı bir özel bileşenle çözmek için meşru bir gerekçe.

## Eksik kalanlar

- 2021'den sonraki ESP32/ESP-IDF geçişleri ve diğer PR'ların tam listesi.
- PR #2283'ün tüm inceleme yorumları (yalnızca bir kısmını görebildim).
- 200 ms ve 60 s kararlarının sahibi.
