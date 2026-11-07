# I007 — CH1 yüksüz kayıt ve kapalı alan istatistik özeti

**Tarih:** 2026-11-07  
**Durum:** İSTATİSTİKSEL EŞİK KARARI VERİLDİ  
**Fiziksel koşul:** Kullanıcı teyidine göre ölçülen hatta yük/enerji yok; fiziksel akım 0 A.  
**Kanal:** CH1  
**Katsayı:** K=24.22

## Kayıt kapsamı

- Süre: yaklaşık 10 saat (9 saat 59 dakika 59 saniye).
- Home Assistant CH1 akım entity: 36.002 örnek.
- Home Assistant CH1 ham SCT entity: 36.002 örnek.
- İncelenen kayıt aralığı: 2026-11-06 21:00:00 UTC – 2026-11-07 06:59:59.863 UTC.
- Kaynak CSV depoya eklenmedi; kullanıcı isteği doğrultusunda yalnızca istatistiksel dayanak tutuldu.

## Dağılım özeti

| İstatistik | CH1 ham SCT | K=24.22 uygulanmış akım |
|---|---:|---:|
| Medyan | 0,00853020 | 0,20660140 A |
| P90 | 0,00941586 | 0,22805208 A |
| P95 | 0,00973880 | 0,23587365 A |
| P99 | 0,01136321 | 0,27521688 A |
| Maksimum | 0,03967249 | 0,96086776 A |

0,24 A eşiğinde K uygulanmış 36.002 ölçümün %96,33'ü eşik altında veya eşittir; %3,67'si üzerindedir.

## Sonuç ve yorum

P95 değeri 0,23587365 A olduğundan, bunun hemen üzerinde yuvarlak ve uygulanabilir bir kapalı alan sınırı olarak **0,24 A** seçildi. Sıçramalar eşik seçiminde aykırı değer temizliğiyle giderilmedi; kullanıcının isteği doğrultusunda dağılımın doğal parçası olarak bırakıldı.

Bu istatistik CH1 ve bu fiziksel yüksüz kayıt koşuluna aittir. CH2/CH3'e veya farklı donanım/kurulumlara genellenmez.

## Karar ve sonraki aralık

- **0–0,24 A:** Kapalı alan.
- **0,24 A–ilk güvenilir akım okuması:** Hesaplanmadı alanı.
- **İlk güvenilir akım okuması ve üzeri:** Hesaplanacak alan.

İlk güvenilir okumanın sayısal sınırı henüz bilinmiyor; sonraki kontrollü yük deneylerinin hedefi bu sınırı bulmaktır.

**İlgili karar:** [ADR-031 — CH1 yüksüz kapalı alan eşiği](../../../docs/decisions/ADR-031-ch1-idle-closed-area-threshold.md).
