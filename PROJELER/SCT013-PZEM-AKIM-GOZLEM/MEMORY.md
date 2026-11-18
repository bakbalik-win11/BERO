# BERO Project Memory - Gemini CLI
## Proje Vizyonu
**BERO (Burak'ın Rumelikavağı Emeklilik Otomasyonu):**
- **Saha:** Rumeli Kavağı hobi evi.
- **Altyapı:** Dual CAT kablolama (RS485 + 24V Power + Ethernet).
- **Gelecek Modüller:** 
    - Su kuyusu deneyleri (Seviye/Kalite).
    - Gri su geri kazanımı (Tuvalet rezervuarı).
    - Fancoil ile pasif soğutma (Kuyu suyu kullanımı).
- **Bilgi Mirası:** Kod ve dökümantasyonun gelecekte kızına veya bir tamirciye rehberlik edecek düzeyde açık ve sürdürülebilir olması.

## Mevcut Teknik Durum (16 Kasım 2026)
...

- **Donanım:** ADS1115 geçişi ile ölçüm hassasiyeti istenen seviyeye ulaştı (Eski 1.65V bias denemeleri başarısızlık sonrası terk edildi).
- **Modül 4 (Evrensel Test Modülü):** 
    - ESP32 + 3 ADS1115 (Kargoda) + SCT013.
    - Ek sensörler: Ses (Kargoda), Hareket (Envanterden), Titreşim.
    - Amaç: Cihazların yanına taşınabilir, çok modlu veri toplama.
- **Kritik Araçlar:** 
    - FNIRSI 2D15P Osiloskop (Kargoda): Pik/gürültü analizi için.
    - Waveshare Modbus Modülleri: Otomasyon omurgası için hazırda.

## Takip Edilen Dosyalar
- `STATUS.md`: Projenin genel tarihsel özeti.
- `PROGRESS_TREE.md`: Görevlerin hiyerarşik durumu.
- `EXPERIMENT_LEDGER.md`: Yapılan deneylerin kayıt defteri.

## Gemini CLI Notları
- Bu dosya, oturumlar arasında sürekliliği sağlamak için Gemini tarafından güncellenecektir.
- Kullanıcı talimatları ve mimari kararlar burada özetlenecektir.
