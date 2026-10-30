# E00A-S01 — ADC girişinin GND referansında kararlılık testi

**Tarih:** 2026-10-30  
**Deney kimliği:** E00A alt adımı S01  
**Kaynak:** Kullanıcının paylaştığı ESPHome logu `Yapıştırılan metin(8).txt`  
**Cihaz:** ESP32D2, ESPHome 2026.9.1, ESP32 rev3.1, ESP-IDF  
**Sensör:** SCT bağlı değil  
**Firmware:** `firmware/esp32d2-e00a-adc.yaml`

## HEDEF
Sensör bağlı değilken ADC girişleri GND'ye referanslandığında iki kanalın uzun süreli kararlılığını gözlemek. Amaç ADC'nin açıkta kalma davranışıyla tanımlı elektriksel giriş davranışını ayırmak.

## LOG
Kullanıcı bildirimi: GPIO34 ve GPIO35 GND'ye bağlandı. Paylaşılan logda:
- Log başlangıcı yaklaşık 14:49:10.
- GPIO34: 14:49:11'den 14:52:24'e kadar görünen tüm örneklerde **0 count**.
- GPIO35: ilk bölümde 0.181–0.195 V civarında değerler, kısa bir geçişte 2.405 V'a yükselme ve sonra düşüş görüldü. Yaklaşık 14:49:29'dan log sonuna (14:52:24) kadar **0.142 V sabit** raporlandı.
- Kararlı bölüm yaklaşık 175 saniyedir. Bu, planlanan 30 saniyeden uzundur.
- Başlangıçtaki geçişin nedeni log tek başına belirlenemiyor; GND bağlantısının ne zaman yapıldığına dair ayrı zaman işareti yok.
- ADC başlatma, kanal yapılandırması ve kalibrasyon durumları her iki kanalda da OK.
- ESPHome sensör güncelleme aralığı 1 saniyedir. Bu log yüksek hızlı ham örnekleme veya gerçek ADC doğruluk testi değildir.

**Kanıt sınıflandırması:** Cihaz logunda görünen değerler doğrudan log kanıtıdır. Pinlerin GND'ye fiziksel olarak bağlandığı bilgisi kullanıcı bildirimidir.

## SONUÇ
1. GPIO34, GND referansında 0 count göstermiş ve log boyunca kararlı kalmıştır.
2. GPIO35, kalibrasyonlu voltaj çıktısında 0.142 V tabanında sabitlenmiştir. Bu değer fiziksel olarak GND'ye bağlı koşulda raporlandığı için ADC voltaj dönüşümünün sıfır noktası/ofset davranışı ayrıca incelenmelidir. Bu tek test, 0.142 V'un nedenini kesinleştirmez.
3. Önceki sensörsüz/açık giriş logunda görülen geniş ve değişken değerler, GND referans testinde görülmemiştir. Bulgular, önceki davranışın ADC girişinin floating (tanımsız empedans/gerilim) kalmasıyla uyumlu olduğunu destekler.
4. Bu test ADC'nin tüm aralıkta doğru olduğunu, 1.65 V ölçümünü veya SCT sinyalini doğru okuyacağını kanıtlamaz.
5. İki ayrı GPIO kullanıldığı için GPIO34 count ile GPIO35 voltajı birbirine dönüştürülerek karşılaştırılamaz.

## Sorun tanımı
**Birincil sorun:** ADC pini sensör/ön uç bağlantısı yokken elektriksel olarak tanımlı bir DC seviyeye bağlı değilse giriş floating kalır. GPIO34 ve GPIO35 klasik ESP32 ADC1 girişleridir; bu pinlerde dahili pull-up/pull-down bulunmadığından yazılımda raw, samples veya ortalama ayarı yapmak girişin elektriksel durumunu tanımlamaz.

Bu, şu anki kanıta göre ADC donanım arızası değildir. GND'ye bağlandığında kararlı sonuç alınması ADC kanalının en azından bu uç koşulda yanıt verdiğini gösterir.

## Elektriksel çözüm seçenekleri
### Tercih edilen tasarım adayı — Vmid'e pasif bias/pull direnci
SCT'nin gerilim çıkışlı (1 V) kullanımında, giriş topolojisi doğrulandıktan sonra ADC düğümünün Vmid'e yüksek değerli bir dirençle bağlanması değerlendirilsin. Böylece SCT fişi çıkarıldığında da ADC düğümü boşta kalmaz; yaklaşık Vmid seviyesinde tanımlı kalır. SCT bağlıyken CT'nin AC çıkışı bu DC çalışma noktası etrafında ADC'ye uygulanır.
- İlk değerlendirme aralığı: **47 kΩ–100 kΩ** Vmid–ADC düğümü direnci; bu bir tasarım önerisidir, henüz onaylanmış BOM değeri değildir.
- 100 kΩ, 2×10 kΩ Vmid bölücüsünü 10 kΩ gibi düşük bir değerle yüklememek ve CT çıkışını gereksiz yüklememek için ilk prototip adayıdır.
- SCT jack pinlerinin hangisinin Vmid'e, hangisinin ADC'ye gideceği mevcut fiziksel kablo/jack bağlantısı doğrulanmadan varsayılmayacak.
- Vmid kaynağı ve ESP32 GND ortak referansta olmalı.
- Bias devresinin 2×10 kΩ bölücüsü ve kondansatörleri korunmalı; mevcut Vmid ağını yeniden tasarlamadan ek yükün gerçek Vmid üzerindeki etkisi multimetreyle ölçülmeli.
- ADC giriş gerilimi ESP32'nin izin verilen sınırları içinde kalmalı. SCT'nin maksimum çıkışı ve geçici durumları doğrulanmadan doğrudan bağlantı yapılmamalı.

### Alternatifler
- GND'ye pull-down: girişin boşta kalmasını önler ama bu BERO sinyalinin DC merkezini 0 V'a çeker; Vmid etrafında AC ölçüm için uygun çözüm değildir.
- GPIO34/35'i yazılımla sıfırlamak/ortalama almak: floating girişin elektriksel belirsizliğini çözmez; önerilmez.
- Daha düşük değerli pull direnci: Vmid bölücüsünü ve CT çıkışını daha fazla yükleyebilir; hesap ve ölçüm olmadan seçilmemeli.

## Sıradaki test
1. GND jumper'larını kaldırmadan önce cihazı enerjisiz bırak.
2. Mevcut bias devresinin Vmid–GND değerini multimetreyle yeniden doğrula.
3. Önce yalnız bir ADC kanalında, akım trafosu bağlı değilken Vmid'e direnç üzerinden tanımlı bias uygula; ADC düğümünün DC değerini multimetreyle doğrula.
4. Logda 60 saniye kararlılığı gözle.
5. Sonra direnç ve jack bağlantı topolojisini doğrulayıp SCT çıkışını bağla; önce yüksüz, ardından kontrollü düşük riskli test yükü.
6. GPIO35'in 0.142 V GND tabanını ayrı bir ADC kalibrasyon gözlemi olarak ele al; ham ve voltaj kanallarını aynı girişin eşdeğeri gibi yorumlama.

**Güvenlik:** Bu çalışma yalnızca izole, düşük gerilimli DC/bias ve SCT sekonder tarafında yapılır. Şebeke gerilimi veya transformatörün ham AC sekonderi ESP32 GPIO'suna bağlanmaz.

## Karar
- **S01 sonucu:** GND referansında kararlılık gözlendi.
- **Floating giriş teşhisi:** Destekleniyor.
- **Elektriksel düzeltme:** Vmid'e yüksek değerli pasif bias direnci, fiziksel jack/CT bağlantısı doğrulandıktan sonra prototiplenecek.
- **E00A:** Tamamlanmadı. Vmid testi, gerçek SCT bağlantısı, ham örnek kaydı ve zaman grafiği hâlâ açık.