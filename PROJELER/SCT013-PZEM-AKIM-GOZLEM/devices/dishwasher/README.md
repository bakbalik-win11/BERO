# MODUL-05 — Bulaşık Makinesi İzleme Modülü

## Amaç
Bu klasör, bulaşık makinesi için üretilecek taşınabilir gözlem modülünün donanım, firmware, ham kayıt, Python analiz ve rapor dosyalarını bir arada tutar.

## Modül kimliği
- **Modül numarası:** ONAY BEKLİYOR. Proje geçmişindeki modül kimlikleriyle tutarlılık sağlandıktan sonra atanacak.
- **Aşama:** PLANLANDI / fiziksel imalat ve doğrulama bekliyor
- **Planlanan gözlem kanalları:** akım, ses ve titreşim
- **Kesinleşmeyenler:** ESP32 kart varyantı, ses/titreşim sensörlerinin kesin modelleri, analog ön uç, I²C çoklayıcı bağlantısı, pin eşlemesi, örnekleme ve kayıt parametreleri.
- Donanım ve bağlantı bilgileri fiziksel montaj ve test sonrasında doğrulanacaktır. Varsayılan pin, sensör veya çalışma değeri kullanılmayacaktır.

## Klasör yapısı
- `hardware/`: gerçek parça listesi, bağlantılar, şemalar ve güvenlik notları.
- `firmware/`: kullanılan ESPHome YAML/kod, sürüm ve derleme/çalışma logları.
- `data/raw/`: kaynaktan alınan değiştirilmemiş ham kayıtlar.
- `data/processed/`: doğrulanmış ve analize hazırlanmış türetilmiş veriler.
- `analysis/python/`: bu modüle ait analiz betikleri ve parametreler.
- `analysis/results/`: CSV/JSON/istatistik ve grafik kaynak çıktıları.
- `analysis/reports/`: yorumlanmış analiz raporları.
- `experiments/`: deney protokolleri, koşullar ve sonuç kayıtları.

## Veri koruma ilkeleri
1. RAW dosyaları değiştirilmez; temizlik ve filtreleme ayrı çıktı üretir.
2. Her kayıt için RECORD_ID, tarih-saat, saat dilimi, kaynak ve modül kimliği metadata'da tutulur.
3. Her analiz, kullandığı RAW dosyasını ve mümkünse SHA-256 özetini belirtir.
4. Python sürümü, bağımlılıklar, analiz betiği sürümü ve parametreler rapora yazılır.
5. Ham kayıt, işlenmiş veri, analiz sonucu ve yorum birbirinden ayrılır.
6. Gerçek donanım testi yapılmadan modül çalışır veya tamamlandı olarak işaretlenmez.

## Kayıt kimliği
- Çamaşır makinesi: `WM-YYYYMMDD-NN`
- Bulaşık makinesi: `DW-YYYYMMDD-NN`
- Her fiziksel kayıt ayrı RECORD_ID alır. Program sınıfı/ayar gruplaması metadata ile ayrıca yapılır.

## İlgili tarihsel kayıtlar

**Not:** Bu klasör yapısının oluşturulması donanımın imal edildiği, bağlandığı veya ölçüm yaptığı anlamına gelmez.
