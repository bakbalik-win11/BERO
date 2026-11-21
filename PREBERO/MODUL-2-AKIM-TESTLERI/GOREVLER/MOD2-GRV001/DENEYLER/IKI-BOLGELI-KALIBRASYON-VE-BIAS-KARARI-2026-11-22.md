# İki bölgeli akım kalibrasyonu ve bias kararı – 2026-11-22

## Durum
**Tasarım kararı alındı; katsayı deneyleri henüz yapılmadı.**

## Kullanıcı kararı
Akım ölçümü iki çalışma bölgesinde ayrı kalibre edilecek:
- **Düşük akım bölgesi:** 1,5 A altı için ayrı katsayı.
- **Yüksek akım bölgesi:** 1,5 A üstü için ayrı katsayı.

Bias devresinin sağladığı katkı, ilave devre ve bağlantı zahmetine değmediği için yeni tasarım yaklaşımında bias tercih edilmeyecek. Kullanıcının tasarım ilkesi: daha basit ölçüm yolu tercih edilecek.

## Teknik yaklaşım
Mevcut tek katsayılı dönüşümün yerine, testlerle belirlenecek iki bölgesel katsayı değerlendirilecek:

\[
I_{hesaplanan} =
\begin{cases}
RMS(ADC) \times K_{düşük}, & I_{ön/ham\ tahmin} < 1.5\ A \\
RMS(ADC) \times K_{yüksek}, & I_{ön/ham\ tahmin} > 1.5\ A
\end{cases}
\]

Bu ifade yöntem taslağıdır; henüz uygulanabilir bir algoritma olarak doğrulanmamıştır. Özellikle hangi ölçüm büyüklüğünün bölge seçimini yapacağı, katsayı seçiminin kararlı olması ve 1,5 A geçişindeki davranış deney ve yazılım tasarımında netleştirilmelidir. Tam 1,5 A sınırındaki seçim kuralı henüz kararlaştırılmamıştır.

## Deney planı
1. Bias kullanılmayan sade analog bağlantı düzeni güvenli biçimde kurulup her ADS1115 girişinin mutlak gerilim sınırları doğrulanacak.
2. 1,5 A'nın belirgin altında birden fazla akım noktası ölçülecek.
3. 1,5 A'nın belirgin üstünde birden fazla akım noktası ölçülecek.
4. 1,5 A çevresinde alt ve üst bölgeyi ayırmak için ek ölçüm noktaları alınacak.
5. Her noktada yeterli sayıda PZEM akım örneği ve SCT/ADS1115 örneği toplanacak; yük ve zaman koşulları kaydedilecek.
6. PZEM ile karşılaştırma referans olarak kullanılacak; ground truth kabul edilmeyecek.
7. Her bölge için katsayı ayrı hesaplanacak ve aynı bölgedeki farklı yük noktalarında doğrulanacak.
8. İki katsayılı modelin tek katsayılı modele göre hata davranışı ve 1,5 A civarında olası sıçrama ayrıca değerlendirilecek.

## Koruma ve mevcut durum
- Mevcut K=27.59 değeri şimdilik korunur; yeni bölgesel katsayılar ölçüm olmadan atanmaz.
- Çalışan YAML ve firmware bu karar kaydıyla değiştirilmez.
- Biaslı deneylerin eski sonuçları tarihsel veri olarak korunur; yeni tasarım tercihi bu sonuçları silmez veya geçmiş deneyleri geçersiz kılmaz.
- Biasın fiziksel olarak devreden çıkarılması ve yeni bağlantının uygulanması, bağlantı şeması ve giriş gerilimleri doğrulandıktan sonra ayrı uygulama adımıdır.
- Bu karar henüz iki bölgeli kalibrasyonun başarılı olduğunu göstermez.

## Açık teknik noktalar
- 1,5 A sınırında hangi katsayının seçileceği.
- Bölge seçiminin hangi ölçümden ve hangi sırada yapılacağı.
- Geçiş çevresinde katsayı değişiminin ani çıktı sıçraması üretip üretmediği.
- Her iki bölgedeki katsayıların birden fazla yük noktasında tekrarlanabilirliği.

## Kapanış / sonraki adım
Biasın yeni tasarımda tercih edilmemesi ve iki bölgeli katsayı yaklaşımı **tasarım kararı olarak kaydedildi**. Kalibrasyon deneyi açık iş olarak kalır. Sonraki adım, bias kullanılmayan güvenli bağlantıyı doğrulamak ve düşük akım bölgesinden başlayarak ölçüm serisini oluşturmaktır.
