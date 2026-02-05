# Hafta 2: Veri Hazirlama (Data Preparation)

## Konu Ozeti

Bu hafta, **veri on isleme** teknikleri ogrenilir. Otomobil yakit tuketimi veri seti (`auto-mpg.data`) uzerinden eksik veri yonetimi, ayiriklastirma, aykiri deger analizi, ornekleme, kodlama ve normalizasyon islemleri uygulanir.

---

## Veri Setleri

| Dosya | Satir | Sutun | Aciklama |
|-------|-------|-------|----------|
| `auto-mpg.data` | 398 | 9 | Otomobil yakit verisi (boslukla ayrilmis, header yok) |
| `auto_mpg_extended.csv` | 2000 | 9 | Sentetik genisletilmis versi (auto-mpg_extended.ipynb ile uretilmis) |

**Sutunlar:** `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin`, `car_name`

**Onemli:** `horsepower` sutununda 6 adet `?` degeri var → `NaN` olarak degistirilir → ortalama ile doldurulur

---

## Notebooklar

| Dosya | Tur | Aciklama |
|-------|-----|----------|
| `02-data-preparation.ipynb` | Temiz ders | Hafta notebooku (week klasoru icin) |
| `2_veri_hazirlama.ipynb` | Ders (ogretim) | Tam cozumlu, tum teknikler aciklamali |
| `2S_veri_hazirlama.ipynb` | Ogrenci | Cozumlu referans versiyonu |
| `2S_task_veri_hazirlama.ipynb` | Gorev (task) | Bosluklu, ogrenci tamamlar |

---

## Ogrenme Hedefleri

### Eksik Veri
- Tespit: `.isnull()`, `.isnull().sum()`
- Doldurma: `.fillna()`, ortalama ile imputation
- `horsepower` sutunundaki `?` → `NaN` → `float` donusumu

### Ayiriklastirma (Binning/Discretization)
- `lambda + map` ile kategori olusturma
- `pd.cut()` → esit aralikli gruplama
- `pd.qcut()` → esit frekanslı gruplama

### Gruplama ve Aggregation
- `groupby()` + `describe()` / `mean()` / `sum()`

### Tekrar Eden Satirlar
- `.duplicated()`, `.drop_duplicates()`

### Aykiri Deger Analizi
- IQR yontemi (Q1, Q3, IQR = Q3 - Q1)
- `sns.boxplot()`, `boxplot_stats()`

### Ornekleme
- Rastgele: `.sample(n=...)`
- Tohumlu: `random.seed()`, `random_state=`
- Tabakalı: `train_test_split(stratify=...)`

### Kodlama (Encoding)
- Label Encoding: `.cat.codes`
- One-Hot/Dummy: `pd.get_dummies()`

### Normalizasyon
- Min-Max: `MinMaxScaler()` → 0-1 arasi
- Z-score: `StandardScaler()` → ortalama=0, std=1

---

## Kullanilan Kutuphaneler

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.cbook import boxplot_stats
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
```

---

## Colab Ortami

- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/auto-mpg.data`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: `auto-mpg.data` ve `auto_mpg_extended.csv` bu klasorde mevcuttur
