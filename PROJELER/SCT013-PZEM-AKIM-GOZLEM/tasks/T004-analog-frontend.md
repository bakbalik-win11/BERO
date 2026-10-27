# T004 — Analog ön uç

- **Durum:** PLANLANDI
- **Faz:** 1.1
- **Bağımlılık:** T002 ve T003
- **Hedef:** Gerçek SCT ve ADC bileşenlerine uygun analog ön ucu hesapla ve güvenli koşullarda doğrula.

## Yapılacak
1. hardware/frontend.md içinde gerçek SCT çıkış türünü, burden var/yok bilgisini, bias ve filtreyi kaydet. Bu aşamada harici ADC kullanılmayacak; MCP3208 sonraki aşamaya ayrılmıştır. ADC çözünürlüğü ve VREF kaydı bu görevin şartı değildir.
2. Tasarım hesabını kullanılan gerçek parçalar için yap; başka projeden direnç değeri kopyalama.
3. ADC giriş aralığı, beklenen maksimum sinyal ve clipping payını hesapla. Varsayımları ve parça toleranslarını yaz.
4. Fiziksel ölçüm gerekiyorsa güvenli düşük gerilim tarafında uygun cihazla ve yetkin inceleme altında yap; ölçülmeyen değerleri varsayımdan ayır.
5. En yüksek planlanan akım senaryosunda clipping kontrolünü yapmadan sonraki deneylere geçme.

## Kabul ölçütü
Hesap, gerçek bileşen kimlikleri ve ölçüm koşulları kayıtlıdır; giriş aralığı ve clipping koşulu kanıtla değerlendirilmiştir. Gerekli ölçüm yapılmadıysa görev doğrulanmış sayılmaz.

## Çıktı / dokunulacak dosyalar
- hardware/frontend.md
- İlgili donanım şeması/fotoğrafı

## Güvenlik
Belirsiz analog giriş veya izolasyon sorunu varken devreyi enerjilendirme.
