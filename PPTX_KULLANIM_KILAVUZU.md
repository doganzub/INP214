# PPTX İşleme Modülü - Kullanım Kılavuzu

## 📚 Genel Bakış

`pptx_processor.py` modülü, herhangi bir PowerPoint (`.pptx`) dosyasını analiz ederek:

1. ✅ **Metinleri** ayırır ve ayrı dosyalar halinde kaydeder
2. ✅ **Görselleri** (resimler, şekiller) çıkarır ve kaydeder  
3. ✅ **Her sayfanın yapısını** analiz eder ve detaylı rapor oluşturur
4. ✅ **Doğrulama** yapar - tüm sayfaların düzgün işlendiğini kontrol eder

---

## 🔧 Kurulum

### 1. Gerekli Kütüphaneleri Yükleyin

```bash
pip3 install python-pptx Pillow
```

**veya** `requirements.txt` kullanarak:

```bash
pip3 install -r requirements.txt
```

---

## 🚀 Kullanım

### Yöntem 1: Komut Satırından

```bash
python3 pptx_processor.py sunum.pptx
```

### Yöntem 2: Python Kodu İçinde

```python
from pptx_processor import PPTXProcessor

# PPTX dosyasını işle
processor = PPTXProcessor("Veri_Gorsellestirme.pptx")
processor.process()

# Tüm sayfaların doğru işlendiğini kontrol et
processor.verify_all_pages()
```

---

## 📂 Çıktı Yapısı

İşlem tamamlandığında şu dizin yapısı oluşur:

```
<dosya_adi>_output/
├── RAPOR.md                          # Detaylı işlem raporu
├── texts/                            # Tüm metinler
│   ├── slide_01_text.txt
│   ├── slide_02_text.txt
│   └── ...
└── images/                           # Tüm görseller
    ├── slide_01_image_01.png
    ├── slide_01_image_02.jpg
    ├── slide_02_image_01.png
    └── ...
```

---

## 📊 Örnek Kullanım: Ekran Görüntülerindeki PPTX

Paylaştığınız ekran görüntülerine göre bir PPTX dosyası için:

```bash
python3 pptx_processor.py "Veri_Gorsellestirme_ve_Python.pptx"
```

**Çıktı:**

```
############################################################
PPTX İŞLEME BAŞLADI: Veri_Gorsellestirme_ve_Python.pptx
############################################################
Toplam Sayfa Sayısı: 1
Çıktı Dizini: Veri_Gorsellestirme_ve_Python_output

============================================================
SAYFA 1 İŞLENİYOR...
============================================================
✓ Metin bulundu: Veri Görselleştirme ve Python...
✓ Metin bulundu: INP214 — Hafta 1: Veriden İçgörüye Giden Yol...
✓ Metin bulundu: csv...
✓ Metin bulundu: JetBrains Mono...
✓ Metin bulundu: Sayıları hikayelere dönüştürme sanatı...
✓ Görsel kaydedildi: slide_01_image_01.png
✓ Görsel kaydedildi: slide_01_image_02.png
✓ Görsel kaydedildi: slide_01_image_03.png
✓ Metinler kaydedildi: slide_01_text.txt

############################################################
İŞLEM TAMAMLANDI!
############################################################
✓ Tüm sayfalar işlendi: 1 sayfa
✓ Metinler kaydedildi: Veri_Gorsellestirme_ve_Python_output/texts
✓ Görseller kaydedildi: Veri_Gorsellestirme_ve_Python_output/images
✓ Rapor oluşturuldu: Veri_Gorsellestirme_ve_Python_output/RAPOR.md

============================================================
DOĞRULAMA YAPILIYOR...
============================================================

📊 DOĞRULAMA SONUÇLARI:
   - Toplam Sayfa: 1
   - İşlenen Metin Dosyası: 1
   - İşlenen Görsel: 3
   ✅ Metinler başarıyla işlendi
   ✅ Görseller başarıyla işlendi

📄 SAYFA DETAYLARI:
   Sayfa  1: Metin [✓]  Görsel [3 adet]

============================================================
DOĞRULAMA TAMAMLANDI
============================================================
```

---

## 📝 Metin Dosyası Örneği

`slide_01_text.txt` içeriği:

```markdown
# SAYFA 1

## Metin Bloğu 1
Veri Görselleştirme ve Python

## Metin Bloğu 2
INP214 — Hafta 1: Veriden İçgörüye Giden Yol

## Metin Bloğu 3
csv
120.5, 45.2, 78.9, 10.1\n98.3...

## Metin Bloğu 4
JetBrains Mono
Sayıları hikayelere dönüştürme sanatı.

## Metin Bloğu 5
NotebookLM
```

---

## 🎯 Özellikler

### ✅ Yapabilecekleri

- **Tüm metin içeriğini** çıkarır (başlıklar, alt başlıklar, gövde metni)
- **Tüm görselleri** (PNG, JPG, JPEG formatında) kaydeder
- **Her sayfa için ayrı** metin ve görsel dosyaları oluşturur
- **Detaylı rapor** (Markdown formatında) üretir
- **Otomatik doğrulama** ile tüm sayfaların düzgün işlendiğini kontrol eder

### ⚠️ Sınırlamalar

- Animasyonları ve geçişleri işleyemez
- Video ve ses dosyalarını çıkaramaz
- Şekil ve diyagramların içindeki gömülü metinleri kısmen çıkarabilir
- Karmaşık tablo yapılarını düz metin olarak çıkarır

---

## 🛠️ İleri Seviye Kullanım

### Sadece Belirli Sayfaları İşlemek

```python
from pptx_processor import PPTXProcessor

processor = PPTXProcessor("sunum.pptx")

# Sadece 3. sayfayı işle
processor.process_slide(processor.prs.slides[2], 3)
```

### Kendi Rapor Formatınızı Oluşturmak

```python
class MyCustomProcessor(PPTXProcessor):
    def save_report(self):
        # Özel rapor formatı
        report_path = self.output_dir / "OZEL_RAPOR.html"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("<html><body>")
            f.write("<h1>İşlem Raporu</h1>")
            for line in self.report:
                f.write(f"<p>{line}</p>")
            f.write("</body></html>")
```

---

## 🐛 Hata Ayıklama

### Hata: "No module named 'pptx'"

**Çözüm:**
```bash
pip3 install python-pptx
```

### Hata: "No module named 'PIL'"

**Çözüm:**
```bash
pip3 install Pillow
```

### Hata: "FileNotFoundError"

**Çözüm:** PPTX dosyasının yolunu kontrol edin:
```python
import os
print(os.path.exists("sunum.pptx"))  # True olmalı
```

---

## 📧 Destek

Herhangi bir sorun veya öneriniz için:
- Modül dosyasını inceleyin: `pptx_processor.py`
- Kod içindeki docstring'leri okuyun
- Örnek kullanımları deneyin

---

## 📌 Notlar

1. **Büyük PPTX dosyaları** uzun süre işlem alabilir
2. **Görsel kalitesi** orijinal dosyadaki kalite ile aynıdır
3. **Türkçe karakterler** UTF-8 encoding ile düzgün işlenir
4. **Rapor dosyası** (RAPOR.md) Markdown ile uyumludur

---

## ✨ Örnek Proje Akışı

```bash
# 1. PPTX dosyasını işle
python3 pptx_processor.py ders_sunumu.pptx

# 2. Çıktı dizinini kontrol et
ls ders_sunumu_output/

# 3. Metinleri oku
cat ders_sunumu_output/texts/slide_01_text.txt

# 4. Görselleri görüntüle
open ders_sunumu_output/images/

# 5. Raporu incele
cat ders_sunumu_output/RAPOR.md
```

---

**🎉 Başarılı işlemler!**
