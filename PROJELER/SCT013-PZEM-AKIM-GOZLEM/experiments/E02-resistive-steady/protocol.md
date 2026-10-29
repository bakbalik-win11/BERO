# E02 — Kararlı rezistif yük

## HEDEF
Kararlı rezistif yük altında SCT pencere istatistiklerinin tekrarlanabilirliğini ve PZEM referans akışına göre farkını gözlemek. Bu deney PZEM'i kusursuz referans veya bağımsız kalibrasyon standardı saymaz.

## Başlangıç hipotezi
**HİPOTEZ —** Bu projede deneyle doğrulanmadı; sonuç gibi raporlanamaz.

## Koşullar ve prosedür
1. Kullanılan SCT modeli, ESP32 kartı/GPIO'su, firmware sürümü, yük ve güvenlik koşullarını kaydet.
2. SCT verisini ve PZEM okumalarını aynı test oturumunda topla; istek/yanıt zamanlarını ve geçersiz okuma durumlarını koru.
3. Yalnızca deney verisiyle kararlı olduğu belirlenen alanları karşılaştır. Sabit bir saniye maskesini veya önceden seçilmiş kararlılık eşiğini doğrulanmış kural sayma.
4. SCT pencere değişkenliğini, geçerli PZEM okuma oranını ve PZEM'e göre farkı raporla. Sıfır/geçersiz PZEM okumaları yüzde sapma hesabına katılmaz.
5. Ham veri, özetler, gerçek örnekleme hızı ve sapmaları deney sonuçlarına bağla.

## Kabul ölçütü
Deney koşulları ve kullanılan kararlı alan seçim yöntemi kayıtlı; pencere değişkenliği, PZEM geçerlilik oranı ve PZEM'e göre fark veriye dayanarak raporlanmış olmalıdır. Ölçüm yapılmadan sonuç yazılmaz.

## Güvenlik
hardware/safety-checklist.md tamamlanmadan şebeke deneyi yapılmaz. Şebeke tarafındaki kurulum yetkin kişi tarafından yapılmalıdır.

## HEDEF / LOG / SONUÇ
- **HEDEF:** Kararlı rezistif yükte pencere istatistiklerini ve PZEM'e uyumu değerlendirmek.
- **LOG:** Gerçek koşullar, veriler, örnek sayıları, gerçekleşen hız, PZEM okuma durumları ve sapmalar.
- **SONUÇ:** Yalnızca kaydedilmiş verinin desteklediği yorum; henüz yapılmadıysa “ölçülmedi”.
