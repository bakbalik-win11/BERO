# BERO Project Memory - Gemini CLI

## Proje Vizyonu
Hassas enerji izleme, akım karakterizasyonu (çamaşır makinesi vb. yük analizi) ve çok kanallı (12 SCT hedeflenen) bir ölçüm sistemi geliştirilmesi.

## Mevcut Teknik Durum (16 Kasım 2026)
- **Donanım:** ESP32 tabanlı, ADS1115 (ADC) ve SCT013 sensörleri kullanılıyor. PZEM-004T referans olarak kullanılıyor.
- **Kritik Sorunlar:** 
    - ADS1115 üzerinde yüksüz hatta rastgele sıçramalar (spikes) gözleniyor (E19 deneyi).
    - Çoklu ADS1115 (E24) için I2C bus genişleme planı (3 ADS modülü tek ESP32).
- **Aktif Deneyler:** 
    - E21: Çamaşır makinesi program analizi (Kayıt bekleniyor).
    - E23: Yeni modül ile sıçrama karşılaştırması.

## Takip Edilen Dosyalar
- `STATUS.md`: Projenin genel tarihsel özeti.
- `PROGRESS_TREE.md`: Görevlerin hiyerarşik durumu.
- `EXPERIMENT_LEDGER.md`: Yapılan deneylerin kayıt defteri.

## Gemini CLI Notları
- Bu dosya, oturumlar arasında sürekliliği sağlamak için Gemini tarafından güncellenecektir.
- Kullanıcı talimatları ve mimari kararlar burada özetlenecektir.
