# E21 — Çamaşır makinesi program davranışı analizi

- **Durum:** PLANLANDI
- **Açılış tarihi:** 2026-11-13
- **Hedef:** İlk etapta çamaşır makinesinin yalnızca bir programını kaba/keşif amaçlı olarak baştan sona kaydetmek. İlk kayıt ayrıntılı program çözümlemesi veya sınıflandırma projesi değildir.
- **İlerideki yön:** İlk akım kaydından sonra farklı sensörler sisteme aşamalı olarak eklenip birlikte değerlendirilebilir. Sensör türleri ve bağlantıları henüz belirlenmedi; bu aşamada varsayılmayacak.
- **Önceki hedef:** PZEM kararlı-alan eşleştirmesiyle eğitim/kalibrasyon verisi üretme iş akışı ADR-026 ile kapatıldı. Bu işin eski kayıtları silinmez.

## 1. İlk testin amacı ve sınırı

İlk test yalnızca **bir programın kaba kaydıdır**. Amaç, programın başından sonuna kadar akımın genel davranışını görmek ve ilerideki sensör entegrasyonu için başlangıç verisi oluşturmaktır. Bu ilk oturumda tüm evreleri kesin tanımlamak, makine durumlarını sınıflandırmak, aynı programı tekrarlamak veya eğitim modeli oluşturmak zorunlu değildir.

İlk kayıt sonrasında hangi ek sensörlerin anlamlı olacağı değerlendirilecektir. Farklı sensörlerle kombinasyon, ayrı bir sonraki aşamadır; ilk testin ön koşulu değildir.

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

## 4. İlk kaba kayıttan beklenen çıktı

İlk tek program kaydından sonra:
1. CSV bütünlüğü, zaman aralığı ve akım entity'si doğrulanır.
2. Program boyunca akımın genel grafiği çıkarılır.
3. Belirgin yükselme, düşme, bekleme ve tekrar eden hareketler kabaca işaretlenir.
4. Programın toplam kayıt süresi ve dikkat çeken zaman aralıkları not edilir.
5. Makinenin iç işlemleri hakkında kesin olmayan yorumlar hipotez olarak bırakılır.

Bu aşamada ayrıntılı evre sınıflandırması, tekrar testi veya ek sensör entegrasyonu yapılması beklenmez.

## 5. Sonraki aşamalar

İlk kayıt değerlendirildikten sonra kullanıcıyla birlikte uygun farklı sensörler seçilecek ve aşamalı biçimde sisteme eklenerek kombinasyonları incelenecektir. Sensör seçimi, bağlantı ve kayıt yöntemi ayrı karar/protokolle belirlenecektir. Aynı programı tekrar etme veya başka programları kaydetme ihtiyacı ilk kaba testin sonucuna göre kararlaştırılır. Tek programdan bütün makine davranışı hakkında genelleme yapılmaz.

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

**Mevcut durum:** İlk kaba tek-program kaydı bekleniyor. Ek sensörler ve çoklu sensör analizi sonraki aşamadır.
