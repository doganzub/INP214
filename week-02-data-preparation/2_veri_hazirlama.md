# **2. Veri Hazırlama (Data Preparation)**

> ## Google LM Studio — Slayt Sunusu Oluşturma Promptu
>
> **Bu dokümanı Google LM Studio'ya vererek "Slayt Sunusu" formatında bir ders materyali oluşturabilirsiniz.**
>
> Aşağıdaki promptu Google LM Studio'da "Slayt Sunusu" aracına yapıştırın:
>
> ---
>
> **PROMPT:**
>
> *Bu doküman, üniversite düzeyinde "Veri Hazırlama (Data Preparation)" konusunu anlatan bir ders notu içermektedir. Bu içerikten pedagojik açıdan etkili bir slayt sunusu oluştur. Hedef kitle, programlama ve veri bilimi konusunda sıfırdan başlayan üniversite öğrencileridir.*
>
> *Slayt sunusunu oluştururken şu kurallara uy:*
>
> *1. **Pedagojik sıralama:** Konular basitten karmaşığa doğru ilerlemeli. Her bölüm önce "Neden önemli?" sorusunu cevaplasın, ardından kavram açıklaması, sonra da Python kod örneği gelsin.*
> *2. **Sade dil:** Teknik terimleri ilk kullanımda mutlaka günlük dilde açıkla. Öğrenci hiçbir ön bilgiye sahip değilmiş gibi yaz. Örneğin: "NaN (Not a Number) = Eksik değer, yani tabloda o hücre boş demektir."*
> *3. **Görsel destekli:** Her kavram için mümkünse bir tablo, diyagram veya kod çıktısı ekle. Kutu grafiği (boxplot) gibi görsellerin ne anlattığını ok ve etiketlerle açıkla.*
> *4. **Her slaytın yapısı:** Başlık → Kısa açıklama (maks 3 cümle) → Örnek veya Görsel → Öğrenci için ipucu/özet kutusu.*
> *5. **Bölüm geçişlerinde bağlam:** Yeni bir konuya geçerken önceki konuyla bağlantısını kur. Örneğin: "Eksik verileri temizledik. Şimdi bu temiz veriyi kategorilere ayırmayı öğreneceğiz."*
> *6. **Kod blokları:** Her Python kod bloğunu satır satır açıkla. Öğrenci kodu kopyalayıp Colab'da çalıştırabilmeli.*
> *7. **Özet slaytları:** Her ana bölümün sonunda 3-5 maddelik bir özet slaytı ekle.*
> *8. **Dil:** Türkçe. Teknik terimler İngilizce parantez içinde verilsin. Örneğin: "Eksik Veri Tamamlama (Missing Data Imputation)".*
> *9. **Ton:** Samimi ama akademik. Öğrenciyi motive edici. "Tebrikler, eksik verileri başarıyla doldurdunuz!" gibi geçiş cümleleri kullan.*
> *10. **Sunum süresi:** Yaklaşık 90 dakikalık bir ders için uygun uzunlukta olsun.*
>
> ---

Bu derste, Python kullanarak veri ön işleme tekniklerini uygulamalı olarak öğreneceğiz. Özellikle otomobil yakıt tüketimi veri seti (auto-mpg.data) üzerinden eksik veri yönetimi, ayrıklaştırma, gruplandırma, tekrarlayan satır tespiti, aykırı değer analizi, örnekleme, kodlama ve normalizasyon adımlarını inceleyeceğiz.

---

## 2.1 **Gerekli Kütüphanelerin Yüklenmesi**

### Neden Önemli?
Veri ön işleme aşamasında kullanılacak tüm fonksiyonları, grafik araçlarını ve veri dönüşüm araçlarını bu kütüphaneler sağlar.

### Bu bölümde ne yapacağız?
- **`NumPy, pandas, seaborn, sklearn`** gibi paketleri import edeceğiz.
- **Veri ön işleme** sırasında kullanacağımız fonksiyonları tanımlayacağız.

```python
import numpy as np                 # Sayısal işlemler
import pandas as pd                # Veri çerçeveleri ile çalışma
import seaborn as sns              # Veri görselleştirme
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats  # Kutu grafiği istatistikleri
import random                      # Rastgele işlemler
from random import sample          # Belirli bir listeden rastgele seçim
from sklearn.model_selection import train_test_split  # Eğitim/Test veri bölme
from sklearn.preprocessing import MinMaxScaler, StandardScaler  # Normalizasyon & standardizasyon


print("✅ Gerekli kütüphaneler başarıyla yüklendi.")
```

**Çıktı:**
```
✅ Gerekli kütüphaneler başarıyla yüklendi.
```

---

## **2.2 Veri Okuma**

### Neden Önemli?
Veriyi doğru biçimde okumak ve bir **`DataFrame`** hâline getirmek, sonraki tüm veri ön işleme ve analiz adımları için kritik bir adımdır. Eğer veri yanlış bir konumdan okunursa veya sütun başlıkları hatalı tanımlanırsa, ileriki aşamalarda eksik ya da hatalı sonuçlar alabiliriz.

### Bu bölümde ne yapacağız?
- Google Drive'ı bağlayarak **(`mount`)** veri setinin bulunduğu klasöre erişeceğiz.
- **`auto-mpg.data`** dosyasını, pandas'ın **`read_csv`** fonksiyonunu kullanarak okuyacağız.
- Dosyada başlık **(`header`)** bulunmadığı için names parametresiyle sütun isimlerini manuel tanımlayacağız.
- Veri setinin sütun veri tiplerini **(`dtypes`)** inceleyeceğiz.
- Ayrıca **`head()`** fonksiyonuyla veri içeriğine hızlıca göz atacağız.

```python
# 1) Google Drive'ı mount ediyoruz
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# 2) Sütun isimlerini belirliyoruz
nitelikAdlari = [
    "mpg", "cylinders", "displacement", "horsepower", "weight",
    "acceleration", "model_year", "origin", "car_name"
]

# 3) 'auto-mpg.data' dosyasını, Colab Notebooks klasöründen tam yol ile okuyoruz
veriSeti = pd.read_csv(
    "/content/drive/MyDrive/Colab Notebooks/auto-mpg.data",  # Dosyanın tam yolu
    sep=r"\s+",        # Boşluk veya tab ayracı
    header=None,       # Dosyada sütun başlığı yok
    names=nitelikAdlari,  # Yukarıda tanımlanan sütun isimleri
    decimal="."        # Ondalık ayırıcı
)

# 4) Veri setinin boyutu ve sütun veri tipleri
print("Sütun Veri Tipleri:\n", veriSeti.dtypes)
display(veriSeti.head(10))
```

**Çıktı:**
```
Sütun Veri Tipleri:
 mpg             float64
cylinders         int64
displacement    float64
horsepower       object
weight          float64
acceleration    float64
model_year        int64
origin            int64
car_name         object
dtype: object
```

> **Not:** `horsepower` sütunu `object` tipinde çünkü içinde `?` karakterleri var. Bu, bir sonraki bölümde ele alınacak.

---

## **2.3 Eksik Veri Tamamlama (Missing Data Imputation)**

### Neden Önemli?
Eksik veriler, modelin doğruluğunu olumsuz etkileyebilir veya hata oluşturabilir. Bu nedenle eksik verileri uygun yöntemlerle doldurmak **(`imputation`)**, veri kalitesini artırır ve analiz veya makine öğrenmesi modellerinden daha güvenilir sonuçlar elde etmemize yardımcı olur.

### Bu bölümde ne yapacağız?
- **`horsepower`** sütunundaki **'?'** karakterlerini **`NaN`'e** dönüştüreceğiz.
- Bu sütunun veri tipini sayısal **`(float64)`** hâline getireceğiz.
- Eksik veri sayısını inceleyip, ortalama değerle dolduracağız.
- **`fillna()`** metodu kullanımını örnek olarak göreceğiz.

```python
soru_isareti_sayisi = (veriSeti["horsepower"] == "?").sum()       # Ön kontrol: horsepower sütununda "?" karakteri var mı?
print("horsepower sütununda '?' sayısı:", soru_isareti_sayisi)    # Bu satır, "?" işareti olan satırların sayısını ekrana basar.

# 1) '?' karakterini NaN'e dönüştürme
veriSeti.loc[veriSeti.horsepower == "?", "horsepower"] = np.nan   # loc[] fonksiyonu, koşul ile belirtilen satırlara erişmemizi sağlar.
                                                                  # horsepower sütununda "?" görülen hücreleri NaN (eksik değer) işaretleme.
# 2) 'horsepower' sütununun tipini float64'e dönüştürme
veriSeti.horsepower = veriSeti.horsepower.astype("float64")       # astype("float64"), sütun tipini sayısal hale getirir.

# 3) Eksik veri sayısını (ilk kontrol) ekrana bastırma
print("Eksik Veri Sayısı (Önce):\n", veriSeti.isnull().sum())     # isnull().sum(), sütun bazında NaN sayısını verir.

# 4) fillna() metodu ile ortalamayla doldurma
veriSeti["horsepower"].fillna(
    veriSeti["horsepower"].mean().round(0),                       # mean().round(0), sütunun ortalamasını en yakın tam sayıya yuvarlar.
    inplace=True                                                  # inplace=True, değişikliği doğrudan veriSeti üzerinde uygular.
)
print("Eksik Veri Sayısı (Sonra):\n", veriSeti.isnull().sum())    # Eksik veri sayısını tekrar kontrol ediyoruz
```

**Çıktı:**
```
horsepower sütununda '?' sayısı: 6
Eksik Veri Sayısı (Önce):
 mpg             0
cylinders       0
displacement    0
horsepower      6
weight          0
acceleration    0
model_year      0
origin          0
car_name        0
dtype: int64
Eksik Veri Sayısı (Sonra):
 mpg             0
cylinders       0
displacement    0
horsepower      0
weight          0
acceleration    0
model_year      0
origin          0
car_name        0
dtype: int64
```

---

## **2.4 Veri Ayrıklaştırma (Binning / Discretization)**

### Neden Önemli?
- Sürekli (sayısal) veriler, kategorik (gruplandırılmış) değerlere dönüştürülür.
- Bu dönüşümle, veriye yeni bir sütun eklenir veya mevcut sütun sınıflara ayrılır.
- Amaç: Sayısal değerleri daha anlamlı ve genellenmiş kategorilere indirgemektir.

Örneğin: `mpg` değişkeni;
- **23.5'in altında** ise → **Düşük**
- **23.5 – 30 arası** ise → **Orta**
- **30 ve üstü** ise → **Yüksek** olarak sınıflandırılabilir.

Bu işlem sonucunda:
- Veri setine **yeni bir kategorik sütun (örneğin: `durum`)** eklenir.
- Satır sayısı değişmez; sadece her satır bir kategoriye atanır.

---

### Bu bölümde ne yapacağız?
- `mpg` sütununu **Düşük**, **Orta** ve **Yüksek** kategorilerine ayıracağız.
- Dört farklı yöntemle ayrıklaştırma işlemi gerçekleştireceğiz:

I. Yöntem:

 **1.** **`lambda` + `map()`** fonksiyonu ile manuel koşullu sınıflandırma yapacağız.

II. Yöntem:

**2.1.** **`pd.cut()`** fonksiyonu ile **sabit aralık (fixed interval)** yöntemi uygulayacağız.
**2.2.** **`pd.qcut()`** fonksiyonu ile **eşit frekans (quantile)** yöntemi kullanacağız.
**2.3.** **`pd.cut()`** fonksiyonu ile **eşit genişlik (equal interval)** yöntemini uygulayacağız.

```python
# ------------------------------------------------------------
# I. Yöntem: lambda + map
# ------------------------------------------------------------
# lambda ifadesi, 'mpg' değerine göre koşullu atama yapar:
# - x < 23.5 ise "Düşük"
# - 23.5 <= x < 30 ise "Orta"
# - x >= 30 ise "Yüksek" olarak etiketler.
veriSeti["durum"] = veriSeti.mpg.map(
    lambda x: "Düşük" if x < 23.5 else ("Orta" if (x >= 23.5 and x < 30) else "Yüksek")
).astype("category")

print("Durum (lambda) dağılım:\n", veriSeti.durum.value_counts())
print(f"\n{'-'*82}\n")

#----------------------------------------------------------------------------------
# II. Yöntem:
#----------------------------------------------------------------------------------

# II.1: Yöntem: Fixed (sabit) aralıklarla bölme
bolmeKategorileri = ["Düşük", "Orta", "Yüksek"]   # önceden belirlenmiş sınırlar kullanılarak 'mpg' değerleri üç kategoriye ayrılır.
bolmeler = [8, 23.4, 29.9, 46.6]                  # Belirlenen sınırlar
veriSeti["durum"] = pd.cut(
    veriSeti["mpg"],
    bins=bolmeler,
    labels=bolmeKategorileri
)
print("Durum (fixed cut) dağılım:\n", veriSeti.durum.value_counts())
print(f"\n{'-'*82}\n")

# II.2: Yöntem: Equal Frequency (qcut)
durum_ef = pd.qcut(veriSeti["mpg"], q=3)        # 'mpg' değerleri yaklaşık eşit sayıda gözlem içerecek şekilde üç gruba ayrılır.

print("Durum (Eşit frekans) dağılım:\n", durum_ef.value_counts())
print(f"\n{'-'*82}\n")

# II.3: Yöntem: Equal Interval (eşit genişlik)
durum_ea = pd.cut(veriSeti["mpg"], bins=3)      # 'mpg' değerlerinin aralığı eşit genişlikli üç dilime bölünür.
print("Durum (Eşit genişlik) dağılım:\n", durum_ea.value_counts())
print(f"\n{'-'*82}\n")
```

**Çıktı:**
```
Durum (lambda) dağılım:
 durum
Düşük     208
Orta       98
Yüksek     92
Name: count, dtype: int64

----------------------------------------------------------------------------------

Durum (fixed cut) dağılım:
 durum
Düşük     208
Orta       98
Yüksek     92
Name: count, dtype: int64

----------------------------------------------------------------------------------

Durum (Eşit frekans) dağılım:
 mpg
(8.999, 19.0]     143
(26.933, 46.6]    133
(19.0, 26.933]    122
Name: count, dtype: int64

----------------------------------------------------------------------------------

Durum (Eşit genişlik) dağılım:
 mpg
(8.962, 21.533]     183
(21.533, 34.067]    171
(34.067, 46.6]       44
Name: count, dtype: int64
```

---

## **2.5 Veri Seti Özeti (describe)**

### Neden Önemli?
Veri setinin genel istatistiksel özelliklerini (ortalama, std, min, max vb.) görmek, veri hakkında hızlıca fikir sahibi olmamızı sağlar. Hem sayısal hem de kategorik sütunların özetini almak, veri analizinin sonraki adımlarını planlamada bize rehberlik eder.

### Bu bölümde ne yapacağız?
- `pd.set_option("display.max_columns", 20)` ayarıyla, DataFrame ekrana basılırken en fazla kaç sütun gösterileceğini belirleyeceğiz.
- `veriSeti.describe(include="all")` fonksiyonunu kullanarak, tüm sütunların (sayısal ve kategorik) temel istatistiksel özetini görüntüleyeceğiz.

```python
# 1) pd.set_option ile ekrana basılacak sütun sayısını 20 ile sınırlıyoruz
pd.set_option("display.max_columns", 20)

# 2) describe(include="all") ile sayısal ve kategorik tüm sütunların özet istatistiklerini alıyoruz
print("Veri Seti Özeti (describe, include='all'):\n", veriSeti.describe(include="all"))
```

---

## **2.6 Veri Gruplandırma (Aggregate)**

### Neden Önemli?
Makine öğrenmesi ve veri bilimi süreçlerinde, bazen tüm veri setini tek bir bütün olarak değerlendirmek yerine, verileri belirli özelliklere göre alt gruplara ayırıp ayrı ayrı incelemek faydalıdır. Bu işlem sayesinde her bir alt grup hakkında istatistiksel özet bilgiler elde edebiliriz.

**Örneğin:** Bir otomobil verisinde araçların yakıt tüketimini (mpg) "durum" kategorisine (Düşük, Orta, Yüksek) göre ayrı ayrı inceleyebilirsiniz.

### **Veri Ayrıklaştırma ile Gruplandırma Arasındaki Fark**

**Veri Ayrıklaştırma (Discretization) = sayısalı kategorik hale getirme**
- **Amaç:** Sürekli değişkenleri kategorik hale getirerek sınıflandırmak.
- **Ön koşul:** Kategorik bir sütun yoksa, analiz için kendimiz üretmeliyiz.

**Veri Gruplandırma (Aggregation) = zaten var olan kategorik değişkene göre istatistik çıkarmak**
- **Amaç:** Var olan kategorik sütuna göre gruplar oluşturup bu gruplar için istatistikler hesaplamak.
- **Ön koşul:** Veri setinde zaten kategorik bir değişken (örneğin durum) varsa doğrudan kullanılabilir.

### Bu bölümde ne yapacağız?
- **`groupby("durum")`** ifadesini kullanarak, durum sütunu bazında veri setini gruplara ayıracağız.
- Farklı toplulaştırma fonksiyonları **(mean, sum, count, min, max, std, describe)** ile her bir kategorinin temel istatistiklerini görüntüleyeceğiz.

```python
# 1. Adım: "durum" kategorisine göre "mpg" değişkeninin temel istatistiklerini çıkar
df_ozet = veriSeti.groupby("durum")["mpg"].describe().round(2)

# 2. Adım: 'durum' değişkeni indeks olarak değil, sütun olarak görünsün diye resetlenir
df_ozet.reset_index(inplace=True)

# 3. Adım: Jupyter defteri kullanılıyorsa tablo şeklinde görselleştirir
display(df_ozet)  # Sadece Jupyter ortamında çalışır. Eğer konsoldaysanız print(df_ozet) yazmalısınız.
```

**Çıktı:**

| durum | count | mean | std | min | 25% | 50% | 75% | max |
|-------|-------|------|-----|-----|-----|-----|-----|-----|
| Düşük | 208.0 | 17.26 | 3.35 | 9.0 | 14.38 | 17.55 | 20.00 | 23.2 |
| Orta | 98.0 | 26.34 | 1.78 | 23.5 | 25.00 | 26.00 | 28.00 | 29.9 |
| Yüksek | 92.0 | 34.63 | 3.83 | 30.0 | 31.88 | 33.90 | 36.55 | 46.6 |

### Yorum:

1. **Yüksek** `durum` kategorisi:
   - En yüksek **ortalama** `mpg` değeriyle (`34.63`) en verimli gruptur.
   - En geniş aralığa (min: 30.0 – max: 46.6) sahip.

2. **Orta** kategori:
   - En düşük standart sapmaya (`1.78`) sahiptir → Değerler birbirine çok yakındır, grup oldukça homojendir.

3. **Düşük** kategori:
   - Ortalama değer (`17.26`) en düşük olan gruptur.
   - Standart sapmanın (`3.35`) yüksek olması → Gruptaki araçlar arasında önemli çeşitlilik vardır.

---

## **2.7 Tekrarlayan Satırların Bulunması (Duplicated Rows)**

### Neden Önemli?
Tekrarlayan **(duplicate)** satırlar, veri analizi sonuçlarını yanıltabilir. Aynı gözlemin veri setinde birden fazla kez yer alması, ortalama ve diğer istatistiksel hesaplamaları etkileyerek hatalı sonuçlara yol açabilir. Bu nedenle tekrarlayan satırları tespit edip, gereksiz olanları temizlemek veri kalitesini artırır.

### Bu bölümde ne yapacağız?
- `duplicated()` fonksiyonunu kullanarak tekrarlayan satırları bulacağız.
- `drop_duplicates()` ile tekrarlayanları temizleyeceğiz.
- Tekrarlayan satırları bulmak için farklı keep parametreleri **(örneğin "first", "last")** deneyeceğiz.

```python
# 1) duplicated(keep="first") ve duplicated(keep="last") ile tekrarlayan satırları tespit ediyoruz
    # keep="first" => ilk tekrar eden satırı False, diğer tekrarlarını True olarak işaretler
    # keep="last"  => son tekrar eden satırı False, diğer tekrarlarını True olarak işaretler
tekrarlar_f = veriSeti.duplicated(keep="first")
tekrarlar_l = veriSeti.duplicated(keep="last")

# 2) Herhangi birinin True olduğu satırlar, tekrarlayan satırlardır
indislerim = tekrarlar_f | tekrarlar_l

# 3) Tekrarlayan gözlemleri ekrana basalım
print("Tekrarlayan Gözlemler:\n", veriSeti[indislerim])

# 4) drop_duplicates() ile veri setinden tekrar eden satırları kaldırıyoruz
veriSeti2 = veriSeti.drop_duplicates()

# 5) Kaldırma işleminden sonra veri setinin boyutunu (shape) inceleyerek değişikliği gözlemleyebiliriz
print("\nTekrarlayanlardan arındırılmış veriSeti2 shape:", veriSeti2.shape)
```

**Çıktı:**
```
Tekrarlayan Gözlemler:
 Empty DataFrame
Columns: [mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name, durum]
Index: []

Tekrarlayanlardan arındırılmış veriSeti2 shape: (398, 10)
```

> **Not:** Bu veri setinde tekrarlayan satır bulunmamaktadır.

---

## **2.8 Aykırı Değer Analizi (IQR ve Boxplot)**

### Aykırı Değer Nedir?

Aykırı değer, veri setindeki diğer değerlerden **belirgin şekilde uzak** olan gözlemlerdir.
Bu değerler çoğu zaman hatalı girişler, ölçüm hataları veya sıra dışı durumları temsil edebilir.

> Örnek: Eğer `horsepower` sütunundaki değerlerin çoğu 50–150 arasında ise, 230 gibi bir değer aykırı olabilir.

### Neden Önemlidir?

- Aykırı değerler analizlerin sonucunu **yanıltabilir**.
- Ortalama, standart sapma gibi istatistikleri bozar.
- Bazı algoritmalar (örneğin KNN, k-means) aykırı değerlerden çok etkilenir.

### Aykırı Değer Nasıl Bulunur?

**1. Görsel yöntem:** Kutu grafiği (boxplot)
**2. İstatistiksel yöntem:** IQR (Interquartile Range) yöntemi

```python
# 1. Kartil (Q1) ve 3. Kartil (Q3) değerlerini hesaplayalım
q1 = veriSeti["horsepower"].quantile(0.25)  # Alt %25'lik değeri temsil eder
q3 = veriSeti["horsepower"].quantile(0.75)  # Üst %25'lik değeri temsil eder

# IQR (çeyrekler arası açıklık): Q3 - Q1
IQR = q3 - q1

# Alt ve üst sınırları belirliyoruz
alt = q1 - 1.5 * IQR
ust = q3 + 1.5 * IQR

print(f"Aykırı değer alt sınırı: {alt}, üst sınırı: {ust}")
```

**Çıktı:**
```
Aykırı değer alt sınırı: 2.5, üst sınırı: 198.5
```

```python
# Aykırı olan satırların indekslerini buluyoruz
ust_aykiriDegerInd = np.where(veriSeti["horsepower"] >= ust)[0]   # Üst sınırın üzerindeki indeksler
alt_aykiriDegerInd = np.where(veriSeti["horsepower"] <= alt)[0]   # Alt sınırın altındaki indeksler

# Üst sınırın üzerindeki aykırı değerleri indeks : değer formatında yazdırıyoruz
print("Üst sınırın üzerindeki aykırı değerler:")
for i in ust_aykiriDegerInd:
    print(f"İndeks: {i}, Değer: {veriSeti['horsepower'][i]}")

# Alt sınırın altındaki aykırı değerleri indeks : değer formatında yazdırıyoruz
print("\nAlt sınırın altındaki aykırı değerler:")
for i in alt_aykiriDegerInd:
    print(f"İndeks: {i}, Değer: {veriSeti['horsepower'][i]}")
```

**Çıktı:**
```
Üst sınırın üzerindeki aykırı değerler:
İndeks: 6, Değer: 220.0
İndeks: 7, Değer: 215.0
İndeks: 8, Değer: 225.0
İndeks: 13, Değer: 225.0
İndeks: 25, Değer: 215.0
İndeks: 26, Değer: 200.0
İndeks: 27, Değer: 210.0
İndeks: 67, Değer: 208.0
İndeks: 94, Değer: 215.0
İndeks: 95, Değer: 225.0
İndeks: 116, Değer: 230.0

Alt sınırın altındaki aykırı değerler:
```

---

### Kutu Grafiği

- **Kutu grafiği (boxplot)**, verinin dağılımını ve olası aykırı değerleri görsel olarak anlamamızı sağlar.
- Orta çizgi: **Ortanca (medyan)**
- Kutunun alt ve üst kenarları: **1. ve 3. çeyrek (Q1, Q3)**
- Alt ve üst "bıyık" çizgileri:
  - Alt sınır = Q1 - 1.5 * IQR
  - Üst sınır = Q3 + 1.5 * IQR
- Bu sınırların **dışındaki daireler**, **aykırı değerleri** gösterir.

```python
# Basit Kutu Grafiği

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(y="horsepower", data=veriSeti)
plt.title("Horsepower Niteliğine Ait Kutu Grafiği")
plt.show()
```

```python
# Açıklamalı Kutu Grafiği

plt.figure(figsize=(10, 7))

# Aykırı değerleri gizleyerek kutu grafiği çiz
sns.boxplot(y="horsepower", data=veriSeti, showfliers=False)
plt.title("Gerçek Verilerle Horsepower Değişkenine Ait Açıklamalı Kutu Grafiği")

# İstatistik değerleri
ortalama = veriSeti["horsepower"].mean()
medyan = veriSeti["horsepower"].median()
q1 = veriSeti["horsepower"].quantile(0.25)
q3 = veriSeti["horsepower"].quantile(0.75)
iqr = q3 - q1
alt = q1 - 1.5 * iqr
ust = q3 + 1.5 * iqr

# Ortalama (turuncu)
plt.plot([0], [ortalama], "o-", color="orange")
plt.text(0.1, ortalama, f"Ortalama:\n{ortalama:.2f}", color="orange", fontsize=10)

# Medyan (siyah nokta)
plt.plot(0, medyan, "ko")
plt.text(-0.35, medyan, f"Medyan\n{medyan:.2f}", fontsize=10)

# Q1
plt.plot(0, q1, "ks")
plt.text(-0.35, q1, f"Q1 (Alt Çeyrek)\n{q1:.2f}", fontsize=9)

# Q3
plt.plot(0, q3, "ks")
plt.text(-0.35, q3, f"Q3 (Üst Çeyrek)\n{q3:.2f}", fontsize=9)

# Alt sınır (mavi kare)
plt.plot(0, alt, "bs")
plt.text(0.15, alt + 2, f"Alt Sınır\n{alt:.2f}", color="blue", fontsize=9)

# Üst sınır (mavi kare)
plt.plot(0, ust, "bs")
plt.text(0.15, ust + 2, f"Üst Sınır\n{ust:.2f}", color="blue", fontsize=9)

# Aykırı değerler (siyah daire)
for i, val in enumerate(veriSeti["horsepower"]):
    if val > ust or val < alt:
        plt.plot(0, val, "ko")
        x_offset = 0.2 if i % 2 == 0 else 0.25
        plt.text(x_offset, val, f"{val:.1f}", fontsize=8, color="black")

plt.ylabel("Horsepower")
plt.xticks([])
plt.show()
```

```python
# 4) Aykırı değerleri kaldırmak için aşağıdaki satırları yorumdan çıkarabilirsiniz
# veriSeti.drop(index=ust_aykiriDegerInd, inplace=True)
# veriSeti.drop(index=alt_aykiriDegerInd, inplace=True)
```

---

## **2.9 Örnekleme (Sampling ve Stratified Sampling)**

### 2.9.1. Eğitim ve Test Veri Seti Oluşturma
Eğitim ve test veri seti oluşturma, model eğitimi ve doğrulama işlemleri için veriyi ayırma işlemidir.
 - Genellikle verinin **%70'i eğitim seti**, **%30'u ise test seti** olarak ayrılır.
 - Eğitim seti, makine öğrenmesi modelinin eğitilmesi için kullanılırken, test seti modelin doğruluğunu ve başarısını değerlendirmek için kullanılır.

```python
egitim = veriSeti.sample(frac=0.7, replace=False, random_state=1)
      # sample(): Veri setinden rastgele örnekleme yapar.
      # frac=0.7 → veri setinin %70'ini seç,
      # replace=False → aynı satır birden fazla kez seçilmesin (tekrarsız seçim),
      # random_state=1 → her çalıştırmada aynı satırların seçilmesini sağlar

ind = veriSeti.index.isin(egitim.index)
      # isin(): Eğitim setindeki index'lerin ana veri setinde olup olmadığını kontrol eder.

test = veriSeti[~ind]
      # ~ind: Eğitim setine dahil olmayan (False olan) satırları seçer.

print("Eğitim Seti Boyutu:", egitim.shape)
print("Test Seti Boyutu:", test.shape)
```

**Çıktı:**
```
Eğitim Seti Boyutu: (279, 10)
Test Seti Boyutu: (119, 10)
```

---

### 2.9.2. Tabakalı Örnekleme (Stratified Sampling)
Tabakalı örnekleme, verinin belirli gruplara (tabakalara) ayrılarak her gruptan orantılı bir şekilde örnekleme yapılmasıdır. Özellikle dengesiz veri setlerinde, her sınıfın doğru bir şekilde temsil edilmesini sağlar.

- Tüm veri setindeki sınıf oranı → eğitim ve test setine eşit şekilde dağılır.
- Model eğitiminde azınlık sınıfların ihmal edilmesi önlenir.
- Eğitim ve test setlerinde "durum" değişkeninin dağılımı korunur.

```python
egitim1, test1 = train_test_split(                         # train_test_split(): veri setini eğitim ve test setine ayırır
    veriSeti,                                              # veriSeti: bölünecek veri
    train_size=0.7,                                        # train_size=0.7 → verinin %70'i eğitim, %30'u test olacak şekilde ayır
    stratify=veriSeti["durum"],                            # stratify: "durum" değişkenine göre orantılı örnekleme yapılır
    random_state=1                                         # random_state=1 → aynı sonucu almak için sabit tohum (seed)
)

print("\nDurum Dağılımı (Tüm veri):\n", veriSeti.durum.value_counts())
print("\nDurum Dağılımı (Eğitim seti):\n", egitim1.durum.value_counts())
print("\nDurum Dağılımı (Test seti):\n", test1.durum.value_counts())
```

**Çıktı:**
```
Durum Dağılımı (Tüm veri):
 durum
Düşük     208
Orta       98
Yüksek     92
Name: count, dtype: int64

Durum Dağılımı (Eğitim seti):
 durum
Düşük     145
Orta       69
Yüksek     64
Name: count, dtype: int64

Durum Dağılımı (Test seti):
 durum
Düşük     63
Orta      29
Yüksek    28
Name: count, dtype: int64
```

---

## **2.10 Yapay Kodlama (Label and Dummy Coding) ve Veri Normalizasyonu**

### 2.10.1. Kategorik Değişkeni Sayısal Forma Dönüştürme (cat.codes ve get_dummies)

#### Neden Önemli?
Makine öğrenmesi ve istatistiksel modeller **sayısal verilerle çalışır**. Bu yüzden kategorik değişkenleri sayısal forma çevirmemiz gerekir. Bu işlem genellikle iki yöntemle yapılır:

---

#### 1. `cat.codes` → Label Encoding (Etiket Kodlama)

- Her kategoriye bir **sayısal değer** atanır.
- Tek bir sütun oluşturur.

Örnek:

| durum   | durum_s1 |
|---------|----------|
| Düşük   | 0        |
| Orta    | 1        |
| Yüksek  | 2        |

---

#### 2. `get_dummies()` → Dummy (One-Hot) Encoding

- Her kategori için **ayrı bir sütun** oluşturur.
- 0 ve 1 değerleri içerir.

Örnek:

| Düşük | Orta | Yüksek |
|-------|------|--------|
| 1     | 0    | 0      |
| 0     | 1    | 0      |
| 0     | 0    | 1      |

---

#### Projede Neden Her İkisi de Kullanıldı?

Kodda hem `cat.codes` hem de `get_dummies()` kullanıldı. Bu sayede:

- `durum_s1` sütunu: **etiket kodlama** için,
- `Düşük`, `Orta`, `Yüksek` sütunları: **dummy kodlama** için oluşturulmuş oldu.

**Hangisi kullanılacak?**
→ Modeliniz sıralı bilgiye ihtiyaç duymuyorsa dummy encoding daha güvenlidir.

---

**Sonuç:**
Kategorik veriyi sayısala çevirmek zorunludur. Ancak **nasıl çevireceğiniz**, kullandığınız algoritmaya bağlıdır.

```python
# Kategorik değişkeni sayısal forma dönüştürme
# 1. (cat.codes)
veriSeti["durum_s1"] = veriSeti["durum"].cat.codes
 # Kategorik 'durum' değişkenini 0,1,2 gibi sayılara çevir
print("durum_s1 değer dağılımı:", veriSeti["durum_s1"].value_counts())
 # Sayısal karşılıkların frekansını yazdır

# 2. (get_dummies())
if not {'Düşük', 'Orta', 'Yüksek'}.issubset(veriSeti.columns):
    durum_s2 = pd.get_dummies(veriSeti["durum"], dtype=int)
    veriSeti = pd.concat([veriSeti, durum_s2], axis=1)
    print("Yapay Kodlama ile eklenen sütunlar:", list(durum_s2.columns))

display(veriSeti.head(5))
```

---

### 2.10.2. Min-Max Normalizasyonu (0-1 Arasına Sıkıştırma)

#### Neden Önemli?
Veri setindeki sayısal sütunlar farklı aralıklarda olabilir (örneğin: **mpg 10–40** arasında, **horsepower 50–200** arasında olabilir).
Bu fark, özellikle uzaklık/matris temelli modellerde (KNN, K-Means, Lojistik Regresyon vb.) bazı değişkenlerin modele daha fazla etki etmesine yol açar.

Bu nedenle, tüm değişkenlerin aynı ölçeğe getirilmesi gerekir.
Min-Max Normalizasyonu, her bir sayısal değeri 0 ile 1 arasına sıkıştırarak bu işlemi yapar.

**Avantajı:**
- Değişkenlerin eşit etki gücüne sahip olmasını sağlar.
- Özellikle mesafe tabanlı algoritmalar için önerilir.

```python
# Min-Max Normalizasyonu (verileri 0-1 arasına sıkıştırma)
veri = veriSeti.iloc[:, 0:8]  # İlk 8 sütunun sayısal olduğunu varsayarak seçiyoruz

scaler = MinMaxScaler()  # Min-Max ölçekleyici nesnesi oluştur
scaler.fit(veri)  # Minimum ve maksimum değerleri öğren
n_veriSeti = scaler.transform(veri)  # Veriyi 0-1 aralığına dönüştür
n_veriSeti = pd.DataFrame(n_veriSeti, columns=veri.columns)  # Sonuçları tekrar DataFrame'e çevir
print("\nMin-Max Normalizasyon sonrası ilk 5 satır:\n", n_veriSeti.head())
```
