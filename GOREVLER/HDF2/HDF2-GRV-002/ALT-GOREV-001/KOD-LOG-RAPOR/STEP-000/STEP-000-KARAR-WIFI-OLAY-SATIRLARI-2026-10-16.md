# STEP-000 — Wi-Fi Olay Satırlarının Veri Akışına Eklenmesi

**Tarih:** 2026-10-16  
**Aşama:** Tasarım kararı — henüz donanım testiyle doğrulanmadı  
**Kapsam:** HDF2-GRV-002 / ALT-GOREV-001 / STEP-000

## 1. Karar

Ölçüm ESP'lerinin sürekli veri akışına, ihtiyaç duyulduğunda kullanılabilecek kısa ve açıkça etiketlenmiş olay satırları eklenmesi denenecek. İlk hedef, SSR'nin ON/OFF durum değişikliklerini ölçüm kayıtlarıyla aynı dosyada görünür kılmak.

Örnek kayıt:

```text
DATA,SEQ=1001,...
DATA,SEQ=1002,...
EVENT,SSR,ID=19,STATE=ON
DATA,SEQ=1003,...
DATA,SEQ=1004,...
EVENT,SSR,ID=20,STATE=OFF
```

Bu örnek yalnızca önerilen kayıt biçimini gösterir; mevcut firmware'in bu biçimi ürettiği anlamına gelmez.

## 2. Neden?

- Ölçüm verisi sürekli akarken SSR gibi başka bir ESP'den gelen durum bilgisi de kayıtlarda görünür olsun.
- Olay bilgisi, ölçüm verisinin içine anlamsal olarak karıştırılmasın; ayrı bir `EVENT` etiketiyle ayırt edilsin.
- Sonradan Python ile analiz yapılırken olay satırları kullanılabilsin veya filtrelenebilsin.
- İlk aşamada kusursuz zaman senkronizasyonu beklemeden, olayların kayıtta görünür olması sağlansın.
- Donanım ve yazılım karmaşıklığı artırılmadan önce basit bir yöntem denenmiş olsun.

## 3. Çalışma ilkeleri

1. **Örnekleme önceliklidir.** Olay mesajını beklemek için ADC örneklemesi durdurulmayacak.
2. **Ağ işlemi örneklemeden bağımsız tutulacaktır.** Wi-Fi alma/gönderme işi örnekleme döngüsünü bloke etmemeli.
3. **Olaylar etiketli olacaktır.** Önerilen başlangıç biçimi: `EVENT,SSR,ID=<event_id>,STATE=<ON|OFF>`.
4. **Sıra ve zaman bilgisi korunacaktır.** Mümkün olduğunda veri paketlerinde örnek sıra numarası, olaylarda olay kimliği ve alım zaman damgası tutulacak.
5. **Veri kaybı izlenecektir.** Tampon taşması, eksik paket veya sıra numarası atlaması kontrol edilecek.
6. **ESP'ler birbirlerinin Wi-Fi mesajlarını kendiliğinden okuyamaz.** Gönderici ve alıcı protokolü açıkça tanımlanmalı; ölçüm ESP'si olay mesajını alacak şekilde yapılandırılmalıdır.

## 4. Beklenen kayıt yaklaşımı

Ölçüm ESP'si örnekleri toplamaya devam eder. Olay bilgisini gönderen ESP, SSR durum değişikliğini kısa bir mesajla yayınlar. Ölçüm ESP'si bu mesajı alıp veri akışına olay satırı olarak ekleyebilir. Böylece Mac tarafında birleştirme yapılması şart olmadan, tek bir akış içinde DATA ve EVENT kayıtları görülebilir.

Bu yaklaşımın uygulanması, mevcut ESP'lerin veri aktarım protokolü ve paket biçimi incelendikten sonra yapılacaktır. Eğer olay satırını doğrudan ölçüm ESP'sine eklemek örneklemeyi bloke edecekse, olayların Mac'te birleştirilmesi yedek yöntem olarak tutulacaktır.

## 5. Risk ve sınırlar

- Tek bir kısa Wi-Fi mesajının etkisi küçük olabilir; ancak etkisinin sıfır olduğu varsayılmayacaktır.
- Ağ işlemi veya metin oluşturma örnekleme yolunda çalışırsa örnek aralığını bozabilir ya da örnek kaybına yol açabilir.
- Olayın akıştaki komşu DATA satırlarının arasına yazılması, tek başına o olayın tam olarak o örnekte gerçekleştiğini kanıtlamaz. Zaman ilişkisi için zaman damgası ve/veya örnek sıra numarası gerekir.
- Wi-Fi gecikmesi nedeniyle olay, gerçekleştiği andan daha sonra kayda ulaşabilir.
- Bu karar şu an için tasarım denemesidir; henüz performans sonucu veya PASS kararı yoktur.

## 6. Doğrulama planı

1. Olay mesajı kapalıyken ölçüm örnek sayısını ve örnekleme aralıklarını kaydet.
2. Aynı ölçümü olay mesajları açıkken tekrarla.
3. İki koşulda örnek sayısını, sıra numarası atlamalarını, tampon taşmasını ve örnekleme aralığı dağılımını karşılaştır.
4. SSR ON/OFF olaylarının kayıt dosyasında doğru etiketle ve doğru olay kimliğiyle göründüğünü doğrula.
5. Sonuçları ham log ve Python raporuyla belgeleyerek etkisinin kabul edilebilir olup olmadığına karar ver.

## 7. STEP-000 çıkış kriteri

- DATA ve EVENT kayıtlarının birbirinden ayırt edilebilmesi.
- Olay mesajı alınırken ölçüm örneklemesinin durmadığının testle gösterilmesi.
- Veri kaybı ve zamanlama etkisinin ölçülüp raporlanması.
- Başarılı testten sonra gerçek paket biçimi ve ilgili ESP kodlarının depoda güncellenmesi.

**Mevcut durum:** Karar ve gerekçesi belgelendi. Firmware değişikliği yapılmadı; test çalıştırılmadı.
