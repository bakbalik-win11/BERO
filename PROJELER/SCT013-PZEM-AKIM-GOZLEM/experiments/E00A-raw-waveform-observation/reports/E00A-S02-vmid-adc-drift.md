# E00A-S02 — Sabit Vmid DC altında ADC voltaj çıktısının düşmesi

**Tarih:** 2026-10-30  
**Kaynak:** Kullanıcının bu oturumda paylaştığı ESPHome logu  
**Cihaz:** ESP32D2, ESPHome 2026.9.1, ESP32 rev3.1, ESP-IDF  
**ADC kanalı:** GPIO35 / ADC1_CH7 / 12 dB / samples 1 / update 1 s  
**Diğer kanal:** GPIO34 / ADC1_CH6 / raw count

## HEDEF
Kullanıcının multimetrede sabit yaklaşık 1,65 V DC gördüğünü bildirdiği koşulda ESP32 ADC voltaj çıktısının kararlılığını incelemek.

## LOG
- Kullanıcı bildirimi: multimetrede yaklaşık 1,65 V DC sabit görülüyor. Multimetre problarının tam olarak hangi iki fiziksel noktaya bağlandığı bu logla belirlenemiyor.
- GPIO35 ADC voltaj çıktısı: 14:57:02.885'te 1,678 V; 14:57:04'te 1,709 V; 14:57:08'de 1,707 V; 14:57:14'te 1,662 V; 14:57:18'de 1,477 V; 14:57:21'de 1,192 V; 14:57:24'te 0,857 V; 14:57:26'da 0,699 V.
- Görünen aralıkta GPIO35 çıktısı yaklaşık 24 saniyede 1,678 V'tan 0,699 V'a düşüyor.
- GPIO34 raw kanalında görünen tüm örnekler 0 count.
- Her iki ADC kanalında Handle Init, Config, Calibration ve Overall Init OK.
- GPIO34 ve GPIO35 farklı fiziksel pinlerdir; aynı analog noktanın iki farklı gösterimi değildir.
- Log parçası 14:57:26'da sona erdiği için daha sonraki davranış bilinmiyor.

## SONUÇ
Bu kayıt, GPIO35 ADC voltaj çıktısının gözlenen zaman aralığında kararlı olmadığını gösterir. Multimetrede bildirilen sabit 1,65 V ile ADC çıktısı arasında açıklanması gereken bir tutarsızlık vardır. Ancak multimetrenin ölçtüğü noktanın GPIO35 pin düğümüyle aynı olduğu henüz teyit edilmediğinden ADC dönüşüm hatası veya ADC donanım arızası sonucu çıkarılamaz.

## Olası nedenler — henüz hipotez
1. Multimetrenin ölçtüğü Vmid noktası ile GPIO35 ADC pininin elektriksel olarak aynı düğüm olmaması veya bağlantı sorunu.
2. Bias kaynağının/bağlantının kaynak empedansı ile ADC giriş örnekleme davranışının etkileşmesi.
3. Kart üzerindeki GPIO35 fiziksel pininin yanlış tanımlanması veya kablo/temas sorunu.
4. ADC kalibrasyonlu voltaj dönüşümünün bu çalışma koşulunda davranışı.

Bu log tek başına ADC arızasını kanıtlamaz. ESPHome ADC başlatma ve kalibrasyon yapılandırmasının OK olması da analog ölçümün doğru olduğunu kanıtlamaz.

## SONRAKİ AYIRICI TEST
1. Multimetre problarını doğrudan ESP32 kartındaki GPIO35 pini ile ESP32 GND arasına bağla; aynı anda Vmid breadboard noktasını değil, doğrudan ADC pinini ölç. Bu bağlantı noktası farkını ortadan kaldırır.
2. GPIO35 pininde multimetre sabit yaklaşık 1,65 V gösterirken logdaki GPIO35 ADC çıktısını izle.
3. GPIO35 pininde multimetre de düşüyorsa sorun ADC dönüşümünden önceki elektriksel bağlantı/bias kaynağı tarafındadır.
4. GPIO35 pininde multimetre sabit kalıyor ama ESPHome ADC çıktısı düşüyorsa aynı pin için ADC ölçüm yolu, giriş empedansı/örnekleme ve kalibrasyon davranışı ayrı test edilir.
5. Bu ayırıcı test bitene kadar pull direnci, ek kondansatör veya yazılım filtresi ekleme; aynı anda birden fazla değişken değiştirme.

## Karar
- **S02:** ADC voltaj çıktısında belirgin düşüş gözlendi; kararlılık kabul edilmedi.
- **Sorun durumu:** Vmid bildirilen DC referansı ile GPIO35 ADC çıktısı arasındaki tutarsızlık henüz kök nedenine ayrıştırılmadı.
- **E00A:** Açık. Önce multimetreyi doğrudan GPIO35–GND noktasında kullanarak düğüm eşitliği doğrulanacak.