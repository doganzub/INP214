# Hafta 1: Veri Gorsellestirme (Data Visualization)

## Konu Ozeti

Bu hafta, Python ile **veri gorsellestirme** teknikleri ogrenilir. Sigorta veri seti (`insurance.csv`) uzerinden cesitli grafik turleri olusturulur ve verinin gorsel analizi yapilir.

---

## Veri Seti

| Dosya | Satir | Sutun | Aciklama |
|-------|-------|-------|----------|
| `insurance.csv` | 1338 | 7 | Sigorta musteri verisi |

**Sutunlar:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`

**Turkcelestirme:**
- `age` → `yas`
- `sex` → `cinsiyet`
- `bmi` → `vki`
- `children` → `cocukSayisi`
- `smoker` → `sigaraDurum`
- `region` → `bolge`
- `charges` → `odemeMiktari`

---

## Notebooklar

| Dosya | Tur | Aciklama |
|-------|-----|----------|
| `01-data-visualization.ipynb` | Temiz ders | Hafta notebooku (week klasoru icin) |
| `1_veri_gorsellestirme.ipynb` | Ders (ogretim) | Tam cozumlu, aciklamali |
| `1S_veri_gorsellestirme.ipynb` | Ogrenci | Cozumlu referans versiyonu |

---

## Ogrenme Hedefleri

- CSV dosyasi okuma: `pd.read_csv()`
- Sutun yeniden adlandirma: `.rename(columns={...})`
- Kategorik tip donusumu: `.astype("category")`
- Betimsel istatistik: `.describe()`
- Grafik turleri:
  - **Cizgi grafigi:** `plt.plot()`
  - **Cubuk grafigi:** `plt.bar()`, `plt.barh()`
  - **Pasta grafigi:** `plt.pie()`
  - **Dagilim grafigi:** `plt.scatter()`, `sns.scatterplot()`
  - **Histogram:** `sns.histplot()`
  - **Kutu grafigi:** `sns.boxplot()`

---

## Kullanilan Kutuphaneler

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Colab Ortami

- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/insurance.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: `insurance.csv` bu klasorde mevcuttur
