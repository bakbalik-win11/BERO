# FNIRSI 2D15P – Bağımsız Osiloskop Öğrenme

- Başlangıç tarihi: 2026-11-22
- Çalışma biçimi: Geceleri yaklaşık 20 dakika
- Durum: Öğrenme alanı açıldı; ilk ders henüz uygulanmadı.
- Kapsam: BERO teknik testlerinden ve veri analizi öğreniminden ayrı, cihaz kullanım eğitimi.

## Amaç

FNIRSI 2D15P osiloskopu sıfırdan öğrenmek. İlk aşamada cihazın kendi sinyal jeneratörünü kullanarak dalga biçimini ekranda göstermek; VOLTS/DIV, TIME/DIV ve TRIGGER ayarlarını anlamak; daha sonra genlik, periyot, frekans ve duty cycle okumayı öğrenmek.

Bu çalışma ticari ölçüm cihazı geliştirme veya laboratuvar kalibrasyonu değildir. Amaç cihazı temel düzeyde güvenli ve bilinçli kullanabilmektir.

## Kullanılacak ekipman

| Ekipman | Rol |
|---|---|
| FNIRSI 2D15P | Osiloskop ve ilk aşamada dahili sinyal jeneratörü |
| Cihazla gelen prob | CH1 üzerinden sinyal görüntüleme |
| SANEC NE555 kare dalga jeneratörü | İlerleyen derslerde harici kaynak olarak karşılaştırma |

İlk derslerde yalnızca FNIRSI'nin kendi jeneratörü kullanılacak. NE555 sonraya bırakıldı.

## Cihaz için başlangıç bilgileri

FNIRSI 2D15P üretici sayfasında listelenen başlıca özellikler:
- İki kanallı osiloskop.
- Tek kanal kullanımında 100 MHz bant genişliği.
- 500 MSa/s örnekleme hızı.
- Dikey ölçek: 10 mV/div – 10 V/div.
- Zaman tabanı: 5 ns/div – 50 s/div.
- Dahili DDS jeneratörü: 0–10 MHz.
- Jeneratör genliği: 0,1–3,0 Vpp.
- Duty cycle ayarı.

Üretici sayfası: https://www.fnirsi.com/products/2d15p

10 mV/div, en hassas dikey ölçek kademesidir; ölçülebilecek en küçük sinyalin mutlak alt sınırı değildir. Prob fiziksel olarak x1/x10 konumuna sahipse cihaz menüsündeki prob oranı da aynı seçilmelidir.

## 20 dakikalık oturum yöntemi

| Süre | İçerik |
|---:|---|
| 0–3 dk | Önceki dersin tekrarı ve bağlantı kontrolü |
| 3–8 dk | Tek yeni kavram veya ayar |
| 8–15 dk | Dahili jeneratörle uygulama |
| 15–18 dk | Ekrandaki sinyali okuma |
| 18–20 dk | Fotoğraf ve oturum notu |

Bir konu anlaşılmadan yenisine geçilmez. Gerekirse aynı ders tekrarlanır.

## Ders sırası

1. Ekran, eksenler, dalga biçimi ve sıfır seviyesi.
2. Dahili jeneratörle 1 kHz kare dalga.
3. VOLTS/DIV ve sinyal genliği.
4. TIME/DIV, periyot ve frekans.
5. TRIGGER ve görüntüyü sabitleme.
6. Vpp ve Vrms.
7. Kare, sinüs ve üçgen dalga karşılaştırması.
8. Duty cycle ve DC offset.
9. Prob x1/x10 ve AC/DC coupling.
10. Otomatik ölçümler ve cursor.
11. Gürültü ve dalga biçimi kararlılığı.
12. İki kanal kullanımı.
13. SANEC NE555 harici jeneratörü.
14. İsteğe bağlı SCT013 gözlemi (eğitim uygulaması; BERO görevi değildir).

## Güvenlik sınırı

İlk dersler yalnızca osiloskopun kendi düşük gerilimli jeneratörüyle yapılacaktır. İlk bağlantıdan önce prob tipi, jeneratör çıkışı ve cihaz üzerindeki soketler birlikte kontrol edilecektir.

Osiloskopun pilde çalışması, şebeke ölçümünde girişlerinin güvenli veya izole olduğu anlamına gelmez. Prob GND klipsi şebeke fazına, nötrüne veya şebekeye bağlı devreye bağlanmayacaktır. Bu eğitimde şebeke ölçümü yapılmayacaktır.

## Kayıtlar

- İlk ders: `DERS-001-ILK-KARE-DALGA.md`
- Her gece için: `OTURUM-LOG.md`

Yapılmamış ders tamamlandı olarak işaretlenmez. Fotoğraf/log, ancak gerçekten uygulandıktan sonra kaydedilir.

## BERO'dan ayrım

Bu klasör bağımsız öğrenme içindir. BERO'nun PREBERO görevlerini, kalibrasyon kararlarını veya firmware'ini değiştirmez. Öğrenme sırasında elde edilen bir gözlem BERO için teknik kanıt niteliğindeyse ayrıca ilgili BERO görevinin altında kaydedilir.
