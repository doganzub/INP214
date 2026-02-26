# Hafta 1: Veri Görselleştirme (Data Visualization)

> **AI-Dostu Açıklama:** Bu klasör, INP214 dersi Hafta 1 için veri görselleştirme materyallerini içerir. İki farklı veri seti (insurance.csv ve tips.csv) üzerinden ders anlatımı, tam çözümlü cevap notebooku ve öğrenci ödev notebooku bulunmaktadır.

---

## Dosya Yapısı ve Açıklamaları

### Veri Setleri

| Dosya | Satır | Sütun | Açıklama |
|-------|-------|-------|----------|
| `insurance.csv` | 1338 | 7 | Sigorta müşteri verisi (orijinal ders veri seti) |
| `tips.csv` | 244 | 7 | Restoran bahşiş verisi (ödev veri seti) |

**insurance.csv Sütunları:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`
- Türkçeleştirme: `age`→`yas`, `sex`→`cinsiyet`, `bmi`→`vki`, `children`→`cocukSayisi`, `smoker`→`sigaraDurum`, `region`→`bolge`, `charges`→`odemeMiktari`

**tips.csv Sütunları:** `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size`
- Türkçeleştirme: `total_bill`→`toplamHesap`, `tip`→`bahsis`, `sex`→`cinsiyet`, `smoker`→`sigaraDurum`, `day`→`gun`, `time`→`ogun`, `size`→`kisiSayisi`
- Kategorik değer çevirileri: `Male`→`erkek`, `Female`→`kadin`, `Yes`→`evet`, `No`→`hayir`, `Sun`→`pazar`, `Sat`→`cumartesi`, `Thur`→`persembe`, `Fri`→`cuma`, `Lunch`→`ogle`, `Dinner`→`aksam`

---

### Notebooklar

| Dosya | Tür | Veri Seti | Açıklama |
|-------|-----|-----------|----------|
| `1_veri_gorsellestirme.ipynb` | **Ders (Öğretim)** | `insurance.csv` | Orijinal ders notebooku. Tüm kodlar, açıklamalar ve grafikler insurance.csv üzerinden anlatılır. Öğretmenin ders sırasında kullandığı referans dosyadır. |
| `1A_veri_gorsellestirme..ipynb` | **Cevap (Answer)** | `tips.csv` | Tam çözümlü cevap notebooku. `1_veri_gorsellestirme.ipynb` ile aynı yapıyı takip eder ancak tips.csv veri seti üzerinden tüm kodlar, yorumlar ve grafikler uyarlanmıştır. Öğrencilerin ödevlerini kontrol etmek için kullanılır. |
| `1Q_veri_gorsellestirme.ipynb` | **Ödev (Question)** | `tips.csv` | Öğrenci ödev notebooku. `1A_veri_gorsellestirme..ipynb` ile aynı yapıda ancak kod hücreleri boşaltılmış, yorum satırları olarak ne yazılması gerektiği açıklanmıştır. Kütüphane import hücresi korunmuştur. Öğrenciler yorum satırlarını açarak/yazarak ödevi tamamlar. |

---

### Notebook İlişki Şeması

```
1_veri_gorsellestirme.ipynb  (DERS - insurance.csv ile)
        │
        ▼  (aynı yapı, tips.csv'ye uyarlanmış)
1A_veri_gorsellestirme..ipynb  (CEVAP - tips.csv ile, tam çözüm)
        │
        ▼  (kodlar kaldırılmış, yorum satırı olarak ipucu verilmiş)
1Q_veri_gorsellestirme.ipynb  (ÖDEV - tips.csv ile, boş kodlar)
```

---

## Notebook İçerik Yapısı (Ortak Bölümler)

Her üç notebook da aşağıdaki bölüm sırasını takip eder:

1. **1.1 Kütüphane Yükleme** — numpy, pandas, matplotlib, seaborn, sklearn, yellowbrick
2. **1.2 Veri Setinin Yüklenmesi ve Temel İşlemler**
   - 1.2.1 Veri Setini Okuma (`pd.read_csv()`)
   - 1.2.2 Sütun İsimlerini Türkçeleştirme (`.rename()`)
   - 1.2.3 Kategorik Sütunları `category` Tipine Dönüştürme (`.astype("category")`)
   - 1.2.4 Kategorik Değerleri Güncelleme (`.replace()`)
3. **1.3 Özet İstatistikler** — `.describe()`, `.describe(include="all")`
4. **1.4 Veri Görselleştirme**
   - 1.4.1 Çizgi Grafik (`plt.plot()`) — 4 örnek
   - 1.4.2 Bar Grafikleri (`plt.bar()`, `plt.barh()`) — 2 örnek
   - 1.4.3 Pasta Grafiği (`plt.pie()`) — 1 örnek
   - 1.4.4 Scatter Plot (`plt.scatter()`, `sns.scatterplot()`) — 3 örnek
   - 1.4.5 Histogram (`sns.histplot()`) — 2 örnek (8 bin, 12 bin)

---

## Öğrenme Hedefleri

- CSV dosyası okuma: `pd.read_csv()`
- Sütun yeniden adlandırma: `.rename(columns={...})`
- Kategorik tip dönüşümü: `.astype("category")`
- Betimsel istatistik: `.describe()`
- Grafik türleri:
  - **Çizgi grafiği:** `plt.plot()`
  - **Çubuk grafiği:** `plt.bar()`, `plt.barh()`
  - **Pasta grafiği:** `plt.pie()`
  - **Dağılım grafiği:** `plt.scatter()`, `sns.scatterplot()`
  - **Histogram:** `sns.histplot()`

---

## Kullanılan Kütüphaneler

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from yellowbrick.cluster import SilhouetteVisualizer
```

---

## Colab Ortamı

- **insurance.csv yolu:** `/content/drive/MyDrive/Colab Notebooks/insurance.csv`
- **tips.csv yolu:** `/content/drive/MyDrive/Colab Notebooks/tips.csv`
- **Drive bağlantısı:** `drive.mount('/content/drive')`
- Lokal kullanım için: Her iki CSV dosyası bu klasörde mevcuttur

---

## AI İçin Yeni Notebook Oluşturma Talimatları

Yeni bir hafta/konu için benzer yapıda materyaller oluşturmak istiyorsanız:

1. **Ders notebooku** (`X_konu.ipynb`): Orijinal veri seti ile tüm kodlar ve açıklamalar.
2. **Cevap notebooku** (`XA_konu.ipynb`): Yeni/farklı bir veri seti ile aynı yapı, tüm kodlar uyarlanmış.
3. **Ödev notebooku** (`XQ_konu.ipynb`): Cevap notebookundan türetilir — kod hücreleri boşaltılır, `# GÖREV:` ve `# İpucu:` yorum satırları eklenir, kütüphane import hücresi korunur.
