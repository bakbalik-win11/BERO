# LOAD-42W-002 — kısa log incelemesi ve HA geçmiş teşhisi

- **Tarih:** 2026-11-01
- **Kaynak:** `Yapıştırılan metin(20261101-101343).txt`
- **Kaynak boyutu:** 50.257 bayt / 668 satır
- **SHA-256:** `0c316527df2df9105d8745dd1fd009d41c9f7f7150d4e0ea95e0377f8165a3fd`
- **Log aralığı:** 13:12:20.893–13:13:28.860 (+03:00); yaklaşık 68 saniye
- **Firmware build bildirimi/logu:** ESPHome 2026.10.1, 2026-11-01 13:10:25

## HEDEF
Kısa çalışma logunda Modül 2'nin üç SCT sıralı okumasının, ADC başlatmalarının ve sensör yayınlarının çalışmasını kontrol etmek; HA History kaydının neden oluşmadığını kod ile HA katmanı arasında ayırmak.

## LOG — cihaz ve çevrim
- ESP32 rev3.1; Wi-Fi bağlantısı YES; sinyal -62 dB.
- GPIO32/33/34/35 ADC init/config/calibration sonuçları OK.
- Üç ct_clamp sensörü 200 ms sample duration ile yapılandırılmış.
- 34 adet SCT1 başlangıç çevrimi ve her çevrimde SCT1 → SCT2 → SCT3 → bias tamamlanma mesajı gözlendi.
- ERROR, [E] veya Disconnected metni bulunmadı.
- Logda API sunucusu `esp32d1.local:6053` adresinde dinliyor. ESPHome CLI'nin cihaza bağlanması kanıtlıdır; Home Assistant API istemcisinin bağlandığına dair açık bir bağlantı satırı bu kısa logda yoktur.

## LOG — 34 yayınlık özet
| Entity adı | n | Ortalama | Medyan | Min | Maks | Örnek SD |
|---|---:|---:|---:|---:|---:|---:|
| SCT1 Faz 1T Akım | 34 | 0.25106 A | 0.253 A | 0.231 A | 0.266 A | 0.00783 A |
| SCT2 Nötr 1T Akım | 34 | 0.24150 A | 0.2395 A | 0.214 A | 0.308 A | 0.01799 A |
| SCT3 Faz 2T Akım | 34 | 0.34732 A | 0.348 A | 0.329 A | 0.376 A | 0.00941 A |
| SCT1 Raw AC entity | 34 | 0.01037 | 0.010455 | 0.00953 | 0.01098 | 0.00032 |
| SCT2 Raw AC entity | 34 | 0.00997 | 0.00989 | 0.00884 | 0.01272 | 0.00075 |
| SCT3 Raw AC entity | 34 | 0.01434 | 0.014365 | 0.01360 | 0.01553 | 0.00039 |
| Ortak bias | 34 | 1.66147 V | 1.661 V | 1.648 V | 1.675 V | 0.00605 V |

## SONUÇ — ölçüm
- Sıralı okuma çevrimi ve sensör durum yayınları kısa kesitte çalışıyor.
- SCT1 faz 1T ortalaması 0.25106 A; SCT3 faz 2T ortalaması 0.34732 A. SCT3/SCT1 oranı yaklaşık 1.383; bu kesitte 2T için beklenen yaklaşık 2x gözlenmedi. Farkın nedeni bu kısa logdan belirlenemez; sensör/konum/primer geçiş düzeni ve düşük akım koşulu ayrıca kontrol edilmeli.
- SCT2 nötr 1T ortalaması 0.24150 A; bir adet 0.308 A üst uç gözlemi var. Bu tek başına arıza kanıtı değildir.
- Bias ortalaması 1.66147 V; kısa kesitte dar aralıkta.
- Bu 68 saniyelik log, uzun süreli kararlılık kanıtı değildir.

## KOD DENETİMİ — önemli veri birimi hatası
Firmware'de `ct_clamp.on_raw_value` içindeki `x`, ct_clamp bileşeninin filtre öncesi ham akım değeridir. Cihaz logu aynı değeri `Raw AC Value: 0.010A` olarak yazarken YAML bu `x` değerini template entity'ye `V` birimiyle yayımlıyor. Dolayısıyla mevcut `Raw AC` entity'leri volt cinsinden ham ADC/CT gerilimi değildir; birim/semantik yanlış etiketlenmiştir. Bu durum HA geçmişinin oluşmasını engellemez, fakat Raw AC geçmişinin fiziksel anlamını yanlış gösterir. Yeni veri analizi öncesinde ayrı kod düzeltmesi gerekir: ya entity filtre öncesi akım olarak A birimiyle tanımlanmalı ya da gerçek ADC voltajı ayrı bir ölçüm yolu ile alınmalıdır. Bu iki seçenekten biri kullanıcıyla kararlaştırılmadan kod değiştirilmemelidir.

## HA HISTORY — teşhis sınırı
- YAML'da `api:` mevcut; cihaz logunda API server dinliyor. Bu, HA Recorder'ın kayıt yaptığını kanıtlamaz.
- ESPHome log görüntüleyicisinin cihaza bağlanması Home Assistant'ın API bağlantısı ile aynı şey değildir.
- `force_update: true` sensörün aynı değeri yeniden yayımlamasını sağlar; Recorder'ı etkinleştirmez, entity'yi Recorder exclude listesinden çıkarmaz ve veritabanına yazma garantisi vermez.
- Kısa logda HA API istemcisi bağlantısını doğrulayan açık kayıt yok.
- Ayırıcı kontrol: HA Developer Tools → States içinde ilgili yeni sensörlerin state değerleri canlı değişiyor mu? Değişiyorsa ama History boşsa Recorder etkinliği/exclude/purge/DB sorunu incelenmeli. State değişmiyorsa ESPHome entegrasyonu bağlantısı, entity'nin devre dışı olması ve entity_id/registry kontrol edilmeli.
- HA Recorder YAML/ayarları ve HA entity registry bu logdan okunamadığı için kesin kök neden henüz bilinmiyor.

## SONRAKİ ADIM
1. Home Assistant Developer Tools → States'te şu anki SCT1/SCT2/SCT3 akım ve bias entity state'lerinin güncellendiğini doğrula.
2. Canlı state değişiyorsa Recorder ayarını ve exclude listesini kontrol et; değişmiyorsa ESPHome entegrasyon cihaz bağlantısını kontrol et.
3. Raw AC birim düzeltmesini ayrı ve kontrollü değişiklik olarak yap.
4. 2T/SCT1 oranını fiziksel primer geçiş ve sensör yerleşimi teyidiyle tekrar gözle.

**Durum:** Kısa firmware/ölçüm döngüsü LOG İLE DESTEKLENDİ. HA geçmiş sorunu ÇÖZÜLMEDİ. Raw AC birim hatası KOD DENETİMİNDE BULUNDU; henüz firmware değiştirilmedi.
