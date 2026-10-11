# PROJE BERO — GRV-005-14 v05 Aşamalı Raporlama Adayı

**Tarih:** 2026-10-11  
**Kaynak:** GRV-005-14 v04 çalışan kodu ve 14:44:55–14:45:08 cihaz logu.

## Neden v05?

v04'te CSV başlığı ve dört veri satırı doğru hizalanmış olsa da, raporlamadan hemen sonra şu uyarı sürdü:

`interval took a long time for an operation (92 ms), max is 50 ms`

v03'teki uyarı ADC sensör bileşeni adına görünürken v04'te interval bileşeni adına görünüyordu. Bu durum raporlama zincirindeki uzun, senkron işlemle ilişkili olabileceğini düşündürüyor; tek başına kesin neden kanıtı değil.

## Adaydaki değişiklikler

- Rapor başlangıcı ve zaman alanları ilk kısa lambda içinde bir kez sabitlenir.
- CSV başlığının iki parçası ayrı lambda adımlarıyla yazdırılır.
- CH0, CH1, CH2 ve BIAS satırları ayrı lambda adımlarına ayrılır.
- Log adımları arasına 20 ms `delay` eklenir; script'in uzun raporlamayı tek bir C++ lambda içinde yapmaması amaçlanır.
- Cihaz adı `esp32d1`, pinler, örnek sayısı ve CSV alan sırası korunmuştur.
- Aday, v04'ün üzerine yazılmamıştır.

## Beklenen doğrulama

1. ESPHome 2026.9.1 ile derleme.
2. Derleme başarılı olursa ayrı çalışan kod kaydı oluşturma.
3. Gerçek cihazda 4 x 1000 örnek, başlığın 16+25 alanı ve dört adet 41 alanlı satır kontrolü.
4. 92 ms uyarısının kaybolup kaybolmadığını kontrol etme.
5. Raporlama aralığının ADC örnek toplamasını etkileyip etkilemediğini inceleme.

## Sınırlar

Bu yalnızca aday YAML'dır; derlenmemiştir ve cihaza yüklenmemiştir. Gecikmelerin uyarıyı kesin kaldıracağı garanti edilmez. Loglama hâlâ ESPHome ana döngüsünde yapılır. Eğer uyarı sürerse bir sonraki seçenek, satırları ayrı aşamalarda üretmekten de ileri giderek veriyi ayrı bir aktarım/yazma yoluyla çıkarmak olacaktır.

## Dosya

`GOREVLER/GRV-005/ADAYLAR/GRV-005-14-v05-ASAMALI-RAPORLAMA-ADAYI.yaml`
