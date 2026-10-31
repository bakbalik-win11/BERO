# LOAD-150W-001 — SCT-1 uzun log analizi

- Tarih: 2026-10-31
- Kaynak log: kullanıcının yüklediği `esp32d1-logs (36).txt`
- Kaynak dosya boyutu: 211,455 bayt
- Kaynak SHA-256: `a407bc3363a804a4a72c06e0163119d3fac2243e8c802a7ff781038f699bdb4e`
- Log zaman aralığı: 16:31:30.179–16:44:32.407 (+03:00)
- Akım yayın aralığı: 16:31:31.121–16:44:31.092 (+03:00)
- Test kimliği: LOAD-150W-001. Dosya 35'teki 133 ölçümün tamamı bu logun başında aynen bulunduğundan dosya 36 aynı testin uzatılmış kaydıdır; yeni test olarak sayılmamıştır.

## Test düzeneği

- Yük: 150 W akkor ampul.
- ESP/modül: ESP32D1 / BERO Modül 2.
- SCT kanalı: SCT-1, sarı kablo, GPIO32 / ADC1_CH4.
- Ortak bias: turuncu kablo, GPIO35 / ADC1_CH7.
- Besleme: masaüstü harici 5 V güç kaynağı (kullanıcı bildirimi).
- ESPHome: 2026.10.1; ESP32 rev3.1.
- ADC attenuation: 12 dB; SCT ve bias ADC entity güncellemesi 1 s.
- ct_clamp: 200 ms örnekleme penceresi; 2 s yayın aralığı.
- K katsayısı: 24.22; test sırasında değiştirilmedi.
- Wi-Fi RSSI: yaklaşık -54 dB.

## UNIT referansı ve kabul bandı

Kullanıcının aynı yük için bildirdiği UNIT okumaları 0.598 A ve 0.599 A'dır.

- Geçici UNIT referans ortalaması: **0.5985 A**
- ±4% alt sınır: **0.57456 A**
- ±4% üst sınır: **0.62244 A**

Bu kıyas UNIT kullanıcı bildirimi referanslıdır. Logda PZEM ölçümü yoktur; sonuç PZEM doğrulaması değildir.

## Akım sonuçları — 391 yayın

| İstatistik | Sonuç |
|---|---:|
| Yayın sayısı | 391 |
| Ortalama | 0.6082148 A |
| Medyan | 0.608 A |
| Minimum–maksimum | 0.591–0.655 A |
| Örnek standart sapma | 0.006595 A |
| UNIT referansına ortalama sapma | +1.6232% |
| UNIT referansına medyan sapması | +1.5873% |
| ±4% bandındaki yayın | 388/391 = 99.23% |

Bandın dışındaki üç yayın:
- 16:32:11.126 — 0.624 A
- 16:32:57.122 — 0.655 A
- 16:41:23.103 — 0.626 A

258 yeni yayından oluşan devam bölümünde ortalama 0.6083605 A, medyan 0.609 A; 257/258 yayın UNIT ±4% bandındadır.

## Analog ve çalışma gözlemleri

| Alan | Yayın | Ortalama | Min–maks |
|---|---:|---:|---:|
| Raw AC | 391 | 0.0251121 V | 0.02438–0.02704 V |
| Ortak bias ADC | 783 | 1.6636003 V | 1.615–1.673 V |
| SCT-1 ADC Voltage | 782 | 1.661110 V | 1.615–1.700 V |

- ct_clamp raporlanan örnekleme hızı: 391 pencere; 16,970–17,885 SPS; ortalama yaklaşık 17,411 SPS.
- Üç adet derleyici/optimizasyon `[W]` uyarısı görüldü.
- `[E]` hata, brownout veya yeniden başlatma işareti görülmedi.
- SCT-1 ADC gerilim aralığı bias ADC aralığından daha geniştir; tek başına arıza kanıtı değildir.

## Teknik yorum ve karar

1. Bu 150 W oturumunda SCT-1 akım yayınının UNIT geçici referansıyla uyumu yüksektir: 391 yayının 388'i (%99.23) ±4% bandındadır.
2. Ortalama sapma +1.62%'dir.
3. **K=24.22 değiştirilmedi.** Bu veri seti için katsayı ayarı önerilmiyor.
4. Bu test PZEM ile eşzamanlı doğrulama değildir. PZEM daha sonraki aşamada ayrı referans kaydı olarak eklenecektir.
5. Bu sonuç yalnız belirtilen yük, kanal, besleme ve test oturumu için geçerlidir; diğer yük/kanal koşullarına genellenmez.

## Kanıt ve eksikler

- Ölçüm istatistikleri: kullanıcı tarafından sağlanan cihaz logundan çıkarım (LOG).
- UNIT 0.598 A ve 0.599 A: kullanıcı bildirimi (KULLANICI BİLDİRİMİ).
- Sapma ve bant içi oran: log ölçümleri ve UNIT bildirimi üzerinden hesap (HESAP).
- PZEM değeri: bu logda mevcut değil.
- ESP 5 V giriş rayı ve 3.3 V regülatör çıkışı doğrudan ölçülmedi.
- Ham logun bu arşivleme adımında GitHub'a tam metin olarak aktarılması mümkün olmadı; özgün dosya adı, boyutu ve SHA-256 özeti burada kayıt altına alındı. Tam ham dosyanın ayrıca `logs/module2/` içine eklenmesi açık arşiv işidir.

## Sonraki adım

150 W yük testi arşivlendi. Sonraki ayrı deney, SCT bağlı ve primer akımı olmayan **boşta okuma** olacak. Boşta kayıt sırasında mevcut akım hesabına yazılımsal sıfır eşiği eklenmeyecek; taban dağılımı ölçülecek. Bu testte yük akımı yok koşulu fiziksel olarak sağlanıp ayrıca not edilecek.
