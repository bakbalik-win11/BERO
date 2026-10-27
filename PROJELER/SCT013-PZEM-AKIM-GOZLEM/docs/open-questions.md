# Açık sorular

Aşağıdaki sorular yalnız bu projede henüz cevaplanmamış proje-özel konulardır. Genel SCT/PZEM/SSR bilgileri [referans klasöründe](../hardware/references/README.md) mevcuttur.

1. PZEM-004T V3.0 modülü 10 A dahili şöntlü varyant mı, yoksa 100 A harici CT'li varyant mı? Harici CT varsa modeli nedir? Fotoğraf modül kimliğini PZEM-004T V3.0 olarak kaydetmeye yeterli; varyantı tek başına netleştirmiyor.
2. Bu projede hangi ESP32 modülü ve hangi geliştirme kartı/revizyonu kullanılacak? Bildirilen stok: 2×WROOM-32D, 1×WROOM-32E, 1×WROOM-32S.
3. Bu projede kullanılacak ADC hangisi ve VREF kaynağı/değeri nedir? BERO'da MCP3208 referansı var, ancak bu proje düzeneğine seçildiği henüz doğrulanmadı.
4. SCT'nin AC sinyali, tamamlanmış yaklaşık 1,65 V bias orta noktasına hangi bağlantı/kuplaj elemanıyla ekleniyor? Bu, bias üretiminin tamamlanmasından ayrı analog ön uç bağlantısıdır.
5. Burden/analog filtre değerleri ile ADC girişinin güvenli maksimum aralığı nedir? Bu projedeki fiziksel devreye ait kanıt kaydı eksik.
6. PZEM'in iç ölçüm/ortalama penceresi nedir; V, I, P ve PF aynı anda mı yenileniyor? Bunlar deneyle ölçülecek.
7. Hangi akımın altında PZEM, bağımsız referansa göre kabul edilemez sapma/kararsızlık gösteriyor?
8. 1 kS/s, 2 kS/s ve 2,5 kS/s seçenekleri arasında hedef yüklerde anlamlı performans farkı var mı?
9. 200 ms pencere kararlı yükte tekrarlanabilir mi; çevrime senkron pencere gerekli mi?
10. True-RMS referans cihazı nedir ve en az üç kontrollü yük seviyesi hangi yüklerle sağlanacak?
11. BERO SSR bu projede kullanılacak mı? Kullanılacaksa üzerindeki tam model, giriş sürme gereksinimi, AC/DC çıkışı, yük gerilimi ve akım kapasitesi ne? Kaynak kayıtta model kesinleşmediği için Omron G3MB yalnız aday referanstır.

**Tamamlandı ve yeniden sorulmayacak:** Temiz yaklaşık 1,65 V bias üretim alt devresi kullanıcı onayıyla tamamlandı. Kayıtlı zincir: RN130421 6 V / 2 VA → KBU6M köprü → 2200 µF / 35 V → L78L33; ayrı breadboardda 2×10 kΩ ve orta noktadan GND'ye 104 kodlu 100 nF seramik. Bağımsız ölçüm raporu yoksa 1,650 V'nin ölçülmüş sonucu olduğu iddia edilmeyecek.
