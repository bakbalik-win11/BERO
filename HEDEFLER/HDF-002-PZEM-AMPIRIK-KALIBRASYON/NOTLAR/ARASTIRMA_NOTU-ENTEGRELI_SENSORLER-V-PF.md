# HDF-002 — Araştırma Notu: Entegreli Sensörler ve Koşullu Etiketleme

**Kayıt tarihi:** 2026-10-12  
**Durum:** Fikir / araştırma yönü; henüz deney sonucu değil.  
**Bağlı hedef:** HDF-002 — Ölçüm Karakterini Öğrenmek ve Gerçek Hayatı Yakalamak

## Neden ayrı not olarak tutuluyor?

Bu düşüncenin ana hedef raporunu gereksiz yere büyütmeden kaybolmaması istenmiştir. Bu belge HDF-002'ye bağlı araştırma notudur; ana rapora yeni bir sonuç veya doğrulanmış yöntem eklemez.

## Fikir

SCT-013 gibi haricî akım trafolarından farklı olarak, bazı sensör/modüllerin içinde ölçüm sinyalini işleyen bir entegre bulunabilir. Entegrenin davranışı, içinde kullanıcı tarafından yazılmış bir yazılım bulunması şart olmadan, devre yapısı ve donanım/işleme mantığı tarafından belirlenebilir.

Bu nedenle araştırma yalnızca SCT-013 ile sınırlı kalmayabilir. Entegreli sensör/modüllerin çıktıları da deneysel olarak gözlenebilir ve aynı fiziksel koşulları tanımlayan referans etiketleriyle ilişkilendirilebilir.

## V, PF ve akım etiketleri

Uygun deneylerde ölçüm bölgesi için şu bağlam birlikte saklanabilir:

- Akım etiketi: `I`
- Gerilim: `V`
- Güç faktörü: `PF`
- Sensör/modül türü, kaynak kanal ve yük/deney koşulu
- Sensörün ham çıktısı ve varsa zaman/kayıt bilgisi

Böylece etiket yalnızca akım değerinden ibaret kalmaz; hangi elektriksel koşullarda gözlendiği de korunur. Benzer V/PF bölgelerinde sensör çıktılarının ve akımın ilişkisi ayrı ayrı incelenebilir.

## Sınırlar ve açık sorular

- V ve PF her sensörün doğrudan girdisi değildir; öncelikle deney koşulunu tanımlayan etiketler olarak düşünülür.
- Bir sensörün V veya PF değişimine duyarlı olup olmadığı varsayılmayacak, deneyle araştırılacaktır.
- Aynı V/PF değerleri tek başına aynı fiziksel olayın veya aynı yük türünün kanıtı değildir.
- Sabit bir `k` katsayısı veya belirli bir matematiksel model önceden kabul edilmeyecektir.
- SCT+MCP gibi ham örnekleme zincirleri ile içinde ölçüm/işleme entegresi bulunan modüllerin davranışları birbirinin aynısı kabul edilmeyecektir.
- Hangi entegreli sensörlerin inceleneceği ve hangi kayıt biçiminin kullanılacağı daha sonra mevcut donanım ve deney planına göre belirlenmelidir.

## Sonraki kullanım

HDF-002 kapsamında sensör/modül envanteri ve bağımsız ham veri toplama yolları incelenirken bu not yeniden ele alınabilir. Uygun bir cihaz seçilirse ayrı deney koşullarıyla sınanır; sonuçlar ham kayıtlar ve raporlarla desteklenmeden doğrulanmış kabul edilmez.
