# MOD2-GRV001 V1.0 – Yüksek yük kararlı pencere analizi

**Tarih:** 2026-11-21  
**Modül:** Modül 2 – Masaüstü akım test düzeneği  
**ADS1115:** Fiziksel modül No.10  
**Test edilen yazılım:** V1.0 – katsayı 30.66  
**Sonuç:** V1.0 yüksek yük analizi tamamlandı; V1.1 için 27.59 deney katsayısı belirlendi.

## 1. Amaç

V1.0 kodunda kullanılan 30.66 katsayısının 150 W üzerindeki yüklerdeki davranışını incelemek ve yeni ölçümlerde denenmek üzere yüksek yük katsayısını hesaplamak.

PZEM akımı karşılaştırma referansıdır; kusursuz ground truth olarak değerlendirilmez.

## 2. Veri kaynağı ve yöntem

Kaynak dosya: kullanıcının sağladığı `history (2).csv`  
Kayıt tarihi: 2026-11-21  
Kayıt aralığı: 16:10–16:38 (Türkiye yerel saati, CSV zaman damgaları UTC olarak tutulmuştur).

Aşağıdaki dört kararlı pencere kullanıldı. Yük geçişleri, kapalı/yüksüz bölümler ve geçiş sıçramaları ortalamalara alınmadı. PZEM'in yaklaşık 5 saniyelik kayıtları ile ESP32D2'nin yaklaşık 1 saniyelik kayıtları aynı zaman pencerelerinde ayrı ayrı ortalandı; örnek sayıları eşit değildir.

## 3. Kararlı pencere sonuçları

| Pencere | Yerel zaman | PZEM güç ort. | PZEM akım ort. | PZEM n | SCT akım ort. | SCT n | Gerekli katsayı |
|---|---|---:|---:|---:|---:|---:|---:|
| HH-01 | 16:27:28–16:28:08 | 2335.55 W | 10.55000 A | 8 | 11.68526 A | 40 | 27.68 |
| HH-02 | 16:29:28–16:30:38 | 1821.65 W | 8.16950 A | 14 | 9.08494 A | 70 | 27.57 |
| HH-03 | 16:34:03–16:34:48 | 1534.10 W | 6.83100 A | 9 | 7.67067 A | 45 | 27.30 |
| HH-04 | 16:36:33–16:37:33 | 773.13 W | 3.40083 A | 12 | 3.74983 A | 60 | 27.81 |

### Katsayı hesabı

V1.0 katsayısı 30.66 olduğundan her pencere için:

`K_yeni = 30.66 × (I_PZEM_ortalama / I_SCT_ortalama)`

Pencere bazında katsayılar:

- HH-01: 27.6813
- HH-02: 27.5706
- HH-03: 27.3038
- HH-04: 27.8065

Dört pencerenin katsayılarının eşit ağırlıklı aritmetik ortalaması:

`(27.6813 + 27.5706 + 27.3038 + 27.8065) / 4 = 27.5905`

İki ondalık basamağa yuvarlanan deneme katsayısı: **27.59**.

Pencere ortalamalarının tümünü birleştirerek bulunan oran yaklaşık 27.57'dir. V1.1 için seçilen 27.59, dört kararlı pencerenin katsayılarına eşit ağırlık veren ortalamadır.

## 4. V1.0 değerlendirmesi

Dört kararlı pencerenin tamamında V1.0'ın 30.66 katsayısı ile hesaplanan SCT akımı PZEM karşılaştırma akımından yüksektir. Bu pencerelerde SCT'nin PZEM'e göre farkı yaklaşık %10.3–%12.3 aralığındadır.

Pencere bazında gerekli katsayıların 27.30–27.81 aralığında toplanması, bu yüksek yük veri kümesinde 27.59 civarında bir katsayının denenmesini desteklemektedir.

Bu sonuç, 27.59'un doğrulanmış nihai katsayı olduğu anlamına gelmez. Yalnızca ADS1115 No.10 ve bu deney zinciri için sonraki testte kullanılacak aday değerdir.

## 5. Sürüm geçiş kararı

- V1.0 YAML ve 30.66 katsayısı değiştirilmeden korunur.
- Bu rapor V1.0 ile alınan yüksek yük verisinin analizini kapatır.
- Yeni deneme sürümü V1.1'de katsayı 27.59 olarak uygulanmıştır.
- V1.1'in başarısı, yeni kararlı ölçümlerle ayrıca değerlendirilecektir.
- Kod 0 ve V1.0 geriye dönük değiştirilmez.

## 6. Veri kayıtları

- Kararlı pencere veri özeti: `V1.0/LOG/YUKSEK-YUK-KARARLI-PENCERELER-2026-11-21.csv`
- Bu rapor: `V1.0/RAPOR/YUKSEK-YUK-KATSAYI-ANALIZI-2026-11-21.md`
- Kaynak: kullanıcının sağladığı `history (2).csv` dosyası.

CSV eki, seçilen dört kararlı pencerenin ortalamalarını, örnek sayılarını, standart sapmalarını ve pencere bazında katsayıları içerir. Tam kaynak history dışa aktarımının kendisi bu dosya değildir.

## 7. Aşama durumu

| İş | Durum |
|---|---|
| V1.0 yüksek yük kararlı pencerelerinin analizi | Tamamlandı |
| Pencere katsayılarının hesaplanması | Tamamlandı |
| 27.59 aday katsayısının seçilmesi | Tamamlandı |
| Veri özeti ve raporun depoya kaydı | Bu kayıtla tamamlandı |
| V1.1 kodunun hazırlanması | Hazır |
| V1.1 cihaz yüklemesi ve yeni test | Bekliyor |
| 27.59 katsayısının doğrulanması | Bekliyor |

**Aşama 1 kapanış kararı:** V1.0 yüksek yük analizi tamamlandı. Bir sonraki deney V1.1 / 27.59 katsayısının doğrulama testidir.
