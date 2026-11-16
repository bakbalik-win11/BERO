# 2026-11-16 — Oturum kaydı: osiloskop güvenliği ve Surface Python planı

## HEDEF
Oturumda konuşulan osiloskop eğitim yaklaşımını ve Surface 11 Snapdragon X Elite cihazının BERO Python analizlerinde olası ikinci çalışma bilgisayarı olarak kullanım planını kalıcılaştırmak.

## DEPO OKUMASI
- Proje `AGENTS.md`, `STATUS.md`, `ROADMAP.md`, `MEMORY.md`, `HISTORY/` dizini ve osiloskop öğrenme günlüğü incelendi.
- Güncel depo yapısında proje dosyaları `PROJELER/SCT013-PZEM-AKIM-GOZLEM/` altındadır; kök dizinde eski varsayılan konumdaki `STATUS.md` veya `ROADMAP.md` bulunmamaktadır.
- Osiloskop öğrenme günlüğü: `../../GUNLUK/2026-11-13-FNIRSI-2D15P-OSILOSKOP-OGRENME.md`.

## YAPILAN / KULLANICI KARARLARI
- Kullanıcı osiloskop konusunda çok sayıda video izlediğini, ancak probun toprak klipsi ve 220–240 V bağlantı güvenliğini netleştirmek istediğini belirtti.
- Standart osiloskop probunun toprak klipsinin koruyucu toprakla ilişkili olabileceği; multimetrenin bağımsız iki ucu gibi davranmadığı açıklandı.
- İlk eğitim düşük gerilimli deneylerle sınırlı tutulacak. Şebeke fazı/nötrüne standart prob toprak klipsi bağlanmayacak; doğrudan şebeke ölçümü yapılmayacak.
- Kullanıcı, mevcut BERO işleri için multimetrenin yeterli olduğunu belirtti. Osiloskop yalnız gerektiğinde analog sinyal şekli/sıçrama teşhisi için yardımcı araçtır.
- Kullanıcı Surface 11 Snapdragon X Elite'i toplantı notu, Excel ve taşınabilir çalışma için kullandığını; ek olarak Python veri işleme işlerinde denemek istediğini belirtti.
- Surface için olası görevler: E21 CSV analizi, veri temizleme/birleştirme, istatistik, korelasyon ve grafik üretimi. İş yerinde küçük Python/CSV/Excel göreviyle deneme yapılabilir.
- İleride Mac mini ve Surface'te aynı dosya/kod çalıştırılarak süre ve bellek karşılaştırması yapılması kararlaştırıldı.
- Gemini uygulaması yalnızca deneme amaçlı; satın alma/abonelik niyeti yok. Gerektiğinde ekran/arayüz veya ek teknik görüş için kullanılabilir; AI çıktısı doğrulama kabul edilmeyecek.

## DOĞRULAMA SINIRI
- Surface'te Python ortamı kurulmadı; kod, CSV analizi veya benchmark çalıştırılmadı.
- Osiloskopla ölçüm yapılmadı; cihaz teslimi ve fiziksel uygulama bekleniyor.
- ADS1115 kargosu henüz teslim edilmedi; yeni modül kurulmadı, derlenmedi ve test edilmedi.
- Bu oturumda yeni çamaşır makinesi CSV'si veya ölçüm sonucu paylaşılmadı; yeni tam program kaydı varmış gibi kaydedilmedi.

## SONRAKİ TEK ADIM
ADS1115 kargosu teslim edildiğinde mevcut çalışan ölçüm zincirinin ayarlarını/sonuçlarını koruyarak yeni modülün kurulumuna başlamak.
