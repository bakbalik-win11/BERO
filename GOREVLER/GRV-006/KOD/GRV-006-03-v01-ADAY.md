# GRV-006-03 v01 — Python → ESPHome Native API → geri okuma adayı

**Durum:** Taslak; derlenmedi, cihazda denenmedi. Çalışan v06 değiştirilmedi.

## Hedef ve ekipman
- ESP: mevcut `esp32d1`, IP kaydı GRV-004 raporundaki `192.168.0.8` (ağ adresi değişmiş olabilir).
- ESPHome Native API, TCP 6053.
- Python 3.10+ ve `aioesphomeapi`.
- Deneme değeri 120; sentetik test değeridir, sensör ölçümü değildir.

## Dosyalar
- Aday YAML: [GRV-006-03-v01-ADAY.yaml](GRV-006-03-v01-ADAY.yaml)
- Python istemcisi: [GRV-006-03-v01-python-api-echo.py](GRV-006-03-v01-python-api-echo.py)

## Tasarım
Aday YAML, mevcut GRV-005-14 v06'nın kopyasıdır. Native API altında `grv006_set_value` eylemi tanımlanır; eylem gelen tamsayıyı `GRV006 Echo Value` template sensöründe yayımlar ve loga yazar. Python istemcisi API'ye bağlanır, eylemi çağırır ve aynı sensör durumunu geri okuyup 120 ile karşılaştırır.

## Önemli ön koşul / teknik risk
ESPHome Native API eylem çağrısının Python istemci kütüphanesindeki kesin çağrı imzası ve state aboneliği, kullanılan `aioesphomeapi` sürümünde henüz çalıştırılarak doğrulanmadı. Bu nedenle Python dosyası da **adaydır**; API sürümüne göre uyarlama gerekebilir. API şifrelemesi/parolası varsa ilgili ortam değişkenleri gerekir. Kimlik bilgileri bu dosyaya yazılmamalıdır.

## Çalıştırma planı
1. Aday YAML'ı ESPHome 2026.9.1 ile derle; v06'ya dokunma.
2. Derleme başarısızsa hata çıktısını kaydet, çalışan cihazı değiştirme.
3. Derleme başarılı olsa bile cihaza yükleme öncesi kullanıcı onayı al.
4. Yükleme sonrası Python istemcisini test et; ancak `SENT` ve `ECHOED` aynı değerdeyse PASS.
5. Servis çağrısı başarılı görünse bile echo state okunamazsa PASS deme.

## Başarı ölçütü
Terminalde gönderilen değer ve ESP'den geri okunan değer açıkça aynı görünür; örneğin `SENT: 120`, `ECHOED: 120`, `RESULT: PASS`. Bu yalnızca API veri aktarımı testidir, ADC/SCT ölçüm doğruluğu değildir.
