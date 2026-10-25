# Proje çalışma protokolü

## Oturum başlangıcı
1. AGENTS.md dosyasını oku.
2. STATUS.md'yi oku.
3. ROADMAP.md'de aktif fazı ve tamamlanma ölçütlerini kontrol et.
4. docs/open-questions.md'yi oku.
5. İlgili donanım ve kaynak dosyalarını incele.

## Kapsam
Proje, SCT ADC edinimi, akım özellikleri çıkarımı ve PZEM okumalarıyla zaman eşleştirmesidir. PF hesabı, FFT/THD, harmonik çözümleme, güç kalitesi analizi veya enerji analizörü geliştirme işi önermeyin.

## Değişmez veri kuralları
- PZEM kusursuz ground truth değildir; davranışı ve gecikmesi ölçülecek referans akışıdır.
- -1.0 gibi sentinel değerler, NaN, timeout ve parse hataları geçerli ölçüm gibi ortalamaya girmez.
- Şüpheli sıfır okumalarını doğrulamadan otomatik silme; gerçek elektrik kesintisi de olabilir.
- Sürekli ham ADC arşivi tutma. Normal kayıtta özet, olay çevresinde kısa ham kesit sakla.
- Birden fazla RMS penceresini doğrudan aritmetik ortalamayla birleştirme; örnek sayısı biliniyorsa kareler üzerinden birleştir.
- Her SCT pencere kaydında calibration_id bulunmalı. Kalibrasyon yapılmadıysa uydurma kimlik üretme.
- İstenen örnekleme hızı ile ölçülen gerçek hızı ayrı kaydet.
- Üretici belgesi, kullanıcı raporu, hipotez ve bu projede ölçülen sonucu birbirinden ayır.

## Kanıt etiketleri
- **ÖLÇÜLDÜ:** Bu proje protokolü ve veri kaydıyla gösterilmiş sonuç.
- **ÜRETİCİ BELGESİ:** Üretici/kılavuzda açıkça belirtilmiş.
- **KULLANICI RAPORU:** Forum veya issue gözlemi.
- **HİPOTEZ:** Doğrulanmamış açıklama.
- **HESAP:** Belirtilen varsayımlardan matematiksel olarak türetilmiş.

Etiketsiz teknik iddia yazma.

## Güvenlik ve deney etiği
- Deney yapılmadan sonuç yazma. Deney yapılmadıysa results.md bunu açıkça söylemeli.
- 220–240 V şebeke bağlantısını yalnız yetkin kişi, uygun muhafaza ve koruma ile kurmalı.
- CT sekonderini, üretici talimatı izin vermedikçe primer akım geçerken açık bırakma.
- Cihaz, ADC, analog ön uç veya kalibrasyon zinciri değişince yeni calibration_id oluştur.
- Karar değişirse yeni ADR aç; eski kararın tarihçesini silme.

## Oturum sonu
- STATUS.md ve ROADMAP.md'yi güncelle.
- Tamamlanan işin kabul kanıtını bağlantıla.
- Açık soruları güncelle; çözülmeyen soruları açık bırak.
- Doğrulanmamış kaynak durumunu SOURCES.md'de belirt.
- Ölçüm sonucu için protokol, ortam, cihaz kimlikleri ve veri yolunu kaydet.
