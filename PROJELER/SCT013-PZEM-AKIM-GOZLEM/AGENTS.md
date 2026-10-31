# Proje çalışma protokolü

## En yüksek öncelik: depo sürekliliği

- Her oturumun başında bu dosyayı, STATUS.md, ROADMAP.md ve ilgili görev/deney dosyalarını oku.
- Yeni karar, kod, deney koşulu, sonuç ve iş sırası değişikliğini aynı çalışma akışında uygun dosyaya kaydet.
- Geçmiş kayıtları silme; karar değişirse yeni ADR ile tarihçeyi koru.
- Depo yazımından sonra dosyayı yeniden oku ve bağlantıları doğrula.
- Yapılmamış işi tamamlandı, doğrulanmamış kodu çalışır diye sunma.

## İki fazlı proje yapısı

Projede yalnızca iki ana faz vardır:
1. **Faz 1 — Çalışan kodu bulmak ve ±%4 hedefine ulaşmak: TAMAMLANDI.** Dış kaynaklı kodla hedef sağlandı. Faz 1 kapsamındaki yapılmamış işler hedefe ulaşıldığı için kapatılmıştır; eski deney dosyaları tarihsel arşivdir.
2. **Faz 2 — Bulunan kodu PZEM ile eğitmek: AKTİF.** İlk görev T007 HA → PC veri aktarımı; sonra T008 kararlı alan eşleştirme/etiketleme; ardından T006 katsayı/model değerlendirmesi.

Her oturumda STATUS.md içindeki tek aktif görev üzerinde çalış. Faz 1 deneylerini yeniden açma. Faz 2 için yeni deneyler ancak somut veri sorusu ortaya çıktığında yeni numaralarla planlanır.

## Değişmez cihaz kimliği

- ESP32D2 cihaz kimliği değiştirilemez.
- YAML düzenlemelerinde esphome.name aynen korunur.
- Her YAML değişikliğinde cihaz kimliğini önce/sonra karşılaştır.

## Veri ve ölçüm kuralları

- PZEM proje referansıdır; kusursuz ground truth değildir.
- -1.0, NaN, timeout ve parse hataları etiketlemeden çıkarılır; ham kaynak kayıt silinmez.
- Şüpheli sıfır okumaları doğrulamadan otomatik silinmez.
- Sürekli ham ADC arşivi tutma; Faz 1'de bu ara iş kapatılmıştır.
- Her SCT etiketli pencere kaydında gerçek calibration_id bulunur; yoksa uydurulmaz.
- Kaynak timestamp, timezone, entity_id, birim ve ham değer korunur.
- Ölçülen sonuç, paylaşılan log, üretici belgesi, hipotez ve hesap birbirinden ayrılır.
- Kullanıcının sağladığı deney logları ve bunlardan çıkarılan karşılaştırma sonuçları proje kanıtıdır; bunları yalnız sözlü beyan gibi etiketleme.

## Kanıt etiketleri

- **ÖLÇÜLDÜ / LOG İLE DESTEKLENDİ:** Proje deneyi veya paylaşılan cihaz loglarıyla desteklenen sonuç.
- **ÜRETİCİ BELGESİ:** Üretici/kılavuzda açıkça belirtilmiş bilgi.
- **HİPOTEZ:** Doğrulanmamış açıklama.
- **HESAP:** Belirtilen varsayımlardan matematiksel olarak türetilmiş sonuç.
- **KULLANICI BİLDİRİMİ:** Yalnızca log veya başka kayıtla desteklenmeyen sözlü bilgi.

Etiketsiz teknik iddia yazma.

## İş durumu sözlüğü

- **PLANLANDI:** hedef ve kabul koşulu belirlendi.
- **HAZIRLANDI:** taslak veya değişiklik hazır.
- **UYGULANDI:** değişiklik hedef dosyada/ortamda mevcut.
- **DOĞRULANDI:** ilgili kontroller ve kanıt incelendi.
- **TAMAMLANDI:** kabul ölçütleri karşılandı.
- **KAPATILDI — HEDEFE ULAŞILDI:** Faz hedefi başka bir yolla sağlandığı için kalan iş yapılmadan kapatıldı.
- **ENGELLENDİ:** gereken erişim, donanım, karar veya test eksik.

## Faz 2 görev sırası

1. T007 — HA geçmişini PC'ye aktarma ve Python veri giriş hattı.
2. T008 — PZEM/SCT kararlı alanlarını ayrı bulma, örtüşen alanları eşleştirme ve PZEM ile etiketleme.
3. T006 — K=24.22 katsayısını değerlendirme; veri gerekçelendirirse model iyileştirme.

## HEDEF / LOG / SONUÇ standardı

Her anlamlı işte:
- **HEDEF:** Soruyu, nedeni ve kabul koşulunu yaz.
- **LOG:** Gerçekte yapılan işlemi, gerçek ayarları, dosya/hash ve çıktıyı kaydet.
- **SONUÇ:** Kanıtın desteklediği yorumu ve sınırları yaz.
Başarılı kodla birlikte gerçek çıktı/log örneği ve yorum depoda saklanır.

## Güvenlik

- 220–240 V şebeke bağlantısını yalnız yetkin kişi, uygun muhafaza ve koruma ile kurmalı.
- CT sekonderini, üretici talimatı izin vermedikçe primer akım geçerken açık bırakma.
- Açık breadboard şebeke tarafında kullanılmaz.

## Oturum sonu

- Gerçek değişiklikleri ve Git farkını incele.
- Yazılan dosyaları yeniden oku; bağlantıları ve durum tutarlılığını doğrula.
- STATUS.md ve PROGRESS_TREE.md güncel tutulur.
- HISTORY/SESSION_LOG.md dosyasına hedef, yapılan iş, doğrulama ve açık kalanlar eklenir.
- Test edilmemiş işi tamamlandı gösterme.
