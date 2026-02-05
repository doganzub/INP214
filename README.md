# INP214 - Uygulamalı Makine Öğrenmesi

Bu depo, **INP214 - Uygulamalı Makine Öğrenmesi** dersi için hazırlanan Jupyter notebooklarını ve veri setlerini içerir. Ders, teorik bilgileri pratik uygulamalarla birleştirerek ML temellerini öğretmeyi amaçlar.

## 📚 Ders İçeriği ve Haftalık Plan

Ders içeriği, haftalık modüller halinde organize edilmiştir:

| Hafta | Konu | Klasör | Notebook |
|-------|------|--------|----------|
| **Hafta 1** | Veri Görselleştirme | `week-01-data-visualization` | [01-data-visualization.ipynb](week-01-data-visualization/01-data-visualization.ipynb) |
| **Hafta 2** | Veri Hazırlama | `week-02-data-preparation` | [02-data-preparation.ipynb](week-02-data-preparation/02-data-preparation.ipynb) |
| **Hafta 3** | K-Means Kümeleme | `week-03-kmeans-clustering` | [03-kmeans.ipynb](week-03-kmeans-clustering/03-kmeans.ipynb) |
| **Hafta 4** | Basit Doğrusal Regresyon | `week-04-simple-linear-regression` | [04-simple-linear-regression.ipynb](week-04-simple-linear-regression/04-simple-linear-regression.ipynb) |
| **Hafta 5** | Çoklu Doğrusal Regresyon | `week-05-multiple-linear-regression` | [05-multiple-linear-regression.ipynb](week-05-multiple-linear-regression/05-multiple-linear-regression.ipynb) |

## 🗂 Veri Setleri

Tüm veri setleri `data/` klasöründe bulunmaktadır:

1.  **Mall Customers** (`data/mall_customers.csv`): Müşteri segmentasyonu için.
2.  **Heart Data** (`data/heart.data.csv`): Kalp hastalığı risk analizi için.
3.  **Income Data** (`data/income.data.csv`): Gelir tahminleme modelleri için.
4.  **Insurance** (`data/insurance.csv`): Sigorta maliyet analizi için.
5.  **Auto MPG** (`data/auto-mpg.data`): Yakıt verimliliği analizi için.

## 🛠 Kurulum ve Kullanım

Bu projeyi kendi bilgisayarınızda çalıştırmak için:

1.  Repoyu klonlayın:
    ```bash
    git clone https://github.com/USER/INP214.git
    cd INP214
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
    ```

3.  Jupyter Notebook'u başlatın:
    ```bash
    jupyter notebook
    ```

## 📝 Notlar

- Her notebook, ilgili konunun teorik anlatımını ve Python ile uygulama örneklerini içerir.
- Notebookları sırasıyla takip etmeniz önerilir.
- `docs/` klasörü ek ders materyallerini içerebilir.