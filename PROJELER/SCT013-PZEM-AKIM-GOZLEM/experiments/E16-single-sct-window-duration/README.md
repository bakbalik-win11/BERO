# E16 — Tek SCT kanalında ct_clamp ölçüm penceresi karşılaştırması

**Durum:** PLANLANDI  
**Dal:** `exp/modul2-ch1-2hz-20261106`  
**Tarih:** 2026-11-06

## HEDEF

E15'te yayın aralığı değiştirildi; `sample_duration=100ms` sabit tutuldu. E16'da bunun tersi yapılacaktır: SCT ölçüm penceresi değişecek, yayın aralığı sabit kalacaktır.

Soru: Aynı tek SCT kanalında, aynı fiziksel koşullarda ct_clamp ölçüm penceresini 50ms, 100ms ve 200ms yapmak katsayısız ölçüm çıktısının dağılımını, ortalamadan sapma büyüklüğünü ve gözlenen sıçrama davranışını nasıl etkiliyor?

## D/E/F tur planı

| Tur | `sample_duration` | `interval` | Süre | Nominal yayın |
|---|---:|---:|---:|---:|
| D | 50ms | 1s | 10 dk | 1 Hz |
| E | 100ms | 1s | 10 dk | 1 Hz |
| F | 200ms | 1s | 10 dk | 1 Hz |

Toplam nominal kayıt süresi 30 dakikadır. Sıra D → E → F.

## Sabit tutulacaklar

- Tek kanal: CH1-1T, sarı kablo, GPIO32 / ADC1_CH4.
- Yayın aralığı: `interval=1s`.
- Katsayı: K=24.22.
- ADC attenuation: 12dB.
- Aynı fiziksel SCT, aynı bağlantı, aynı ölçüm noktası ve karşılaştırılabilir yük koşulu.
- UDP 4210 olay alıcısı ve 100ms non-blocking alım kontrolü korunur.
- CH2, CH3 ve ayrı GPIO35 bias ADC okuması bu deney firmware'inde yoktur.

## Değiştirilecek tek değişken

Yalnızca `ct_clamp.sample_duration`: D=50ms, E=100ms, F=200ms. Her turda başka YAML ayarı değiştirilmez.

## Ölçüm ve değerlendirme

Öncelikli akış, `on_raw_value` ile yayımlanan katsayısız ct_clamp çıktısıdır. Bu değer **ham ADC örneği değildir**; ct_clamp hesaplamasının K çarpanı uygulanmadan önceki çıktısıdır. K=24.22 uygulanmış ikinci entity ayrıca korunur.

Her tur 10 dakika sürer. HA zaman damgalarıyla gerçek yayın aralığı ve geçerli kayıt sayısı doğrulanır. Aynı seçim kuralıyla kararlı bölümler karşılaştırılır. Ortalama, medyan, SD, MAD, P95/P99, maksimum, mutlak ortalamadan sapma dağılımı ve ardışık yayın farkları raporlanır. Sıçrama eşiği kullanılacaksa sonuçlar incelenmeden önce üç tur için ortak belirlenir; eşik sonradan veriye göre seçilmez.

## Kanıt sınırları

- E15 A/B/C, `sample_duration=100ms` sabitken yayın aralığını 500ms/1s/2s olarak değiştirdi.
- E16 D/E/F, yayın aralığını 1s sabit tutup ölçüm penceresini değiştirecektir.
- 50ms, 100ms ve 200ms pencereler aynı sayıda şebeke periyodu içermez; bu fark deneyin değişkenidir.
- Bu plan henüz cihazda derlenmiş, yüklenmiş veya test edilmiş değildir.
- UDP STATE fiziksel yükün açık/kapalı olduğunu kanıtlamaz.
- 1s yayın aralığı, iki yayın arasında oluşup kaybolan olayları göstermeyebilir. Sonuçlar yayımlanan değerler için yorumlanacaktır.

## D turu firmware

[bero-modul2-e16-single-sct-window-d-50ms.yaml](../../firmware/experiments/bero-modul2-e16-single-sct-window-d-50ms.yaml)
