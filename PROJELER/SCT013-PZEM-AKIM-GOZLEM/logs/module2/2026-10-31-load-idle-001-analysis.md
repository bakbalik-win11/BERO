# LOAD-IDLE-001 — Modül 2 yüksüz SCT-1 ilk log analizi

- TEST ID: LOAD-IDLE-001
- Senaryo: Modül 2 / yüksüz (boşta) okuma. Bağımsız test senaryosudur; yük testlerinden ayrı tutulur.
- Kaynak: Yapıştırılan metin(20261031-135010).txt
- Boyut: 36.687 bayt; 514 satır.
- SHA-256: 9ac3ece0770a85219e7ad6664f15f1ccc9db9b561d04f6195ef034d4e718e455
- Zaman: İlk akım yayını 16:47:55.066, son akım yayını 16:49:53.052 (+03:00); yaklaşık 1 dk 58 sn.
- Düzenek: ESP32D1 / Modül 2 / SCT-1 GPIO32 ADC1_CH4; ortak bias GPIO35 ADC1_CH7. ESPHome 2026.10.1; ESP32 rev3.1. ADC 12 dB, samples 1, update 1 s. ct_clamp 200 ms, update 2 s. Wi-Fi RSSI −54 dB.
- UNIT/PZEM: Yüksüz senaryoda UNIT referansı aranmadı. Logda PZEM verisi yok.
- K: Değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.

## Akım sonuçları

60 adet akım yayını:
- Ortalama 0,011267 A
- Medyan 0,000 A
- Min–maks 0,000–0,104 A
- Örnek SD 0,025876 A
- Tam sıfır: 48/60 (%80,0)
- Sıfır dışı: 12/60 (%20,0)

Sıfır dışı yayınlar (A): 0,051; 0,085; 0,103; 0,014; 0,060; 0,025; 0,039; 0,047; 0,104; 0,066; 0,042; 0,040. Bu değerlerin kaynağı (gerçek primer akımı, girişim veya ölçüm zinciri davranışı) yalnız bu logla ayrıştırılamaz.

## Analog gözlem

| Entity | Yayın | Ortalama | Min–maks |
|---|---:|---:|---:|
| Raw AC | 60 | 0,0004657 V | 0,00000–0,00428 V |
| Common Bias GPIO35 | 118 | 1,663881 V | 1,652–1,678 V |
| SCT-1 ADC GPIO32 | 118 | 1,662508 V | 1,652–1,673 V |

Bias ve SCT ADC yayınları 1 saniyelik ayrı güncellemeler olduğundan birebir eşzamanlı çiftler olarak ele alınmadı.

## Örnekleme ve cihaz durumu

- ct_clamp DEBUG SPS: 17.465–18.280; ortalama yaklaşık 17.971 SPS. Bu, ESPHome logunun raporladığı değerdir; bağımsız ölçüm değildir.
- GPIO32 ve GPIO35 ADC başlatma/konfigürasyon/kalibrasyon durumları OK.
- Üç derleyici/optimizasyon uyarısı var; [E] hata, brownout veya reboot işareti yok.

## Teknik yorum

1. 60 akım yayınının %80'i 0,000 A; yüksüz durumda çoğunlukla sıfır okuma doğrudan gözlendi.
2. Kalan %20'de 0,014–0,104 A aralığında düşük sıfır dışı yayınlar var. Bu değerler silinmedi veya eşikle bastırılmadı.
3. Bias ve SCT-1 ADC ortalamaları yaklaşık 1,66 V seviyesinde ve birbirine yakın.
4. Yaklaşık iki dakikalık tek kayıt, ilk yüksüz taban gözlemidir; kalıcı eşik veya katsayı kararı için yeterli değildir.
5. K değiştirilmedi; yazılımsal sıfır eşiği eklenmedi.

SONUÇ: LOAD-IDLE-001 ilk logu analiz edildi. %80 sıfır yayın ve %20 düşük sıfır dışı yayın gözlendi. Test senaryosu açık kalır; sonraki yüksüz kayıtlar bu tabanla karşılaştırılacaktır.
