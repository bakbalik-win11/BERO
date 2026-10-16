# PROJE BERO — ESP32-WR1-PZEM UDP ALICI TESTİ
Tarih: 2026-10-16
ESPHome: 2026.9.1
PZEM ESP: 192.168.0.52
SSR ESP: 192.168.0.111
UDP port: 4210

## Sonuç: PASS
Kullanıcının paylaştığı OTA logu, PZEM firmware'inin derlenip yüklendiğini ve SSR olaylarının PZEM alıcısına ulaştığını doğruluyor.

Derleme zamanı: 2026-10-16 14:56:56 +0300.
PZEM UART: TX GPIO17, RX GPIO16, 9600 baud.
PZEM ölçüm sensörleri çalışıyor ve yaklaşık 5 saniyede bir ölçüm yayımlıyor.

## Gerçek UDP alım kanıtları
Aşağıdaki kayıtlar paylaşılan cihaz logundan alınmıştır:

```text
[15:01:31.995][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=22,STATE=OFF
[15:01:51.889][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=23,STATE=ON
[15:02:31.999][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=24,STATE=OFF
[15:02:51.995][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=25,STATE=ON
[15:03:31.988][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=26,STATE=OFF
[15:03:51.987][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=27,STATE=ON
[15:04:31.887][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=28,STATE=OFF
[15:04:51.987][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=29,STATE=ON
[15:05:31.885][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=30,STATE=OFF
[15:05:51.989][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=31,STATE=ON
[15:06:31.886][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=32,STATE=OFF
[15:06:51.988][I][bero_udp:171]: UDP_EVENT_RECEIVED from=192.168.0.111 payload=BERO_EVT,BOOT_ID=AF39B8E4,EVENT_ID=33,STATE=ON
```

BOOT_ID sabit kalıyor, EVENT_ID ilerliyor ve ON/OFF mesajları PZEM logunda görünüyor.

## PZEM ölçüm gözlemi
Logda gerilim yaklaşık 225.9–228.3 V; ON sırasında akım yaklaşık 0.052–0.053 A ve güç yaklaşık 7.7–7.9 W; OFF sırasında akım 0.000 A ve güç 0.00 W. Frekans yaklaşık 49.9–50.0 Hz. Bu değerler SSR olaylarıyla zamansal olarak örtüşüyor; tek başına ölçüm doğruluğu veya elektriksel güvenlik sertifikasyonu değildir.

## Açık işler
- UDP olayları alınıyor ancak henüz dosyaya/CSV'ye kaydedilmiyor.
- Mac Mini Python tarafında olay ve ölçüm loglarını birleştirme yapılacak.
- DS3231 I2C hatası ve SSR GPIO ON geri okuma uyumsuzluğu ayrı açık işlerdir.
- İlk aşamada SCT 1T/2T/4T ESP'lerine UDP olay dinleme eklenmeyecek.

## Devam noktası
Mac Mini üzerinde SSR olayları ve PZEM ölçümlerini zaman damgası/olay aralıklarıyla kaydedip Python ile eşleştirmek.
