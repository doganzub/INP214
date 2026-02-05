# Hafta 3: K-Means Kumeleme (K-Means Clustering)

## Konu Ozeti

Bu hafta, **gozetimsiz ogrenme** yontemlerinden **K-Means kumeleme** algoritmasi ogrenilir. Musteri segmentasyonu ornegi uzerinden (`mall_customers.csv`) kumeleme analizi yapilir. Ek olarak Iris veri seti ile de uygulama gerceklestirilir.

---

## Veri Setleri

| Dosya | Satir | Sutun | Aciklama |
|-------|-------|-------|----------|
| `mall_customers.csv` | 200 | 5 | Alisveris merkezi musteri verisi |
| Iris (sklearn dahili) | 150 | 4+1 | Cicek turu siniflandirma (IRIS notebookunda) |

**mall_customers.csv Sutunlari:** `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`

**Optimal k:** 5 kume (Elbow + Silhouette yontemleri ile dogrulanmis)

---

## Notebooklar

| Dosya | Tur | Aciklama |
|-------|-----|----------|
| `03-kmeans.ipynb` | Temiz ders | Hafta notebooku (week klasoru icin) |
| `3_k_means.ipynb` | Ders (ogretim) | Tam cozumlu, `mall_customers.csv` |
| `3S_k_means.ipynb` | Ogrenci | Cozumlu referans, `mall_customers.csv` |
| `IRIS_3_k_means.ipynb` | Ek ornek | Iris veri seti ile K-Means uygulamasi |

---

## Ogrenme Hedefleri

### Korelasyon Analizi
- Korelasyon matrisi: `df.corr()`
- Isı haritasi: `sns.heatmap()`

### K-Means Algoritmasi
- Model olusturma: `KMeans(n_clusters=k)`
- Egitim: `.fit()`
- Kume etiketleri: `.labels_`
- Merkez noktalari: `.cluster_centers_`
- Inertia (WSS): `.inertia_`

### Optimal Kume Sayisi Belirleme
- **Elbow Yontemi:** WSS/inertia degerlerinin k'ya gore grafigi, "dirsek" noktasi
- **Silhouette Skoru:** `silhouette_score()`, `SilhouetteVisualizer()`

### Gorsellestirme
- Kume scatter plot: her kume farkli renkte
- Centroid (merkez) isaretleme
- Silhouette grafigi

### IRIS Ek Calismasi
- `sklearn.datasets.load_iris()` ile dahili veri seti
- Turkce sutun adlari: `canakU`, `canakG`, `tacU`, `tacG`, `tur`
- 3 tur: setosa, versicolor, virginica
- Optimal k = 3

---

## Kullanilan Kutuphaneler

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn import datasets
```

---

## Colab Ortami

- Veri yolu: `/content/drive/MyDrive/Colab Notebooks/mall_customers.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: `mall_customers.csv` bu klasorde mevcuttur
