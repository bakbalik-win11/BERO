# GRV-004 — Dört kanal ADC: MIN / MAX / ORT / STD logu

- Tarih: 2026-10-10
- Cihaz: `esp32d1`; ESPHome 2026.9.1; ESP-IDF
- Pinler: GPIO32 BIAS, GPIO33 1T, GPIO34 2T, GPIO35 3T
- Test yapılandırması: `update_interval: 10ms`; kanal başına 1000 örnek hedefi; sürekli turlar; PZEM yok.
- Yeni kod snapshot'ı: [STD sürümü YAML](KOD/esp32d1-4ch-1000-min-max-avg-std-continuous-20261010.yaml)
- Yeni cihaz logu: [esp32d1-logs (12).txt](LOG/esp32d1-4ch-adc-std-20261010-logs-12.txt)
- Önceki STD'siz sürüm korunmuştur: [önceki YAML](KOD/esp32d1-4ch-1000-min-max-avg-continuous-20261010.yaml)

## Logun gösterdiği

- API bağlantısı ve handshake başarılı.
- TUR=1–18 arası 18 adet `ADC_TEST` satırı var.
- Her satır BIAS/K1/K2/K3 için MIN, MAX, avg ve std değerleri içeriyor.
- Tur satırları yaklaşık 10,6 saniye aralıklarla geliyor.
- Bir adet `safe_mode took a long time for an operation (66 ms), max is 50 ms` uyarısı görünüyor.
- İki ESP32 optimizasyon önerisi de logda mevcut; bu logda derlemeyi engelleyen hata görünmüyor.

## Teknik notlar

- Kod, standart sapmayı `sqrt(E[x²] - E[x]²)` biçiminde hesaplıyor. Bu, N ile bölen **popülasyon standart sapmasıdır**; N−1 kullanan örnek standart sapması değildir.
- Negatif kayan nokta varyansı sıfıra kırpılıyor.
- Logda 18 tur sonuç üretilmiş olması, her turda sayaçların 1000'e ulaştığını doğrudan göstermiyor; sayaçlar satırda raporlanmıyor. Bu yüzden 1000 örnek/kanal/tur koşulu bağımsız doğrulanmış olarak işaretlenmedi.
- Log, tam olarak hangi YAML'ın cihaza yüklendiğini tek başına kanıtlamaz. YAML ayrı bir kullanıcı-kod snapshot'ı olarak saklanmıştır; derleme sonucu ayrıca doğrulanmalıdır.
- Bu log ham örnekleri içermiyor; dolayısıyla ORT/STD değerleri ham örneklerden bilgisayarda yeniden hesaplanıp karşılaştırılamaz.

## Örnek — TUR=1

- BIAS: avg 1.66274 V, std 0.008191 V
- 1T: avg 1.66150 V, std 0.013758 V
- 2T: avg 1.66027 V, std 0.008648 V
- 3T: avg 1.65603 V, std 0.006849 V

Bu sayılar cihazın bildirdiği özetlerdir; ham örneklerden bağımsız hesaplanmış değildir.

## Durum

- [x] STD alanları içeren 18 sonuç satırı loglandı.
- [x] Yeni STD kod snapshot'ı ayrı dosya olarak arşivlendi.
- [ ] Her turdaki 1000 örnek/kanal sayısı doğrudan doğrulanmadı.
- [ ] Ham örneklerden bağımsız ORT/STD hesabı yapılmadı.
- [ ] Arşivlenen YAML'ın bu logu üreten birebir derlenmiş sürüm olduğu doğrulanmadı.
- [ ] Sonraki alt görev: ham örnekleri dışarı aktarıp ORT/STD hesabını bilgisayarda bağımsız doğrulamak.
