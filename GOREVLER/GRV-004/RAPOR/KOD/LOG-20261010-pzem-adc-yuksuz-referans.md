# BERO GRV-004 — ESP32D1 PZEM + 4 Kanal ADC Log Kaydı
Tarih: 2026-10-10
Cihaz: esp32d1 @ 192.168.0.8
ESPHome: 2026.9.1
Kaynak: Kullanıcının 2026-10-10 tarihinde paylaştığı OTA/API log dosyası.
Kayıt türü: Aşağıda, orijinal logdan ADC_TEST tur satırları ve ilgili PZEM başlangıç/ölçüm bilgileri ayrıştırılarak korunmuştur. Bu dosya tam ham logun birebir kopyası değildir.

## Bağlantı ve PZEM başlangıç ölçümleri
- API çözümleme ve handshake başarılı.
- PZEM Gerilim: 228.4 V (başlangıç); sonraki ölçümlerde yaklaşık 227.7–229.0 V.
- PZEM Akım: 0.028 A (logda yuvarlanmış değer).
- PZEM Güç: başlangıçta 1.70 W; sonraki ölçümlerde yaklaşık 1.50–1.70 W.
- PZEM Enerji: 10394 Wh.
- PZEM Frekans: yaklaşık 49.9–50.0 Hz.
- PZEM Güç Faktörü: yaklaşık 0.23–0.27.

## Birleşik ADC_TEST satırları
```text
[20:14:30.923] TUR=1 PZEM[A=0.028 P=1.7W V=228.4] BIAS[min=1.56500 max=1.68800 avg=1.66253 std=0.005573] K1[min=1.59700 max=1.78700 avg=1.66137 std=0.007770] K2[min=1.61200 max=1.71200 avg=1.65977 std=0.005985] K3[min=1.56700 max=1.70000 avg=1.65522 std=0.006187]
[20:14:41.491] TUR=2 PZEM[A=0.028 P=1.5W V=229.0] BIAS[min=1.37700 max=1.80100 avg=1.66424 std=0.012386] K1[min=1.45300 max=1.84200 avg=1.66311 std=0.013202] K2[min=1.55800 max=1.79900 avg=1.66125 std=0.009663] K3[min=1.60300 max=1.71700 avg=1.65652 std=0.006323]
[20:14:52.083] TUR=3 PZEM[A=0.028 P=1.5W V=228.2] BIAS[min=1.57000 max=1.78400 avg=1.66413 std=0.007134] K1[min=1.50000 max=1.76600 avg=1.66246 std=0.008102] K2[min=1.64200 max=1.73500 avg=1.66114 std=0.005826] K3[min=1.63400 max=1.70400 avg=1.65674 std=0.004846]
[20:15:02.623] TUR=4 PZEM[A=0.028 P=1.5W V=228.6] BIAS[min=1.54000 max=1.77400 avg=1.66384 std=0.007521] K1[min=1.56300 max=1.69500 avg=1.66216 std=0.006250] K2[min=1.61800 max=1.76600 avg=1.66085 std=0.006287] K3[min=1.62000 max=1.69700 avg=1.65636 std=0.005622]
[20:15:13.250] TUR=5 PZEM[A=0.028 P=1.6W V=228.2] BIAS[min=1.60700 max=1.75100 avg=1.66425 std=0.006063] K1[min=1.56800 max=1.74700 avg=1.66261 std=0.007555] K2[min=1.52900 max=1.80600 avg=1.66061 std=0.009090] K3[min=1.53500 max=1.72000 avg=1.65629 std=0.006783]
[20:15:23.809] TUR=6 PZEM[A=0.028 P=1.6W V=228.2] BIAS[min=1.44700 max=1.75200 avg=1.66289 std=0.012056] K1[min=1.49700 max=1.84800 avg=1.66124 std=0.011933] K2[min=1.60700 max=1.74800 avg=1.65993 std=0.006296] K3[min=1.59600 max=1.70700 avg=1.65541 std=0.006266]
[20:15:34.338] TUR=7 PZEM[A=0.028 P=1.6W V=228.6] BIAS[min=1.50000 max=1.74800 avg=1.66357 std=0.007677] K1[min=1.49200 max=1.92600 avg=1.66239 std=0.017974] K2[min=1.59200 max=1.72700 avg=1.66059 std=0.006292] K3[min=1.57600 max=1.70400 avg=1.65570 std=0.006242]
[20:15:44.928] TUR=8 PZEM[A=0.028 P=1.5W V=228.5] BIAS[min=1.54000 max=1.82900 avg=1.66470 std=0.015938] K1[min=1.56700 max=1.92500 avg=1.66311 std=0.016722] K2[min=1.54300 max=1.83500 avg=1.66139 std=0.013477] K3[min=1.59900 max=1.72100 avg=1.65653 std=0.007313]
[20:15:55.423] TUR=9 PZEM[A=0.028 P=1.5W V=227.7] BIAS[min=1.57100 max=1.77100 avg=1.66381 std=0.009408] K1[min=1.48200 max=1.82200 avg=1.66234 std=0.012739] K2[min=1.56400 max=1.77300 avg=1.66025 std=0.008258] K3[min=1.59000 max=1.71600 avg=1.65620 std=0.006857]
[20:16:06.057] TUR=10 PZEM[A=0.028 P=1.5W V=227.9] BIAS[min=1.47400 max=1.78600 avg=1.66515 std=0.010036] K1[min=1.56300 max=1.84500 avg=1.66305 std=0.010245] K2[min=1.57400 max=1.70800 avg=1.66095 std=0.006985] K3[min=1.59300 max=1.70300 avg=1.65675 std=0.005838]
[20:16:16.659] TUR=11 PZEM[A=0.028 P=1.5W V=228.4] BIAS[min=1.54200 max=1.77100 avg=1.66423 std=0.008552] K1[min=1.44600 max=1.86800 avg=1.66253 std=0.014825] K2[min=1.51300 max=1.76800 avg=1.66100 std=0.010406] K3[min=1.59700 max=1.75300 avg=1.65658 std=0.007881]
[20:16:27.272] TUR=12 PZEM[A=0.028 P=1.5W V=228.8] BIAS[min=1.53900 max=1.68700 avg=1.66393 std=0.007548] K1[min=1.47700 max=1.85300 avg=1.66258 std=0.010994] K2[min=1.59500 max=1.69500 avg=1.66079 std=0.005436] K3[min=1.62100 max=1.73100 avg=1.65678 std=0.005689]
[20:16:37.752] TUR=13 PZEM[A=0.028 P=1.5W V=228.8] BIAS[min=1.54900 max=1.75300 avg=1.66374 std=0.009335] K1[min=1.39400 max=1.85400 avg=1.66215 std=0.016288] K2[min=1.56600 max=1.76600 avg=1.66103 std=0.008702] K3[min=1.56100 max=1.71100 avg=1.65639 std=0.006864]
[20:16:48.294] TUR=14 PZEM[A=0.028 P=1.5W V=228.7] BIAS[min=1.57700 max=1.70900 avg=1.66371 std=0.005737] K1[min=1.58900 max=1.87200 avg=1.66257 std=0.010997] K2[min=1.60600 max=1.76300 avg=1.66058 std=0.005925] K3[min=1.56900 max=1.71300 avg=1.65622 std=0.006492]
[20:16:58.859] TUR=15 PZEM[A=0.028 P=1.5W V=228.3] BIAS[min=1.60300 max=1.74800 avg=1.66421 std=0.005809] K1[min=1.53500 max=1.94600 avg=1.66325 std=0.014168] K2[min=1.54000 max=1.80000 avg=1.66137 std=0.010170] K3[min=1.60300 max=1.72300 avg=1.65661 std=0.005968]
[20:17:09.482] TUR=16 PZEM[A=0.028 P=1.5W V=228.5] BIAS[min=1.64300 max=1.75200 avg=1.66457 std=0.004810] K1[min=1.53900 max=1.76400 avg=1.66270 std=0.006876] K2[min=1.64300 max=1.70300 avg=1.66119 std=0.004532] K3[min=1.63100 max=1.70000 avg=1.65688 std=0.004844]
[20:17:19.945] TUR=17 PZEM[A=0.028 P=1.5W V=228.4] BIAS[min=1.55400 max=1.87500 avg=1.66433 std=0.013098] K1[min=1.52700 max=1.74000 avg=1.66226 std=0.007028] K2[min=1.55000 max=1.80000 avg=1.66087 std=0.009755] K3[min=1.57600 max=1.74000 avg=1.65631 std=0.007349]
```

## Logda ayrıca görülen uyarılar
- ESP32 chip revision için minimum_chip_revision: 3.1 önerisi.
- SRAM1 as IRAM için öneri.
- Bir kez safe_mode işleminin 67 ms sürdüğü uyarısı.
- Bu kayıtta ADC_TEST satırları TUR=1–17 görünür; PZEM sensör satırları devam eder.
