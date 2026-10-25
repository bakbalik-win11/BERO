# Akım kalibrasyon prosedürü

**Durum: HAZIR, UYGULANMADI.** Tercihen kalibrasyon durumu bilinen True-RMS ampermetre kullan; PZEM'i kusursuz referans varsayma.

## Ön koşullar
- Güvenlik listesi tamamlanmış.
- SCT varyantı ve analog ön uç doğrulanmış.
- ADC VREF ve bias ölçülmüş.
- En az üç kontrollü rezistif yük seviyesi hazır.

## Adımlar
1. Tarih, cihaz kimlikleri, ortam ve bağlantı şemasını kaydet.
2. Yük kapalıyken ADC ortalaması ve gürültüsünü en az 30 s gözle.
3. Düşük, orta ve yüksek güvenli akım seviyelerinde referans akım ve aynı aralıktaki SCT RMS'i kaydet.
4. Her nokta için sample_count, gerçek örnekleme hızı, pencere süresi ve clipping'i yaz.
5. Dönüşüm katsayısını hesapla; kullanılan noktaları belirt.
6. Kalibrasyonda kullanılmayan bir doğrulama noktasıyla sınama yap.
7. Yeni calibration_id oluştur ve calibrations.csv'ye ekle.

Kabul toleransı deneyden önce belirlenmeli. Sonuca göre geriye dönük tolerans değiştirme; değişiklik gerekçesini kaydet.
