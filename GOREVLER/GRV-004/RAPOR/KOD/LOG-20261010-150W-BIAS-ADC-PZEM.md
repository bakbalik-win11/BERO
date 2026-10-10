# GRV-004 — 150 W Yük Deneyi
Tarih: 2026-10-10
Kaynak: esp32d1-logs (13).txt
Cihaz: esp32d1 @ 192.168.0.8; ESPHome 2026.9.1

## Özet
Kaynak logda TUR=38–51 arasında 14 adet ADC_TEST satırı 150 W nominal yük dönemine denk geliyor. PZEM bu aralıkta 147.2–148.9 W, 226.9–228.6 V ve 0.650–0.653 A gösteriyor. TUR=52'de değerler 1.7 W / 0.028 A seviyesine dönüyor; bu da yükün kaldırılmasıyla uyumlu.

## Yük altı birleşik log satırları
```text
[20:21:01.801] TUR=38 PZEM[A=0.652 P=148.5W V=228.2] BIAS[avg=1.66390 std=0.024603] K1[avg=1.66164 std=0.049165] K2[avg=1.65997 std=0.072893] K3[avg=1.65592 std=0.006766]
[20:21:12.368] TUR=39 PZEM[A=0.652 P=148.2W V=227.9] BIAS[avg=1.66339 std=0.024894] K1[avg=1.66232 std=0.049181] K2[avg=1.66083 std=0.072478] K3[avg=1.65656 std=0.007521]
[20:21:23.014] TUR=40 PZEM[A=0.652 P=148.5W V=228.2] BIAS[avg=1.66351 std=0.024027] K1[avg=1.66182 std=0.047088] K2[avg=1.66022 std=0.071967] K3[avg=1.65649 std=0.004378]
[20:21:33.501] TUR=41 PZEM[A=0.653 P=148.9W V=228.6] BIAS[avg=1.66275 std=0.025776] K1[avg=1.66156 std=0.047737] K2[avg=1.66054 std=0.072121] K3[avg=1.65610 std=0.006505]
[20:21:44.114] TUR=42 PZEM[A=0.652 P=148.4W V=228.0] BIAS[avg=1.66333 std=0.024272] K1[avg=1.66155 std=0.047600] K2[avg=1.66042 std=0.071709] K3[avg=1.65640 std=0.005866]
[20:21:54.617] TUR=43 PZEM[A=0.652 P=148.3W V=227.9] BIAS[avg=1.66286 std=0.025365] K1[avg=1.66092 std=0.049303] K2[avg=1.66042 std=0.072380] K3[avg=1.65580 std=0.006916]
[20:22:05.328] TUR=44 PZEM[A=0.652 P=148.2W V=227.9] BIAS[avg=1.66304 std=0.025097] K1[avg=1.66161 std=0.048833] K2[avg=1.66008 std=0.073066] K3[avg=1.65625 std=0.007657]
[20:22:15.715] TUR=45 PZEM[A=0.650 P=147.2W V=226.9] BIAS[avg=1.66327 std=0.025381] K1[avg=1.66218 std=0.047906] K2[avg=1.66079 std=0.072850] K3[avg=1.65596 std=0.007975]
[20:22:26.276] TUR=46 PZEM[A=0.651 P=147.5W V=227.1] BIAS[avg=1.66356 std=0.024576] K1[avg=1.66223 std=0.047951] K2[avg=1.66040 std=0.072372] K3[avg=1.65664 std=0.005425]
[20:22:36.870] TUR=47 PZEM[A=0.651 P=147.6W V=227.3] BIAS[avg=1.66398 std=0.025836] K1[avg=1.66286 std=0.048381] K2[avg=1.66142 std=0.072102] K3[avg=1.65716 std=0.005685]
[20:22:47.474] TUR=48 PZEM[A=0.651 P=148.0W V=227.6] BIAS[avg=1.66483 std=0.024854] K1[avg=1.66347 std=0.049340] K2[avg=1.66147 std=0.072435] K3[avg=1.65695 std=0.006566]
[20:22:57.992] TUR=49 PZEM[A=0.651 P=147.9W V=227.6] BIAS[avg=1.66422 std=0.024038] K1[avg=1.66262 std=0.047447] K2[avg=1.66134 std=0.072449] K3[avg=1.65744 std=0.005811]
[20:23:08.532] TUR=50 PZEM[A=0.651 P=147.7W V=227.3] BIAS[avg=1.66406 std=0.024180] K1[avg=1.66231 std=0.047258] K2[avg=1.66133 std=0.071806] K3[avg=1.65681 std=0.006388]
[20:23:19.113] TUR=51 PZEM[A=0.651 P=147.5W V=227.2] BIAS[avg=1.66452 std=0.024736] K1[avg=1.66303 std=0.047745] K2[avg=1.66108 std=0.072011] K3[avg=1.65752 std=0.006756]
[20:23:29.675] TUR=52 PZEM[A=0.028 P=1.7W V=228.0] BIAS[avg=1.66469 std=0.010764] K1[avg=1.66347 std=0.017013] K2[avg=1.66144 std=0.020115] K3[avg=1.65708 std=0.006270]
```

Bu dosya ilgili yük dönemi satırlarının arşividir; kullanıcı tarafından yüklenen 727 satırlık kaynak dosyanın birebir tam kopyası değildir.
