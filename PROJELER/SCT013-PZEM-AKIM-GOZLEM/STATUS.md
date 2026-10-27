# Proje durumu

**Son güncelleme:** 2026-10-27  
**Aktif faz:** Faz 0 — hazırlık ve güvenlik  
**Aktif görev:** [T004 — Analog ön uç](tasks/T004-analog-frontend.md) — PLANLANDI. T003, PZEM'e göre ±%4 bağıl sapma ve Python `OK` karar kuralı belirlenerek kapatıldı. T001 envanter ve T002 güvenlik kontrolü kullanıcı beyanlarıyla kaydedilip kapatıldı; T002 fiziksel kontrolleri asistan tarafından bağımsız doğrulanmadı.  
**Öncelikli SCT:** SCT013-030 (30 A / 1 V)  
**PZEM:** Esas kaynak [DONANIM/PZEM-004T/README.md](../../DONANIM/PZEM-004T/README.md); CT modeli kullanıcı tarafından PZCT-02 (0–100 A) olarak belirtildi.  
**Bias üretim alt devresi:** TAMAMLANDI — kullanıcı onayı. RN130421 + KBU6M + 2200 µF / 35 V + L78L33; ayrı breadboardda 2 × 10 kΩ bölücü ve orta noktadan GND'ye 104 (100 nF) kondansatör. Bağımsız ölçüm raporu bu kayda eklenmedi.  
**SCT/bias devresi:** Kullanıcının bildirdiği mevcut devre breadboard üzerinde hazırlanmış bias alt devresidir: 2 × 10 kΩ dirençle orta nokta ve orta noktadan GND'ye 104 (100 nF) kondansatör. 8 kanallı analog arayüz kartı mevcut değildir. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır. SCT AC sinyalinin bias noktasına kuplajı ve ESP32 dahili ADC girişindeki güvenli aralık belgelenmeli. GPIO/pin numarası firmware/pin planlama aşamasında belirlenecek; T001’de pin seçimi şartı değil.  
**SCT/PZEM etiketleme ve kalibrasyon hedefi:** [Hedef mimari notu](docs/architecture/sct-pzem-labeling-and-calibration.md) — zaman damgası/sabit süre odaklı değil, paket bağlamı ve PZEM/SCT kararlı alanlarını algoritma-istatistikle belirleyip etiketleme; Python'da etiketli SCT verisiyle sensör başına katsayı/`f(x)` modeli çıkarma; ardından modeli çok paketli ham akışta sınayıp gerekirse iyileştirme. Firmware, algoritma ve deneyler henüz yapılmadı.  
**SSR:** SAMM Market 5 V, 2 kanallı kart; tedarikçi kodu İzmo9659, SKU MP02637. Giriş mantığı ve kart üzerindeki SSR'nin tam kodu doğrulanmalı.  
**RTC:** İki DS3231 modülünde de 2032 tipi pil bulunduğu kullanıcı beyanıdır. Kullanıcı RTC kodunun çalıştığını ve güç kesilip yeniden verildikten sonra saatin korunduğunu daha önce test ettiğini bildirdi. Bu beyanlar esas alınır; test tekrar istenmeyecek. Yüksek hızlı örnekleme zamanlaması ESP32 monoton zamanlayıcısına aittir.  
**Deney durumu:** YAPILMADI.

## Bildirilen stok

| Bileşen | Adet / özellik | Kaynak |
|---|---:|---|
| SCT013-030 (30 A / 1 V) | 7 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013-100A-1V | 10 | Kullanıcı bildirimi; jack çıkışlı |
| SCT013 toplamı | 17 | Kullanıcı bildirimi |
| ESP32-C3 SuperMini | 1 | Kullanıcı bildirimi / önceki SSR düğümü |
| ESP32 ölçüm düğümü | 1 | Kullanıcı bildirimi / önceki PZEM düğümü |
| PZEM-004T | V3.0 | Kullanıcı bildirimi |
| Masaüstü güç kaynağı | 5 V / 1,8 A | Kullanıcı bildirimi |
| Test yükleri | 100 W ve 150 W ampuller ana deney yükleri; 5 W LED ampul farklı PF için | Kullanıcı bildirimi; gerçek güç, akım ve PF ölçümle doğrulanacak |
| Breadboard bias alt devresi | 2 × 10 kΩ, orta nokta; orta noktadan GND'ye 104 (100 nF) | Kullanıcı bildirimi; hazırlanmış |
| Jack yuvaları ve bağlantı/ölçüm parçaları | Tam takım mevcut | Kullanıcı bildirimi |

## Mevcut bilgi
- Önceki BERO'daki SCT, PZEM, ESP32, MCP3208, SSR ve DS3231 teknik kaynakları proje referanslarına bağlandı.
- Bias üretim alt devresi, kullanıcının onayıyla tamamlandı sayılıyor; bağımsız voltaj ölçüm raporu eklenmedi.
- SCT013 sinyalinin breadboard bias devresi üzerinden ESP32'nin dahili ADC'sine alınması planlanıyor. 8 kanallı analog arayüz kartı mevcut değildir. MCP3208 sonraki aşamaya ayrılmıştır.
- PZEM için mevcut BERO kaydı kullanılıyor; bağlı CT modeli PZCT-02 (0–100 A) olarak belirtildi.
- SSR kartının tam giriş tetik mantığı ve fiziksel SSR parça kodu doğrulanmalı.
- Deneyler ve kalibrasyon sonuçları henüz eklenmedi.

## Karar kapıları
- [ ] G1 — SCT RMS kalibrasyonu hata hedefinde ve clipping yok.
- [ ] G2 — PZEM okuma durumu izleniyor; geçersiz okumalar özetlerden dışlanıyor.
- [ ] G3 — örnekleme hızı hedef yüklerde ölçülmüş metriklerle gerekçelendirilmiş.

## Sıradaki işler
1. [x] [T003 — PZEM tabanlı model hata hedefi](tasks/T003-reference-and-error-target.md): ±%4 bağıl sapma; Python geçerli örneklerde `OK` kararı verir.
2. [ ] [T004 — Analog ön uç](tasks/T004-analog-frontend.md): bias kuplajı ve güvenli ADC aralığı.
3. [ ] T005 — E01 gürültü tabanı: T004 tamamlandıktan sonra protokol ve ölçüm.

## Açık engeller
- SCT AC kuplajı, breadboard bias devresinin sinyal bağlantısı ve güvenli ESP32 ADC giriş aralığı belgelenmeli. Kullanılacak kartın ADC GPIO eşlemesi ve firmware ayarları pin planlama/kodlama aşamasında doğrulanmalı; bu T001 kapatma şartı değildir. Genel NodeMCU kartı kullanılacaksa PCB revizyonu kablolama öncesi belirlenmeli.
- SCT AC sinyalinin breadboard bias noktasına kuplajı ve güvenli ESP32 ADC giriş aralığı.
- SSR'nin hangi iki AC yükü anahtarlayacağı, GPIO eşlemesi ve giriş mantığının düşük gerilimde doğrulanması.
- T003 TAMAMLANDI: model tahmini geçerli PZEM akımından ±%4 bağıl sapma içindeyse Python sonucu `OK` işaretler. Kararlı alan gözlemi ve SCT istatistikleri ayrı görev/deneylerde ele alınır. Test yükleri ilgili test kaydında beyan edilecek.

Firmware, deney ve kalibrasyon sonuçları henüz eklenmedi.
