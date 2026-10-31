# FIXED-LOAD-0130A-001 — SCT-1 log değerlendirmesi

## HEDEF
0,130 A sabit yük gözlem planı kapsamında ESP32D1 / Modül 2 / SCT-1 akışını incelemek. 0,130 A, testin hedef değeri olarak tutulur; logda UNIT veya PZEM referansı bulunduğu doğrulanmamıştır.

## KAYNAK
- Kullanıcı dosyası: `esp32d1-logs (56).txt`
- Boyut: 298.344 bayt
- Satır: 3.986
- SHA-256: `15c94083291b374e60f80d932494d6a6a58cbef9b5a3d82227cc2f58703dc20a`
- Cihaz log zamanı: 20:47:28–21:06:00 (2026-10-31, yerel saat +03:00); ilk/son akım yayını 20:47:30–21:06:00.
- 556 SCT-1 akım yayını; yaklaşık 18 dakika 30 saniye, yaklaşık 2 saniye aralık.
- Kaynak tam metni kullanıcı yüklemesinde korunur. Bu committe ham TXT'nin tamamı Git'e aktarılmamıştır; dosya adı, boyutu ve SHA-256 kaydedilmiştir.

## DÜZENEK / KOD
- ESPHome 2026.10.1; ESP32D1 / Modül 2.
- SCT-1 ADC GPIO32 / ADC1_CH4; ortak bias GPIO35 / ADC1_CH7.
- ADC attenuation 12 dB, ADC entity update 1 s.
- ct_clamp sample_duration 200 ms; update_interval 2 s.
- Firmware deposundaki `firmware/esp32d1.yaml` katsayısı K=24.22; yazılımsal sıfır eşiği yok. Bu testte firmware değiştirilmediği kabulü, log başlangıç konfigürasyonu ile depo YAML eşleşmesine dayanır; binary eşleşmesi iddia edilmez.
- Wi-Fi bağlantısı mevcut; sinyal yaklaşık -56 dB.

## SCT-1 AKIM İSTATİSTİKLERİ — LOG İLE DESTEKLENDİ
- n=556
- Ortalama: 0,203637 A
- Medyan: 0,203 A
- Minimum–maksimum: 0,157–0,291 A
- Örnek standart sapma: 0,017971 A
- Değişim katsayısı: %8,82

## ANALOG / ÖRNEKLEME
- Raw AC n=556; ortalama 0,0084077 V; medyan 0,00838 V; min–maks 0,00648–0,01202 V.
- Ortak bias n=1112; ortalama 1,663729 V; min–maks 1,647–1,675 V.
- ct_clamp log örnekleme hızı n=556; ortalama 17.171 SPS; min–maks 16.695–17.670 SPS.

## ZAMAN İÇİNDE DAVRANIŞ
Yaklaşık iki dakikalık 10 ardışık blokta ortalamalar sırasıyla 0,2081; 0,2062; 0,2005; 0,2007; 0,2052; 0,2054; 0,2069; 0,2009; 0,1993 ve son kısmi blokta 0,2020 A'dır. İlk bloktan son bloğa belirgin bir aşağı/yukarı sürüklenme görülmez; ortalama yaklaşık 0,20 A çevresinde korunmuştur. Tekil üst değerler vardır: 0,25 A üzeri 6, 0,27 A üzeri 4 yayın. Ham örnekler korunmuştur.

## YORUM
- **LOG İLE DESTEKLENDİ:** SCT-1 zinciri bu oturumda yaklaşık 18,5 dakika boyunca düzenli aralıklarla 556 akım yayını üretmiştir.
- **LOG İLE DESTEKLENDİ:** Akım göstergesi ortalama 0,2036 A ve medyan 0,203 A çevresinde toplanmıştır. Blok ortalamaları 0,1993–0,2081 A aralığında olduğundan uzun dönemli ortalama belirgin biçimde kaymamıştır.
- **LOG İLE DESTEKLENDİ:** Anlık dağılım geniştir (SD 0,0180 A; CV %8,82); minimum 0,157 A, maksimum 0,291 A. Bu nedenle tek bir sabit değer gibi yorumlanmamalıdır.
- **ÖNEMLİ SINIR:** 0,130 A hedefi ile logdaki 0,2036 A ortalaması farklıdır. Ancak logda UNIT/PZEM referans örneği veya fiziksel yük kimliği görünmediğinden bu farkı ölçüm hatası/sapma diye adlandırmak doğru değildir. 0,130 A, hedef değer olarak kalır; doğrulanmış referans olarak kullanılmaz.
- 0,30 A altı düşük akım gözlem bölgesinde ±%4 kabul/ret uygulanmaz. Burada amaç davranış, dağılım ve tekrarlanabilirliği gözlemlemektir.
- Bu tek log, 0,130 A akımın doğrulukla ölçüldüğünü, K=24.22'nin bu bölgede kalibre olduğunu veya yükün fiziksel olarak sabit kaldığını kanıtlamaz.

## SONUÇ / DURUM
**GÖZLEM LOGU ANALİZ EDİLDİ.** FIXED-LOAD-0130A-001 planı, SCT-1 gözlem kaydıyla güncellendi; referans cihaz/değer ve fiziksel yük kimliği doğrulanana kadar test nihai doğrulama olarak kapatılmaz. K=24.22 korunur; yazılımsal sıfır eşiği eklenmez.

## AÇIK KALANLAR
1. Fiziksel yükün adı/gücü ve 0,130 A hedefinin hangi cihaz/ölçüme dayandığı.
2. UNIT veya PZEM ile aynı kararlı zaman penceresinde referans.
3. Ham TXT'nin Git deposuna tam dosya olarak eklenmesi (şu an kaynak dosya adı/boyutu/hash kayıtlı; tam metin kullanıcı yüklemesinde).
