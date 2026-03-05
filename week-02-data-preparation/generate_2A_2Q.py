#!/usr/bin/env python3
"""
Generate 2A_veri_hazirlama.ipynb and 2Q_veri_hazirlama.ipynb
Following the exact pedagogical pattern of week-01:
  - 2_ uses auto-mpg.data (lecture)
  - 2A uses automobile.csv (answer key) 
  - 2Q is 2A with empty code cells + GÖREV comments
"""

import json
import copy

def make_cell(cell_type, source, cell_id=None):
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source.split("\n") if isinstance(source, str) else source
    }
    # Fix: join lines with newline for proper notebook format
    lines = source.split("\n") if isinstance(source, str) else source
    # Each line except the last should end with \n
    fixed = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            fixed.append(line + "\n")
        else:
            fixed.append(line)
    cell["source"] = fixed
    
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    if cell_id:
        cell["metadata"]["id"] = cell_id
    return cell


# ============================================================
# 2A NOTEBOOK CELLS
# ============================================================
cells_2A = []

# --- Cell 0: Title ---
cells_2A.append(make_cell("markdown", """# **2A_veri_hazirlama**"""))

# --- Cell 1: Library imports markdown ---
cells_2A.append(make_cell("markdown", """# **2.1 Gerekli Kutuphanelerin Yuklenmesi**

### Neden Onemli?
Veri on isleme asamasinda kullanilacak tum fonksiyonlari, grafik araclarini ve veri donusum araclarini bu kutuphaneler saglar.

### Bu bolumde ne yapacagiz?
- **`NumPy, pandas, seaborn, sklearn`** gibi paketleri import edecegiz.
- **Veri on isleme** sirasinda kullanacagimiz fonksiyonlari tanimlayacagiz."""))

# --- Cell 2: Library imports code ---
cells_2A.append(make_cell("code", """import numpy as np                 # Sayisal islemler
import pandas as pd                # Veri cerceveleri ile calisma
import seaborn as sns              # Veri gorsellestirme
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats  # Kutu grafigi istatistikleri
import random                      # Rastgele islemler
from random import sample          # Belirli bir listeden rastgele secim
from sklearn.model_selection import train_test_split  # Egitim/Test veri bolme
from sklearn.preprocessing import MinMaxScaler, StandardScaler  # Normalizasyon & standardizasyon


print("Gerekli kutuphaneler basariyla yuklendi.")"""))

# --- Cell 3: Separator ---
cells_2A.append(make_cell("markdown", """---

---

---"""))

# --- Cell 4: Data reading markdown ---
cells_2A.append(make_cell("markdown", """# **2.2 Veri Okuma**

### Neden Onemli?
Veriyi dogru bicimde okumak ve bir **`DataFrame`** haline getirmek, sonraki tum veri on isleme ve analiz adimlari icin kritik bir adimdir. Eger veri yanlis bir konumdan okunursa veya sutun basliklari hatali tanimlanirsa, ileriki asamalarda eksik ya da hatali sonuclar alabiliriz.

### Bu bolumde ne yapacagiz?
- Google Drive'i baglayarak **(`mount`)** veri setinin bulundugu klasore erisecegiz.

- **`automobile.csv`** dosyasini, pandas'in **`read_csv`** fonksiyonunu kullanarak okuyacagiz.
- Veri setinin sutun veri tiplerini **(`dtypes`)** inceleyecegiz.
- Ayrica **`head()`** fonksiyonuyla veri icerigine hizlica goz atacagiz."""))

# --- Cell 5: Data reading code ---
cells_2A.append(make_cell("code", """# 1) Google Drive'i mount ediyoruz
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# 2) 'automobile.csv' dosyasini, Colab Notebooks klasorunden tam yol ile okuyoruz
veriSeti = pd.read_csv(
    "/content/drive/MyDrive/Colab Notebooks/automobile.csv"  # Dosyanin tam yolu
)

# 3) Veri setinin boyutu ve sutun veri tipleri
print("Veri Seti Boyutu:", veriSeti.shape)
print("\\nSutun Veri Tipleri:\\n", veriSeti.dtypes)
display(veriSeti.head(10))"""))

# --- Cell 6: Separator ---
cells_2A.append(make_cell("markdown", """---

---

---"""))

# --- Cell 7: Missing data markdown ---
cells_2A.append(make_cell("markdown", """# **2.3 Eksik Veri Tamamlama (Missing Data Imputation)**

### Neden Onemli?
Eksik veriler, modelin dogrulugunu olumsuz etkileyebilir veya hata olusturabilir. Bu nedenle eksik verileri uygun yontemlerle doldurmak **(`imputation`)**, veri kalitesini artirir ve analiz veya makine ogrenmesi modellerinden daha guvenilir sonuclar elde etmemize yardimci olur.

### Bu bolumde ne yapacagiz?
- **`normalized_losses`** sutunundaki **'?'** karakterlerini **`NaN`'e** donusturecegiz.
- **`horsepower`** ve **`peak_rpm`** sutunlarindaki **'?'** karakterlerini de **`NaN`'e** donusturecegiz.
- Bu sutunlarin veri tipini sayisal **`(float64)`** haline getirecegiz.
- Eksik veri sayisini inceleyip, ortalama degerle dolduracagiz.
- **`fillna()`** metodu kullanimini ornek olarak gorecegiz."""))

# --- Cell 8: Missing data code ---
cells_2A.append(make_cell("code", """# On kontrol: '?' karakteri iceren sutunlari tespit edelim
for col in veriSeti.columns:
    soru_isareti = (veriSeti[col] == "?").sum()
    if soru_isareti > 0:
        print(f"{col} sutununda '?' sayisi: {soru_isareti}")

# 1) '?' karakterini NaN'e donusturme (tum ilgili sutunlar icin)
eksik_sutunlar = ["normalized_losses", "horsepower", "peak_rpm"]
for col in eksik_sutunlar:
    veriSeti.loc[veriSeti[col] == "?", col] = np.nan   # loc[] fonksiyonu, kosul ile belirtilen satirlara erismemizi saglar.

# 2) Ilgili sutunlarin tipini float64'e donusturme
for col in eksik_sutunlar:
    veriSeti[col] = veriSeti[col].astype("float64")     # astype("float64"), sutun tipini sayisal hale getirir.

# 3) Eksik veri sayisini (ilk kontrol) ekrana bastirma
print("\\nEksik Veri Sayisi (Once):\\n", veriSeti.isnull().sum())

# 4) fillna() metodu ile ortalama ile doldurma
for col in eksik_sutunlar:
    veriSeti[col] = veriSeti[col].fillna(veriSeti[col].mean().round(0))
    # mean().round(0), sutunun ortalamasini en yakin tam sayiya yuvarlar.

print("\\nEksik Veri Sayisi (Sonra):\\n", veriSeti.isnull().sum())"""))

# --- Cell 9: Separator ---
cells_2A.append(make_cell("markdown", """---

---

---"""))

# --- Cell 10: Binning markdown ---
cells_2A.append(make_cell("markdown", """# **2.4 Veri Ayiriklastirma (Binning / Discretization)**

### Neden Onemli?
- Surekli (sayisal) veriler, kategorik (gruplandirilmis) degerlere donusturulur.
- Bu donusumle, veriye yeni bir sutun eklenir veya mevcut sutun siniflara ayrilir.
- Amac: Sayisal degerleri daha anlamli ve genellenmis kategorilere indirgemektir.

Ornegin: `city_mpg` degiskeni;
- **21'in altinda** ise -> **Dusuk**
- **21 - 30 arasi** ise -> **Orta**
- **30 ve ustu** ise -> **Yuksek** olarak siniflandirilabilir.

Bu islem sonucunda:
- Veri setine **yeni bir kategorik sutun (ornegin: `durum`)** eklenir.
- Satir sayisi degismez; sadece her satir bir kategoriye atanir.

---

### Bu bolumde ne yapacagiz?
- `city_mpg` sutununu **Dusuk**, **Orta** ve **Yuksek** kategorilerine ayiracagiz.
- Dort farkli yontemle ayiriklastirma islemi gerceklestirecegiz:

I. Yontem:

 **1.** **`lambda` + `map()`** fonksiyonu ile manuel kosullu siniflandirma yapacagiz.

II. Yontem:

**2.1.** **`pd.cut()`** fonksiyonu ile **sabit aralik (fixed interval)** yontemi uygulayacagiz.
**2.2.** **`pd.qcut()`** fonksiyonu ile **esit frekans (quantile)** yontemi kullanacagiz.
**2.3.** **`pd.cut()`** fonksiyonu ile **esit genislik (equal interval)** yontemini uygulayacagiz.


Her yontemde amac, `city_mpg` degerlerini farkli siniflandirma stratejileriyle gruplandiirmak ve analizlerde kullanilabilecek kategorik yapilar olusturmaktir."""))

# --- Cell 11: Binning code ---
cells_2A.append(make_cell("code", """# ------------------------------------------------------------
# I. Yontem: lambda + map
# ------------------------------------------------------------
# lambda ifadesi, 'city_mpg' degerine gore kosullu atama yapar:
# - x < 21 ise "Dusuk"
# - 21 <= x < 30 ise "Orta"
# - x >= 30 ise "Yuksek" olarak etiketler.
veriSeti["durum"] = veriSeti.city_mpg.map(
    lambda x: "Dusuk" if x < 21 else ("Orta" if (x >= 21 and x < 30) else "Yuksek")
).astype("category")

print("Durum (lambda) dagilim:\\n", veriSeti.durum.value_counts())
print(f"\\n{'-'*82}\\n")

#----------------------------------------------------------------------------------
# II. Yontem:
#----------------------------------------------------------------------------------

# II.1: Yontem: Fixed (sabit) araliklarla bolme
bolmeKategorileri = ["Dusuk", "Orta", "Yuksek"]   # onceden belirlenmis sinirlar kullanilarak 'city_mpg' degerleri uc kategoriye ayrilir.
bolmeler = [12, 20.9, 29.9, 50]                   # Belirlenen sinirlar
veriSeti["durum"] = pd.cut(
    veriSeti["city_mpg"],
    bins=bolmeler,
    labels=bolmeKategorileri
)
print("Durum (fixed cut) dagilim:\\n", veriSeti.durum.value_counts())
print(f"\\n{'-'*82}\\n")

# II.2: Yontem: Equal Frequency (qcut)
durum_ef = pd.qcut(veriSeti["city_mpg"], q=3)        # 'city_mpg' degerleri yaklasik esit sayida gozlem icerecek sekilde uc gruba ayrilir.

print("Durum (Esit frekans) dagilim:\\n", durum_ef.value_counts())
print(f"\\n{'-'*82}\\n")

# II.3: Yontem: Equal Interval (esit genislik)
durum_ea = pd.cut(veriSeti["city_mpg"], bins=3)      # 'city_mpg' degerlerinin araligi esit genislikli uc dilime bolunur.
print("Durum (Esit genislik) dagilim:\\n", durum_ea.value_counts())
print(f"\\n{'-'*82}\\n")"""))

# --- Cell 12: Separator ---
cells_2A.append(make_cell("markdown", """---

---

---"""))

# --- Cell 13: Describe markdown ---
cells_2A.append(make_cell("markdown", """# **2.5 Veri Seti Ozeti (describe)**

### Neden Onemli?
Veri setinin genel istatistiksel ozelliklerini (ortalama, std, min, max vb.) gormek, veri hakkinda hizlica fikir sahibi olmamizi saglar. Hem sayisal hem de kategorik sutunlarin ozetini almak, veri analizinin sonraki adimlarini planlamada bize rehberlik eder.

### Bu bolumde ne yapacagiz?
- pd.set_option("display.max_columns", 20) ayariyla, DataFrame ekrana basilirken en fazla kac sutun gosterilecegini belirleyecegiz.

- veriSeti.describe(include="all") fonksiyonunu kullanarak, tum sutunlarin (sayisal ve kategorik) temel istatistiksel ozetini goruntuleyecegiz."""))

# --- Cell 14: Describe code ---
cells_2A.append(make_cell("code", """# 1) pd.set_option ile ekrana basilacak sutun sayisini 20 ile sinirlandiriyoruz
pd.set_option("display.max_columns", 20)

# 2) describe(include="all") ile sayisal ve kategorik tum sutunlarin ozet istatistiklerini aliyoruz
print("Veri Seti Ozeti (describe, include='all'):\\n", veriSeti.describe(include="all"))"""))

# --- Cell 15: Groupby markdown ---
cells_2A.append(make_cell("markdown", """# **2.6 Veri Gruplama (Aggregate)**

### Neden Onemli?
Makine ogrenmesi ve veri bilimi sureclerinde, bazen tum veri setini tek bir butun olarak degerlendirmek yerine, verileri belirli ozelliklere gore alt gruplara ayirip ayri ayri incelemek faydalidir. Bu islem sayesinde her bir alt grup hakkinda istatistiksel ozet bilgiler elde edebiliriz. Bu, veriyi anlamak, farkli alt gruplari karsilastirmak ve karar vermek acisindan onemlidir.

**Ornegin:** Bir otomobil verisinde araclarin sehir ici yakit tuketimini (city_mpg) "durum" kategorisine (Dusuk, Orta, Yuksek) gore ayri ayri inceleyebilirsiniz. Boylece her grubun yakit tuketim ozelliklerini ayri ayri degerlendirebilirsiniz.


### **Veri Ayiriklastirma ile Gruplama Arasindaki Fark**

**Veri Ayiriklastirma (Discretization) = sayisali kategorik hale getirme**
- **Amac:** Surekli degiskenleri kategorik hale getirerek siniflandirmak.
- **On kosul:** Kategorik bir sutun yoksa, analiz icin kendimiz uretmeliyiz.

**Veri Gruplama (Aggregation) = zaten var olan kategorik degiskene gore istatistik cikarmak**
- **Amac:** Var olan kategorik sutuna gore gruplar olusturup bu gruplar icin istatistikler hesaplamak.
- **On kosul:** Veri setinde zaten kategorik bir degisken (ornegin durum) varsa dogrudan kullanilabilir.



### Bu bolumde ne yapacagiz?
- **groupby("durum")** ifadesini kullanarak, durum sutunu bazinda veri setini gruplara ayiracagiz.

- Farkli toplulastirma fonksiyonlari **(mean, sum, count, min, max, std, describe)** ile her bir kategorinin temel istatistiklerini goruntuleyecegiz."""))

# --- Cell 16: Groupby code ---
cells_2A.append(make_cell("code", """# 1. Adim: "durum" kategorisine gore "city_mpg" degiskeninin temel istatistiklerini cikar
df_ozet = veriSeti.groupby("durum", observed=False)["city_mpg"].describe().round(2)

# 2. Adim: 'durum' degiskeni indeks olarak degil, sutun olarak gorunsun diye resetlenir
df_ozet.reset_index(inplace=True)

# 3. Adim: Jupyter defteri kullaniliyorsa tablo seklinde gorsellestirir
display(df_ozet)  # Sadece Jupyter ortaminda calisir. Eger konsoldaysaniz print(df_ozet) yazmalisiniz."""))

# --- Cell 17: Stats interpretation markdown ---
cells_2A.append(make_cell("markdown", """## `durum` Degiskenine Gore `city_mpg` (Sehir Ici Yakit Verimliligi) Istatistikleri

Asagidaki tablo, `city_mpg` (sehir ici mil per galon) sayisal degiskeninin, `durum` adli kategorik degiskene gore gruplandirilarak (aggregation) temel istatistiklerle ozetlenmesini gostermektedir.

---

### Yorum:

1. **Yuksek** `durum` kategorisi:
   - En yuksek **ortalama** `city_mpg` degeriyle en verimli gruptur.
   - Bu grupta yuksek yakit verimliligi olan araclar bulunur.

2. **Orta** kategori:
   - Orta duzeyde yakit verimliligi gosteren araclari icerir.
   - Degerler belirli bir aralikta yogunlasmistir.

3. **Dusuk** kategori:
   - Ortalama deger en dusuk olan gruptur.
   - Gruptaki araclar arasinda onemli cesitlilik olabilir.

---
---"""))

# --- Cell 18: Separator ---
cells_2A.append(make_cell("markdown", """---

---

---"""))

# --- Cell 19: Duplicates markdown ---
cells_2A.append(make_cell("markdown", """# **2.7 Tekrarlayan Satirlarin Bulunmasi (Duplicated Rows)**

### Neden Onemli?
Tekrarlayan **(duplicate)** satirlar, veri analizi sonuclarini yaniltabilir. Ayni gozlemin veri setinde birden fazla kez yer almasi, ortalama ve diger istatistiksel hesaplamalari etkileyerek hatali sonuclara yol acabilir. Bu nedenle tekrarlayan satirlari tespit edip, gereksiz olanlari temizlemek veri kalitesini artirir.

### Bu bolumde ne yapacagiz?
- `duplicated()` fonksiyonunu kullanarak tekrarlayan satirlari bulacagiz.
- `drop_duplicates()` ile tekrarlayanlari temizleyecegiz.
- Tekrarlayan satirlari bulmak icin farkli keep parametreleri **(ornegin "first", "last")** deneyecegiz."""))

# --- Cell 20: Duplicates code ---
cells_2A.append(make_cell("code", """# 1) duplicated(keep="first") ve duplicated(keep="last") ile tekrarlayan satirlari tespit ediyoruz
    # keep="first" => ilk tekrar eden satiri False, diger tekrarlarini True olarak isaretler
    # keep="last"  => son tekrar eden satiri False, diger tekrarlarini True olarak isaretler
tekrarlar_f = veriSeti.duplicated(keep="first")
tekrarlar_l = veriSeti.duplicated(keep="last")

# 2) Herhangi birinin True oldugu satirlar, tekrarlayan satirlardir
indislerim = tekrarlar_f | tekrarlar_l

# 3) Tekrarlayan gozlemleri ekrana basalim
print("Tekrarlayan Gozlemler:\\n", veriSeti[indislerim])

# 4) drop_duplicates() ile veri setinden tekrar eden satirlari kaldiriyoruz
veriSeti2 = veriSeti.drop_duplicates()

# 5) Kaldirma isleminden sonra veri setinin boyutunu (shape) inceleyerek degisikligi gozlemleyebiliriz
print("\\nTekrarlayanlardan arindirilmis veriSeti2 shape:", veriSeti2.shape)"""))

# --- Cell 21: Outlier markdown ---
cells_2A.append(make_cell("markdown", """# **2.8 Aykiri Deger Analizi (IQR ve Boxplot)**

### Aykiri Deger Nedir?

Aykiri deger, veri setindeki diger degerlerden **belirgin sekilde uzak** olan gozlemlerdir.
Bu degerler cogu zaman hatali girisler, olcum hatalari veya sira disi durumlari temsil edebilir.

> Ornek: Eger `horsepower` sutunundaki degerlerin cogu 50-150 arasinda ise, 200 uzerinde bir deger aykiri olabilir.

---

### Neden Onemlidir?

- Aykiri degerler analizlerin sonucunu **yaniltabilir**.
- Ortalama, standart sapma gibi istatistikleri bozar.
- Bazi algoritmalar (ornegin KNN, k-means) aykiri degerlerden cok etkilenir.

---

### Aykiri Deger Nasil Bulunur?

**1. Gorsel yontem:** Kutu grafigi (boxplot)
**2. Istatistiksel yontem:** IQR (Interquartile Range) yontemi
Bu derste, `horsepower` degiskenini ornek alarak hem istatistiksel hem gorsel yontemle aykiri degerleri belirleyecegiz."""))

# --- Cell 22: IQR code ---
cells_2A.append(make_cell("code", """# 1. Kartil (Q1) ve 3. Kartil (Q3) degerlerini hesaplayalim
q1 = veriSeti["horsepower"].quantile(0.25)  # Alt %25'lik degeri temsil eder
q3 = veriSeti["horsepower"].quantile(0.75)  # Ust %25'lik degeri temsil eder

# IQR (ceyrekler arasi aciklik): Q3 - Q1
IQR = q3 - q1

# Alt ve ust sinirlari belirliyoruz
alt = q1 - 1.5 * IQR
ust = q3 + 1.5 * IQR

print(f"Aykiri deger alt siniri: {alt}, ust siniri: {ust}")"""))

# --- Cell 23: Outlier indices code ---
cells_2A.append(make_cell("code", """# Aykiri olan satirlarin indekslerini buluyoruz
ust_aykiriDegerInd = np.where(veriSeti["horsepower"] >= ust)[0]   # Ust sinirin uzerindeki indeksler
alt_aykiriDegerInd = np.where(veriSeti["horsepower"] <= alt)[0]   # Alt sinirin altindaki indeksler

# Ust sinirin uzerindeki aykiri degerleri indeks : deger formatinda yazdiriyoruz
print("Ust sinirin uzerindeki aykiri degerler:")
for i in ust_aykiriDegerInd:
    print(f"Indeks: {i}, Deger: {veriSeti['horsepower'][i]}")

# Alt sinirin altindaki aykiri degerleri indeks : deger formatinda yazdiriyoruz
print("\\nAlt sinirin altindaki aykiri degerler:")
for i in alt_aykiriDegerInd:
    print(f"Indeks: {i}, Deger: {veriSeti['horsepower'][i]}")"""))

# --- Cell 24: Boxplot explanation markdown ---
cells_2A.append(make_cell("markdown", """### Kutu Grafigi

- **Kutu grafigi (boxplot)**, verinin dagilimini ve olasi aykiri degerleri gorsel olarak anlamamizi saglar.
- Orta cizgi: **Ortanca (medyan)**
- Kutunun alt ve ust kenarlari: **1. ve 3. ceyrek (Q1, Q3)**
- Alt ve ust "biyik" cizgileri:
  - Alt sinir = Q1 - 1.5 * IQR
  - Ust sinir = Q3 + 1.5 * IQR
- Bu sinirlarin **disindaki daireler**, **aykiri degerleri** gosterir.

Bu grafik sayesinde:
- Hangi degerlerin aykiri oldugunu gorsellestirebiliriz.
- Alt sinirin altinda aykiri deger olup olmadigini,
- Ust sinirin uzerinde ne kadar aykiri deger oldugunu kolayca gozlemleyebiliriz."""))

# --- Cell 25: Simple boxplot code ---
cells_2A.append(make_cell("code", """# Basit Kutu Grafigi

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(y="horsepower", data=veriSeti)
plt.title("Horsepower Niteligne Ait Kutu Grafigi")
plt.show()"""))

# --- Cell 26: Annotated boxplot code ---
cells_2A.append(make_cell("code", """# Aciklamali Kutu Grafigi

plt.figure(figsize=(10, 7))

# Aykiri degerleri gizleyerek kutu grafigi ciz
sns.boxplot(y="horsepower", data=veriSeti, showfliers=False)
plt.title("Gercek Verilerle Horsepower Degiskenine Ait Aciklamali Kutu Grafigi")

# Istatistik degerleri
ortalama = veriSeti["horsepower"].mean()
medyan = veriSeti["horsepower"].median()
q1 = veriSeti["horsepower"].quantile(0.25)
q3 = veriSeti["horsepower"].quantile(0.75)
iqr = q3 - q1
alt = q1 - 1.5 * iqr
ust = q3 + 1.5 * iqr

# Ortalama (turuncu)
plt.plot([0], [ortalama], "o-", color="orange")
plt.text(0.1, ortalama, f"Ortalama:\\n{ortalama:.2f}", color="orange", fontsize=10)

# Medyan (siyah nokta)
plt.plot(0, medyan, "ko")
plt.text(-0.35, medyan, f"Medyan\\n{medyan:.2f}", fontsize=10)

# Q1
plt.plot(0, q1, "ks")
plt.text(-0.35, q1, f"Q1 (Alt Ceyrek)\\n{q1:.2f}", fontsize=9)

# Q3
plt.plot(0, q3, "ks")
plt.text(-0.35, q3, f"Q3 (Ust Ceyrek)\\n{q3:.2f}", fontsize=9)

# Alt sinir (mavi kare)
plt.plot(0, alt, "bs")
plt.text(0.15, alt + 2, f"Alt Sinir\\n{alt:.2f}", color="blue", fontsize=9)

# Ust sinir (mavi kare)
plt.plot(0, ust, "bs")
plt.text(0.15, ust + 2, f"Ust Sinir\\n{ust:.2f}", color="blue", fontsize=9)

# Aykiri degerler (siyah daire)
for i, val in enumerate(veriSeti["horsepower"]):
    if val > ust or val < alt:
        plt.plot(0, val, "ko")
        x_offset = 0.2 if i % 2 == 0 else 0.25
        plt.text(x_offset, val, f"{val:.1f}", fontsize=8, color="black")

plt.ylabel("Horsepower")
plt.xticks([])
plt.show()"""))

# --- Cell 27: Drop outliers code (commented) ---
cells_2A.append(make_cell("code", """# 4) Aykiri degerleri kaldirmak icin asagidaki satirlari yorumdan cikarabilirsiniz
# veriSeti.drop(index=ust_aykiriDegerInd, inplace=True)
# veriSeti.drop(index=alt_aykiriDegerInd, inplace=True)"""))

# --- Cell 28: Sampling title markdown ---
cells_2A.append(make_cell("markdown", """# **2.9 Ornekleme (Sampling ve Stratified Sampling)**"""))

# --- Cell 29: Random sampling markdown ---
cells_2A.append(make_cell("markdown", """## 2.9.1. Rastgele Ornekleme (Random Sampling)
Bir veri kumesinden rastgele olarak veri noktalari secmeyi ifade eder. Her bir veri noktasinin secilme sansi esittir.
- **1'den 20'**ye kadar olan sayilar arasinda rastgele **5** sayi secmek istiyorsaniz, bu sayilar her seferinde farkli olabilir.
- Ornegin: **[15, 6, 9, 14, 5]** ve baska bir secimde farkli sayilar olabilir: **[16, 1, 17, 14, 10]**."""))

# --- Cell 30: Random sampling code ---
cells_2A.append(make_cell("code", """# 1'den 20'ye kadar sayilar
listem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# diger yol:  # listem = list(np.arange(1, 21))

# Rastgele 5 sayi secimi
# sample() fonksiyonu ile her cagirda farkli rastgele elemanlar secilir ve tekrar eden sayi bulunmaz.
print("Ornek Secim 1:", sample(listem, 5))
print("Ornek Secim 2:", sample(listem, 5))"""))

# --- Cell 31: Seeded sampling markdown ---
cells_2A.append(make_cell("markdown", """## 2.9.2. Sabit Tohumlu Rastgele Ornekleme (Seeded Sampling)
Rastgele ornekleme, her calistirildiginda farkli sonuclar uretir. Ancak bazen belirli bir sonucu tekrarlamak isteriz. Bunun icin bir "tohum" (seed) degeri kullanilir. Ayni tohum degeriyle rastgele secim yapilirsa, her seferinde ayni secimler elde edilir.

- Raporlar yazarken ya da tekrarlanabilirlik isteyen deneyler yaparken faydalidir."""))

# --- Cell 32: Seeded sampling code ---
cells_2A.append(make_cell("code", """# Ayni seed ile benzer sonuclar
random.seed(123)                                          # Algoritma icin baslangic noktasini 123 olarak belirler.
print("Ornek Secim 3 (seed=123):", sample(listem, 5))
random.seed(123)
print("Ornek Secim 4 (seed=123):", sample(listem, 5))

random.seed(5)                                            # 5 yazarsaniz baslangic noktasi degisir.
print("Ornek Secim 5 (seed=5):", sample(listem, 5))
random.seed(5)
print("Ornek Secim 6 (seed=5):", sample(listem, 5))"""))

# --- Cell 33: Replacement sampling markdown ---
cells_2A.append(make_cell("markdown", """## 2.9.3. Yerine Koyarak Secim (Sampling with Replacement)
Veri kumesindeki bir oge birden fazla kez secilebilir ve her secimde ayni oge tekrar kullanilabilir.
- Bir kutuda 10 top oldugunu dusunun. Bu kutudan 3 top seciyorsunuz, ancak her seferinde topu kutuya geri koyuyorsunuz. Bu durumda ayni topu tekrar secebilirsiniz."""))

# --- Cell 34: Replacement sampling code ---
cells_2A.append(make_cell("code", """# Yerine koyarak secim
print("Yerine koyarak secim:", random.choices(listem, k=10))"""))

# --- Cell 35: Train/test markdown ---
cells_2A.append(make_cell("markdown", """## 2.9.4. Egitim ve Test Veri Seti Olusturma
Egitim ve test veri seti olusturma, model egitimi ve dogrulama islemleri icin veriyi ayirma islemidir.
 - Genellikle verinin **%70'i egitim seti**, **%30'u ise test seti** olarak ayrilir.
 - Egitim seti, makine ogrenmesi modelinin egitilmesi icin kullanilirken, test seti modelin dogrulugunu ve basarisini degerlendirmek icin kullanilir."""))

# --- Cell 36: Train/test code ---
cells_2A.append(make_cell("code", """egitim = veriSeti.sample(frac=0.7, replace=False, random_state=1)
      # sample(): Veri setinden rastgele ornekleme yapar.
      # frac=0.7 -> veri setinin %70'ini sec,
      # replace=False -> ayni satir birden fazla kez secilmesin (tekrarsiz secim),
      # random_state=1 -> her calistirmada ayni satirlarin secilmesini saglar

ind = veriSeti.index.isin(egitim.index)
      # isin(): Egitim setindeki index'lerin ana veri setinde olup olmadigini kontrol eder.

test = veriSeti[~ind]
      # ~ind: Egitim setine dahil olmayan (False olan) satirlari secer.

print("Egitim Seti Boyutu:", egitim.shape)
print("Test Seti Boyutu:", test.shape)"""))

# --- Cell 37: Stratified sampling markdown ---
cells_2A.append(make_cell("markdown", """## 2.9.5. Tabakali Ornekleme (Stratified Sampling)
Tabakali ornekleme, verinin belirli gruplara (tabakalara) ayrilarak her gruptan orantili bir sekilde ornekleme yapilmasidir. Ozellikle dengesiz veri setlerinde, her sinifin dogru bir sekilde temsil edilmesini saglar.

- Tum veri setindeki sinif orani -> egitim ve test setine esit sekilde dagilir.
- Model egitiminde azinlik siniflarin ihmal edilmesi onlenir.
- Egitim ve test setlerinde "durum" degiskeninin dagilimi korunur."""))

# --- Cell 38: Stratified sampling code ---
cells_2A.append(make_cell("code", """egitim1, test1 = train_test_split(                         # train_test_split(): veri setini egitim ve test setine ayirir
    veriSeti,                                              # veriSeti: bolunecek veri
    train_size=0.7,                                        # train_size=0.7 -> verinin %70'i egitim, %30'u test olacak sekilde ayir
    stratify=veriSeti["durum"],                            # stratify: "durum" degiskenine gore orantili ornekleme yapilir
    random_state=1                                         # random_state=1 -> ayni sonucu almak icin sabit tohum (seed)
)

print("\\nDurum Dagilimi (Tum veri):\\n", veriSeti.durum.value_counts())    # value_counts(): "durum" degiskeninin sinif dagilimini gosterir
print("\\nDurum Dagilimi (Egitim seti):\\n", egitim1.durum.value_counts())  # Egitim setindeki sinif dagilimini yazdirir
print("\\nDurum Dagilimi (Test seti):\\n", test1.durum.value_counts())      # Test setindeki sinif dagilimini yazdirir"""))

# --- Cell 39: Encoding title markdown ---
cells_2A.append(make_cell("markdown", """# **2.10 Yapay Kodlama (Label and Dummy Coding) ve Veri Normalizasyonu**"""))

# --- Cell 40: Encoding explanation markdown ---
cells_2A.append(make_cell("markdown", """### 2.10.1. Kategorik Degiskeni Sayisal Forma Donusturme (cat.codes ve get_dummies)
#### Neden Onemli?
Makine ogrenmesi ve istatistiksel modeller **sayisal verilerle calisir**. Bu yuzden kategorik degiskenleri sayisal forma cevirmemiz gerekir. Bu islem genellikle iki yontemle yapilir:

---

#### 1. `cat.codes` -> Label Encoding (Etiket Kodlama)

- Her kategoriye bir **sayisal deger** atanir.
- Tek bir sutun olusturur.
Ornek:

| durum   | durum_s1 |
|---------|----------|
| Dusuk   | 0        |
| Orta    | 1        |
| Yuksek  | 2        |

---

#### 2. `get_dummies()` -> Dummy (One-Hot) Encoding

- Her kategori icin **ayri bir sutun** olusturur.
- 0 ve 1 degerleri icerir.
Ornek:

| Dusuk | Orta | Yuksek |
|-------|------|--------|
| 1     | 0    | 0      |
| 0     | 1    | 0      |
| 0     | 0    | 1      |

---

#### Projede Neden Her Ikisi de Kullanildi?

Kodda hem `cat.codes` hem de `get_dummies()` kullanildi. Bu sayede:

- `durum_s1` sutunu: **etiket kodlama** icin,
- `Dusuk`, `Orta`, `Yuksek` sutunlari: **dummy kodlama** icin olusturulmus oldu.

**Hangisi kullanilacak?**
-> Modeliniz sirali bilgiye ihtiyac duymuyorsa dummy encoding daha guvenlidir.

---

Sonuc:
Kategorik veriyi sayisala cevirmek zorunludur. Ancak **nasil cevirecginiz**, kullandiginiz algoritmaya baglidir."""))

# --- Cell 41: Encoding code ---
cells_2A.append(make_cell("code", """# Kategorik degiskeni sayisal forma donusturme
# 1. (cat.codes)
veriSeti["durum_s1"] = veriSeti["durum"].cat.codes
 # Kategorik 'durum' degiskenini 0,1,2 gibi sayilara cevir
print("durum_s1 deger dagilimi:", veriSeti["durum_s1"].value_counts())
 # Sayisal karsiliklarin frekansini yazdir

# 2. (get_dummies())
if not {'Dusuk', 'Orta', 'Yuksek'}.issubset(veriSeti.columns):    # get_dummies() her seferinde yeni sutunlar ekler. issubset ile tekrar eklenmesini onlemek gerekir.
    durum_s2 = pd.get_dummies(veriSeti["durum"], dtype=int)       # 'Dusuk', 'Orta', 'Yuksek' gibi her sinif icin ayri sutun
    veriSeti = pd.concat([veriSeti, durum_s2], axis=1)            # Yeni dummy sutunlarini veriSeti'ne ekle
    print("Yapay Kodlama ile eklenen sutunlar:", list(durum_s2.columns))  # Eklenen sutun isimlerini yazdir

display(veriSeti.head(5))"""))

# --- Cell 42: Normalization markdown ---
cells_2A.append(make_cell("markdown", """### 2.10.2. Min-Max Normalizasyonu (0-1 Arasina Sikistirma)
#### Neden Onemli?
Veri setindeki sayisal sutunlar farkli araliklarda olabilir (ornegin: **city_mpg 13-49** arasinda, **horsepower 48-288** arasinda olabilir).
Bu fark, ozellikle uzaklik/matris temelli modellerde (KNN, K-Means, Lojistik Regresyon vb.) bazi degiskenlerin modele daha fazla etki etmesine yol acar.

Bu nedenle, tum degiskenlerin ayni olcege getirilmesi gerekir.
Min-Max Normalizasyonu, her bir sayisal degeri 0 ile 1 arasina sikistirarak bu islemi yapar.

**Avantaji:**
- Degiskenlerin esit etki gucune sahip olmasini saglar.

- Ozellikle mesafe tabanli algoritmalar icin onerilir."""))

# --- Cell 43: Normalization code ---
cells_2A.append(make_cell("code", """# Min-Max Normalizasyonu (verileri 0-1 arasina sikistirma)
# Sayisal sutunlari seciyoruz
sayisal_sutunlar = ["city_mpg", "engine_size", "horsepower", "curb_weight", "peak_rpm", "normalized_losses"]
veri = veriSeti[sayisal_sutunlar]

scaler = MinMaxScaler()  # Min-Max olcekleyici nesnesi olustur
scaler.fit(veri)  # Minimum ve maksimum degerleri ogren
n_veriSeti = scaler.transform(veri)  # Veriyi 0-1 araligina donustur
n_veriSeti = pd.DataFrame(n_veriSeti, columns=veri.columns)  # Sonuclari tekrar DataFrame'e cevir
print("\\nMin-Max Normalizasyon sonrasi ilk 5 satir:\\n", n_veriSeti.head())"""))


# ============================================================
# BUILD 2A NOTEBOOK
# ============================================================
nb_2A = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {"name": "python"}
    },
    "cells": cells_2A
}

with open("/Users/zuber/INP214/week-02-data-preparation/2A_veri_hazirlama.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb_2A, f, ensure_ascii=False, indent=1)

print("2A_veri_hazirlama.ipynb olusturuldu!")
print(f"Toplam hucre sayisi: {len(cells_2A)}")


# ============================================================
# BUILD 2Q NOTEBOOK (from 2A with empty code cells + GÖREV)
# ============================================================
cells_2Q = []

# Task counter
gorev_no = 0

for i, cell in enumerate(cells_2A):
    new_cell = copy.deepcopy(cell)
    
    if cell["cell_type"] == "code":
        # First code cell (library imports) stays intact - same as 1Q pattern
        if i == 2:  # Library imports cell
            cells_2Q.append(new_cell)
            continue
        
        gorev_no += 1
        
        # Create task descriptions based on section
        if i == 5:  # Data reading
            task_source = f"# GOREV {gorev_no}: automobile.csv dosyasini okuyarak veriSeti degiskenine atayin\n# Dosya yolu: '/content/drive/MyDrive/Colab Notebooks/automobile.csv'\n\n\n# Veri setinin boyutunu ve sutun veri tiplerini ekrana yazdirin\n\n\n# Ilk 10 satiri goruntuleyin\n"
        elif i == 8:  # Missing data
            task_source = f"# GOREV {gorev_no}: Eksik veri tamamlama islemlerini gerceklestirin\n# a) '?' karakteri iceren sutunlari tespit edin\n# b) '?' karakterlerini NaN'e donusturun (normalized_losses, horsepower, peak_rpm)\n# c) Bu sutunlarin tipini float64'e donusturun\n# d) Eksik veri sayisini kontrol edin\n# e) Eksik degerleri ortalama ile doldurun\n# f) Eksik veri sayisini tekrar kontrol edin\n"
        elif i == 11:  # Binning
            task_source = f"# GOREV {gorev_no}: city_mpg sutununu 3 kategoriye ayirin (Dusuk, Orta, Yuksek)\n# I. Yontem: lambda + map() ile (<21: Dusuk, 21-30: Orta, >=30: Yuksek)\n# II.1: pd.cut() ile sabit aralik yontemi\n# II.2: pd.qcut() ile esit frekans yontemi\n# II.3: pd.cut() ile esit genislik yontemi\n"
        elif i == 14:  # Describe
            task_source = f"# GOREV {gorev_no}: Veri setinin ozet istatistiklerini goruntuleyin\n# pd.set_option ile max sutun sayisini 20 yapin\n# describe(include='all') fonksiyonunu kullanin\n"
        elif i == 16:  # Groupby
            task_source = f"# GOREV {gorev_no}: 'durum' kategorisine gore 'city_mpg' degiskeninin istatistiklerini cikarin\n# groupby('durum') ve describe() fonksiyonlarini kullanin\n# Sonucu display() ile goruntuleyin\n"
        elif i == 20:  # Duplicates
            task_source = f"# GOREV {gorev_no}: Tekrarlayan satirlari bulun ve temizleyin\n# a) duplicated(keep='first') ve duplicated(keep='last') ile tespit edin\n# b) Tekrarlayan gozlemleri ekrana basin\n# c) drop_duplicates() ile temizleyin\n# d) Temizlenmis veri setinin boyutunu yazdirin\n"
        elif i == 22:  # IQR
            task_source = f"# GOREV {gorev_no}: horsepower degiskeni icin IQR yontemiyle aykiri deger sinirlarini hesaplayin\n# Q1, Q3 ve IQR degerlerini bulun\n# Alt ve ust sinirlari hesaplayin\n"
        elif i == 23:  # Outlier indices
            task_source = f"# GOREV {gorev_no}: Aykiri degerlerin indekslerini ve degerlerini bulup yazdirin\n# np.where() kullanarak ust ve alt sinirin disindaki degerleri bulun\n"
        elif i == 25:  # Simple boxplot
            task_source = f"# GOREV {gorev_no}: horsepower degiskeni icin basit bir kutu grafigi (boxplot) cizin\n# seaborn ve matplotlib kullanin\n"
        elif i == 26:  # Annotated boxplot
            task_source = f"# GOREV {gorev_no}: horsepower degiskeni icin aciklamali kutu grafigi cizin\n# Ortalama, medyan, Q1, Q3, alt/ust sinir ve aykiri degerleri isaretleyin\n"
        elif i == 27:  # Drop outliers
            task_source = f"# GOREV {gorev_no}: (Opsiyonel) Aykiri degerleri kaldirmak icin gerekli kodlari yazin\n# Yorumlu olarak birakin\n"
        elif i == 30:  # Random sampling
            task_source = f"# GOREV {gorev_no}: 1'den 20'ye kadar bir liste olusturun ve rastgele 5 sayi secin\n# sample() fonksiyonunu kullanin, 2 farkli secim yapin\n"
        elif i == 32:  # Seeded sampling
            task_source = f"# GOREV {gorev_no}: Sabit tohumlu (seed) rastgele ornekleme yapin\n# seed=123 ve seed=5 ile ornekler olusturun\n"
        elif i == 34:  # Replacement sampling
            task_source = f"# GOREV {gorev_no}: Yerine koyarak secim yapin\n# random.choices() ile 10 elemanlik bir ornek secin\n"
        elif i == 36:  # Train/test
            task_source = f"# GOREV {gorev_no}: Veri setini %70 egitim, %30 test olarak bolin\n# sample() ve isin() fonksiyonlarini kullanin\n# Her iki setin boyutunu yazdirin\n"
        elif i == 38:  # Stratified
            task_source = f"# GOREV {gorev_no}: Tabakali ornekleme ile veri setini bolin\n# train_test_split() fonksiyonunu stratify parametresiyle kullanin\n# Tum veri, egitim ve test setlerindeki durum dagilimini yazdirin\n"
        elif i == 41:  # Encoding
            task_source = f"# GOREV {gorev_no}: Kategorik degiskeni sayisal forma donusturun\n# a) cat.codes ile etiket kodlama yapin (durum_s1)\n# b) get_dummies() ile dummy kodlama yapin\n# c) Sonucu goruntuleyin\n"
        elif i == 43:  # Normalization
            task_source = f"# GOREV {gorev_no}: Min-Max Normalizasyonu uygulayin\n# Sayisal sutunlari secin\n# MinMaxScaler ile 0-1 arasina donusturun\n# Ilk 5 satiri yazdirin\n"
        else:
            task_source = f"# GOREV {gorev_no}: Ilgili islemi gerceklestirin\n"
        
        new_cell["source"] = [task_source]
        new_cell["outputs"] = []
        new_cell["execution_count"] = None
    
    cells_2Q.append(new_cell)

nb_2Q = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {"name": "python"}
    },
    "cells": cells_2Q
}

# Fix 2Q title
nb_2Q["cells"][0] = make_cell("markdown", """# **2Q_veri_hazirlama**""")

with open("/Users/zuber/INP214/week-02-data-preparation/2Q_veri_hazirlama.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb_2Q, f, ensure_ascii=False, indent=1)

print("2Q_veri_hazirlama.ipynb olusturuldu!")
print(f"Toplam hucre sayisi: {len(cells_2Q)}")
print(f"Toplam GOREV sayisi: {gorev_no}")
