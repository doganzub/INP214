# Hafta 5: Coklu Dogrusal Regresyon (Multiple Linear Regression)

## Konu Ozeti

Bu hafta, **coklu dogrusal regresyon** yontemi ogrenilir. Birden fazla bagimsiz degisken (X1, X2) ile bir bagimli degisken (Y) arasindaki dogrusal iliski analiz edilir. Iki farkli veri seti uzerinde calisilir:
1. **Bisiklet Kullanimi + Sigara → Kalp Hastaligi** (`heart.data.csv`)
2. **Hava Sicakligi + Nem → Bisiklet Kiralama** (`day.csv`)

### Matematiksel Model
```
Y = B0 + B1 * X1 + B2 * X2 + e
```

---

## Veri Setleri

| Dosya | Satir | Sutun | X1 | X2 | Y | R² |
|-------|-------|-------|----|----|---|-----|
| `heart.data.csv` | 498 | 4 | `biking` (bisikletKullanimi) | `smoking` (sigaraDurum) | `heart.disease` (kalpHastaligi) | 0.978 |
| `day.csv` | 731 | 16 | `temp` (havaSicakligi) | `hum` (nemOrani) | `cnt` (kiralamaSayisi) | 0.436 |

### heart.data.csv
- **Turkcelestirme:** `biking→bisikletKullanimi`, `smoking→sigaraDurum`, `heart.disease→kalpHastaligi`
- **Regresyon Denklemi:** `kalpHastaligi = 14.935 - 0.200 * bisikletKullanimi + 0.181 * sigaraDurum`
- **Yorum:** Bisiklet kullanimi kalp hastaligini azaltir (negatif katsayi), sigara artirir (pozitif katsayi)
- **Pearson r:** bisiklet↔kalp: -0.935, sigara↔kalp: +0.309
- **Kaynak:** Bevans (2023b), Scribbr

### day.csv (Bike Sharing Dataset)
- **Turkcelestirme:** `temp→havaSicakligi`, `hum→nemOrani`, `cnt→kiralamaSayisi`
- **Regresyon Denklemi:** `kiralamaSayisi = 2716.457 + 6857.488 * havaSicakligi - 2604.412 * nemOrani`
- **Yorum:** Sicaklik kiralama sayisini artirir (pozitif), nem azaltir (negatif)
- **Pearson r:** sicaklik↔kiralama: +0.627, nem↔kiralama: -0.101
- **Kaynak:** UCI Bike Sharing Dataset (Fanaee-T & Gama, 2013)

---

## Notebooklar

| Dosya | Tur | Veri Seti | Aciklama |
|-------|-----|-----------|----------|
| `05-multiple-linear-regression.ipynb` | Temiz ders | `heart.data.csv` | Hafta notebooku (week klasoru icin) |
| `5_coklu_dogReg.ipynb` | Ders (ogretim) | `heart.data.csv` | Kalp hastaligi analizi, tam cozumlu |
| `5_coklu_dogReg_day.ipynb` | Ders (ogretim) | `day.csv` | Bisiklet kiralama analizi, tam cozumlu |
| `5S_coklu_dogReg.ipynb` | Ogrenci | `heart.data.csv` | Cozumlu referans versiyonu |
| `5S_task_coklu_dogReg_day.ipynb` | Gorev (task) | `day.csv` | Bosluklu, ogrenci tamamlar |

---

## Ogrenme Hedefleri

### Korelasyon Analizi
- Pearson korelasyon: `pearsonr(x, y)` → her degisken cifti icin
- Kollinearite kontrolu: bagimsiz degiskenler arasi korelasyon

### Model Kurma
- OLS modeli: `smf.ols("y ~ x1 + x2", data=egitim).fit()`
- Katsayilar: `model.params` (Intercept, X1 katsayisi, X2 katsayisi)
- Aciklayicilik: `model.rsquared`, `model.rsquared_adj`
- F-istatistigi: modelin genel anlamliligi
- Model ozeti: `model.summary()`

### Egitim/Test Bolme
- `sample(frac=0.7, random_state=1)` → %70 egitim
- `veriSeti.drop(egitim.index)` → %30 test

### Performans Degerlendirme
- **MAE** (Mean Absolute Error): `mean_absolute_error()`
- **MSE** (Mean Squared Error): `mean_squared_error()`
- **RMSE** (Root MSE): `np.sqrt(mse)`
- Yuzdelik hata: `%MAE`, `%RMSE`

### Gorsellestirme
- Scatter plot: gercek degerler vs tahminler
- Regresyon dogrusu
- Bir degisken sabitken diger degiskenin etkisi grafigi

### Basit vs Coklu Regresyon Farki
- Basit: tek X degiskeni (Hafta 4)
- Coklu: birden fazla X degiskeni (Hafta 5)
- Adj-R²: degisken sayisi duzeltilmis aciklayicilik

---

## Kullanilan Kutuphaneler

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error, mean_absolute_error
from matplotlib.cbook import boxplot_stats
```

---

## Colab Ortami

- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/heart.data.csv`
- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/day.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: Her iki CSV bu klasorde mevcuttur
