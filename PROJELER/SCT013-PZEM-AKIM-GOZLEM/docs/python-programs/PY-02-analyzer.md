# PY-02 — BERO Analyzer

- Durum: TASLAK — kullanıcı incelemesi bekliyor.
- Tür: Kullanıcı tarafından başlatılan ana giriş noktası; küçük analiz görevlerini yönetir.
- Platform: Windows ARM64 ve macOS ARM64.
- Çalışma alanı: Harici SSD.
- İlgili kararlar: ADR-022, ADR-024, ADR-025, ADR-027, ADR-028, ADR-029, ADR-030.
- İlgili görev sırası: T007 → T008 → T006.

## Amaç

PY-01 tarafından RAW arşive alınmış HA History kayıtlarını değiştirmeden okumak; veri profilini çıkarmak, olay paketlerinin bütünlüğünü denetlemek, PZEM ve SCT kararlılığını ayrı ayrı incelemek, geçerli eşleşmelerden tek kanallı eğitim verisi üretmek ve tam kayıt davranışını değerlendirmek.

## Sorumluluk sınırı

Yalnız SSD'deki RAW arşivden okur. Gelen-kutu yönetmez, RAW dosyaları değiştirmez, HA'ya veya Recorder'a bağlanmaz. Her analiz çıktısı RAW kaynaktan ayrı türetilmiş alanda saklanır.

## Alt görevler

1. ANL-01 Arşiv envanteri: RAW dosyaları ve manifest kayıtlarını listeler; kaynak hash'iyle izlenebilir envanter üretir.
2. ANL-02 Veri profili: CSV kolonlarını, entity_id değerlerini, zaman aralığını, birimleri, boş/geçersiz/tekrar kayıtları raporlar. Ham kaydı değiştirmez.
3. ANL-03 Olay paketi doğrulama: PZEM ve SCT olay akışlarını ayrı ayrı ADR-022/024 ile kontrol eder. Eksik ON/OFF, EVENT_ID boşluğu, sıra hatası veya BOOT_ID değişimini tahminle düzeltmez.
4. ANL-04 PZEM kararlılığı: PZEM'in kendi akışından kararlı alan adayları çıkarır. Parametreler gerçek veriden sonra belirlenecek.
5. ANL-05 SCT kararlılığı: CH1/CH2/CH3 akışlarını birbirinden bağımsız inceler. Sayısal kararlılık tanımı henüz açık değildir.
6. ANL-06 Kararlı alan örtüşmesi: geçerli aynı ON paketi içindeki kararlı alanların zaman kesişimini hesaplar. ADR-028'e göre başlangıçta SCT ve PZEM birlikte kararlı olmalı; alan SCT kararlılığını kaybedince bitmelidir. PZEM'in gecikmeli OFF'u alanı uzatmaz.
7. ANL-07 Eğitim etiketi: PZEM akımını proje referansı olarak eşleşen SCT alanına ekler. Her set tek SCT kanalıdır; CH1-E/CH2-E/CH3-E seçimi ADR-027'ye uyar.
8. ANL-08 Tam kayıt değerlendirmesi: öğrenilmiş katsayı/modeli ham kaydın tamamında davranış açısından değerlendirir. Geçişte PZEM'i örnek başına mutlak referans saymaz.
9. ANL-09 Rapor üretimi: doğrulanmış çıktıları kaynak hash'i, görev sürümü, kanal, turn_count ve gerçekse calibration_id bilgileriyle raporlar.

## Girdi

- PY-01 tarafından oluşturulmuş RAW arşiv ve alım manifestosu.
- Kullanıcı tarafından onaylanmış entity/kanal eşleme yapılandırması.
- Olay protokolü ve ilgili ADR'ler.
- Gerçekse calibration_id, firmware/kod sürümü ve turn_count. Bilinmeyen değer uydurulmaz.

## Çıktı

Veri profili; paket doğrulama raporları; ayrı PZEM/SCT kararlılık tabloları; örtüşme tablosu; tek kanallı etiketli eğitim setleri; tam kayıt değerlendirmesi; kaynak hash'i, görev sürümü ve parametreleri içeren işlem kayıtları.

## Hata ve yeniden başlatma davranışı

- Her alt görev kendi checkpoint ve çıktı kaydına sahip olur.
- Bir görev başarısız olursa önceki görevlerin doğrulanmış çıktıları korunur.
- Yarım çıktı nihai dosya olarak yayımlanmaz.
- Bir dosyanın/kanalın hatası diğer bağımsız analizleri engellemez.
- Tekrar çalıştırmada girdi hash'i ve görev sürümü kontrol edilir; eski sonuç sessizce üzerine yazılmaz.
- Algoritma/parametre değişirse yeni görev veya çıktı sürümü üretilir.

## Başarı ölçütleri

- RAW arşiv değişmeden kalır.
- Her çıktı kaynak dosyayı ve görev sürümünü gösterir.
- Paket hataları tahminle düzeltilmez.
- PZEM ve SCT kararlılıkları bağımsız hesaplanır.
- Eşleştirme geçerli paket ve örtüşme kurallarını uygular.
- Eğitim seti tek SCT kanalından oluşur.
- Kesinti sonrası son doğrulanmış checkpoint'ten devam edilebilir.
- Gerçek CSV ile çıktı/log ve yorumu depoya eklenir.

## Kapsam dışı

HA/Recorder bağlantısı; RAW arşiv değişikliği; veriyi görmeden kararlılık parametresi seçmek; PZEM'i kusursuz ground truth saymak; enerji analizi, PF, FFT/THD.

## Açık sorular

- Analiz görevleri tek tek mi başlatılacak, yoksa PY-02 bağımlılık sırasına göre mi çalıştıracak?
- PZEM/SCT kararlılık çıktılarının ortak veri şeması ne olacak?
- Paket doğrulaması iki akış için ayrı mı, birleşik mi raporlanacak?
- Büyük CSV'lerde ara veri biçimi ve bellek stratejisi ne olacak?
