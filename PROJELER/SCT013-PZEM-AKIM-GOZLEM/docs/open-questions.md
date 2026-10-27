# Açık sorular

Hiçbiri cevaplanmış sayılmaz. Deney sonrası sonuç ve kanıt bağlantısı ekleyin. Genel donanım özellikleri `hardware/references/` altında; aşağıdaki sorular bu projede henüz cevaplanmamış proje-özel bilgileri veya deneyle ölçülmesi gereken davranışları listeler.

1. PZEM'in iç ölçüm/ortalama penceresi nedir? Yaklaşık 2 s tahmini doğrulanmış üretici bilgisi değildir.
2. V, I, P ve PF aynı anda mı yenileniyor?
3. Sensör önceliği belirlenmiştir: SCT013-030 (30 A / 1 V) ilk tercih. Kullanılacak fiziksel ünitenin etiket fotoğrafı ve stok kaydının kanıt bağlantısı `hardware/photos/` içine alınacak mı? Bu oturumdaki görsel henüz depo dosyası değildir.
4. Bu projedeki fiziksel PZEM'in 10 A / 100 A varyantı ve varsa CT etiketi/sınıfı nedir? Genel PZEM-004T V3.0 kaydı bu fiziksel varyantı tek başına doğrulamaz.
5. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
6. 1 kS/s hedef yüklerde RMS ve olay algılaması için yeterli mi?
7. 2 ile 2,5 kS/s arasında anlamlı iyileşme var mı?
8. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?
9. Gerçek ADC ve analog ön uç nedir? Burden, bias, VREF ve maksimum güvenli aralık ölçüldü mü?
10. PZEM register'larının değişim / tekrar etme dinamikleri birbirine benziyor mu?
11. Yaklaşık 3 s geçiş etiketi bu modülde yeterli mi?
12. Stokta bulunduğu bildirilen 100 nF / 50 V seramik kondansatörlerin gerçek şemada kullanılacağı nokta ve görevi nedir? Bu, analog ön uç tasarımı sırasında kararlaştırılmalıdır.
13. “Bias trafosu”nda RN130421 6 V AC sekonderinden sonra KBU6M (6 A / 1000 V) köprü doğrultucu, L78L33 TO-92 regülatör ve korunaklı kutu olduğu kullanıcı tarafından bildirildi. Köprü sonrası filtre kondansatörünün değeri/konumu ve regülatör bypass kondansatörleri nelerdir?
14. Bias trafosu kutusu ve ayrı breadboardda hangi kondansatörlerin tam değeri, adedi ve konumu nedir? 100 nF seramik stokunun kaç tanesi bu devrede kullanılıyor?
15. İki 10 kΩ direncin ayrı breadboarddaki besleme/GND bağlantıları nedir? 1,65 V orta nokta değeri nominal hesap mı, fiziksel ölçüm mü?
16. SCT sinyalinin 1,65 V bias noktasına nasıl kuplaj yapıldığı ve “şebeke dalgalanmasını aynı motifle yansıtma” hedefinin devrede hangi sinyal yolu ile sağlandığı nedir? L78L33 düzenleme yaptığı için, normal regülasyon koşulunda çıkışın şebeke dalgalanmasını takip ettiği varsayılmamalıdır.
