# PROJE BERO — GRV-Freeze-1 / GRV-008.2 Akşam Test Raporu

**Tarih:** 2026-10-13  
**Durum:** TESTE HAZIRLIK ADAYI — derleme ve fiziksel test sonucu henüz yok.  
**Kod durumu:** Aday kod hazırlandı; derleme onayı gelmeden `KOD` klasörüne taşınmayacak. Önceki deneyler değiştirilmedi.

## 1. Amaç
ESP32-WROOM → Mac Mini → Python → grafik hattından ilk gerçek ham SCT/BIAS verisini almak. MCP3208 kullanılmayacak. GPIO34 / ADC1_CH6 SCT adayı, GPIO35 / ADC1_CH7 BIAS adayıdır; fiziksel kablolama teyidi beklenir.

- Her kanal için hedef: 10 kHz.
- Her frame: 1.000 SCT + 1.000 BIAS örneği.
- Hedef frame süresi: yaklaşık 100.000 µs.
- Ham ADC verisi korunur. Bu aşamada RMS, BIAS çıkarma, filtreleme, kalibrasyon veya akım hesabı yoktur.
- 1T/2T/4T eşzamanlama bu testin dışındadır.

## 2. GRV-Freeze-1 kararı
Mimariye yeni özellik eklemeyi durdurup ilk gerçek kayda geçiyoruz. Freeze, doğrulama anlamına gelmez: kod derlemesi, sürücü API uyumu, örnekleme zamanlaması, frame bütünlüğü ve taşma sayaçları gerçek cihazda sınanmalıdır.

## 3. Önemli protokol düzeltmesi
Binary frame biçimi: 9 adet uint32 başlık (36 bayt) + 2.000 adet uint16 örnek (4.000 bayt) + uint32 bitiş marker'ı (4 bayt) = **4.040 bayt**. Python biçim dizgesi bitiş marker'ını da içermelidir:

```python
FRAME_FORMAT = f"<IIIIIIIII{SAMPLE_COUNT * 2}HI"
FRAME_SIZE = struct.calcsize(FRAME_FORMAT)  # 4040 bytes
```

Paketin son dört baytı `0xCAFEBABE` marker'ı olarak doğrulanır; örnek verisinin son dört baytı marker sanılmaz. Seri okuma sınırında başlangıç marker'ı bölünebileceğinden, marker bulunamazsa akışın son 3 baytı korunur.

## 4. ESP32 aday kodunda sahiplik ilkesi
Aday C++ kodu ayrı ham DMA tampon havuzu, ham tampon serbest/hazır kuyrukları, frame serbest/hazır kuyrukları ve USB aktarımı tamamlanınca frame'i serbest bırakma yaklaşımını kullanır. Tek bir ortak ISR tamponu kullanılmamalıdır. Kanal numarası kontrol edilerek CH6 ve CH7 eşleştirilir; örnek indeksi yalnızca iki kanal değeri de hazır olduğunda ilerletilir.

DMA bloğu 100 çift örnek içerir; 10 blok bir frame oluşturur. Böylece frame başlangıç/bitiş callback zamanları aynı callback'e düşmez. Yine de bu süre örnek başına 100 µs aralığını kanıtlamaz; yalnızca kaba frame-süresi kontrolüdür.

## 5. TEST-001 — sensör bağlı, yük yok
100 frame alınır. Kaydedilecekler:
- Geçerli frame sayısı, frame ID ve marker doğrulaması
- Frame süresi (hedef yaklaşık 100.000 µs)
- İlk frame BIAS ham ADC ortalaması ve standart sapması
- DMA overflow, raw queue overflow, frame queue overflow sayaçları
- Ham CSV ve ilk beş frame grafiği

## 6. TEST-002 — 100 W lamba
Güvenli ve uygun bağlantıyla 100 W lamba açıkken 100 frame alınır. Ham SCT/BIAS dalgası, peak ve peak-to-peak gözlemlenebilir. Bunlar kalibre akım sonucu değildir. Gerçek kayıt olmadan PASS denmez.

## 7. TEST-003 — aç/kapat
100 W lamba kayıt penceresi içinde açılıp kapatılır. Mevcut Python betiği 100 frame alır; geçiş bu pencere içinde yapılmalıdır. Tepki süresi, örnekleme zaman ekseni doğrulanmadan kesin metrik sayılmaz.

## 8. Mac Mini
Kurulum:
```bash
python3 -m pip install pyserial numpy matplotlib
python3 grv008_test_receiver.py
```
Python dosyasındaki `SERIAL_PORT` gerçek seri porta ayarlanmalıdır. Yer tutucu: `/dev/cu.usbserial-REPLACE_ME`. ESP seri portundan debug metni gönderilmemelidir; binary akış bozulur.

Python betiği `grv008_capture/grv008_raw_samples.csv` ve `grv008_capture/first_five_frames.png` üretir. Grafik ham ADC count değerlerini gösterir; filtreleme veya kalibrasyon yapmaz.

## 9. Test durumu

| Kontrol | Durum |
|---|---|
| Derleme | Bekliyor |
| ESP32'ye yükleme | Bekliyor |
| TEST-001 / 100 frame | Bekliyor |
| Frame süresi | Gerçek ölçüm bekliyor |
| BIAS ortalama / std | Gerçek ölçüm bekliyor |
| Taşma sayaçları | Gerçek ölçüm bekliyor |
| CSV / ilk beş grafik | Gerçek test bekliyor |

## 10. Kod dosyaları
Bu raporla birlikte hazırlanan tam aday dosyalar:
- `GRV-008.2_candidate.ino` — ESP32-WROOM Arduino/ADC continuous binary motor
- `grv008_test_receiver.py` — Mac Mini binary alıcı, frame doğrulama, CSV ve ilk beş frame grafiği

Bu iki dosya bu raporun yerel ekleri olarak verilir. Test/derleme onayı öncesinde repo `KOD` alanına eklenmez.

**Kayıt ilkesi:** Bu bir hazırlık raporudur, PASS raporu değildir. Gerçek test sonuçları yeni ve tarihli rapora yazılacak; geçmiş deneylerin üzerine yazılmayacaktır.
