# Modül 4 — Çamaşır Makinesi İzleme Modülü

## Amaç
Bu klasör, çamaşır makinesi için üretilecek taşınabilir gözlem modülünün donanım, firmware, ham kayıt, Python analiz ve rapor dosyalarını bir arada tutar.

## Modül kimliği
- **Modül numarası:** MODÜL 4 — kullanıcı tarafından 2026-11-20 tarihinde onaylandı.
- **Aşama:** PLANLANDI / fiziksel imalat ve doğrulama bekliyor
- **Birincil gözlem kanalları:** ses ve titreşim. **Akım kanalı:** yardımcı/ikincil gözlem olarak değerlendirilecek; donanım bağlantısı ve kapsamı montaj öncesi kesinleştirilecek.
- **Kesinleşmeyenler:** ESP32 kart varyantı, ses/titreşim sensörlerinin kesin modelleri, analog ön uç, I²C çoklayıcı bağlantısı, pin eşlemesi, örnekleme ve kayıt parametreleri.
- Donanım ve bağlantı bilgileri fiziksel montaj ve test sonrasında doğrulanacaktır. Varsayılan pin, sensör veya çalışma değeri kullanılmayacaktır.

## Gözlem ve analiz yaklaşımı

Bu modülün ana veri kaynağı ses ve titreşim kayıtları olacaktır. Akım verisi, makine davranışını yorumlamaya yardımcı olabilecek ikincil bir kanal olarak ele alınır; kesin sensör, bağlantı ve örnekleme kararı henüz verilmemiştir.

Veri akışı aşamalıdır: sensörlerden ham kayıt → Python ile zaman serisi/özellik çıkarımı ve karşılaştırma → yeterli tekrar ve doğrulama sonrasında davranış sınıfları/karar ağacı → daha ileri aşamada bildirim üretimi. Karar ağacı ve bildirim sistemi şu anki imalat kapsamı değildir; eşikler ve sınıflar veriyle doğrulanmadan otomatik karar verilmeyecektir.

14 Kasım 2026 tarihli çamaşır makinesi akım kayıtları ilk keşif/deneme kayıtlarıdır. Bunlar yeni ses-titreşim modülünün ana veri seti veya multimodal doğrulaması sayılmaz.

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
- Çamaşır makinesi E21 ilk program kayıtları: [E21](../../experiments/E21-washing-machine-program-analysis/README.md)
- Eski çamaşır makinesi kayıt şablonları: [washing-machine logs](../../logs/washing-machine/)

**Not:** Bu klasör yapısının oluşturulması donanımın imal edildiği, bağlandığı veya ölçüm yaptığı anlamına gelmez.
