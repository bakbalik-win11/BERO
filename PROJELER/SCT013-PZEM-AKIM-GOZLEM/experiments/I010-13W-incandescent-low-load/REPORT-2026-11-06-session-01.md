# I010 — 18 W ON/OFF ayrışma raporu
## Oturum 1 — 6 Kasım 2026, 16:00–17:59 (+03:00)

## 1. Sonuç özeti

**Bu veri setinde 18 W yükün ON ve OFF durumları, PZEM ile eşleştirilen 16 tekrarlı çevrimde CH1 üzerinden istatistiksel olarak ayırt edilebildi.** Bu sonuç mevcut donanım, CH1-1T, K=24.22 ve bu oturum koşulları için geçerlidir; henüz farklı gün/oturumlarda bağımsız doğrulama değildir.

Buna karşılık **0.20 A mutlak ve her koşulda geçerli bir OFF eşiği değildir.** 18 W çevrimlerinden hemen önceki uzun yüksüz bölümde PZEM 0 W iken K uygulanmış CH1 medyanı 0.2532 A'dır ve değer zamanın %78.6'sında 0.20 A üzerindedir. Dolayısıyla yalnızca `CH1 < 0.20 A => NO_CURRENT` kuralı bütün oturum için güvenilir değildir.

Bu oturumun en güçlü bulgusu sabit eşikten ziyade **ON/OFF çevrimleri sırasında CH1 dağılım merkezinin tekrarlı ve tutarlı biçimde yer değiştirmesidir.**

## 2. Kaynak veri ve kapsam

- Kaynak: Home Assistant `history (50).csv`
- SHA-256: `fb92ba4b1acaf1fe470b33419f37f1b38cdabf32061e8a9babe01755acc9c8cc`
- Boyut: 1,626,778 byte
- Satır: 18,826; sütun: `entity_id,state,last_changed`
- Zaman aralığı: 6 Kasım 2026 16:00:00–17:59:35 (+03:00)
- CH1 K uygulanmış entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_akim`
- CH1 katsayısız entity: `sensor.esp32d1_bero_mod2_ch1_1t_faz_ham_akim`
- PZEM akım: `sensor.bero_modul_3_wroom_bero_pzem_akim`
- PZEM aktif güç: `sensor.bero_modul_3_wroom_bero_pzem_guc`
- SSR: `switch.bero_modul_3_wroom_bero_ssr_kontrol`
- CH1 kayıt aralığının medyanı yaklaşık 1.0 saniyedir. PZEM akım/güç kayıtları daha seyrektir ve kendi timestamp'leriyle ele alınmıştır.

### Kapsam dışı bırakılan bölümler

Kullanıcı talimatı gereği 15 W içeren bölümler kontrollü sınıflandırma karşılaştırmasına alınmadı. 17:30 sonrası 57 W + 15 W birleşik yük bölümü de dışarıda bırakıldı. Ham kaynak dosya değiştirilmedi.

CSV, 16:30 civarında PZEM aktif gücünün 14.6 W olduğunu gösterdiği için 16:30–17:00 aralığı OFF referansı olarak kullanılmadı; 15 W dönemi kapsam dışıdır.

## 3. Gerçek yüksüz referans

17:37:47.864–17:42:42.850 aralığında PZEM aktif güç kaydı 0 W olarak kaldı; PZEM akım durumu da sıfırdı. Bu aralık, 18 W denemesinden hemen önceki uzun fiziksel OFF referansı olarak ele alındı.

| Ölçüt | K uygulanmış CH1 |
|---|---:|
| Süre | 294.1 s |
| Örnek sayısı | 295 |
| Medyan | 0.2532 A |
| MAD | 0.0329 A |
| P05 | 0.1726 A |
| P95 | 0.3205 A |
| 0.20 A üzerindeki süre oranı | %78.6 |
| 0.20 A üzerinde en uzun kesintisiz bölüm | yaklaşık 42 s |

**Yorum:** Fiziksel yüksüz bölümde CH1'in 0.20 A üzerinde uzun süre kalması, 0.20 A'nın tek başına mutlak OFF eşiği olamayacağını gösterir. Bu bulgu sıçrama değildir; eşik üstü davranış onlarca saniye sürmüştür. Bu nedenle yalnızca kısa sıçrama filtresi eklemek global eşik sorununu çözmez.

## 4. 18 W ON/OFF deneyi

- Kullanıcı tarafından bildirilen başlangıç: 17:43 (+03:00).
- CSV'de ilk SSR ON geçişi: 17:43:31.316.
- Veri sonu: 17:59:35.711.
- Tamamlanan tekrar: 16 ON + 16 OFF çevrimi.
- SSR örüntüsü: yaklaşık 40 s ON / 20 s OFF.
- Her geçişte ilk 3 saniye ve sonraki geçişten önceki son 2 saniye kararlı pencere istatistiğinden çıkarıldı. Böylece her çevrimde 35 s ON ve 15 s OFF incelendi.
- Toplam kararlı analiz: 560 s ON, 240 s OFF.
- Bu geçiş koruması yalnızca raporlama yöntemidir; nihai sınıflandırma gecikmesi olarak onaylanmış değildir.

### 4.1 CH1 sonuçları — K=24.22 uygulanmış

| Ölçüt | 18 W ON | 18 W OFF |
|---|---:|---:|
| Kararlı örnek sayısı | 560 | 240 |
| Çevrim medyanlarının medyanı | 0.2557 A | 0.1850 A |
| Çevrim MAD değerlerinin medyanı | 0.0140 A | 0.0105 A |
| Çevrim P05 değerlerinin medyanı | 0.2272 A | 0.1656 A |
| Çevrim P95 değerlerinin medyanı | 0.3023 A | 0.2178 A |
| 0.20 A üzerinde geçirilen zamanın çevrim medyanı | %100 | %22.6 |

- ON çevrimlerinin 16/16'sında kararlı pencere medyanı 0.20 A üzerindeydi.
- OFF çevrimlerinin 16/16'sında kararlı pencere medyanı 0.20 A altındaydı.
- OFF pencerelerinde 0.20 A üzerindeki okumalar kısa süreliydi; gözlenen en uzun ardışık bölüm yaklaşık 2 saniyeydi.
- ON kararlı pencerelerinde 0.20 A üstü davranış pencere boyunca sürdü.
- Çevrim medyanları arasında ON–OFF farkı yaklaşık 0.0707 A'dır.

### 4.2 PZEM çapraz kontrolü

- 18 W ON kararlı pencerelerinde PZEM aktif güç kayıtlarının medyanı yaklaşık 17.95 W; görülen aralık 17.6–18.1 W.
- OFF kararlı pencerelerinde PZEM aktif güç kayıtları 0 W gösterdi.
- ON akım kayıtlarının medyanı yaklaşık 0.079 A.
- PZEM güncelleme hızı CH1'den daha düşüktür; her CH1 örneği için PZEM örneği varmış gibi bire bir eşleştirme yapılmadı.

PZEM, fiziksel ON/OFF ayrımını destekleyen pratik referans olarak kullanıldı; mutlak ground truth kabul edilmedi.

## 5. 0.20 A eşiğinin değerlendirmesi

Bu veri iki farklı sonucu aynı anda gösteriyor:

1. **18 W çevrimlerinin kendi içinde:** 0.20 A çevresinde güçlü bir ayrım var. ON medyanları eşiğin üzerinde, OFF medyanları altında. OFF tarafındaki eşik üstü okumalar kısa; ON tarafındaki eşik üstü davranış süreklidir.
2. **Oturumlar/koşullar arasında mutlak eşik olarak:** 0.20 A güvenilir değil. 18 W öncesindeki uzun OFF referansı yaklaşık 0.253 A medyan ve yaklaşık 42 saniyelik kesintisiz eşik üstü bölüm içeriyor.

Bu nedenle `0.20 A + süre koşulu` yalnızca aynı yerel baz çizgisi koşullarında işe yarayan aday bir karar özelliğidir; mevcut kanıtla evrensel OFF kuralı yapılamaz.

## 6. Bu deneyin yanıtladığı soru

**“18 W yükte akım var/yok kararı verilebilir mi?”**

- **Evet — bu oturumdaki tekrarlı 18 W ON/OFF çevrimleri için:** CH1 dağılımının merkezi ON ve OFF arasında 16 çevrim boyunca tutarlı biçimde ayrıştı; PZEM güç kayıtları bunu destekledi.
- **Henüz genel sistem kararı olarak hayır:** Uzun yüksüz referansta CH1 baz çizgisi 18 W çevrimlerinin OFF seviyesinden belirgin biçimde farklıydı. Bu, tek sabit 0.20 A eşiğinin farklı zaman/koşullarda yanlış sınıflandırma üretebileceğini gösteriyor.

Bir sonraki algoritma adımı, tek mutlak eşik yerine OFF referansının zamanla değişimini izleyen yerel/adaptif baz çizgisi ve süre-temelli dağılım karşılaştırmasını sınamaktır. Bu algoritma henüz uygulanmış veya doğrulanmış değildir.

## 7. Deney kararı ve devam

- Bu dosya, 18:00 öncesi ilk veri diliminin raporudur ve **Oturum 1 kapatılmıştır**.
- Kullanıcı 18:00 sonrasında 18 W ON/OFF testine devam edeceğini bildirdi. Bu sonraki kayıt ayrı veri dilimi/oturum olarak alınacak; mevcut raporun sayıları geriye dönük değiştirilmeden bağımsız tekrar doğrulaması olarak eklenecektir.
- 15 W içeren bölümler sonraki karşılaştırmalarda da kontrollü referans olarak kullanılmayacak.
- Ham CSV saklanır; türetilmiş istatistikler ham verinin yerine geçmez.

## 8. Çevrim medyanları

Kararlı pencerelerin K uygulanmış CH1 medyanları (A):

| Çevrim | ON | OFF |
|---:|---:|---:|
| 1 | 0.2618 | 0.1791 |
| 2 | 0.2634 | 0.1817 |
| 3 | 0.2640 | 0.1804 |
| 4 | 0.2522 | 0.1764 |
| 5 | 0.2630 | 0.1822 |
| 6 | 0.2555 | 0.1835 |
| 7 | 0.2548 | 0.1926 |
| 8 | 0.2527 | 0.1913 |
| 9 | 0.2513 | 0.1866 |
| 10 | 0.2607 | 0.1901 |
| 11 | 0.2553 | 0.1827 |
| 12 | 0.2665 | 0.1925 |
| 13 | 0.2521 | 0.1953 |
| 14 | 0.2559 | 0.1895 |
| 15 | 0.2533 | 0.1936 |
| 16 | 0.2648 | 0.1773 |

