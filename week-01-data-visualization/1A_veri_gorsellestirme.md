---
# GOOGLE NOTEBOOKLM PROMPT — BU BOLUMU OKUYARAK BASLA
---

> **Bu dokuman, universite duzeyinde bir veri bilimi dersinin ders notudur.**
> Amac: Bu icerikten **sunum (PPTX)**, **video ders (MP4)** ve **sesli anlatim (MPA/podcast)** uretmektir.
>
> **Hedef kitle:** Bilgisayar bilimi / yazilim muhendisligi 2. sinif ogrencileri. Python bilgisi temel duzey.
>
> **Uretim kurallari:**
> 1. **Her bolum bir slayt/sahne olsun.** Basliklar (`##`) slayt basliklarini, alt basliklar (`###`) slayt icerigini tanimlar.
> 2. **Kod bloklari gosterilmeli.** Her kod blogunu once goster, sonra satirlarin ne yaptigini kisa ve net acikla.
> 3. **Ciktilar/tablolar ekle.** Kodun urettigi ciktiyi goster — ogrenci "bu kodu calistirinca ne olacak?" sorusunu gormeli.
> 4. **Gorsellestirme adimlarina ozel onem ver.** Grafik turleri (cizgi, bar, pasta, scatter, histogram) icin:
>    - Grafigin amacini 1 cumle ile acikla
>    - Hangi degiskenlerin kullanildigini belirt
>    - Grafigin nasil yorumlanacagini ogret
> 5. **Istatistik yorumlari anlat.** Ortalama, standart sapma, min/max degerlerini gercek hayat baglamiyla acikla.
> 6. **Turkce anlatim tonu kullan.** Resmi ama samimi, ogretici, motivasyon verici.
> 7. **Veri seti bilgisi:** Bu derste `tips.csv` (restoran bahsis verisi, 244 satir, 7 sutun) kullanilmaktadir.
>    Sutunlar: `total_bill` (toplam hesap), `tip` (bahsis), `sex` (cinsiyet), `smoker` (sigara durumu), `day` (gun), `time` (ogun), `size` (kisi sayisi).
> 8. **Podcast/sesli anlatim icin:** Kod satirlarini okurken fonksiyon isimlerini acikla (ornegin: "pe-de nokta read_csv fonksiyonu dosyayi okur"), degisken isimlerini Turkce soyle.
> 9. **Sunum akisi:** Giris → Kutuphane → Veri Yukleme → Veri Duzenleme → Istatistikler → Gorsellestirme (5 grafik turu) → Ozet

---

# **1. Python ile Veri Gorsellestirme (Tips Veri Seti)**

Bu derste, Python kullanarak veri gorsellestirme tekniklerini uygulamali olarak ogrenecegiz. Restoran bahsis veri seti (tips.csv) uzerinden veri setinin yuklenmesi, sutun isimlerinin Turkcelesstirilmesi, veri tiplerinin duzenlenmesi ve cesitli grafiklerin (cizgi, bar, scatter, histogram, pasta) olusturulmasi adimlarini inceleyecegiz.

---

## Veri Seti Tanitimi: tips.csv

Bu derste kullandigimiz veri seti, bir restoranda toplanan **244 musteri kaydini** icerir.

| Sutun | Turkce Karsiligi | Veri Tipi | Aciklama |
|-------|-----------------|-----------|----------|
| `total_bill` | `toplamHesap` | float64 | Toplam hesap miktari ($) |
| `tip` | `bahsis` | float64 | Birakilan bahsis miktari ($) |
| `sex` | `cinsiyet` | object → category | `Male` → `erkek`, `Female` → `kadin` |
| `smoker` | `sigaraDurum` | object → category | `Yes` → `evet`, `No` → `hayir` |
| `day` | `gun` | object → category | `Sun` → `pazar`, `Sat` → `cumartesi`, `Thur` → `persembe`, `Fri` → `cuma` |
| `time` | `ogun` | object → category | `Lunch` → `ogle`, `Dinner` → `aksam` |
| `size` | `kisiSayisi` | int64 | Masadaki kisi sayisi |

**Ornek veriler (ilk 5 satir):**

| total_bill | tip  | sex    | smoker | day | time   | size |
|-----------|------|--------|--------|-----|--------|------|
| 16.99     | 1.01 | Female | No     | Sun | Dinner | 2    |
| 10.34     | 1.66 | Male   | No     | Sun | Dinner | 3    |
| 21.01     | 3.50 | Male   | No     | Sun | Dinner | 3    |
| 23.68     | 3.31 | Male   | No     | Sun | Dinner | 2    |
| 24.59     | 3.61 | Female | No     | Sun | Dinner | 4    |

---

## 1.1 Google Drive Baglantisi ve Kutuphane Yukleme

### Neden Kutuphane Yukluyoruz?
Python'da veri analizi ve gorsellestirme yapmak icin hazir kutuphaneler kullaniyoruz. Bu kutuphaneler binlerce satir kodu tek bir komutla kullanmamizi saglar.

### Kullanilan Kutuphaneler ve Aciklamalari

- **`numpy`** — Sayisal hesaplamalar ve matris islemleri icin kullanilir. Ornegin: diziler olusturma, matematiksel islemler.
- **`pandas`** — Veri isleme, analiz ve veri cerceveleri (DataFrame) ile calisma imkani sunar. CSV dosyalarini okumak icin kullanilir.
- **`matplotlib`** — Grafik ve veri gorsellestirme icin temel kutuphanelerden biridir. Cizgi, bar, pasta grafikleri cizdirilebilir.
- **`seaborn`** — Daha gelismis ve estetik veri gorsellestirme icin matplotlib'in uzerine insa edilmistir.
- **`sklearn`** (scikit-learn) — Veri on isleme, modelleme ve degerlendirme araclari icerir.
- **`yellowbrick`** — Makine ogrenmesi modellerinin gorsellestirilmesini saglayan bir kutuphane.

```python
# Gerekli kutuphanelerin yuklenmesi
!pip install -q numpy pandas scikit-learn matplotlib seaborn yellowbrick

# Kutuphanelerin iceri aktarilmasi
import numpy as np                # Sayisal hesaplamalar ve diziler icin
import pandas as pd               # Veri cerceveleri ile calismak icin
import matplotlib.pyplot as plt   # Grafik cizimi icin
import seaborn as sns             # Gelismis veri gorsellestirme icin

# Ek moduller ve sklearn fonksiyonlari
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from yellowbrick.cluster import SilhouetteVisualizer

from google.colab import drive
drive.mount('/content/drive')       # Google Drive'a baglanmayi saglar (Colab).
```

> **Not:** `drive.mount()` komutu yalnizca Google Colab ortaminda calisir. Lokal ortamda bu satiri atlayabilirsiniz.

---

## 1.2 Tips (Bahsis) Veri Setinin Yuklenmesi ve Temel Islemler

Bu bolumde yapacaklarimiz:
1. `tips.csv` dosyasini okuyacagiz
2. Sutun isimlerini Turkcelesstirecegiz
3. Kategorik sutunlari `category` tipine donusturecegiz
4. Kategorik degerleri Turkce'ye cevirecegiz
5. Ozet istatistikleri inceleyecegiz

---

### 1.2.1 Veri Setini Okuma

```python
# Veri setini Google Drive'dan okuyoruz
# Pandas DataFrame formatina ceviriyoruz
# ve 'tips_df' isimli degiskene atiyoruz
tips_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tips.csv')

# 'dtypes' Her sutunun veri tipini gosterir
print(tips_df.dtypes)

# Ilk 5 satiri goruntuleyerek veri setine goz atalim
display(tips_df.head())
```

**Cikti:**
```
total_bill    float64
tip           float64
sex            object
smoker         object
day            object
time           object
size            int64
dtype: object
```

> **Yorum:** `sex`, `smoker`, `day`, `time` sutunlari `object` tipinde gorunuyor. Bunlari `category` tipine donusturecegiz.

---

### 1.2.2 Sutun Isimlerini Turkceslestirme

```python
# Ingilizce sutun isimlerini Turkceye ceviriyoruz
# DataFrame.rename(columns={...}): Sutun adlarini degistirmemizi saglar.

tips_df = tips_df.rename(columns={
    "total_bill": "toplamHesap",
    "tip": "bahsis",
    "sex": "cinsiyet",
    "smoker": "sigaraDurum",
    "day": "gun",
    "time": "ogun",
    "size": "kisiSayisi"
})

# Degisiklikleri dogrulamak icin ilk 5 satiri tekrar gozlemleyelim
tips_df.head()
```

**Eslestirme tablosu:**

| Orijinal | Turkce | Aciklama |
|----------|--------|----------|
| `total_bill` | `toplamHesap` | Musteri toplam hesabi |
| `tip` | `bahsis` | Birakilan bahsis |
| `sex` | `cinsiyet` | Musteri cinsiyeti |
| `smoker` | `sigaraDurum` | Sigara icme durumu |
| `day` | `gun` | Ziyaret edilen gun |
| `time` | `ogun` | Ogun (ogle/aksam) |
| `size` | `kisiSayisi` | Masadaki kisi sayisi |

---

### 1.2.3 `object` Kategorik Sutunlari → `category` Veri Tipine Donusturme

#### Neden `category` Tipine Donusturuyoruz?

**1. Bellek Kullanimini Azaltir**
- `object` veri tipi, her hucre icin ayri ayri metin (string) saklar ve fazla yer kaplar.
- `category` tipi, tekrar eden degerleri hafizada tek bir kez saklayarak daha az bellek kullanir.

**2. Islem Verimliligini Artirir**
- Makine ogrenmesi ve veri analizi islemlerinde kategorik degiskenler genellikle numerik olarak islenir.
- `category` veri tipi, islemleri hizlandirir cunku daha hizli karsilastirma ve gruplama yapabilir.

**3. Veri Analizini Kolaylastirir**
- Kategorik degiskenlerin siniflarini (`.cat.categories`) ve frekanslarini (`.value_counts()`) daha kolay analiz edebilirsiniz.

```python
# Sutunlarin ilk veri tiplerini kontrol etme
print("Ilk veri tipleri:")
print(tips_df.dtypes)
```

**Cikti:**
```
Ilk veri tipleri:
toplamHesap     float64
bahsis          float64
cinsiyet         object
sigaraDurum      object
gun              object
ogun             object
kisiSayisi        int64
dtype: object
```

```python
# astype('category'): Nesnel (object) tipindeki sutunlari kategorik tipine cevirerek
# bellek kullanimini ve islem verimliligini artirir.

tips_df["cinsiyet"] = tips_df["cinsiyet"].astype("category")
tips_df["sigaraDurum"] = tips_df["sigaraDurum"].astype("category")
tips_df["gun"] = tips_df["gun"].astype("category")
tips_df["ogun"] = tips_df["ogun"].astype("category")

# Donusum sonrasi veri tiplerini kontrol etmek icin:
print("\nDonusturme sonrasi veri tipleri:")
print(tips_df.dtypes)
```

**Cikti:**
```
Donusturme sonrasi veri tipleri:
toplamHesap     float64
bahsis          float64
cinsiyet       category
sigaraDurum    category
gun            category
ogun           category
kisiSayisi        int64
dtype: object
```

> **Yorum:** `cinsiyet`, `sigaraDurum`, `gun`, `ogun` sutunlari artik `category` tipinde. Bu hem bellek tasarrufu saglar hem de gruplama islemlerini hizlandirir.

---

### 1.2.4 Kategorik Degerleri Guncelleme (Ingilizce → Turkce)

`.cat.rename_categories({...})`: Kategorik sutun degerlerini yeniden adlandirir.

```python
# Kategorik degerlerin Turkcelesstirilmesi
tips_df["cinsiyet"] = tips_df["cinsiyet"].cat.rename_categories({"Male": "erkek", "Female": "kadin"})
tips_df["sigaraDurum"] = tips_df["sigaraDurum"].cat.rename_categories({"No": "hayir", "Yes": "evet"})
tips_df["gun"] = tips_df["gun"].cat.rename_categories({
    "Sun": "pazar", "Sat": "cumartesi", "Thur": "persembe", "Fri": "cuma"
})
tips_df["ogun"] = tips_df["ogun"].cat.rename_categories({"Lunch": "ogle", "Dinner": "aksam"})

# Degisiklikleri gormek icin
tips_df.head(10)
```

**Donusum tablosu:**

| Sutun | Orijinal | Turkce |
|-------|----------|--------|
| cinsiyet | `Male` / `Female` | `erkek` / `kadin` |
| sigaraDurum | `No` / `Yes` | `hayir` / `evet` |
| gun | `Sun` / `Sat` / `Thur` / `Fri` | `pazar` / `cumartesi` / `persembe` / `cuma` |
| ogun | `Lunch` / `Dinner` | `ogle` / `aksam` |

---

## 1.3 Veri Setinin Ozet Istatistikleri

```python
print("\nSayisal ozet (describe):")
# describe(): Sayisal sutunlar icin istatistiksel ozet (ortalama, std, min, max vb.) verir.
print(tips_df.describe())

pd.set_option("display.max_columns", 20)
print("\nTum sutun ozet bilgisi:")
# describe(include='all'): Kategorik sutunlari da ozetleyerek benzersiz deger sayisi,
# en sik gorulen deger vb. bilgileri gosterir.
print(tips_df.describe(include="all"))
```

**Cikti (sayisal ozet):**

|          | toplamHesap | bahsis | kisiSayisi |
|----------|-----------|--------|------------|
| count    | 244.00    | 244.00 | 244.00     |
| mean     | 19.79     | 3.00   | 2.57       |
| std      | 8.90      | 1.38   | 0.95       |
| min      | 3.07      | 1.00   | 1.00       |
| 25%      | 13.35     | 2.00   | 2.00       |
| 50%      | 17.80     | 2.90   | 2.00       |
| 75%      | 24.13     | 3.56   | 3.00       |
| max      | 50.81     | 10.00  | 6.00       |

---

## 1.3 Veri Setinin Istatistik Aciklamalari

### Toplam Hesap Dagilimi
- **En dusuk hesap:** 3.07$
- **En yuksek hesap:** 50.81$
- **Ortalama hesap:** ~19.79$
- **Standart sapma:** ~8.90$

> **Yorum:** Musterilerin buyuk cogunlugu (~%68) **10.89$ ile 28.69$** arasinda hesap odemektedir. Bu aralik ortalama +/- 1 standart sapmadir.

---

### Bahsis Dagilimi
- **En dusuk bahsis:** 1.00$
- **En yuksek bahsis:** 10.00$
- **Ortalama bahsis:** ~3.00$
- **Standart sapma:** ~1.38$

> **Yorum:** Musterilerin buyuk cogunlugu (~%68) **1.62$ ile 4.38$** arasinda bahsis birakmaktadir.

---

### Kisi Sayisi
- **Minimum kisi sayisi:** 1
- **Maksimum kisi sayisi:** 6
- **Ortalama kisi sayisi:** ~2.57

> **Yorum:** Masalarin cogu **2-3 kisilik**tir.

---

### Cinsiyet Dagilimi
- **Erkek musteri sayisi:** 157
- **Kadin musteri sayisi:** 87

> **Yorum:** Musterilerin **%64'u erkektir**.

---

### Sigara Icme Durumu
- **Sigara icmeyen musteri sayisi:** 151
- **Sigara icen musteri sayisi:** 93

> **Yorum:** Musterilerin **%62'si sigara icmiyor**.

---

### Gun Dagilimi
- **En yogun gun:** Cumartesi — **87 musteri**
- Diger gunler: Pazar (76), Persembe (62), Cuma (19)

> **Yorum:** Hafta sonu gunleri (Cumartesi ve Pazar) en yogun zamanlardir.

---

### Ogun Dagilimi
- **Aksam yemegi musteri sayisi:** 176
- **Ogle yemegi musteri sayisi:** 68

> **Yorum:** Musterilerin **%72'si aksam yemeginde** gelmektedir.

---

## 1.4 Veri Gorsellestirme (Tips)

Bu bolumde 5 farkli grafik turu ogrenecegiz:
1. **Cizgi Grafik** (Line Plot) — trend ve degisim gosterir
2. **Bar Grafikleri** (Bar Chart) — kategorik karsilastirma yapar
3. **Pasta Grafigi** (Pie Chart) — oran/yuzde dagilimini gosterir
4. **Serpilme Diyagrami** (Scatter Plot) — iki degisken arasindaki iliskiyi gosterir
5. **Histogram** — frekans dagilimini gosterir

---

### 1.4.1 Cizgi Grafik (Line Plot)

Cizgi grafik, verinin sirasiyla nasil degistigini gostermek icin kullanilir. Ozellikle zaman serisi veya sirali verilerde etkilidir.

---

**Ornek 1:** Ilk 20 musterinin bahsis degerlerini cizgi grafik ile gorsellestirme.

```python
x_line = np.arange(1, 21)  # Musteri ID'leri 1'den 20'ye
y_line = tips_df.iloc[0:20, 1]  # Ilk 20 musterinin bahsis sutunu (index 1)

plt.figure()
plt.plot(x_line, y_line, linestyle="dashed", color="hotpink", linewidth=5)
plt.title("Ilk 20 Musterinin Bahsis Degerleri")
plt.xlabel("Musteri ID")
plt.ylabel("Bahsis")
plt.show()
```

> **Yorum:** Bu grafik ilk 20 musterinin biraktigi bahsis miktarini sirasiyla gosterir. Kesikli cizgi stili (`dashed`) ve pembe renk (`hotpink`) kullanilmistir.

---

**Ornek 2:** 40-60. Musterilerin Toplam Hesap Dagilimi

```python
x_line = np.arange(40, 61)
y_line = tips_df.iloc[40:61, 0]  # Dizi boyutunu esitlemek icin 40:61 kullanildi

plt.figure()
plt.plot(x_line, y_line, color="blue", linewidth=3)
plt.title("40-60. Musterinin Toplam Hesap Dagilimi")
plt.xlabel("Musteri ID")
plt.ylabel("Toplam Hesap")
plt.show()
```

> **Yorum:** 40 ile 60 arasindaki musterilerin toplam hesap degerlerini gosterir. Bu tur grafik, belirli bir aralikta verinin nasil degistigini gormek icin kullanilir.

---

**Ornek 3:** Ilk 20 ile 21-40 arasindaki musterilerin bahsis degerlerinin karsilastirilmasi.

```python
x_line2 = np.arange(1, 21)        # X ekseni icin 1'den 20'ye kadar degerler
y1 = tips_df.iloc[0:20, 1]        # Ilk 20 musterinin bahsis verisi
y2 = tips_df.iloc[20:40, 1]       # Sonraki 20 musterinin bahsis verisi (21-40. satirlar)

plt.figure()                       # Yeni bir grafik figuru olustur
plt.xticks(x_line2)                # X ekseninde 1'den 20'ye kadar tam sayilari goster
plt.plot(x_line2, y1, label="Ilk 20")      # Ilk 20 musteri icin cizgi grafigi
plt.plot(x_line2, y2, label="Ikinci 20")   # Ikinci 20 musteri icin cizgi grafigi

plt.title("Bahsis Karsilastirmasi")  # Grafiğe baslik ekle
plt.legend()                         # Aciklama kutusu (legend) ekle
plt.tight_layout(pad=1)              # Grafik duzenini optimize et
plt.show()
```

> **Yorum:** Iki farkli musteri grubunun bahsis miktarlarini ayni grafik uzerinde karsilastiriyoruz. `legend()` fonksiyonu her cizginin hangi gruba ait oldugunu gosterir.

---

**Ornek 4:** Ilk 50 musterinin toplam hesap dagiliminin cizgi grafigi.

```python
x_bill = np.arange(1, 51)            # 1'den 50'ye kadar musteri ID'leri
y_bill = tips_df.iloc[0:50, 0]       # Ilk 50 musterinin toplam hesap bilgileri (0. sutun)

plt.figure()
plt.title("Ilk 50 Musterinin Toplam Hesabi")
plt.xlabel("Musteri ID")
plt.ylabel("Toplam Hesap")

plt.plot(x_bill, y_bill)
plt.grid(color="red", linestyle="solid", linewidth=0.5)  # Kirmizi izgara cizgileri ekle

plt.show()
```

> **Yorum:** `plt.grid()` fonksiyonu, grafige izgara cizgileri ekleyerek verilerin okunmasini kolaylastirir.

---

### 1.4.2 Bar Grafikleri

Bar grafikleri, kategorik verileri karsilastirmak icin idealdir. Dikey (`plt.bar()`) ve yatay (`plt.barh()`) versiyonlari vardir.

---

**Ornek 1:** Sigara icme durumuna gore ortalama bahsis miktarinin bar grafigi.

```python
# Sigara icme durumuna gore ortalama bahsis miktarini hesapla
ozet = tips_df.groupby("sigaraDurum", observed=True)["bahsis"].mean()
        # - groupby("sigaraDurum"): Veriyi sigara durumuna gore gruplar
        # - ["bahsis"].mean(): Her grup icin ortalama bahsis hesaplar

plt.figure()

plt.bar(x=ozet.index, height=ozet.values, color="r")
        # Dikey cubuk grafigi ciz
        # - x=ozet.index: Kategorik degerler (hayir/evet)
        # - height=ozet.values: Cubuk yukseklikleri (ortalama bahsis)
        # - color="r": Kirmizi renk

plt.xlabel("Sigara Icme Durumu")
plt.ylabel("Ortalama Bahsis Miktari")
plt.title("Sigara Durumuna Gore Bahsis Miktari")
plt.show()
```

> **Yorum:** Sigara icen musterilerin ortalama bahsis miktari ile icmeyenlerin karsilastirilir. `groupby()` fonksiyonu veriyi gruplarken, `mean()` ortalama hesaplar.

---

**Ornek 2:** Yatay bar grafigi.

```python
plt.figure()

# Yatay cubuk grafigi ciz
plt.barh(y=ozet.index, width=ozet.values, color="b")
      # - y=ozet.index: Kategorik degerler
      # - width=ozet.values: Cubuk uzunluklari
      # - color="b": Mavi renk

plt.xlabel("Bahsis Miktari")
plt.title("Yatay Bar Grafigi")
plt.show()
```

> **Yorum:** Yatay bar grafigi, ozellikle kategori isimleri uzun oldugunda tercih edilir. `plt.barh()` fonksiyonu kullanilir (`h` = horizontal = yatay).

---

### 1.4.3 Pasta Grafigi (Pie Chart)

Pasta grafigi, bir butunun parcalara ayrilmasini gostermek icin kullanilir. Her dilim, toplamin yuzde kacini olusturdugunu gosterir.

---

**Ornek:** Gune gore toplam bahsis miktarini gosteren pasta grafigi.

```python
# "gun" sutununa gore gruplandirarak her gundeki toplam bahsis miktarini hesapla
ozet_gun = tips_df.groupby("gun", observed=True)["bahsis"].sum()
        # - groupby("gun"): Veriyi gunlere gore gruplar
        # - ["bahsis"].sum(): Her gun icin toplam bahsis hesaplar

etiketler = ozet_gun.index   # Pasta grafigi icin gun isimleri
degerler = ozet_gun.values   # Pasta dilimlerinin buyuklugu
renkler = sns.color_palette("viridis", len(etiketler))  # Renk paleti
explode_vals = [0] * len(etiketler)   # Baslangicta tum dilimleri normal goster

# Ucuncu dilimi patlat (grafigkte one cikarmak icin)
if len(etiketler) >= 3:
    explode_vals[2] = 0.2

plt.figure()

plt.pie(
    degerler,               # Pasta dilimlerinin buyuklugu
    explode=explode_vals,   # Hangi dilimler one cikarilacak
    labels=etiketler,       # Dilimlerin etiketleri (gun isimleri)
    autopct="%4.1f%%",      # Dilimlerin yuzdesini goster
    shadow=True,            # Golgeli efekt ekle
    startangle=360,         # Grafigi 360 dereceden baslat
    colors=renkler           # Dilimler icin renk paletini uygula
)

plt.title("Gune Gore Toplam Bahsis Miktari")
plt.show()
```

> **Yorum:** Hangi gunde daha fazla bahsis birakildigi gorulebilir. `explode` parametresi bir dilimi one cikararak vurgu saglar. `autopct` her dilimin yuzdesini gosterir.

---

### 1.4.4 Serpilme/Dagilim Plot (Scatter Plot)

Scatter plot, iki sayisal degisken arasindaki iliskiyi gormek icin kullanilir. Her nokta bir gozlemi temsil eder.

---

**Ornek 1:** Toplam hesap ile bahsis arasindaki iliski.

```python
plt.figure()

# Toplam hesap ve bahsis arasindaki iliskiyi gosteren sacilim grafigi
plt.scatter(tips_df["toplamHesap"], tips_df["bahsis"])
      # - tips_df["toplamHesap"]: X ekseni icin toplam hesap verileri
      # - tips_df["bahsis"]: Y ekseni icin bahsis verileri
      # - plt.scatter(): Her veri noktasini bir nokta olarak cizer

plt.xlabel("Toplam Hesap")
plt.ylabel("Bahsis")
plt.title("Toplam Hesap ve Bahsis Iliskisi")
plt.show()
```

> **Yorum:** Noktalar sag uste dogru yigiliyorsa, toplam hesap arttikca bahsis de artma egilimindedir — **pozitif korelasyon** vardir.

---

**Ornek 2:** Toplam hesap ve bahsis miktari (Sigara Durumuna Gore)

```python
plt.figure()

# Seaborn ile scatter plot — sigara durumuna gore renklendirme
sns.scatterplot(x="toplamHesap", y="bahsis", hue="sigaraDurum", data=tips_df)
      # - x="toplamHesap": X eksenine toplam hesap
      # - y="bahsis": Y eksenine bahsis
      # - hue="sigaraDurum": Sigara durumuna gore renklendirme
      # - data=tips_df: Veri kaynagi

plt.title("Toplam Hesap ve Bahsis (Sigara Durumuna Gore)")
plt.show()
```

> **Yorum:** `hue` parametresi, ucuncu bir kategorik degiskeni renk ile grafige ekler. Boylece sigara icen ve icmeyen musterilerin bahsis davranilarini ayni grafik uzerinde karsilastirabiliriz.

---

**Ornek 3:** Secili musterilerin toplam hesap ve bahsis miktari

```python
# Secili musterilerin indeks numaralarini iceren liste
secim = [200, 150, 100, 50, 10, 180, 120, 80, 30, 230]

# Secilen indekslerin veri cercevesinin sinirlarini asmadigini kontrol et
secim = [i for i in secim if i < len(tips_df)]

# Secili musterilerin toplam hesap ve bahsis bilgilerini iceren alt veri kumesi
altkume = tips_df.iloc[secim][["toplamHesap", "bahsis"]]

plt.figure()

plt.scatter(altkume["toplamHesap"], altkume["bahsis"])

plt.xlabel("Toplam Hesap")
plt.ylabel("Bahsis")
plt.title("Secili Musterilerin Toplam Hesap ve Bahsis Miktari")
plt.show()
```

> **Yorum:** Belirli musterileri secip sadece onlari gorsellestirmek, detayli analiz icin kullanislidir. `iloc[secim]` ile indekse gore satirlar secilir.

---

### 1.4.5 Histogram

Histogram, bir sayisal degiskenin frekans dagilimini gosterir. X ekseni deger araliklarini (bin), Y ekseni o araliktaki gozlem sayisini gosterir.

---

**Ornek:** Toplam hesap dagilimini 8 ve 12 bin'li histogram ile gorsellestirme.

```python
plt.figure()
# Toplam hesap dagilimini gosteren histogram (8 bin)
sns.histplot(data=tips_df, x="toplamHesap", color="yellow", bins=8)
        # - data=tips_df:       Veriyi secer
        # - x="toplamHesap":    X ekseninde toplam hesap degerleri
        # - color="yellow":     Histogram sari renkte cizilir
        # - bins=8:             8 aralikli bin (sutun) olusturur

plt.title("Toplam Hesap Histogram (8 Bin)")
plt.show()


plt.figure()
# Toplam hesap dagilimini gosteren histogram (12 bin)
sns.histplot(data=tips_df, x="toplamHesap", color="darkblue", bins=12)
        # - color="darkblue":   Histogram koyu mavi renkte cizilir
        # - bins=12:            12 aralikli bin (sutun) olusturur

plt.title("Toplam Hesap Histogram (12 Bin)")
plt.show()


# Toplam hesap degiskeninin tanimlayici istatistikleri
print("Toplam Hesap icin describe:")
print(tips_df["toplamHesap"].describe())
```

**Cikti:**
```
Toplam Hesap icin describe:
count    244.000000
mean      19.785943
std        8.902412
min        3.070000
25%       13.347500
50%       17.795000
75%       24.127500
max       50.810000
Name: toplamHesap, dtype: float64
```

> **Yorum:**
> - **8 bin** kullanildiginda daha genel bir dagilim gorunur.
> - **12 bin** kullanildiginda daha detayli bir dagilim gorunur.
> - `bins` parametresini degistirerek histogramin cozunurlugunu ayarlayabilirsiniz.
> - Toplam hesap dagililimi **saga carpik (right-skewed)** gorunuyor: cogu deger 10-25$ arasinda yogunlasirken, 40$'in uzerinde cok az musteri var.

---

## Ozet

Bu derste ogrendiklerimiz:

| Konu | Fonksiyon / Yontem | Aciklama |
|------|-------------------|----------|
| CSV okuma | `pd.read_csv()` | Dosyayi DataFrame olarak yukle |
| Sutun yeniden adlandirma | `.rename(columns={...})` | Sutun isimlerini degistir |
| Kategorik tip donusumu | `.astype("category")` | Bellek ve hiz optimizasyonu |
| Kategorik deger guncelleme | `.cat.rename_categories({...})` | Degerleri Turkceletstir |
| Istatistik ozet | `.describe()` | Ortalama, std, min, max |
| Cizgi grafik | `plt.plot()` | Trend ve sirali veri |
| Bar grafik | `plt.bar()`, `plt.barh()` | Kategorik karsilastirma |
| Pasta grafik | `plt.pie()` | Oran/yuzde dagilimi |
| Scatter plot | `plt.scatter()`, `sns.scatterplot()` | Iki degisken iliskisi |
| Histogram | `sns.histplot()` | Frekans dagilimi |

### Anahtar Kavramlar
- **DataFrame:** Pandas'in temel veri yapisi — satir ve sutunlardan olusan bir tablo.
- **Kategorik degisken:** Sinirli sayida benzersiz degere sahip degisken (cinsiyet, gun, vb.).
- **Betimsel istatistik:** Veriyi ozetleyen sayisal degerler (ortalama, medyan, standart sapma).
- **Pozitif korelasyon:** Bir degisken artinca digeri de artma egiliminde olmasi.
- **Histogram bin sayisi:** Dagilimi ne kadar detayli gostermek istediginizi belirler.
