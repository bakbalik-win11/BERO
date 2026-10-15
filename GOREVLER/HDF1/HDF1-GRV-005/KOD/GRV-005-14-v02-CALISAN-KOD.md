# PROJE BERO — GRV-005-14 v02 Çalışan Kod Kaydı

- Tarih: 2026-10-11
- Kaynak: Kullanıcının sağladığı `Yapıştırılan metin(20261011-112457).txt`
- Kaydedilen kaynak: [GRV-005-14-v02-CALISAN-KOD.yaml](./GRV-005-14-v02-CALISAN-KOD.yaml)
- ESPHome cihaz adı: `esp32d1` (korundu)
- Derleme/çalışma kanıtı: Kullanıcının paylaştığı ESPHome 2026.9.1 cihaz logu; derleme zamanı 2026-10-11 14:21:41 +0300, API bağlantısı başarılı, CH0/CH1/CH2/BIAS için 1000 örnekli satırlar ve PZEM değerleri görülüyor.

## Kaynak koruma notu

YAML, kullanıcının verdiği kaynak metinden içerik değiştirilmeden kaydedildi. Kaynağın üst açıklamasında hâlâ “derleme öncesi aday” uyarısı bulunuyor; bu metin kaynakla birebirliği korumak için sessizce değiştirilmedi. Çalışma logu bu kaynakla aynı derleme dosyası olduğunu tek başına kriptografik olarak doğrulamaz; kayıt, kullanıcının bu dosyayı çalışan kod olarak belirtmesine dayanır.

## Kapsam ve bilinen sınırlar

- GPIO33: CH0-1T
- GPIO34: CH1-2T
- GPIO35: CH2-3T
- GPIO32: BIAS
- UART GPIO16/GPIO17, 9600 baud: PZEM
- Her ADC hattı için 1000 örnek; tek rapor penceresi.
- Başlık ve dört satır ESPHome loguna yazılır; bu kod yerel CSV dosyası oluşturmaz ve otomatik yeni pencere başlatmaz.
- `pzem_update_millis`, gerçek Modbus yanıt zaman damgası olarak garanti edilmez.
- Çalışma logunda `invalid_count=NOT_TRACKED` ve boş zaman damgası alanları görülüyor; CSV/QC hizalaması ayrıca değerlendirilmelidir.

Bu kayıt yeni bir sürüm kaydıdır; eski raporlar ve deney geçmişi korunur.
