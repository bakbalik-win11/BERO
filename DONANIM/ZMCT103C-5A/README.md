# ZMCT103C — 5 A tek fazlı AC akım sensörü

## Sensör türü ve model

ZMCT103C, primer iletkenin çekirdek deliğinden geçirildiği **akım çıkışlı bir akım transformatörüdür (CT)**. Hall sensörü değildir ve DC akım ölçemez. Sekonder akımı ADC'ye doğrudan bağlanmaz; uygun burden (yük) direnciyle gerilime çevrilmelidir.

## Üretici veri sayfası

- Üretici: Qingxian Zeming Langxi Electronic Devices / ZEMING
- [Üretici ürün sayfası ve PDF](https://www.micro-transformer.com/pcb-mounting-current-transformer-ZMCT103C.html)
- [ZMCT103C specification PDF](https://5nrorwxhmqqijik.leadongcdn.com/ZMCT103C%2Bspecification-aidirBqoKomRilSjpimnokp.pdf)
- [LCSC parça kaydı](https://www.lcsc.com/product-detail/Current-Transformers_ZMCT103C-AType_C94571.html)

## Temel özellikler

| Özellik | Üretici dokümanındaki bilgi |
|---|---|
| Model | ZMCT103C |
| Nominal primer akımı | 5 A |
| Nominal sekonder akımı | 5 mA @ 5 A primer |
| Sarım oranı | 1000:1 |
| Giriş aralığı | 0–10 A (50 Ω koşuluyla listelenmiş) |
| Faz hatası | ≤15 arcmin; 5 A ve 50 Ω koşulunda |
| Doğruluk sınıfı | 0.2 olarak listelenmiş |
| Doğrusallık | ≤0.2% (belirtilen test aralığında) |
| İzolasyon gerilimi | 4500 V olarak listelenmiş; test koşulları ayrıca doğrulanmalı |
| Çalışma sıcaklığı | −40…+85 °C |
| Yapı | Epoksi kaplı, PCB montajlı |

Bunlar çıplak CT için üretici değerleridir. OP07 op-amp, potansiyometre, direnç veya filtre içeren satıcı modüllerinin çıkış ölçeği farklı olabilir.

## Burden direnci hesabı

5 A primer akımda nominal sekonder akım 5 mA'dir.

| Burden | İdeal gerilim |
|---:|---:|
| 50 Ω | 0,25 V RMS |
| 100 Ω | 0,50 V RMS |
| 200 Ω | 1,00 V RMS |

Hesap: V = I × R. Üretici test koşulunda 50 Ω belirtir; daha büyük burden daha yüksek gerilim üretir ancak doğruluk ve çekirdek yükünü değiştirir.

**Sekonderi primer akım geçerken açık devre bırakma.** Burden bağlantısını enerjiyi keserek yap ve primer akım uygulamadan önce doğrula.

## Pin ve bağlantı

- Primer: ölçülecek tek iletken merkez delikten geçirilir.
- Sekonder: üretici çiziminde pin 1 ve 2 olarak gösterilir.
- AC çıkış negatif yarım dalga içerir; tek beslemeli ADC'ye doğrudan bağlanmamalıdır.
- ADC için burden, bias/orta nokta ve gerekiyorsa koruma/filtre tasarlanmalıdır.
- MCP3208 girişini AGND–VREF aralığında tut; VREF ≤ VDD olmalıdır.
- Faz ve nötrü birlikte delikten geçirmek akımları birbirine karşı iptal ettirebilir.

## BERO için test sırası

1. Elindeki ürünün çıplak CT mi yoksa op-amp'lı modül mü olduğunu belirle.
2. Enerji yokken sekonder ve burden bağlantısını doğrula.
3. Düşük, bilinen AC akımda burden üzerindeki RMS gerilimini ölç.
4. Bias ve ADC giriş aralığını doğrula; kırpılma olmadığını kontrol et.
5. Ham ADC örneklerini zaman damgasıyla kaydet, biası çıkar ve RMS hesapla.
6. Referans True-RMS ampermetreyle birden fazla noktada kalibrasyon yap.
7. Op-amp'lı modül çıkışına çıplak CT'nin 1000:1 oranını doğrudan uygulama; kart kazancını ölç.

## Kaynaklar

- [ZEMING üretici sayfası](https://www.micro-transformer.com/pcb-mounting-current-transformer-ZMCT103C.html)
- [Üretici datasheet PDF](https://5nrorwxhmqqijik.leadongcdn.com/ZMCT103C%2Bspecification-aidirBqoKomRilSjpimnokp.pdf)
- [LCSC ZMCT103C](https://www.lcsc.com/product-detail/Current-Transformers_ZMCT103C-AType_C94571.html)
- [Uraz Elektronik Türkiye ürün kaydı](https://www.urazelektronik.com/products/zmct103c-current-transformer-5a)
- [Burden ve CT ölçümü açıklaması](https://datacapturecontrol.com/articles/data-acquisition/measurements/current-overview)

**Doğrulama notu:** Gerçek BERO ürününün PCB şeması, burden değeri, op-amp kazancı ve çıkış ölçeği fiziksel olarak doğrulanmış değildir.