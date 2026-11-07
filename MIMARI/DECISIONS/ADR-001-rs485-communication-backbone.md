# ADR-001 — BERO kalıcı haberleşme omurgası olarak RS485

- **Durum:** KABUL EDİLDİ
- **Tarih:** 2026-11-07
- **Karar sahibi:** Kullanıcı
- **Kapsam:** BERO genel haberleşme mimarisi

## Bağlam

BERO, farklı ölçüm kaynakları ve ESP tabanlı bölgesel düğümlerden oluşacak çoklu sensörlü bir gözlem sistemidir. Düğümler arasında kalıcı, kablolu bir haberleşme omurgası belirlenmesi gerekmektedir.

## Karar

1. **RS485, BERO'nun kalıcı haberleşme omurgasıdır.**
2. ESP tabanlı ölçüm düğümleri, ürettikleri ölçüm/veri kayıtlarını RS485 üzerinden bölgesel düğümlere aktaracak şekilde geliştirilecektir.
3. Wi-Fi şu aşamada geçici haberleşme/aktarımı için kullanılabilir; kalıcı BERO omurgası olarak kabul edilmez.
4. RS485 omurgası BERO'nun sensörden ve belirli bir ESP kartından bağımsız üst seviye mimari kararıdır.
5. PZEM-014 AC RS485 Modbus Güç Tüketim Ölçer + USB ile yapılacak çalışma, RS485 tabanlı haberleşmenin ilk uygulama alanlarından biridir. Cihaz henüz kullanılmamıştır; devreye alma ve gerçek haberleşme testi ileride yapılacaktır.
6. Ekranlı ESP'ler, ölçümlerin yerel/canlı görüntülenmesi için sistemin parçası olarak değerlendirilecektir. Kullanılacak ekran/kart modeli ve düğüm rolleri henüz kesinleştirilmemiştir.

## Katman ve protokol ayrımı

- **RS485**, fiziksel/elektriksel haberleşme katmanını ve çok noktalı kablolu omurga tercihinin kendisini tanımlar.
- **Modbus RTU**, PZEM-014 gibi cihazlarla RS485 üzerinden haberleşmek için kullanılabilecek protokoldür.
- PZEM-014 ile Modbus RTU haberleşmesi, BERO bölgesel düğümleri arasındaki uygulama mesajlaşma protokolünü kendiliğinden belirlemez.
- **Kablo yaklaşımı (kullanıcı kararı):** RS485 A/B diferansiyel haberleşmesi CAT kablo üzerinden taşınacaktır. Aynı kablo güzergâhında/altyapısında RS485 A/B hattının yanında aynı CAT kablo üzerinden **24 V DC ana besleme** de bölgesel düğüme taşınacaktır; düğüm noktasında DC-DC dönüştürücüyle **5 V DC** seviyesine indirilecektir. Bu RS485/besleme kablosu, mevcut Ethernet kablosundan dış kılıf rengiyle ayırt edilecektir.
- Kablo yaklaşımı belirlenmiş olsa da CAT kablonun kesin tipi/kategori ve damar eşlemesi, 24 V DC kaynağın kapasitesi, düğüm başına akım/güç, hat uzunluğu ve gerilim düşümü hesabı, yerel 24 V→5 V DC-DC dönüştürücü tipi, koruma/sigorta, topraklama/referans ve aşırı gerilim önlemleri henüz belirlenmemiştir.
- BERO düğümleri arası adresleme, mesaj çerçevesi, veri modeli, bus erişim yöntemi, baud hızı, terminasyon, bias ve hata/yeniden deneme davranışları bu ADR ile karara bağlanmamıştır.

## Kapsam dışı / henüz kararlaştırılmamış

Bu karar aşağıdakileri henüz belirlemez:
- Bölgesel düğüm sayısı, yerleşimi ve görev dağılımı.
- RS485 transceiver/modül modeli ve ESP pin eşlemesi.
- Modbus RTU'nun BERO düğümleri arası genel protokol olarak kullanılması.
- Wi-Fi'ın ne zaman ve hangi aşamada kaldırılacağı.
- Ekran modelleri, kullanıcı arayüzü ve canlı gösterim tasarımı.
- CAT kablonun kesin damar/pair tahsisi, 24 V DC ana beslemenin kapasitesi ve 24 V→5 V dönüştürücü tasarımı.
- Gerçek donanım bağlantısı, firmware, derleme, saha testi veya performans kabul ölçütleri.

## Uygulama ilkesi

Önce PZEM-014 üzerinden RS485/Modbus RTU okuma zinciri gerçek donanımda devreye alınabilir; ardından ESP düğümleri ve ekranlar aşamalı olarak entegre edilir. Her aşama gerçek bağlantı, çalışan kod ve log/çıktı ile ayrıca doğrulanır.

## Doğrulama sınırı

Bu kayıt bir **mimari/kablolama kararıdır**. CAT kablo üzerinden RS485 A/B ile 24 V DC ana beslemenin birlikte taşınması, beslemenin düğümde 5 V'a dönüştürülmesi ve kablonun Ethernet hattından dış kılıf rengiyle ayrılması kullanıcı tarafından belirlenmiştir. PZEM-014 henüz kullanılmamıştır. Hat kurulmamış; gerilim düşümü, besleme kapasitesi, koruma ve haberleşme performansı hesaplanıp test edilmemiştir. ESP düğümleri arası veri aktarımı denenmemiş, ekranlar devreye alınmamış ve firmware/derleme/fiziksel test yapılmamıştır.
