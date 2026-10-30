# Aşama 3 — 150 W akkor ve 8,5 W LED

Neden: 100 W koşulundaki bulguların yalnızca o yüke özgü olup olmadığını görmek. 150 W akkor farklı akım seviyesini, 8,5 W LED farklı yük tipini temsil eder.

Uygulama: Her iki yükte de aynı 3 × 3 matrisi uygula: 1/2/4 kablo turu ve 1/2/2,5 kS/s hedefleri. RMS, mutlak Peak ve Peak-to-Peak aynı örnek penceresinden çıkarılır.

PZEM veya başka ESP'nin ortalama akımı varsa genel koşul notu olarak yazılabilir; SCT pencereleriyle zaman eşleştirilmez. Nominal watt değerinden gerçek akım varsayılmaz.

Sorular: Yöntemlerin değişkenliği yükle değişiyor mu? Tur sayısının etkisi iki yükte benzer mi? LED ve akkor yükte yöntemler farklı davranıyor mu? Bu aşama laboratuvar doğruluğu sıralaması değildir.

## PF ve fiziksel akım yorumu

Bu aşamadaki yük karşılaştırmalarında düşük PF'nin, aynı gerilim ve aktif güç koşulunda RMS akımı artırabileceği akılda tutulur. Dolayısıyla LED gibi farklı elektriksel karakteristiğe sahip bir yükte daha yüksek SCT RMS/Peak görülmesi otomatik olarak sensör hatası değildir. Her koşulun gerçek PZEM gerilim, aktif güç, akım ve PF değerleri ayrı kaydedilir; nominal watt değerleri ölçüm yerine geçmez.

E08 yalnızca SCT sinyal karakterizasyonudur; PZEM ile zaman eşleştirmesi veya kalibrasyon sonucu çıkarılmaz. PZEM alanları genel koşul notu olarak kaydedilirse PF ve akım birlikte tutulur. Bu gözlemler daha sonraki E09 yorumuna bağlanır.
