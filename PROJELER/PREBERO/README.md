# PREBERO — Yeni çalışma aşaması

**Durum:** AÇIK — yeni başlangıç.

Önceki SCT/PZEM akım okuma çalışmasının pratik hedefi, SCT + ADS1115 zinciriyle hedeflenen ev içi yük koşullarında akım okuyabilmekti. Bu hedefe ulaşıldığı kabul edilerek eski çalışma kapatıldı; tüm kod, deney, log ve kararlar [tarihsel arşivde](../SCT013-PZEM-AKIM-GOZLEM/README.md) korunuyor.

PREBERO yeni ve bağımsız çalışma alanıdır. Eski PZEM kararlı pencere/eğitim hattı, çok kanallı SCT planları, eski ses-titreşim donanım listeleri ve eski görev sıraları yeni aşamaya otomatik olarak taşınmaz.

## Güncel sıra
1. ADS1115 hobi düzeyinde teknik raporu.
2. Masaüstü ESP32D2 + ADS1115 + SCT prototipinin gerçek bağlantı ve yazılım incelemesi.
3. Bias'lı/bias'sız ölçüm karşılaştırması.
4. Osiloskopla sinyal gözlemi.
5. Modül 4 tasarım kararı, imalatı ve gerçek donanım doğrulaması.
6. Modül 4 kabulünden sonra Modül 5/6/7 saha ihtiyaçlarının yeni baştan tanımlanması.

## Modül görünümü
- **Modül 4:** Masaüstü ESP32D2 + ADS1115 + SCT prototipini inceleme ve sabit modüle dönüştürme. Henüz nihai modül değildir.
- **Modül 5:** Çamaşır makinesi gözlem ihtiyacı — yeniden tanımlanacak.
- **Modül 6:** Bulaşık makinesi gözlem ihtiyacı — yeniden tanımlanacak.
- **Modül 7:** Ana hat/PZEM gözlem ihtiyacı — yeniden tanımlanacak.

Modül 5/6/7 adları şimdilik çalışma başlığıdır. Eski ESP32-D, MAX4466, MPU6050, ikiz donanım ve besleme kararları yeni aşamada onaylı tasarım değildir.

## Açık kararlar
- ADS1115 AIN pinlerinin gerçek gerilimleri ve ortak-mod davranışı.
- Bias gerekli mi?
- Bias gerekiyorsa nasıl üretilecek?
- Modül 4'ün nihai analog ön ucu, beslemesi, bağlantıları ve fiziksel tasarımı.
- Modül 5/6/7'nin yeni sensörleri, haberleşmesi, veri kaydı ve kurulum biçimi.

## Hobi projesi sınırı
ADS1115 üzerinde laboratuvar seviyesinde kapsamlı karakterizasyon hedeflenmez. BERO'da doğru ve güvenli kullanım için gereken veri sayfası bilgisi, temel hesaplar ve osiloskop gözlemleri yeterlidir. Üreticinin elektriksel sınırları ve güvenlik koşulları mutlaka gözetilir.

## Başlangıç okuma sırası
1. [AGENTS.md](AGENTS.md)
2. [STATUS.md](STATUS.md)
3. [ROADMAP.md](ROADMAP.md)
4. [PROGRESS_TREE.md](PROGRESS_TREE.md)
5. [ADR-001](docs/decisions/ADR-001-prebero-scope-reset.md)
6. [T001 — ADS1115 teknik raporu](tasks/T001-ads1115-technical-report.md)
