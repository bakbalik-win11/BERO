# MOD2-GRV001 – 100 W akkor ampul dimmer deneyi: PF ve ölçüm farkı

**Tarih:** 2026-11-21  
**Yük:** 100 W akkor ampul  
**Kontrol:** SANEC AC 220 V dimmer  
**Ölçüm:** Modül 3 PZEM akım/PF ve Modül 2 ESP32D2 + ADS1115 No.10 + SCT013 30A/1V  
**Firmware:** V1.1, K=27.59 (değişmedi)  
**Durum:** **KAPATILDI – dimmer ile katsayı/kalibrasyon taraması sürdürülmeyecek.**

## 1. Amaç

Aynı 100 W akkor ampul yükünde dimmer ayarı değiştikçe PZEM'in bildirdiği PF ile PZEM ve SCT/ADS1115 akım okumaları arasındaki ilişkinin gözlenmesi. Amaç yeni katsayı üretmek değil, dimmer koşulunun ölçüm zincirleri üzerindeki etkisini ayırt etmektir.

## 2. Deney koşulları ve veri kaynakları

- Yük: 100 W akkor ampul.
- Dimmer: SANEC AC 220 V.
- PZEM: Modül 3 WROOM.
- SCT ölçüm zinciri: ESP32D2, ADS1115 fiziksel modül No.10, SCT013 30A/1V.
- Firmware V1.1 ve 27.59 katsayısı sabit tutuldu.
- Kaynak kayıt: kullanıcı tarafından sağlanan `history (7).csv` (724 satır; 2026-11-21, UTC zaman damgaları Türkiye saatine çevrildi).
- PZEM PF örnekleri seyrek ve PZEM akım örnekleme aralığı SCT'den uzundur. Pencereler PF'nin sabit kaldığı zaman aralıklarına göre seçildi; örnek sayıları tabloda verildi.

## 3. PF kararlı pencereleri

| PF | Yerel zaman penceresi | PZEM ort. A | PZEM n | SCT ort. A | SCT n | SCT/PZEM | SCT sapması |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1.00 | 18:22:16–18:23:41 | 0.46325 | 4 | 0.42657 | 85 | 0.921 | -7.92% |
| 0.89 | 18:23:51–18:25:06 | 0.42800 | 7 | 0.44343 | 75 | 1.036 | +3.61% |
| 0.73 | 18:25:11–18:26:51 | 0.37656 | 9 | 0.44861 | 100 | 1.191 | +19.14% |
| 0.61 | 18:27:11–18:28:46 | 0.33750 | 8 | 0.50866 | 95 | 1.507 | +50.71% |

Hesaplar:
- `SCT/PZEM = SCT ortalama / PZEM ortalama`
- `SCT sapması (%) = (SCT ortalama - PZEM ortalama) / PZEM ortalama × 100`

## 4. Bulgular

1. PF 1.00 penceresinde SCT ortalaması PZEM ortalamasından %7.92 düşüktür.
2. PF 0.89 penceresinde iki ölçüm birbirine yaklaşmış; SCT PZEM'den %3.61 yüksek kalmıştır.
3. PF 0.73 penceresinde SCT sapması +%19.14'e çıkmıştır.
4. PF 0.61 penceresinde SCT/PZEM oranı 1.507, SCT sapması +%50.71 olmuştur.
5. Seçilen pencerelerde PF azalırken SCT/PZEM oranı belirgin biçimde yükselmiştir. Ölçüm farkının yönü PF 1.00 civarında negatifken daha düşük PF değerlerinde pozitife dönmüştür.

Bu veri, dimmer koşulunda PZEM PF değeri ile PZEM–SCT ölçüm farkı arasında güçlü bir deneysel ilişki gösterir. PF tek başına bağımsız bir neden olarak kanıtlanmış değildir. Dimmerin faz kesmeli akım dalga biçimi hem PF'yi hem de ölçüm zincirlerinin davranışını birlikte değiştirebilir. Teknik yorum, PF'nin tek başına sebep olduğu değil, **dimmerin oluşturduğu çalışma/dalga biçimi koşulunun PF ile birlikte ölçüm farkını değiştirdiği** şeklindedir.

## 5. Pens ampermetre kayıtlarının durumu

UNI-T UT200B+ ile alınan ilk düşük akım okumalarında faz ve nötr iletkenlerinin birbirine yapışık olması nedeniyle pensin tek iletkeni kavramadığı anlaşıldı. Kablolar ayrılmadan alınan 0.25 A, 0.20 A ve 0.10 A gibi okumalar geçersiz kabul edildi ve bu PF analizine dahil edilmedi.

Kablolar ayrıldıktan sonra kullanıcı yeni pens okumaları bildirdi. Ancak bu okumalar otomatik zaman damgalı veri olarak `history (7).csv` içinde bulunmadığından, PF pencereleriyle eşzamanlı hesaplamaya alınmadı. Bu raporun ana bulgusu PZEM–SCT karşılaştırmasına dayanır.

## 6. Deney kararı

**Deney kapatıldı. Dimmerle katsayı alanı veya genel kalibrasyon taraması sürdürülmeyecek.**

Gerekçe:
- Dimmer ayarı akım seviyesini değiştirirken akım dalga biçimini de değiştiriyor.
- PF, dalga biçimi/çalışma koşuluyla birlikte değişiyor.
- Aynı sabit katsayı ile PZEM–SCT ilişkisi bu koşullarda sabit kalmıyor.
- Bu düzenek, normal şebeke koşullarındaki katsayı alanını izole etmek için uygun değil.

## 7. BERO için korunacak sonuç

- PF ile SCT/PZEM ölçüm oranı arasında bu deneyde güçlü, monoton yönlü bir ilişki gözlendi.
- Dimmer altında SCT/ADS1115 ölçümü PZEM ile aynı oranda değişmedi.
- Bulgular dimmerli ölçüm koşuluna özgüdür; normal şebeke kalibrasyonuna genellenmez.
- V1.1 YAML değiştirilmedi.
- K=27.59 korunuyor.
- Dimmer verileri normal kalibrasyon veri grubuna karıştırılmayacak.
- Bu rapor laboratuvar doğrulaması, harmonik analizi veya PF hesaplama çalışması değildir.

## 8. Kayıtlar

- Kararlı pencere özeti: `../LOG/DIMMER-100W-PF-KARARLI-PENCERELER-2026-11-21.csv`
- Kaynak kullanıcı dosyası: `history (7).csv` (724 satır; orijinal dosyanın kendisi bu commit'e eklenmedi).
- Önceki tost makinesi/dimmer üçlü ölçüm gözlem raporu ayrı rapor olarak korunur.
