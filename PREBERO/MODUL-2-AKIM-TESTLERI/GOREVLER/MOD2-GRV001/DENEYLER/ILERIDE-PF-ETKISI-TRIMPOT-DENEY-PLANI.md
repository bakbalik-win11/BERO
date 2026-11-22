# İlerideki PF Etkisi Araştırması – Trimpotlu Faz Kaydırma Düzeneği

**Tarih:** 2026-11-22  
**Modül / görev:** Modül 2 – MOD2-GRV001  
**Durum:** PLANLANDI – fiziksel deney yapılmadı  
**İlişki:** Mevcut akım kalibrasyonu çalışmasından ayrı araştırma

## Amaç

Mevcut SCT013 + ADS1115 A0–A1 akım kalibrasyonu için geliştirilen negatif eğimli K fonksiyonunun başarısını öncelikle ±%4 hata zarfında değerlendirmek. Güç faktörü (PF) etkisini bu kalibrasyon çalışmasına varsayımla dahil etmemek; ileride trimpotla ayarlanabilir faz kaydırma düzeneği kullanılarak PF etkisini ayrı bir deney serisinde incelemek.

## Kullanıcı kararı

- Mevcut doğrusal K fonksiyonu yaklaşımı kabul edilebilir çalışma hipotezidir; başarı ölçütü PZEM akımına göre ±%4 hata zarfıdır.
- Ampul ve birleşik ampul deneyleri mevcut fonksiyonun doğrulaması olarak sürdürülecektir.
- Vantilatör gibi farklı karakteristikteki yükler ayrıca sınanacaktır.
- Trimpotlu faz kaydırma düzeneği, ileride PF etkisini araştırmak için kullanılabilecek ayrı bir deney fırsatı olarak saklanacaktır.
- PF araştırması mevcut kalibrasyon serisine karıştırılmayacaktır.

## Deney henüz yapılmadı – açık teknik noktalar

Trimpotun bulunduğu devrenin gerçek bağlantı topolojisi ve faz kaydırma mekanizması bu kayıtta tanımlı değildir. Trimpotun PF'yi hangi aralıkta ve ne ölçüde değiştirebildiği doğrulanmış değildir. Önce devre şeması/bağlantısı incelenmeli; ardından osiloskopla gerilim-akım faz ilişkisi ve dalga şekli gözlenerek kontrollü değişim doğrulanmalıdır.

Bir faz kaydırma devresinin oluşturduğu sinyal, gerçek bir motor veya başka yükün PF davranışıyla otomatik olarak eşdeğer kabul edilmeyecektir. Aktif güç, RMS akım, gerilim, PF ve SCT/ADS1115 ölçümleri birlikte kaydedilmelidir. PZEM karşılaştırma referansıdır; ground truth değildir.

## Mevcut kalibrasyon çalışmasına etkisi

- K=27.59 ve mevcut çalışan YAML korunur.
- Negatif eğimli K fonksiyonu, kullanıcı onayı ve ayrı kod sürümü olmadan uygulanmaz.
- PF için düzeltme katsayısı veya ilave matematiksel terim eklenmez.
- PF araştırması için alınacak veriler ayrı raporlanır; mevcut ampul kalibrasyon noktalarıyla aynı regresyona otomatik olarak dahil edilmez.

## Güvenlik ve doğrulama

Faz kaydırma devresinin şebeke ile ilişkisi, izolasyonu ve osiloskop ölçüm referansı anlaşılmadan bağlantı yapılmaz. Şebeke bağlantıları enerjisizken kurulur/değiştirilir. Osiloskop probu GND klipsi devrenin izolasyonu ve referans noktası doğrulanmadan bağlanmaz. Pil ile çalışan osiloskop kullanılması tek başına galvanik izolasyon kanıtı değildir.

## Sonraki aşama

Mevcut akım kalibrasyonunun ±%4 doğrulama çalışması sürdürülür. PF araştırması, trimpotlu düzeneğin şeması ve güvenli bağlantı yapısı incelendikten sonra ayrı deney olarak açılır.
