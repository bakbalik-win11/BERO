# MIXED-LOAD-001 — 100 W akkor + FAN-3 / SCT-1 analiz raporu

**Tarih:** 2026-10-31  
**Durum:** Gozlem oturumu kapatildi; ±%4 UNIT karsilastirmasi bu log icin gecti. PZEM ve gecis testi kapsami tamamlanmadi.  
**Referans:** UNIT-reported 0.573 A (kullanici bildirimi; PZEM degil).

## Kaynak ve duzenek

- Kullanici kaynak dosyasi: `esp32d1-logs (44).txt`
- Kaynak SHA-256: `f6f3434e540402e7d9a7d63fb38aed0f7dc660b96cb3ef14e00ad6affc07e910`
- Kaynak boyutu: 77,072 bayt.
- ESPHome 2026.10.1; ESP32D1 / Modul 2; SCT-1 sari GPIO32 ADC1_CH4; ortak bias turuncu GPIO35 ADC1_CH7.
- ADC 12 dB, 1 s yayin; ct_clamp 200 ms pencere, 2 s yayin; K=24.22.
- Harici besleme durumu: onceki test kurulumundaki Modul 2 duzenegi; bu logda guc raylari olculmemistir.

## Akim istatistikleri

- Akim yayin sayisi: 136.
- Ilk/son yayin: 17:55:57.139–18:00:27.106 (+03:00), 4 dk 29.967 sn.
- Ortalama: 0.582456 A.
- Medyan: 0.582 A.
- Min–maks: 0.564–0.609 A.
- Ornek standart sapma: 0.007335 A.
- UNIT referansi: 0.573 A.
- Mutlak ortalama fark: +0.009456 A.
- Ortalama sapma: +1.650%.
- Medyan sapmasi: +1.571%.
- ±%4 araligi: 0.55008–0.59592 A.
- Aralik icindeki yayin: 130/136 (%95.59). Disarida kalan 6 yayin ust sinirin uzerindedir; alt sinirin altinda yayin yoktur.

## Analog ve ornekleme gozlemleri

- Raw AC ortalama: 0.024048 V (136 yayin).
- Ortak bias GPIO35 ortalama: 1.663754 V (272 yayin).
- SCT-1 ADC GPIO32 ortalama: 1.663051 V (273 yayin).
- ct_clamp raporlanan ornekleme hizlari yaklasik 16.9–17.9 kSPS bandindadir; firmware logu bu degerleri her 200 ms pencere icin raporlar.
- Acilis bolumunde ADC, bias ve ct_clamp baslatma/kalibrasyon durumlari OK gorunur.
- Uc ESPHome derleyici/optimizasyon uyarisi vardir. Gorunen kayitta runtime [E] hatasi, brownout veya yeniden baslama belirtisi yoktur.

## Teknik yorum

Bu oturumda SCT-1'in karma yuk toplam hat akimi UNIT'in 0.573 A bildirimine yakin ve kararlidir. Ortalama +1.65% farkla ±4% araligindadir; yayinlarin %95.59'u da ayni aralikta kalmistir. Bu nedenle **bu oturumun kararlı pencere UNIT karsilastirmasi ±4% kriterini sagladi**.

Bu sonuc PZEM dogrulamasi degildir. Logda PZEM akim, aktif guc veya PF bulunmamaktadir. UNIT de mutlak dogru/ground truth kabul edilmez; kaynak turu UNIT-reported olarak korunur.

Logun baslangic ve bitisinde fan acma/kapama olayina ait isaret veya kullanici zaman notu yoktur. Bu nedenle fan gecis cevabi, SCT-PZEM tepki suresi ve gecis dinamikleri bu kayittan cikarilamaz. Bu log tek bir birlikte-yuk kararlı oturumudur; test planindaki tum asamalar tamamlanmis degildir.

K=24.22 degistirilmemistir. Yazilimsal sifir esigi eklenmemistir. Alt/ust sinirin disindaki 6 yayini silmek veya ortalamayi degistirmek icin filtre uygulanmamistir.

## Kapanis sinifi

- MIXED-LOAD-001'in **100 W + FAN-3 birlikte kararlı yuk gozlem asamasi** kapatildi.
- Bu oturum UNIT 0.573 A referansina gore ±4% kriterini sagladi.
- Tum MIXED-LOAD-001 deney plani (tekli yukler, PZEM eslestirmesi ve olay-isaretli gecisler) tamamlanmis sayilmaz; bunlar ayri/eksik kapsam olarak acik kalir.
- Kapanis YAML'i, logun baslangicinda gorulen ESPHome ayarlariyla ayni aktif `firmware/esp32d1.yaml` iceriginden snapshot alinmistir. Bu, YAML/config seviyesinde eslesmedir; derlenmis binary hash eslesmesi iddia edilmez.

## Kaynak siniflandirmasi

- **LOG:** SCT, Raw AC, ADC, bias, zaman ve ESPHome baslangic/uyari bilgileri.
- **KULLANICI BILDIRIMI:** UNIT 0.573 A birlikte-yuk referansi; yuklerin 100 W akkor + FAN-3 oldugu.
- **HESAP:** Istatistikler, sapma ve ±4% yayin sayimi.
- **EKSIK KANIT:** PZEM akim/PF, fan gecis olay isaretleri, guc rayi olcumu.
