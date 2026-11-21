# Osiloskop Test Raporu – Yük Kademeleri / Biaslı SCT013

- **Tarih:** 2026-11-21
- **Görev:** MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları
- **Test durumu:** Osiloskop yük kademeleri tamamlandı; ADS1115 karşılaştırması bekliyor.
- **Sensör:** SCT013 30A/1V
- **Ölçüm:** Osiloskop CH1, bias bağlı, her yükte 6 ayrı Single yakalama.
- **Amaç:** SCT sekonder sinyalinin yükle değişimini görmek; tekil Vrms dağılımını ve ortalamaları nominal SCT beklentisiyle karşılaştırmak.
- **Önemli sınır:** Bu test ADS1115 ölçümü değildir. PZEM akım kayıtları bu rapora dahil değildir.

## 1. Test koşulları

Bias bağlantısı bütün yük kademelerinde korunmuştur. Yüksüz durum ayrı kayıt olarak tutulmuştur; yük eğrisi ve nominal yük karşılaştırmasına dahil edilmemiştir.

42 W ve 57 W kademelerinde kullanıcı tarafından yalnızca altı Vrms değeri yapılandırılmış biçimde verilmiştir. 100 W ve 150 W kademelerinde beş osiloskop parametresi kaydedilmiştir. Verilmeyen alanlar tahmin edilmemiştir.

## 2. Tekil Vrms okumaları

Birim: mV RMS.

| Yük | Single 1 | Single 2 | Single 3 | Single 4 | Single 5 | Single 6 | Ortalama |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Yüksüz | 1.60 | 5.39 | 5.01 | 5.07 | 1.05 | 2.29 | 3.4017 |
| 42 W | 6.57 | 6.56 | 6.50 | 6.55 | 6.55 | 6.52 | 6.5417 |
| 57 W | 9.24 | 9.25 | 9.22 | 9.21 | 9.71 | 9.16 | 9.2983 |
| 100 W | 16.59 | 16.57 | 16.64 | 16.57 | 16.53 | 16.52 | 16.5700 |
| 150 W | 22.91 | 22.92 | 22.77 | 22.86 | 22.80 | 22.77 | 22.8383 |

## 3. 100 W – tam Single kayıtları

Avg değeri altı kayıtta +0.33 mV olarak sabit kaydedildi.

| Single | Vrms (mV) | Avg (mV) | Vp-p (mV) | Vmax (mV) | Vmin (mV) |
|---:|---:|---:|---:|---:|---:|
| 1 | 16.59 | +0.33 | 49.00 | +23.67 | -25.33 |
| 2 | 16.57 | +0.33 | 50.00 | +24.00 | -26.00 |
| 3 | 16.64 | +0.33 | 49.00 | +24.33 | -24.67 |
| 4 | 16.57 | +0.33 | 47.67 | +23.67 | -24.00 |
| 5 | 16.53 | +0.33 | 49.33 | +24.33 | -25.00 |
| 6 | 16.52 | +0.33 | 49.67 | +24.67 | -25.00 |

## 4. 150 W – tam Single kayıtları

Avg değeri altı kayıtta +0.33 mV olarak sabit kabul edildi.

| Single | Vrms (mV) | Avg (mV) | Vp-p (mV) | Vmax (mV) | Vmin (mV) |
|---:|---:|---:|---:|---:|---:|
| 1 | 22.91 | +0.33 | 69.33 | +35.00 | -34.33 |
| 2 | 22.92 | +0.33 | 67.67 | +32.00 | -35.67 |
| 3 | 22.77 | +0.33 | 66.00 | +31.67 | -34.33 |
| 4 | 22.86 | +0.33 | 69.67 | +33.00 | -36.67 |
| 5 | 22.80 | +0.33 | 65.00 | +32.00 | -33.00 |
| 6 | 22.77 | +0.33 | 67.00 | +32.33 | -34.67 |

## 5. Nominal beklentiyle ilk karşılaştırma

Ön değerlendirme için 220 V ve güç faktörü 1 olan dirençli yük varsayılmıştır.

SCT013 30A/1V nominal oranından:

`I = P / 220`

`V_{SCT} = I / 30`

| Yük | Nominal beklenti (mV) | Ölçüm ortalaması (mV) | Fark (%) |
|---:|---:|---:|---:|
| 42 W | 6.36 | 6.5417 | +2.8 |
| 57 W | 8.64 | 9.2983 | +7.6 |
| 100 W | 15.15 | 16.5700 | +9.4 |
| 150 W | 22.73 | 22.8383 | +0.5 |

Bu tablo yaklaşık teorik karşılaştırmadır; gerçek PZEM akımı yerine yük etiket gücü ve 220 V varsayımı kullanılmıştır. Gerçek kalibrasyon veya doğruluk sonucu değildir. PZEM değerleri geldiğinde ayrı karşılaştırma yapılmalıdır.

## 6. Gözlem ve yorum

- Yük arttıkça ölçülen Vrms ortalaması düzenli artmıştır.
- 42 W, 100 W ve 150 W kademelerinde altı ölçümün dağılımı dardır.
- 57 W serisinde 9.71 mV tekil değer, diğer beş ölçümden yüksektir; ham veri korunmuştur.
- 100 W ve 150 W tam parametre tabloları da kaydedilmiştir.
- Yüksüz biaslı altı ölçümün ortalaması 3.4017 mV'dir; bu değer yük eğrisine dahil edilmemiş ve sıfır düzeltme değeri olarak kabul edilmemiştir.
- Osiloskop sonuçları SCT sekonder sinyalinin yük kademelerinde düzenli değiştiğini gösterir. ADS1115'in ölçüm başarısı hakkında henüz sonuç vermez.

## 7. Sonuç ve sıradaki deney

Osiloskopla bias bağlı yük kademeleri testi tamamlandı. Sıradaki adım, ADS1115 No. 1 ile yalnızca ham diferansiyel gerilim okumaktır.

Karşılaştırma deneyi:
1. Aynı SCT013, aynı bias bağlantısı ve aynı yük kademeleri kullanılacak.
2. ADS1115 A0-A1 diferansiyel ham gerilim okunacak.
3. İlk aşamada RMS, akım katsayısı, sıfır düzeltmesi ve filtre uygulanmayacak.
4. ADS1115 ham verisi, aynı koşuldaki osiloskop Vrms ve dalga şekliyle karşılaştırılacak. ADS1115'in örnekleme yöntemi nedeniyle ham örneklerin doğrudan osiloskop Vrms ile eşdeğer olmadığı dikkate alınacak; sonraki aşamada ADS1115 örneklerinden uygun RMS hesabı ayrıca değerlendirilecek.
5. I²C haberleşmesi, adres 0x48, pin eşleşmeleri ve A0/A1 pinlerinin GND'ye göre mutlak gerilimleri doğrulanacak.
6. Ölçüm logu ve yorum, ADS1115 kod sürümünün kendi LOG/RAPOR klasöründe tutulacak.

**Durum:** Osiloskop yük testi tamamlandı. ADS1115 ham okuma ve karşılaştırma henüz yapılmadı.
