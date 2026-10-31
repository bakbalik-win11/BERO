# Faz 2 açık soruları

Bu dosya yalnız aktif Faz 2 çalışmasında gerçekten cevaplanması gereken soruları tutar. Faz 1'in eski ADC, gürültü tabanı, örnekleme hızı ve analog ön uç soruları ana hedefe ulaşıldığı için kapatılmıştır; yeniden açılmaz.

## T007 — Home Assistant → PC veri aktarımı

1. Home Assistant'taki gerçek PZEM entity_id'leri hangileri?
2. Mevcut SCT ölçüm yolunun hangi entity_id'leri kullanılacak (SCT akım ve Raw AC dahil)?
3. HA geçmişini PC'ye almak için mevcut erişim koşullarında en basit ve tekrar çalıştırılabilir yöntem hangisi?
4. Gerçek dışa aktarılan örneğin dosya biçimi, alanları, timestamp/timezone gösterimi ve boyutu nedir?
5. Dışa aktarımda state değişimleri mi, belirli aralıkla örnekler mi bulunuyor? Gerçek veri görüldükten sonra karar verilecek.

## T008 — Kararlı alan eşleştirme

1. PZEM ve SCT entity'lerinin gerçek güncelleme aralıkları ve timestamp boşlukları nasıl?
2. Her iki akış için ayrı kararlılık ölçütlerini hangi gerçek kayıt özellikleri destekliyor?
3. Aynı yük olayında örtüşen kararlı alanları seçmek için hangi zaman eşleştirme yaklaşımı yeterli?
4. Geçersiz PZEM okumaları ve eksik/tekrarlı kayıtlar veri setinde nasıl raporlanacak?

## T006 — Katsayı/model

1. Etiketlenmiş kararlı alanlarda K=24.22'nin sapması yük/akım aralığına göre nasıl değişiyor?
2. Sistematik ve tekrarlanabilir hata var mı; yoksa mevcut katsayıyı korumak mı doğru?
3. Yeni katsayı veya model gerekirse en basit yeterli yöntem ve yeni calibration_id nasıl sürümlenecek?

## Şimdilik karar verilmemişler

- HA aktarım yöntemi, entity_id listesi ve dışa aktarım biçimi.
- Kararlılık penceresi süresi/eşikleri ve eşleştirme toleransı.
- Python program/modül sayısı ve eğitim veri kümesi biçimi.

Bu alanlar gerçek HA örneği PC'ye alınmadan tahmin edilmeyecek. İlk aktif iş T007'dir.
