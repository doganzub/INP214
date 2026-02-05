# INP214 - Uygulamalı Makine Öğrenmesi (Applied Machine Learning)

> **AI Prompt Context:** Bu README, bir AI asistanının bu repo ile çalışırken ders yapısını, veri setlerini, haftalık konuları ve notebook-veri bağlantılarını hızlıca anlaması için optimize edilmiştir.

---

## Ders Kimliği

- **Ders Kodu:** INP214
- **Ders Adı:** Uygulamalı Makine Öğrenmesi (Applied Machine Learning)
- **Dil:** Türkçe (değişken isimleri, açıklamalar, markdown hücreleri Türkçe)
- **Platform:** Google Colab (tüm notebooklar `google.colab.drive` mount eder)
- **Python:** 3.13.4
- **Veri Kaynağı:** `data/` klasörü (Colab'da `/content/drive/MyDrive/Colab Notebooks/` yolundan okunur)

---

## Haftalık Müfredat ve Konu Haritası

| Hafta | Konu (TR) | Konu (EN) | Ders Notebook | Task Notebook | Veri Seti |
|-------|-----------|-----------|---------------|---------------|-----------|
| 1 | Veri Görselleştirme | Data Visualization | `docs/1_veri_gorsellestirme.ipynb` | `docs/1S_veri_gorsellestirme.ipynb` | `data/insurance.csv` |
| 2 | Veri Hazırlama | Data Preparation | `docs/2_veri_hazirlama.ipynb` | `docs/2S_veri_hazirlama.ipynb`, `docs/2S_task_veri_hazirlama.ipynb` | `data/auto-mpg.data`, `data/auto_mpg_extended.csv` |
| 3 | K-Means Kümeleme | K-Means Clustering | `docs/3_k_means.ipynb` | `docs/3S_k_means.ipynb`, `docs/IRIS_3_k_means.ipynb` | `data/mall_customers.csv` |
| 4 | Basit Doğrusal Regresyon | Simple Linear Regression | `docs/4_basit_dogReg_deneyim_maas.ipynb`, `docs/4_basit_dogReg_gelir_mutluluk.ipynb` | `docs/4S_basit_dogReg_gelir_mutluluk.ipynb`, `docs/4S_task_basit_dogReg_deneyim_maas.ipynb` | `data/Salary_dataset.csv`, `data/income.data.csv` |
| 5 | Coklu Dogrusal Regresyon | Multiple Linear Regression | `docs/5_coklu_dogReg.ipynb`, `docs/5_coklu_dogReg_day.ipynb` | `docs/5S_coklu_dogReg.ipynb`, `docs/5S_task_coklu_dogReg_day.ipynb` | `data/heart.data.csv`, `data/day.csv` |

---

## Notebook Adlandirma Kurali

- `X_konu.ipynb` → Ders (ogretim) notebooku (tam cozumlu, aciklamali)
- `XS_konu.ipynb` → Ogrenci versiyonu (cozumlu referans)
- `XS_task_konu.ipynb` → Gorev notebooku (bosluklu, TODO formatinda)
- `IRIS_3_k_means.ipynb` → Ek ornek (Iris veri seti ile K-Means)

---

## Veri Setleri Detayli Haritasi

### `data/insurance.csv` → Hafta 1
- **Satir:** 1338, **Sutun:** 7
- **Sutunlar:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`
- **Kullanim:** Veri gorsellestirme (line, bar, pie, scatter, histogram, box plot)
- **Turkcelestirme:** `age→yas`, `sex→cinsiyet`, `bmi→vki`, `children→cocukSayisi`, `smoker→sigaraDurum`, `region→bolge`, `charges→odemeMiktari`

### `data/auto-mpg.data` → Hafta 2
- **Satir:** 398, **Sutun:** 9 (boslukla ayrilmis, header yok)
- **Sutunlar:** `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin`, `car_name`
- **Kullanim:** Eksik veri (horsepower `?`), binning, outlier (IQR), sampling, label/dummy encoding, normalization
- **Onemli:** `horsepower` sutununda 6 adet `?` var → `NaN` → ortalama ile doldurulur

### `data/auto_mpg_extended.csv` → Hafta 2 (genisletilmis)
- **Satir:** 2000, **Sutun:** 9 (boslukla ayrilmis, header yok)
- **Olusan:** `data/auto-mpg_extended.ipynb` ile uretilmis sentetik veri

### `data/mall_customers.csv` → Hafta 3
- **Satir:** 200, **Sutun:** 5
- **Sutunlar:** `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`
- **Kullanim:** K-Means kumeleme, Elbow yontemi, Silhouette skoru
- **Optimal k:** 5 kume (Elbow + Silhouette ile dogrulanmis)

### `data/Salary_dataset.csv` → Hafta 4
- **Satir:** 30, **Sutun:** 3 (index + 2 ozellik)
- **Sutunlar:** `YearsExperience`, `Salary`
- **Kullanim:** Basit dogrusal regresyon (deneyim → maas)
- **Turkcelestirme:** `YearsExperience→deneyim`, `Salary→maas`
- **Sonuc:** R²=0.95, maas = 24190 + 9662 * deneyim

### `data/income.data.csv` → Hafta 4
- **Satir:** 500, **Sutun:** 3 (index + 2 ozellik)
- **Sutunlar:** `income`, `happiness`
- **Kullanim:** Basit dogrusal regresyon (gelir → mutluluk)

### `data/heart.data.csv` → Hafta 5
- **Satir:** 498, **Sutun:** 4 (index + 3 ozellik)
- **Sutunlar:** `biking`, `smoking`, `heart.disease`
- **Kullanim:** Coklu dogrusal regresyon (bisiklet+sigara → kalp hastaligi)
- **Turkcelestirme:** `biking→bisikletKullanimi`, `smoking→sigaraDurum`, `heart.disease→kalpHastaligi`
- **Sonuc:** R²=0.978, kalpHastaligi = 14.935 - 0.200*bisiklet + 0.181*sigara

### `data/day.csv` → Hafta 5
- **Satir:** 731, **Sutun:** 16
- **Sutunlar:** `instant`, `dteday`, `season`, `yr`, `mnth`, `holiday`, `weekday`, `workingday`, `weathersit`, `temp`, `atemp`, `hum`, `windspeed`, `casual`, `registered`, `cnt`
- **Kullanim:** Coklu dogrusal regresyon (bisiklet paylasim verisi, hava durumu etkileri)

### `data/hcvdat0.csv` → Ek veri
- **Satir:** 616, **Sutun:** 14
- **Sutunlar:** `Category`, `Age`, `Sex`, `ALB`, `ALP`, `ALT`, `AST`, `BIL`, `CHE`, `CHOL`, `CREA`, `GGT`, `PROT`
- **Kullanim:** Hepatit C siniflandirma / ek analiz icin

---

## Kullanilan Kutuphaneler ve Versiyonlar

```
numpy>=1.26.0        # Sayisal hesaplama, diziler
pandas>=2.2.0        # Veri cerceveleri, CSV okuma
matplotlib>=3.8.0    # Grafik cizimi (line, bar, pie, scatter, histogram, box)
seaborn>=0.13.0      # Gelismis gorsellestirme (heatmap, scatterplot, boxplot, histplot)
scikit-learn>=1.4.0  # ML modelleri (KMeans, LinearRegression, train_test_split, StandardScaler, MinMaxScaler, silhouette_score)
scipy>=1.12.0        # Istatistik (pearsonr korelasyon)
statsmodels>=0.14.0  # OLS regresyon modeli (smf.ols)
yellowbrick>=1.5     # ML gorsellestirme (SilhouetteVisualizer)
ipywidgets>=8.1.0    # Colab buton ve widget destegi
```

Tum bagimliliklar: `requirements.txt`

---

## Haftalik Ogrenme Hedefleri ve Teknikler

### Hafta 1: Veri Gorsellestirme
- CSV okuma (`pd.read_csv`)
- Sutun yeniden adlandirma (`rename`)
- Kategorik tip donusumu (`astype("category")`)
- Betimsel istatistik (`describe`)
- Grafikler: `plt.plot`, `plt.bar`, `plt.barh`, `plt.pie`, `plt.scatter`, `sns.scatterplot`, `sns.histplot`

### Hafta 2: Veri Hazirlama
- Eksik veri tespiti ve doldurma (`isnull`, `fillna`, ortalama ile)
- Ayiriklastirma: `lambda+map`, `pd.cut`, `pd.qcut`
- Gruplama: `groupby + describe/mean/sum`
- Tekrar eden satirlar: `duplicated`, `drop_duplicates`
- Aykiri deger: IQR yontemi, `boxplot`, `boxplot_stats`
- Ornekleme: `sample`, `random.seed`, `train_test_split`, tabakalı (`stratify`)
- Kodlama: `cat.codes` (label), `pd.get_dummies` (one-hot/dummy)
- Normalizasyon: `MinMaxScaler` (0-1), `StandardScaler` (z-score)

### Hafta 3: K-Means Kumeleme
- Korelasyon matrisi: `df.corr()`, `sns.heatmap`
- K-Means: `KMeans(n_clusters=k)`, `fit`, `labels_`, `cluster_centers_`
- Kume sayisi belirleme: Elbow (WSS/inertia), Silhouette skoru
- Gorsellestirme: kume scatter plot, centroid isaretleme

### Hafta 4: Basit Dogrusal Regresyon
- Pearson korelasyon: `pearsonr(x, y)` → r ve p-degeri
- OLS model: `smf.ols("y ~ x", data).fit()`
- Katsayilar: `model.params`, `model.rsquared`
- Egitim/test bolme: `sample(frac=0.7)` veya `train_test_split`
- Hata metrikleri: MAE, MSE, RMSE (`mean_absolute_error`, `mean_squared_error`)
- Gorsellestirme: scatter + regresyon dogrusu + residual

### Hafta 5: Coklu Dogrusal Regresyon
- Birden fazla bagimsiz degisken: `smf.ols("y ~ x1 + x2", data).fit()`
- Model yorumlama: katsayilar, p-degerleri, R², Adj-R²
- Performans: MAE, MSE, RMSE (test seti uzerinden)
- Gorsellestirme: bir degisken sabitken digeri ile regresyon

---

## Proje Yapisi

```
INP214/
├── README.md                          # Bu dosya (AI-dostu dokumantasyon)
├── requirements.txt                   # Python bagimliliklari
├── task_README.md                     # Task notebook hazirlama kilavuzu
├── clean_notebooks.py                 # Notebook temizleme scripti
├── data/                              # Tum veri setleri
│   ├── insurance.csv                  # Hafta 1 - Sigorta verisi
│   ├── auto-mpg.data                  # Hafta 2 - Otomobil yakit verisi
│   ├── auto_mpg_extended.csv          # Hafta 2 - Genisletilmis otomobil verisi
│   ├── auto-mpg_extended.ipynb        # auto_mpg_extended uretim notebooku
│   ├── mall_customers.csv             # Hafta 3 - Musteri segmentasyonu
│   ├── Salary_dataset.csv             # Hafta 4 - Deneyim/maas verisi
│   ├── income.data.csv                # Hafta 4 - Gelir/mutluluk verisi
│   ├── heart.data.csv                 # Hafta 5 - Kalp hastaligi verisi
│   ├── day.csv                        # Hafta 5 - Bisiklet paylasim verisi
│   └── hcvdat0.csv                    # Ek - Hepatit C verisi
├── docs/                              # Ders ve task notebooklari
│   ├── 1_veri_gorsellestirme.ipynb    # Hafta 1 ders
│   ├── 1S_veri_gorsellestirme.ipynb   # Hafta 1 ogrenci
│   ├── 2_veri_hazirlama.ipynb         # Hafta 2 ders
│   ├── 2S_veri_hazirlama.ipynb        # Hafta 2 ogrenci
│   ├── 2S_task_veri_hazirlama.ipynb   # Hafta 2 task
│   ├── 3_k_means.ipynb               # Hafta 3 ders
│   ├── 3S_k_means.ipynb              # Hafta 3 ogrenci
│   ├── IRIS_3_k_means.ipynb           # Hafta 3 ek (Iris)
│   ├── 4_basit_dogReg_deneyim_maas.ipynb      # Hafta 4 ders (deneyim-maas)
│   ├── 4_basit_dogReg_gelir_mutluluk.ipynb    # Hafta 4 ders (gelir-mutluluk)
│   ├── 4S_basit_dogReg_gelir_mutluluk.ipynb   # Hafta 4 ogrenci
│   ├── 4S_task_basit_dogReg_deneyim_maas.ipynb # Hafta 4 task
│   ├── 5_coklu_dogReg.ipynb                   # Hafta 5 ders (kalp hastaligi)
│   ├── 5_coklu_dogReg_day.ipynb               # Hafta 5 ders (bisiklet paylasim)
│   ├── 5S_coklu_dogReg.ipynb                  # Hafta 5 ogrenci
│   └── 5S_task_coklu_dogReg_day.ipynb         # Hafta 5 task
├── week-01-data-visualization/        # Hafta 1 calisma klasoru
├── week-02-data-preparation/          # Hafta 2 calisma klasoru
├── week-03-kmeans-clustering/         # Hafta 3 calisma klasoru
├── week-04-simple-linear-regression/  # Hafta 4 calisma klasoru
└── week-05-multiple-linear-regression/ # Hafta 5 calisma klasoru
```

---

## Colab Ortaminda Calistirma

Notebooklar Google Colab icin tasarlanmistir. Her notebook basinda:

1. **GitHub Token butonu** → repo senkronizasyonu icin
2. **Drive & GitHub Senkronizasyon butonu** → notebook kayit/yukleme
3. **Kutuphane yukleme:** `!pip install -q numpy pandas scikit-learn matplotlib seaborn yellowbrick`
4. **Drive baglantisi:** `drive.mount('/content/drive')`
5. **Veri okuma yolu:** `/content/drive/MyDrive/Colab Notebooks/<dosya_adi>`

### Lokal Calistirma

```bash
git clone <repo_url>
cd INP214
pip install -r requirements.txt
jupyter notebook
```

> **Not:** Lokal calistirmada `google.colab` importlarini ve `drive.mount()` satirlarini yorum satirina alin. Veri yollarini `data/<dosya_adi>` olarak degistirin.

---

## AI Asistan Icin Hizli Referans

**Bu repoyu anlaman gereken temel bilgiler:**

1. Ders Turkce islenilir, degisken isimleri Turkcedir
2. Her hafta farkli bir ML konusu isler (gorsellestirme → veri hazirlama → kumeleme → basit regresyon → coklu regresyon)
3. Veri setleri `data/` klasorundedir, her biri belirli haftalara aittir (yukaridaki haritaya bak)
4. `docs/` klasorundeki X_ prefiksi ders notebookunu, XS_ ogrenci versiyonunu, XS_task_ gorev versiyonunu gosterir
5. Notebooklar Colab icin yazilmistir (Drive mount, pip install satirlari mevcut)
6. Temel kutuphaneler: pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels, yellowbrick, scipy
7. Her notebook icinde Turkce markdown aciklamalar, kod yorumlari ve istatistik tablolari vardir
8. `week-XX-*` klasorleri ogrenci calisma alanlaridir
9. `task_README.md` dosyasi task notebook hazirlama kilavuzudur