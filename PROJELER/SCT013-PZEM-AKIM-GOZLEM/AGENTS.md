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
2. **Faz 2 — Pratik yeniden kurulum ve sistem geliştirme: AKTİF.** Faz 2, yalnız mevcut kodu PZEM ile eğitme aşaması değildir. Kayıtlı kodlar ve çalışan örneklerden yararlanarak modüller/ESP düğümleri yeniden devreye alınır, temel işlevleri gerçek donanımda doğrulanır ve sistem geliştirilir. PZEM referanslı veri aktarımı/etiketleme bu işleyen sistemin sonraki alt aşamasıdır.

Faz 2'nin ilk aktif görevi T009'dur: modülleri ve ESP düğümlerini pratik olarak devreye alma. Ardından T007 → T008 → T006 yürütülür. Her oturumda STATUS.md içindeki tek aktif görev üzerinde çalış. Faz 1 deneylerini yeniden açma. Yeni deneyler ancak gerçek bir uygulama/ölçüm sorusu ortaya çıktığında yeni numaralarla planlanır.

## Pratik geliştirme ilkesi

- Önce çalışan kod, örnek proje, kütüphane veya hazır modül uygulaması bul ve değerlendir; sonra gereken en az uyarlamayı yap.
- Depodaki YAML'lar, kodlar, loglar ve kararlar başlangıç referansıdır; yeni kurulumda gerekirse kontrollü biçimde uyarlanabilir.
- Donanım ve ESP düğümlerini modül modül, tek işlevden başlayarak devreye al. Derleme, bağlantı ve gerçek çıktı adımlarını ayrı doğrula.
- Ana hedef çalışan sistemi kurmak ve SCT akımını güvenilir biçimde okuyabilmektir. Teorik derinleşme, manyetik modelleme veya ESP32 ADC iç mimarisi incelemesi yalnız somut bir engel/arıza/karar gerektirirse yapılır.
- Önceki teorik ve ADC araştırmalarını silme veya değersizleştirme; bunlar gerektiğinde başvurulacak tarihsel teknik kayıttır.
- Gerçek test/log olmadan kodu çalışıyor, modülü tamamlandı olarak gösterme.

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

1. T009 — Modülleri ve ESP düğümlerini pratik olarak yeniden devreye alma.
2. T007 — Çalışan PZEM/SCT düğümlerinin HA geçmişini PC'ye aktarma.
3. T008 — PZEM/SCT kararlı alanlarını ayrı bulma, örtüşen alanları eşleştirme ve PZEM ile etiketleme.
4. T006 — K=24.22 katsayısını değerlendirme; veri gerekçelendirirse model iyileştirme.

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
