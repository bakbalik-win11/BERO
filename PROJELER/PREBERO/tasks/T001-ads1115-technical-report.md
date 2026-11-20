# T001 — ADS1115 hobi düzeyinde teknik raporu

- **Durum:** AKTİF
- **Amaç:** ADS1115'i BERO'daki SCT akım okuma uygulaması için anlayacak kadar tanımak.
- **Çıktı:** Kaynaklı, BERO kullanımına bağlı teknik rapor: [ADS1115-TEKNIK-RAPOR.md](../docs/ADS1115-TEKNIK-RAPOR.md).

## İncelenecek başlıklar
1. ADC ve delta-sigma dönüşümün pratik açıklaması.
2. 16 bit çözünürlük ve PGA aralığına göre LSB hesabı.
3. Single-ended/diferansiyel ölçüm.
4. MUX, negatif diferansiyel sonuç ve common-mode.
5. PGA'nın ölçüm aralığına etkisi; fiziksel yükselteç olmaması.
6. 8–860 SPS veri hızları ve dönüşüm davranışı.
7. Besleme, AIN GND–VDD çalışma aralığı ve mutlak maksimumlar.
8. Bias ihtiyacının SCT sinyalindeki rolü.
9. ESP32 I²C bağlantısı ve 3.3 V lojik uyumu.

## Kabul ölçütü
TI veri sayfasına dayalı açıklama; negatif diferansiyel sonuç ile AIN pininin GND altına inmesini açıkça ayırma; bilinmeyen fiziksel bağlantılar hakkında varsayım yapmama. Laboratuvar seviyesinde kapsamlı karakterizasyon yok.
