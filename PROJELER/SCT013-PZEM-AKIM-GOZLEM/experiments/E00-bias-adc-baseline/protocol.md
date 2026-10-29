# E00 — Bias noktasını ADC ile okuma (SCT bağlı değil)

## Amaç
İlk donanım/yazılım basamağı: SCT013 bağlamadan, yalnız bias orta noktasını ESP32'nin ADC destekli GPIO'suna bağlayıp iki API'nin çıktısını anlamak:
- `analogRead(pin)`: ham ADC sayısı.
- `analogReadMilliVolts(pin)`: milivolt cinsinden tahmini giriş gerilimi.

Bu deney akım ölçümü veya gürültü tabanı deneyi değildir.

## Düzenek
- Bias devresi ve ESP32'nin GND'si ortak olmalı.
- Bias orta noktası → seçilecek ESP32 ADC GPIO'su.
- SCT013 bu deneyde bağlı olmayacak.
- Voltmetre aynı bias noktasında yaklaşık 1,65 V gösterdiği varsayılabilir; bu yalnız örnek varsayımıdır, BERO ölçüm sonucu değildir.
- ESP32 kart modeli ve ADC GPIO'su gerçek donanıma göre kaydedilmelidir. GPIO34 her ESP32 modelinde bulunmaz; ESP32-C3'te GPIO34 yoktur.
- ADC pinine güvenli giriş aralığını kartın teknik özelliklerine göre doğrula; pinine 3V3 üstü gerilim uygulama.

## Basit örnek kod
```cpp
const int ADC_PIN = /* seçilen ADC GPIO */;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  // Kart/Arduino-ESP32 sürümünün desteklediği ADC zayıflatma ayarı
  // seçilen pine ve karta göre ayrıca belirlenir.
}

void loop() {
  int raw = analogRead(ADC_PIN);
  uint32_t mv = analogReadMilliVolts(ADC_PIN);

  Serial.printf("raw=%d | voltage=%lu mV (%.3f V)\n",
                raw, (unsigned long)mv, mv / 1000.0);
  delay(500);
}
```

Kodda gerçek ADC pini ve uygun attenuation ayarı seçilmeden derlenip çalıştırılmaya hazır olduğu varsayılmamalıdır.

## Ham sayı nasıl anlaşılır?
12 bit çözünürlükte ham sayı aralığı nominal olarak 0–4095'tir. İdeal, doğrusal 0–3,3 V dönüştürücü varsayımında 1,65 V için kaba teorik hesap:
`1.65 / 3.3 × 4095 ≈ 2048`.
Bu yalnız açıklayıcı ideal hesaptır. ESP32 ADC gerçek ölçümünde attenuation, çip modeli, doğrusal olmama ve kalibrasyon nedeniyle gerçek ham değer 2048 olmak zorunda değildir. `analogRead()` değeri yazılımın ölçerek döndürdüğü ham sayıdır; 2048 sabitini koda yazmayız.

`analogReadMilliVolts()` kalibrasyon desteğiyle voltaj karşılığı döndürür; hassas voltmetre sonucu garantilemez.

## Prosedür
1. SCT bağlı değilken bias noktasının voltajını voltmetreyle ölç ve kaydet.
2. ESP32 kart modelini, firmware/Arduino-ESP32 sürümünü, GPIO'yu ve attenuation ayarını kaydet.
3. Aynı döngüde ham ADC ve milivolt çıktısını seri porta yazdır.
4. En az 30 saniye örnek kaydet; ham sayının ve mV değerinin değişip değişmediğine bak.
5. Voltmetre, ham ADC ve mV okumalarını karşılaştır. Ham sayıyı voltaja dönüştürmek için kaba teorik eşitliği gerçek kalibrasyon gibi sunma.

## Kabul ölçütü
SCT bağlı olmadan iki fonksiyonun çıktısı aynı örnek döngüsünde alınmış; kullanılan donanım/ayarlar ve gözlenen değerler kaydedilmiş olmalı. Deney çalıştırılmadan sonuç yazılmaz.

## Durum
PLANLANDI. Donanımda henüz ölçüm yapılmadı.
