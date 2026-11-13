# E21 — Çamaşır makinesi program davranışı analizi

- **Durum:** PLANLANDI
- **Açılış tarihi:** 2026-11-13
- **Hedef:** Çamaşır makinesinin seçilen bir yıkama programını baştan sona SCT-013 + ADS1115 akım zaman serisi üzerinden gözlemlemek; programın elektriksel davranış evrelerini, sürelerini, geçişlerini ve tekrar eden örüntülerini çıkarmak.
- **Önceki hedef:** PZEM kararlı-alan eşleştirmesiyle eğitim/kalibrasyon verisi üretme iş akışı ADR-026 ile kapatıldı. Bu işin eski kayıtları silinmez.

## 1. Araştırma sorusu

Bir çamaşır makinesi programı boyunca akım davranışından hangi çalışma evreleri birbirinden ayırt edilebilir? Aynı program tekrarlandığında evre sırası, süreleri ve akım örüntüleri ne kadar benzer?

Bu çalışma enerji tüketimi veya güç kalitesi analizi değildir. SCT zincirinin ürettiği akım gözlemi, cihazın çalışma karakterini incelemek için kullanılacaktır.

## 2. İlk kayıt kapsamı

İlk oturumda yalnızca **bir tam program** kaydedilir. Program adı ve makine panelindeki seçenekler kullanıcı tarafından bildirilecektir; makine modeli, program, sıcaklık, sıkma devri, ek seçenekler veya çamaşır yükü varsayılmaz.

Kayıt öncesi not edilecekler:
- Makine marka/modeli (biliniyorsa).
- Seçilen programın paneldeki tam adı.
- Sıcaklık, sıkma devri ve ek seçenekler.
- Yaklaşık çamaşır yükü ve yükün niteliği (kullanıcı bildirimi).
- Programın başlatıldığı saat ve programın bittiği saat.
- Kullanıcının gözlemlediği olaylar (su alma, tambur hareketi, bekleme, boşaltma, sıkma vb.); yalnız gerçekten gözlenenler.

## 3. Ölçüm ve veri ilkeleri

- Aynı SCT-013 + ADS1115 + ESP32D2 ölçüm zinciri kullanılacak; gerçek firmware/YAML sürümü ve çalışan ayarlar kayıt altına alınacak.
- Kullanıcı ayrıca onaylamadıkça mevcut gain, SPS, ct_clamp sample_duration, update_interval, filtre ve katsayı değiştirilmeyecek.
- Ham Home Assistant History CSV değişmeden korunacak; analiz çıktıları ayrı dosyalardır.
- Kaynak timestamp, timezone, entity_id, birim ve ham state korunur.
- PZEM verisi mevcutsa yardımcı karşılaştırma/bağlam olarak saklanabilir. Yeni hedefte PZEM kararlı alan eşleştirmesi veya PZEM etiketli eğitim verisi zorunlu değildir.
- 2 saniyelik yayın aralığı kullanılıyorsa rapor evre geçişlerinin bu zaman çözünürlüğüyle gözlendiğini açıkça belirtir; alt-saniye olay süresi iddia edilmez.
- Makinenin program evreleri yalnız akım değerinden kesin adlandırılmaz. Akım örüntüsü önce tarafsız biçimde bölümlenir; isimler panel bilgisi ve kullanıcı gözlemiyle ilişkilendirilir.
- OFF/yüksüz alanlar eğitim etiketi değildir; ancak tam program davranışını anlamak için ham zaman serisinde korunur.

## 4. İlk analiz çıktıları

İlk tam kayıt geldikten sonra:
1. CSV bütünlüğü, kolonlar, entity'ler, zaman aralığı ve örnek sayıları doğrulanır.
2. Akım zaman serisi çizilir; boşluklar, sıfıra inişler, darbeler ve kararlı seviyeler belirlenir.
3. Gözlenen evre adayları sıralanır; her biri için başlangıç/bitiş, süre, medyan/ortalama, dağılım ve tepe değerler raporlanır.
4. Tekrarlayan motor/rezistans/pompa benzeri örüntüler yalnız kanıt düzeyine uygun ifadelerle adlandırılır.
5. Kullanıcı gözlemleriyle eşleştirme yapılır; doğrulanmayan evre isimleri “aday/hipotez” olarak kalır.

## 5. Tekrar ve karşılaştırma

İlk program kaydı bir keşif/baseline oturumudur. Aynı programın sonraki tekrarları, mümkünse benzer sıcaklık, sıkma devri, seçenek ve yük koşuluyla karşılaştırılır. Farklı programlar daha sonra ayrı oturumlar olarak eklenir. Tek programdan bütün makine davranışı hakkında genelleme yapılmaz.

## 6. Güvenlik ve sınırlar

- ADS1115 A0/A1 ortak-mod ve GND–VDD giriş sınırlarının fiziksel doğrulaması açık ön koşuldur; iyi görünen ölçüm grafiği giriş güvenliğini kanıtlamaz.
- Şebeke ve CT kurulumu uygun muhafaza/koruma ve yetkin uygulamayla yapılmalıdır.
- Bu çalışma enerji tüketimi, gerçek güç, PF, harmonik veya arıza teşhisi iddiası taşımaz.
- Makine kapağı/interlock veya güvenlik mekanizmalarına müdahale edilmez.

## 7. Kabul ölçütü

E21 ilk oturumu ancak aşağıdakiler tamamlandığında “ilk kayıt analiz edildi” sayılır:
- Tam program CSV'si mevcut ve kaynak bütünlüğü kontrol edilmiş.
- Program/ayar/yük bilgileri kullanıcıdan kaydedilmiş.
- Akım zaman serisi ve gözlenen evre tablosu üretilmiş.
- Gözlem, kullanıcı bildirimi ve hipotezler birbirinden ayrılmış.
- Ham veri ve analiz özeti depoda birbirine bağlanmış.

**Mevcut durum:** Program kaydı ve analiz henüz yok; bu belge yalnızca yeni hedefin protokolüdür.
