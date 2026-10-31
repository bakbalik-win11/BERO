# T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı

- **Durum:** AKTİF — Faz 2'nin ilk görevi
- **Faz:** Faz 2 — Bulunan kodu PZEM ile eğitmek
- **Bağımlılık:** Faz 1'de bulunan çalışan SCT ölçüm yolu ve mevcut PZEM-004T V3.0 veri akışı.
- **Hedef:** Home Assistant'ta kaydedilen PZEM ve SCT entity geçmişlerini PC'ye taşıyacak, kaynak bilgilerini koruyacak ve aynı veri üzerinde tekrar çalıştırılabilecek en küçük Python veri giriş hattını kurmak.

## Neden ilk iş bu?

PZEM ve SCT kararlı alanlarını eşleştirebilmek için önce iki akışın aynı PC çalışma alanında, kaynak timestamp'leri bozulmadan bulunması gerekir. Kararlılık algoritması, etiket şeması veya katsayı modeli bu veri yolu görülmeden kesinleştirilmeyecek. Eski E00A/E00/E01 ADC deneyleri T007'nin ön koşulu değildir; Faz 1 hedefe ulaşıldığı için kapatılmıştır.

## Bilinen hedef

- Home Assistant geçmişinden PZEM ve mevcut SCT entity kayıtları alınacak.
- Veriler PC'de Python ile işlenecek.
- Kaynak entity_id, state/value, unit, timestamp ve mevcutsa attributes korunacak.
- PZEM ve SCT farklı güncelleme hızlarında olabilir; aktarım bunları yapay olarak eşitlemeyecek.
- Aynı dışa aktarılan dosya tekrar analiz edilebilir olmalı.

## Bu görevde yapılacaklar

1. Home Assistant'ta gerçek PZEM ve SCT entity_id listesini belirle; tahmin etme.
2. HA geçmişini PC'ye almanın mevcut en basit yolunu seç (ör. HA export/API veya dosya dışa aktarımı); seçim gerçek erişim ve örnek veri üzerinden yapılacak.
3. Küçük bir gerçek örnek dışa aktar ve dosya biçimini/alanlarını incele.
4. Python tarafında dosyayı okuyup satır sayısı, zaman aralığı, entity dağılımı, eksik/geçersiz değer sayısı ve birim özetini çıkar.
5. Kaynak dosya adı, hash'i, aktarım zamanı ve kullanılan kod sürümünü sonuç kaydına ekle.
6. Başarılı kod, örnek log/çıktı ve yorumunu depoda sakla.

## Bu görevde yapılmayacaklar

- Faz 1 deneylerini yeniden açmak.
- Sürekli ham ADC veya 50 Hz dalga kaydı geliştirmek.
- Şimdiden sabit örnekleme/polling aralığı veya kararlılık eşiği belirlemek.
- PZEM ve SCT timestamp'lerini aynı zamana yuvarlamak veya yapay senkronize etmek.
- K=24.22 katsayısını değiştirmek.
- \`ct_clamp\` kaynak kodunu değiştirmek.
- Henüz veri görmeden yeni deney serisi tasarlamak.

## Kabul ölçütü

- Gerçek HA dışa aktarımı PC'ye alınmış ve Python ile açılmış olmalı.
- PZEM ve SCT kayıtları entity_id bazında ayrıştırılabilmeli.
- Timestamp, birim ve kaynak değerleri korunmuş olmalı.
- Aktarım/okuma kodu tekrar çalıştırılabilir olmalı.
- Bir gerçek örnek çıktı/log ve kısa yorumu depoya eklenmiş olmalı.

## HEDEF / LOG / SONUÇ

- **HEDEF:** Faz 2'nin ilk veri yolunu kurmak.
- **LOG:** Henüz bu yeni görev kapsamında HA verisi dışa aktarılmadı ve Python uygulaması yazılmadı.
- **SONUÇ:** T007 AKTİF. İlk somut adım, gerçek HA entity listesini ve dışa aktarılabilir geçmiş örneğini elde etmektir.
