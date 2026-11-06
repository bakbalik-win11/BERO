# I010 — Oturum 2: 18 W uzun ON/OFF çevrimleri

**Tarih:** 2026-11-06 (+03:00)  
**Veri aralığı:** 16:00:00–20:39:50.631 (CH1 kayıtları); Oturum 2 çevrim analizi 18:00:00–20:39:50  
**Durum:** CSV analizi yapıldı; uzun fiziksel yüksüz oturum bu veri diliminde henüz görülmüyor.

## Kaynak dosyalar ve bütünlük

İki HA History CSV birleştirilerek analiz edildi. Ham dosyalar değiştirilmedi.

- `history (51).csv` — SHA-256: `f692e758eb3435895f3866c4dee71d719bd9b205678a42c5176342914de26c8a`
- `history (52).csv` — SHA-256: `83d7d9b9ecd496736a49ea914d0635a04da1221633738ca9daa2d2e6dd6f3c7b`

Her iki dosyanın kolon yapısı: `entity_id,state,last_changed`. Zamanlar UTC'den Türkiye yerel saatine (+03:00) çevrilerek işlendi.

## 18:00 sonrası kayıt kapsamı

- CH1 K uygulanmış entity: 16.793 kayıt tüm CSV aralığında; 18:00 sonrası analiz pencerelerinde 7.960 CH1 örneği.
- CH1 katsayı öncesi ct_clamp entity ayrı olarak mevcut.
- PZEM gerilim, akım ve aktif güç entity'leri mevcut.
- SSR ve UDP olay durum kayıtları mevcut.
- Ayrı bir bias entity/serisi iki CSV'de de bulunamadı. Bu nedenle bias değişimi bu oturumdan hesaplanamaz.
- CH1 yayın aralığı tüm veri boyunca yaklaşık 1 saniye medyan; PZEM gerilim ve güç kayıtları yaklaşık 5 saniyelik, değişim odaklı/seyrek kayıtlar.

## Çevrim segmentasyonu

18:00:00 sonrası SSR durum geçişleri kullanılarak ON/OFF aralıkları çıkarıldı. Gözlenen çevrim yapısı yaklaşık 40 saniye SSR ON ve 20 saniye SSR OFF şeklindedir.

Her aralığın başındaki 3 saniye ve sonundaki 2 saniye geçiş/yerleşme etkisini azaltmak amacıyla kararlı pencere özetinden çıkarıldı. Bu kesme yalnızca türetilmiş analiz içindir; ham kayıt korunmuştur.

- ON penceresi sayısı: 160
- OFF penceresi sayısı: 160
- ON kararlı CH1 örnek sayısı: 5.560
- OFF kararlı CH1 örnek sayısı: 2.400

## CH1 sonuçları

K=24.22 uygulanmış CH1 çevrim medyanlarının dağılımı:

| İstatistik | 18 W ON çevrim medyanları | Fiziksel OFF çevrim medyanları |
|---|---:|---:|
| Çevrim sayısı | 160 | 160 |
| Medyan | 0.26534 A | 0.19332 A |
| Medyan mutlak sapma (MAD) | 0.00433 A | 0.00418 A |
| P05 | 0.25656 A | 0.18455 A |
| P95 | 0.27533 A | 0.20687 A |
| En düşük / en yüksek çevrim medyanı | 0.24913 / 0.28441 A | 0.18089 / 0.21257 A |

Kullanıcının sınıflandırma kuralı: hesaplanmış CH1 değeri 0.20 A'nın altındaysa OFF. Bu kurala göre:

- ON çevrim medyanları: 160/160 kez 0.20 A veya üzerinde.
- Fiziksel OFF çevrim medyanları: 135/160 kez 0.20 A altında; 25/160 kez 0.20 A veya üzerinde.
- OFF pencerelerindeki 25 eşik-üstü medyan otomatik ON sayılmaz. Bu pencerelerde OFF koşulunu doğrulayan 0.20 A altı kanıtı yoktur; ayrıca değerlendirme gerekir.
- Tekil örnek seviyesinde kararlı OFF örneklerinin %64.3'ü 0.20 A altında, %35.7'si 0.20 A veya üzerindedir. ON örneklerinin %99.98'i 0.20 A veya üzerindedir. Tekil örnek oranları tek başına durum kararı değildir.

Bu veri, 18 W ON çevrimlerinin 0.20 A üstü medyan davranışını tutarlı biçimde gösterdiğini destekler. Aynı zamanda fiziksel OFF çevrimlerinin tamamının 0.20 A altına inmediğini gösterir. Dolayısıyla kural tek yönlüdür: <0.20 A => OFF; >=0.20 A => otomatik ON değil, ek kanıt gerekir.

## PZEM referansı

Kararlı ON pencerelerinde PZEM aktif güç çevrim medyanlarının medyanı 18.10 W (aralık 17.90–18.30 W); OFF pencerelerinde gözlenen geçerli güç medyanları 0 W'tır. PZEM güç/akım kayıtları yaklaşık 5 saniye aralıklı olduğundan her 20 saniyelik OFF penceresinde aynı sayıda kayıt bulunmaz. PZEM bu analizde pratik durum referansıdır; mutlak ground truth olarak ele alınmamıştır.

## Şebeke gerilimi

18:00–20:39 aralığında PZEM gerilimi:

- n = 1.659
- Medyan = 228.8 V
- P05–P95 = 227.4–230.1 V
- Min–maks = 225.8–231.3 V

Dakikalık CH1 medyanı ile dakikalık gerilim medyanı arasındaki Pearson korelasyonu yaklaşık 0.13'tür. Bu tek oturumda güçlü doğrusal eş hareket kanıtı görülmemiştir. Bu sonuç gerilimin etkisiz olduğunu kanıtlamaz; bias serisi de olmadığı için bias/gerilim etkilerini birbirinden ayırmak mümkün değildir.

## Uzun yüksüz oturum hakkında sınır

CSV'nin sonuna kadar SSR yaklaşık 40 s ON / 20 s OFF çevrimi sürmektedir. Son kayıtlarda PZEM gücü yeniden yaklaşık 18 W göstermektedir. Bu nedenle bu iki dosya uzun ON/OFF çevrim oturumunu kapsar; sonrasında planlanan çok uzun, sürekli fiziksel yüksüz kayıt bu veri diliminde henüz yer almamaktadır.

## Sonuç ve sonraki adım

1. 18 W ON davranışı çevrimler boyunca CH1 medyanında tutarlı biçimde 0.20 A üstünde gözlendi.
2. Fiziksel OFF çevrimlerinin yaklaşık %15.6'sında çevrim medyanı 0.20 A altına inmedi. Bunlar otomatik ON değil, OFF kararı verilemeyen/ek kanıt gereken pencerelerdir.
3. PZEM gerilimi mevcut; bias entity'si yok. Uzun yüksüz kayda başlamadan önce firmware ve HA entity yapılandırmasında biasın gerçekten yayınlanıp yayınlanmadığı kontrol edilmeli. Yoksa bias ölçümü ayrı entity olarak eklenmeli, doğrulanmalı ve sonra uzun yüksüz kayıt başlatılmalı.
4. Bias ve gerilim için düzeltme/kompanzasyon bu veriye dayanarak uygulanmayacak. Önce eşzamanlı veri toplanıp ilişki araştırılacak.
5. Uzun fiziksel yüksüz veri, bu çevrim oturumundan ayrı kayıt dilimi olarak tutulacak.

**Güvenlik notu:** Yazılımın OFF sınıfı elektriksel güvenlik veya hattın enerjisiz olduğunun garantisi değildir.
