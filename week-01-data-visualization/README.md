# Hafta 1: Veri Gorsellestirme (Data Visualization)

## AI Prompt — Pedagojik Yapi ve Dosya Iliskileri

> **Bu README, bir AI asistaninin week-01 klasorunu tamamen anlamasi icin yazilmistir.**
> Asagidaki bilgileri okuduktan sonra notebook dosyalarini tek tek incelemenize gerek yoktur.

### Pedagojik Desen (Tum Haftalar Icin Gecerli)

Her hafta uc katmanli bir notebook sistemi kullanilir:

| Katman | Adlandirma | Veri Seti | Aciklama |
|--------|-----------|-----------|----------|
| **Ders (Lecture)** | `N_konu.ipynb` | Orijinal veri | Ogretmenin kullandigi tam cozumlu ders materyali. |
| **Cevap Anahtari (Answer Key)** | `NA_konu.ipynb` | **Farkli ama benzer** veri | Ders notebookunun bire-bir aynisi yapisal olarak, ama **farkli bir veri seti** ile. Ogrencinin cozumu dogrulamasi icin referans. |
| **Gorev (Task)** | `NQ_konu.ipynb` | Cevap anahtariyla ayni veri | Cevap anahtarinin (NA) kopyasi, ancak **tum kod hucreleri bosaltilmis** ve `# GOREV:` yorumlariyla degistirilmis. Ogrenci bu dosyayi doldurur. |

**Onemli kurallar:**
- `NA` ile `NQ` **ayni veri setini** kullanir (lecture'daki degil).
- `NQ`'da **hicbir cozum kodu** bulunmaz — sadece `# GOREV` yorumlari ve ipuclari.
- `NQ`'da kutuphane import hucresi (`import numpy as np ...`) oldugu gibi korunur.
- `NA`'da markdown aciklamalari, `N_` ile **ayni yapisal siraya** sahiptir.

---

## Week-01 Dosya Yapisi

### Veri Setleri

| Dosya | Satir | Sutun | Aciklama |
|-------|-------|-------|----------|
| `insurance.csv` | 1338 | 7 | Saglik sigortasi musteri verisi (ders notebooku icin orijinal veri seti) |
| `tips.csv` | 244 | 7 | Restoran bahsis verisi (cevap anahtari ve gorev notebooku icin) |

#### insurance.csv Sutunlari (Orijinal → Turkcesi)

| Orijinal | Turkce | Tip | Aciklama |
|----------|--------|-----|----------|
| `age` | `yas` | int64 | Musteri yasi |
| `sex` | `cinsiyet` | object→category | `male`→`erkek`, `female`→`kadin` |
| `bmi` | `vki` | float64 | Vucut Kitle Indeksi |
| `children` | `cocukSayisi` | int64 | Cocuk sayisi |
| `smoker` | `sigaraDurum` | object→category | `yes`→`evet`, `no`→`hayir` |
| `region` | `bolge` | object→category | `southeast`→`guneydogu`, `northwest`→`kuzeybati`, `southwest`→`guneybati`, `northeast`→`kuzeydogu` |
| `charges` | `odemeMiktari` | float64 | Sigorta odeme miktari |

#### tips.csv Sutunlari (Orijinal → Turkcesi)

| Orijinal | Turkce | Tip | Aciklama |
|----------|--------|-----|----------|
| `total_bill` | `toplamHesap` | float64 | Toplam hesap miktari |
| `tip` | `bahsis` | float64 | Bahsis miktari |
| `sex` | `cinsiyet` | object→category | `Male`→`erkek`, `Female`→`kadin` |
| `smoker` | `sigaraDurum` | object→category | `Yes`→`evet`, `No`→`hayir` |
| `day` | `gun` | object→category | `Sun`→`pazar`, `Sat`→`cumartesi`, `Thur`→`persembe`, `Fri`→`cuma` |
| `time` | `ogun` | object→category | `Lunch`→`ogle`, `Dinner`→`aksam` |
| `size` | `kisiSayisi` | int64 | Kisi sayisi |

#### Veri Seti Eslestirme Tablosu

| insurance.csv (Ders) | tips.csv (Cevap/Gorev) | Rol |
|---------------------|----------------------|-----|
| `yas` (int) | `toplamHesap` (float) | Sayisal ana degisken |
| `vki` (float) | `bahsis` (float) | Sayisal ikinci degisken |
| `cinsiyet` (category) | `cinsiyet` (category) | Kategorik — encoding, gruplama |
| `sigaraDurum` (category) | `sigaraDurum` (category) | Kategorik — gruplama, scatter hue |
| `bolge` (category) | `gun` (category) | Kategorik — pasta grafigi, gruplama |
| `odemeMiktari` (float) | `toplamHesap` (float) | Sayisal — hedef degisken |
| `cocukSayisi` (int) | `kisiSayisi` (int) | Sayisal — tamsayi |

### Notebooklar

| Dosya | Veri Seti | Rol | Hucre Sayisi |
|-------|-----------|-----|-------------|
| `1_veri_gorsellestirme.ipynb` | `insurance.csv` | Ders (ogretim) | 42 |
| `1A_veri_gorsellestirme..ipynb` | `tips.csv` | Cevap anahtari | 42 |
| `1Q_veri_gorsellestirme.ipynb` | `tips.csv` | Gorev | 42 (17 GOREV, kod hucreleri bos) |

**Not:** `1A` dosya adinda cift nokta (`..`) bulunmaktadir — bu bilerek birakilmistir.

### Notebook Iliski Semasi

```
1_veri_gorsellestirme.ipynb  (DERS - insurance.csv)
        |
        v  (ayni yapi, tips.csv'ye uyarlanmis)
1A_veri_gorsellestirme..ipynb  (CEVAP - tips.csv, tam cozum)
        |
        v  (kodlar kaldirilmis, # GOREV yorumlari eklenmis)
1Q_veri_gorsellestirme.ipynb  (GOREV - tips.csv, bos kodlar)
```

### Bolum Yapisi (Tum 3 Notebook Icin Ayni Sira)

| No | Bolum | Ders (`1_`) islem | Cevap (`1A`) islem |
|----|-------|-------------------|-------------------|
| 1.1 | Kutuphane Yukleme | numpy, pandas, matplotlib, seaborn, sklearn, yellowbrick | Ayni importlar |
| 1.2.1 | Veri Okuma | `pd.read_csv("insurance.csv")` → `insurance_df` | `pd.read_csv("tips.csv")` → `tips_df` |
| 1.2.2 | Sutun Turkceles. | 7 sutun rename (age→yas, sex→cinsiyet...) | 7 sutun rename (total_bill→toplamHesap...) |
| 1.2.3 | Category Donusum | `cinsiyet`, `sigaraDurum`, `bolge` → category | `cinsiyet`, `sigaraDurum`, `gun`, `ogun` → category |
| 1.2.4 | Kategorik Deger Guncelleme | male→erkek, yes→evet, southeast→guneydogu... | Male→erkek, Yes→evet, Sun→pazar... |
| 1.3 | Ozet Istatistikler | `describe()`, `describe(include="all")` | `describe()`, `describe(include="all")` |
| 1.4.1 | Cizgi Grafik | 4 ornek: VKI, yas, karsilastirma, grid | 4 ornek: bahsis, toplamHesap, karsilastirma, grid |
| 1.4.2 | Bar Grafikleri | 2 ornek: dikey (sigaraDurum→odemeMiktari), yatay | 2 ornek: dikey (sigaraDurum→bahsis), yatay |
| 1.4.3 | Pasta Grafigi | 1 ornek: bolge→odemeMiktari | 1 ornek: gun→bahsis |
| 1.4.4 | Scatter Plot | 3 ornek: yas-vki, yas-odeme(hue=sigara), secili | 3 ornek: toplamHesap-bahsis, hue=sigara, secili |
| 1.4.5 | Histogram | 2 ornek: vki (8 bin, 12 bin) | 2 ornek: toplamHesap (8 bin, 12 bin) |

### 1Q Gorev Listesi (17 GOREV)

| GOREV | Bolum | Aciklama |
|-------|-------|----------|
| 1 | 1.2.1 | tips.csv oku, tips_df degiskenine ata |
| 2 | 1.2.2 | Sutun isimlerini Turkcelestitr |
| 3 | 1.2.3 | Veri tiplerini ekrana yazdir |
| 4 | 1.2.3 | cinsiyet, sigaraDurum, gun, ogun → category |
| 5 | 1.2.4 | Kategorik degerleri Turkcelestitr |
| 6 | 1.3 | describe() ile ozet istatistikler |
| 7 | 1.4.1 | Ilk 20 musterinin bahsis cizgi grafigi |
| 8 | 1.4.1 | 40-60 musteri toplam hesap cizgi grafigi |
| 9 | 1.4.1 | Ilk 20 vs 21-40 bahsis karsilastirmasi |
| 10 | 1.4.1 | Ilk 50 musteri toplam hesap + grid |
| 11 | 1.4.2 | sigaraDurum→bahsis dikey bar grafigi |
| 12 | 1.4.2 | Ayni veri yatay bar grafigi |
| 13 | 1.4.3 | gun→bahsis pasta grafigi |
| 14 | 1.4.4 | toplamHesap-bahsis scatter plot |
| 15 | 1.4.4 | Scatter + hue=sigaraDurum |
| 16 | 1.4.4 | Secili musteriler scatter |
| 17 | 1.4.5 | toplamHesap histogram (8 bin + 12 bin) |

---

## Diger Dosyalar

| Dosya | Aciklama |
|-------|----------|
| `1_veri_gorsellestirme.md` | Ders notebookunun markdown (duz metin) versiyonu — kod, cikti ve aciklamalar dahil |

---

## Ogrenme Hedefleri

- CSV dosyasi okuma: `pd.read_csv()`
- Sutun yeniden adlandirma: `.rename(columns={...})`
- Kategorik tip donusumu: `.astype("category")`
- Kategorik deger guncelleme: `.cat.rename_categories({...})`
- Betimsel istatistik: `.describe()`, `.describe(include="all")`
- Grafik turleri:
  - **Cizgi grafigi:** `plt.plot()` — trend, karsilastirma, grid
  - **Cubuk grafigi:** `plt.bar()`, `plt.barh()` — dikey, yatay
  - **Pasta grafigi:** `plt.pie()` — oran/yuzde dagilimi
  - **Dagilim grafigi:** `plt.scatter()`, `sns.scatterplot()` — iliski, hue
  - **Histogram:** `sns.histplot()` — frekans dagilimi, bin sayisi

---

## Kullanilan Kutuphaneler

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

## Colab Ortami

- Ders veri yolu: `/content/drive/MyDrive/Colab Notebooks/insurance.csv`
- Cevap/Gorev veri yolu: `/content/drive/MyDrive/Colab Notebooks/tips.csv`
- Drive baglantisi: `drive.mount('/content/drive')`
- Lokal kullanim icin: `insurance.csv` ve `tips.csv` bu klasorde mevcuttur

---

## Yeni Notebook Olusturma Rehberi (AI Icin)

Eger yeni bir hafta icin benzer notebooklar olusturmaniz gerekiyorsa:

1. **Ders notebookunu** (`N_konu.ipynb`) okuyun — veri seti, bolum yapisi, kullanilan teknikler
2. **Benzer veri seti bulun** — ayni domain, benzer sutun yapisi, Kaggle/UCI'dan
3. **Cevap anahtari olusturun** (`NA_konu.ipynb`) — ders ile birebir ayni bolum sirasi, farkli veri seti
4. **Gorev notebooku olusturun** (`NQ_konu.ipynb`) — cevap anahtarindan turetilir, kod hucreleri bosaltilir, `# GOREV:` yorumlari eklenir, kutuphane import hucresi korunur

---

## Ders Kitabi Referansi: Makine Ogrenmesi — Bolum 3: Python ile Veri Gorsellestirme

> **Kaynak:** `docs/makine_ogrenmesi.md` (Zuber Dogan — Yeditepe Universitesi Meslek Yuksek Okulu)

### Bolum Kazanimlari

1. Veri gorsellestirmenin onemini anlar, farkli gorsellestirme tekniklerinin projelerde nasil kullanilabilecegini bilir.
2. **Cizgi grafigi** (line chart) kullanim alanlarini anlar, Python ile cizgi grafigi cizebilir.
3. **Sutun grafigi** (bar chart) kullanarak kategorik verileri gorsellestirebilir.
4. **Pasta grafigi** (pie chart) ile oranlari ve yuzdeleri temsil edebilir.
5. **Serpilme diyagrami** (scatter plot) ile iki degisken arasindaki iliskiyi gorsellestirebilir.
6. **Histogram** ile veri setindeki frekans dagilimini gosterebilir.
7. **Kutu grafigi** (box plot) ile aykiri degerleri tespit edebilir.
8. **Violin grafigi** ile bir niteligin dagilimini gorsellestirebilir.
9. **Isi haritasi** (heatmap) ile nitelikler arasindaki iliskileri analiz edebilir.

### Bu Hafta ile Ders Kitabi Iliskisi

| Ders Kitabi (Bolum 3) | Notebook Karsiligi |
|------------------------|---------------------|
| Cizgi Grafigi (3.2) | Bolum 1.4.1 — `plt.plot()` |
| Sutun Grafigi (3.3) | Bolum 1.4.2 — `plt.bar()`, `plt.barh()` |
| Pasta Grafigi (3.4) | Bolum 1.4.3 — `plt.pie()` |
| Serpilme Diyagrami (3.5) | Bolum 1.4.4 — `plt.scatter()`, `sns.scatterplot()` |
| Histogram (3.6) | Bolum 1.4.5 — `sns.histplot()` |

### Hangi Grafik Turu Ne Zaman Kullanilir?

| Grafik Turu | Kullanim Alani | Veri Tipi | Ornek |
|-------------|---------------|-----------|--------|
| **Cizgi Grafigi** | Zaman serisi, sirali veri trendi | Surekli sayisal | Musteri yaslarinin sirali goruntusu |
| **Sutun Grafigi** | Kategorik karsilastirma | Kategorik + sayisal | Sigara icenlerin ortalama bahsisi |
| **Pasta Grafigi** | Oran/yuzde dagilimi | Kategorik | Gunlere gore toplam bahsis dagilimi |
| **Serpilme Diyagrami** | Iki degisken iliskisi | Iki surekli sayisal | Toplam hesap vs. bahsis iliskisi |
| **Histogram** | Frekans dagilimi, yogunluk | Surekli sayisal | Bahsis miktari dagilimi |
| **Kutu Grafigi** | Ceyrekler, aykiri degerler | Surekli sayisal | Yas dagilimi, medyan, Q1, Q3 |
| **Violin Grafigi** | Yogunluk + dagilim | Surekli sayisal | Bahsis dagiliminin detayli gorunumu |
| **Isi Haritasi** | Coklu degisken iliskisi | Matris/korelasyon | Nitelikler arasi korelasyon matrisi |
