# PREBERO — Güncel durum ve devam noktası

> Bu dosya PREBERO için tek güncel çalışma noktasıdır. Oturuma yeniden başlarken önce burayı oku; ayrıntılı deney verilerini ilgili görev veya donanım kaydından aç. Bu dosyada yalnızca son karar, mevcut aşama, kısa geçmiş ve bir sonraki somut adım tutulur.

## Güncel durum — 2026-11-27

- **Aktif modül/görev:** Modül 2 / MOD2-GRV002 — BERO için pratik PF ölçümü ve PF etkili akım düzeltmesi.
- **MOD2-GRV001:** Kapalı. V1.6 EXP/K(x) modeli ve YAML korunur.
- **Kullanıcının seçtiği ilk yöntem:** ZMPT101B hazır kartını tanı; güvenlik ön kontrolünden sonra trimpotla yaklaşık 220–230 V AC gerilim okumasını PZEM'e yaklaştır; ardından SCT013 ile faz/PF ilişkisini dene.
- **PF deneyi:** Sabit ampul yükünü dimmerin farklı ayarlarında çalıştır; her kararlı pencerede PZEM V/I/P/PF değerlerini BERO'nun ham ve hesaplanan sonuçlarıyla karşılaştır. Dimmer ayarı PF yanında akımı ve dalga şeklini de değiştirebilir.
- **Akım formülü:** BERO PF bilgisiyle yeni PF etkili akım düzeltme adayı geliştirilebilir. Gerilim genlik ayarı, PHASE_CORRECTION ve akım düzeltmesi birbirinden ayrı tutulur. V1.6'ya dokunulmaz; yeni model MOD2-GRV002'de tutulur.
- **PZEM:** Geliştirme/karşılaştırma referansıdır; mutlak doğru kabul edilmez ve son BERO hattı için zorunlu değildir.
- **Araştırma notları:** Diğer yapay zekâların karşılaştırmalı özeti, metodoloji ve dış kaynak incelemeleri isteğe bağlı başvurudur. Güncel deney sırasının yerine geçmez.
- **Kanıt durumu:** Bu yeni yöntem için fiziksel deney, PF katsayısı ve firmware doğrulaması henüz yoktur.

## Bir sonraki somut adım

ZMPT101B kartının ön/arka yüzünü ve revizyon/pin işaretlerini kaydet; trimpotun etkisini ve güvenli ön test düzenini belirle. Kartın giriş devresi, yalıtım/mesafe, terminal koruması ve kapalı test düzeneği kontrol edilmeden 220–230 V bağlantısına geçme. Osiloskop ground klipslerini şebekeye bağlama.

## Modül durumu

| Modül | Çalışma | Durum |
|---|---|---|
| 1 — Bias trafosu | Fiziksel bias güç kutusu | Mevcut; imalat kaydı [burada](MODUL-1-BIAS-TRAFOSU/IMALAT/IMALAT.md) |
| 2 — Akım/PF | MOD2-GRV001 kapalı; MOD2-GRV002 açık | Aktif |
| 3 — Çamaşır makinesi | MOD3-AKM001 saha kaydı | Kayıt tamamlandı; ileri çalışmalar kendi görevinde |
| 4 — Bulaşık makinesi | Program aşaması gözlemi | Bekliyor |
| 5 — Ana pano | Ev içi elektriksel faaliyetleri izleme | Bekliyor |

## Kısa geçmiş

- **2026-11-21:** Biaslı/biassız SCT karşılaştırmaları yapıldı. Biaslı kolun ölçüm ortalamasına etkisi yaklaşık 0,47 A çalışma noktasında gözlendi; gürültü azalması kanıtlanmadı.
- **2026-11-22:** MOD2-GRV001 için V1.6 tek fonksiyonlu EXP/K(x) modeli kabul edildi; görev kapatıldı ve referans korunuyor.
- **2026-11-24:** PF ve PF etkili akım araştırması için MOD2-GRV002 açıldı.
- **2026-11-27:** Kullanıcı, pratik ZMPT trimpot + PZEM gerilim karşılaştırmasıyla başlayıp SCT013/PF denemesine ve yeni akım düzeltme adayına ilerleme sırasını seçti. Henüz deney yapılmadı.

Ayrıntılı teknik geçmiş Modül 2 [TARIHCE.md](MODUL-2-AKIM-TESTLERI/TARIHCE.md), MOD2-GRV002 [görev kaydı](MODUL-2-AKIM-TESTLERI/GOREVLER/MOD2-GRV002/GOREV.md) ve ilgili donanım kayıtlarındadır. Oturum sonunda önce ilgili tarihçe/görev kanıtını, sonra bu dosyadaki güncel durum ve sıradaki adımı yenile.
