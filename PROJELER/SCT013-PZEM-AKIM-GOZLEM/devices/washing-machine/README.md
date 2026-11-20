# MODÜL 5 — Çamaşır Makinesi İzleme Modülü

## Amaç
Bu klasör, çamaşır makinesi için üretilecek taşınabilir gözlem modülünün donanım, firmware, ham kayıt, Python analiz ve rapor dosyalarını bir arada tutar.

## Modül kimliği ve aşama
- **Modül numarası:** MODÜL 5 — kullanıcı tarafından 2026-11-20 tarihinde onaylandı.
- **Aşama:** PLANLANDI / fiziksel imalat ve doğrulama bekliyor.
- **Mimari:** Modül 6 ve Modül 6 aynı elektronik tasarımın ikiz kopyalarıdır. Donanım ve firmware temeli ortak; cihaz adı, modül kimliği ve kayıt etiketleri farklıdır.
- **Güç durumu:** Kullanıcı bildirimi: kurulum noktasındaki prizde 5 V besleme mevcut. Beslemenin kaynağı/akım kapasitesi ve bağlantı güvenliği montaj öncesinde kontrol edilecek.
- **İmalat sırası:** İlk yapılacak modül.
- **Birincil gözlem kanalları:** ses ve titreşim.
- **Yardımcı kanal:** akım; makine çalışma evrelerini yorumlamak için bağlamsal veri olarak kullanılacak.
- Ayrıntılı ortak karar: [ADR-032 — İkiz sensör modülleri](../../docs/decisions/ADR-032-washing-dishwasher-twin-sensor-modules.md).

## Ortak donanım listesi — bu modülden birer adet
| Bileşen | Adet | Görev / bağlantı yaklaşımı |
|---|---:|---|
| ESP32-D | 1 | Ana kontrolcü; tam kart/revizyon teyidi bekliyor |
| Vidalı terminal shield | 1 | ESP32-D için fiziksel bağlantı/dağıtım |
| MAX4466 | 1 | Ses; analog çıkış ESP32 ADC girişine |
| MPU6050 | 1 | İvme/titreşim; birinci ve ayrı I²C hattına |
| SCT013 30 A / 1 V | 1 | Yardımcı akım algılayıcısı |
| ADS1115 | 1 | SCT013 analog sinyalini okuyan harici ADC; ikinci ve ayrı I²C hattına |

İki modülün toplam planlanan miktarı her bileşenden ikişer adettir.

## Bağlantı mimarisi — karar verilen / bekleyen

- MAX4466 OUT → ESP32 ADC: doğrudan analog okuma hedefleniyor. ADC pini, ses örnekleme hızı, çözünürlük ve kayıt biçimi belirlenmedi.
- MPU6050 → I²C-1: SDA/SCL pinleri fiziksel kart ve shield üzerinden teyit edilecek.
- ADS1115 → I²C-2: MPU6050 hattından ayrı SDA/SCL çifti kullanılacak. Bu ayrım kullanıcı tarafından kesinleştirilmiştir; fiziksel bağlantı kolaylığı nedeniyle iki ayrı bus kullanılacaktır. Kart/framework üzerinde gerçek bağlantı ve firmware ile doğrulanması yine gereklidir.
- SCT013 → ADS1115 analog giriş: giriş bias/ölçekleme/koruma, ADS1115 gain ve data rate, CT sekonder koşulları ve kalibrasyon henüz belirlenmedi.
- Besleme gerilimi, toprak referansı, kablo düzeni ve muhafaza fiziksel montaj öncesi kontrol edilecek.
- Bu doküman pin şeması veya enerjili şebeke bağlantısı talimatı değildir. Şebeke tarafı bağlantılar uygun koruma ve muhafaza ile yetkin kişi tarafından yapılmalıdır.

## Gözlem ve analiz yaklaşımı

Ses ve titreşim ana veri kanallarıdır. Akım, ses/titreşim olaylarının yorumlanmasına yardımcı olacak ikincil kanaldır. Bulaşık makinesi için su alma ve boşaltma evrelerinin ses/titreşim izlerinde görünmesi araştırılacak; evre imzaları ölçüm ve tekrarlarla doğrulanmadan sabit kabul edilmeyecektir.

Veri akışı: sensörlerden ham kayıt → Python ile zaman serisi/özellik çıkarımı ve karşılaştırma → yeterli tekrar ve doğrulama sonrasında davranış örüntüleri/sınıfları → daha ileri aşamada karar mantığı ve bildirim. Karar ağacı ve bildirim şu anki imalat kapsamı değildir.

14 Kasım 2026 tarihli eski çamaşır makinesi akım kayıtları keşif/ön kayıt niteliğindedir; yeni ses-titreşim modülünün ana veri seti veya multimodal doğrulaması değildir.

## Klasör yapısı
- `hardware/`: gerçek parça listesi, bağlantılar, şemalar ve güvenlik notları.
- `firmware/`: kullanılan kod/YAML, sürüm ve derleme/çalışma logları.
- `data/raw/`: kaynaktan alınan değiştirilmemiş ham kayıtlar.
- `data/processed/`: doğrulanmış ve analize hazırlanmış türetilmiş veriler.
- `analysis/python/`: analiz betikleri ve parametreler.
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

**Durum notu:** Bu README, kullanıcı kararlarını ve planlanan bağlantı mimarisini kaydeder. Donanımın imal edildiği, bağlandığı, firmware'in derlendiği veya ölçüm yaptığı anlamına gelmez.
