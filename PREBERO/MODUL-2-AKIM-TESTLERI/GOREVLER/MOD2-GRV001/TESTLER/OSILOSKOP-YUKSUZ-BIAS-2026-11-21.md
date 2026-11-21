# Osiloskop Testi – Yüksüz / Biaslı SCT Ölçümü

- **Tarih:** 2026-11-21
- **Görev:** MOD2-GRV001 – Akım davranışı ve katsayı çalışmaları
- **Test durumu:** Yüksüz ölçüm aşaması tamamlandı; yük altında ölçümler henüz yapılmadı.
- **Koşul:** Yük kapalı (yüksüz). Kullanıcı tarafından bias devresinin bağlı olduğu bildirildi.
- **Ölçüm noktası:** SCT013 sinyalinin biaslı osiloskop ölçümü.
- **Ölçüm yöntemi:** Altı ayrı Single yakalama; her yakalamada ekrandaki Vrms değeri kaydedildi.
- **Osiloskopta görülen ayarlar:** CH1, prob X1, 10 mV/div, 5 ms/div, 3.125 MSa/s.
- **Not:** Bu kayıt yalnızca bu altı yüksüz yakalamayı kapsar. Ekrandaki frekans göstergeleri ölçüm amacıyla kullanılmamıştır.

## Ham ölçüm tablosu

| Durum | Bias | Single No | Vrms |
|---|---|---:|---:|
| Yüksüz | Var | 1 | 1.60 mV |
| Yüksüz | Var | 2 | 5.39 mV |
| Yüksüz | Var | 3 | 5.01 mV |
| Yüksüz | Var | 4 | 5.07 mV |
| Yüksüz | Var | 5 | 1.05 mV |
| Yüksüz | Var | 6 | 2.29 mV |

## Özet

- **Ölçüm adedi:** 6
- **Vrms aralığı:** 1.05–5.39 mV
- **Aritmetik ortalama:** 3.4017 mV (yaklaşık **3.40 mV**)

Hesap:
`(1.60 + 5.39 + 5.01 + 5.07 + 1.05 + 2.29) / 6 = 3.4017 mV`

## İlk gözlem

Altı yüksüz Single yakalamasında Vrms değerleri aynı seviyede sabit kalmamış, 1.05 mV ile 5.39 mV arasında değişmiştir. Bu nedenle 3.40 mV yalnızca bu altı yakalamanın aritmetik ortalamasıdır; kalıcı ofset, gürültü tabanı veya sıfır düzeltme katsayısı olarak henüz kabul edilmez.

## Kapsam ve sınırlamalar

- Bias bağlı yüksüz durum kaydedilmiştir.
- Bu testte yük akımı ve PZEM karşılaştırma değeri bulunmamaktadır.
- SCT013 30A/1V oranıyla akım hesabı yapılmamıştır; yük akımlı ölçümler geldikten sonra karşılaştırma grafiğine dahil edilecektir.
- Bu sonuç tek başına biasın gerekliliğini, sıfır düzeltmesini veya kalibrasyon katsayısını doğrulamaz.
- Bu kayıt, görevde daha önce planlanan iki SCT'nin ADS1115 A0-A1 / A2-A3 biaslı-biassız karşılaştırma deneyinin yapıldığı anlamına gelmez.

## Sonraki adım

Aynı osiloskop ayarları ve bias bağlantısı korunarak belirlenen yük kademelerinde altı ayrı Single yakalama alınacak; her kademenin altı Vrms değeri ve ortalaması ayrı kaydedilecektir. PZEM akımı da aynı yük koşulunda not edilecektir.
