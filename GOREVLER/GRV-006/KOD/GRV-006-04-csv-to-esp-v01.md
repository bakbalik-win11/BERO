# GRV-006-04 — CSV → Python → ESP echo

**Hedef:** Kaydedilmiş BERO CSV dosyasındaki `adc_rms_ac` değerlerini topla, sonucu bağımsız yeniden okuma hesabıyla doğrula, tamsayı olarak ESP'ye gönder ve echo sensöründen geri oku.

## Kullanım
1. Python dosyasını ve CSV'yi aynı klasöre koy.
2. Sanal ortam açıkken çalıştır: `python GRV-006-04-csv-to-esp-v01.py`
3. Başka CSV kullanmak için `GRV006_CSV` ortam değişkenini dosya yoluna ayarla.

Varsayılan girdi: `GRV-005-14-v06-QC-GIRDİSİ-20261011.csv`.

## Önceki çalıştırmanın kanıtı
Kullanıcı Mac mini Terminal çıktısı:
- CSV: 4 satır okundu.
- CH0-1T=15.038437; CH1-2T=9.631619; CH2-3T=12.415383.
- Toplam=37.085439; gönderilen tamsayı=37085.
- Bağımsız kontrol=37085.
- ESP'ye gönderilen=37085; geri okunan=37085.0.
- Sonuç: `PASS — CSV processed value returned by ESP`.

## Kanıt sınırı
Girdi, daha önce kaydedilmiş örnek CSV'dir; yeni canlı SCT ölçümü değildir. Bu deney fiziksel akım doğruluğunu kanıtlamaz. `invalid_count` alanı `NOT_TRACKED` olduğundan geçersiz örnek sayısı bilinmiyor.

Geçmiş sürümler korunur; bu dosya yeni, ayrı kayıt olarak eklenmiştir.
