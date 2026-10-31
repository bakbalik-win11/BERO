# T007 — Home Assistant verisini PC'ye aktarma ve Python başlangıcı

- **Durum:** BEKLEMEDE — pratik modül devreye alma sonrasında
- **Faz:** Faz 2 — Pratik yeniden kurulum ve sistem geliştirme (veri aktarımı alt aşaması)
- **Bağımlılık:** T009 kapsamında PZEM ve SCT düğümlerinin temel işlevlerinin gerçek donanımda çalışması ve Home Assistant'ta gerçek entity üretmesi.
- **Hedef:** Home Assistant'ta kaydedilen PZEM ve SCT entity geçmişlerini PC'ye taşıyacak, kaynak bilgilerini koruyacak ve aynı veri üzerinde tekrar çalıştırılabilecek en küçük Python veri giriş hattını kurmak.

## Neden T009 sonrasında?

Veri aktarımı için önce PZEM ve SCT düğümlerinin gerçek veriyi Home Assistant'a yayınlıyor olması gerekir. Faz 2'nin ilk hedefi veri analizi değil, modülleri pratik olarak yeniden devreye alıp temel işlevlerini doğrulamaktır. T009 kabul koşulları karşılandıktan ve gerçek entity listesi görüldükten sonra T007 başlatılır.

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
- **SONUÇ:** T007 BEKLEMEDE. PZEM/SCT düğümleri T009 kapsamında çalıştırılıp gerçek entity'leri doğrulanınca açılacaktır.
