# **1. Python ile Veri Görselleştirme**

Bu derste, Python kullanarak veri görselleştirme tekniklerini uygulamalı olarak öğreneceğiz. Özellikle sigorta veri seti (insurance.csv) üzerinden veri setinin yüklenmesi, sütun isimlerinin Türkçeleştirilmesi, veri tiplerinin düzenlenmesi ve çeşitli grafiklerin (çizgi, bar, scatter, histogram, box, pasta, scatter matrix) oluşturulması adımlarını inceleyeceğiz.

---

## 1.1 **Google Drive Bağlantısı ve Kütüphane Yükleme**

**Açıklama (Mark):**  
- Google Drive'daki veri setlerine erişebilmek için Drive'ı bağlamamız gerekir (Colab kullanıyorsanız).  
- Gerekli Python kütüphaneleri yüklenip içe aktarılır.  
- Bu kod bloğu, temel kütüphanelerin kurulumunu ve içe aktarılmasını gösterir.  

### Kullanılan Kütüphaneler ve Açıklamaları:

- **`numpy`** — Sayısal hesaplamalar ve matris işlemleri için kullanılır.
- **`pandas`** — Veri işleme, analiz ve veri çerçeveleri ile çalışma imkanı sunar.
- **`matplotlib`** — Grafik ve veri görselleştirme için temel kütüphanelerden biridir.
- **`seaborn`** — Daha gelişmiş ve estetik veri görselleştirme için matplotlib'in üzerine inşa edilmiştir.
- **`sklearn`** (scikit-learn) — Veri ön işleme, modelleme ve değerlendirme araçları içerir.
- **`yellowbrick`** — Makine öğrenmesi modellerinin görselleştirilmesini sağlayan bir kütüphane.

**Bu kütüphaneler, veri analizi ve modelleme süreçlerinde sıkça kullanılır.**

```python
# Gerekli kütüphanelerin yüklenmesi
!pip install -q numpy pandas scikit-learn matplotlib seaborn yellowbrick

# Kütüphanelerin içeri aktarılması
import numpy as np                # Sayısal hesaplamalar ve diziler için
import pandas as pd               # Veri çerçeveleri ile çalışmak için
import matplotlib.pyplot as plt   # Grafik çizimi için
import seaborn as sns             # Gelişmiş veri görselleştirme için

# Ek modüller ve sklearn fonksiyonları
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (mean_squared_error, mean_absolute_error,
                             accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay,
                             silhouette_score)
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn import datasets     # Veri ön işleme, modelleme ve değerlendirme araçları

from google.colab import drive
drive.mount('/content/drive')       # Google Drive'a bağlanmamızı sağlar (Colab).
```

---

## **1.2 Sigorta Veri Setinin Yüklenmesi ve Temel İşlemler**

- Google Drive'da bulunan `insurance.csv` dosyası okunacaktır.
- Veri setinin sütun isimleri İngilizce'den Türkçe'ye çevrilecek (ör. `age` → `yas`, `sex` → `cinsiyet`, vb.).
- Kategorik sütunların veri tipi `category` olarak ayarlanacak.
- Kategorik değerler güncellenecek (örneğin, "male" → "erkek").
- Son olarak, veri setinin özet istatistikleri alınarak veri yapısı kontrol edilecektir.

---

## **1.2.1 Veri Setini Okuma**

```python
# Veri setini Google Drive'dan okuyoruz
# Pandas DataFrame formatına çeviriyoruz
# ve 'insurance_df' isimli değişkene atıyoruz
insurance_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/insurance.csv')

# 'dtypes' Her sutunun veri tipini gösterir
print(insurance_df.dtypes)

# İlk 5 satırı görüntüleyerek veri setine göz atalım
display(insurance_df.head())
```

**Çıktı:**
```
age           int64
sex          object
bmi         float64
children      int64
smoker       object
region       object
charges     float64
dtype: object
```

---

## **1.2.2 Sütun İsimlerini Türkçeleştirme**

```python
# İngilizce sütun isimlerini Türkçeye çeviriyoruz
# DataFrame.rename(columns={...}): Sütun adlarını değiştirmemizi sağlar.

insurance_df = insurance_df.rename(columns={
    "age": "yas",
    "sex": "cinsiyet",
    "bmi": "vki",
    "children": "cocukSayisi",
    "smoker": "sigaraDurum",
    "region": "bolge",
    "charges": "odemeMiktari"
})

# Değişiklikleri doğrulamak için ilk 5 satırı tekrar gözlemleyelim
insurance_df.head()
```

---

## **1.2.3 `object` Kategorik Sütunları → `category` Veri Tipine Dönüştürme**

### Neden `"category"` Veri Tipine Dönüştürüyoruz?

#### ✅ Bellek Kullanımını Azaltır  
- **`object` veri tipi**, her hücre için ayrı ayrı metin (string) saklar ve fazla yer kaplar.  
- **`category` tipi**, tekrar eden değerleri hafızada tek bir kez saklayarak **daha az bellek kullanır**.

#### ✅ İşlem Verimliliğini Artırır
- Makine öğrenmesi ve veri analizi işlemlerinde kategorik değişkenler genellikle **nümerik olarak işlenir**.  
- **`category` veri tipi**, işlemleri hızlandırır çünkü **daha hızlı karşılaştırma ve gruplama yapabilir**.

#### ✅ Veri Analizini Kolaylaştırır  
- Kategorik değişkenlerin **sınıflarını** (`.cat.categories`) ve **frekanslarını** (`.value_counts()`) daha kolay analiz edebilirsin.

---

### **İlk Veri Tipleri** Kontrol Etme

```python
# Sütunların ilk veri tiplerini Kontrol etme
print("İlk veri tipleri:")

# DataFrame.dtypes: Her sütunun veri tipini (int, float, object vs.) gösterir.
print(insurance_df.dtypes)
```

**Çıktı:**
```
İlk veri tipleri:
yas               int64
cinsiyet         object
vki             float64
cocukSayisi       int64
sigaraDurum      object
bolge            object
odemeMiktari    float64
dtype: object
```

---

### **Dönüştürme İşlemi ve Sonrası Veri Tipleri** Kontrol Etme

```python
# `astype('category')`: Nesnel (object) tipindeki sütunları kategorik tipine çevirerek
# bellek kullanımını ve işlem verimliliğini artırır.

insurance_df["cinsiyet"] = insurance_df["cinsiyet"].astype("category")
insurance_df["sigaraDurum"] = insurance_df["sigaraDurum"].astype("category")
insurance_df["bolge"] = insurance_df["bolge"].astype("category")

# Dönüşüm sonrası veri tiplerini kontrol etmek için:
print("\nDönüştürme sonrası veri tipleri:")
print(insurance_df.dtypes)
```

**Çıktı:**
```
Dönüştürme sonrası veri tipleri:
yas                int64
cinsiyet        category
vki              float64
cocukSayisi        int64
sigaraDurum     category
bolge           category
odemeMiktari     float64
dtype: object
```

---

## **1.2.4 Kategorik Değerleri Güncelleme (İngilizce → Türkçe)**

- `.cat.rename_categories({...})`: Kategorik sütun değerlerini yeniden adlandırır.

```python
# Kategorik değerlerin Türkçeleştirilmesi
# .cat.rename_categories(): Kategori isimlerini yeniden adlandırmak için kullanılır
insurance_df["cinsiyet"] = insurance_df["cinsiyet"].cat.rename_categories({"male": "erkek", "female": "kadin"})
insurance_df["sigaraDurum"] = insurance_df["sigaraDurum"].cat.rename_categories({"no": "hayir", "yes": "evet"})
insurance_df["bolge"] = insurance_df["bolge"].cat.rename_categories({
    "southeast": "guneydogu", "northwest": "kuzeybati",
    "southwest": "guneybati", "northeast": "kuzeydogu"
})

# Değişiklikleri görmek için
insurance_df.head(10)
```

---

## **1.3 Veri Setinin Özet İstatistikleri**

```python
print("\nSayısal özet (describe):")

# describe(): Sayısal sütunlar için istatistiksel özet (ortalama, std, min, max vb.) verir.
print(insurance_df.describe())

pd.set_option("display.max_columns", 20)
print("\nTüm sütun özet bilgisi:")
# describe(include='all'): Kategorik sütunları da özetleyerek benzersiz değer sayısı,
# en sık görülen değer vb. bilgileri gösterir.
print(insurance_df.describe(include="all"))
```

---

## **1.3 Veri Setinin İstatistik Açıklamaları**

### 📊 **Yaş Dağılımı:**
- **En genç birey:** 18 yaş  
- **En yaşlı birey:** 64 yaş  
- **Ortalama yaş:** 39.2  
- **Yaş dağılımındaki standart sapma:** 14.05  
  → **Bireylerin büyük çoğunluğu (~%68) 25 ile 53 yaş arasındadır.**

---

### 📊 **Vücut Kitle İndeksi (VKİ):**
- **En düşük VKİ:** 15.96  
- **En yüksek VKİ:** 53.13  
- **Ortalama VKİ:** 30.66  
- **VKİ'nin standart sapması:** 6.09  
  → **Bireylerin büyük çoğunluğu (~%68) 24.57 ile 36.75 VKİ aralığındadır.**

---

### 📊 **Çocuk Sahibi Olma Durumu:**
- **Maksimum çocuk sayısı:** 5  
- **Ortalama çocuk sayısı:** 1.09  
- **Çocuk sahibi olmayan bireylerin yüzdesi:** %50'den fazla  
  → **Bireylerin çoğu ya çocuksuz ya da en fazla 1-2 çocuğa sahiptir.**

---

### 📊 **Sigara İçme Durumu:**
- **Sigara içmeyen birey sayısı:** 1064  
- **Sigara içen birey sayısı:** 274  
  → **Bireylerin %79'u sigara içmiyor.**

---

### 📊 **Bölgesel Dağılım:**
- **En fazla birey bulunan bölge:** Güneydoğu (*guneydogu*) — **364 kişi**  
- **Diğer bölgeler:** Kuzeybatı (*kuzeybati*), Güneybatı (*guneybati*), Kuzeydoğu (*kuzeydogu*)  
  → **Bireylerin en yoğun bulunduğu bölge Güneydoğu'dur.**

---

### 📊 **Sağlık Sigortası Ödeme Miktarları:**
- **En düşük ödeme:** **1,121.87$**  
- **En yüksek ödeme:** **63,770.42$**  
- **Ortalama ödeme:** **13,270.42$**  
- **Ödeme miktarlarının standart sapması:** **12,110.01$**  
  → **Bireylerin büyük çoğunluğu (~%68) 1,160$ ile 25,380$ arasında ödeme yapmaktadır.**

---

## **1.4 Veri Görselleştirme (Insurance)**

---

### **1.4.1 Çizgi Grafik (Line Plot)**

**Örnek 1:** İlk 20 müşterinin VKİ (Vücut Kitle İndeksi) değerlerini çizgi grafik ile görselleştirme.

```python
x_line = np.arange(1, 21)  # Müşteri ID'leri 1'den 20'ye
y_line = insurance_df.iloc[0:20, 2]  # İlk 20 müşterinin VKİ sütunu (index 2)

plt.figure()
plt.plot(x_line, y_line, linestyle="dashed", color="hotpink", linewidth=5)
plt.title("İlk 20 Müşterinin VKİ Değerleri")
plt.xlabel("Müşteri ID")
plt.ylabel("VKİ")
plt.show()
```

---

**Örnek 2:** 40-60 Müşterilerin Yaş Dağılımı

```python
x_line = np.arange(40, 61)
y_line = insurance_df.iloc[40:61, 0]  # Dizi boyutunu eşitlemek için 40:61 kullanıldı

plt.figure()
plt.plot(x_line, y_line, color="blue", linewidth=3)
plt.title("40-60. Müşterinin Yaş Dağılımı")
plt.xlabel("Müşteri ID")
plt.ylabel("Yaş")

plt.show()
```

---

**Örnek 3:** İlk 20 ile 21-40 arasındaki müşterilerin VKİ değerlerinin karşılaştırılması.

```python
x_line2 = np.arange(1, 21)        # X ekseni için 1'den 20'ye kadar olan değerleri içeren bir NumPy dizisi oluşturuluyor
y1 = insurance_df.iloc[0:20, 2]   # İlk 20 müşterinin 2. sütundaki (VKİ gibi bir değer) verisini al
y2 = insurance_df.iloc[20:40, 2]  # Sonraki 20 müşterinin 2. sütundaki verisini al (21-40. satırlar)

plt.figure()                      # Yeni bir grafik figürü oluştur

plt.xticks(x_line2)               # X ekseninde 1'den 20'ye kadar olan tam sayıları göster
plt.plot(x_line2, y1, label="İlk 20")  # İlk 20 müşteri için çizgi grafiği oluştur
plt.plot(x_line2, y2, label="İkinci 20")  # İkinci 20 müşteri için çizgi grafiği oluştur

plt.title("VKİ Karşılaştırması")  # Grafiğe başlık ekle
plt.legend()                      # Çizgilerin hangi gruba ait olduğunu gösteren bir açıklama (legend) ekle
plt.tight_layout(pad=1)           # Grafik düzenini optimize ederek kenar boşluklarını ayarla
plt.show()                        # Grafiği ekrana bastır
```

---

**Örnek 4:** İlk 50 müşterinin yaş dağılımının çizgi grafiği.

```python
import numpy as np
import matplotlib.pyplot as plt

x_age = np.arange(1, 51)            # 1'den 50'ye kadar müşteri ID'lerini içeren NumPy dizisi oluştur
y_age = insurance_df.iloc[0:50, 0]  # İlk 50 müşterinin yaş bilgilerini içeren sütunu seç (0. sütun)

plt.figure()                        # Yeni bir grafik figürü oluştur
plt.title("İlk 50 Müşterinin Yaşı") # Grafiğe başlık ekle
plt.xlabel("Müşteri ID")            # X ekseni etiketi (Müşteri ID'leri)
plt.ylabel("Yaş")                   # Y ekseni etiketi (Müşterilerin yaşları)

plt.plot(x_age, y_age)              # Müşteri ID'lerine karşılık gelen yaşları çizgi grafiği olarak çiz
plt.grid(color="red", linestyle="solid", linewidth=0.5)  # Grafiğe kırmızı renkli ve ince bir ızgara çizgisi ekle

plt.show()
```

---

### **1.4.2 Bar Grafikleri**

**Örnek 1:** Sigara içme durumuna göre ortalama ödeme miktarının bar grafiği.

```python
# Sigara içme durumuna göre ortalama ödeme miktarını hesapla
print(insurance_df.columns)
ozet = insurance_df.groupby("sigaraDurum", observed=True)["odemeMiktari"].mean()
        # - 'groupby("sigaraDurum")'  Veriyi "sigara içme durumu" sütununa göre gruplar.
        # - '["odemeMiktari"].mean()'  Her grup için ödeme miktarının ortalamasını alır.

plt.figure()  # Yeni bir grafik figürü oluştur

plt.bar(x=ozet.index, height=ozet.values, color="r")
        # Dikey çubuk grafiği çiz
        # - 'x=ozet.index'  Çubukların kategorik değerleri (sigara içen/içmeyen).
        # - 'height=ozet.values'  Çubukların yüksekliği (ortalama ödeme miktarları).
        # - 'color="r"'  Çubukların rengi kırmızı ("r") olarak ayarlanır.

plt.xlabel("Sigara İçme Durumu")      # X ekseni etiketi
plt.ylabel("Ortalama Ödeme Miktarı")  # Y ekseni etiketi
plt.title("Sigara Durumuna Göre Ödeme Miktarı")  # Grafiğe başlık ekle

plt.show()
```

---

**Örnek 2:** Yatay bar grafiği.

```python
plt.figure()          # Yeni bir grafik figürü oluştur

# Yatay çubuk grafiği çiz
plt.barh(y=ozet.index, width=ozet.values, color="b")
      # - 'y=ozet.index'  Çubukların kategorik değerleri (sigara içme durumu gibi).
      # - 'width=ozet.values'  Çubukların uzunluğu (ödeme miktarları).
      # - 'color="b"'  Çubukların rengi mavi ("b") olarak ayarlanır.

plt.xlabel("Ödeme Miktarı")     # X eksenine etiket ekle (Ödeme miktarlarını gösterir)
plt.title("Yatay Bar Grafiği")  # Grafiğe başlık ekle
plt.show()
```

---

### **1.4.3 Pasta Grafiği (Pie Chart)**

**Örnek:** Bölgeye göre toplam ödeme miktarını gösteren pasta grafiği.

```python
# "bolge" sütununa göre gruplandırarak her bölgedeki toplam ödeme miktarını hesapla
ozet_bolge = insurance_df.groupby("bolge", observed=True)["odemeMiktari"].sum()
        # - 'groupby("bolge")'  Veriyi bölgelere göre gruplar.
        # - '["odemeMiktari"].sum()'  Her bölge için ödeme miktarlarının toplamını hesaplar.

etiketler = ozet_bolge.index  # Pasta grafiği için bölge isimlerini etiket olarak al
degerler = ozet_bolge.values  # Pasta dilimlerinin büyüklüğünü belirlemek için ödeme miktarlarını al
renkler = sns.color_palette("viridis", len(etiketler))  # Pasta grafiği için renk paleti oluştur (Her dilime farklı bir renk atar).
explode_vals = [0] * len(etiketler)                     # Başlangıçta tüm dilimleri patlatma (normal göster)

# Eğer en az 3 bölge varsa, üçüncü dilimi patlat (grafikte öne çıkarmak için)
if len(etiketler) >= 3:
    explode_vals[2] = 0.2  # 3. dilimi biraz dışarı çıkar

plt.figure()  # Yeni bir grafik figürü oluştur

plt.pie(
    degerler,               # Pasta dilimlerinin büyüklüğü
    explode=explode_vals,   # Hangi dilimler öne çıkarılacak (explode effect)
    labels=etiketler,       # Dilimlerin etiketleri (Bölge isimleri)
    autopct="%4.1f%%",      # Dilimlerin yüzdesini göster (4.1f → %4.1 formatında göster)
    shadow=True,            # Gölgeli efekt ekle (grafiği daha okunaklı yapar)
    startangle=360,         # Grafiği 360 dereceden başlat (dilimlerin konumunu belirler)
    colors=renkler          # Dilimler için renk paletini uygula
)

plt.title("Bölgeye Göre Toplam Ödeme Miktarı")  # Grafiğe başlık ekle
plt.show()
```

---

### **1.4.4 Serpilme/Dağılım Plot (Scatter Plot)**

**Örnek 1:** Yaş ile VKİ arasındaki ilişki.

```python
plt.figure()  # Yeni bir grafik figürü oluştur

# Yaş ve VKİ (Vücut Kitle İndeksi) arasındaki ilişkiyi gösteren saçılım grafiği (scatter plot) çiz.
plt.scatter(insurance_df["yas"], insurance_df["vki"])
      # - 'insurance_df["yas"]'  X ekseni için yaş verileri.
      # - 'insurance_df["vki"]'  Y ekseni için vücut kitle indeksi (VKİ) verileri.
      # - 'plt.scatter()'  Her bir veri noktasını bir nokta olarak çizer (korelasyon olup olmadığını anlamak için kullanılır).

plt.xlabel("Yaş")                  # X ekseni etiketini belirle (Yaş bilgisi)
plt.ylabel("Vücut Kitle İndeksi")  # Y ekseni etiketini belirle (VKİ bilgisi)
plt.title("Yaş ve VKİ İlişkisi")   # Grafiğe başlık ekle
plt.show()
```

---

**Örnek 2:** Yaş ve ödeme miktarı (Sigara Durumuna Göre)

```python
plt.figure()  # Yeni bir grafik figürü oluştur

# Yaş ve ödeme miktarı arasındaki ilişkiyi gösteren saçılım grafiği çiz (Seaborn kullanarak).
sns.scatterplot(x="yas", y="odemeMiktari", hue="sigaraDurum", data=insurance_df)
      # - 'x="yas"'  X eksenine yaş sütunu yerleştirilir.
      # - 'y="odemeMiktari"'  Y eksenine ödeme miktarı sütunu yerleştirilir.
      # - 'hue="sigaraDurum"'  Sigara içme durumuna göre noktaların rengi belirlenir (Sigara içenler ve içmeyenler farklı renklerde olur).
      # - 'data=insurance_df'  Verinin hangi veri çerçevesinden alınacağını belirtir.

plt.title("Yaş ve Ödeme Miktarı (Sigara Durumuna Göre)")
plt.show()
```

---

**Örnek 3:** Seçili müşterilerin Yaş ve ödeme miktarı

```python
# Seçili müşterilerin indeks numaralarını içeren liste oluştur (Müşteri ID gibi düşünülebilir).
secim = [1072, 548, 1032, 437, 154, 653, 645, 862, 25, 603]

# Seçilen indekslerin veri çerçevesinin sınırlarını aşmadığından emin olmak için filtreleme yap
secim = [i for i in secim if i < len(insurance_df)]
        # - 'if i < len(insurance_df)'  Eğer indeks değeri veri çerçevesindeki toplam satır sayısını aşarsa listeden çıkarılır.
        # - Bu işlem, "IndexError" hatasını önlemek için yapılır.

# Seçili müşterilerin yaş ve ödeme miktarı bilgilerini içeren alt veri kümesi oluştur.
altkume = insurance_df.iloc[secim][["yas", "odemeMiktari"]]
        # - 'insurance_df.iloc[secim]'  Seçili indekslere göre satırları alır.
        # - '[["yas", "odemeMiktari"]]'  Sadece "yaş" ve "ödeme miktarı" sütunlarını seçer.

plt.figure()  # Yeni bir grafik figürü oluştur

# Seçili müşterilerin yaş ve ödeme miktarı arasındaki ilişkiyi gösteren saçılım grafiği çiz.
plt.scatter(altkume["yas"], altkume["odemeMiktari"])
        # - 'altkume["yas"]'  X ekseni için yaş verileri.
        # - 'altkume["odemeMiktari"]'  Y ekseni için ödeme miktarları.
        # - 'plt.scatter()'  Her müşteri için bir nokta olarak veriyi görselleştirir.

plt.xlabel("Yaş")
plt.ylabel("Ödeme Miktarı")
plt.title("Seçili Müşterilerin Yaş ve Ödeme Miktarı")
plt.show()
```

---

### **1.4.5 Histogram**

```python
plt.figure()
# VKİ dağılımını gösteren histogram (8 bin)
sns.histplot(data=insurance_df, x="vki", color="yellow", bins=8)
        # - 'data=insurance_df'  Veriyi seçer.
        # - 'x="vki"'            X ekseninde VKİ değerleri kullanılır.
        # - 'color="yellow"'     Histogram sarı renkte çizilir.
        # - 'bins=8'             8 aralıklı bin (sütun) oluşturur.

plt.title("VKİ Histogram (8 Bin)")
plt.show()


plt.figure()
# VKİ dağılımını gösteren histogram (12 bin)
sns.histplot(data=insurance_df, x="vki", color="darkblue", bins=12)
        # - 'color="darkblue"'   Histogram koyu mavi renkte çizilir.
        # - 'bins=12'            12 aralıklı bin (sütun) oluşturur.

plt.title("VKİ Histogram (12 Bin)")
plt.show()


# VKİ değişkeninin tanımlayıcı istatistiklerini ekrana yazdır
print("VKİ için describe:")
print(insurance_df["vki"].describe())
        # - 'describe()'         Ortalama, min, max, standart sapma gibi istatistikleri gösterir.
```

---

**VKİ İçin İstatistikler:**
```
count    1338.000000
mean       30.663397
std         6.098187
min        15.960000
25%        26.296250
50%        30.400000
75%        34.693750
max        53.130000
Name: vki, dtype: float64
```
