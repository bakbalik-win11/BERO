# IRON-001 — Ütü / termostatlı yüksek akım gözlemi

## HEDEF
Tek sarım Modül 2 / SCT-1 düzeninde ütünün termostat çevrimlerini gözlemek. Açık kararlı bölümler, kapalı süreler ve geçişler aynı deneyin geçerli verileridir. Termostatın uzun süre kapalı kalması veri kaybı veya deney hatası sayılmaz.

## DÜZENEK
- Yük: ütü; termostat nedeniyle otomatik açma-kapama.
- Modül: 2 / ESP32D1 / SCT-1 GPIO32 ADC1_CH4 / ortak bias GPIO35 ADC1_CH7.
- ESPHome: 2026.10.1.
- ADC: 12 dB, 1 s güncelleme; ct_clamp örnek penceresi 200 ms, çıktı güncellemesi 2 s.
- K: 24.22; firmware ve yazılımsal eşik değiştirilmeyecek.
- Primer: tek tur.
- UNIT: 10,16 A kullanıcı bildirimi; ölçümün her SCT kararlı penceresiyle eşzamanlılığı ayrıca teyit edilmelidir. PZEM değildir.

## DEĞERLENDİRME KURALI
1. Ütü açıkken kararlı akım örnekleri ayrı analiz edilir.
2. Termostat kapalıyken sıfır ve sıfıra yakın değerler korunur; kapalı kalma süresi deney verisidir.
3. Açılma/kapanma geçişleri ayrı işaretlenir.
4. Her yeni çevrim bağımsız özetlenir; tüm çevrimlerin tek ortalaması geçişleri ve kapalı süreleri maskelemez.
5. Eksik log aralıkları ölçülmüş süre gibi yorumlanmaz.
6. UNIT ve PZEM ayrı kaynaklardır. Eşzamanlılık doğrulanmadan sapma, doğruluk veya kalibrasyon kararı verilmez.

## 2026-10-31 — İlk iki log parçası (Log 60–61)
- Log 60: 25.500 bayt / 361 satır; kaynak SHA-256 `77b60843c4812ac2c9f585d225afbe37511732519bb6eefdcba1014d4413ed54`.
- Log 61: 11.129 bayt / 170 satır; kaynak SHA-256 `01197ceecfcb9519ae9b26b1323a4db284b404690f39075c71639fc39f69da96`.
- SCT akım yayınları: Log 60'da 38, Log 61'de 11; toplam 49.
- Açık çevrim 1: 5 yayın, 21:40:42.179–21:40:50.187; ortalama 9,2852 A; medyan 9,291 A; aralık 9,237–9,311 A; örnek SD 0,0285 A.
- Açık çevrim 2: 4 yayın, 21:43:50.190–21:43:56.173; ortalama 9,3605 A; medyan 9,351 A; aralık 9,314–9,426 A; örnek SD 0,0542 A.
- UNIT 10,16 A'ya göre aritmetik ortalama farkları sırasıyla −%8,61 ve −%7,87'dir. UNIT/SCT zaman örtüşmesi doğrulanmadığı için bunlar yalnız betimleyici hesap olarak tutulur.
- Kapalı/düşük akım sınıfı (SCT ≤0,25 A): 40 yayın; 27 tam 0,000 A; kalan 13 yayın 0,011–0,092 A aralığında. Bu değerler silinmedi veya aykırı diye atılmadı.
- Log 60'da 21:40:52.182'de 0,000 A'ya düşüş ve 21:41:56.178'e kadar kapalı/düşük akım yayınları var. Log 61'de 21:43:40.175–21:43:48.182 aralığında yeniden düşük akım, 21:43:50.190'da tekrar 9,426 A yükselişi ve 21:43:58.169'da 0,047 A'ya iniş görülüyor.
- İki dosya arasında yaklaşık 104 saniyelik kayıt boşluğu vardır. Bu boşlukta ne olduğu bilinmiyor; kapalı süreye ölçülmüş veri olarak eklenmez.
- Bu ilk parçalar kısa çevrim örnekleridir; uzun dönem kararlılık veya nihai doğruluk sonucu değildir. PZEM verisi bu loglarda yoktur.
- Ham loglar: [Log 60](log60-full.txt), [Log 61](log61-measurement-evidence.txt).
- Analiz: [ilk bölüm analizi](initial-analysis.md).

## IRON-001 KAPANIŞ RAPORU — 2026-10-31

**Kapanış kapsamı:** Kullanıcının sağladığı iki log parçasının gözlem raporu. Ütünün tüm termostat çalışma aralığı veya uzun dönem çevrim karakteristiği doğrulanmış değildir.

### Sonuç tablosu

| Parametre | Çevrim 1 | Çevrim 2 |
|---|---:|---:|
| Açık durum yayını | 5 | 4 |
| Açık pencere | 8,008 s | 5,983 s |
| Ortalama SCT akımı | 9,2852 A | 9,3605 A |
| Medyan | 9,291 A | 9,351 A |
| Min–maks | 9,237–9,311 A | 9,314–9,426 A |
| Örnek SD | 0,0285 A | 0,0542 A |

UNIT 10,16 A kullanıcı bildirimine göre çevrim ortalamalarının aritmetik farkı sırasıyla −%8,61 ve −%7,87'dir. UNIT ile SCT örneklerinin tam zaman eşleşmesi doğrulanmadığından bu farklar doğruluk veya kalibrasyon sonucu değildir.

### Kapalı durum ve geçiş verisi

- İki logda toplam 49 SCT akım yayını vardır.
- SCT ≤0,25 A sınıfında 40 yayın: 27 tam 0,000 A; 13 yayın 0,011–0,092 A.
- Log 60'da 21:40:52.182'de akım 0,000 A'ya düşmüştür. Log 61'de 21:43:50.190'da 9,426 A'ya yükselmiş, 21:43:58.169'da 0,047 A'ya inmiştir.
- Log 60 son yayını ile Log 61 ilk yayını arasında yaklaşık 104 saniyelik kayıt boşluğu vardır. Bu aralık ölçülmüş kapalı süre olarak raporlanmaz.
- Kapalı durumdaki sıfır ve sıfıra yakın okumalar geçerli veri olarak korunmuştur; aykırı diye silinmemiştir.

### Teknik değerlendirme

**LOG İLE DESTEKLENDİ:** İki kısa açık çevrimde SCT-1 yaklaşık 9,3 A göstermiş; kapalı/düşük akım durumunda sıfır ve sıfıra yakın okumalar kaydedilmiştir.

**KULLANICI BİLDİRİMİ:** UNIT 10,16 A.

**HESAP:** Açık çevrim ortalamalarının UNIT'e göre aritmetik farkları −%8,61 ve −%7,87.

**SINIRLAR:** PZEM kaydı yoktur. UNIT zaman eşleşmesi doğrulanmamıştır. İki çevrim, ütünün tüm termostat davranışını veya uzun süreli performansını temsil etmeye yeterli değildir.

**KARAR:** IRON-001, mevcut iki logun gözlem ve ön değerlendirme raporu tamamlandığı için kapatıldı. Bu kapanış, doğruluk/kalibrasyon onayı anlamına gelmez. Firmware ve K=24.22 değiştirilmemiştir.

## DURUM
KAPATILDI — iki logluk gözlem raporu tamamlandı; kapsam ve veri sınırları yukarıda belirtilmiştir.
