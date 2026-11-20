# PREBERO çalışma kuralları

## Oturum başlangıcı
1. AGENTS.md, STATUS.md ve ROADMAP.md dosyalarını oku.
2. Aktif görev kartını ve ilgili deney/protokol kayıtlarını oku.
3. Eski SCT/PZEM arşivini yalnızca tarihsel kanıt olarak kullan; eski hedefleri aktif sayma.

## Kapsam
- Bu klasör PREBERO'nun yeni çalışma alanıdır.
- Eski SCT + ADS1115 akım okuma hedefi başarıldığı kabul edilerek kapatılmıştır.
- Yeni aşama baştan ele alınır. Eski PZEM eğitim/kararlı pencere akışı, eski çok kanallı modül planları, eski ses/titreşim donanım listeleri ve eski görevler otomatik devralınmaz.
- Modül 4 masaüstü prototiptir; imal edilmiş nihai donanım değildir.
- Modül 5/6/7 çalışma başlıklarıdır; eski tasarımlar yeni karar alınmadan kullanılmaz.
- Bias gerekliliği deney öncesinde varsayılmaz.

## Kanıt disiplini
- Ölçüm, kullanıcı bildirimi, üretici belgesi, hesap ve hipotezi ayır.
- Bilinmeyen pin/bağlantı/gerilim değerlerini tahmin ederek kesinleştirme.
- Test yapılmadan kodu veya modülü çalışır olarak işaretleme.
- Ham log ve veriyi değiştirme; yorum ve türetilmiş çıktıyı ayrı sakla.
- Başarılı kodla birlikte gerçek cihaz logunu ve log yorumunu sakla.
- Kabul ölçütleri karşılanmadan sonraki aşamaya geçme.

## Depo düzeni
- Yeni kararları ADR olarak kaydet; geçmiş kararları silme.
- Görevlerde amaç, bağlantı/koşul, beklenen çıktı ve kabul ölçütü bulunsun.
- Oturum sonunda STATUS.md, HISTORY/SESSION_LOG.md ve gerekiyorsa PROGRESS_TREE.md güncellensin.
- Yazılan dosyaları yeniden oku ve yerel bağlantıları kontrol et.
- Yapılmamış işi tamamlandı diye raporlama.

## Güvenlik
- Şebeke bağlantıları uygun koruma, muhafaza ve yetkinlik gerektirir.
- Osiloskop yalnız uygun şekilde izole edilmiş düşük gerilimli ölçüm tarafında kullanılmalıdır; şebeke iletkenine doğrudan prob bağlanmaz.
- ADS1115 analog pinleri üreticinin GND–VDD çalışma aralığı ve mutlak maksimum sınırları içinde tutulur.
