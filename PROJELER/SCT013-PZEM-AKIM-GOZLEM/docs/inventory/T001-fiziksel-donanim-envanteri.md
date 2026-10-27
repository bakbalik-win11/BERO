# T001 — Fiziksel Donanım Envanteri

**Durum:** Tamamlandı. Bilgiler kullanıcı beyanına dayanmaktadır.

## Kontrol ve ölçüm donanımı

| Bileşen | Özellik / adet | Durum |
|---|---|---|
| ESP32-C3 SuperMini | 1 | Mevcut |
| ESP32 ölçüm düğümü | 1 | Mevcut |
| SSR kartı | SAMM Market, 5 V, 2 kanal | Mevcut |
| RTC | DS3231 | Mevcut |
| PZEM-004T | V3.0 | Mevcut |
| Güç kaynağı | Masaüstü, 5 V / 1,8 A | Mevcut |
| Test yükü | Lamba | Mevcut |

## SCT013 sensörleri

| Tür | Adet | Bağlantı |
|---|---:|---|
| SCT013 30 A / 1 V | 7 | Jack çıkışlı |
| SCT013 100 A / 1 V | 10 | Jack çıkışlı |
| **Toplam** | **17** | Jack yuvaları mevcut |

## Hazır analog arayüz

Kullanıcı daha önce 8 kanallı, her kanalı ayrı bias ve direnç ağına sahip bir kart hazırlamıştır. SCT013 sinyali jack yuvasından bu arayüze bağlanır ve bias uygulanmış sinyal ESP32 ADC girişinden okunur. İstenirse MCP serisi harici ADC de bağlanabilir.

Kullanıcı beyanına göre SCT013 aksesuarları, jack yuvaları ve bağlantı/ölçüm parçalarının tamamı mevcuttur.

## Bağlantı özeti

**SCT013 → jack yuvası → kanal başına ayrı bias/direnç ağı olan 8 kanallı kart → ESP32 ADC**

İsteğe bağlı olarak MCP ADC eklenebilir. MCP modeli, direnç değerleri, bias gerilimi ve kesin pin eşlemesi bu envanter görüşmesinde belirtilmedi; ayrıca teknik olarak belgelenebilir.

## Kapanış

**T001 — Fiziksel Donanım Envanteri tamamlandı.** Kullanıcı, listelenen donanımların tümünün elinde olduğunu ve eksik parça bulunmadığını bildirmiştir. Bu kayıt envanteri belgelendirir; elektriksel doğrulama raporu değildir.
