# ADR-001 — PREBERO yeni aşama kapsamı

- **Tarih:** 2026-11-20
- **Durum:** KABUL EDİLDİ
- **Karar sahibi:** Kullanıcı

## Karar
Önceki SCT013/PZEM akım okuma çalışması, SCT + ADS1115 zinciriyle hedeflenen ev içi yük koşullarında akım okuyabilme hedefine ulaştığı için kapatılır. Eski proje dosyaları ve deney/kod/log/karar kayıtları tarihsel arşiv olarak korunur.

Yeni çalışma PREBERO adıyla ayrı proje klasöründe, temiz görev ve dokümantasyon ağacıyla başlar. Eski projenin diğer hedefleri, deney sıraları, görevleri ve donanım planları yeni aşamanın aktif gereksinimi değildir.

## Başlangıç sırası
1. ADS1115 hobi düzeyinde teknik raporu.
2. Masaüstü ESP32D2 + ADS1115 + SCT prototipinin gerçek bağlantı incelemesi.
3. Bias'lı/bias'sız karşılaştırma.
4. Osiloskopla sinyal gözlemi.
5. Modül 4 tasarım kararı, imalatı ve doğrulaması.
6. Modül 4 kabulünden sonra Modül 5/6/7 saha ihtiyaçlarını yeni baştan tanımlama.

## Açık kararlar
- Bias gerekli mi ve gerekiyorsa nasıl üretilecek?
- ADS1115 giriş topolojisi ve gerçek pin gerilimleri.
- Modül 4 nihai bağlantı ve fiziksel tasarımı.
- Modül 5/6/7'nin yeni kapsamı ve donanım mimarisi.

## Devralınmayan eski hedefler
PZEM kararlı pencere/eğitim hattı; eski Modül 2/3 çoklu SCT ve SSR/UDP mimarisi; eski Modül 5/6 ikiz ses-titreşim donanım listesi; 12 kanal genişleme ve E22/E24 fikirleri; eski T001–T011 görev sıraları.

Bu karar eski ölçüm sonuçlarını geçersiz kılmaz. Yalnızca yeni aşamanın hedef ve iş sırasını yeniden başlatır.
