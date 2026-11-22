# Birleşik Yük Kademeleri Analizi – ADS1115 No.10 / A0–A1

**Tarih:** 2026-11-22  
**Görev:** MOD2-GRV001  
**Kaynak:** Kullanıcının sağladığı `150-42-57-100.csv` (2.675 satır; HA Recorder dışa aktarımı)  
**ADC:** ADS1115 No.10, I²C 0x48  
**Kontrol kartı:** ESP32D2  
**Sensör:** SCT013 30A/1V  
**Kanal:** A0–A1  
**Hesapta kullanılan mevcut katsayı:** K=27.59  
**Durum:** Kararlı kademe analizi; yük bazlı katsayılar ön sonuçtur. K=27.59 değiştirilmemiştir.

## 1. Analiz yöntemi

Dört yük kademesi, PZEM akımının sıfır olmadığı ve açılış/kapanış geçişlerinin dışında kalan zaman pencereleriyle incelendi. Her pencere için SCT ve PZEM örnekleri ayrı ayrı pencere içine alındı; ortalamalar üzerinden:

`K_yeni = 27.59 × (PZEM akım ortalaması / A0–A1 akım ortalaması)`

hesaplandı. PZEM karşılaştırma referansıdır; ground truth kabul edilmez. PZEM ve SCT örnekleme sıklıkları farklıdır; bu özet, aynı pencere içindeki ortalamaların karşılaştırmasıdır.

## 2. Kararlı kademe sonuçları

| Yük | UTC penceresi | PZEM akım ort. (std) | PZEM güç ort. | A0–A1 ort. (medyan) | A0–A1 std (n) | Sapma, K=27.59 | Örtüşen K |
|---|---|---:|---:|---:|---:|---:|---:|
| 150 W | 08:06:38–08:10:45 | 0.6411 A (0.0011 A) | ~146.2 W | 0.5896 A (0.5896 A) | 0.0034 A (247) | -8.03% | **30.00** |
| 42 W | 08:15:03–08:21:00 | 0.1873 A (0.0009 A) | ~42.4 W | 0.1538 A (0.1538 A) | 0.0025 A (357) | -17.85% | **33.58** |
| 57 W | 08:21:58–08:27:30 | 0.2643 A (0.0008 A) | ~60.3 W | 0.2190 A (0.2189 A) | 0.0017 A (332) | -17.14% | **33.30** |
| 100 W | 08:28:38–08:38:40 | 0.4701 A (0.0011 A) | ~107.6 W | 0.4231 A (0.4209 A) | 0.0067 A (602) | -9.99% | **30.65** |

Örnek sayıları, ortalamalar ve katsayılar kaynak CSV'den yeniden hesaplanmıştır. Yuvarlama nedeniyle tabloda son basamak farkları görülebilir.

## 3. Gözlemler

- 42 W ve 57 W pencerelerinde PZEM akım standart sapması yaklaşık 0.0008–0.0009 A iken A0–A1 ölçümü PZEM ortalamasına göre sırasıyla %17.85 ve %17.14 daha düşüktür. Katsayılar 33.58 ve 33.30'dur.
- 100 W ve 150 W pencerelerinde fark sırasıyla %9.99 ve %8.03 seviyesine iner. Katsayılar 30.65 ve 30.00'dır.
- Dört pencere, tek bir sabit K'nın tüm bu yük seviyelerinde aynı uyumu vermediğini gösterir. Düşük akım grubu (42/57 W) ile daha yüksek akım grubu (100/150 W) arasında belirgin bir katsayı ayrışması vardır.
- Bu gözlem tek başına nedenin yalnızca akım seviyesi olduğunu kanıtlamaz. Sensör/kanal, analog bağlantı, bias durumu ve YAML sürümünün deneyler arasında aynı olduğu ayrıca doğrulanmalıdır.

## 4. 100 W penceresindeki iç seviye değişimi

100 W penceresinin tamamı tek bir kararlı A0–A1 seviyesi değildir. İlk yaklaşık 230 saniyede A0–A1 ortalaması yaklaşık 0.4309 A; sonraki bölümde yaklaşık 0.4183 A'dır. PZEM her iki bölümde de yaklaşık 0.470 A seviyesinde kalır.

| Alt pencere | A0–A1 n | A0–A1 ort. | PZEM n | PZEM ort. | PZEM std | Güç ort. | Bu alt pencerenin K'sı |
|---|---:|---:|---:|---:|---:|---:|---:|
| 08:28:38–yaklaşık 08:32:28 UTC | 230 | 0.430886 A | 20 | 0.470550 A | 0.001234 A | 107.87 W | **30.13** |
| Yaklaşık 08:32:28–08:38:40 UTC | 372 | 0.418343 A | 19 | 0.469632 A | 0.000761 A | 107.47 W | **30.97** |

Bu nedenle 100 W penceresinin tamamından çıkan K=30.65, iki farklı A0–A1 seviyesinin birleşik ortalamasıdır; tek bir homojen kararlı kademe katsayısı olarak yorumlanmamalıdır. Seviye değişiminin fiziksel/yazılımsal nedeni bu CSV tek başına belirlenemez.

08:38:41 UTC'de A0–A1 değeri sıfıra iner; 08:38:43 UTC civarında PZEM akımı da sıfıra iner. Sonraki kayıtlar yükün kapanışından sonraki bölümdür ve kararlı akım katsayısı hesabına alınmamıştır.

## 5. Teknik yorum ve karar sınırları

1. 42/57 W katsayıları kendi aralarında yakın; 100/150 W katsayıları da kendi aralarında yakındır.
2. 100 W penceresindeki iki seviyeli davranış ayrıca incelenmelidir. Bu pencerenin tek K değeri iki alt seviyeyi gizlemektedir.
3. Bu dört katsayı ön sonuçtur; tek ortak düşük bölge katsayısı henüz seçilmemiştir.
4. Bias durumu ve kullanılan YAML dosyası/sürümü birleşik CSV'den kesin olarak doğrulanamıyor. Bu nedenle sonuçlar “aynı biassız konfigürasyonla doğrulanmış seri” olarak ilan edilmez.
5. PZEM referans alınmıştır; PZEM'in mutlak doğruluğu varsayılmamıştır.
6. Mevcut YAML ve K=27.59 korunur. Bu analiz tek başına firmware/YAML değişikliği talimatı değildir.
7. Sonraki ampul kademesi verileri ve konfigürasyon teyidi görülmeden katsayı birleştirme yöntemi seçilmez.

## 6. Kaynak ve tekrar üretilebilirlik

- Kaynak CSV: `150-42-57-100.csv` (bu raporun oluşturulmasında kullanıcı tarafından sağlandı; CSV'nin kendisi bu raporla birlikte depoya yüklenmedi).
- Zaman damgaları UTC'dir.
- İlgili katsayı geçmişi: `../RAPORLAR/KATSAYI-RAPORU-ADS1115-NO10-SCT013.md`.
