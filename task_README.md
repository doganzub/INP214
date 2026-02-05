# Task Notebook Hazırlama Teknik Kılavuzu

Bu teknik kılavuz, uygulamalı makine öğrenmesi dersi için `SX_task_konu_adi.ipynb` formatında görev notebookları hazırlamak isteyen eğitmenler için referans niteliğindedir. Kılavuzu takip ederek, mevcut öğretim notebooklarınızı (`X_konu_adi.ipynb`) öğrencilerin görev tamamlayarak öğrenebileceği yapılandırılmış task notebooklarına dönüştürebilirsiniz.

## 1. Task Notebook Yapısı ve Temel Prensipler

Task notebookları şu temel prensiplere göre hazırlanmalıdır:

1. **Paralel İçerik Akışı**: Task notebook, öğretim notebookuna paralel bir akış izlemeli
2. **Boşluk Bırakma**: Öğrencilerin doldurması için boş hücreler bırakılmalı
3. **Zorluk Kademesi**: Zorluk seviyesi kademeli olarak artmalı
4. **Rehberli Öğrenme**: İpuçları ve yönergelerle rehberlik sağlanmalı
5. **Doğrulama Mekanizmaları**: Öğrencilerin sonuçlarını doğrulayabilecekleri test hücreleri eklenmeli

## 2. Öğretim Notebookundan Task Notebook Oluşturma Adımları

### 2.1. Başlangıç İçeriğinin Hazırlanması

**Adım 1**: Öğretim notebookunuz için bir SX_ önekli kopya oluşturun.

```bash
# Örnek (terminal):
cp 2_veri_hazirlama.ipynb S2_task_veri_hazirlama.ipynb
```

**Adım 2**: Temel kütüphane importlarını ve ortam kurulumunu koruyun. Bu bölümleri öğrenciler için hazır bırakmalısınız.

```python
# Bu hücreyi olduğu gibi bırakın
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Görselleştirme ayarları
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
```

**Adım 3**: Teorik açıklamaları olduğu gibi tutun veya hafifçe kısaltın. Öğrencilerin kavramsal anlayışı için gereklidir.

### 2.2. Kod Hücrelerini Task Formuna Dönüştürme

Öğretim notebookunda bulunan her kod hücresi için aşağıdaki yapıyı kullanın:

**Öğretim Notebookunda (2_veri_hazirlama.ipynb):**
```python
# Veri setini yükleyelim
df = pd.read_csv('heart.data.csv')
print(df.head())
```

**Task Notebookunda (S2_task_veri_hazirlama.ipynb):**
```python
# TODO: Veri setini yükleyin ve ilk 5 satırını görüntüleyin
# İpucu: pd.read_csv() fonksiyonunu kullanın

# Kodunuzu buraya yazın
```

**Dönüştürme Prensipleri:**
1. Her kod hücresini önce analiz edin:
   - Temel amaç nedir?
   - Hangi fonksiyonlar/yöntemler kullanılıyor?
   - Bu adımın öğrenme hedefi nedir?

2. Ardından şu kalıbı kullanın:
   - İlk satır: `# TODO: [yapılacak görev]`
   - İkinci satır: `# İpucu: [yardımcı bilgi, kullanılacak fonksiyon vb.]`
   - Bir boş satır
   - Son satır: `# Kodunuzu buraya yazın`

## 3. Zorluk Seviyesinin Kademeli Olarak Artırılması

Task notebookunun başında daha fazla yardım ve ipucu sunarken, ilerleyen bölümlerde aşamalı olarak ipuçlarını azaltın:

**Başlangıç Seviyesi (Yüksek Yardım):**
```python
# TODO: Veri setini yükleyin
# İpucu: pd.read_csv('heart.data.csv') komutunu kullanın

# Kodunuzu buraya yazın
```

**Orta Seviye (Orta Düzey Yardım):**
```python
# TODO: Veri setini yükleyin
# İpucu: pd.read_csv() fonksiyonunu kullanın

# Kodunuzu buraya yazın
```

**İleri Seviye (Minimum Yardım):**
```python
# TODO: Heart veri setini yükleyin ve ilk 5 satırını görüntüleyin

# Kodunuzu buraya yazın
```

## 4. Kontrol Noktaları Oluşturma

Öğrencilerin çözümlerini doğrulamaları için test hücreleri ekleyin:

```python
# Test - Sonucunuzu kontrol edin
try:
    if isinstance(df, pd.DataFrame) and df.shape[0] > 0:
        print("✓ Tebrikler! Veri setini başarıyla yüklediniz.")
        print(f"  Veri seti boyutu: {df.shape}")
    else:
        print("✗ Veri setini yükleme işlemi tamamlanmamış görünüyor.")
except NameError:
    print("✗ 'df' değişkeni tanımlanmamış. Lütfen kodunuzu kontrol edin.")
```

Test hücreleri şu özelliklere sahip olmalıdır:
1. Hata yakalama mekanizması (`try-except`)
2. Açık, öğretici geri bildirim
3. Doğru çözümün neye benzediğine dair ipuçları

## 5. Görev Türleri ve Şablonlar

### 5.1. Veri Yükleme ve İnceleme Görevleri

```python
# TODO: [veri_seti] veri setini yükleyin ve ilk 5 satırını görüntüleyin
# İpucu: pd.read_csv() fonksiyonunu kullanın

# Kodunuzu buraya yazın
```

### 5.2. Veri Ön İşleme Görevleri

```python
# TODO: Eksik değerleri tespit edin ve sayılarını görüntüleyin
# İpucu: isnull() ve sum() fonksiyonlarını kullanabilirsiniz

# Kodunuzu buraya yazın
```

### 5.3. Veri Görselleştirme Görevleri

```python
# TODO: [değişken] değişkeninin histogramını çizin
# İpucu: plt.hist() veya df['değişken'].hist() kullanabilirsiniz

# Kodunuzu buraya yazın
```

### 5.4. Model Oluşturma Görevleri

```python
# TODO: X ve y değişkenlerini kullanarak bir model oluşturun ve eğitin
# İpucu: model_adı() sınıfını import edin ve fit() metodunu kullanın

# Kodunuzu buraya yazın
```

### 5.5. Model Değerlendirme Görevleri

```python
# TODO: Modelin performansını değerlendirin
# İpucu: mean_squared_error, accuracy_score gibi metrikler kullanabilirsiniz

# Kodunuzu buraya yazın
```

## 6. Örnek Dönüşüm: Karma Kod

### Öğretim Notebookunda (2_veri_hazirlama.ipynb):

```python
# Kategorik değişkenleri one-hot encoding yapalım
df_encoded = pd.get_dummies(df, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
print(df_encoded.head())

# Veri setini normalize edelim
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
df_encoded[features] = scaler.fit_transform(df_encoded[features])
print(df_encoded.head())
```

### Task Notebookunda (S2_task_veri_hazirlama.ipynb):

```python
# TODO: Aşağıdaki kategorik değişkenleri one-hot encoding ile dönüştürün:
# 'sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'
# İpucu: pd.get_dummies() fonksiyonunu ve columns parametresini kullanın

# Kodunuzu buraya yazın


# Test - One-hot encoding kontrolü
try:
    if df_encoded.shape[1] > df.shape[1]:
        print("✓ Tebrikler! One-hot encoding başarıyla uygulandı.")
        print(f"  Orijinal veri setinde {df.shape[1]} sütun vardı, şimdi {df_encoded.shape[1]} sütun var.")
    else:
        print("✗ One-hot encoding doğru uygulanmamış görünüyor. Lütfen kodunuzu kontrol edin.")
except NameError:
    print("✗ 'df_encoded' değişkeni tanımlanmamış. Lütfen kodunuzu kontrol edin.")


# TODO: Aşağıdaki sayısal değişkenleri StandardScaler kullanarak normalize edin:
# 'age', 'trestbps', 'chol', 'thalach', 'oldpeak'
# İpucu 1: sklearn.preprocessing modülünden StandardScaler sınıfını import etmeniz gerekiyor
# İpucu 2: fit_transform() metodunu kullanın

# Kodunuzu buraya yazın


# Test - Normalizasyon kontrolü
try:
    numeric_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    if all(abs(df_encoded[numeric_cols].mean()).max() < 0.01) and all(abs(df_encoded[numeric_cols].std() - 1).max() < 0.01):
        print("✓ Tebrikler! Normalizasyon başarıyla uygulandı.")
        print("  Sayısal değişkenlerin ortalaması yaklaşık 0, standart sapması yaklaşık 1.")
    else:
        print("✗ Normalizasyon doğru uygulanmamış görünüyor. Lütfen kodunuzu kontrol edin.")
except (NameError, KeyError):
    print("✗ Hata: Değişkenler doğru tanımlanmamış veya dönüştürülmemiş.")
```

## 7. Task Notebook Yazımında Dikkat Edilecek Noktalar

1. **Açık ve Net Yönergeler**: Öğrencilerin ne yapması gerektiğini net olarak anlamasını sağlayın.
2. **Kademeli Zorluk**: Notebook ilerledikçe ipuçlarını azaltarak zorluk seviyesini artırın.
3. **Test Mekanizmaları**: Her önemli adım için öğrencinin kendini değerlendirebileceği test hücreleri ekleyin.
4. **Teorik Bağlantılar**: Görevleri teorik bilgilerle ilişkilendirin, uygulama öncesi kavramsal açıklamaları koruyun.
5. **Hazır Kütüphaneler**: Gerekli kütüphane importlarını ve ortam kurulumlarını hazır verin.
6. **Öğrenme Hedefleri**: Her bölümün başında o bölümdeki görevlerin hangi öğrenme hedeflerine hizmet ettiğini belirtin.

## 8. Örnek Task Notebook Hazırlama Süreci (2_veri_hazirlama.ipynb → S2_task_veri_hazirlama.ipynb)

1. Öğretim notebookunu analiz edin ve bölümlere ayırın
2. Her bölüm için öğrenme hedeflerini belirleyin
3. Her kod hücresini uygun zorluk seviyesinde task formatına dönüştürün
4. Teorik açıklamaları koruyun veya gerektiğinde kısaltın
5. Test hücreleri ekleyin
6. Zorluk seviyesinin kademeli olarak arttığından emin olun
7. Hazır kod bloklarını (kütüphane importları gibi) koruyun
8. Görsel formatlamaya dikkat edin (markdown hücrelerini düzenli kullanın)

## 9. Öğretim ve Task Notebookları Arasındaki Temel Farklılıklar

Task ve öğretim notebookları arasında yapısal ve pedagojik olarak önemli farklılıklar vardır:

### 9.1. İçerik Organizasyonu Karşılaştırması

| Özellik | Öğretim Notebookları | Task Notebookları |
|---------|----------------------|-------------------|
| Kod Hücreleri | Tam çözümler içerir | Boşluklar ve tamamlanacak kısımlar içerir |
| Teorik Açıklamalar | Detaylı ve kapsamlı | Özet ve yönlendirici |
| Kütüphane İmportları | Adım adım gösterilir | Genellikle hazır verilir |
| Çıktı Görselleştirmeleri | Sonuçlar görüntülenir | Öğrencinin oluşturması beklenir |
| Kod Açıklamaları | Detaylı yorumlar içerir | TODO ve ipuçları formatındadır |

### 9.2. Pedagojik Yaklaşım Farklılıkları

* **Öğretim Notebookları**: "Göster ve anlat" yaklaşımı ile bilgi aktarır
* **Task Notebookları**: "Yap ve öğren" prensibiyle aktif öğrenmeyi teşvik eder

### 9.3. Örnek Dönüşümler: K-Means Kümeleme

**Öğretim Notebookunda (3_kmeans_kumeleme.ipynb):**
```python
# K-Means modelini oluşturalım
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Küme etiketlerini alalım
clusters = kmeans.labels_

# Sonuçları görselleştirelim
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', s=50, alpha=0.8)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', s=200, alpha=0.8, marker='X')
plt.title('K-Means Kümeleme Sonuçları')
plt.xlabel('Özellik 1')
plt.ylabel('Özellik 2')
plt.show()
```

**Task Notebookunda (S3_task_kmeans_kumeleme.ipynb):**
```python
# TODO: Veri için uygun bir K-Means modeli oluşturun ve eğitin
# İpucu 1: sklearn.cluster modülünden KMeans sınıfını import edin
# İpucu 2: 3 küme kullanın ve random_state=42 ayarlayın

# Kodunuzu buraya yazın


# Test - Model kontrolü
try:
    if isinstance(kmeans, KMeans) and hasattr(kmeans, 'cluster_centers_') and kmeans.n_clusters == 3:
        print("✓ K-Means modeli başarıyla oluşturuldu ve eğitildi.")
        print(f"  Küme merkezleri şekli: {kmeans.cluster_centers_.shape}")
    else:
        print("✗ K-Means modeli doğru oluşturulmamış veya eğitilmemiş görünüyor.")
except NameError:
    print("✗ 'kmeans' değişkeni tanımlanmamış. Lütfen kodunuzu kontrol edin.")


# TODO: Küme etiketlerini alın ve veriyi renklendirilmiş kümelerle görselleştirin
# İpucu 1: Etiketler için kmeans.labels_ kullanabilirsiniz
# İpucu 2: plt.scatter() ile görselleştirme yapabilirsiniz
# İpucu 3: Küme merkezlerini kırmızı 'X' ile işaretlemeyi unutmayın

# Kodunuzu buraya yazın
```

## 10. Farklı Konular İçin Özel Task Şablonları

### 10.1. Veri Görselleştirme için Task Formatı

Veri görselleştirme görevlerinde görsel kalite ve açıklamaların önemi vurgulanmalı:

```python
# TODO: [değişken1] ve [değişken2] arasındaki ilişkiyi gösteren bir scatter plot oluşturun
# İpucu 1: plt.scatter() fonksiyonunu kullanın
# İpucu 2: Eksenleri, başlığı ve uygun bir renk şeması eklemeyi unutmayın

# Kodunuzu buraya yazın


# Test - Görselleştirme kontrolü
try:
    current_fig = plt.gcf()
    if len(current_fig.axes) > 0 and len(current_fig.axes[0].collections) > 0:
        print("✓ Scatter plot başarıyla oluşturuldu.")
        if current_fig.axes[0].get_xlabel() and current_fig.axes[0].get_ylabel() and current_fig.axes[0].get_title():
            print("✓ Eksen etiketleri ve başlık eklenmiş.")
        else:
            print("! Eksen etiketleri veya başlık eksik olabilir.")
    else:
        print("✗ Scatter plot oluşturulmamış görünüyor.")
except Exception as e:
    print(f"✗ Hata: {e}")
```

### 10.2. Regresyon Modelleri için Task Formatı

Regresyon modellerinde metrik seçimi ve değerlendirme sürecine odaklanın:

```python
# TODO: Lineer regresyon modeli oluşturun, eğitin ve tahminler yapın
# İpucu 1: sklearn.linear_model modülünden LinearRegression sınıfını import edin
# İpucu 2: Modeli X_train ve y_train ile eğitin, X_test ile tahmin yapın

# Kodunuzu buraya yazın


# TODO: Modelin performansını MSE, MAE ve R² metrikleri ile değerlendirin
# İpucu: sklearn.metrics modülünden mean_squared_error, mean_absolute_error ve r2_score fonksiyonlarını kullanın

# Kodunuzu buraya yazın


# Test - Model performans kontrolü
try:
    metrics_exist = 'mse' in locals() and 'mae' in locals() and 'r2' in locals()
    if metrics_exist:
        print("✓ Model performans metrikleri hesaplanmış:")
        print(f"  MSE: {mse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  R²: {r2:.4f}")
        if r2 < 0:
            print("! R² değeri negatif. Model geliştirilebilir.")
    else:
        print("✗ Bazı metrikler hesaplanmamış görünüyor.")
except Exception as e:
    print(f"✗ Hata: {e}")
```

## 11. Öğrenme Takibi ve Değerlendirme Stratejileri

Task notebookları aracılığıyla öğrenci gelişimini takip etmek için şu stratejileri kullanabilirsiniz:

### 11.1. İlerleme Değerlendirme Metriklerini Notebooka Dahil Etme

Her notebook sonunda öğrencinin kendi performansını değerlendirebileceği bir özdeğerlendirme bölümü ekleyin:

```python
# Özdeğerlendirme - Bu hücreyi çalıştırın
tasks_completed = 0
total_tasks = 10  # Bu değeri toplam görev sayısına göre ayarlayın

# Tamamlanan görevleri kontrol edelim
try:
    # Görev 1: Veri yükleme
    if isinstance(df, pd.DataFrame) and df.shape[0] > 0:
        tasks_completed += 1
    
    # Görev 2: Eksik değer tespiti
    if 'missing_values' in locals() and isinstance(missing_values, pd.Series):
        tasks_completed += 1
    
    # Diğer görevleri burada kontrol edin...
    
    # Sonuçları gösterelim
    completion_rate = (tasks_completed / total_tasks) * 100
    print(f"Tamamlanan görevler: {tasks_completed}/{total_tasks} ({completion_rate:.1f}%)")
    
    if completion_rate == 100:
        print("🏆 Tebrikler! Tüm görevleri başarıyla tamamladınız.")
    elif completion_rate >= 80:
        print("👍 İyi iş çıkardınız! Eksik kalan görevleri gözden geçirin.")
    elif completion_rate >= 50:
        print("👀 Yarısından fazlasını tamamladınız. Kalan görevlere odaklanın.")
    else:
        print("🔄 Henüz yolun başındasınız. Adım adım ilerleyin.")
        
except Exception as e:
    print(f"Değerlendirme sırasında bir hata oluştu: {e}")
    print("Lütfen kodunuzu kontrol edin ve yeniden deneyin.")
```

### 11.2. Zorluk Seviyesine Dayalı Puanlama Sistemi

Görevleri zorluk seviyelerine göre ağırlıklandırarak daha adil bir değerlendirme yapın:

```python
# Zorluk seviyesine göre puanlama
easy_tasks_completed = 0   # Kolay görevler (1 puan)
medium_tasks_completed = 0 # Orta zorlukta görevler (2 puan)
hard_tasks_completed = 0   # Zor görevler (3 puan)

total_points = 0
max_points = 20  # Maksimum puan

# Görevleri zorluk seviyesine göre kontrol edelim
try:
    # Kontrolleri burada yapın...
    
    # Toplam puanı hesaplayalım
    total_points = (easy_tasks_completed * 1) + (medium_tasks_completed * 2) + (hard_tasks_completed * 3)
    
    # Sonucu gösterelim
    print(f"Toplam puan: {total_points}/{max_points}")
    print(f"Başarı oranı: {(total_points/max_points)*100:.1f}%")
    
except Exception as e:
    print(f"Değerlendirme sırasında bir hata oluştu: {e}")
```

Bu teknik kılavuzu izleyerek, mevcut öğretim materyallerinizi pedagojik açıdan etkili task notebooklarına dönüştürebilir, öğrencilerinizin aktif öğrenme deneyimiyle makine öğrenmesi konularını daha derinlemesine anlamalarını sağlayabilirsiniz. 