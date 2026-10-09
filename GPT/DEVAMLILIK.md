# GPT — BERO Devamlılık Kaydı

Bu klasör, BERO üzerinde sonraki oturumlarda çalışırken bağlamı korumak için tutulur. Bir insanın yerine geçmez; doğrulanmış proje kararlarını, açık teknik soruları ve çalışma kurallarını kısa ve güncel biçimde saklar.

## 1. Çalışma kuralları

- Kullanıcı Türkçe iletişim kuruyor; teknik terimlerin İngilizcelerini de öğrenmek istiyor. Açıklamalarda Türkçe + gerekli İngilizce terim kullan.
- Kullanıcı açıkça görev verdiğinde gereksiz onay veya tekrar soru sorma. Önce mevcut bilgiyi incele, yapılabileni uygula, sonucu doğrula.
- Yapılmayan işi yapılmış, denenmeyen şeyi test edilmiş, varsayımı doğrulanmış gibi sunma.
- İşlem başarısız olursa net olarak söyle: ne denendi, ne sonuçlandı, ne kaldı. Aynı işi kullanıcıya tekrar tekrar yaptırma.
- Yapı karmaşıklaşırsa yeni klasör/dosya eklemeden önce gerçekten gerekli olup olmadığını değerlendir. Sadelik önceliklidir.
- Proje geçmişini kendiliğinden geri getirme veya yeniden kurmaya çalışma. Kullanıcı yeni başlangıç istedi; yalnızca bundan sonra açıkça gerekli olan bilgileri tut.
- Her teknik değişiklikten sonra mümkünse GitHub'daki gerçek sonucu oku ve doğrula.
- Bu dosyayı yalnızca önemli, kalıcı kararlar veya güncel teknik durum değiştiğinde güncelle. Günlük konuşma dökümü gibi kullanma.

## 2. Yeni GitHub deposu ve mevcut durum

- Depo: https://github.com/bakbalik-win11/BERO
- Varsayılan dal: `main`
- Kullanıcı eski proje yapısını kökünden sildi ve temiz bir başlangıç yaptı. Eski klasör yapısını geri getirme.
- Şu klasörler GitHub'da oluşturuldu ve ağaç kontrolüyle doğrulandı:
  - `DONANIM/`
  - `ENVANTER/`
  - `KOD/`
- Boş klasörleri Git'te tutmak için her birinde `.gitkeep` var.
- Bu kayıt dosyası için `GPT/` klasörü oluşturuluyor. Kullanıcının amacı, oturumlar arasında devamlılık sağlamak ve önemli bağlamın kaybolmasını azaltmak.
- Şimdilik kullanıcı istemedikçe başka ana klasörler üretme.

## 3. Proje amacı ve kalıcı mimari kararlar

- Proje adı: BERO.
- Ev otomasyonu/enerji izleme bağlamı; Home Assistant ve ESPHome kullanılıyor.
- Önceki mimari notlarda 10 adet SCT-013 100A/1V akım sensörü, analog bias devreleri, MCP3208 ADC'ler ve ESP32 ile ölçüm planı bulunuyordu. Ancak güncel ADC araştırması ayrıca MCP3204 üzerine yoğunlaştı; parça/model adlarını karıştırma, her testte kullanılan gerçek donanımı doğrula.
- Home Assistant altyapısı: Raspberry Pi 4 8GB + Argon SSD kasası; Home Assistant OS 18.2, Core 2026.8.2, Supervisor 2026.07.5 bilgileri 2026-08/09 döneminde kaydedildi; güncel sürüm olduğu varsayılmamalı.
- Güç mimarisi için mühürlü karar (2026-08-25):
  - Raspberry Pi 4 + Argon + SSD için ayrılmış/izole 5 V hattı.
  - P4 LCD + panel ESP/sensörler için ayrı 5 V hattı.
  - Oda/saha BUS hattı 24 V.
- Rumelikavağı evi HVAC planında ilk kalıcı yatırım bağımsız, CO₂ kontrollü filtreli havalandırma sistemidir. Multi-split klima seçenek olarak kalır; fan-coil ve kuyu soğutması başlangıç yatırımına dahil değildir. Kuyu en az bir yıl sensörlü/loglu test edilecektir.
- Kullanıcı Modbus ve RS485 tabanlı çözümleri tercih ediyor; ev otomasyonunda ayrı güç hatları ve düzenli modüler yapı önemli.

## 4. Açık teknik konu — ADC/SPI

Bu bölüm önceki testlerden kalan çalışma bağlamıdır; her yeni oturumda güncel donanım ve son test sonucu doğrulanmalıdır.

- ESP32 + MCP3204/MCP3208 SPI ADC okumasında hatalı/kararsız RX desenleri ve sıfır okumalar araştırıldı; kök neden kesinleşmiş değil.
- Kaydedilmiş test bağlantısı: SPI2_HOST, SCLK GPIO18, MISO GPIO19, MOSI GPIO23, CS GPIO5; MODE0, 500 kHz, DMA kapalı, polling, 24-bit transaction. Bu pinler belirli bir test düzenine aittir; yeni donanıma otomatik uygulama.
- Kullanılmış decode ifadesi:
  `uint16_t value = ((rx[1] & 0x0F) << 8) | rx[2];`
- `SPI_ERROR_COUNT = 0` görülmüş olması, verinin doğru olduğunu tek başına kanıtlamaz.
- MCP söküldüğünde benzer RX örüntülerinin görülmesi kaydedildi; dolayısıyla yalnızca ADC'yi suçlama.
- 2026-10-09 tarihli Microchip destek yanıtı (#01906706) için önceki notlar:
  - VREF=3.12 V iken 1 LSB yaklaşık 762 µV.
  - Sabit girişin bias noktasına bağlanıp test edilmesi ve VREF kaynağı/buffer kontrolü önerildi.
  - CS düşükken fazla saat darbesi veri bitlerinin tekrarına neden olabilir; çerçeve uzunluğu tek başına veriyi kaydırmaz.
  - Açılışta CS'nin yüksek-düşük geçişi önemli olabilir.
  - 1 kSPS için Nyquist 500 Hz; CT harmonikleri/anahtarlama gürültüsü aliasing oluşturabilir, anti-alias filtre gerekebilir.
  - 173 ms örnek aralığı boşluğu host zamanlamasından kaynaklanabilir; 1 ms varsayımıyla RMS entegrasyonu hatalı olur. Zaman damgası/timer ve ağırlıklı hesaplama değerlendirilmeli.
- Sıfır değerleri RMS dışında tutma yalnızca geçici pratik kuraldı; kök nedenin çözüldüğü anlamına gelmez.
- Yeni testte ölçülen gerçek RX/TX byte'ları, CS/CLK/DIN/DOUT zamanlaması, VREF ve bias değerlerini kaydet. Önceki varsayımları sonuç gibi tekrar etme.

## 5. Önceki kararları ve deneyleri ele alma

- Eski depo yapısı, eski klasör hiyerarşisi ve geçmiş belgeler kullanıcı tarafından terk edildi; kullanıcı açıkça istemedikçe bunları yeni depoya taşımaya çalışma.
- Yukarıdaki teknik notlar yalnızca tekrar aynı hatalara düşmemek ve bağlamı korumak içindir. Eski raporları otomatik olarak yeniden üretme.
- Yeni test sonucu geldiğinde bu dosyayı kısa bir güncelleme ile değiştir: tarih, donanım/firmware sürümü, test koşulu, gözlem, sonuç ve açık kalan soru.
- Kesinleşmemiş bilgileri açıkça “hipotez”, “geçici kural” veya “doğrulanmadı” olarak etiketle.

## 6. Oturum başında yapılacaklar

1. Depodaki güncel dosyaları oku; bu dosyanın eski kalmış olabileceğini unutma.
2. Kullanıcının son talebini ve en son doğrulanmış sonucu esas al.
3. Tek bir küçük, doğrulanabilir adımla ilerle.
4. İş sonunda yalnızca gerçekten yapılanları ve doğrulananları bildir.

## 7. MCP3204 / MCP3208 adlandırma uyarısı (2026-10-09)

- Üretici ayrımı: MCP3204 = 12 bit, 4 tek uçlu kanal, 14 pinli paket seçenekleri; MCP3208 = 12 bit, 8 tek uçlu kanal, 16 pinli paket seçenekleri. Her ikisi de SPI ADC'dir. Resmî referans: https://www.microchip.com/en-us/product/MCP3204 , https://www.microchip.com/en-us/product/MCP3208 , veri sayfası https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf
- **Kritik tarihsel not:** BERO'nun önceki ESPHome denemelerinde bileşen/kod adı `mcp3204` olarak geçtiği hâlde yapılandırma 8 kanal (CH0–CH7) okuma amacıyla kullanılmıştı. Bu isim çelişkisini sonraki oturumlarda unutma.
- Yazılım bileşen adı, fiziksel entegre modelini kanıtlamaz. Gerçek çipin işaretlemesi/pin sayısı, bileşen sürümü ve 8 kanal desteği birbirinden bağımsız doğrulanmalıdır. MCP3204'ün kendisi 8 analog kanal sunmaz.
- BERO'da MCP3208 için donanım referansı `DONANIM/MCP3208/README.md`, kod ve geçmiş test kaydı `KOD/MCP3208/README.md` altındadır.
- Önceki SPI testinde CH0 0.000 V raporlanmış; benzer RX desenleri ADC sökülüyken de görülmüş; kök neden hâlâ doğrulanmamıştır. Eski test ayarlarını doğrulanmış çözüm gibi sunma.

## 8. Microchip Support arşivi

- Destek yazışmaları: [GPT/MICROCHIP-SUPPORT/DESTEK-YAZISMALARI.md](MICROCHIP-SUPPORT/DESTEK-YAZISMALARI.md)
- Asistan için teknik tecrübe ve sonraki test sırası: [GPT/MICROCHIP-SUPPORT/TEKNIK-TECRUBE.md](MICROCHIP-SUPPORT/TEKNIK-TECRUBE.md)
- Destek yanıtının özellikle vurguladığı başlıklar: statik girişte 2040–2051 kod yayılımı; VREF kaynağı ve bias ağı; CS'nin başlangıç durumu ve fazla saat darbeleri; ham TX/RX ile zero-bit kontrolü; 173 ms örnek aralığının RMS hesabına etkisi; 1 kSPS için anti-aliasing.
- Destek yazışmasından aktarılan öneriler ile BERO'da fiziksel olarak ölçülüp doğrulanmış sonuçları birbirinden ayrı tut.

