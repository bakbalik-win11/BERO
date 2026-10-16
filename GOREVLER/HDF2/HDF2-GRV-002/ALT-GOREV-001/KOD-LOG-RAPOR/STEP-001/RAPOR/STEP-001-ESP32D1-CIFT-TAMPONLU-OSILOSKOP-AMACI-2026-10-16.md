# STEP-001 — ESP32D1 Çift Tamponlu Osiloskop Hedefi
**Tarih:** 2026-10-16  
**Durum:** AÇIK — amaç ve tasarım yönü kaydedildi; firmware henüz hazırlanmadı/derlenmedi/test edilmedi.

## Amaç
ESP32D1 kartını osiloskop benzeri bir ham sinyal yakalama birimi olarak kullanmak. ADC örneklerini iki RAM tamponunda dönüşümlü toplamak: bir tampon dolduğunda örnekleme diğer tampona geçerken dolan tamponun verisi Mac'e aktarılacak. Mac tarafında Python veriyi alacak, dosyaya kaydedecek ve sonraki aşamada dalga biçimini/ölçümleri işleyecek.

## İlk hedeflenen ayarlar
- Örnekleme hızı: 10 kHz.
- Tampon başına: 1.000 örnek.
- Bir tamponun hedef süresi: 100 ms.
- 50 Hz sinyal için: yaklaşık 5 tam periyot / tampon.
- İlk deneyde MCP3208 kullanılmayacak; ESP32'nin dahili ADC'si kullanılacak.
- Veri işleme ve dosyalama Mac üzerinde Python ile yapılacak.
- Veri aktarımında binary çerçeveleme hedefleniyor.

Bu değerler ilk test hedefleridir; kart, ADC API'si ve firmware tasarımıyla doğrulanmaları gerekir.

## Tasarım yönü
Önceki GRV-Freeze-1 tasarımında ele alınan ADC Continuous + DMA + çift tampon yaklaşımı incelenecek ve gerçek hedef kartla uyumu doğrulanacak. Örnekleme sırasında seri metin yazdırma yapılmaması hedefleniyor; veri örnekleme penceresinden sonra aktarılacak.

İki tampon tek başına veri kaybını önlemeyi garanti etmez. Aktarım gecikmesi iki tamponu da doldurabileceği için en azından taşma/overrun sayacı, frame sıra numarası ve paket doğrulaması tasarıma dahil edilmelidir. Tampon sahipliği ve aktarım kuyruğu açık biçimde tanımlanmalıdır.

## Donanım ve bağlantı bilgisi
- Cihaz: ESP32D1.
- ESPHome cihaz adı: ESP32D1.
- Mevcut Home Assistant ekranında görülen IP: 192.168.0.13.
- Mevcut YAML adı: `esp32d1.yaml`.
- Mac'te görülen seri port: `/dev/cu.usbserial-0001`.

Home Assistant'ta çevrimiçi görünmesi, USB seri portunun kesin olarak bu karta ait olduğunu tek başına kanıtlamaz. Port-kart eşlemesi gerektiğinde fiziksel bağlantı ile doğrulanacaktır.

## Önemli uygulama notu
Mevcut `esp32d1.yaml` ESPHome yapılandırmasıdır. DMA tabanlı, zamanlaması kontrollü osiloskop firmware'inin yalnızca YAML'a birkaç satır eklenerek kurulacağı varsayılmamalıdır. Uygun Arduino-ESP32/ESP-IDF hedefi ve ayrı Mac Python alıcısı belirlenmelidir. Firmware yüklemesi mevcut ESPHome işlevinin yerini alabilir; mevcut YAML ve çalışan ayarlar değiştirilmeden önce yedeklenmelidir.

## Sıradaki işler
1. STEP-001'deki mevcut GRV-008.2 kod adayını ve ilişkili Python alıcısını incele.
2. Kodun gerçek hedef kart, ADC Continuous/DMA API'si, kanal sırası ve örnek sayısıyla uyumunu doğrula.
3. Tampon sahipliği, binary frame, sıra numarası ve taşma davranışını belirle.
4. ESP32D1 için firmware ile Mac Python alıcısını uyumlu hale getir.
5. Önce derle; derleme çıktısını LOG'a kaydet. Başarılı derleme olmadan donanım testine geçildiğini söyleme.
6. Donanım testinde ham veriyi dosyaya kaydet, örnek sayısını ve frame sırasını doğrula, sonra dalga grafiğini üret.

## Başarı ölçütleri
- Derleme sonucu ve kullanılan sürümler kayıtlı.
- İki tamponun dönüşümlü çalıştığı ve örnek kaybı göstergelerinin izlendiği kanıtlanmış.
- Mac Python alıcısı frame'leri doğrulayıp ham veriyi dosyaya kaydetmiş.
- Gerçek test çıktısı ayrıca kaydedilmiş.

## Bu kayıt anındaki sonuç
Bu rapor yalnızca amaç ve tasarım kararını kaydeder. Firmware yazıldığı, derlendiği veya donanımda test edildiği anlamına gelmez.
