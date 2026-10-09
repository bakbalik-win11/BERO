# Hesaplama-3 — Modbus ve ölçüm doğrulama

## Devreye alma
1. Modelin PZEM-014 olduğuna (10 A dahili şönt) emin ol.
2. USB–RS485 adaptörünün sürücüsünü ve COM/tty portunu doğrula.
3. 9600 8N1 ve slave adresini kılavuzdan kontrol et.
4. İlk sorgularda yalnızca okuma işlevi kullan.
5. Ham register değerlerini ve yanıt/CRC durumunu kaydet.
6. Register adresi ve ölçek katsayılarını aynı cihaz revizyonunun kılavuzuyla eşleştir.
7. Gerilim, akım, güç, PF, frekans ve enerji değerlerini referans cihazla karşılaştır.

## Hata ayıklama
- Yanıt yok: A/B yönü, seri port, baud, slave ID, besleme ve cihaz sürümü.
- CRC hatası: kablo, parazit, baud ayarı, sonlandırma/topoloji.
- Yanlış ölçek: register adresi ve birim/çarpan uyuşmazlığı.
- P=V×I ile uyuşmuyor: güç faktörü ve dalga biçimini dikkate al.

Modbus 0x41 kalibrasyon ve 0x42 enerji sıfırlama işlevleri rutin okuma için değildir. Şebeke bağlantıları yetkin elektrikçi gözetiminde yapılmalıdır.