# PROJE BERO — EVENT_ID FAZ A KAYDI
Tarih: 2026-10-16

## Amaç
SSR ESP'nin ON/OFF durum geçişlerinde, diğer cihazların daha sonra kullanabileceği ortak bir olay kimliği üretmesi.

## Yapılan kod değişikliği
Dosya: `DONANIM/DS3231/examples/ds3231_ssr_40on_20off.yaml`

- Her açılışta `esp_random()` ile yeni `BOOT_ID` oluşturulur.
- `EVENT_ID` açılışta 0'dan başlar.
- SSR'nin ON ve OFF geçişlerinde EVENT_ID bir artırılır.
- Seri loga şu biçimde olay yazılır:
  `BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=N STATE=ON|OFF`
- Bu kimlik RTC saatinden bağımsızdır; RTC/DS3231 yazma hatası çözülmüş sayılmaz.
- Mevcut SSR çevrimi ve GPIO yapılandırması değiştirilmedi.

## Doğrulama durumu
- GitHub YAML değişikliği kaydedildi.
- Derleme yapılmadı; ESP'ye yüklenmedi; donanım üzerinde test edilmedi.
- Bu nedenle Faz A henüz çalışma zamanı açısından PASS değildir.
- `BOOT_ID` rastgele 32 bit değerdir; çakışma olasılığı düşüktür ama matematiksel olarak sıfır değildir.
- Bu aşamada olay yalnızca SSR ESP'nin loguna yazılır; PZEM'e gönderilmiyor.

## Devam adımı
1. YAML'ı ESPHome ile derle.
2. Cihazda en az bir ON ve bir OFF geçişini gözle.
3. Logdaki BOOT_ID'nin aynı açılış boyunca sabit, EVENT_ID'nin ardışık ve STATE'in ON/OFF olduğunu doğrula.
4. Ardından PZEM ESP'nin gerçek firmware dosyasını inceleyip iki cihaz arasında olay taşıma yöntemini seç. BERO deposunda PZEM kodu araması bu çalışma sırasında sonuç vermedi; mevcut kodun depo dışında olma ihtimali var.

## Kabul ölçütü
En az şu iki ardışık kaydın gerçek cihaz logunda görülmesi:
```
BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=1 STATE=ON
BERO_SHARED_EVENT BOOT_ID=XXXXXXXX EVENT_ID=2 STATE=OFF
```
Yukarıdaki satırlar örnektir; gerçek test çıktısı değildir.
