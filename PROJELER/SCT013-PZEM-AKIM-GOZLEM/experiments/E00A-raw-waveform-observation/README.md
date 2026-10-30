# E00A — Bias trafosu çıkışı ve Vmid ADC gözlemi

## Amaç
SCT bağlanmadan, bias trafosunun iki DC noktasını ESP32-WROOM-32D dahili ADC'siyle ayrı ayrı gözlemek:
1. Bias trafosunun L78L33 regülatör çıkışı: nominal 3,3 V DC.
2. 2 × 10 kΩ bias bölücüsünün orta noktası: nominal yaklaşık 1,65 V DC (Vmid).

Her iki noktada ADC ham sayısı, `analogReadMilliVolts()` sonucu ve zaman içindeki değişim kaydedilir. Multimetre ölçümü karşılaştırma referansı olarak ayrıca LOG'a yazılır. Bu adım SCT ölçümü değildir; akım hesabı/kalibrasyon da değildir.

## Güvenli ADC bağlantısı
GPIO34'e nominal 3,3 V hattını doğrudan bağlamak bu deney için uygun değildir: ADC'nin ölçüm aralığının üst ucuna dayanabilir ve küçük bir besleme yükselmesi doygunluk/ölçüm hatası oluşturabilir. İlk koşulda L78L33 çıkışı, ADC giriş aralığına uygunluğu doğrulandıktan sonra **ayrı/geçici 10 kΩ / 10 kΩ ölçüm bölücüsü** üzerinden GPIO34'e uygulanır. Bu bölücü bias trafosunun parçası değildir; yalnız 3,3 V çıkışı ADC için ölçekleyen ölçüm aparatı olarak planlanmıştır. Bölücü orta noktası ADC'ye, alt 10 kΩ GND'ye; üst 10 kΩ 3,3 V çıkışa bağlanır. Böylece ADC yaklaşık 1,65 V görür; yazılımda bu koşulun tahmini kaynak voltajı ADC pinindeki mV değerinin iki katı olarak raporlanır. Bu geçici ölçüm bölücüsü, bias devresinin kendi 2 × 10 kΩ Vmid bölücüsüyle karıştırılmamalıdır.

İkinci koşulda GPIO34 doğrudan bias Vmid noktasına bağlanır. Her iki koşulda bias trafosu GND'si ile ESP32 GND ortak olmalıdır. Bağlantılar enerji kesikken yapılır. Kartın gerçek modeli/pinout'u doğrulanmadan GPIO34 kullanılmaz. Multimetre ile 3,3 V ve Vmid gerçek değerleri kaydedilir. ESP32 ADC girişine 0 V altı veya kart besleme sınırını aşan gerilim uygulanmaz.

## Kapsam ve sıra
- A — L78L33 3,3 V çıkışı: ayrı/geçici 10 kΩ/10 kΩ ölçüm bölücüsü üzerinden ADC; bölücü henüz fiziksel olarak kurulmuş sayılmaz.
- B — Bias Vmid: yaklaşık 1,65 V orta nokta doğrudan ADC.
- SCT jack'i bağlı değildir; ölçülen hatta yük/akım deneyi yoktur.
- İlk gözlem penceresi koşul başına 30 saniyedir. Tek ESP32 kullanılacak; örnekleme hızı firmware aşamasında seçilip gerçekleşen hız ayrıca kaydedilecektir. 2 kS/s yalnız başlangıç hedefidir, doğrulanmış performans değildir. Hedef hız doğrulanmış performans değildir.
- Önce A kaydı ve kontrolü tamamlanır; bağlantı enerjisizken B'ye alınır, sonra B kaydı yapılır.

## Her kayıttan üretilecek çıktılar
- Ham ADC örnekleri: `sample_index,adc_raw` CSV; yerel diskte, varsayılan olarak Git dışında.
- Her örnek için ADC ham sayısı ve mV API'si karşılaştırması; ham CSV ayrı tutulur.
- Ortalama, minimum, maksimum, tepe-tepe aralığı ve standart sapma.
- Multimetre DC değeri, hedef hız, gerçek süre, örnek sayısı ve yaklaşık gerçekleşen örnekleme hızı.
- İki koşulun kısa karşılaştırması ve ADC-değer/zaman grafiği.

Bu istatistikler DC seviyesinin kararlılığını tanımlar; tek başına ADC doğruluğu veya hassas voltmetre performansı kanıtı değildir. `analogReadMilliVolts()` kalibrasyon destekli tahmindir; multimetreyle farkı kaydedilir.

## Durum
PLANLANDI. Firmware, fiziksel bağlantı, derleme ve ölçüm henüz yapılmadı.


## İlk donanım verisi — 2026-10-30

- **Kaynak:** Kullanıcı multimetre ile bias trafosunun L78L33 DC çıkışını ölçtü.
- **Ölçülen değer:** 3,31 V DC.
- **Kanıt etiketi:** KULLANICI BİLDİRİMİ (kullanıcının multimetre ölçüm raporu); bağımsız tekrar veya fotoğraf kaydı bu oturumda yok.
- **Sınır:** Bu değer ESP32 ADC ölçümü değildir. GPIO34 bağlantısı, ADC ham değerleri ve 30 saniyelik kayıt henüz yapılmadı.
