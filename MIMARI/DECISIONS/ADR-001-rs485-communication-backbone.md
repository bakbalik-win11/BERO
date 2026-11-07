# ADR-001 — BERO kalıcı haberleşme omurgası olarak RS485

- **Durum:** KABUL EDİLDİ
- **Tarih:** 2026-11-07
- **Karar sahibi:** Kullanıcı
- **Kapsam:** BERO genel haberleşme tercihi

## Bağlam

BERO'da ESP tabanlı düğümler arasında kalıcı bir haberleşme omurgası belirlenmesi gerekmektedir.

## Karar

**RS485, BERO'nun kalıcı ve temel haberleşme omurgası olacaktır.** ESP tabanlı düğümler arası veri aktarımı RS485 üzerinden tasarlanacaktır.

## Katman ayrımı

RS485 fiziksel/elektriksel haberleşme katmanını tanımlar. Modbus RTU gibi bir protokolün seçilmesi, BERO düğümleri arasındaki uygulama mesajlaşma protokolünü kendiliğinden belirlemez.

## Henüz belirlenmeyenler

Bu karar; RS485 transceiver modeli, kablo ve damar tahsisi, baud hızı, topoloji, terminasyon/bias, adresleme, mesaj çerçevesi, bus erişimi ve hata yönetimi gibi uygulama ayrıntılarını belirlemez.

## Doğrulama sınırı

Bu kayıt mimari tercihi belgelendirir. RS485 ağı henüz kurulmuş veya gerçek donanım üzerinde test edilmiş değildir.
