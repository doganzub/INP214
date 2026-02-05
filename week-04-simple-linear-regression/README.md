# Hafta 4: Basit Dogrusal Regresyon (Simple Linear Regression)

## Konu Ozeti

Bu hafta, **basit dogrusal regresyon** yontemi ogrenilir. Tek bir bagimsiz degisken (X) ile bir bagimli degisken (Y) arasindaki dogrusal iliski analiz edilir. Iki farkli veri seti uzerinde calisilir:
1. **Deneyim → Maas** (`Salary_dataset.csv`)
2. **Gelir → Mutluluk** (`income.data.csv`)

### Matematiksel Model
```
Y = B0 + B1 * X + e
```

---

## Veri Setleri

| Dosya | Satir | Sutun | Bagimsiz (X) | Bagimli (Y) | R² |
|-------|-------|-------|---------------|--------------|-----|
| `Salary_dataset.csv` | 30 | 3 | `YearsExperience` (deneyim) | `Salary` (maas) | 0.957 |
| `income.data.csv` | 498 | 3 | `income` (gelir) | `happiness` (mutluluk) | 0.749 |

### Salary_dataset.csv
- **Turkcelestirme:** `YearsExperience→deneyim`, `Salary→maas`
- **Regresyon Denklemi:** `maas = 25792.20 + 9449.96 * deneyim`
- **Pearson r:** 0.978 (cok guclu pozitif iliski)
- **Kaynak:** Kaggle - Simple Linear Regression

### income.data.csv
- **Turkcelestirme:** `income→gelir`, `happiness→mutluluk`
- **Regresyon Denklemi:** `mutluluk = 0.228 + 0.708 * gelir`
- **Pearson r:** 0.866 (guclu pozitif iliski)
- **Kaynak:** Bevans (2023b), Scribbr

---

## Notebooklar

| Dosya | Tur | Veri Seti | Aciklama |
|-------|-----|-----------|----------|
| `04-simple-linear-regression.ipynb` | Temiz ders | `income.data.csv` | Hafta notebooku (week klasoru icin) |
| `4_basit_dogReg_deneyim_maas.ipynb` | Ders (ogretim) | `Salary_dataset.csv` | Deneyim-maas analizi, tam cozumlu |
| `4_basit_dogReg_gelir_mutluluk.ipynb` | Ders (ogretim) | `income.data.csv` | Gelir-mutluluk analizi, tam cozumlu |
| `4S_basit_dogReg_gelir_mutluluk.ipynb` | Ogrenci | `income.data.csv` | Cozumlu referans versiyonu |
| `4S_task_basit_dogReg_deneyim_maas.ipynb` | Gorev (task) | `Salary_dataset.csv` | Bosluklu, ogrenci tamamlar |

---

## Ogrenme Hedefleri

### Korelasyon Analizi
- Pearson korelasyon: `pearsonr(x, y)` → r degeri ve p-degeri
- r > 0.8 → guclu pozitif iliski

### Model Kurma
- OLS modeli: `smf.ols("y ~ x", data=egitim).fit()`
- Katsayilar: `model.params` (Intercept = B0, degisken = B1)
- Aciklayicilik: `model.rsquared` (R²)
- Model ozeti: `model.summary()`

### Egitim/Test Bolme
- `sample(frac=0.7, random_state=1)` → %70 egitim
- Kalan %30 → test seti

### Performans Degerlendirme
- **MAE** (Mean Absolute Error): `mean_absolute_error()`
- **MSE** (Mean Squared Error): `mean_squared_error()`
- **RMSE** (Root MSE): `np.sqrt(mse)`

### Gorsellestirme
- Scatter plot: gercek degerler (pembe noktalar)
- Regresyon dogrusu: tahmin edilen degerler (mavi cizgi)
- Residual: gercek ile tahmin arasindaki dikey mesafe

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

- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/Salary_dataset.csv`
- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/income.data.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: Her iki CSV bu klasorde mevcuttur
