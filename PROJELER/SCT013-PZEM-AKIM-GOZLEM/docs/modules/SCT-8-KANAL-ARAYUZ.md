# BERO Modülü — 8 Kanallı SCT Arayüz Düzeneği

**Modül kimliği:** BERO-SCT-8CH-001  
**Adı:** 8 Kanallı SCT Arayüz Düzeneği  
**Durum:** Kullanıcı tarafından bildirildi; bağlantı ve çalışma doğrulaması yapılmadı.

## 1. Kısa tanım

BERO kapsamında sekiz SCT bağlantı noktası bulunan ayrı bir analog arayüz düzeneği mevcuttur. Her dişi SCT bağlantısının kendine ait bias devresi vardır. Düzeneğe MCP tabanlı harici ADC de bağlanabilmektedir.

## 2. Kullanıcı tarafından bildirilen özellikler

- SCT bağlantı kapasitesi: 8 kanal.
- Her dişi bağlantı için ayrı bias.
- MCP harici ADC bağlantı imkânı.
- Bu düzenek, diğer SCT test modüllerinden ayrı bir donanım olarak ele alınacaktır.

## 3. Henüz tanımlanmayan ayrıntılar

Aşağıdaki bilgiler bu kısa modül kaydında bilinçli olarak açık bırakılmıştır:

- MCP'nin tam modeli ve kart üzerindeki bağlantısı.
- Her kanalın bias devresindeki bileşen değerleri ve şeması.
- Jack uçlarının pin dizilimi ve kanal eşlemesi.
- ADC referans gerilimi, besleme ve haberleşme bağlantıları.
- Sekiz kanalın eşzamanlı okunup okunmadığı.
- ESP modeli, GPIO eşlemesi ve firmware.

## 4. Kayıt sınırı

Bu belge yalnızca modülün varlığını ve kullanıcı tarafından bildirilen temel özelliklerini kaydeder. Devre şeması, pin bağlantısı, ölçüm performansı veya çalışır durum doğrulaması anlamına gelmez. Ayrıntılar, bu modülün incelenmesine geçildiğinde eklenecektir.
