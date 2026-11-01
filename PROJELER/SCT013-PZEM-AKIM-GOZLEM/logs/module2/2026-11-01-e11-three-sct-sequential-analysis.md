# E11 — Üç SCT log analizi

Kaynak: `esp32d1-logs (64).txt`; 2026-11-01 11:57:10.927–12:03:01.718 (+03:00). 2.795 satır, 208.718 bayt. Kaynak SHA-256: `97a36071b8319625df5e717b358c8ec69fea609be928ba71e6e3a5153c081484`.

## Özet

176 çevrim; SCT1/2/3 için 176 akım ve 176 Raw AC yayını; 176 ortak bias yayını. İlk çevrim açılış verisi olarak ayrıldı. Kararlı istatistikler sonraki 175 çevrimden hesaplandı.

| Kanal | GPIO | Ortalama A | Medyan A | SD A | CV | Min–maks A | Raw AC ort. V |
|---|---:|---:|---:|---:|---:|---:|---:|
| SCT1 | 32 | 0.42141 | 0.420 | 0.00833 | 1.98% | 0.404–0.452 | 0.017399 |
| SCT2 | 33 | 0.42283 | 0.422 | 0.00999 | 2.36% | 0.403–0.478 | 0.017459 |
| SCT3 | 34 | 0.42686 | 0.428 | 0.00891 | 2.09% | 0.408–0.478 | 0.017623 |

SCT2, SCT1'den ortalama %0.34; SCT3, SCT1'den %1.29 yüksektir. SCT1 en dar dağılıma, SCT2 en geniş dağılıma sahiptir. Bias ortalaması 1.66022 V, medyan 1.660 V, min–maks 1.642–1.682 V.

## Örnek sayısı

İlk çevrim hariç ortalama farklı örnek / 200 ms: SCT1 3400 (17000 SPS), SCT2 3236 (16180 SPS), SCT3 3416 (17078 SPS). SCT2'nin kabul edilen farklı örnek sayısı daha düşüktür; tek başına doğruluk hatası kanıtı değildir.

## Zamanlama

176 çevrim işaretlerinden medyan geçişler: SCT1→SCT2 251 ms; SCT2→SCT3 253 ms; SCT3→bias 253 ms. 159 çevrimde üç geçiş de 200–300 ms aralığındadır. 17 çevrimde en az bir geçiş bu aralığın dışındadır.

12:01:07.174 çevriminde aralıklar 16 ms, 454 ms ve 392 ms olarak kaydedilmiştir. Aynı çevrimde debug örnek sayıları 200 ms penceresiyle uyumlu görünse de sıra işaretleri çelişkilidir. Bu nedenle gerçek pencere başlangıç/bitişi ve çakışmasızlık kesin doğrulanmış değildir. 50 ms geçiş payı azaltılmamalıdır.

## Eski kayıtla kıyas

LOAD-100W-004 önceki Modül 2 SCT1 oturumu: ortalama 0.425 A, medyan 0.423 A, SD 0.01149 A. Yeni SCT1: ortalama 0.42141 A, medyan 0.420 A, SD 0.00833 A; önceki ortalama/medyana göre yaklaşık -0.85% / -0.71%. Bu benzerlik, aynı fiziksel yük ve besleme koşulu doğrulanmadığından koşullu kıyastır.

0.427 A değeri depoda geçici UNIT beklentisidir, PZEM değildir. Yeni logda eşzamanlı PZEM veya UNIT kaydı yoktur. K=24.22 korunmuştur; kalibrasyon veya ±%4 kabul kararı verilmez.

## Sonuç

Üç kanal da düzenli veri üretmiştir ve kararlı bölüm dağılımları birbirine yakındır. SCT2 örnek sayısı farkı ve tek çevrimdeki zamanlama anomalisi takip edilmelidir. T010 henüz tüm kabul kapılarını kapatmış sayılmaz.

Tam ağ kimlikleri maskelenmiş log: `2026-11-01-e11-three-sct-sequential-full-sanitized.txt`.
