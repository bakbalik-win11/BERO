# STEP-005 — En yüksek güvenilir örnekleme hızını belirleme

**Durum:** BEKLİYOR

- Başlangıç hızından ilerleyerek ölçüm hızını kontrollü biçimde artır.
- Her basamakta gerçek örnek sayısı, zamanlama kanıtı, frame bütünlüğü ve overflow sayaçlarını kaydet.
- Callback süresini tek başına ADC örnek aralığının kanıtı sayma.
- Dalga biçimi yeterli ayrıntıda ve kayıpsız gösterilemiyorsa daha düşük güvenilir hızı seç.

Başarı kanıtı: hız karşılaştırma tablosu, ham kayıtlar ve açıkça belirtilmiş ölçüm yöntemi.


# STEP-005 — En yüksek güvenilir örnekleme hızını belirleme

**Durum:** BEKLİYOR

## Amaç
Veri bütünlüğü ve gerçek örnekleme zamanlaması kanıtlarıyla güvenilir hızı belirlemek.

## Planlanan işler
1. Başlangıç hızından kontrollü biçimde ilerle.
2. Her hızda örnek sayısı, süre ölçümünün neyi temsil ettiği, frame kaybı ve overflow sayaçlarını kaydet.
3. Callback sürelerini tek başına örnekleme aralığının kanıtı sayma.
4. Karşılaştırma tablosu çıkar ve güvenilir üst hızı belirle.

## Tamamlanan işler
- Henüz tamamlanan iş kaydedilmedi.

## Kapanış ölçütü
Ham kayıtlarla desteklenen hız karşılaştırması ve seçilen güvenilir hız raporlanmış.

## Çalışma kaydı
Her tamamlanan işin tarihi, kullanılan kod sürümü, test sonucu ve kanıt bağlantısı aşağıya alt alta eklenecek. Step ancak kapanış ölçütü kanıtlandığında kapatılacak.

