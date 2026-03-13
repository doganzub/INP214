# **2. Veri Hazırlama (Data Preparation)**

> ## Google LM Studio — Slayt Sunusu Oluşturma Promptu
>
> **Bu dokümanı Google LM Studio'ya kaynak olarak yükleyin, ardından "Slayt Sunusu" aracını seçip aşağıdaki promptu yapıştırın.**
>
> ---
>
> **PROMPT:**
>
> *Bu dokümandaki ders notunu kullanarak üniversite düzeyinde bir slayt sunusu oluştur. Aşağıdaki tüm kurallara MUTLAKA uy.*
>
> ---
>
> **HEDEF KİTLE:**
>
> *Programlama, Python ve veri bilimi konusunda HİÇBİR ön bilgisi olmayan, konuya SIFIRDAN başlayan üniversite öğrencileri. Öğrencinin "DataFrame nedir?", "NaN ne demek?", "import ne işe yarar?" gibi en temel soruları bile bilmediğini varsay. Her kavramı ilk kez duyan birine anlatır gibi yaz.*
>
> ---
>
> **TASARIM VE ARKA PLAN KURALLARI (KRİTİK — MUTLAKA UY):**
>
> *1. **DÜMDÜZ BEYAZ ARKA PLAN:** Tüm slaytlarda arka plan SADECE düz beyaz (#FFFFFF) olmalı. Gradyan, desen, doku, resim, illüstrasyon veya herhangi bir arka plan görseli KESINLIKLE KULLANMA. Hiçbir slaytın arka planında dekoratif öğe olmamalı.*
> *2. **3D GÖRSEL YASAĞI:** Hiçbir slayta 3D illüstrasyon, 3D nesne, 3D ikon veya fotorealistik görsel KOYMA. Bu tür görseller akademik değildir.*
> *3. **İLLÜSTRASYON VE SÜSLEME YASAĞI:** Huni, makine, fabrika, robot, karakter, metafor görseli veya benzer dekoratif illüstrasyonlar KULLANMA. Bunlar ders notuna uygun değildir.*
> *4. **SADECE bu görsel türlerini kullan:**
>   - Düz metin ve madde işaretleri (bullet points)
>   - Basit düz tablolar (siyah kenarlıklı, beyaz arka planlı)
>   - Basit 2D akış şemaları (düz kutucuklar + oklar, tek renk kenarlık)
>   - Kod blokları (açık gri arka planlı, monospace yazı tipi)
>   - Basit 2D kutu grafiği (boxplot) çizimleri (sadece çizgiler ve etiketler)*
> *5. **MİNİMAL RENK PALETİ:** En fazla 3 renk kullan: siyah (metin), koyu mavi (başlıklar ve vurgular), açık gri (kod blokları arka planı). Başka renk KULLANMA. Parlak, canlı, neon renk kullanma.*
> *6. **TEMİZ DÜZEN:** Her slaytda bol boşluk (white space) bırak. Slaytı bilgiyle doldurup sıkıştırma. Az metin, çok boşluk.*
>
> ---
>
> **PEDAGOJİK YAKLAŞIM:**
>
> *7. **Basitten karmaşığa ilerleme:** Konuları ders notundaki sırayla sun. Her bölümde önce "Bu nedir ve neden önemli?" sorusunu cevapla, sonra kavramı açıkla, en son Python kod örneğini göster.*
> *8. **Sade ve anlaşılır dil:** Her teknik terimi ilk geçtiği yerde günlük dille açıkla. Örneğin: "NaN (Not a Number) = Eksik değer, yani tablodaki o hücre boş demektir." veya "DataFrame = Excel tablosu gibi düşünün, satır ve sütunlardan oluşan bir veri yapısı."*
> *9. **Bölümler arası bağlam:** Yeni konuya geçerken önceki konuyla bağlantı kur. Örneğin: "Az önce eksik verileri temizledik. Şimdi bu temiz veriyi kategorilere ayırmayı öğreneceğiz."*
> *10. **Pedagojik doğrulama:** Her slaytı sıfırdan başlayan bir öğrenci gözüyle kontrol et. Anlaşılmayan veya varsayım yapılan nokta varsa düzelt.*
>
> ---
>
> **SLAYT YAPISI:**
>
> *11. **Her slaytın formatı:** Başlık (koyu mavi, büyük punto) → Kısa açıklama (en fazla 3 cümle) → Tablo, kod bloğu veya madde listesi → Varsa kısa ipucu kutusu.*
> *12. **Kod blokları:** Python kodlarını açık gri arka planlı kutucuklarda, monospace yazı tipiyle göster. Her satırı kısa yorum satırıyla açıkla.*
> *13. **Özet slaytları:** Her ana bölümün sonunda 3-5 maddelik bir özet slaytı ekle.*
> *14. **Sunum süresi:** Yaklaşık 90 dakikalık bir ders için uygun uzunlukta olsun.*
>
> ---
>
> **DİL VE TON:**
>
> *15. **Dil:** Türkçe. Teknik terimler İngilizce parantez içinde verilsin. Örneğin: "Eksik Veri Tamamlama (Missing Data Imputation)".*
> *16. **Ton:** Akademik ve net. Gereksiz süslü cümleler kullanma. Kısa, öz ve bilgilendirici ol.*
>
> ---
>
> **YASAKLAR ÖZETİ (BUNLARI YAPMA):**
>
> *- Renkli veya desenli arka plan KULLANMA*
> *- 3D görsel, illüstrasyon, huni, makine, fabrika metaforu KULLANMA*
> *- Parlak, neon veya canlı renkler KULLANMA*
> *- Slaytı bilgiyle sıkıştırma, bol boşluk bırak*
> *- Ders notunda OLMAYAN bilgi veya görsel ekleme*
> *- Çocuksu, karikatürize veya dekoratif tasarım öğesi KULLANMA*
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
import numpy as np                                                  # NumPy: Matematiksel işlemler için kullanılır (örneğin: NaN değerleri, diziler)
import pandas as pd                                                 # pandas: Tablo şeklindeki verileri okumak, işlemek ve analiz etmek için kullanılır
import seaborn as sns                                               # seaborn: Güzel ve anlaşılır grafikler çizmek için kullanılır
import matplotlib.pyplot as plt                                     # matplotlib: Grafik çizim kütüphanesi (seaborn'un altyapısını oluşturur)
from matplotlib.cbook import boxplot_stats                          # boxplot_stats: Kutu grafiği için istatistik değerleri hesaplar
import random                                                       # random: Rastgele sayı üretmek için Python'un yerleşik modülü
from random import sample                                           # sample: Bir listeden tekrarsız rastgele eleman seçmek için kullanılır
from sklearn.model_selection import train_test_split                # train_test_split: Veriyi eğitim ve test setine otomatik bölmek için kullanılır
from sklearn.preprocessing import MinMaxScaler, StandardScaler     # MinMaxScaler: Verileri 0-1 arasına sıkıştırmak için, StandardScaler: Ortalama=0, std=1 yapmak için


print("Gerekli kütüphaneler başarıyla yüklendi.")
```

**Çıktı:**
```
Gerekli kütüphaneler başarıyla yüklendi.
```

---

## **2.2 Veri Okuma**

### Neden Önemli?
Veriyi doğru biçimde okumak ve bir **`DataFrame`** hâline getirmek, sonraki tüm veri ön işleme ve analiz adımları için kritik bir adımdır. Eğer veri yanlış bir konumdan okunursa veya sütun başlıkları hatalı tanımlanırsa, ileriki aşamalarda eksik ya da hatalı sonuçlar alabiliriz.

### Bu bölümde ne yapacağız?
- Google Drive'ı bağlayarak **(`mount`)** veri setinin bulunduğu klasöre erişeceğiz.
- **`automobile.csv`** dosyasını, pandas'ın **`read_csv`** fonksiyonunu kullanarak okuyacağız.
- Veri setinin sütun veri tiplerini **(`dtypes`)** inceleyeceğiz.
- Ayrıca **`head()`** fonksiyonuyla veri içeriğine hızlıca göz atacağız.

```python
# 1) Google Drive'i mount ediyoruz (Colab'da dosyalarimiza erismek icin Drive'i baglamamiz gerekir)
from google.colab import drive                                      # google.colab modulu sadece Google Colab ortaminda calisir
drive.mount('/content/drive', force_remount=True)                   # Drive'i '/content/drive' yoluna baglar, force_remount=True her seferinde yeniden baglanir

# 2) 'automobile.csv' dosyasini, Colab Notebooks klasorunden tam yol ile okuyoruz
veriSeti = pd.read_csv(                                             # pd.read_csv(): CSV dosyasini okuyup bir DataFrame (tablo) olusturur
    "/content/drive/MyDrive/Colab Notebooks/automobile.csv"         # Dosyanin Google Drive'daki tam yolu
)

# 3) Veri setinin boyutu ve sutun veri tipleri
print("Veri Seti Boyutu:", veriSeti.shape)                          # shape: (satir sayisi, sutun sayisi) seklinde boyutu gosterir
print("\nSutun Veri Tipleri:\n", veriSeti.dtypes)                   # dtypes: Her sutunun veri tipini gosterir (int64, float64, object vb.)
display(veriSeti.head(10))                                          # head(10): Tablonun ilk 10 satirini ekrana gosterir
```

---

## **2.3 Eksik Veri Tamamlama (Missing Data Imputation)**

### Neden Önemli?
Eksik veriler, modelin doğruluğunu olumsuz etkileyebilir veya hata oluşturabilir. Bu nedenle eksik verileri uygun yöntemlerle doldurmak **(`imputation`)**, veri kalitesini artırır ve analiz veya makine öğrenmesi modellerinden daha güvenilir sonuçlar elde etmemize yardımcı olur.

### Bu bölümde ne yapacağız?
- **`normalized_losses`**, **`horsepower`** ve **`peak_rpm`** sütunlarındaki **'?'** karakterlerini **`NaN`'e** dönüştüreceğiz.
- Bu sütunların veri tipini sayısal **`(float64)`** hâline getireceğiz.
- Eksik veri sayısını inceleyip, ortalama değerle dolduracağız.
- **`fillna()`** metodu kullanımını örnek olarak göreceğiz.

```python
# On kontrol: '?' karakteri iceren sutunlari tespit edelim
for col in veriSeti.columns:                                        # veriSeti.columns: Tum sutun isimlerini listeler
    soru_isareti = (veriSeti[col] == "?").sum()                     # Her sutunda '?' olan hucrelerin sayisini hesaplar
    if soru_isareti > 0:                                            # Eger '?' sayisi 0'dan buyukse ekrana yazdir
        print(f"{col} sutununda '?' sayisi: {soru_isareti}")

# 1) '?' karakterini NaN'e donusturme (tum ilgili sutunlar icin)
eksik_sutunlar = ["normalized_losses", "horsepower", "peak_rpm"]    # Icinde '?' bulunan sutunlari bir listeye topluyoruz
for col in eksik_sutunlar:                                          # Her bir sutun icin dongu baslatiyoruz
    veriSeti.loc[veriSeti[col] == "?", col] = np.nan                # loc[kosul, sutun]: '?' olan hucreleri bulup NaN (bos deger) ile degistir

# 2) Ilgili sutunlarin tipini float64'e donusturme
for col in eksik_sutunlar:                                          # Ayni sutunlar icin tekrar dongu
    veriSeti[col] = veriSeti[col].astype("float64")                 # astype("float64"): Sutunu metin tipinden ondalikli sayi tipine cevirir

# 3) Eksik veri sayisini (ilk kontrol) ekrana bastirma
print("\nEksik Veri Sayisi (Once):\n", veriSeti.isnull().sum())     # isnull().sum(): Her sutundaki NaN (bos) degerlerin sayisini verir

# 4) fillna() metodu ile ortalama ile doldurma
for col in eksik_sutunlar:                                          # Eksik deger iceren her sutun icin
    veriSeti[col] = veriSeti[col].fillna(veriSeti[col].mean().round(0))  # fillna(): NaN degerleri, sutunun ortalamasiyla doldurur. round(0): tam sayiya yuvarlar

print("\nEksik Veri Sayisi (Sonra):\n", veriSeti.isnull().sum())    # Doldurma isleminden sonra tekrar kontrol: Artik 0 olmali
```

---

## **2.4 Veri Ayrıklaştırma (Binning / Discretization)**

### Neden Önemli?
- Sürekli (sayısal) veriler, kategorik (gruplandırılmış) değerlere dönüştürülür.
- Bu dönüşümle, veriye yeni bir sütun eklenir veya mevcut sütun sınıflara ayrılır.
- Amaç: Sayısal değerleri daha anlamlı ve genellenmiş kategorilere indirgemektir.

Örneğin: `city_mpg` değişkeni;
- **21'in altında** ise → **Düşük**
- **21 – 30 arası** ise → **Orta**
- **30 ve üstü** ise → **Yüksek** olarak sınıflandırılabilir.

Bu işlem sonucunda:
- Veri setine **yeni bir kategorik sütun (örneğin: `durum`)** eklenir.
- Satır sayısı değişmez; sadece her satır bir kategoriye atanır.

---

### Bu bölümde ne yapacağız?
- `city_mpg` sütununu **Düşük**, **Orta** ve **Yüksek** kategorilerine ayıracağız.
- Dört farklı yöntemle ayrıklaştırma işlemi gerçekleştireceğiz:

I. Yöntem:

 **1.** **`lambda` + `map()`** fonksiyonu ile manuel koşullu sınıflandırma yapacağız.

II. Yöntem:

**2.1.** **`pd.cut()`** fonksiyonu ile **sabit aralık (fixed interval)** yöntemi uygulayacağız.
**2.2.** **`pd.qcut()`** fonksiyonu ile **eşit frekans (quantile)** yöntemi kullanacağız.
**2.3.** **`pd.cut()`** fonksiyonu ile **eşit genişlik (equal interval)** yöntemini uygulayacağız.

```python
# ------------------------------------------------------------
# I. Yontem: lambda + map
# ------------------------------------------------------------
# lambda ifadesi, 'city_mpg' degerine gore kosullu atama yapar:
# - x < 21 ise "Dusuk"
# - 21 <= x < 30 ise "Orta"
# - x >= 30 ise "Yuksek" olarak etiketler.
veriSeti["durum"] = veriSeti.city_mpg.map(                          # map(): Her satira tek tek bir fonksiyon uygular
    lambda x: "Dusuk" if x < 21 else ("Orta" if (x >= 21 and x < 30) else "Yuksek")  # lambda: Isimsiz kisa fonksiyon tanimlar
).astype("category")                                                # astype("category"): Sutunu kategorik (sinifli) veri tipine cevirir

print("Durum (lambda) dagilim:\n", veriSeti.durum.value_counts())   # value_counts(): Her kategoriden kac tane oldugunu sayar
print(f"\n{'-'*82}\n")

#----------------------------------------------------------------------------------
# II. Yontem:
#----------------------------------------------------------------------------------

# II.1: Yontem: Fixed (sabit) araliklarla bolme
bolmeKategorileri = ["Dusuk", "Orta", "Yuksek"]                    # Olusturulacak kategori isimleri
bolmeler = [12, 20.9, 29.9, 50]                                    # Sinir degerleri: 12-20.9=Dusuk, 20.9-29.9=Orta, 29.9-50=Yuksek
veriSeti["durum"] = pd.cut(                                         # pd.cut(): Sayisal degerleri belirlenen araliklara gore keser ve etiketler
    veriSeti["city_mpg"],                                           # Hangi sutunu bolecegimizi belirtiyoruz
    bins=bolmeler,                                                  # bins: Bolme sinirlarini tanimlar
    labels=bolmeKategorileri                                        # labels: Her araliga verilecek isimler
)
print("Durum (fixed cut) dagilim:\n", veriSeti.durum.value_counts())
print(f"\n{'-'*82}\n")

# II.2: Yontem: Equal Frequency (qcut)
durum_ef = pd.qcut(veriSeti["city_mpg"], q=3)                      # pd.qcut(): Verileri esit sayida gozlem icerecek sekilde 3 gruba boler

print("Durum (Esit frekans) dagilim:\n", durum_ef.value_counts())
print(f"\n{'-'*82}\n")

# II.3: Yontem: Equal Interval (esit genislik)
durum_ea = pd.cut(veriSeti["city_mpg"], bins=3)                     # pd.cut(bins=3): Deger araligini esit genislikte 3 parcaya boler
print("Durum (Esit genislik) dagilim:\n", durum_ea.value_counts())
print(f"\n{'-'*82}\n")
```

---

## **2.5 Veri Seti Özeti (describe)**

### Neden Önemli?
Veri setinin genel istatistiksel özelliklerini (ortalama, std, min, max vb.) görmek, veri hakkında hızlıca fikir sahibi olmamızı sağlar. Hem sayısal hem de kategorik sütunların özetini almak, veri analizinin sonraki adımlarını planlamada bize rehberlik eder.

### Bu bölümde ne yapacağız?
- `pd.set_option("display.max_columns", 20)` ayarıyla, DataFrame ekrana basılırken en fazla kaç sütun gösterileceğini belirleyeceğiz.
- `veriSeti.describe(include="all")` fonksiyonunu kullanarak, tüm sütunların (sayısal ve kategorik) temel istatistiksel özetini görüntüleyeceğiz.

```python
# 1) pd.set_option ile ekrana basilacak sutun sayisini 20 ile sinirlandiriyoruz
pd.set_option("display.max_columns", 20)                            # Cok sutunlu tablolarda hepsinin gorunmesini saglar (varsayilan sinir dusuktur)

# 2) describe(include="all") ile sayisal ve kategorik tum sutunlarin ozet istatistiklerini aliyoruz
print("Veri Seti Ozeti (describe, include='all'):\n", veriSeti.describe(include="all"))  # describe(): Ortalama, std, min, max gibi temel istatistikleri gosterir
```

---

## **2.6 Veri Gruplandırma (Aggregate)**

### Neden Önemli?
Makine öğrenmesi ve veri bilimi süreçlerinde, bazen tüm veri setini tek bir bütün olarak değerlendirmek yerine, verileri belirli özelliklere göre alt gruplara ayırıp ayrı ayrı incelemek faydalıdır. Bu işlem sayesinde her bir alt grup hakkında istatistiksel özet bilgiler elde edebiliriz.

**Örneğin:** Bir otomobil verisinde araçların şehir içi yakıt tüketimini (city_mpg) "durum" kategorisine (Düşük, Orta, Yüksek) göre ayrı ayrı inceleyebilirsiniz.

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
# 1. Adim: "durum" kategorisine gore "city_mpg" degiskeninin temel istatistiklerini cikar
df_ozet = veriSeti.groupby("durum", observed=False)["city_mpg"].describe().round(2)  # groupby(): Veriyi "durum" sutununa gore gruplar, describe(): Her grubun istatistiklerini hesaplar

# 2. Adim: 'durum' degiskeni indeks olarak degil, sutun olarak gorunsun diye resetlenir
df_ozet.reset_index(inplace=True)                                   # reset_index(): Grup isimlerini normal bir sutuna cevirir, inplace=True: Degisikligi kalici yapar

# 3. Adim: Jupyter defteri kullaniliyorsa tablo seklinde gorsellestirir
display(df_ozet)                                                    # display(): Tabloyu guzel formatli sekilde ekranda gosterir (sadece Jupyter/Colab'da calisir)
```

---

## **2.7 Tekrarlayan Satırların Bulunması (Duplicated Rows)**

### Neden Önemli?
Tekrarlayan **(duplicate)** satırlar, veri analizi sonuçlarını yanıltabilir. Aynı gözlemin veri setinde birden fazla kez yer alması, ortalama ve diğer istatistiksel hesaplamaları etkileyerek hatalı sonuçlara yol açabilir. Bu nedenle tekrarlayan satırları tespit edip, gereksiz olanları temizlemek veri kalitesini artırır.

### Bu bölümde ne yapacağız?
- `duplicated()` fonksiyonunu kullanarak tekrarlayan satırları bulacağız.
- `drop_duplicates()` ile tekrarlayanları temizleyeceğiz.
- Tekrarlayan satırları bulmak için farklı keep parametreleri **(örneğin "first", "last")** deneyeceğiz.

```python
# 1) duplicated() ile tekrarlayan satirlari tespit ediyoruz
tekrarlar_f = veriSeti.duplicated(keep="first")                     # keep="first": Ilk tekrari tutar (False), sonrakileri True isaretler
tekrarlar_l = veriSeti.duplicated(keep="last")                      # keep="last": Son tekrari tutar (False), onceki tekrarlari True isaretler

# 2) Herhangi birinin True oldugu satirlar, tekrarlayan satirlardir
indislerim = tekrarlar_f | tekrarlar_l                              # | (veya): Iki kosuldan en az biri True ise o satir tekrar eden satirdir

# 3) Tekrarlayan gozlemleri ekrana basalim
print("Tekrarlayan Gozlemler:\n", veriSeti[indislerim])             # veriSeti[indislerim]: Sadece True olan (tekrarlayan) satirlari filtreler

# 4) drop_duplicates() ile veri setinden tekrar eden satirlari kaldiriyoruz
veriSeti2 = veriSeti.drop_duplicates()                              # drop_duplicates(): Tekrarlayan satirlari siler, her satirdan sadece birini birakir

# 5) Kaldirma isleminden sonra veri setinin boyutunu (shape) inceleyerek degisikligi gozlemleyebiliriz
print("\nTekrarlayanlardan arindirilmis veriSeti2 shape:", veriSeti2.shape)  # Satir sayisi azaldiysa tekrarlayan satirlar vardi demektir
```

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
# 1. Kartil (Q1) ve 3. Kartil (Q3) degerlerini hesaplayalim
q1 = veriSeti["horsepower"].quantile(0.25)                          # quantile(0.25): Verinin alt %25'lik degerini bulur (Q1 = 1. ceyrek)
q3 = veriSeti["horsepower"].quantile(0.75)                          # quantile(0.75): Verinin ust %75'lik degerini bulur (Q3 = 3. ceyrek)

# IQR (ceyrekler arasi aciklik): Q3 - Q1
IQR = q3 - q1                                                       # IQR: Verinin orta %50'sinin yayildigi aralik, aykiri deger tespitinde kullanilir

# Alt ve ust sinirlari belirliyoruz
alt = q1 - 1.5 * IQR                                                # Alt sinir: Bu degerin altindaki her sey aykiri deger sayilir
ust = q3 + 1.5 * IQR                                                # Ust sinir: Bu degerin ustundeki her sey aykiri deger sayilir

print(f"Aykiri deger alt siniri: {alt}, ust siniri: {ust}")          # Hesaplanan alt ve ust sinirlari ekrana yazdirir
```

```python
# Aykiri olan satirlarin indekslerini buluyoruz
ust_aykiriDegerInd = np.where(veriSeti["horsepower"] >= ust)[0]     # np.where(): Kosulu saglayan satirlarin indeks numaralarini dondurur
alt_aykiriDegerInd = np.where(veriSeti["horsepower"] <= alt)[0]     # Alt sinirin altindaki degerlerin indekslerini bulur

# Ust sinirin uzerindeki aykiri degerleri indeks : deger formatinda yazdiriyoruz
print("Ust sinirin uzerindeki aykiri degerler:")
for i in ust_aykiriDegerInd:                                        # Her bir aykiri degerin indeksini tek tek gezeriz
    print(f"Indeks: {i}, Deger: {veriSeti['horsepower'][i]}")       # f-string: Degiskenleri metin icine yerlestirmek icin kullanilir

# Alt sinirin altindaki aykiri degerleri indeks : deger formatinda yazdiriyoruz
print("\nAlt sinirin altindaki aykiri degerler:")
for i in alt_aykiriDegerInd:                                        # Alt sinir icin de ayni islemi tekrarlariz
    print(f"Indeks: {i}, Deger: {veriSeti['horsepower'][i]}")
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
# Basit Kutu Grafigi

import seaborn as sns                                               # seaborn kutuphanesini tekrar import ediyoruz (guvenlik icin)
import matplotlib.pyplot as plt                                     # matplotlib grafik cizim kutuphanesi

plt.figure(figsize=(8, 5))                                          # figsize=(genislik, yukseklik): Grafik boyutunu inc cinsinden ayarlar
sns.boxplot(y="horsepower", data=veriSeti)                          # boxplot(): horsepower sutunu icin kutu grafigi cizer (aykiri degerler daire olarak gorunur)
plt.title("Horsepower Niteligne Ait Kutu Grafigi")                  # title(): Grafigin basligini belirler
plt.show()                                                          # show(): Grafigi ekranda gosterir
```

```python
# Aciklamali Kutu Grafigi

plt.figure(figsize=(10, 7))                                         # Daha buyuk bir grafik alani olustur

# Aykiri degerleri gizleyerek kutu grafigi ciz
sns.boxplot(y="horsepower", data=veriSeti, showfliers=False)        # showfliers=False: Aykiri degerleri kutu grafiginde gizler (biz kendimiz ekleyecegiz)
plt.title("Gercek Verilerle Horsepower Degiskenine Ait Aciklamali Kutu Grafigi")

# Istatistik degerleri
ortalama = veriSeti["horsepower"].mean()                            # mean(): Sutunun aritmetik ortalamasini hesaplar
medyan = veriSeti["horsepower"].median()                            # median(): Verileri siralayinca ortaya dusen degeri bulur
q1 = veriSeti["horsepower"].quantile(0.25)                          # 1. ceyrek (alt %25)
q3 = veriSeti["horsepower"].quantile(0.75)                          # 3. ceyrek (ust %25)
iqr = q3 - q1                                                       # Ceyrekler arasi aciklik
alt = q1 - 1.5 * iqr                                                # Aykiri deger alt siniri
ust = q3 + 1.5 * iqr                                                # Aykiri deger ust siniri

# Ortalama (turuncu)
plt.plot([0], [ortalama], "o-", color="orange")                     # plot(): Grafik uzerine bir nokta koyar ("o-" = daire isareti)
plt.text(0.1, ortalama, f"Ortalama:\n{ortalama:.2f}", color="orange", fontsize=10)  # text(): Noktanin yanina aciklama yazisi ekler

# Medyan (siyah nokta)
plt.plot(0, medyan, "ko")                                           # "ko" = siyah (k=black) daire (o=circle)
plt.text(-0.35, medyan, f"Medyan\n{medyan:.2f}", fontsize=10)

# Q1
plt.plot(0, q1, "ks")                                               # "ks" = siyah kare (s=square)
plt.text(-0.35, q1, f"Q1 (Alt Ceyrek)\n{q1:.2f}", fontsize=9)

# Q3
plt.plot(0, q3, "ks")
plt.text(-0.35, q3, f"Q3 (Ust Ceyrek)\n{q3:.2f}", fontsize=9)

# Alt sinir (mavi kare)
plt.plot(0, alt, "bs")                                               # "bs" = mavi (b=blue) kare (s=square)
plt.text(0.15, alt + 2, f"Alt Sinir\n{alt:.2f}", color="blue", fontsize=9)

# Ust sinir (mavi kare)
plt.plot(0, ust, "bs")
plt.text(0.15, ust + 2, f"Ust Sinir\n{ust:.2f}", color="blue", fontsize=9)

# Aykiri degerler (siyah daire)
for i, val in enumerate(veriSeti["horsepower"]):                     # enumerate(): Her degeri indeks numarasiyla birlikte gezer
    if val > ust or val < alt:                                       # Eger deger sinir disindaysa -> aykiri degerdir
        plt.plot(0, val, "ko")                                       # Aykiri degeri siyah daire olarak ciz
        x_offset = 0.2 if i % 2 == 0 else 0.25                      # Yazilar ust uste binmesin diye konum kaydirma
        plt.text(x_offset, val, f"{val:.1f}", fontsize=8, color="black")

plt.ylabel("Horsepower")                                            # Y ekseninin etiketini belirler
plt.xticks([])                                                       # X eksenindeki isaretleri gizler (tek degisken oldugu icin gerekmez)
plt.show()
```

```python
# 4) Aykiri degerleri kaldirmak icin asagidaki satirlari yorumdan cikarabilirsiniz
# veriSeti.drop(index=ust_aykiriDegerInd, inplace=True)             # drop(index=...): Belirtilen indekslerdeki satirlari siler
# veriSeti.drop(index=alt_aykiriDegerInd, inplace=True)             # inplace=True: Silme islemini dogrudan veriSeti uzerinde uygular
```

---

## **2.9 Örnekleme (Sampling ve Stratified Sampling)**

### 2.9.1. Eğitim ve Test Veri Seti Oluşturma
Eğitim ve test veri seti oluşturma, model eğitimi ve doğrulama işlemleri için veriyi ayırma işlemidir.
 - Genellikle verinin **%70'i eğitim seti**, **%30'u ise test seti** olarak ayrılır.
 - Eğitim seti, makine öğrenmesi modelinin eğitilmesi için kullanılırken, test seti modelin doğruluğunu ve başarısını değerlendirmek için kullanılır.

```python
egitim = veriSeti.sample(frac=0.7, replace=False, random_state=1)   # sample(): Veri setinden rastgele satirlar secer
      # frac=0.7 -> veri setinin %70'ini sec (0.7 = %70 demektir)
      # replace=False -> ayni satir birden fazla kez secilmesin (tekrarsiz secim)
      # random_state=1 -> her calistirmada ayni satirlarin secilmesini saglar (tekrarlanabilirlik icin)

ind = veriSeti.index.isin(egitim.index)                             # isin(): Egitim setindeki satirlarin indekslerini ana veri setinde arar, True/False listesi dondurur

test = veriSeti[~ind]                                                # ~ind: True'lari False, False'lari True yapar -> egitim setinde OLMAYAN satirlari secer (test seti)

print("Egitim Seti Boyutu:", egitim.shape)                          # Egitim setinin satir ve sutun sayisini gosterir
print("Test Seti Boyutu:", test.shape)                              # Test setinin satir ve sutun sayisini gosterir
```

---

### 2.9.2. Tabakalı Örnekleme (Stratified Sampling)
Tabakalı örnekleme, verinin belirli gruplara (tabakalara) ayrılarak her gruptan orantılı bir şekilde örnekleme yapılmasıdır. Özellikle dengesiz veri setlerinde, her sınıfın doğru bir şekilde temsil edilmesini sağlar.

- Tüm veri setindeki sınıf oranı → eğitim ve test setine eşit şekilde dağılır.
- Model eğitiminde azınlık sınıfların ihmal edilmesi önlenir.
- Eğitim ve test setlerinde "durum" değişkeninin dağılımı korunur.

```python
egitim1, test1 = train_test_split(                                  # train_test_split(): Veri setini otomatik olarak egitim ve test setine ayirir
    veriSeti,                                                       # Bolunecek veri seti
    train_size=0.7,                                                 # train_size=0.7: Verinin %70'i egitim, %30'u test olacak
    stratify=veriSeti["durum"],                                     # stratify: "durum" sutunundaki sinif oranlarini egitim/test setlerinde de korur
    random_state=1                                                  # random_state=1: Her calistirmada ayni bolunmeyi garantiler
)

print("\nDurum Dagilimi (Tum veri):\n", veriSeti.durum.value_counts())    # Tum veri setindeki sinif dagilimini gosterir
print("\nDurum Dagilimi (Egitim seti):\n", egitim1.durum.value_counts())  # Egitim setindeki sinif dagilimi (oranlar korunmus olmali)
print("\nDurum Dagilimi (Test seti):\n", test1.durum.value_counts())      # Test setindeki sinif dagilimi (oranlar korunmus olmali)
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
# Kategorik degiskeni sayisal forma donusturme

# 1. Yontem: cat.codes (Etiket Kodlama)
veriSeti["durum_s1"] = veriSeti["durum"].cat.codes                  # cat.codes: Kategorik degiskeni sayilara cevirir (Dusuk=0, Orta=1, Yuksek=2)
print("durum_s1 deger dagilimi:", veriSeti["durum_s1"].value_counts())  # Her sayisal koddan kac tane oldugunu gosterir

# 2. Yontem: get_dummies() (Yapay/Dummy Kodlama)
if not {'Dusuk', 'Orta', 'Yuksek'}.issubset(veriSeti.columns):     # issubset(): Bu sutunlar zaten varsa tekrar eklememek icin kontrol eder
    durum_s2 = pd.get_dummies(veriSeti["durum"], dtype=int)         # get_dummies(): Her kategori icin ayri bir sutun olusturur (0 veya 1 degerli)
    veriSeti = pd.concat([veriSeti, durum_s2], axis=1)              # pd.concat(axis=1): Yeni sutunlari mevcut tablonun sagina ekler
    print("Yapay Kodlama ile eklenen sutunlar:", list(durum_s2.columns))  # Eklenen yeni sutun isimlerini yazdirir

display(veriSeti.head(5))                                           # Tablonun ilk 5 satirini gosterir (yeni sutunlari gorebilmek icin)
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
# Min-Max Normalizasyonu (verileri 0-1 arasina sikistirma)

# Sayisal sutunlari seciyoruz
sayisal_sutunlar = ["city_mpg", "engine_size", "horsepower", "curb_weight", "peak_rpm", "normalized_losses"]
veri = veriSeti[sayisal_sutunlar]                                   # Sadece normalizasyon uygulanacak sayisal sutunlari aliyoruz

scaler = MinMaxScaler()                                             # MinMaxScaler: Her degeri 0 ile 1 arasina sikistiracak nesneyi olusturur
scaler.fit(veri)                                                    # fit(): Verinin minimum ve maksimum degerlerini ogrenir (henuz donusum yapmaz)
n_veriSeti = scaler.transform(veri)                                 # transform(): Ogrenilen min-max degerlerine gore veriyi 0-1 arasina donusturur
n_veriSeti = pd.DataFrame(n_veriSeti, columns=veri.columns)        # Sonucu tekrar DataFrame (tablo) formatina cevirir, sutun isimlerini korur
print("\nMin-Max Normalizasyon sonrasi ilk 5 satir:\n", n_veriSeti.head())  # head(): Ilk 5 satiri gosterir, tum degerler artik 0-1 arasinda olmali
```
