# Proje çalışma protokolü

## Oturum başlangıcı — atlanamaz
Kullanıcı için kısa kontrol listesi: [Gün sonu kontrolü](GUN_SONU_KONTROLU.md). Kullanıcıdan teknik diff/JSON/test ayrıntılarını kendi başına denetlemesini bekleme; gerekli kanıtları asistan sunmalı.

1. Mevcut GitHub `main` dalını ve son commit'i kontrol et.
2. Bu dosyayı, `STATUS.md`, `ROADMAP.md`, `docs/open-questions.md` ve ilgili görev/deney dosyasını bu oturumda gerçekten oku.
3. Bir önceki durum kaydıyla depodaki gerçek dosya/PR durumunu karşılaştır.
4. Kullanıcıya işin başlangıç durumunu, hedefini ve kabul ölçütünü kısa biçimde belirt.
5. Bu dosyalar okunamadıysa okumuş gibi davranma; bunu engel olarak belirt.

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

## İş durumu sözlüğü
- **PLANLANDI:** kapsam ve kabul koşulu belirlendi.
- **HAZIRLANDI:** taslak veya değişiklik hazır, hedefe uygulanmış/aktarılmış olmayabilir.
- **UYGULANDI:** değişiklik hedef dalda/ortamda mevcut.
- **DOĞRULANDI:** ilgili kontroller çalıştırılmış ve kanıt kaydedilmiş.
- **TAMAMLANDI:** bütün kabul ölçütleri karşılanmış ve sonuç kanıtla doğrulanmış.
- **ENGELLENDİ:** gereken erişim, donanım, karar veya test yok.

Yalnızca dosyanın var olması ya da bir komutun başarılı dönmesi işi **TAMAMLANDI** yapmaz.

## Görev sözleşmesi
Her anlamlı depo işi için başlamadan önce hedefi, dosya/alan kapsamını, kabul ölçütlerini ve doğrulama yöntemini tanımla. Çalışma sonunda her kabul ölçütünü tek tek sonuçlandır: geçti, kaldı veya uygulanamadı. Başarısız/çalıştırılmayan testi başarılı olarak sunma.

## Güvenlik ve deney etiği
- Deney yapılmadan sonuç yazma. Deney yapılmadıysa results.md bunu açıkça söylemeli.
- 220–240 V şebeke bağlantısını yalnız yetkin kişi, uygun muhafaza ve koruma ile kurmalı.
- CT sekonderini, üretici talimatı izin vermedikçe primer akım geçerken açık bırakma.
- Cihaz, ADC, analog ön uç veya kalibrasyon zinciri değişince yeni calibration_id oluştur.
- Karar değişirse yeni ADR aç; eski kararın tarihçesini silme.

## Oturum sonu — depo işi için zorunlu
Ayrıntılı adımlar [SESSION_PROTOCOL.md](SESSION_PROTOCOL.md) içindedir. Her anlamlı depo çalışmasında:
1. Gerçek değişiklikleri ve Git farkını incele.
2. İlgili testleri/bağlantıları/şemaları doğrula; çalıştırılmayan testleri belirt.
3. `STATUS.md` ve gerektiğinde `ROADMAP.md` / görev dosyalarını güncelle.
4. `HISTORY/SESSION_LOG.md` dosyasına [şablona](HISTORY/SESSION_TEMPLATE.md) uygun oturum kaydı ekle.
5. Dal, commit, PR ve doğrulama kanıtlarını kontrol et.
6. Bir koşul tamamlanmadıysa durumu tamamlandı gösterme; açıkça ENGELLENDİ veya DEVAM EDİYOR olarak bırak.

Bu protokol bir sohbetin kendi kendine başlamasını garanti etmez. Yeni oturumda dosyalar yeniden okunmalı. GitHub Actions, PR'da durum/günlük güncellemesinin yapılıp yapılmadığını kontrol eder; teknik doğruluğun tümünü otomatik kanıtlamaz.

## Oturum sonu
- Deney sonucu için protokol, ortam, cihaz kimlikleri ve veri yolunu kaydet.
- Kanıt yoksa başarı iddiası yazma.
- Depoda değişiklik yapıldıysa kullanıcıya kesin yolları ve PR/commit bağlantısını ver.
- Yalnız yerel dosya hazırlandıysa uzak depoya aktarılmış gibi sunma.
