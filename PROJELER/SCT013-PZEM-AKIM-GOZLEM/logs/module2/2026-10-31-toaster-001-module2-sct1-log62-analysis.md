# TOASTER-001 — Log 62 teknik analiz

- **Tarih:** 2026-10-31
- **Kaynak:** `esp32d1-logs (62).txt`
- **Ham arşiv:** [Log 62 tam metin](2026-10-31-toaster-001-module2-sct1-log62-full.txt)
- **Kaynak boyutu:** 68.572 bayt; 934 satır; 68.564 UTF-8 karakter.
- **SHA-256:** `4790b00e69aaba791339f6d43aa13041efe373c5a87b9ed7fd4c1f481ce551f2`
- **Cihaz/yazılım:** ESP32D1, ESP32 rev3.1, ESPHome 2026.10.1.
- **Kanal:** Modül 2 / SCT-1 / GPIO32 ADC1_CH4; ortak bias GPIO35 ADC1_CH7.
- **Örnekleme/işleme:** ADC 12 dB / 1 s; ct_clamp 200 ms pencere / 2 s yayın; K=24.22.
- **Kullanıcı referansı:** UNIT 7,89 A bildirimi. PZEM değildir; zaman örtüşmesi doğrulanmamıştır.

## HEDEF
Tost makinesinin yüksek akım bölgesinde mevcut K=24.22 ile SCT-1 davranışını gözlemek. Katsayıyı değiştirmek veya kalibrasyon yapmak bu testin hedefi değildir.

## LOG — kararlı ON bölgesi
İlk 119 SCT akım yayını 21:52:30.185–21:56:26.262 aralığında yaklaşık 236,1 saniyelik bir kararlı bölüm oluşturuyor. Sonraki tek düşük yayın bu istatistiklerden ayrı tutuldu.

| Ölçüt | Sonuç |
|---|---:|
| Yayın sayısı | 119 |
| Ortalama SCT akımı | 7,1900 A |
| Medyan | 7,188 A |
| Min–maks | 7,135–7,264 A |
| Örnek standart sapma | 0,0247 A |
| CV | %0,344 |
| Raw AC ortalaması | 0,29686 V |
| Raw AC min–maks | 0,29461–0,29991 V |
| GPIO35 bias ortalaması | 1,66391 V |
| SPS ortalaması | 18.561 |

## LOG — son geçiş örneği
21:56:28.190 zamanında SCT yayını 6,096 A; hemen önceki yayın 7,208 A. Raw AC aynı geçişte 0,29759 V'tan 0,25169 V'a indi. Bu tek örnek kararlı pencereye dahil edilmedi. Tek başına termostat OFF çevrimini kanıtlamaz; sonraki loglarda geçişin tekrarı aranmalıdır.

## HESAP — UNIT ile betimleyici fark
UNIT 7,89 A kullanıcı bildirimiyle SCT kararlı ortalaması arasındaki aritmetik fark yaklaşık −%8,87; medyan farkı yaklaşık −%8,90'dır. Ancak UNIT ölçümünün aynı zaman penceresinde alındığı doğrulanmadığı için bu fark eşzamanlı doğruluk sapması veya kalibrasyon sonucu değildir. Logda PZEM verisi yoktur.

## SONUÇ
- Mevcut K=24.22 ile yaklaşık 7,19 A seviyesinde SCT yayını dar dağılım göstermiştir (CV %0,344).
- UNIT 7,89 A ile aritmetik fark kayda değerdir; fakat zaman eşleşmesi olmadığı için doğruluk yorumu yapılamaz.
- Son 6,096 A örneği ayrı geçiş adayıdır; termostat çevrimi olarak sınıflandırılmamıştır.
- K=24.22 ve firmware değiştirilmedi; katsayı değişikliği önerilmez. Bu çalışma yüksek akım karakterizasyonudur.
- PZEM ölçümü ve eşzamanlı UNIT zaman damgası bulunmamaktadır.

## KANIT / SINIR
- Ham kaynak tam olarak GitHub'a arşivlendi; SHA-256 yukarıda verilmiştir.
- Log başlangıcında ESPHome bağlantısı ve ADC/ct_clamp başlatma bilgileri görülür. Üç framework optimizasyon önerisi ölçüm hatası olarak yorumlanmamıştır.
- Bu tek log termostat davranışını, cihazın uzun dönem çevrimini veya genel yüksek akım doğruluğunu doğrulamaz.
