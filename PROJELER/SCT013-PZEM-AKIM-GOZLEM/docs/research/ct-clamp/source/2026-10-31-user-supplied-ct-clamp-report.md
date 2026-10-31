# ESPHome ct_clamp iç çalışma raporu

**BERO E00F – SCT013-030 / ESP32 / GPIO33 ölçüm zinciri analizi**

> Bu dosya, kullanıcının yüklediği dört sayfalık DOCX raporunun metin aktarımıdır. İçerik ve raporun kendi varsayım/uyarıları korunmuştur; biçim Markdown'a dönüştürülmüştür. Kaynak dosya 9.547 bayt, SHA-256: `cfb2d76f64a93efd8d80e0005c6e80b974d9086e77b72f61542898aa03f88a05`.

Kaynak: ct_clamp_sensor.cpp, ESPHome 2026.10.1 API belgesi (satır numaraları buna göre). Sayısal örneklerin bir kısmı sandbox simülasyonudur, BERO ölçümü değildir. Varsayımlar: LSB ≈ 0,75 mV (tahmin), ADC gürültüsü 0,3–2 mV, 5 kSPS civarı. Bölüm 9'un sonu, kaynak mesajın kesilmesi nedeniyle kendi çıkarımımla tamamlandı.

## 1. Ölçüm zinciri

| Aşama | Giriş → Çıkış | Birim | Tipik değer |
|---|---|---|---|
| SCT013-030 (iç burden dahil) | Primer akım → AC gerilim | A → V RMS | Nominal 30 A → 1 V (33 mV/A). 24,22 katsayısı ≈ 41 mV/A öngörüyor |
| Bias devresi (2×10 kΩ + 100 nF) | AC gerilim → ~1,65 V DC üzerine bindirilmiş AC | V | 0,447 A: 1,65 V ± 26 mV tepe |
| ESP32 ADC (GPIO33, 12 dB) | Analog gerilim → 12 bit sayı | V → count | ≈ 2200 count (bias) ± 35 count |
| ESPHome ADC sensörü (raw: false) | Kalibre mV → volt | V | Örn. 1,653 V, 1 mV basamaklı |
| ct_clamp loop/update | V örnekleri → standart sapma | V | 0,447 A: ≈ 0,0185 V |
| Filtreler (multiply, lambda) | V → A | A | 0,0185 × 24,22 ≈ 0,447 A |

SCT013-030'un 1 V'luk sürümünde burden iç olduğu için harici burden direnci yok. 24,22 ile nominal 30 arasındaki yaklaşık %24 fark (sensör toleransı, ADC kalibrasyonu, bias) henüz açıklanmış değil.

## 2. Kaynak kod gezintisi

- setup() yok. Dosyada yalnızca dump_config (11–15), update (17–51) ve loop (53–70) var. Hiçbir ADC hazırlığı ct_clamp'te yapılmıyor.
- update() yalnızca başlatıcı. Yorum satırı: "Update only starts the sampling phase, in loop() the actual sampling is happening."
  - Satır 21: high_freq_.start(), ana döngüyü gecikmesiz çalıştırır.
  - Satır 24: set_timeout("read", sample_duration_, …) ile bitiş zamanlayıcısı.
  - Satır 46–50: last_value_, num_samples_ ve iki toplam sıfırlanır, is_sampling_ = true.
- Zamanlayıcı geri çağrısı (25–43): örneklemeyi kapatır, high_freq_.stop(). num_samples_ == 0 ise publish_state(NAN). Aksi halde sırasıyla:
  - rms_ac_dc_squared = sample_squared_sum_ / num_samples_ (34)
  - rms_dc = sample_sum_ / num_samples_ (35)
  - rms_ac_squared = rms_ac_dc_squared − rms_dc² (36)
  - Pozitifse karekök, değilse 0 (37–39)
  - Debug log (40–41), publish_state(rms_ac) (42)
- loop() (53–70): is_sampling_ değilse hemen çıkar (54–55). source_->sample() bir kez çağrılır (58). NaN atlanır (59–60). Önceki kabul edilen değerle aynıysa atlanır (63–64). Aksi halde N, Σv ve Σv² güncellenir (67–69).
- Değişkenler: sample_sum_ ve sample_squared_sum_ float, num_samples_ uint32_t (header 46–48). VoltageSampler::sample() volt döner.

## 3. RMS ayrıntısı

`σ = √( (1/N)·Σvᵢ² − ((1/N)·Σvᵢ)² )`, vᵢ yalnızca ardışık olarak farklı kabul edilen örnekler.

- Bias çıkarma: sabit değer yok. Pencere ortalaması varyans özdeşliğiyle çıkarılıyor. Bias kayması pencere içinde sabitse sorun çıkmaz.
- Mutlak değer: kullanılmıyor.
- Kare ortalaması: evet.
- Örnek sayısı: çalışma anında belli, kaynakta yok. Log satırı veriyor.
- Ağırlık: her kabul edilen örnek eşit ağırlıklı, ama zamanda eşit aralıklı değil. Dedup ve döngü süresi yüzünden ağırlık zamana göre bozuluyor. Çıktı, gerçek zaman ağırlıklı RMS'ten farklı olabilir.

## 4. sample_duration analizi

Pencere x periyot ise, tam sayı olmadığında en kötü durumda göreli RMS hatası yaklaşık 1/(4π·x) (kendi türetmem). x tam sayıysa hata sıfır. Gerçek pencere zamanlayıcı ve döngü gecikmesi yüzünden tam 200 ms değil. 1 ms sapma yaklaşık %0,1 etki eder.

| Süre | 50 Hz periyot | En kötü kesir hatası | Zaman çözünürlüğü | Float32 riski (N ile büyür) |
|---|---:|---:|---|---|
| 100 ms | 5 | ≈ %1,6 | En iyi | En düşük |
| 200 ms | 10 | ≈ %0,8 | İyi | Düşük |
| 500 ms | 25 | ≈ %0,3 | Orta | Orta |
| 1 s | 50 | ≈ %0,16 | Kötü, olayları ortalar | En yüksek |

Uzun pencere kesir hatasını azaltır ama float32 hatası ve CPU yükü (2 s'de %50) artar. 200 ms bu açıdan makul bir orta nokta.

## 5. update_interval ilişkisi

Sürekli örnekleme yok. Kodla kanıt:

- is_sampling_ yalnızca update() içinde (50) true yapılıyor, zamanlayıcı bitince (25) false.
- loop() satır 54–55'te false iken hemen dönüyor, yani hiç sample() çağrılmıyor.
- high_freq_.stop() (26) döngüyü normal hıza döndürüyor.

200 ms / 2 s için: aradaki 1,8 s'de ADC okunmuyor. Görev oranı %10. Sonuç: ölçüm kısa olayları kaçırabilir ve her yayın yalnızca o 200 ms'lik anlık görüntü. PZEM ile eşleştirmede kararlı pencere aranmasının nedeni bu.

update_interval < sample_duration olursa aynı isimli "read" zamanlayıcısı ve sıfırlama (46–50) devreye girer. ESPHome'un aynı isimli zamanlayıcıyı değiştirdiğini genel bilgiyle varsayıyorum, burada doğrulamadım. Mevcut ayarda bu durum yok.

## 6. ESP32'ye özel

- Çözünürlük: 12 bit, 12 dB'de LSB ≈ 0,75 mV (tahmin). Espressif ESP32 için 11 dB'de önerilen aralığı 150–2450 mV olarak veriyor. 1,65 V bias bunun içinde.
- Kalibrasyon: line-fitting, varsayılan Vref 1100 mV (adc_sensor_esp32.cpp ~95–112). Çıktı tam sayı mV (186–190).
- Gürültü: Espressif kondansatör ve çoklu örneklemeyi öneriyor. samples: 1 bunu kullanmıyor.
- Ofset: kalibrasyon mutlak ofseti düzeltir ama ct_clamp mutlak değer kullanmıyor, yalnızca değişimi ölçüyor. DC ofseti asıl sorun değil.
- Düşük genlik: 0,1 A için tepe yalnızca ~6 mV ≈ 8 LSB. Çözünürlük, gürültü ve dedup orada belirleyici.

## 7. Düşük akım (0,1–0,5 A)

Beklenen sinyal: 0,1 A → 4,1 mV RMS (5,5 LSB), 0,5 A → 20,6 mV (27 LSB). Simülasyon (5 kSPS, %15 jitter), her faktör ayrı:

| Akım | Yalnızca kuantizasyon | +1 mV gürültü | +2 mV gürültü | 2 mV bias kayması/pencere | float32 | Dedup |
|---|---:|---:|---:|---:|---:|---:|
| 0,1 A | 0,099 | 0,102 | 0,111 | 0,101 | 0,026 ± 0,022 | 0,099 |
| 0,2 A | 0,198 | 0,201 | 0,207 | 0,201 | 0,191 ± 0,004 | 0,188 |
| 0,5 A | 0,499 | 0,500 | 0,503 | 0,500 | 0,504 | 0,452 |

Yorum:

- Kuantizasyon: düşük etki (≤ %1,5).
- Gürültü: kuadratik toplanır. 2 mV gürültü 0,1 A'da +%11, 0,5 A'da +%0,7.
- Bias kayması: pencere içindeki lineer kayma standart sapmaya yalnızca ikinci dereceden girer. Küçük etki.
- Burden seçimi: SCT013-030'un burden'ı iç ve sabit, müdahale alanı yok.
- Örnek sayısı: float32 hatasını N büyütür. Dedup oranı örnekleme hızına bağlı.
- RMS yöntemi: float32 + cancellation 0,1 A'da dominant çıktı, 0,2 A'da küçük, 0,5 A'da zayıf. Dedup ise 0,5 A'da bile −%10 gösterdi, ama gerçek hız bilinmiyor.

Önemli ek bulgu: Boştaki Raw AC'nin 0,006–0,009 V olması gerçek analog gürültü olmayabilir. Aynı sandbox'ta, sıfır sinyalle (yalnızca 0,4 mV gürültü) float32 hesabı bazı N değerlerinde 0,005–0,0065 V yapay taban üretti, bazılarında sıfır. Bu, N'e bağlı bir hesap artefaktı. Henüz BERO'da kanıtlanmadı, ama D1 yüksüz kaydında "Raw AC, N ile birlikte 0 ile ~0,006 V arasında zıplıyor mu?" bakışıyla doğrudan test edilebilir.

## 8. Yüksek akım (3, 8, 10 A)

- Lineer beklenir mi? Kod lineer (σ gerilimle ölçeklenir). Simülasyonda 3, 8, 10 A'da float32 hatası ≤ %0,1.
- Doğrusallığı bozabilecek: dedup (3 A'da −%1,2, 8 A'da −%0,5 civarı), ADC eğrisi ve SCT çekirdek doğrusallığı (ölçülmedi).
- Doyum: tepe gerilim 3 A: 0,17 V, 8 A: 0,47 V, 10 A: 0,58 V. Bias üstünde ≈ 2,24 V'a kadar çıkar, 2,45 V önerilen üst sınırın altında. Önerilen sınıra yaklaşım yaklaşık 13,5 A RMS (bu duyarlılıkla, hesabım). Kettle 6,39 A için tepe ≈ 2,03 V, doyum yok.
- Kettle −%3,8: ADC doyumu değil. Adaylar: dedup (sim'de 20 kSPS'te yaklaşık −%3,5, işaret ve büyüklük uyumlu), ADC eğrisi, PZEM tarafı. Hiçbiri kanıtlı değil.

## 9. Gerçek sistem için yorum

Beklenen sınırlamalar: %10 görev oranı, düzensiz örnekleme, dedup kaynaklı genliğe bağlı sapma, float32 kaynaklı düşük akım kararsızlığı, N ve gerçek okuma sayısının görünmemesi, tek katsayı.

Güvenilir akım bölgesi (çıkarım):

| Bölge | Beklenti | Dayanak |
|---|---|---|
| < 0,1 A | Güvenilmez | float32/gürültü/yuvarlama; simülasyon + boş taban gözlemi |
| 0,1–0,3 A | Belirsiz, değişken | Simülasyon; ölçülmedi |
| 0,3–~10 A | ±%4 civarı | Kullanıcı ölçümleri: 0,447 A %0, 0,616 A −%0,2, 0,637 A +%3, 6,39 A −%3,8 |
| > ~13 A | Bilinmiyor | ADC önerilen aralığa yaklaşım |

0,35 A eşiği "belirsiz" bölgenin içinde. Bu, eşiğin keyfi olmadığını gösteriyor, ama LED'i (0,041 A) kesin gizliyor.

Test önerisi: D1'de Raw AC, N ve SPS'i birlikte kaydedin. Taban N'e göre değişiyorsa hesap artefaktı, N'den bağımsız sabitse analog kaynaklı demektir.
