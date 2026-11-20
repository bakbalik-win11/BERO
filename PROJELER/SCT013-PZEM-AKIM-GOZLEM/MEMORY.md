# BERO Project Memory - Gemini CLI
## Proje Vizyonu
**BERO (Burak'ın Rumelikavağı Emeklilik Otomasyonu):**
- **Saha:** Rumeli Kavağı hobi evi.
- **Altyapı:** Dual CAT kablolama (RS485 + 24V Power + Ethernet).
- **Su Yönetimi & Korelasyon:**
    - Ana su hattı basınç sensörü (Kesinti/Arıza tespiti).
    - Cihaz-Su İlişkisi: Su kesintisi nedeniyle makinenin su alamayıp beklemede kalmasını ayırt eden zeka (Basınç yok + Akım düşük + Ses yok -> Su Kesintisi Bildirimi).
- **Gelecek Modüller:** 
    - **Akıllı Havalandırma:** CO2, Toz (PM2.5/10) ve HEPA filtre sağlığı (basınç farkı ile).
    - **Isı Geri Kazanımı:** Seramik serpantinli ısı geri kazanımlı havalandırma (Heat Recovery Ventilation).
    - **Enerji Yönetimi:** Oda bazlı klape kontrolü (boş odaları ısıtma/soğutma dışı bırakma).
    - **Güvenlik:** Mutfak özelinde vana ve tehlikeli gaz yönetimi.
    - **Su Dünyası:** Su kuyusu deneyleri, gri su geri kazanımı ve fancoil ile pasif soğutma.
- **Bilgi Mirası:** Kod ve dökümantasyonun gelecekte kızına veya bir tamirciye rehberlik edecek düzeyde açık ve sürdürülebilir olması.

## Mevcut Teknik Durum (16 Kasım 2026)
...
## Mevcut Teknik Durum (16 Kasım 2026)
- **Donanım:** ADS1115 geçişi ile ölçüm hassasiyeti ulaşıldı. 
- **Aktif masaüstü düzenek:** Modül 4 = mevcut günlük ESP32D2 + ADS1115 + SCT ölçüm düzeneği.
- **PREBERO Fazı (Yeni):** Gerçek BERO öncesi saha veri toplama ve test aşaması.
    - Modül 4 (Çamaşır) & Modül 5 (Bulaşık): Akım + Ses + Titreşim (WiFi üzerinden HA'ya).
    - Modül 6 (Ana Giriş): SCT + ADS1115 + PZEM (WiFi üzerinden HA'ya).
- **Düğüm Otonomisi:** Uç birimlerin (ESP32) HA veya ekran bağımsız çalışabilmesi, yerel veri kaydı ve kesinti sonrası senkronizasyon yeteneği.
- **PREBERO Laboratuvarı:** ESP32-S3 Ekranlı kart + Raspberry Pi 4 (HA) + Çift RS485 hattı (Master/Slave rolleri) ile masaüstü test düzeneği.


## Takip Edilen Dosyalar
- `STATUS.md`: Projenin genel tarihsel özeti.
- `PROGRESS_TREE.md`: Görevlerin hiyerarşik durumu.
- `EXPERIMENT_LEDGER.md`: Yapılan deneylerin kayıt defteri.

## Gemini CLI Notları
- Bu dosya, oturumlar arasında sürekliliği sağlamak için Gemini tarafından güncellenecektir.
- Kullanıcı talimatları ve mimari kararlar burada özetlenecektir.
