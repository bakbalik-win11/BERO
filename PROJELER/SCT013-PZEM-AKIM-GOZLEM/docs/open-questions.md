# Açık sorular

Aşağıdaki sorular yalnız bu projede hâlâ cevaplanmamış proje-özel konulardır. Genel donanım bilgileri [referans klasöründe](../hardware/references/README.md) ve ana BERO `DONANIM/` belgelerinde mevcuttur.

1. Bu projede hangi ESP32 modülü ve hangi geliştirme kartı/revizyonu kullanılacak? Bildirilen stok: 2×WROOM-32D, 1×WROOM-32E, 1×WROOM-32S.
2. Bu projede kullanılacak ADC hangisi ve VREF kaynağı/değeri nedir? BERO'da MCP3208 referansı var, ancak bu projedeki fiziksel düzeneğe seçildiği henüz doğrulanmadı.
3. SCT013-030 AC sinyali tamamlanmış yaklaşık 1,65 V bias orta noktasına hangi bağlantı/kuplaj elemanıyla eklenecek? Bias üretimi tamamlandı; bu, ayrı analog ön uç entegrasyon işidir.
4. Burden/analog filtre değerleri ile ADC girişinin güvenli maksimum aralığı nedir? Bu projedeki nihai bağlantı kanıtı kaydı eksik.
5. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
6. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
7. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
8. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?
9. True-RMS referans cihazı nedir ve en az üç kontrollü yük seviyesi hangi yüklerle sağlanacak?
10. BERO SSR bu projede kullanılacak mı? Kullanılacaksa kaynak kayıtta fiziksel model kesinleşmediğinden üzerindeki tam model, giriş sürme gereksinimi, AC/DC çıkışı, yük gerilimi ve akım kapasitesi doğrulanmalı.

**Karara bağlandı; yeniden sorulmayacak:**
- Öncelikli sensör: SCT013-030 (30 A / 1 V).
- PZEM kaydı: mevcut [DONANIM/PZEM-004T/README.md](../../../DONANIM/PZEM-004T/README.md) esas alınır.
- Bağlı CT: PZCT-02, 0–100 A; kullanıcı tarafından model olarak belirtildi ve PZEM'e bağlı olduğu fotoğrafta gösterildi. Bu, 100 A harici CT'li yapılandırmadır.
- Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin cihazla ölçüldüğü iddia edilmeyecek.
