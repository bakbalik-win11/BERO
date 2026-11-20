# BERO Depo Bütünlüğü — Haftalık Kontrol Prosedürü

## Amaç
BERO GitHub deposunun dosya bütünlüğünü, yapısal tutarlılığını, dokümantasyon bağlantılarını ve proje kayıtlarının izlenebilirliğini düzenli olarak kontrol etmek.

**Sıklık:** Haftada bir kez. Ayrıca büyük klasör taşıma/yeniden adlandırma, çok sayıda dosya güncellemesi veya önemli mimari değişiklik sonrasında ek kontrol yapılır.

**Kapsam:** Depodaki bütün projeler ve ortak dokümantasyon. Kontrol yalnızca SCT013-PZEM projesiyle sınırlı değildir.

## Kontrol sırası

### 1. Git ve depo durumu
- [ ] Yerel çalışma kopyası doğru BERO deposuna ve beklenen uzak depoya bağlı.
- [ ] Güncel ana dal değişiklikleri çekildi; senkronizasyon hatası yok.
- [ ] `git status --short` çıktısı incelendi; açıklanamayan yerel değişiklik yok.
- [ ] `git diff --check` boş; boşluk/çatışma işaretçisi kaynaklı sorun yok.
- [ ] `git fsck --full` tamamlandı; bozuk veya erişilemeyen Git nesnesi raporlanmadı.
- [ ] Son commit ve uzak dalın durumu kaydedildi.

### 2. Dosya ve klasör yapısı
- [ ] Proje klasörleri beklenen yerde; kritik README, STATUS, ROADMAP, AGENTS ve indeks dosyaları mevcut.
- [ ] Boş kalması tasarlanan klasörlerdeki `.gitkeep` dosyaları korunuyor.
- [ ] Yanlış yere kaydedilmiş, yinelenmiş veya sahipsiz dosyalar kontrol edildi.
- [ ] RAW veri, firmware, analiz çıktısı ve raporlar kendi amaçlanan klasörlerinde.

### 3. Dokümantasyon ve çapraz bağlantılar
- [ ] README ve indekslerdeki yerel dosya bağlantıları hedef dosyaya ulaşıyor.
- [ ] STATUS, ROADMAP, PROGRESS_TREE ve görev/deney kayıtları birbiriyle çelişmiyor.
- [ ] Modül adları, numaraları ve klasör yolları tutarlı.
- [ ] Kapanmış, ertelenmiş veya yapılmadan kapatılmış işler yanlışlıkla aktif/tamamlandı gösterilmiyor.
- [ ] Teknik iddialar kanıt türüyle uyumlu; kullanıcı bildirimi, ölçüm, üretici belgesi, hesap ve hipotez ayrımı korunuyor.

### 4. Kod, yapılandırma ve deney kayıtları
- [ ] YAML/kod dosyalarının ilişkili donanım ve cihaz kimlikleri korunuyor.
- [ ] Başarılı olduğu belirtilen kod için gerçek derleme/çalışma logu veya doğrulama kanıtı bulunuyor.
- [ ] Deney sonuçları, ham veri kaynakları ve analiz dosyaları arasında izlenebilir bağlantı var.
- [ ] Ham veri üzerine yazılmamış; türetilmiş veriler ayrı tutulmuş.
- [ ] Gizli anahtar, parola, token veya kişisel erişim bilgisi yanlışlıkla depoya eklenmemiş.

### 5. GitHub ve otomasyon
- [ ] Son haftadaki commit'ler ve değişiklikler gözden geçirildi.
- [ ] Etkin GitHub Actions iş akışlarının son çalışmaları incelendi; başarısız işler açıklanmış.
- [ ] Kullanılmayan, kırık veya artık geçerli olmayan iş akışı/bağlantı bulunup bulunmadığı değerlendirildi.

## Sonuç sınıflandırması

- **TEMİZ:** Kontrol maddeleri tamamlandı; kritik bütünlük sorunu bulunmadı.
- **UYARILI:** Depo kullanılabilir; ancak açıklanmış ve takip gerektiren eksikler var.
- **BAŞARISIZ:** Bozuk dosya/nesne, kritik eksik, çözülemeyen bağlantı veya kayıt çelişkisi var. Sorun giderilmeden temiz sonucu verilmez.
- **KISMİ:** Kontrolün bazı bölümleri erişim veya zaman nedeniyle yapılamadı. Kontrol tamamlandı gibi gösterilmez.

## Haftalık kontrol raporu

Her kontrol için `docs/integrity/YYYY-MM-DD.md` dosyası oluşturulur. Rapor en az şu bilgileri içerir:

- Kontrol tarihi ve kontrolü yapan kişi/araç.
- İncelenen dal ve HEAD commit SHA.
- Kullanılan komutlar ve gerçek çıktılar (özellikle `git status --short`, `git diff --check`, `git fsck --full`).
- Kontrol edilen klasörler, indeksler ve bağlantılar.
- Bulunan sorunlar; önem derecesi, ilgili dosya ve düzeltme durumu.
- Sonuç sınıfı: TEMİZ / UYARILI / BAŞARISIZ / KISMİ.
- Sonraki kontrol tarihi veya açık takip işi.

**Kural:** Komut çalıştırılmadıysa başarılı olarak yazılmaz. Yalnızca GitHub web görünümüne bakmak, yerel Git nesne bütünlüğünün `git fsck` ile kontrol edildiği anlamına gelmez.

## Rapor şablonu

```markdown
# BERO Haftalık Depo Bütünlüğü — YYYY-MM-DD

- Dal:
- HEAD commit:
- Kontrol kapsamı:
- Sonuç: TEMİZ / UYARILI / BAŞARISIZ / KISMİ

## Komut kontrolleri
- git status --short:
- git diff --check:
- git fsck --full:
- GitHub Actions:

## Yapısal ve dokümantasyon kontrolleri
- Kritik dosyalar:
- Yerel bağlantılar:
- İndeks/durum tutarlılığı:
- RAW veri ve kayıt izlenebilirliği:

## Bulgular
- Yok / bulguları ve önem dereceleri

## Düzeltmeler ve açık işler
- 

## Sonraki kontrol
- YYYY-MM-DD
```
