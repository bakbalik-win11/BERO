# 0,30 A Altı Düşük Akım Deney Planı

**Durum:** PLANLANDI — fiziksel deney henüz yapılmadı.

## 1. Amaç ve kapsam

30 A/1 V sınıfı SCT sensörün BERO'da 0,30 A altındaki yüklerdeki davranışını ayrı bir deney alanında incelemek. Bu bölge için ±%4 kabul/ret kriteri uygulanmayacaktır. 0,30 A sınırı BERO test sınıflandırmasıdır; üretici doğruluk garantisi veya sensörün mutlak alt ölçüm sınırı değildir.

Bu deney enerji analizi, PF hesaplama, harmonik/FFT veya güç kalitesi çalışması değildir. PZEM akım ve PF alanları yalnız aynı yük penceresini tanımlamak ve karşılaştırmayı bağlama oturtmak için kaydedilir.

## 2. Başlangıçta korunacaklar

- Mevcut SCT-1 bağlantısı: sarı kablo GPIO32 / ADC1_CH4.
- Ortak bias: turuncu kablo GPIO35 / ADC1_CH7.
- ESP32D1 Modül 2, tek aktif SCT kanalı.
- ESPHome/firmware sürümü, ct_clamp 200 ms penceresi ve 2 s yayın aralığı test kaydında açıkça belirtilir.
- K=24.22 korunur; deney sırasında firmware katsayısı değiştirilmez.
- Yazılımsal sıfır eşiği eklenmez.

## 3. Deney matrisi — önerilen sıra

| Koşul | İletkenin CT çekirdeğinden geçişi | Amaç |
|---|---:|---|
| A | 1 tur | Mevcut tek tur temel koşulu |
| B | 2 tur | Sinyal büyümesinin gözlenmesi |
| C | 4 tur | Daha yüksek amper-sarım ile düşük akım gözlemi |

Her koşul ayrı oturum ve ayrı log olarak kaydedilir. Aynı yük, aynı besleme ve mümkün olduğunca aynı çalışma noktası korunur. Önce A koşulu kaydedilir; B ve C yalnız güvenli fiziksel düzenek hazırlandıktan sonra uygulanır.

## 4. Çok turlu ölçümün yorumlanması

Aynı tek yalıtılmış iletken CT çekirdeğinden N kez geçirilirse CT, yaklaşık N kat amper-sarım görür. Mevcut tek tur ölçeğiyle gösterilen akım bu nedenle gerçek hat akımının yaklaşık N katı olabilir. Bu, sensör sinyalini büyütme deneyidir; doğrudan gerçek akım değeri diye raporlanmaz.

Analiz dosyasında iki değer ayrı tutulur:

1. Firmware'in gösterdiği ham/ct_clamp akım göstergesi.
2. Yalnız deneysel normalizasyon olarak gösterge / tur sayısı hesabı.

Bu normalizasyon firmware K katsayısını değiştirmez ve kalibrasyon sonucu sayılmaz. Tur sayısı ve iletken yönü fotoğraf/not ile kayıt altına alınır.

## 5. Her kararlı pencerede kaydedilecekler

- Deney ID, koşul (1T/2T/4T), yük ve fiziksel düzenek.
- UNIT bildirimi varsa tam değer ve kaynak türü.
- PZEM akım ve PF; mümkünse aynı kararlı çalışma penceresinden.
- SCT ct_clamp akım yayını, Raw AC (V), bias ADC (V), SCT ADC (V).
- ESPHome sürümü, YAML snapshot/commit, besleme türü, GPIO ve SCT modeli.
- İlk geçiş pencereleri ile kararlı pencere ayrımı; olay zamanı yoksa sınır belirsizliği.
- Ortalama, medyan, min/maks, standart sapma ve yayın sayısı.

## 6. Değerlendirme

- 0,30 A altında ±%4 başarı/başarısızlık kararı verilmez.
- Öncelik, 1T/2T/4T koşullarında Raw AC ve ct_clamp çıktısının tekrarlanabilir biçimde değişip değişmediğini gözlemlemektir.
- PF olası açıklama değişkenidir; yalnız PZEM'in aynı pencereye ait PF verisiyle incelenebilir. PF etkisi veri olmadan varsayılmaz.
- Düşük akım bölgesinde daha uygun CT, ayrı sensör aralığı veya yük tipine özel eğitim/model seçenekleri ileride karşılaştırılabilir. Bu dosya bunlardan herhangi birini seçmiş değildir.
- Sonuçlar yetersizse 0,30 A altı çalışma kapsam dışında bırakılabilir. Bu da geçerli bir proje kararıdır.

## 7. Güvenlik

- Sarım düzeni değiştirilmeden önce devre enerjisiz bırakılır.
- CT çekirdeğinden yalnız aynı tek yalıtılmış iletken geçirilir; faz ve nötr birlikte geçirilmez.
- İletkenin yalıtımı zarar görmez; çekirdek/klips mekanik olarak zorlanmaz.
- Şebeke tarafında açıkta iletken veya enerjili düzenek üzerinde sarım değişikliği yapılmaz.

## 8. İlgili fan gözlemleri

- FAN-1 UNIT: 0,093 A. Mevcut uzun SCT logu yalnız ısınma/deneme gözlemidir; ±%4 değerlendirmesi değildir. [FAN kayıtları](../fan/README.md).
- FAN-2 UNIT: 0,106 A. Mevcut 54 yayınlık log yalnız gözlem istatistiğidir; PZEM akım + PF beklenmektedir.

**Açık durum:** Plan yazıldı; test matrisi henüz fiziksel olarak uygulanmadı. Her test kapanışında kullanılan son YAML snapshot'ı ve ham log/analiz ilişkisi ayrıca kaydedilecektir.
