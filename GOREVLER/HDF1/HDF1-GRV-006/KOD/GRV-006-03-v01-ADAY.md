# GRV-006-03 v01 — Python → ESPHome Native API → geri okuma adayı

**Durum (2026-10-11):** Kullanıcının paylaştığı ESPHome logunda derleme bilgisi (`ESPHome 2026.9.1`, compiled 2026-10-11 18:19:09 +0300) ve `esp32d1 @ 192.168.0.9` API bağlantısı/handshake görülüyor. Python eylem çağrısı ve geri okuma henüz doğrulanmadı. Çalışan v06 dosyası değiştirilmedi.

## Hedef ve ekipman
- ESP: mevcut `esp32d1`, son kullanıcı logunda `192.168.0.9`. Python varsayılan adresi de bu loga göre güncellendi.
- ESPHome Native API, TCP 6053.
- Python 3.10+ ve `aioesphomeapi`.
- Deneme değeri 120; sentetik test değeridir, sensör ölçümü değildir.

## Dosyalar
- Aday YAML: [GRV-006-03-v01-ADAY.yaml](GRV-006-03-v01-ADAY.yaml)
- Python istemcisi: [GRV-006-03-v01-python-api-echo.py](GRV-006-03-v01-python-api-echo.py)

## Tasarım
Aday YAML, mevcut GRV-005-14 v06'nın kopyasıdır. Native API altında `grv006_set_value` eylemi tanımlanır; eylem gelen tamsayıyı `GRV006 Echo Value` template sensöründe yayımlar ve loga yazar. Python istemcisi API'ye bağlanır, eylemi çağırır ve aynı sensör durumunu geri okuyup 120 ile karşılaştırır.

## Teknik durum ve sınırlar
- YAML için kullanıcı derleme/cihaz logu sağladı; logda `INFO Loaded validated config cache ... skipping validation` satırı bulunduğundan bu kopyada ayrıca tam doğrulama çıktısı görünmüyor. Kullanıcı derlendiğini bildirdiği için derleme sonucu kullanıcı beyanıyla kayda alındı.
- ESPHome API bağlantısı ve handshake başarılı; cihaz adresi `192.168.0.9` olarak görünüyor.
- Bu logda `GRV006_RECEIVED` satırı, Python'dan gönderilen değer veya `ECHOED` sonucu yok. Dolayısıyla Python → ESP → geri okuma testi henüz PASS değil.
- Python istemcisi, `aioesphomeapi` kaynak kodundan kontrol edilen `list_entities_services()` ve `execute_service(service, data)` biçimini kullanacak şekilde güncellendi; fakat kullanıcı ortamında çalıştırılmadı.
- API şifrelemesi açıksa `ESPHOME_NOISE_PSK` ortam değişkeni kullanılmalı; gizli anahtar dosyaya yazılmamalıdır.

## Çalıştırma planı
1. Aday YAML'ı ESPHome 2026.9.1 ile derle; v06'ya dokunma.
2. Derleme başarısızsa hata çıktısını kaydet, çalışan cihazı değiştirme.
3. Derleme başarılı olsa bile cihaza yükleme öncesi kullanıcı onayı al.
4. Yükleme sonrası Python istemcisini test et; ancak `SENT` ve `ECHOED` aynı değerdeyse PASS.
5. Servis çağrısı başarılı görünse bile echo state okunamazsa PASS deme.

## Başarı ölçütü
Terminalde gönderilen değer ve ESP'den geri okunan değer açıkça aynı görünür; örneğin `SENT: 120`, `ECHOED: 120`, `RESULT: PASS`. Bu yalnızca API veri aktarımı testidir, ADC/SCT ölçüm doğruluğu değildir.


## 2026-10-11 — Derleme ve API bağlantısı kaydı

Kullanıcı, ESPHome 2026.9.1 logunu paylaştı. Derleme bilgisi: `2026-10-11 18:19:09 +0300`; ESP32 rev3.1, 2 çekirdek; cihaz `192.168.0.9`; API çözümleme, bağlantı ve handshake başarılı. Logun kullanıcı tarafından gönderilen parçası `[18:23:17.784]` satırında bitiyor; bu nedenle kayıt yalnızca görünen satırları kapsar. Python eylem çağrısı ve geri okuma henüz kanıtlanmadı.

Tam görünen log: [GRV-006-03 cihaz logu](../RAPOR/GRV-006-03-v01-CIHAZ-LOGU-20261011.md).
