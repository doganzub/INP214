# Hafta 2: Veri Hazirlama (Data Preparation)

## AI Prompt — Pedagojik Yapi ve Dosya Iliskileri

> **Bu README, bir AI asistaninin week-02 klasorunu tamamen anlamasi icin yazilmistir.**
> Asagidaki bilgileri okuduktan sonra week-01 dosyalarina bakmaniza gerek yoktur.

### Pedagojik Desen (Tum Haftalar Icin Gecerli)

Her hafta uc katmanli bir notebook sistemi kullanilir:

| Katman | Adlandirma | Veri Seti | Aciklama |
|--------|-----------|-----------|----------|
| **Ders (Lecture)** | `N_konu.ipynb` | Orijinal veri | Ogretmenin kullandigi tam cozumlu ders materyali. GitHub token/sync hucreleri icerir. |
| **Cevap Anahtari (Answer Key)** | `NA_konu.ipynb` | **Farkli ama benzer** veri | Ders notebookunun bire-bir aynisi yapisal olarak, ama **farkli bir veri seti** ile. GitHub token hucreleri **icermez**. Ogrencinin cozumu dogrulamasi icin referans. |
| **Gorev (Task)** | `NQ_konu.ipynb` | Cevap anahtariyla ayni veri | Cevap anahtarinin (NA) kopyasi, ancak **tum kod hucreleri bosaltilmis** ve `# GOREV N:` yorumlariyla degistirilmis. Ogrenci bu dosyayi doldurur. |

**Onemli kurallar:**
- `NA` ile `NQ` **ayni veri setini** kullanir (lecture'daki degil).
- `NQ`'da **hicbir cozum kodu** bulunmaz — sadece `# GOREV` yorumlari ve ipuclari.
- `NQ`'da kutuphane import hucresi (`import numpy as np ...`) oldugu gibi korunur.
- `NA`'da markdown aciklamalari, `N_` ile **ayni yapisal siraya** sahiptir.

### Week-01 Ornegi (Referans — dosyalara bakmaniza gerek yok)

| Dosya | Veri Seti | Rol |
|-------|-----------|-----|
| `1_veri_gorsellestirme.ipynb` | `insurance.csv` (7 sutun, 1338 satir) | Ders |
| `1A_veri_gorsellestirme..ipynb` | `tips.csv` (7 sutun, 244 satir) | Cevap anahtari |
| `1Q_veri_gorsellestirme.ipynb` | `tips.csv` | Gorev (bos kod hucreleri, `# GOREV` yorumlari) |

`tips.csv`, `insurance.csv` ile ayni domaine (restoran/hizmet) ait, benzer sutun yapisi olan farkli bir veri setidir. Kaggle'da deep search yapilarak bulunmustur.

---

## Week-02 Dosya Yapisi

### Veri Setleri

| Dosya | Satir | Sutun | Format | Aciklama |
|-------|-------|-------|--------|----------|
| `auto-mpg.data` | 398 | 9 | Boslukla ayrilmis, header yok | Ders notebooku icin orijinal UCI Auto MPG veri seti |
| `automobile.csv` | 205 | 9 | CSV, header var | Cevap anahtari ve gorev notebooku icin UCI Automobile veri seti (Kaggle deep search ile bulundu) |

#### auto-mpg.data Sutunlari
`mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin`, `car_name`
- **Eksik veri:** `horsepower` sutununda 6 adet `?` karakteri
- **Okuma:** `pd.read_csv(..., sep=r"\s+", header=None, names=[...])`

#### automobile.csv Sutunlari
`city_mpg`, `engine_size`, `horsepower`, `curb_weight`, `peak_rpm`, `normalized_losses`, `body_style`, `fuel_type`, `make`
- **Eksik veri:** `normalized_losses` (41 adet `?`), `horsepower` (2 adet `?`), `peak_rpm` (2 adet `?`)
- **Okuma:** `pd.read_csv(...)` (standart CSV, header mevcut)
- **Kaynak:** UCI Machine Learning Repository — 1985 Ward's Automotive Yearbook (https://archive.ics.uci.edu/dataset/10/automobile)

#### Veri Seti Eslestirme Tablosu

| auto-mpg.data sutunu | automobile.csv karsiligi | Rol |
|---------------------|------------------------|-----|
| `mpg` (float) | `city_mpg` (int) | Surekli hedef, binning icin |
| `displacement` (float) | `engine_size` (int) | Sayisal ozellik |
| `horsepower` (object, ? var) | `horsepower` (object, ? var) | Eksik veri + aykiri deger analizi |
| `weight` (float) | `curb_weight` (int) | Sayisal ozellik |
| `acceleration` (float) | `peak_rpm` (object, ? var) | Sayisal ozellik |
| `model_year` (int) | `normalized_losses` (object, 41x ? var) | Sayisal, eksik veri imputation |
| `origin` (int 1/2/3) | `body_style` (string) | Kategorik, encoding icin |
| — | `fuel_type` (string) | Ek kategorik ozellik |
| `car_name` (string) | `make` (string) | Metin tanimlayici |

### Notebooklar

| Dosya | Veri Seti | Rol | Hucre Sayisi |
|-------|-----------|-----|-------------|
| `2_veri_hazirlama.ipynb` | `auto-mpg.data` | Ders (ogretim) | 46 (2 GitHub token + 44 icerik) |
| `2A_veri_hazirlama.ipynb` | `automobile.csv` | Cevap anahtari | 44 (GitHub token yok) |
| `2Q_veri_hazirlama.ipynb` | `automobile.csv` | Gorev | 44 (18 GOREV, kod hucreleri bos) |

### Bolum Yapisi (Tum 3 Notebook Icin Ayni Sira)

| No | Bolum | Ders (`2_`) islem | Cevap (`2A`) islem |
|----|-------|-------------------|-------------------|
| 2.1 | Kutuphane Yukleme | Ayni importlar | Ayni importlar |
| 2.2 | Veri Okuma | `auto-mpg.data`, `sep="\s+"`, `header=None` | `automobile.csv`, standart `read_csv` |
| 2.3 | Eksik Veri | `horsepower`'da 6x `?` → `NaN` → `mean` | 3 sutunda `?` → `NaN` → `mean` |
| 2.4 | Ayiriklastirma | `mpg` → Dusuk/Orta/Yuksek (23.5/30) | `city_mpg` → Dusuk/Orta/Yuksek (21/30) |
| 2.5 | Describe | `describe(include="all")` | `describe(include="all")` |
| 2.6 | Gruplama | `groupby("durum")["mpg"]` | `groupby("durum")["city_mpg"]` |
| 2.7 | Tekrarlayan Satirlar | `duplicated()`, `drop_duplicates()` | `duplicated()`, `drop_duplicates()` |
| 2.8 | Aykiri Deger | IQR `horsepower`, boxplot | IQR `horsepower`, boxplot |
| 2.9 | Ornekleme | random, seed, replacement, train/test, stratified | random, seed, replacement, train/test, stratified |
| 2.10 | Kodlama + Normalizasyon | `cat.codes`, `get_dummies`, `MinMaxScaler` | `cat.codes`, `get_dummies`, `MinMaxScaler` |

### 2Q Gorev Listesi (18 GOREV)

| GOREV | Bolum | Aciklama |
|-------|-------|----------|
| 1 | 2.2 | automobile.csv oku, dtypes ve head goruntule |
| 2 | 2.3 | ? → NaN, tip donusumu, fillna(mean) |
| 3 | 2.4 | city_mpg binning (4 yontem) |
| 4 | 2.5 | describe(include='all') |
| 5 | 2.6 | groupby + describe |
| 6 | 2.7 | duplicated + drop_duplicates |
| 7 | 2.8 | IQR hesapla |
| 8 | 2.8 | Aykiri deger indeksleri bul |
| 9 | 2.8 | Basit boxplot |
| 10 | 2.8 | Aciklamali boxplot |
| 11 | 2.8 | Aykiri deger kaldirma (opsiyonel) |
| 12 | 2.9.1 | Rastgele ornekleme |
| 13 | 2.9.2 | Tohumlu ornekleme |
| 14 | 2.9.3 | Yerine koyarak secim |
| 15 | 2.9.4 | Egitim/test bolme |
| 16 | 2.9.5 | Tabakali ornekleme |
| 17 | 2.10.1 | cat.codes + get_dummies |
| 18 | 2.10.2 | MinMaxScaler normalizasyon |

---

## Ogrenme Hedefleri

### Eksik Veri
- Tespit: `.isnull()`, `.isnull().sum()`
- Doldurma: `.fillna()`, ortalama ile imputation
- `?` karakteri → `NaN` → `float64` donusumu

### Ayiriklastirma (Binning/Discretization)
- `lambda + map` ile kategori olusturma
- `pd.cut()` → sabit aralikli / esit genislikli gruplama
- `pd.qcut()` → esit frekanslı gruplama

### Gruplama ve Aggregation
- `groupby()` + `describe()` / `mean()` / `sum()`

### Tekrar Eden Satirlar
- `.duplicated()`, `.drop_duplicates()`

### Aykiri Deger Analizi
- IQR yontemi (Q1, Q3, IQR = Q3 - Q1)
- `sns.boxplot()`, aciklamali boxplot

### Ornekleme
- Rastgele: `sample()`, `random.sample()`
- Tohumlu: `random.seed()`, `random_state=`
- Yerine koyarak: `random.choices()`
- Egitim/Test: `.sample(frac=0.7)` + `.isin()`
- Tabakali: `train_test_split(stratify=...)`

### Kodlama (Encoding)
- Label Encoding: `.cat.codes`
- One-Hot/Dummy: `pd.get_dummies()`

### Normalizasyon
- Min-Max: `MinMaxScaler()` → 0-1 arasi

---

## Kullanilan Kutuphaneler

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.cbook import boxplot_stats
import random
from random import sample
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
```

---

## Colab Ortami

- Ders veri yolu: `/content/drive/MyDrive/Colab Notebooks/auto-mpg.data`
- Cevap/Gorev veri yolu: `/content/drive/MyDrive/Colab Notebooks/automobile.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: `auto-mpg.data` ve `automobile.csv` bu klasorde mevcuttur

---

## Yeni Notebook Olusturma Rehberi (AI Icin)

Eger yeni bir hafta icin benzer notebooklar olusturmaniz gerekiyorsa:

1. **Ders notebookunu** (`N_konu.ipynb`) okuyun — veri seti, bolum yapisi, kullanilan teknikler
2. **Benzer veri seti bulun** — ayni domain, benzer sutun yapisi, eksik veri iceren, Kaggle/UCI'dan
3. **Cevap anahtari olusturun** (`NA_konu.ipynb`) — ders ile birebir ayni bolum sirasi, farkli veri seti, GitHub token hucreleri olmadan
4. **Gorev notebooku olusturun** (`NQ_konu.ipynb`) — cevap anahtarindan turetilir, kod hucreleri bosaltilir, `# GOREV N:` yorumlari eklenir, kutuphane import hucresi korunur
