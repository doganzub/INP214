# PYTHON PROGRAMLAMA - eKitap

**Züber Doğan**
Yeditepe Üniversitesi - Meslek Yüksekokulu

---

## İÇİNDEKİLER

1. Python ile Programlamaya Giriş
2. Değişkenler ve Veri Tipleri
3. Veri Yapıları: Liste, Demet, Küme, Sözlük
4. Koşul İfadeleri
5. Döngüler
6. Fonksiyonlar
7. Nesneye Yönelik Programlama
8. NumPy ve Pandas Kütüphaneleri ile Çalışma

---


Yeditepe Üniversitesi
Meslek Yüksekokulu


PYTHON PR OGRAMLAMA
Züber Doğan


# 1. PYTHON İLE PROGRAMLAMAYA GİRİŞ


**Bölümle İlgl Özlü Söz**

Python, en başından ber Google'ın öneml br parçası olmuştur ve sstem büyüyüp gelştkçe de öyle kalacaktır . Bugün
düznelerce Google mühends Python kullanıyor ve bu dlde becer sahb daha fazla kş arıyoruz.
Peter  Norvg , Google, Inc. Arama Kaltes Yönetcs

**Kazanımlar**

1. Python programlama dl genel yapı ve sözdzm hakkındak temel kavramları blr .
2. Python kurulumunu gerçekleştreblr , çalıştırablr , yen br Python betk dosyası oluşturablr ve kaydedeblr .
3. Python dlnn tümleşk gelştrme ortamlarını blr .
4. Spyder IDE kurulumunu ve yapılandırılmasını gerçekleştreblr , Spyder IDE’y çalıştırablr , Spyder IDE’y kullanarak
yen br Python betk dosyası oluşturablr ve kaydedeblr .
5. Spyder IDE’nn arayüzünde bulunan paneller ve bu panellern görevlern blr .
6. Kaynak kod ve çalıştırılablr kod dosyaları arasındak farkı açıklayablr .
7. Derleyc ve yorumlayıcı arasındak farkı fade edeblr .
8. Python dlnn betk dosyasını çalıştırma sürecn anlatablr .
9. Python modül, paket, kütüphane ve çerçeve hakkında blg sahbdr .
10. Python sanal ortamların ne olduğunu, neden ve nasıl kullanıldığını blr .
11. Spyder IDE çnde farklı Python sanal ortamlarını tanımlayıp değştreblr .
12. Python çndek yardım kaynaklarını kullanarak Python le lgl fonksyonlar hakkında daha fazla blg edneblr .

**Brlkte Düşünelm**

1. Python programlama dlnn temel özellkler nedr?
2. Python dlnn farklı sektörlerde nasıl kullanılableceğ hakkında kısaca blg vernz.
3. Python kurulumu nasıl yapılır? Kurulum sırasında dkkat edlmes gereken öneml adımlar nelerdr?
4. Spyder IDE kurulumu nasıl yapılır?
5. Br Python betk dosyası nasıl oluşturulur?
6. Python betk dosyaları nasıl çalıştırılır?
7. Python dağıtımları nelerdr?
8. Python çn gelştrlen “Tümleşk Gelştrme Ortam”ları (IDE’ler) nelerdr?
9. Kaynak kod dosyası le çalıştırılablr dosya arasındak fark nedr?
10. Python betk dosyasını nasıl çalıştırır?
11. Python çalıştırılablr kod dosyası oluşturmak mümkün müdür?
12. Python dlndek modül, paket, kütüphane ve çerçeve kavramlarını kısaca açıklayınız?


13. Python sanal ortam kullanımı ne gb faydalar sağlar?
14. Farklı projeler çn farklı Python sanal ortamları oluşturmak neden önemldr? Br proje çn sanal ortam
oluşturmanın avantajları nelerdr?
15. Python çnde yardım kaynaklarını kullanmanın yolları nelerdr?

**Başlamadan Önce**

Python, sektörde ve akademde araştırmacıların çoğunlukla terch ettğ popüler br programlama dldr . Kolay
kullanımı, ücretsz erşleblmes ve dünya çapındak kullanıcı desteğ Python dlnn popüler hale gelmesndek
etkenlerden bazılarıdır . Son yıllarda özellkle makne öğrenmes, dern öğrenme, yapay zekâ çalışma alanlarında
gerçekleştrlen analzlerdek performansı le ön plana çıkmıştır . Akadem ve sektörde yer alan brçok araştırmacı
tarafından kullanılmaktadır . İşte ktabın bu bölümü, Python programlama dlnn temel özellklern ve pratk kullanımını
ele alan br başlangıç noktası olacaktır .
Bu bölümünde, Python kurulumundan temel sözdzmne, tümleşk gelştrme ortamlarından ( Integrated Development
Envr onment-IDE ) sanal ortam ( vrtual envr onment ) oluşturmaya kadar öneml konular ele alınmıştır . Bu bölüm lk
adımdan tbaren, Python dlnn temel özellklern anlamak ve Python dlnn kullanım alanlarını keşfetmek çn br
rehber ntelğnde olacaktır . Ayrıca, Spyder gb popüler br tümleşk gelştrme ortamının nasıl yükleneceğ, Python
kodlarının nasıl etkl br şeklde düzenleneceğ kavranacaktır . Modül, paket, kütüphane ve çerçeve kavramları le
Python kodlarının nasıl daha verml hale getrlebleceğ açıklanmıştır . Python sanal ortamların önem vur gulanmıştır .
Son olarak, Python dlndek yardım kaynakları kullanımına yönelk açıklamalar verlmştr .
Bu bölümdek konular , sade br dlle anlatılmış, ekran görüntüler ve örneklerle desteklenerek okuyucuya sunulmuştur
Bu sayede, Python dünyasına adım atmak okuyucu açısından keyfl olacaktır . Bu lk bölüm le Python’a lşkn sağlam
br temel oluşturulması hedeflenmştr .

## 1.1. Python Pr ogramlama Dlnn Genel Özellkler

Python programlama dl Gudo Van Rossum tarafından gelştrlmş ve lk sürümü 1990 tarhnde yayınlanmıştır . Python
adını, Gudo’nun hayranı olduğu “ The Monty Python's Flyng Cr cus” adlı ünlü komed dzsnden almıştır (Lutz, 201 1).
Statsta (2022) tarafından 2022 yılında dünya genelnde gelştrcler arasında en çok kullanılan programlama dl
Javascrpt (%65.36), HTML/CSS (%55.08) ve SQL  (49.43)’den sonra Python (%48.07) olmuştur . Dolayısıyla Python çn
en popüler programlama dllernden brdr demek yanlış olmaz.
Python Nesneye Yönelml Programlama (Object Orented Pr ogrammng - OOP ) dldr . Nesneye yönelml
programlama dl olması Python dlnn nesneler e (objects ), sınıflara  (classes ) ve bu nesneler üzernde gerçekleştrlen
şlemlere konsantre olduğunu fade eder . Python dlnde her şey br nesnedr , yan her varlık  (entty ) bazı meta ver lere
(özellklere, ntelklere, attrbutes ) ve lşkl metot lara (fonksyonlara, methods ) sahptr anlamına gelr (V anderPlas,
2016a). Bu özellk ve fonksyonlara nokta (.) sözdzm aracılığıyla erşlr . Mras alma  (kalıtım, nhertance ), çok
bçmllk  (polmorfzm, polymorphsms ), kapsülleme  (encapsulaton ) gb gerçek dünya varlıklarını programlamada
temsl etmey, uygulamayı amaçlar . Nesneye yönelml programlamanın ana fkr, ver ve üzernde çalışan fonksyonları
tek br brm olarak brbrne bağlamaktır . Bu sayede, kodun başka hçbr bölümü bu verye erşemeyecektr . Python
dlnn nesneye yönelml programlamaya yönelk özellklerne Bölüm 7’de yer verlmştr .
Günümüze kadar pek çok programlama dl gelştrlmştr ve halhazırda programcılar htyaçları doğrultusunda farklı
programlama dllern terch edeblmektedr . C, C++, C# gb dller brer derleyc  (compler ) kullanır . Derleyc, günlük
İnglzce konuşma dlne daha yakın olarak blnen yüksek sevyel ( hgh-level ) programlama dllern blgsayarın
anlayableceğ makne dlne çevrr (Detel & Detel, 2010). Bu tür dllerde yazılan programın çalıştırılablmes çn kod
dosyası yukarıdan aşağı derleyc tarafından okunur , eğer program kodunda hata varsa hata mesajı tüm program
tarandıktan sonra döndürülmektedr . Br derleycnn kaynak kodunu analz etmes çok zaman alır; ancak, şlem
yürütmek çn harcanan toplam süre çok daha hızlıdır (Bureau, 2019). Oysa, C, C++ gb dllern aksne Python br
yorumlayıcı  (nterpr eter) kullanır . Yorumlayıcılar , yüksek sevyel dller le yazılan kodların makne dlne çevrlmeden
satır satır çalıştırılmasını sağlar (Detel & Detel, 2010). İlk hata le karşılaşılıncaya kadar program çevrlmeye devam
eder. Herhang br hata tespt edlrse çalışma durdurulur ve dolayısıyla hatanın tespt edlmes ve gderlmes (hata
ayıklama) kolaylaşır (Bureau, 2019).
Python programlama dlnn öne çıkan özellkler şöyle sıralanmıştır (wk.python.or g, 2023a):
• Çeştl temel ver tpler ve yapıları mevcuttur: sayılar (kayan noktalı ( floatng ), karmaşık ve sınırsız uzunluklu uzun
tamsayılar), metnsel fadeler ( strngs ) (hem ASCII hem de Uncode), lsteler ( lsts) ve sözlükler ( dctonares ).


• Python, sınıf ve çoklu kalıtım le nesneye yönelml programlamayı destekler .
• Kod, modüller ( modules ) ve paketler ( packages ) halnde gruplandırılablr .
• Dl, stsna durumların ( exceptons ) oluşturulmasını ve yakalanmasını destekleyerek daha temz hata şleme sağlar .
• Ver tpler güçlü ve dnamk olarak yazılır . Uyumsuz tpler karıştırılması (örneğn metnsel br fadeye br sayı
eklemeye çalışmak gb) br stsna durumun ortaya çıkmasına neden olur , bu nedenle hatalar daha erken yakalanır .
• Python, generators (Python’a özgü fonksyonlar) ve lst comprehensons (lste elemanları le gerçekleştrlen şlemlern
brden fazla satır kullanmak yerne tek satırda daha pratk bçmde gerçekleştrlmes) gb gelşmş programlama
özellkler çerr .
• Python dlnn otomatk bellek yönetm, kodlamada belleğ manuel olarak ayırma ve boşaltma zorunluluğunu ortadan
kaldırmaktadır .
Python özgür  br yazılım  olarak adlandırılmaktadır , çünkü Python'ı ndrmenn, kullanmanın veya br uygulamaya dâhl
etmenn herhang br  malyet yoktur . Python kodları dünyanın dört br yanındak programcılar tarafından farklı
görevler ve amaçlarda kullanılması çn Kaggle, GtHub gb platformlardan paylaşılmaktadır . Ayrıca Python serbestçe
değştrleblr ve yenden dağıtılablr , çünkü Python dl telf hakkıyla korunsa da açık kaynak  (open-sour ce)
lsanslıdır .

## 1.2. Python Dlnn Kullanım Alanları

Python kurulumu sırasında, Python le hem kod yorumlayıcısı hem de şlemlern yürütülmesn sağlayan brtakım yerleşk
standart kütüphaneler/paketler de yüklenmektedr . Ayrıca, Python üçüncü part uygulama kütüphaneler le genşletleblr .
Bu sayede, web stes yapımı, sayısal programlama, ser bağlantı noktası erşm, oyun gelştrme ve daha pek çok amaç
çn kullanılablmektedr (Lutz, 2009).
Python programlama dl makne öğrenmes, dern öğrenme, ver madenclğ ve yapay zekâ gb ver blm temelnde
gerçekleştrlen ver ön-şleme, modelleme, model performans değerlendrme gb analzlerde (k bu alanda R
programlama dl le çokça kıyaslanmaktadır) kullanılmaktadır (bknz. keras, sckt-learn, tensorflow , opencv
kütüphaneler). Bu analzlere temel matematksel ve statstksel hesaplamalar da dâhl edleblr . Ayrıca brbrnden
kullanışlı grafklern hazırlanmasında araştırmacılara mkân tanır (bknz. matplotlb ve seaborn kütüphaneler).
Python, yazılım gelştrme ve web programlama amacıyla kullanılablmektedr . Web gelştrme, komut dosyası ve araç
oluşturma gb pek çok uygulama çn terch edlmektedr (Python.or g, 2023a). Programlanablr br arayüz sağlamak çn
br uygulamaya da gömüleblr . Web sunucularına bağlanma, metn arama, dosya okuma ve değştrme gb brçok yaygın
programlama görevn destekleyen standart kütüphanelerle brlkte gelr . Web stelernden sstematk bçmde ver çekme
çn de kullanılmaktadır ( web scrappng/web crawlng ). Oyun endüstrsnde oyun gelştrme çn de Python terch
edlmektedr (bknz. pygame, panda3D, cocos2D kütüphaneler). Sms 4, World of Tanks, Cvlzaton IV , Eve Onlne,
Prates of the Carbbean, Brdge Commander ve Battlefeld 2 gb popüler oyunlar , çok çeştl fonksyon ve eklentler çn
Python programlamayı kullanmaktadır (Costa, 2020; geeksfor geeks.or g, 2021). Ses ve vdeo uygulamaları da Python
dlnn en şaşırtıcı uygulama alanları arasında görülmektedr (bknz. dejavu, pyo, mngus, scpy , opencv kütüphaneler)
(geeksfor geeks.or g, 2021). Python le kodlanan uygulamalar arasında Netflx, Spotfy ve YouTube gb popüler
uygulamalar yer alır .
Günümüzde Python programlama dlnden faydalanan bazı frmalar ve kullanım alanları şöyle sıralanablr (Lutz, 2009):
Google, web arama sstemlernde, YouTube vdeo paylaşım hzmetnn yazılmasında Python dln kullanmıştır .
BtTorrent dosya paylaşım sstem br Python programıdır . Intel, Csco, Hewlett-Packard, Seagate, Qualcomm ve IBM,
donanım test çn, Industral Lght & Magc, Pxar ve dğerler, anmasyon flmlernn üretmnde Python’ı
kullanmaktadır . JPMor gan Chase, UBS, Getco ve Ctadel, fnansal pyasa tahmnnde, NASA, Los Alamos, Fermlab, JPL
ve dğerler blmsel hesaplamalarda Python dlnden faydalanmaktadır . Robot, tcar robotk chazlar gelştrmek çn
Python dln kullanır . ESRI, popüler coğraf blg sstemler hartalama ürünler çn br son kullanıcı özelleştrme aracı
olarak Python'u kullanmaktadır . NSA, krptograf ve sthbarat analz çn Python’ı kullanmaktadır . IronPort e-posta
sunucusu ürününde Python kodları kullanılmıştır .


## 1.3. Python Kurulumu

Python programlama dl Mac OS X, Wndows, Lnux ve Unx dâhl olmak üzere her ortamda çalışablr , Rasberry P ve
Arduno gb uygulama gelştrme platformlarında da kullanılablmektedr (Uğuz, 2021). Bu ktapta Wndows üzerndek
kurulum ve kullanımı dkkate alınmıştır . Python le çalışmak çn Python.or g (2023b) adresnden şletm sstemne uygun
Python sürümü blgsayara ndrleblr , yükleneblr ve Python le çalışmaya başlanablr (bu ktap hazırlanırken Python
dlnn en güncel versyonu 3.1 1.4 d).
Kurulumun lk adımında “ Add Python.exe to P ATH” seçeneğnn seçl olmasına dkkat edlmeldr . Bu sayede, kurulum
tamamlandıktan sonra Python dlnn br komut penceresnden çalıştırılması ve kullanılması mümkün olacaktır . Bunun
çn Wndows’ ta Başlat menüsüne “cmd” yazarak br komut dosyası açılması, ardından gelen syah ekrana “python”
yazılması yeterl olacaktır .
Python kurulum aşamalarına at ekran görüntüler aşağıda sıralanmaktadır .


Kurulum tamamlandıktan sonra hem Python hem de IDLE (Wndows’ ta) Başlat Menüsü’nde lstelenen programlar
arasında görülecektr . IDLE, Python kurulumu le gelen bast ve temel br gelştrme ortamıdır .
CPython , Python dlnn resmî web stesnde yer alan dağıtımıdır ( dstrbuton ). CPython, C programlama dlnde
yazılmış Python dlnn yorumlayıcısıdır . En sık kullanılan programlama dl uygulamasıdır ve fl referans uygulaması
olarak kabul edlr . Bunun dışında CPython’a dayalı dağıtımlar da vardır (Python Software Foundaton, 2023b): Jython ,
Python kodunun Java platformlarında yürütülmesn sağlayan Python programlama dlnn br Java uygulamasıdır . Ayrıca,
tüm Java kütüphaneler çe aktarılablr ve dnamk olarak kullanılablr . IronPython , dlden bağımsız ve platformdan
bağımsız uygulama gelştrme ve yürütme çn br standart olan ( Ortak Dl Altyapısı  (Common Language Infrastructur e-
CLI) le uyumlu br Python uygulamasıdır . IronPython, C# le yazılmıştır ve Python kodunun .NET  ve Mono gb CLI
uyumlu çalışma zamanı ortamlarında yürütülmesne zn verr . PyPy , çevrcler tarafından lgl hedef dle (C, Java, C#)
taşınan Python dlnn br alt kümes olan RPython'dak br Python uygulamasıdır . Sık kullanılan kodu çevrmek çn
çalışma zamanında br JIT  derleycs ekleneblr .
Farklı amaçlar çn özelleştrlmş, daha fazla Python kütüphanes çeren ActveState ActvePython, Anaconda, Portable
Python, Tny Python, WnPython gb dağıtımlar da mevcuttur . Ayrıca Python, Phone, Androd, Wndows Moble, Noka
S60 ve dğerler gb br dz cep telefonu platformuna taşınmıştır .

## 1.4. Python le “Merhaba Dünya!”

Temel Python yüklemes çalışma ortamı olarak kodun yazılması ve çalıştırılmasını çeren blgsayarın DOS ekranına
benzeyen syah arka planlı temel br konsol  (console ) arayüzü sunmaktadır .
Bu ekran karşınıza geldkten sonra, br programlama dl yen öğrenlmeye başlarken br klask halne gelen “Merhaba
Dünya!” yazısını yazdırablrsnz. Bunun çn bastçe aşağıdak prnt() fonksyonunun yer aldığı kod satırı kullanılablr .
Kod satırını yazdıktan sonra ardından klavyedek “ Enter ” tuşuna basmak yeterl olacaktır .


Temel sevyede farklı örnekler çn temel matematksel şlemler de Python konsolda gerçekleştrleblr .
Temel Python yorumlayıcısını açmak çn Wndows’ ta CMD ekranına python yazılablr . Arkadak Python tarafından
sağlanan kod penceres ken, ön tarafta yer alan Wndows CMD ekranıdır . Bu ekranda da br öncekne benzer şeklde
“Enter ” tuşuna basılarak kod satırları çalıştırılablr .

## 1.5. Python çn Tümleşk Gelştrme Ortamları

Tümleşk Gelştrme Ortamı  (Integrated Development Envr onment- IDE ), program kodu yazarken brtakım avantajlar
sunan, grafk arayüzlü metn edtörlerdr . IDE kullanımı le programcıların program kodlarını verml bçmde
yazablmeler sağlanır . Farklı programlama dller çn farklı IDE’ler bulunur . Python çn 2023’ün en popüler IDE’ler
arasında IDLE, PyCharm, Vsual Studo Code, Sublme Text 3, Atom, Jupyter , Spyder , PyDev , Thonny ve Wng yer
almaktadır (Gupta, 2023). Bunlar çnde bast ve temel gelştrme ortamı olan IDLE ( Integrated Development and
Learnng Envr onment ) Python kurulumu le halhazırda blgsayara yüklenmektedr (Python Software Foundaton,
2023a). Blg düzey, kullanım amacı, eldek donanım gb faktörler seçenekler arasından en y IDE terchnde
bulunulmasına yardımcı olacaktır . Bu ktapta Python çn Spyder  IDE  kullanımı terch edlmştr .

## 1.6. Spyder ’ın Yüklenmes

Spyder ( Scentfc PYthon Development EnvRonment ), Python çn Python le yazılmış ücretsz ve açık kaynak br
tümleşk gelştrme ortamıdır . Spyder ’ı bağımsız yükleyc yardımı le blgsayara ndreblmek çn https://www .spyder -
de.or g/ adresne gdlerek “Download” menü başlığına tıklanır ve şletm sstemne uygun Spyder blgsayara ndrlr . Bu
noktada, en son sürüm otomatk olarak blgsayara ndrlecektr . Spyder IDE ndrlrken kend Python kurulumunu da
yapmaktadır . Bu nedenle Bölüm 1.3’de verlen Python kurulumunun gerçekleştrlmes br zorunluluk değldr . Bu ders
ktabının yazıldığı süreçte Spyder ’ın en güncel versyon 5.4.2, Spyder le ndrlen Python dlnn en güncel versyonu se
3.8.10’dur .


Kurulum aşamalarına at ekran görüntüler şöyle sıralanmaktadır .
Spyder yüklendkten sonra çalıştırdığınızda karşınıza gelecek ekran aşağıdak gbdr .


Spyder Edtör ü yen br kaynak dosyasının oluşturulması, açılması ya da düzenlenmesn ve kodun çalıştırılmasını sağlar .
Kod yazarken, kodların renklendrlmes, otomatk tamamlama gb çeştl faydalı özellklern desteklendğ görülecektr .
IPython , Fernando Perez tarafından 2001’de gelştrlen, standart Python yorumlayıcısına göre zengnleştrlmş br
Python yorumlayıcısıdır (Pérez & Granger , 2007). IPython ( Interactve Python ) Console  Python komutlarını
çalıştırabldğnz ve IPython yorumlayıcıları çndek verlerle etkleşme geçebldğnz br alandır . İster harc
yüklenmş sterse de Spyder tarafından başlatılmış br IPython  konsolu; otomatk kod tamamlama, fonksyonlar çn
gerçek zamanlı pucu sağlama, gelşmş Spyder hata ayıklayıcı le tam görsel kullanıcı arayüzü  (Graphcal User
Interface – GUI ) entegrasyonu, brçok yerleşk ve üçüncü taraf Python nesnes çn GUI tabanlı düzenleyclere sahp
değşken gezgn  (varable explor er), Matplotlb grafklernn seçme bağlı olarak Spyder ’ın Grafkler bölmesnde ya da
konsolda görüntülenmes gb özellkler destekler . Ayrıca IPython, Python kodu çn br çekrdek  (kernel ) çerr . Kernel,
kullanıcının kodunu çalıştırmaya ve ncelemeye yarar (python.or g, 2023). IPython , Wndows’ ta CMD ekranı
kullanılarak da çalıştırılablr . Bunun çn CMD’ye python yazılması yeterldr .
Değşken Gezgn (varable explor er) çalışırken oluşturduğunuz değşken, dz, lste, fonksyon gb Python nesnelern
görüp yönetmenze zn verr .
Grafkler  (plots) alanı özellkle ver blm çalışmalarında sıklıkla kullanılan br bölümdür . Oluşturulan grafklern
gösterldğ bölmedr .
Hata ayıklama mekanzması  (debuggng ) bulunmaktadır . Böylelkle yazdığınız koda kesme noktaları (breakpont’ler)
ekleyerek kodun yürütme akışının ncelenmes mümkün kılınır , olası hatalar okunablr .
Ayrıca herhang br modül, sınıf, fonksyon ya da metoda lşkn merak edlenler yardım  (help) bölümü kullanılarak
öğrenleblr . Örneğn; br fonksyonun ne şe yaradığı, hang ver tpnde parametreler aldığı ve nasıl br çıktı ürettğ
gb.
Spyder IDE hakkında daha detaylı blg çn bknz. (spyder -de.or g, 2022).
Bölüm 1.4’ te verlen, ekrana “Merhaba Dünya!” yazdırma alıştırması, Spyder ’dak Console kullanılarak da yapılablr .
Bu sırada yazının renklendrlmes, otomatk tamamlama, fonksyonun kullanımı hakkında pucu verme gb avantajlar da
deneymlenmş olacaktır .


Spyder edtöründek Python Console’da da “Enter” tuşu le kod satırları çalıştırılablr .

## 1.7. Kaynak Kod ve Çalıştırılablr  Dosya

Herhang br programlama dl le yazılan, program kodlarının yer aldığı derlenmemş programa kaynak kod  (source
code ) denmektedr (Çobanoğlu, 2021). Bölüm 1.4 ve Bölüm 1.6’ te verlen örnekler yalnızca Python konsolu kullanılarak
gerçekleştrlmştr . Oysa Python çn de kaynak kod dosyası oluşturulablr . Bunun çn Spyder ’ın sol bölmes
kullanılacaktır . Spyder açıldıktan sonra, varsayılan olarak blgsayarda henüz herhang br dosya yoluna kaydedlmemş
.py uzantılı br dosyanın görüntülenmesn sağlar . Tahmn edleceğ gb Python betk  (scrpt ) dosyaları .py uzantılıdır .
Şmdye kadar Python ya da IPython yorumlayıcısı kullanılarak kodların nasıl çalıştırılableceğ gösterlmşt; ancak daha
karmaşık programlarda bu tür br ortam yeterl gelmeyeblr . Program kodlarının br Python betk dosyasına yazarak daha
sonra yenden çalıştırılması ve kullanılması çn blgsayarda stenlen br konumda saklanablr . Normalde br metn
dosyasına Python kodlarının yazmak ve ardından .py uzantısı le saklamak da benzer ş görecektr . Farklı br Python
dosyası oluşturmak çn üst menüde Fle ->  New Fle  seçenekler ya da yne üst menüde dosya smges ( New Fle :
Ctrl+N ) tıklanablr .
Açılan .py uzantılı dosyaya bastçe aşağıdak Python kodu yazılsın ve dosya masaüstüne kaydedlsn. Kaydetmek çn
yne üst menüde yer alan Fle -> Save (Ctrl+S)  ya da Save as  başlıkları kullanılablr . Save  (kaydet ), o ank çalışma
klasörüne, Save as  (farklı kaydet ) se br kayıt penceres açarak blgsayarda stenlen dosya konumuna dosyanın
kaydedlmesn sağlayacaktır . Daha sonra kaydedlen bu dosyayı açmak çn üst menüden Fle ->  Open  seçeneğ ya da
yne üst menüdek klasör smges seçlerek stenen .py uzantılı dosya açılablecektr .
Python Console’dan farklı olarak .py uzantılı betk dosyasına yazılan kodlar klavyedek “ F9 tuşu ” le çalıştırılır . İlgl
kod satırına mlecn getrlmes ya da lgl kod satırı veya kod bloğunun seçlmesyle F9 tuşlanır ve çalıştırılır . Tools ->
Preferences ->  Keyboard shortcuts kullanılarak açılan ekranda “ run selecton ” çn belrlenmş olan klavye kısayolu
değştrleblr . Örneğn aşağıdak ekran görüntüsünde “ run selecton ” çn F9 yerne “ Ctrl+Enter ” tuşları kullanılmıştır .
Benzer şlem çn üst menüde bulunan “seçm ya da mevcut satırı çalıştır” ( run selecton or curr ent lne ) düğmes de
kullanılablr 
 .
Özellkle brden fazla kod satırının seçlmes söz konusu olduğunda, k ya da daha fazla satıra taşan kod satırı olduğu
zaman tüm kod bloğunun seçldkten sonra çalıştırıldığına emn olunması gerekldr , aks halde uyarı mesajı le
karşılaşılacaktır .


Yalnızca Python le değl, tüm programlama dller le çalışılırken gelştrlen program kodları ve bu kodlarla bağlantılı
tüm dğer dosyaların (örneğn; görseller , ver setler vb.) tek br klasörde olması terch edlmeldr . Bunun çn br çalışma
klasörü nün ( workng dr ectory ) belrlenmes önerlr . Spyder ’da varsayılan çalışma klasörü üst menüde sağ tarafta
“C:\Users\elf ” olarak verlmştr . Bu çalışma klasörü yolu stenldğ gb ayarlanablr .
Örneğn; Bölüm 1.6’dak alıştırma ornek.py  olarak Masaüstüne ( Desktop ) kaydedlsn. Daha sonra kaydedlen bu Python
dosyası üst menüde yer alan Oynat ( Play) düğmes 
  le baştan sona kadar çalıştırılablr . Tüm dosyada çalıştırılablr
yalnızca tek satır yazdırma komutu olduğundan, konsolda, dosyadak kodların çalıştırılmasını sağlayan Python kodu ve
program çıktısı belrecektr .
Benzer şlemler CMD ekranından se aşağıdak gb yapılablr:
Python, betk dosyasını çalıştırırken öncelkle kaynak kod “byte code” olarak derlenr , ardından da Python Sanal
Maknes ne (Python V rtual Machne - PVM ) yönlendrlr (Lutz, 2009). Derleme yalnızca br çevr adımıdır ve byte
kodu, kaynak kodun daha düşük düzeyde, platformdan bağımsız br temsldr . Python Sanal Maknes, Python dlnn
çalışma zamanı  (runtme ) motorudur , her zaman Python sstemnn br parçası olarak bulunur (ayrıca yüklenmes
gerekmez) ve betkler gerçekten çalıştıran bleşendr . Teknk olarak, "Python yorumlayıcısı" denen şeyn son adımıdır .


Br programlama dl le yazılmış olan kaynak kodun derlenmes sonucu, makne dlne çevrlmş, çalışmaya hazır
programa çalıştırılablr  dosya  (executable fle ) denr (Çobanoğlu, 2021). Bu tür dosyaların uzantısı . exe’dr. Python le
yazılmış programların herhang br Python yorumlayıcısı veya herhang br modül yüklemeden çalıştırılması PyInstaller
gb programlar le sağlanablr (pynstaller .org, 2023).

## 1.8. Modül, Paket, Kütüphane ve Çerçeve

Python betk dosyaları dışında, Python kodlarının ve bu kodların yazıldığı betk dosyalarının br araya gelme bçmlerne
göre brbrnden farklı adlandırılan yen yapılar meydana gelmştr . Python programlamada lteratürde sıklıkla
karşılaşılablecek bu yapılar şu şeklde açıklanablr (Kodan, 2021):
.py uzantılı dosyalara kaydedlen brbryle lşkl br grup Python kodu modül  (module ) dye adlandırılmaktadır
(örneğn; random, math, html, datetme, re modüller). Br modülün çne, fonksyonlar , sınıflar ya da değşkenler
yerleştrleblmektedr . Örneğn; Python le math modülünü çağırmak çn aşağıdak kod satırını kullanmak yeterldr
(Hjelle, 2020).
Modül çağrıldıktan sonra artık çnde yer alan tüm fonksyon, değşken vb. unsurlar kullanılablr hale gelmştr demektr .
Genellkle br betk dosyasının en başında gerekl modül çağırma şlemler yapılır . Örneğn; math  modülünde tanımlı p
sayısını kullanablmek çn modül çağırıldıktan sonra aşağıdak kod satırı yazılablr .
Eğer yalnızca math modülünün çnden p sayısını tutan değşkenn getrlmes stenyorsa, aşağıdak gb o değşkene
özel br çağırma şlem yapılır .
Br modül çağırılırken yenden adlandırılablmektedr . math modülü aşağıda m olarak yenden adlandırılmıştır .
Dolayısıyla çnden br unsura erşlmek stendğnde artık math. değl m. fades kullanılacaktır .
Çalışma klasörü le lgl şlemlernn aşağıdak kod satırları yardımı le yönetlmes mümkündür . mport le os modülü
çağrılır . Ardından os modülündek getcwd() fonksyonu yardımı le mevcut çalışma klasörü yolu (“ C:\Users\elf ”) alınır
ve bu blg calsmaKlasoru değşkennde tutulur . Çalışma klasörünün dosya yolu prnt() fonksyonu le ekrana yazdırılır .
Eğer, çalışma klasörünün “ G:\My Drve\MYYBS\2023\auzefKtaplar\python\kodlar ” olarak belrlenmes stenyorsa,
aşağıdak gb yen çalışma klasörü yolu os modülünün chdr() fonksyonuna verlr . Bu noktada, edtörün sağ üst
köşesne bakılacak olursa, çalışma klasörünün değştğ görüleblr . Aşağıdak kod bloğunda değşklkler sonrası çalışma
klasörünün yolu tekrar ekrana yazdırılmıştır . İlgl değşklk buradan da bell olacaktır .


Python paketler  (packages ), temel olarak br modül koleksyonunun br dzndr (örneğn; NumPy , pandas, pytest
paketler). Paketler , modül ad alanının ( namespace ) hyerarşk yapısına olanak sağlar . Br sabt sürücüdek dosyalar nasıl
klasörler ve alt klasörler halnde or ganze edlyorsa, modüller de paketler ve alt paketler halnde or ganze edleblr .
Kütüpane  (lbrary ), yenden kullanılablr br kod parçasına atıfta bulunan genş anlamlı br termdr (örneğn;
matplotlb, pytorch, pygame kütüphaneler). Genellkle br Python kütüphanes, lgl modüller ve paketlerden oluşan br
koleksyon çerr . Python dlnde “paket” ve "kütüphane" termler brbrnn yerne kullanılablmektedr , çünkü paketler
ayrıca modüller ve dğer paketler (alt paketler) çereblr . Bununla brlkte, genellkle br paket br modüller koleksyonu,
br kütüphane de br paketler koleksyonu olarak görülmektedr .
Python çerçeveler  (frameworks ), kütüphanelere benzer şeklde programcıların gelştrme sürecn hızlı br şeklde
zlemesne yardımcı olan br modüller ve paketler koleksyonudur . Ayrıca kütüphaneler belrl şlemler gerçekleştren
paketler çerrken, çerçeveler uygulamanın temel akışını ve mmarsn çerr (örneğn; django, flask ve bottle çatıları).
Python programlama dlnde özellkle standart kütüphane dışında farklı br kütüphane kurulmak stenrse bunu
gerçekleştrmenn en kolay yollarından br pp kullanımıdır . Elbette öncelkle pp’n Wndows’a yüklenmes
gerekmektedr . Bunun çn (GeeksforGeeks, 2020):
(1) get-pp.py ( https://bootstrap.pypa.o/get-pp.py ) dosyası ndrlr ve Python dlnn kurulu olduğu dzne kopyalanır .
(2) Komut satırındak dznn geçerl yolu, lk adımda kaydedlen dosyanın bulunduğu dznn yoluyla değştrlr .
(3) get-pp.py , kullanıcıların Python ortamlarına pp yüklemesne olanak tanıyan br önyükleme betğdr ve aşağıda
verlen komut satırı çalıştırılır:
(4) Br öncek adımdak komut satırı çalıştırıldığında blgsayara pp yüklenene kadar beklenr .

## 1.9. Python Sanal Ortamı

Python sanal ortamı  (vrtual envr onment ), br Python kodunu çalıştırmak çn yalıtılmış br ortamda htyaç duyulan her
şey sunan br klasör yapısıdır (Breuss, 2017). Br Python sanal ortamı; br yorumlayıcı, br kütüphane (tpk olarak
Python Standart Kütüphanes) ve br dz kurulu paketten oluşur (Mcrosoft, 2022). Python sanal ortamı kullanma
nedenler şu şeklde sıralanablr (Breuss, 2017):
1) Python kullanılarak öncek bölümlerde bahsedldğ üzere çok farklı amaçlar çn programlar yazablr ve projeler
oluşturulablr . Bu süreçte programlama amacına yönelk farklı kütüphane ve paketlere htyaç duyulablr . Hatta aynı
paketn farklı versyonları ble üzernde çalışılan projeler çn değşklk göstereblr . Örneğn; Python dlnde özel olarak
belrtlmedğ sürece paket yüklemek çn gereken pp kurulan tüm harc paketler temel Python kurulumundak ste-
packages/ adlı br klasöre yerleştrecektr . Python sanal ortamı, projeye göre farklı paketlerle, aynı kütüphanenn k farklı
sürümü le çalışılmasına mkân tanır .
2) Proje paket bağımlılıklarının kolaylıkla keşfedleblmesn sağlar ve olası br paylaşım durumunu kolay hale getrr .
3) Çoklu çalışma ortamlarında klasör bazında kullanıcı yetklendrmeler le karşılaşılablr . Bu tür durumlarda yen br
paket yüklerken Python sanal ortamı yetk problemnn ortadan kalkmasını sağlar .


4) Lnux ve macOS şletm sstemnn kend ç şlemlernde kullandığı br Python versyonu le gelmektedr . Eğer yen
yüklenecek paketler bu Python global ortamına yüklenrse, şletm sstem tarafından kullanılan dğer paketler le karışır .
Bu karışıklık, şletm sstem çn önem arz eden şlemler çn beklenmedk yan etklere yol açablr . Ayrıca, şletm
sstemndek br güncelleme Python çalışmalarında kullanılan paketlere etk edeblecektr .
Spyder ’da br Python sanal ortamı oluşturmak çn Termnal ekranı kullanılablr . Ekran görüntüsünde çalışma klasörü
C:\Users\elf\Desktop\projem olarak belrlenmştr . Termnal penceresnn sağ üst köşesnde yer alan + sembolüne
tıklanırsa, Termnal dzn lgl çalışma klasöründe açılacaktır .
Python sanal ortamı oluşturmak çn aşağıdak kod bloğunda yer alan lk satır kullanılır . Böylelkle my_vrt_env adlı
Python sanal ortamı projem adlı bu klasörün çnde oluşturulacaktır . İlgl sanal ortam çnde çalışmak çn sanal ortam
knc satırdak kod le aktve edlr . Sanal ortam aktve edldğnde Termnalde yen satır başında parantez çnde sanal
ortamın adı (my_vrt_env) yazacaktır . Örneğn; Matplotlb  gb ek br paket yüklenmek stenrse üçüncü satırdak kod
satırı çalıştırılır . İlgl sanal ortamda çalışma btrldğnde dördüncü satırda yer alan deactvate komutunun çalıştırılması
yeterldr . Sanal ortamın slnmes çn lgl dzne gdlerek sanal ortam çn oluşturulan klasör slneblr .

## 1.10. Spyder ’da Python Ortamını Değştrme

Öncek bölümlerde bahsedldğ üzere, Spyder ’ın varsayılan yüklemes le berabernde Python 3.8.10 yüklenmektedr .
Dolayısıyla Spyder açıldığında Console’da varsayılan olarak Spyder le gelen Python yorumlayıcısı (Default seçeneğ)
kullanılmaktadır; ancak farklı Python kurulumları ya da farklı Python sanal ortamlarına htyaç duyulablr . Dolayısıyla da
farklı Python yorumlayıcıları le çalışılmak steneblr .


Örneğn; Bölüm 1.3’ te yüklenen Python 3.1 1.4 le gelen farklı br Python yorumlayıcısı le çalışmak çn sırasıyla şu
adımlar zlenr (Panwar , 2022):
1) Spyder'ın PYTHONP ATH yönetcsne Spyder ’da kullanılmak stenen Python kurulumunun (3.1 1.4) dosya yolu
eklenmeldr . Bunun çn Başlat’ ta Python dlnn dosya konumu açılarak Python 3.1 1 (64-bt)  dosyasına sağ tıklanır ve
özellkler açılır . Açılan ekranda Shortcut  sekmesnde dosya yolu
(C:\Users\elf\AppData\Local\Pr ograms\Python\Python31 1) kopyalanır (Bu dosya yolu szde kurulan klasöre göre
farklılık göstereblr). Sonrasında Spyder ’dak üst menüde Tools ->  PYTHONP ATH MANAGER  açılarak dosya yolu
eklenr .
2) Spyder ’dak varsayılan Python yorumlayıcısı değştrlr . Bunun çn Spyder üst menüdek Tools ->  Preferences -
> Python Interpr eter -> Use the followng Python nterpr eter alanında lk adımda bulunan Python dosya yolu
(C:\Users\elf\AppData\Local\Pr ograms\Python\Python31 1) seçlr .


3) Bu şlem gerçekleştrldkten sonra Python kernelnn (çekrdeğ) yenden başlatılması gerekmektedr . Bunun çn
Spyder üst menüsündek Consoles - > Restart kernel  seçeneğ kullanılablr . Spyder konsolunuzu çalıştırmak stedğnz
çalışma ortamında spyder -kernels paketnn desteklenen br sürümünün bulunmasını gerektrr . Bu paket kurulu değlse,
aşağıdak hata mesajı görüntülenecektr .
Hata mesajına stnaden Spyder kernellernn yükleneblmes çn blgsayardan komut stem penceres ( CMD ) açılır ve
aşağıdak kod satırı çalıştırılır .


Bu örnekte, kullanmak stenlen Python sürümü C:\Users\elf dosya yolunda olduğundan, CMD’de doğrudan spyder -
kernel yükleme şlem gerçekleştrlmştr; ancak Python yorumlayıcısı, blgsayarda masaüstünde çalışılan proje çn
oluşturulan br sanal ortam çnde de bulunablrd ( C:\Users\elf\Desktop\pr ojem\my_vrt_env\Scrpts ). Böyle br
durumda, CMD penceresnde lgl dzne ( C:\Users\elf\Desktop\pr ojem ) nlerek (cd …) sanal ortam aktf hale
getrlmel (my_vrt_env\Scrpts\actvate), ardından spyder -kernel yükleme adımı gerçekleştrlmeldr .
Yükleme tamamlandıktan sonra değşklklern yansıtılablmes çn Spyder yenden başlatılır . Spyder açıldığında
Console-un Python dlnn  3.8.10  sürümü yerne 3.11.4 sürümünü kullanıldığı görülecektr .

## 1.11. Python Dlnde Yardım

Python dlnde kullanılan nesneler , fonksyonlar vb. hakkında yardım almak çn help() fonksyonu kullanılablmektedr .
Örneğn; toplama çn kullanılan sum() fonksyonu hakkında yardım alınması stenrse help(sum) yazılablr . Sum??
fades de aynı sonucu verecektr . Yardım alınması stenlen komut seçlp Ctrl+I  tıklanırsa edtörün sağ üst tarafında yer
alan Yardım penceres açılacaktır .


Ayrıca, daha önce de belrtldğ gb Python dlnn genş br kullanıcı/gelştrc topluluğu bulunmaktadır . Dolayısıyla,
nternette brçok web stes ve forumda Python’a lşkn kod örnekler, kod dosyaları paylaşılmakta, araştırmacıların
sorduğu sorulara lşkn dünyanın brçok yernden araştırmacıların verdğ cevaplar yer almaktadır .

**Bölüm Özet**

Bu bölümde Python programlama dlnn temeller okuyucuya sunulmuştur . Python dlnn hang şletm sstemler ve
platformlarda çalıştığı, Python dağıtımları ve tümleşk gelştrme ortamları konusunda blgler verlmştr . Python dlnn
ve Spyder IDE’nn kurulumu adım adım açıklanmıştır . Spyder IDE’nn arayüzünde yer alan paneller ve bu panellern
görevler tanıtılmıştır . Okuyucular , bölümdek talmatları zleyerek lk Python kodlarını yazmış, br Python betk dosyası
oluşturmuş, kaydetmş ve çalıştırmıştır . Derleyc ve yorumlayıcı arasındak farklara değnlmş ve son olarak Python
dlnn br betk dosyasını çalıştırma sürec anlatılmıştır . Ayrıca, modül, paket, kütüphane ve çerçeve kavramları ve
Python sanal ortamı bölümde ele alınan öneml konulardan bazılarıdır . Bölüm, Python dlnde yardım kaynaklarının nasıl
kullanılacağının anlatımıyla sonlandırılmıştır .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de


Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1


sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Python programlama dlnn genel özellkler le lgl aşağıda verlenlerden hangs doğrudur?
(Çoktan Seçmel)
(A) Python nesne yönelml br programlama dldr .
(B) Python yalnızca web gelştrme alanında kullanılır .
(C) Python, düşük sevyel br dldr .
(D) Python, sadece Lnux ve Ubuntu şletm sstemlernde çalışablr .
(E) Python dlnn temel sözdzm, dğer programlama dllerne benzemez.


Cevap-1 :
Python nesne yönelml br programlama dldr .
Soru-2 :
Python kurulumu le lgl hangs doğrudur?
(Çoktan Seçmel)
(A) Python yalnızca macOS üzernde kurulablr .
(B) Python dlnn farklı versyonlarından brn seçerken, projenn gereksnmlern dkkate almak önemldr .
(C) Python dlnn yalnızca onlne olarak çalışan versyonları vardır , ndrmeye gerek yoktur .
(D) Wndows’ ta Python kurulumu şletm sstemyle brlkte hazır gelr .
(E) Python tamamen tcar br yazılımdır .
Cevap-2 :
Python dlnn farklı versyonlarından brn seçerken, projenn gereksnmlern dkkate almak önemldr .
Soru-3 :
Kaynak kod ve çalıştırılablr dosya le lgl hangs doğrudur?
(Çoktan Seçmel)
(A) Python kaynak kod dosyalarının uzantısı genellkle " .pyc" şeklndedr .
(B) Python kaynak kodlarını çalıştırmak çn python dosya_ad.py komutu kullanılır .
(C) Çalıştırılablr dosyalar , Python yorumlayıcısı le kaynak kod dosyasına dönüştürülür .
(D) Python kaynak kodu, çalıştırılablr dosyaya dönüştürüldüğünde her zaman daha hızlı çalışır .
(E) Python kaynak kodunu çalıştırmak çn her zaman br tümleşk gelştrme ortamı (IDE) kullanmak gerekldr .
Cevap-3 :
Python kaynak kodlarını çalıştırmak çn python dosya_ad.py komutu kullanılır .
Soru-4 :
Spyder ’da Python ortamını değştrme konusunda aşağıdaklerden hangs doğrudur?
(Çoktan Seçmel)
(A) Spyder IDE çnde Python sanal ortamını değştrmenn avantajı, farklı projelerde farklı paket ve kütüphaneler
kullanablme esneklğdr .
(B) Spyder , Python sanal ortamlarını yönetme özellğne sahp değldr .
(C) Python sanal ortamını değştrmek, blgsayarınıza başka br Python sürümü yüklemek le eşdeğerdr .
(D) Spyder ’da Python sanal ortamını değştrmek çn ekstra eklentler yüklenmeldr .
(E) Python sanal ortamını değştrmek, Spyder ’ın performansını olumsuz etkler .
Cevap-4 :


Spyder IDE çnde Python sanal ortamını değştrmenn avantajı, farklı projelerde farklı paket ve kütüphaneler
kullanablme esneklğdr .
Soru-5 :
Python yardım kaynakları konusunda aşağıdaklerden hangs doğrudur?
(Çoktan Seçmel)
(A) Python yardım desteğ çermez.
(B) Python dlnn yardım taleplerne cevap veren aktf br topluluğu mevcut değldr .
(C) Python le lgl nternettek kaynaklar oldukça kısıtlıdır .
(D) Python dlnde yardım alınmak stenen fonksyonun yanına ??? eklenerek fonksyonla lgl yardımcı blglere
ulaşılablr .
(E) Python belgelernn yanı sıra, help() fonksyonu kullanılarak yardım alınablr .
Cevap-5 :
Python belgelernn yanı sıra, help() fonksyonu kullanılarak yardım alınablr .
Soru-6 :
Aşağıdaklerden hangs Python IDE’lernden br değldr?
(Çoktan Seçmel)
(A) Spyder
(B) Jupyter
(C) CPython
(D) Thonny
(E) Wng
Cevap-6 :
CPython
Soru-7 :
Aşağıdaklerden hangs Python dlnn gelştrcsdr?
(Çoktan Seçmel)
(A) Mark Zuckerber g
(B) Yann LeCun
(C) Geof frey Hnton
(D) Gudo Van Rossum
(E) Elon Musk
Cevap-7 :
Gudo Van Rossum


Soru-8 :
Spyder edtöründe aşağıdaklerden hangs bulunur?
(Çoktan Seçmel)
(A) Tanımlanan nesnelern görülebleceğ pencere.
(B) Yardım dokümanlarını gösteren pencere.
(C) Dosyaların görülebleceğ pencere.
(D) Python Console
(E) Heps
Cevap-8 :
Heps
Soru-9 :
Spyder ’da Python yorumlayıcısını değştrmek çn aşağıdak seçeneklern hangs kullanılablr?
(Çoktan Seçmel)
(A) Tools -> Preferences -> Python Interpreter .
(B) Fle -> Open
(C) Vew -> Panes -> Help
(D) Consoles -> Connect to exstng kernel
(E) Help -> Troubleshootng
Cevap-9 :
Tools -> Preferences -> Python Interpreter .
Soru-10 :
Aşağıdak seçeneklerden hangsnde br kod satırının Spyder IDE le çalıştırılablmes çn varsayılan  klavye tuşu
verlmştr?
(Çoktan Seçmel)
(A) Enter
(B) Alt-Enter
(C) F2
(D) F9
(E) F1 1
Cevap-10 :
F9


# 2. DEĞİŞKENLER VE VERİ TİPLERİ


**Bölümle İlgl Özlü Söz**

Programlamada zor olan problem çözmek değl hang problemn çözüleceğne karar vermektr .
Paul Graham , Blgsayar Blmc

**Kazanımlar**

1. Değşken kavramını anlar , şaretç ve lteral kavramlarını blr ve nasıl kullanıldığını kavrar .
2. Blgsayar belleğnn temel çalışma prensplern anlar ve Python bellek yönetm sürecn blr .
3. Python programlama dlndek temel ver tplernn (örneğn, nt, float, strng, bool, NoneT ype) neler olduğunu blr , bu
ver tplernn nasıl tanımlandığını ve kullanıldığını kavrar .
4. Python matematksel, atama, btsel şlem, karşılaştırma, mantıksal, üyelk ve kmlk operatörlernn nasıl kullanıldığını
blr, bu operatörlern farklı ver tpler üzernde nasıl şlem yaptığını anlar .
5. Açık ( explct ) ve örtülü ( mplct ) ver tp dönüşümünün ne olduğunu anlar , ver tpler arasında dönüşüm yapmanın
nasıl gerçekleştğn öğrenr , uygun ver tp dönüşümünü avantaj ve dezavantajları le değerlendrerek kullanablr .
6. Değşr ( mutable ) ve değşmez ( mmutable ) nesnelern ne olduğunu kavrar , hang ver tpler ve ver yapılarının değşr
veya değşmez olduğunu blr , değşr ve değşmez nesneler uygun bçmde kullanablr .

**Brlkte Düşünelm**

1. Değşken nedr? Pyhton’da br değşken nasıl tanımlanır?
2. İşaretçler (ponters) nedr ve hang durumlarda kullanılırlar?
3. Lteral fadeler nedr? Örnek vernz.
4. Blgsayarda bellek yönetm nasıl gerçekleşr?
5. Python dlnn blgsayar bellek yönetm sürecndek rolü nedr?
6. Python programlama dlnde hang temel ver tpler bulunur? Her brnn özellkler nelerdr?
7. Ver tpler arasında kaç türlü dönüşüm yapılablr?
8. Python dlnde kullanılan operatörler nelerdr?
9. Açık ve örtülü ver tp dönüşümü arasındak fark nedr?
10. Hang durumlarda açık, hang durumlarda kapalı dönüşüm yapmanız gerekeblr? Neden?
11. Değşr (mutable) ve değşmez (mmutable) nesneler arasındak temel farklar nelerdr?
12. Ver yapıları ve türler arasında hangler değşr , hangler değşmezdr?

**Başlamadan Önce**

Br programlama dlnde ver saklamak ve şlem yapmak çn değşkenlere ( varables ) htyaç duyulmaktadır . Python
dlnde de dğer dllerde olduğu gb değşkenler tanımlanmaktadır; ancak Python dlndek değşkenler , değşkenn ver
tp, adı ve referans sayısı adı verlen blglerle tanımlanmaktadır . Br nev şaretç ( ponter ) konumundadırlar . Değşken
tanımı gerçekleştrldkten sonra öneml br dğer kavram se bellek yönetm konusudur , çünkü blgsayar belleğnn
verml bçmde kullanılması, blgsayar programı çn de önem teşkl etmektedr . Bu nedenle, bu bölümde Python


programlama dlnn bellek yönetm le lşksne değnlmştr . Br Python programı çnde kullanılablen farklı ver
tpler tanıtılarak bu ver tplerne özgü farklı fonksyonların kullanımı gösterlmştr .
Değşken ve farklı ver tplernn verlmes sayesnde elde bulunan probleme özgü çeştl şlemlern gerçekleştrles
mümkündür . Bunun çn Python le kullanılan her brnn farklı farklı görevler olan matematksel, atama, btsel şlem,
karşılaştırma, mantıksal, üyelk ve kmlk operatörlerne ve bu operatörlerle gerçekleştrlmş olan çeştl örneklere yer
verlmştr .
Br Python programına klavyeden grlen br ver metnsel br fade bçmnde okunablr . Pek ya bu vernn sayısal hale
dönüştürülmes gerekrse? Bu ve benzer durumlarda ver tp dönüşümü yapmak gerekeblmektedr . Bu bölümde açık
(castng/explct converson ) ve örtülü ( coercon, mplct converson ) ver tp dönüşümünden bahsedlmş, her k
yöntemn avantaj ve dezavantajlarına değnlrken, farklı örneklerle konunun anlaşılması sağlanmaya çalışılmıştır . Dğer
programlama dllernde olduğu gb Python dlnn da yapı ve şleyş le lgl kendne özgü bazı unsurları
bulunmaktadır . Bu unsurların önemllernden ks, değşr (mutable) ve değşmez (mmutable) nesne kavramlarıdır . Bu
nedenle son olarak, değşr ve değşmez nesne kavramları anlatılmıştır . Nesnelernn bellekte nasıl davranış
sergledklern kavrayarak programın daha y kontrol edlmes sağlanmış olur .

## 2.1. Değşken, İşar etç ve Lteral

Programlamada ver saklamak üzere blgsayar belleğndek adreslere verlen sme değşken  (varable ) adı verlmektedr .
Değşkenler km zaman br karakter , br fade, br metn ya da ondalıklı sayı olablr . Bu çeştllk, değşkenn ver tp n
(data type ) gösterr . Örneğn; C dlnde aşağıdak bçmde br fade verlmş olsun (V anderPlas, 2016a).
nt a = 25
Bu kod satırında 25 değer a değşkenne atanmıştır . Dğer br fade le blgsayar belleğnde br alan a olarak
smlendrlmştr . Değşkenn ver tp tam sayı (nteger/nt) olarak belrlenmştr . = matematkte kullanılan eşttr şaret
değl, artık br atama (assgnment) operatörüdür . Atama çoğu programlama dllernde sağdan sola doğru yapılır . Tersne
br örnek verlecek olursa; R programlama dlnde a = 25 (sağdan sola), 25 -> a (soldan sağa) ve a <- 25 (sağdan sola)
fadelernn tümü 25’n a değşkenne atanmasını sağlar .
Python dlnde se aşağıdak lk kod satırında aslında br şaretç (ponter ) tanımlanmış olur . Yan tanımlanan a sm lgl
bellek adresn şaret eder . Bunun çn önceden br ver tp tanımlanmasına gerek duyulmaz. Dnamk bçmde a’nın
gösterdğ ver tp değştrleblr . 25, "Yrm Beş", 2.5 gb a’nın aldığı değerlere lteral  adı verlr .
Çeştl programlama dllernde noktalı vr gül kullanımının (;) ortak anlamı, mevcut fadey btrmek veya sonlandırmaktır
(Sawant, 2021). C, C++ ve Java gb programlama dllernde, br kod satırını sonlandırmak çn noktalı vr gül kullanmak
gerekr; ancak yukarıdak kod bloğundan da anlaşılacağı gb Python dlnde böyle br zorunluluk yoktur . Python dlnde
noktalı vr gül daha çok br ayırım fade etmektedr ve aynı satırda brden fazla şlem yapılması durumlarında kullanımı
terch edleblmektedr . Örneğn; aşağıda aynı satırda üç farklı değşken tanımlanmıştır .
Yukarıda dyez/hashtag (#) şaret le gösterlen br yorum satırı dır (comment lne ). Yorum satırları programlamada sıkça
kullanılan özellklerden brdr . Dlden dle gösterm bçm değşse de kullanım amacı kod dosyasını okuyan kşler çn
lgl koda lşkn br pucu verlmesdr . Yukarıda tek br satırdan oluşan Python yorum satırı bulunmaktadır (# İlk
tanımlanan değşkenler: ). Çok satırdan oluşan yorum satırları üç çft tırnak (""" … """) arasına yazılarak oluşturulablr .
Bununla lgl örneğe aşağıda yer verlmştr .

**Değşken Tanımlama Kuralları**


Dğer programlama dllernde olduğu gb Python dlnde de değşken tanımlamanın belrl kuralları vardır . Python
programlama dlnde br değşken adı verlrken aşağıdak hususlara dkkat edlmeldr .
• Mutlaka br harf veya alt çzg (_) karakter le başlamalıdır .
• Asla br sayı le başlayamaz, yalnızca alfanümerk karakterler ve alt çzgler çereblr (A-z, 0-9 ve _ ), değşken
adlarında Türkçe karakter (ç, ğ, ı, ö, ş, ü) kullanımı terch edlmez, değşken adı arasına boşluk(lar) konmaz.
• Python’a özgü anahtar kelmelerden herhang br olamaz (max, mn, f, elf, whle, for , sum, vb.).
Aşağıda hatalı değşken tanımlamalarına örnekler verlmştr . Aslında Spyder bunu fark edp 086_say değşkennn
tanımlandığı satırının başına kırmızı br kaz şaret ble koymuştur (Bu özellk de aslında Spyder edtörünün yazım
hatalarını otomatk algılaması sayesndedr). Bu satırda yer alan değşken adı 086 gb br sayı le başlatılmaya
çalışılmıştır . lk-say değşken tanımlanırken arada çıkarma şlem operatörü olan kısa çzg yer almaktadır . Son
değşkende se değşken adı arasında br boşluk bırakılmıştır .
Kend adımı kullanarak yapmaya çalıştığım 21 numaralı kod satırını çalıştırırsanız elf aynı zamanda Python dlnde karar
yapıları çn kullanıldığından, yan Python’a özgü br sözcük olduğundan Console’da şu şeklde br hata mesajı
dönecektr .
Bu durumda adaşım olmadığınız ve elbette yukarıda verlen değşken tanımlama kurallarına uyduğunuz sürece kend
adınızı kullanarak değşken tanımlayablrsnz. Hatalı değşken tanımlamalarına lşkn örnekler nceledkten sonra
uygun değşken tanımlamalarına lşkn bazı örnekler şöyle verleblr:
Python’da değşken adları büyük/küçük harfe duyarlıdır ( case senstve ). Aşağıda verlen örnekte olduğu gb eğer br
değşken lkSay adında tanımlanıp sonrasında lksay olarak çağrılırsa hata mesajı alınır .
Python dlnn öne çıkan özellklernden br de çoklu atama şlemne zn verlmesdr . Örneğn; aşağıdak kod satırında
aynı anda a, b, c, d değşkenlerne 5, 10, 20, 25  değerler atanmıştır . Python dlnde makne öğrenmes, ver görselleştrme
gb çeştl amaçlarla gelştrlen fonksyonların ger döndürdüğü değerlern blnmes ve çoklu atama kullanımı daha
verml kod yazılmasını sağlar .


## 2.2. Blgsayar  Belleğ ve Bellek Yönetm

Br blgsayarın belleğ sayfaları boş olan br ktaba benzetleblr (V anTol, 2019). Ktabın yazarları, bellekte ver
depolamak steyen blgsayardak brtakım farklı uygulama ya da süreçler olarak görüleblr . Elbette ktaba yazı yazma ve
slme şlern düzenleyen yan bellekte ver yönetmn sağlayan br yönetc bulunmaktadır . Bellek yönetm (memory
management ), uygulamaların ver okuması ve yazması şlemdr . Yen verlern saklanması, yenlere yer açılablmes çn
artık kullanılmayan verlern bellekten kaldırılması şlemler gerçekleştrlmektedr . İşte bu, blgsayardak bellek tahss
(memory allocaton ) sürecnn en sade bçmdek tanımıdır . Bu noktada şletm sstem, bellekten okuma ve belleğe
yazma şlern yürütürken, Python gerçekleştrm/yorumlayıcısı ( mplementaton ) da Python uygulaması tarafından
yürütülen Python kodları çn bellek yönetmn sağlar . İlk bölümde anlatıldığı gb Python dlnn br
gerçekleştrm/yorumlayıcısı, CPython referans uygulaması tarafından temsl edldğ gb, Python dlnde yazılmış
programların yürütülmes çn destek sağlayan br program veya ortam olarak anlaşılmalıdır (wk.python.or g, 2023b).
Örneğn; C gb br dlde aşağıda verlen kod satırını yazarak, x adlı br hafıza alanı ( memory bucket ) tahss edlr ve bu
alana 10 değern yazılır (V anderPlas, 2016a).
Python dlnn nesneye yönelml yapısı gereğ her şeyn aslında brer nesne olduğu fade edlmektedr . Bu durum
s.nstance() fonksyonuyla kontrol edleblr . Aşağıdak Python kodunda x ve ad olarak tanımlanan değşkenlern brer
nesne olduğu sonucu ger döndürülecektr (ekrana True yazdırılır).
Br Python nesnes; (1) tanımlanan değşkenn ver tp  (type), (2) esas değer  (value ) ve (3) bellek yönetmnde
kullanılan referans sayısı  (reference count ) olmak üzere üç temel blgy tutmaktadır . Referans sayısı, br nesnenn
sstemdek dğer nesneler tarafından kaç kez referans verldğn gösterr (geeksfor geeks.or g, 2020). Br nesneye yapılan
referanslar kaldırıldığında, lgl nesnenn referans sayısı azalır . Referans sayısı sıfır olduğunda se nesnenn bellekten
kaldırılması sağlanır . Python dlnde x değşken tanımlandığında bu durum aşağıdak şeklde olduğu gb temsl
edleblr .
Yukarıdak tanımlama le aynı nesneye atıfta bulunacak başka br y referans değşken yaratılır çünkü Python, nesne zaten
aynı değere sahpse, aynı nesne referansını yen br değşkene tahss ederek bellek kullanımını optmze eder .


x le y değşkenlernn aynı bellek adresn gösterdğ d() fonksyonu le kontrol edleblr . Her ks çn de
140703148548976 döndürülmüştür .
Eğer x’e 10 eklenrse bu defa artık x’n 10 le olan bağlantısı kaldırılır ve artık 20 değern gösterr , y’de herhang br
değşklk yaşanmaz. Farklı bellek adreslern gösterdkler yne d() fonksyonu kullanılarak görüleblr .

**Intern Nesneler**

Python, bellekte belrl br nesne alt kümesn önceden oluşturur ve bunları günlük kullanım çn genel ad alanı nda
(global namespace ) tutar . Bunlara ntern nesne  denlmektedr . CPython 3.7’de; -5 le 256 arasındak tam sayılar , yalnızca
ASCII harflern, rakamlarını veya alt çzgler çeren metnsel fadeler ntern nesnelerdr (Jones, 2019). a ve b
değşkenlernn aynı bellek adresn şaret ettğ görüleblr . Tanımlanan c ve d değşkenler se ntern nesne tanımında
verlen lmt 256’yı geçtğnden farklı bellek adreslerne sahptr .
Benzer durum metn1, metn2, metn3 ve metn4 değşkenler çn de geçerldr .


## 2.3. Python Dlnde Temel Ver Tpler

Python programlama dlndek temel ver tpler aşağıdak tabloda verlmektedr . Bunlar , tam sayılar , kayan noktalı
sayılar , kompleks sayılar , Boolean değerler , metnsel fadeler ve None tpdr .
Strng (str):  Her türlü karakter ve metnsel fadeler (dzge) çn kullanılablmektedr . Bastçe, metnsel fadeler , karakter
tutan br koleksyon şeklnde düşünüleblr . Tek ya da çft tırnak arasında yazılan her şey br metnsel fadedr . Aşağıda
verlen satırlarda ad ve soyad sml k str tpnde değşken verlmştr . Bu metnsel fadeler ster tek ster çft tırnak
kullanılarak tanımlanablr .
Br öncek bölümde Python’a merhaba demek çn kullanılan prnt() fonksyonunun genel görev ekrana yazdırma
şlemn gerçekleştrmektr . Metnsel fadeler başta olmak üzere dğer ver tpleryle brlkte yazdırma şlemlernde
sıklıkla terch edlmektedr . Yukarıdak ad ve soyad değşkenlerne lâveten br yas değşken tanımlansın. prnt()
fonksyonu çnde farklı ver tplernden olan değşkenler brbrlernden vr gülle ayrılarak uyumlu br bçmde Console
ekranına yazdırılablr .
Elde edlecek ekran görüntüsü şu şeklde olur .
Eğer fade veya değşkenlern değer Consol’da alt alta yazı yazdırmak stenrse, tıpkı çoklu yorum satırlarında olduğu
gb metn üçer çft tırnak arasına yerleştrleblr . Aşağıda lgl Python kodları ve Console çıktısı yer almaktadır .


Metnsel fadeler + operatörü le de brleştrleblr (bknz. aşağıdak lk kod satırı); ancak metn dışında br değşken le
denenrse hata mesajı dönecektr (bknz. aşağıdak knc kod satırı).
Ayrıca dğer programlama dllernde olduğu gb metnsel fadelerle çalışırken alt satıra nme, satır başına geçme gb
çeştl şlemlere htyaç duyulablr . Bu tür şlemler kaçış  (escape ) karakterler le sağlanmaktadır . Aşağıdak tabloda sıkça
kullanılan bazı kaçış karakterlerne yer verlmştr (w3schools.com, 2023).
Karakter Açıklama
\' Tek tırnak
\” Çft tırnak
\\ Ters bölü (Backslash)
\n Yen satır
\r Satır başı
\t Tab
\b Ger tuşu (Backspace)
Kaçış karakterler le lgl bazı örnekler nceleneblr .
Ayrıca metnler brer karakter  dzs  olarak düşünüleblr . Bu dznn elemanlarına se ndeksler kullanarak ulaşmak
mümkündür . Unutulmaması gereken en öneml nokta se Python dlnde ndeks değernn sıfırdan başlamasıdır . Örneğn;
adSoyad = "Züber Doğan" olsun. Bu durumda verlen Python kodları çn aşağıdak çıktılar elde edlecektr .
Python Kodu Çıktı
adSoyad[1] l
adSoyad[1:] lf Kartal
adSoyad[:1] E


adSoyad[1::2] lfKra
Python dlnde metnsel fadelere (strng) özgü pek çok metot mevcuttur . Bu metotlardan bazılarını ncelemek çn
rastgele oluşturulan br dna değşken tanımlansın. Bu değşkenn uzunluğu (strng ver tpnde olduğundan kaç
karakterden oluştuğu blgs) len() fonksyonu yardımı le bulunablr . Büyük ya da küçük harfe dönüştürme, ndeks
bulma ya da belrl br parçanın yer değştrmes gb bazı örneklere aşağıda yer verlmştr .
Python Kodu Çıktı
len(dna) 28
dna.upper() TGTCGT AGGGACGGGCCAACGTTCCT AG
dna.fnd("tag",0,len(dna)) 5
dna.rfnd("cc",0,len(dna)) 23
dna.replace("tag", "gta") tgtcggtaggacgggccaacgttccgta
Unutulmamalıdır k yukarıdak tabloda verlen metodların kullanımıyla dna değşkennn yapısında herhang br kalıcı
değşklk olmaz. Yapılan değşklğn kalıcı olması çn atama şlemnn de gerçekleştrlmes gerekr . Örneğn; tüm dna
dzlmn büyük harfe kalıcı bçmde çevrmek çn aşağıdak kod satırı kullanılablr:
Tam Sayı ( nteger , nt): Ondalıklı kısmı bulunmayan her sayı tam sayılara grmektedr . Aşağıda verlen örnek Python
kodlarında x, y ve z adında tam sayı değşkenler tanımlanmıştır ve bunlara sırasıyla 50, -900 ve 0 değerler atanmıştır .
Tam sayılar çn belrlenen br maksmum/mnmum üst/alt lmt bulunmamaktadır . Blgsayarın kullanılablr adres alanı
mktarı le sınırlıdır .
Kayan Ondalıklı Sayı ( float ): Çoğu kaynakta kayan ondalıklı sayı olarak Türkçeye çevrlmştr . Devrl ya da ondalıklı
sayılar bu ver tp altında nceleneblr . x, y ve z değşkenler float ver tpnde tanımlanmıştır . 109. ve 1 10. satırlarda se
sayıların blmsel gösterm şekl yer almaktadır . 109. satır çalıştırıldığında 100.0, 1e-3 çalıştırıldığında se 0.001 yazdırılır .
Kompleks Sayılar  (complex ): Kompleks sayılar br gerçel ( real) ve br de sanal ( magnary ) bölümden oluşan sayılardır .
Yalnızca sanal kısmı da bulunablr . Kompleks sayılara lşkn değşken tanımlaması örneklerne aşağıda yer verlmştr:
Boolean ( bool): Boolean Cebr matematğn en öneml konularından brdr . Boolean cebrnde ele alınan mantıksal
önermeler bastçe ya Doğru (T rue) ya da False (Y anlış) olarak ntelendrleblr . Örneğn; “Tüm memel hayvanlar karada
yaşar .” -> Yanlış!
Blgsayarlar açısından nceleyecek olursak, temel anlamda bldğmz blgsayarların (kuantum blgsayarları harç
tutuyoruz) çalışma prensb 0 ve 1 mantığı kl (bnary) sayı sstemne dayalıdır . Her türlü ver 0 ve 1’ler le gösterleblr .
Örneğn; 250’nn bnary karşılığı 1 1111010, “elf”n bnary karşılığı se 01 100101 01 101100 01 101001 01 1001 10 olarak
verleblr . İkl kodlama br bakıma vernn daha bast ve kolay saklanmasını ve şlenmesn sağlar . VE (AND), VEY A
(OR) ya da DEĞİL  (NOT) gb mantıksal şlemler de bu sayede gerçekleştrleblr .
Python dlndek bool ver tp True ve False gb k değer almaktadır . Operatörler le gerçekleştrlen şlemlern sonucu
olarak bool ver tpnde döndürülürler .


NoneT ype:None, hçbr şey (null) olarak düşünüleblr . None dışında başka mümkün olası değer mevcut değldr . Python
dlnde gerye döndüreceğ değer olmayan fonksyonların döndürdüğü değer None’dır . Genellkle ver blm
çalışmalarında verdek eksk değerler None le gösterlmektedr . Aşağıdak n değşken None olarak tanımlanmıştır .

## 2.4. Operatörler  le İşlemler

Bu bölümde Python dlnde yer alan matematksel operatörler , atama operatörler, btsel şlem operatörler, karşılaştırma
operatörler, mantıksal operatörler le üyelk ve kmlk operatörler ele alınmıştır .

### 2.4.1. Matematksel Operatörler

Özellkle sayılar söz konusu se matematksel şlem yapablmek çn toplama, çıkarma gb bazı artmetk operatörlerne
htyaç duyulmaktadır . Aşağıda yer alan tabloda bazı temel artmetk operatörlerne yer verlmştr . Örneğn; a ve b gb
k değşken tanımlansın:
Operatör Açıklama Örnek Sonuç
+ Toplama a + b 17.5
- Çıkarma a - b 2.5
* Çarpma a * b 75.0
/ Bölme a / b 1.3333333333333333
% Mod alma a % b 2.5
** Üs a ** b 31622776.60168379
// Kalansız Bölme a // b 1.0
İşlemlerdek öncelk sırası da yne matematkte olduğu gbdr . Öncelkle, parantez çndek şlemler yapılır . Ardından
çarpma ve bölme, sonrasında da toplama ve çıkarma gerçekleştrlr . Bu nedenle aşağıda verlen kod satırının sonucu
-1980.0’dır .

### 2.4.2. Atama Operatörler

Python atama operatörler ve bu operatörlern bazı özel bçmlerde fade edlş bçmler aşağıdak tabloda sunulmaktadır .
Tanımlanan a değşken çn atama operatörler le verlen örneklere ve elde edlen sonuçlara yer verlmştr .
Operatör Örnek Benzer  Gösterm Sonuç
= a = 25 a = 25 25
+= a += 25 a = a + 25 50
-= a -= 25 a = a - 25 0
*= a *= 25 a = a * 25 625
/= a /= 25 a = a / 25 1.0


%= a %= 25 a = a % 25 0
//= a //= 25 a = a // 25 1
**= a **= 3 a = a ** 3 15625

### 2.4.3. Btsel İşlem Operatörler

Btsel şlem yapan operatörlere at tablo se aşağıda verlmştr . Bu tablodan elde edlen sonuçlar çn a ve b
değşkenlernn 8 byte’lık göstermler düşünülmeldr . Bu nedenle de aşağıdak kod satırlarında değşkenler
tanımlandıktan sonra btsel karşılıkları da ekrana yazdırılmıştır . Buna göre a ve b değşkenlernn btsel karşılığı sırasıyla
0001 1001 ve 00010100’dr .
&btsel and, | btsel or ve ^ se btsel xor operatörüdür . >> verlen kayma sayısı kadar sağa kaydırır ve sol kısma sıfır
ekler , << verlen kayma sayısı kadar sola kaydırır ve sağ kısma sıfır ekler .
Operatör Örnek Benzer  Gösterm Sonuç
& a &= 25 a = a & b 16
| a | = 25 a = a | b 29
^ a ^= 25 a = a ^ b 13
>> a >>= 25 a = a >> 1 12
<< a <<= 25 a = a << 1 50

### 2.4.4. Karşılaştırma Operatörler

Python le aşağıdak gb k değşken tanımlansın.
Karşılaştırma çn kullanılan bazı operatörler , bu operatörler kullanılarak hazırlanarak oluşturulan örnekler ve elde edlen
sonuçlar aşağıdak tabloda verlmştr .
Operatör Açıklama Örnek Sonuç
== Eşttr a == b False
!= Eşt değldr a != b True
> Büyüktür a > b False
< Küçüktür a < b True
>= Büyük eşttr a >= b False
<= Küçük eşttr a <= b True

### 2.4.5. Mantıksal Operatörler

Programlamada özellkle kontrol yapıları ve döngüler le lgl bölümlernde mantıksal fadelerden ve dolayısıyla boolean
fadelerden sıklıkla yararlanılmaktadır . Daha önce fade edldğ gb VE (AND), VEY A (OR) ya da DEĞİL  (NOT)
Python dlnde kullanılan mantıksal operatörlerdr . and  operatörü  önünde ve arkasındak fadelern her ksnn de True
olması durumunda True döndürür , aks halde False döndürür . or operatörü  önünde ve arkasındak fadelern brnn True
olması durumunda True döndürür , aks halde False döndürür . not operatörü se çıkan sonucun tam tersn döndürür , br
başka deyşle fade True se False, False se True döndürür .
Aşağıda a, b ve c gb üç değşken tanımlanmıştır . Tanımlanan bu değşkenlerle karşılaştırma ve mantıksal operatörler
temel alınarak altı farklı fade yazılmıştır .


Bu fadelerden elde edlen sonuçlar sırasıyla şöyledr: False, False, True, True, True, True.

### 2.4.6. Üyelk ve Kmlk Operatörler

nüyelk  (membershp ) operatörüdür . Eğer hedeflenen değer bulunursa True, aks durumda False döndürülür . not n se
elde edlen değern tam tersn döndürür . s kmlk ( dentty ) operatörüdür . Eğer adres değerler eştse True, aks durumda
False döndürülür . s not n se elde edlen değern tam tersn döndürür . Aşağıda verlen fadelerden elde edlen sonuçlar
sırasıyla şöyledr: True, True, False, True.
Bu noktaya kadar ele alınan operatörlern öncelk sırası yüksekten düşüğe doğru şöyle verlmektedr: **, ~ , * / % //, + -,
>> <<, & (btsel), ^ |, <= < > >=, <> == !=, = %= /= //= -= += *= **=, s s not, n not n, not or and (Uzun, 2023).
Brlkte verlen karma şlemlerde bu sıra göz önünde bulundurulmalıdır .

## 2.5. Açık ve Örtülü Ver Tp Dönüşümü

Açık ver tp dönüşümü  (castng/explct converson ) adından da anlaşılacağı gb br değşkenn ver tpn br başka ver
tpne değştrme anlamına gelr . Ver tp dönüşümü; nt(), bool(), float(), str() gb tp dönüşümü çn hazır bulunan
fonksyonlarla gerçekleştrlmektedr . Bunlar aynı zamanda lgl ver tpne özgü yapıcı metot  (constructor ) olarak da
anılmaktadırlar .
İşlem Dönüşüm Sonuç
bool(1000) nt→boolean True
bool(750) nt→boolean True
bool("Elf") strng→boolean True
bool(0) nt→boolean False
bool(-300) nt→boolean True
bool("") strng→boolean False
float(100) nt→float 100.0
float(-25) nt→float -25.0
float("Elf") strng→float ValueError: could not convert strng to float: 'Elf'
float(T rue) boolean→float 1.0
nt(False) boolean→nt 0
nt(25.5) float→nt 25
str(52000) nt→strng '52000'
str(-50) nt→strng '-50'
str(False) boolean→strng 'False'
Açık ve örtülü ver tp dönüşümü ( coercon, mplct converson ) arasındak en büyük fark, dönüştürmenn manuel
yapılırken tp zorlamanın otomatk yapılmasıdır (Mathew , 2021). Python, ver kaybını önlemek çn her zaman daha
küçük ver tplern daha büyük ver tplerne dönüştürür . Açık ver tp dönüşümü sonuçları daha tahmn edleblrdr;
oysa örtülü ver tp dönüşümünde beklenmeyen sonuçlarla karşılaşılablr . Her ksnde de blg kaybı yaşanablr; ancak
açık ver tp dönüşümü söz konusu olduğunda programcının gerekl blgy koruma konusunda daha fazla kontrolü


bulunmaktadır . Örtülü ver tp dönüşümü önceden belrlenen kurallarla sınırlı kalırken, açık ver tp dönüşümü daha
esnektr (vegbt, 2023).
Örtülü ver tp dönüşümü konusunda da aşağıda verlen örnekler nceleneblr . Örnek 1 ve 2’de c’nn ver tp float olarak
ortaya çıkar . Örnek 1’de c’nn değer 11.0, Örnek 2’de se 0.6’dır. Örnek 3’ te c’nn değer 7 olarak elde edlr . Tam sayı ve
boolean ver tplernn toplanması yne br tamsayı değşkenn elde edlmesn sağlamıştır . Örnek 4’ te se a ve b’nn
farkının c’ye atanması sırasında “ TypeErr or: unsupported operand type(s) for -: 'str' and 'nt' “ hatası ortaya çıkar ve bu
şlem gerçekleştrlemez.

## 2.6. Değşr  ve Değşmez Nesneler

Programlamada, br nesne oluşturduktan sonra durumunu değştremezsenz bu nesneye değşmez  (mmutable ) denr .
Aksne, oluşturulduktan sonra dâhl durumunu değştrmenze zn veren nesnelere değşr  (mutable ) denr . Kısaca
özetlemek gerekrse, br nesnenn durumunu veya çerdğ very değştrp değştremeyeceğnz, o nesnenn değşr m
yoksa değşmez m olduğunu belrlemektedr .
Python programlama dlnde tamsayılar , kayan ondalıklı sayılar , karmaşık sayılar ve boolean gb tek öğel ver tpler her
zaman değşmezdr ( mmutable ). Değşmez ver tplerne metnsel fadeler de dâhldr . Bunların değern değştrmenn br
yolu yoktur . Sadece yen br değere sahp yen br nesne oluşturma ve esksn atma seçeneğ bulunmaktadır .
Python le programlamada br sonrak bölümde ele alınacak olan lste (lst), demet  (tuple ), küme  (set) ve sözlük
(dctonary ) gb koleksyon ver yapıları söz konusu olduğunda, şler braz daha farklıdır . Lste, küme ve sözlükler
değşr , demet değşmezdr .
Ver Tp Sınıfı Mutable/Immutable
Sayılar nt, float, complex Immutable
Metnsel fadeler str Immutable
Demet tuple Immutable
Boolean bool Immutable
Lsteler lst Mutable
Kümeler set Mutable
Sözlükler dctonary Mutable
Verlen blgler doğrultusunda küçük br hatırlatma yapılacak olursa, Python dlnde değşkenler verlern kendsn
tutmaz; ancak verlern depolandığı bellek adresne başvurur . Mevcut br değşken yensne atadığınızda, orjnal
değşken çn br takma ad  (alas ) oluşturulur .Var olan br değşkenn takma adını oluşturduğunuzda, her k değşken de
aynı referansa sahp olacaktır . Değşken takma adları, aynı nesneye veya ver parçasına şaret ederek aynı bellek adresn
referans alır:


Sayılar , dzeler ve demetler gb değşmez nesnelere şaret eden değşken takma adları oluşturduğunuzda, değşklkler
(mutasyonlar) hakkında endşelenmeye gerek yoktur . Değşr türlerde, belrl br takma addak değşklk dğer takma
adların ger kalanını etkleyecektr .
Örneğn; br öncek örnekte tanımlanan a değer 1 artırıldığında, b değernde br değşklk meydana gelmemektedr .
Br sonrak kod bloğunda değşr nesnelere örnek olması bakımından br renkpalet_A  lstes tanımlanmıştır , sonrasında
renkpalet_A  kullanılarak renkpalet_B oluşturulmuştur . renkpalet_A ’ya yeşl reng eklendğnde bu değşklğn
renkpalet_B’ye de yansıdığı görüleblr .

**Bölüm Özet**

Bu bölümde, programlama dünyasının temel kavramları ve Python dlndek temel ver tpler ncelenmştr . Değşkenler ,
şaretçler ve lteraller hakkında blg verlrken, blgsayar belleğ ve bellek yönetm konularına da değnlmştr . Ayrıca,
operatörlerle yapılan şlemler ve açık ( explct ) ve örtülü ( mplct ) ver tp dönüşümler açıklanmıştır . Değşr ( mutable ) ve
değşmez ( mmutable ) nesnelern farkı anlatılarak, programlamaya yen başlayanlara ve deneyml programcılara yönelk
faydalı br kaynak oluşturulmuştur .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/


Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53


Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew


wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Br değşkenn tanımı aşağıdaklerden hangsdr?
(Çoktan Seçmel)
(A) Br metn fades.
(B) Br sabt değer .
(C) İsmlendrlmş br bellek alanı.
(D) Br şaretç türü.
(E) Matematksel br operatör .
Cevap-1 :
İsmlendrlmş br bellek alanı.
Soru-2 :
İşaretçler (ponters) aşağıdaklerden hangsyle lşkldr?
(Çoktan Seçmel)
(A) Dosya şlemler
(B) Ver sıkıştırma
(C) Döngüler
(D) Bellek yönetm
(E) Koşul fadeler
Cevap-2 :
Bellek yönetm
Soru-3 :
Hang ver tp (kayan) ondalıklı sayıları temsl eder?
(Çoktan Seçmel)
(A) float
(B) str
(C) NoneT ype
(D) bool
(E) char


Cevap-3 :
float
Soru-4 :
Aşağıdaklerden hangs Python’a özgü ver yapılarından brdr?
(Çoktan Seçmel)
(A) nt
(B) tuple
(C) NoneT ype
(D) bool
(E) char
Cevap-4 :
tuple
Soru-5 :
İk değer karşılaştırmak çn hang Python operatörünü kullanablrsnz?
(Çoktan Seçmel)
(A) =
(B) ||
(C) &
(D) |
(E) ==
Cevap-5 :
==
Soru-6 :
Aşağıdak seçeneklerden hangsnde “a değşkennn 3’e bölümünden kalanın 1 olması” fades doğru bçmde
yazılmıştır?
(Çoktan Seçmel)
(A) a / 3 == 1
(B) a % 3 == 1
(C) a / 3 = 1
(D) a % 3 = 1
(E) a & 3 = 1
Cevap-6 :


a % 3 == 1
Soru-7 :
Örtülü ver tp dönüşümü nedr?
(Çoktan Seçmel)
(A) Kullanıcının müdahales olmadan yapılan dönüşümdür .
(B) Ver kaybını önlemek çn kullanılan dönüşüm türüdür .
(C) Ver türünün açıkça belrtldğ dönüşüm türüdür .
(D) İsteğe bağlı olarak gerçekleşen ver tp dönüşümüdür .
(E) Yalnızca sayısal ver tpler arasında yapılan dönüşüm türüdür .
Cevap-7 :
Kullanıcının müdahales olmadan yapılan dönüşümdür .
Soru-8 :
Aşağıdaklerden hangs değşmez ( mmutable ) ver tpne örnektr?
(Çoktan Seçmel)
(A) lst
(B) dct
(C) set
(D) tuple
(E) Hçbr
Cevap-8 :
tuple
Soru-9 :
Aşağıda verlen Python kodu çalıştırıldığında elde edlen sonuç seçeneklern hangsnde doğru şeklde verlmştr?
(Çoktan Seçmel)
(A) 1
(B) 1.0
(C) True
(D) False
(E) 0
Cevap-9 :
1.0


Soru-10 :
Aşağıda verlen Python kodu çalıştırıldığında elde edlen sonuç seçeneklern hangsnde doğru şeklde verlmştr?
(Çoktan Seçmel)
(A) True
(B) False
(C) 50
(D) 25
(E) 0
Cevap-10 :
False


# 3. VERİ YAPILARI: LİSTE, DEMET, KÜME, SÖZLÜK

SÖZLÜK

**Bölümle İlgl Özlü Söz**

Önce yap, sonra doğru yap, sonra daha y yap.
Addy Osman , Yazılım Mühends

**Kazanımlar**

1. Python dlnde lste ( lst) kavramını blr ve br lste oluşturma, br lsteye eleman ekleme ve çıkarma, lste elemanlarına
ndeks kullanarak ulaşma, br lstenn uzunluğunu bulma ve elemanların sıralanması gb lstelerle lşkl temel
fonksyonları kullanablr .
2. Python dlnde demet ( tuple ) kavramını, lstelerle olan benzerlkler ve farklılıkları blr ve br demet oluşturma, br
demetn elemanlarına erşme, br demetten ndeks kullanarak eleman çağırma, br demette br elemanın kaç defa tekrar
ettğ gb demetlerle lşkl temel fonksyonları kullanablr .
3. Python dlnde sözlük ( dctonary ) kavramını blr , br sözlüğün nasıl oluşturulacağını, br sözlüğe anahtar -değer çftler
ekleme ve çıkarma, sözlüktek br değere anahtarıyla erşme gb temel sözlük şlemlern gerçekleştreblr .
4. Python dlnde küme ( set) kavramını blr , br kümey oluşturma, kümeye eleman ekleme ve çıkarma le kümeler
kullanarak kesşm, brleşm, fark gb matematksel şlemler gerçekleştrme vb. temel küme şlemlern yapablr .
5. Python programında lste, demet, sözlük ve küme ver yapılarından uygun olanı seçeblr .
6. Lste, demet, sözlük ve küme ver yapılarından hangsnn değşr ( mutable ) ve hangsnn değşmez ( mmutable )
olduğunu blr .

**Brlkte Düşünelm**

1. Ver yapıları neden önemldr?
2. Python dlnde kullanılan temel ver yapıları nelerdr?
3. Br lste nasıl oluşturulur ve hang tür verler çereblr?
4. Lstenn ndeksler hang sayıdan başlar?
5. Br lsteye br eleman nasıl eklenr , çıkarılır ve değştrlr?
6. Demetler değşr nesneler mdr yoksa değşmez nesneler mdr?
7. Br demet nasıl oluşturulur ve hang ver tplern çereblr?
8. Lste ve demet arasındak farklar ve benzerlkler nelerdr?
9. Br demetn elemanlarına nasıl erşlr?
10. Br sözlük nasıl oluşturulur , nasıl eleman eklenr ve çıkarılır?
11. Br sözlükte br anahtara bağlı değer nasıl elde edleblr?
12. Br küme nasıl oluşturulur?
13. Kümeler üzernde gerçekleştrleblen temel şlemler nelerdr?

**Başlamadan Önce**


Ver yapıları, blgsayar programlarıyla çalışırken verler or ganze etmek, saklamak ve şlemek çn kullanılan temel
yapı taşlarıdır . Python, çeştl ver yapıları sunar ve bu ver yapılarından her br farklı kullanım senaryolarına ve
avantajlara sahptr . Bu bölümde, Python programlama dlnn temel ver yapıları olan lste, demet, sözlük ve küme
kavramları ele alınmıştır . Her br ver yapısının ne olduğu, nasıl oluşturulduğu ve çeştl fonksyonlarla nasıl
kullanılableceğ detaylı br şeklde, örneklerle açıklanmıştır . Python yardımı le ver yapılarının programlamadak rolü
ve önem kavranarak, hang durumlarda hang ver yapısının terch edlmes gerektğ gb konularda lerye yönelk
deneym kazanılacaktır .

## 3.1. Python Ver Yapıları

Br öncek bölümde Python programlama dlndek tam sayı ( nt), kayan noktalı sayı ( float ), kompleks sayılar ( complex ),
boolean, metnsel fadeler ( strng ) ve None temel ver tpler  ele alınmıştır . Bu bölümün konusu, Python dlnde dğer
ver tpler çn br tutucu (ya da kap) görev göreblen brkaç yerleşk bleşk ver yapısı bulunmaktadır . Bunlar aşağıdak
tabloda verlmştr . Tablodan da görüleceğ gb bu ver yapıları oluşturulurken köşel, yuvarlak ve kıvırcık (süslü)
parantezler kullanılmıştır . Hang ver yapısının nasıl oluşturulduğuna dkkat etmek gerekr . Her br ver yapısına at
detaylı açıklama ve örnekler sırasıyla verlecektr .
Ver Yapısı Örnek Açıklama
lst [“e”,”l”,””,”f”] Sıralı değşr koleksyon
tuple (1,2,3) Sıralı değşmez koleksyon
dct{34: “İstanbul”,
54: “Sakarya”}Sırasız değşr eşleme
set {1, 3, 5, 7} Benzersz değerlern sırasız değşr koleksyonu

## 3.2. Lsteler

Lsteler , Python dlndek temel sıralı ve değşken ver toplama türüdür (V anderPlas, 2016b). Köşel parantezler arasında
vrgülle ayrılmış değerlerle tanımlanablrler; örneğn, oluşturulan br sm lstes aşağıda yer almaktadır . type() le ver
yapısının lste olduğu görüleblr .
Lstelere özgü farklı fonksyonlar bulunmaktadır . Bunlardan en sık kullanılanı len() fonksyonudur . Lstenn kaç elemanı
olduğunu (uzunluğunu) döndürür . Aşağıdak kod satırı çalıştırıldığında 4 değer elde edlecektr .
Python, tek öğeler çn ndeksleme ( ndexng ) ve brden çok öğe çn dlmleme ( slcng ) yoluyla bleşk türlerdek öğelere
erşm sağlamaktadır . Bu konuda, Bölüm 2.3’ te metnsel fadeler le yapılan şlemlern benzer lstelere de uygulanablr .
Köşel parantez söz dzm kullanılarak erşm sağlanır . Python dlnde ndeksn sıfırdan başladığı kesnlkle
unutulmamalıdır . Aşağıda 1 1 elemanlı saylar lstes verlmektedr . Lste elemanlarına erşm örnekler saylar kullanılarak
sırayla açıklanmıştır .
Kod bloğunun lk satırında saylar lstes tanımlanmıştır . Ardından, lstenn 0. ndeksnde yer alan lk elemanı, sonrasında
da lstenn 3 ndeks numaralı dördüncü elemanı yazdırılmıştır . İndeks numarasındak eks (-) ndsn tersten (lstenn
sonundan) okunacağına şaret eder . Yan lstenn son elemanı olan 70’n ndeks numarası -1’dr , 63’ün ndeks numarası
-2’dr , … Bu şeklde devam eder . Dolayısıyla saylar[-1] le ekrana 70, saylar[-5] le ekrana 42 yazdırılır .


Aşağıdak kod bloğunda lstenn çnde belrl aralıklarda ya da düzende yer alan elemanlara erşm sağlanmaktadır . İlk
satırda ndeks 0’dan 5’e kadar olan elemanlar yazdırılır . 5. ndekstek eleman döndürülmez. saylar[5:] le 5. İndekstek
eleman dâhl lstenn sonuna kadar tüm elemanlar yazdırılır . Br sonrak adımda se -5. ndste yer alan elemandan (42)
ler doğru yazdırılır . saylar[0:5:2] satırında sona eklenen 2, ndeks 0’dan 5’e kadar olan elemanların 2’şer nds
atlanarak yazdırılacağını gösterr . Netcede [1, 14, 28] döndürülür . saylar[::5] se lstenn başından sonuna kadar 5’er
nds atlanarak elemanları döndürür . Br sonrak kod satırı da saylar[0:len(saylar):5] benzer şlem yapar . Sonuncu satır
saylar[::-1] se br nev lstey ters çevrr .
Lsteler tek ver tpnden oluşableceğ gb, brbrnden farklı ver tpnde nesnelere sahp olablr . Aşağıdak kod
bloğunda yer alan lk nesne örneğ öncek örnekteklere benzer şeklde; ancak bu kez boolean ver tpnde elemanlara
sahp br lstedr . Br sonrak örnekte se lste elemanlarının ver tp str , str, boolean, nt, float, lst olarak sıralanablr .


Aşağıdak ekran görüntüsünden anlaşılableceğ gb lsteler değşr ( mutable ) özellktedr . Elemanları değştrleblrdr .
Lstede 1. ndekste yer alan elf kartal , kara kartal  olarak değştrlmştr .
Br lste, lst() yapıcı metodu le de oluşturulablr . Örneğn;
Lstenn sonuna ekleme yapmak stenrse append() metodu kullanılablr . Aşağıda tanımlanan ml lstesnn sonuna 1 1
elemanı eklenmştr . Sonrasında lstenn stenlen ndeksne (önce 2. ndekse 20, sonra 10. ndekse 20 elemanı) özel olarak
eklenmştr .
Elemanları lsteden kaldırablmek çn remove() metodu kullanılır . Kaldırılmak stenen elemanı varsayılan olarak lste
başından kontrol etmeye başlar ve gördüğü lk ndekstekn kaldırır . Örneğn; ml lstesnden 20 elemanı kaldırılmak
stenrse, önce ndeks 2 olan 20 kaldırılacaktır .
Lste sonuna eleman eklenebldğ gb, lste sonundan eleman slmek de oldukça kolaydır . Bunun çn pop() metodu
kullanılır . Aşağıdak örnekte, lste sonundak 1 1 elemanı kaldırılmıştır .


Br elemanın lste çndek ndeks değernn de bulunmasına htyaç duyulablr . Bunun çn ndex() metodu kullanılablr .
Tıpkı remove()’da olduğu gb elemanın baştan lk görüldüğü yerdek ndeks numarası (9) döndürülür
Mevcut lstey sıralamak çn sort() metodu kullanılır . Varsayılan olarak artan bçmde sıralama yapılır .
Lstey tersne çevrmek çnse reverse() metodu kullanılablr . Tersne çevrme şlem lstede kalıcı br etk yaratacaktır .
Değşkenlern yer aldığı pencereden de bu durum görüleblr .
Boş br lste yaratmak çn aşağıdak kod satırının kullanılması yeterldr . Lstenn slnmes çnse del deym kullanılır .
Son satır my_lst lstesn slecektr .

## 3.3. Demetler

Demetler ( tuples ) brçok yönden lstelere benzemektedr; ancak köşel parantezler yerne yuvarlak parantezlerle
tanımlanmaktadırlar (bknz. tuple a). Ayrıca, herhang br parantez kullanılmadan da tanımlanablrler (bknz. tuple b).
Lstelerdekne benzer şeklde elemanlarına ulaşablmek mümkündür . Bu konuda aşağıdak örnekler ve sonrasında verlen
ekran görüntüler nceleneblr .


Demetler Python dlnde br fonksyonun ger döndürdüğü değerlern ver yapısı olarak da kullanılmaktadır (V anderPlas,
2016b). Örneğn; kayan noktalı sayıların (float) as_nteger_rato() metodu, pay ve payda bçmnde verlen sayıyı ger
döndürmek çn demet yapısını kullanmaktadır .
Demetler hakkında unutulmaması gereken en öneml özellklerden br değşemez ( mmutable ) olduklarıdır . Eğer
elemanlarından brnn lstelerde olduğu gb değern değştrmek stenrse, demetlern buna zn vermeyeceğne dar hata
mesajı alınır .
Br demete yen br eleman eklemek çn bazı yollara başvurulablr . Lstelerdek gb demetler çn de tanımlı tuple()
yapıcı metodu bulunmaktadır . Bu sayede dönüşümler rahatlıkla sağlanmaktadır . Örneğn; mevcut a demetn lste halne
getrmek ya da lstey demet halne getrmek mümkün olablr . Dolayısıyla br demet lsteye çevrdkten sonra htyaç


duyulan ekleme/çıkarma şlemler yapılablr ve ardından yenden demet halne getrleblr . Aşağıda verlen örnekte a
demetnde 4. ndekstek eleman 2 değer, “k” değerne çevrlmştr .
Eğer tek elemanlı br demet tanımlanmak stenrse, yuvarlak parantezler arasına yalnızca elemanı yazmak yeterl olmaz,
sona br de vr gül eklenmeldr; aks takdrde tanımlanan metnsel br fade (strng) olacaktır .
Br demetn slneblmes çn del deym kullanılablr . Bu deym aslında br ad alanına veya kapsayıcı türünden
nesnelere referansların kaldırılmasını sağlar (Pozo Ramos, 2023). Atama fadesnn ters br şlem gerçekleştrr . del, br
tür atama kaldırma fadesdr .
Tanımlanan k demet brleştreblmek çn + operatöründen faydalanılablr . Aşağıdak kod bloğundan çıktı olarak ('e', 'l',
'', 'f', 2, 0, 2, 3) elde edlr .
Tanımlanan bu son demetn kaç elemanlı (8) olduğunu göreblmek çn lstelerdekne benzer bçmde len() fonksyonu
kullanılablr .
Br elemanın br demet çnde kaç defa tekrarlandığı count() metodu yardımıyla bulunablr . Aşağıdak lk örnekte,
tamSaylar demetnn çnde kaç adet 1 sayısının olduğu bulunmaya çalışılmıştır . Sonuçta ekrana 3 yazdırılır . Eğer
demetn çnde olmayan br eleman count() metoduna verlrse, 0 (sıfır ) döndürülür .


Br demet çndek elemanın ndeks değern bulurken ve sıralarken lstelerdekne benzer şlemler gerçekleştrlr . ndex(),
“f” çn 3 değern döndürür; ancak son k satırda kontrol edlen elemanlar halhazırda a demetnn elemanı olmadığından
hata mesajı letr .
max(), mn(), any(), all() gb fonksyonlar lste ve demetlern elemanları le şlem yapmak çn uygundur . Örneğn; yen
adında br demetn en büyük ve en küçük elemanları max() ve mn() fonksyonları yardımı le bulunsun:
any() fonksyonu, eğer nesne elemanlarından herhang br çn True se True, all() fonksyonu se eğer nesne
elemanlarından her br çn True se True döndürmektedr . Bu blgye göre aşağıdak kod satırları nceleneblr . Sırasıyla,
False, True, True, False çıktıları üretlecektr .


## 3.4. Sözlükler

Sözlükler ( dctonares ), anahtar:değer  (key:value ) prensbn kullanan son derece esnek eşleme yapılarıdır ve Python
dlnn dâhl uygulamasının çoğunun temeln oluşturmaktadır (V anderPlas, 2016b). Kıvırcık parantezler çndek vr gülle
ayrılmış br anahtar:değer çftler lstes aracılığıyla oluşturulablrler . Br sözlüktek elemanlara, lste ve demetler çn
kullanılan dzn oluşturma sözdzm aracılığıyla erşlr ve ayarlanır , burada elemanın ndeks sıfır tabanlı br düzende
değl, sözlükte geçerl br anahtardır . Lste ya da demette olduğu gb elemanların belrl br düzen yoktur . Bu sıralama
eksklğ, sözlüklern çok verml br şeklde uygulanmasına zn verr , böylece sözlüğün boyutu ne olursa olsun rastgele
öğelere erşm çok hızlıdır .
baskentler adında br sözlük oluşturulmuştur . Bu örnekte, sözlük elemanları kıvırcık parantezler arasına tanımda fade
edldğ gb anahtar:değer mantığı le yazılmıştır . Anahtar:değer  eşleşmes örnek çn ülke:başkent  şeklndedr .
Aşağıdak kod bloğunun son k satırda, br anahtar kullanarak br sözlüğün değerne ulaşmak çn k farklı yol
verlmştr .
Elbette, br sözlüğün tüm anahtarlarını ve değerlern lstelemek mümkündür . Bu, sırası le keys() ve values() metotları le
gerçekleştrlr .
Sözlüğe yen br eleman eklenmes demek, yen br anahtar:değer çftnn eklenmes demektr . Köşel parantez çne
eklenecek olan yen anahtar yazılır , ardından eştlğn sağ tarafına bu anahtara karşılık atanacak değer yazılır .


Br sözlükten br anahtar:değer çft çıkarılmak stenrse, lste ve demette olduğu gb del deym kullanılablmektedr .
Ayrıca, sözlüğün son elemanını anahtar kullanarak çıkarmak çn pop(), doğrudan çıkarablmek çn poptem()
metotlarından da faydalanılablr .
Br sözlüğün elemanlarını lstelemek çn tems() metodu kullanılmaktadır .
Örneğn, aşağıdak gb yen adlı br sözlük tanımlanmış olsun. Bu yen sözlüğü baskentler sözlüğü le brleştrmek,
ardından “Y unanstan” anahtarına sahp “Athens” değernn “Atna” olarak değştreblmek çn update() metodu
kullanılır .
Tanımlanan br sözlüğün elemanlarını slmek çn clear() metodu kullanılır . Aşağıdak kod satırları çalıştırıldıktan sonra
ekrana {} yazdırılır , çünkü yen sözlüğü değl, yalnızca sözlük elemanları slnmştr .


Boş br sözlük oluşturmak çn aşağıdak kod satırı çalıştırılablr . Br öncek örnekte olduğu gb, eğer yenSozluk ekrana
yazdırılmak stenrse {} yazdırılacaktır .
Sözlükler konusunda dkkat edlmes gereken en öneml hususlardan brs anahtarların benzersz olmasıdır . Aynı anda k
ya da daha fazla aynı anahtardan bulunamaz. Bunun çn aşağıdak örnek nceleneblr . Aşağıda verlen sözlük
tanımlamasında 10 anahtarı k farklı değer çn kullanılmıştır; ancak lgl kod satırı çalıştırıldığında hata mesajı
döndürülmez. Bunun yerne aynı anahtarlardan sonuncu ve ona bağlı değer dkkate alınmaktadır .

## 3.5. Kümeler

Kümeler ( set), benzersz, sıralı olmayan ve değşr koleksyonlardandır . Python dlndek kümeler , metot ve operatörler
aracılığıyla küme matematğnde yer alan brleşm, kesşm, fark vb. şlemler yerleşk olarak çermektedr (V anderPlas,
2016b). Aşağıda 1-20 arasındak tek sayıları ve asal sayıları çeren k farklı küme tanımlanmıştır . Tanımlamada kıvırcık
parantezler kullanılmaktadır .
Bu k kümeye yen elemanlar eklemek çn add(), kümeden eleman slmek çnse pop() metotları kullanılablr .
Aşağıdak kod bloğunda asalSaylar kümesnn tekSaylar kümes le kesşm, brleşm ve asalSaylar kümesnn
tekSaylar kümesnden farkı gb üç temel küme şlem yer almaktadır . Bu şlemler sırasıyla, ntersecton(), unon() ve
dfference() metotlarıyla yapılableceğ gb bu metotlar yerne sırasıyla &, | ve – operatörler de kullanılablr .

**Bölüm Özet**

Bu bölümde, Python programlama dlndek temel ver yapıları ele alınmıştır . İlk olarak, lsteler üzernde durulmuştur .
Lsteler , brden çok very br araya getren, sıralı ve değşr ver yapılarıdır . Elemanlarını ndeksleme ve dlmleme
yöntemleryle erşmek mümkündür . Ardından, demetler ncelenmştr . Demetler de lstelere benzemektedr; ancak
değşmez ver yapılarıdır . Demetler , özellkle verlern değştrlmes stenmeyen durumlarda kullanılır . Sözlükler se


anahtar:değer çftleryle ver depolamak çn kullanılmaktadır . Anahtarlar , benzersz ve değşmez olmalıdır . Sözlükler ,
verler hızlı br şeklde arama ve erşm yapmak çn etkl br yapı sunar . Son olarak, kümeler ele alınmıştır . Kümeler ,
benzersz ve sırasız ver öğelern çeren yapılar olup, matematksel küme şlemler çn dealdr .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-


34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-


Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Hang Python ver yapısı brden fazla öğey sıralı br şeklde depolamak çn kullanılır?
(Çoktan Seçmel)
(A) Lsteler
(B) Demetler
(C) Sözlükler
(D) Kümeler
(E) Dzler
Cevap-1 :
Demetler
Soru-2 :
Python dlndek ver yapılarının temel amacı nedr?
(Çoktan Seçmel)
(A) Rastgele sayılar üretmek.
(B) Verler düzenlemek, saklamak ve şlemek.
(C) Programın hızını yavaşlatmak.
(D) Verler gzlemek.
(E) Ver yedeklemek.
Cevap-2 :
Verler düzenlemek, saklamak ve şlemek.


Soru-3 :
Aşağıdak Python kod parçasında hang ver yapısı kullanılmıştır?
(Çoktan Seçmel)
(A) Lsteler
(B) Demetler
(C) Sözlükler
(D) Kümeler
(E) Dzler
Cevap-3 :
Lsteler
Soru-4 :
Hang Python fonksyonu, br lstenn uzunluğunu döndürür?
(Çoktan Seçmel)
(A) length(lste)
(B) count(lste)
(C) len(lste)
(D) sze(lste)
(E) uzunluk(lste)
Cevap-4 :
len(lste)
Soru-5 :
Br lste çndek elemanlara nasıl ulaşılablr?
(Çoktan Seçmel)
(A) lstem(ndeks)
(B) lstem.ndeks
(C) lstem{ndeks}
(D) lstem.at
(E) lstem[ndeks]
Cevap-5 :
lstem[ndeks]
Soru-6 :


Hang Python kodu, br sözlüğün çndek br değer getrr?
(Çoktan Seçmel)
(A) szlk.get("anahtar")
(B) szlk[anahtar]
(C) szlk.value("anahtar")
(D) szlk.fnd("anahtar")
(E) szlk.fetch("anahtar")
Cevap-6 :
szlk[anahtar]
Soru-7 :
Python le aşağıdak gb a ve b adlı kümeler tanımlanıyor . Buna göre, a.df ference(b) çalıştırıldığında gerye ne
döndürülür?
(Çoktan Seçmel)
(A) {2,4,6,8}
(B) {1,3,5,7,12}
(C) {10}
(D) {1,2,3,4,5,6,7,8,10,12}
(E) {1,3,5,7,10,12}
Cevap-7 :
{2,4,6,8}
Soru-8 :
Br E lstes aşağıdak gb tanımlanıyor . Buna göre, E[3:8:1] çalıştırıldığında gerye ne döndürülür?
(Çoktan Seçmel)
(A) [22, 25, 28]
(B) [7, 10, 13, 16, 19]
(C) [10, 13, 16, 19, 22, 25]
(D) [10, 13, 16, 19, 22]
(E) [7, 10, 13, 16, 19, 22, 25, 28]
Cevap-8 :
[10, 13, 16, 19, 22]


Soru-9 :
Python le br A = [28, 15, 32, 86, 29, 30] lstes verlyor . Lstenn knc elemanı le ndeks numarası k olan elemanın
toplamı hang seçenekte doğru verlmştr?
(Çoktan Seçmel)
(A) 43
(B) 47
(C) 58
(D) 59
(E) 60
Cevap-9 :
47
Soru-10 :
Python le yalnızca “elf” smn çeren E adında br demet tanımlanmak stenyor . Aşağıdak tanımlamalardan hangs
doğrudur?
(Çoktan Seçmel)
(A) E = {“elf”}
(B) E = (“elf”)
(C) E = (“elf”,)
(D) E = {“elf”,}
(E) E = [“elf”]
Cevap-10 :
E = (“elf”,)


# 4. KOŞUL İFADELERİ


**Bölümle İlgl Özlü Söz**

Harka br programcı değlm; Ben sadece harka alışkanlıkları olan y br programcıyım.
Kent Beck , Yazılım Mühends

**Kazanımlar**

1. Gerçek hayattak br koşulun Python dl le kontrol edlmesn sağlar ve koşul doğruysa belrl kod bloklarını
çalıştırablr ve koşulun yanıtı doğruysa, belrl kodların yürütülmesn sağlayablr .
2.Gerçek hayattak br koşulun k farklı senaryoya göre Python dl le kontrol edlmesn sağlar , koşul doğruysa br kod
bloğunu, aks halde başka br kod bloğunu çalıştırablr .
3. Gerçek hayattak brden fazla koşulun Python dl le kontrol edlmesn sağlar ve bu koşullara bağlı olarak farklı kod
bloklarını çalıştırablr .
4. Br koşulun çnde başka br koşulun olması durumunu göz önünde bulundurarak uygun f-elf-else yapısını kurablr
ve çalıştırablr .
5. Dğer programlama dllernde belrl br değern farklı durumlarını kontrol etmek çn kullanılan swtch-case yapısının
Python versyonu match-case yapısını verlen gerçek hayat koşullarına göre uygun br şeklde oluşturablr ve
çalıştırablr .

**Brlkte Düşünelm**

1. Br kullanıcıdan alınan br sayının poztf m, negatf m yoksa sıfır mı olduğu nasıl kontrol edleblr?
2. Br onlne alışverş platformunda, br kullanıcının sepetndek ürünlern toplam fyatına göre ndrmler nasıl
uygulanablr?
3. Br öğrencnn sınav notunu alıp, not aralığına göre harf notunu hesaplayan br program nasıl oluşturulablr?
4. Br restoran menüsünde, kullanıcının seçtğ yemeğn yanında ekstra malzemeler veya seçenekler kontrol etmek çn
ç çe geçmş f yapısı nasıl kullanablr?
5. Br renk seçc programı tasarlanması stenyor . Kullanıcının grdğ reng alıp, hang renk RGB kodunun
döndürüleceğne lşkn (10 adet renk seçeneğ kullanılablr) programda match-case yapısı nasıl kullanılablr?

**Başlamadan Önce**

Bu bölümde, programlamanın temel yapı taşlarından br olan koşullu fadeler ve karar yapılarının Python programlama
dl le nasıl kullanıldığı gösterlmektedr . Koşullu fadeler , programların belrl koşullara nasıl tepk vereceğn ve farklı
senaryolara nasıl yönlendrleceğn belrlemek çn kullanılır . Gerçek hayattak karar verme bçmnn programlamada
nasıl yapıldığına lşkn detaylı açıklamalar yer almaktadır . Ktabın bu bölümünde, bast "f" fadesnn nasıl
kullanılacağını, "f-else" ve "f-elf-else" fadelernn nasıl daha karmaşık senaryolar ele aldığını, ç çe geçmş ( nested )
"f" fadelernn nasıl kullanılableceğn ve Python programlama dlnde yer alan "match-case" yapısının nasıl etkl br
şeklde kullanılableceğ gösterlmektedr . Her br konu başlığı, gerçek dünya uygulamaları ve örneklerle desteklenerek,
okuyucuların koşullu fadelern ve karar yapılarının fonksyonunu ve gücünü anlamalarına yardımcı olacaktır .

## 4.1. f-elf-else Koşul İfadeler

Tıpkı gündelk hayatta olduğu gb programlamada da karar vermey gerektrecek durumlar ve buna bağlı brtakım
şlemlern gerçekleştrlmesne htyaç duyulmaktadır . Programlamada karar vermek denldğnde akla koşul fadeler
(condtonal statements ) ve elbette f-fades gelmektedr . Bu bölümde f koşul fades en temelden en karmaşığa doğru
adım adım anlatılmıştır .


Örneğn; k sayıdan büyük olanın bulunması stensn. Aşağıdak kod bloğunda; çerde tanımlanan x değşken le
kullanıcıdan alınan y değşken f le kontrol edlmektedr . Eğer x, y’ye eştse konsola “İk değşken brbrne eşttr .”
yazdırılır . f cümlesnn yazım bçm en bast hal le aşağıda verldğ şekldedr . f anahtar kelmesnden sonra
karşılaştırma fades yer almaktadır ve ardından : şaret konur . Buradan alt satıra geçldğnde grnt verlr , daha çten
başlanır . Kodların düzgün çalışması çn grntler e dkkat edlmes çok önemldr . f-den sonra gelen mantıksal
fadenn doğru (T rue) olması durumunda Consol’a “x eşttr y” yazdırılacaktır .
Verlen f fades tek satırda aşağıdak bçmde gösterleblr ( short-hand f ).
f’den sonra sadece tek br koşul gelebleceğ gb, and, or gb mantıksal operatörler kullanılarak brbrne bağlanmış olan
brleşk (compound ) br koşul fades  de yer alablr . Bu durumda brleşk koşul fadesnden dönen nha sonuç göz
önünde bulundurulacaktır . Örneğn aşağıda x==y , x>0 ve y>0 gb üç farklı koşul and operatörü le bağlanmıştır . Yan lk
örnekte olduğu gb yalnızca x’n y’ye eşt olması yetmez. Bu örnekte f koşuluna at bloğun çalıştırılablmes çn
(konsola “İk değşken brbrne eşt ve poztftr .” yazdırılması çn) x, y’ye eşt olmalı ve x sıfırdan büyük olmalı ve y
sıfırdan büyük olmalıdır . and le bağlanan brleşk br koşuldan elde edlecek nha sonucun True döndürülmes çn üç
koşul sonucunun da ayrı ayrı True olması gerekldr . Dğer tüm durumlarda konsola herhang br şey yazdırılmayacaktır .
Ayrıca yne f-den sonra sadece tek br kod satırı yer almak zorunda değldr . Peş peşe brden fazla şlemn
gerçekleştrlmes de mümkündür; ancak bu şlemler sıralanırken grntye dkkat edlmeldr . Eğer f bloğunda brden
fazla şlem gerçekleştrlecekse, f-den sonrak tüm komut satırlarının aynı hzada olması gerekr . Örneğn; aşağıda
kullanıcının 25 grmes durumunda, öncelkle x ve y toplanır ve z değşkenne atanır , ardından konsola “İk değşken
brbrne eşttr .” yazdırılır ve son olarak alt satıra “T oplam= 50” bçmnde z değşkennn değer yazdırılır .
Bu noktaya kadar verlen örneklerde ancak f-den sonra gelen koşulun True olması durumunda ne yapılacağına dar
komutlar verlmştr . Oysa, program çnde f koşulunun sağlanmadığı dğer durumlar çn geçerl şlem ya da şlemlern
de tanımlanması gerekeblr . Bu durumda else anahtar kelmes kullanılır .
Aşağıda verlen kod bloğunda amaç verlen k sayıdan büyük sayının ekrana yazdırılmasıdır . Örnekte x ve y gb k
değşken tanımlanmıştır . Eğer x, y’den büyükse, f bloğu çndek prnt(), aks halde se else bloğu çndek prnt()
çalışacaktır . x ve y’nn verlen değerlerne göre konsola “100 50 den büyüktür .” yazdırılır . Eğer y’nn değer 150 yapılırsa
yen durumda konsola “100 küçük eşttr 150” yazdırılır .


Bu örnek aşağıdak bçmde de fade edleblr ( short-hand f-else ).
Verlen örnekte k sayıdan brnn dğerne göre büyük olma durumu ve aks durumu dkkate alınmıştır; ancak verlen
sayılar brbrne eşt olablr ve bu durum çn de ek br kontrol fadesne htyaç duyulablr . Bu nedenle f ’de kontrol
edlen duruma lâveten farklı koşulların da kontrolü söz konusu se her br çn elf anahtar kelmes kullanılablr .
Aşağıdak örnekte x 10, y se 500 olarak tanımlanmıştır . Öncelkle x>y koşulu kontrol edlr , False ger
döndürüldüğünden elf ’te yer alan x<y koşulu kontrol edlr . True ger döndürüldüğünden konsola “x küçüktür y”
yazdırılır , else çalıştırılmaz.
Bazı durumlarda programcılar ç-çe f (nested f ) fadelernden yararlanmaktadır . Örneğn; aşağıda verlen örnekte eğer x,
20’den küçükse çtek f koşulunun kontrolü sağlanır .
Python dlnde koşul fadelernn temel kullanım türler şu şeklde özetleneblr:
f fadeler boş olamaz, ancak herhang br nedenle çerğ olmayan br f fades bulunuyorsa, hata almamak çn pass
fades kullanılablr . Buna göre aşağıdak kod bloğu ncelendğnde x’n sıfırdan küçük eşt olması durumunda hçbr
şlem yapılmayacaktır .
Programcıların C, C++ gb programlama dllerde aşna oldukları, belrl br değşken değernn br dz koşul tbar le
kontrol edldğ ve buna göre lgl şlemn gerçekleştrldğ swtch-case yapısının Python versyon 3.10’a kadar brebr
kullanımı mevcut değld. Versyon 3.10’dan sonra swtch-case benzer br yapı olan match-case tanıtılmıştır .


match-case, match anahtar kelmesyle başlatılır .match deym, br parametre almakta ve br blok oluşturmaktadır .
Ardından bu blokta match-te alınan parametreyle eşleşmes çn case anahtar sözcüğü le çeştl durumlar ncelenr . Alınan
parametrenn tanımlanan hçbr durumla eşleşmemes halnde "_" joker karakter çalıştırılacaktır . Bu nedenle, kodlama bu
durum göz önünde bulundurularak gerçekleştrlmeldr .
Örneğn; gun adında tanımlanan br değşkenn aldığı değere göre haftanın günlern döndüren kısa br Python programı
düşünülsün.
Yukarıda da belrtldğ üzere, örneğn gerçekleştrlmes çn Python 3.10 ve üzer br versyona sahp olunması
gerekmektedr . Bunun çn; (1) Bölüm 1.3’ te bağımsız kurulumunu gerçekleştrdğnz Python 3.1 1.4 konsolu
kullanılablr , (2) Bölüm 1.3.10’dak talmatlar gereğ Spyder ’dak Python ortamını 3.1 1.4 olacak şeklde değştrdkten
sonra Spyder ’da çalıştırılablr , ya da (3) Python 3.10 ve üzerne sahp farklı br edtörde çalıştırılablr .
gun adlı br değşken tanımlanır ve ardından bu değşken yalnızca 1 le 7 arasında sayı alableceğnden lgl durumlara
karşılık ekrana yazdırılacak olan çıktılar her br case-te tanımlanır . En sondak case-te gun değşkennn 1 le 7 arasındak
sayılardan farklı br değer alması durumunda kullanıcıya “Lütfen 1-7 arasında br sayı grnz.” şeklnde br uyarı mesajı
verlmes sağlanır .
Verlen lk ekran görüntüsünde gun değşken 5 değern almıştır , buna göre beklenen çıktı Cuma olarak elde edlmştr .
İknc ekran görüntüsünde se gun değşken karakter olarak 3 değern almıştır . case-lerde buna uygun br kontrol mevcut
olmadığından son case le belrlenen mesaj ekrana yazdırılmıştır . Eğer program kodunda, 3. case-te aşağıdakne benzer
br revzyon yapılırsa “Çarşamba” çıktısı elde edlecektr .


## 4.2. Koşul İfadeler le Örnekler

Bu bölümde, Bölüm 3.1.’de teork açıklamaları verlen koşul fadeler le lgl farklı örnekler verlmştr .
Örnek 1:  Klavyeden grlen lk sayının knc sayı le tam bölünüp bölünmeyeceğn kontrol eden, sayının bölünme ve
bölünmeme durumuna göre kullanıcıya blg mesajı döndüren Python programını yazınız.
Çözüm:  Örnek program yazılırken öncelkle klavyeden 2 sayı grlmes beklenmektedr . Bu, nput() fonksyonu le
sağlanır; ancak unutulmamalıdır k nput() fonksyonu gerye karakter ver tp döner . Dolayısıyla, grlen değer bastçe
tam sayı ver tpne döndürülmüştür . Ardından, f bloğunda öncelkle lk sayının knc sayıya bölümünden kalan sıfıra
eşt m? dye kontrol edlr . Eğer sıfırsa, yan lk sayı knc sayıya tam bölünüyorsa, program çıktısı tam bölünür mesajı
olacak, aks halde program çıktısı tam bölünmez mesajı olacaktır . İk farklı duruma lşkn durum ncelemelerne at ver
grş ve programın döndürdüğü sonuca aşağıda yer verlmştr .
Pek ya kullanıcı knc sayı olarak 0 grerse?


Görüldüğü gb sıfır le bölme hatası alınır . Bu nedenle; grlen knc sayının da (payda) kontrol edlmes ve sıfır olması
durumunda kullanıcıdan farklı br sayı grmes steneblr . Bu nedenle de program kodları şu şeklde yenleneblr .
Bu yen durumda, sayılar grldkten sonra s2 kontrol edlr . Eğer sıfırsa, program yenden çalıştırıldığında kullanıcıdan
farklı br sayı grmes stenr , aks halde programın çalışma prensb br öncek aşamada olduğu gb kalacaktır .
Örnek 2:  Değerler atanma esnasında verlen a, b, c adlı değşkenlerle br üçgen oluşturup oluşturulamayacağını
döndüren Python programını yazınız.
Çözüm Yolu: Üçgen oluşturma konusunda üçgen eştszlğ yardımcı olacaktır . Üçgen eştszlğne göre k kenarın
toplamı üçüncüden büyük olmalıdır .
Çözüm: Programın başında a, b, c değşkenlerne lk değer atamaları yapılmaktadır . Sonrasında ç-çe f yapısıyla a+b>c,
a+c>b, b+c>a durumları kontrol edlmş ve bu üç koşulun brlkte (üçgen eştszlğnn) sağlanması durumuna uygun
üçgen oluşturulacağı mesajı döndürülmüştür . Aks halde, yan üç koşuldan brnn ble sağlanamaması durumunda
üçgenn oluşturulamayacağına yönelk mesaj döndürülmüştür . Programda a, b, c değşkenlernn değerler sırasıyla 5, 5,
10 şeklnde tanımlandığından elde edlecek çıktı: 5 - 5 - 10 br üçgen oluşturmaz.  şeklnde olacaktır .
a, b, c = 5, 5, 5 şeklnde tanımlanırsa, programdan elde edlecek çıktı: 5 - 5 - 5 br üçgen oluşturur . olacaktır .
Aynı problemn çözümü çn farklı br çözüm yolu da kullanılablr . Koşulların ç-çe f le fade edlmes yerne and
bağlaçları le bağlanarak kontrolü de söz konusu olablr . İlgl Python kodu ve kod çalıştırıldığında elde edlen ekran
görüntüsü aşağıda verlmştr .


Elbette başlangıçta a, b ve c değşkenlern sıfırdan farklı olup olmadığının kontrolü de sağlanablr . Grlen sayılardan
hangsnn sıfırdan farklı olduğunu bulmak çn de basamaklı br kontrol şlem sağlanablr; ancak aşağıdak kod bloğu
da problemn çözümü çn yeterl olacaktır . Üçgen eştszlğ le lgl esas kontrol şlem, and bağlacıyla a, b ve c’nn
sıfırdan farklı olup olmadığının kontrol edldğ f bloğu altına alınmıştır .
Örnek 3:  Natonal Insttutes of Health’e göre verlen yaş aralıklarına göre grlen br yaşın kategorsn bulup, ekrana
yazdıran Python kodunu yazınız. Bu örnekte 140 yaş üst sınır olarak belrlenmştr . (Yaş aralıkları çn bknz.
https://www .nh.gov/nh-style-gude/age )
• Yendoğan + Bebek: 1 yıla kadar .
• Çocuklar: 1 yaşından 12 yaşına kadar .
• Ergenler: 13 la 17 yaş arası.
• Yetşknler: 18 yaş ve üstü.
• Yaşlı: 65 ve üzer.
Çözüm:  Program yazılırken öncelkle kullanıcıdan br yaş değer almakta başlanmıştır . Ardından kullanıcıya gösterlecek
yazı çn mesaj adlı br değşken kullanılmıştır . Sonrasında f-elf-else kullanılarak, örnek açıklamasında verlen her br
yaş kategors çn koşullar kontrol edlmştr . Aralıklar yazılırken unutulmaması gereken herhang br değern dışarıda
kalması ya da brden fazla duruma dâhl edlp edlmemesdr . Aralıklar and bağlacıyla oluşturulmuştur ve else-bloğunda
kategorler dışında grlecek br değer çn kullanıcıya gösterlecek çıktı değer belrlenmştr . f-elf-else’den sonra artık
prnt() fonksyonu kullanılarak mesaj değşkennn değer ekrana yazdırılmıştır . Dolayısıyla Python programı
çalıştırıldığında sonuçlar aşağıdak gb elde edlecektr:
• Yaş = 36 se program çıktısı: Yetşkn
• Yaş = -8 se program çıktısı: Lütfen uygun br yaş değer grnz.
• Yaş = 0.6 se program çıktısı: Yendoğan + Bebek
• Yaş = 290 se program çıktısı: Lütfen uygun br yaş değer grnz.


Örnek 4:  Br sstemn yönetc kullanıcı adı sys_admn , parolası yrjRttTk0=*?  olarak tanımlanıyor . Klavyeden grlen
kullanıcı adı ve şfre sstem yönetcs çn tanımlananlarla eşleşmes durumunda herhang br şlemn
gerçekleştrlmedğ, aks halde grlen blglerden hangsnn uyuşmadığı mesajının kullanıcıya döndürüldüğü Python
kodunu yazınız.
Çözüm:  Verlen Python programı sstem yönetcsnn kullanıcı adı ve şfresnn tanımlandığı satırlarla başlamaktadır . Bu
k blg strng olarak tutulmaktadır . Ardından nput() fonksyonu le kullanıcıdan kullanıcı adı ve şfre blgsn grş
yapması beklenmektedr . Bu noktada nput() fonksyonu da strng döndüreceğnden bu noktada herhang br ver tp
dönüşüne htyaç yoktur .
Programda lk beklenen kullanıcı adı ve şfrenn doğru grlmes durumunda herhang br şey şlemn
gerçekleştrlmemesdr . Bu durum f bloğunda kontrol edlmş, pass anahtar kelmesyle de herhang br şlem
gerçekleştrlmeden geçş yapılması sağlanmıştır . Ardından grlen blglerden hangsnn uyuşmadığı mesajının
kullanıcıya gösterlmes gerekmektedr . Bu nedenle; lk elf bloğunda kullanıcı adının doğru şfrenn yanlış olması, knc
elf bloğunda kullanıcı adının hatalı şfrenn doğru olması, son olarak else bloğunda se hem kullanıcı adı hem de şfrenn
hatalı olması durumu kontrolü gerçekleştrlmş ve gerekl hata mesajı kullanıcıya döndürülmüştür . Aşağıda farklı
durumlar çn elde edlen ekran görüntülerne yer verlmştr .


Örnek 5:  Br mağaza müşterlernn harcamalarına göre ndrm yapmayı planlıyor . İndrm çn alt sınır 500TL  olarak
belrlenmştr . 500-1800TL ’lk harcama aralığında %10’luk, 1800-6000TL ’lk harcama aralığında %30 ve 6000TL
üzerndek harcamalara se %50 ndrm yapılacaktır . Buna göre, toplam harcama mktarı grlen br müşternn ödeme
mktarını döndüren Python programını yazınız.
Çözüm: Programda, odemeMktar değşkennde müşternn normalde yapacağı ödeme mktarı tutulmaktadır . f-elf-else
bloğu le verlen aralıklar göz önünde bulundurularak müşternn yapacağı yen ödeme tutarı (sonFyat) belrlenmştr .
Müşter 500TL ’nn altında harcama yaptıysa herhang br ndrm uygulanmayacaktır . Çünkü ndrm alt sınırı 500TL ’dr.
Dolayısıyla sonFyat, odemeMktarna eşt olacaktır . İlk başta f bloğu kontrol edlmekte, verlen koşul sağlanmazsa br
sonrak elf bloğuna geçleceğ blnmektedr . Bu nedenle eğer lk elf bloğu çalışırsa odemeMktar çn artık 500TL ’nn
altında olmadığı anlaşılablr . Bu kez artık odemeMktarı 500-1800TL  aralığında olup olmadığı kontrol edlmektedr
anlamına gelr . Benzer mantık, sonrak elf blokları çn de geçerldr . else bloğunda 6000TL  ve üzer harcamalar çn
yapılan %50’lk ndrm uygulanacaktır . Program son olarak müşternn yapacağı ödeme mktarının ekrana
yazdırılmasıyla son bulmaktadır . 2500TL ’lk br harcama yapan müşter çn f çalışmaz, lk elf çalışmaz; ancak knc
elf bloğu çalıştırılacaktır . Unutulmamalıdır k; bu aşamadan sonra artık else-bloğunun kontrol edlmesne gerek yoktur ,
çünkü f-elf-else boyunca eğer br koşul sağlanmazsa dğerne, ardından dğerne ve ardından br sonrakne gdlerek
kontrol sağlanır . Bu nedenle de koşul sağlandıktan sonra, kendnden sonra gelen koşul(lar) kontrol edlmeyecektr .
Yapılması ger eken ödeme: 1750.0  çıktısı elde edlr . Müşternn harcaması (odemeMktar) 6500TL  se bu durumda
Yapılması ger eken ödeme: 3250.0  çıktısı elde edlr .
Örnek 6:
  brer reel sayı ve 
  olmak üzere,
  şeklnde verlen, 
  katsayıları kullanıcı
tarafından grlen knc dereceden br denklemn köklern bulan Python programını yazınız.
Çözüm yolu:
 knc dereceden verlen br denklemn dskrmnantı olarak tanımlanır ve denklemn kökler
hakkında blg verr:
• Eğer dskrmnant sıfırdan büyükse, denklemn k farklı reel kökü vardır .
• Eğer dskrmnant sıfıra eştse, denklemn reel kökler vardır ve brbrne eşttr .
• Eğer dskrmnant sıfırdan küçükse, bu defa da verlen denklemn kökler komplekstr ve brbrnden farklıdır .
Çözüm: Dğer örneklerden farklı olarak bu örnekte kök alma şlemne htyaç duyulduğundan bu şlem çn math
kütüphanesnde yer alan sqrt() fonksyonu kullanılmıştır . Bunun çn programın başında mport math le kütüphane
çalışmaya dâhl edlmştr . Bu dâhl etme şlemnn gerçekleştrldğ kod satırından sonra artık math kütüphanesnn
çnde yer alan fonksyonlar çalışma ortamında kullanılablr hale gelmştr .
Program çalıştırılırken lk üç kod satırında kullanıcıdan denklemn katsayıları alınır ve ardında reel sayı (float dönüşümü
yapılmıştır) olarak a, b ve c değşkenler tanımlanmış olur . Sonrasında, denklemn dskrmnantı delta hesaplanır .
Denklem knc dereceden br denklem olduğu çn a’nın sıfırdan farklı br değer alması gerekr . Bu nedenle öncelkle bu


durum kontrol edlr . Eğer sıfıra eşt se kullanıcının programı farklı br a değer kullanarak yenden çalıştırmaya
yönlendrlr; aks halde se denklem kökler le lgl koşullara geçlr .
Bu problemde dskrmnanta bağlı üç farklı koşul olduğundan, f-elf-else kullanılması uygundur . f bloğunda köklern
reel ve brbrnden farklı olma durumu, elf bloğunda köklern reel, brbrne eşt olma durumu ve son olarak else
bloğunda k farklı kompleks kök olma durumu ncelenr . Her br durumda, örneğn çözüm yolunda verlen kök
hesaplamaları gerçekleştrlr ve kullanıcıya blg mesajı verlr . Dkkat edlecek öneml br husus, else bloğundak
kompleks sayı gösterm bçmdr . Kompleks sayı oluşturucusunda vr gülden önceye reel, sonraya se sanal (majner)
kısım yazılmıştır . Sonuçta; Grlen denklemn k farklı r eel kökü var dır: -0.5 -2.0  elde edlr .
a, b, c = 2, 4, 2 olmak üzere elde edlecek çıktı: Grlen denklemn k farklı r eel kökü var dır ve bunlar brbrne eşttr:
-1.0 -1.0
a, b, c = 2, 4, 2 olmak üzere elde edlecek çıktı: Grlen denklemn k farklı kompleks kökü var dır:
(-0.25+0.37080992435478316j) (-0.25-0.37080992435478316j)
Örnek 7:  Br kar go frması çn kamet edlen aşağıdak şehrlere göre br kar gonun kaç günde teslm edlebleceğn
döndüren Python programını match-case kullanarak yazınız.
• İzmt, Sakarya, Yalova (1 ş günü)
• Muğla, Antalya, Alanya (2 ş günü)
Çözüm: Bu örnekte, verlen llere göre kar gonun hang lde ne zaman olacağı blgs letlmek stenmektedr . Başlangıçta,
kullanıcıdan l adı alınmaktadır . İl adı programda sehrAd olarak tutulmaktadır . match parametre olarak sehrAdnı
almaktadır . Bu doğrultuda her br case-te grlen şehr adına göre kar gonun teslmatına lşkn blglendrme mesajı
oluşturulmuştur . case-lerde kontrol edlen hçbr durum karşılanmadığında case _: çalıştırılacaktır . Aşağıda programa
farklı grdler verlmesyle elde edlen ekran görüntülerne yer verlmştr .


Pek ya klavyeden “Sakarya” yerne “SAKAR YA” grlrse?
Her ne kadar bzler çn “Sakarya” ve “SAKAR YA” aynı anlama gelse de blgsayar çn durum farklıdır! Sakarya şehr
çn teslmat tarh belrl olmasına rağmen, sank lstelenmeyen br şehr adıymış gb Üzgünüz, kar gonun belrtlen şehr e
teslmat tarh blnmemektedr . mesajı döndürülmüştür . Bu gb büyük-küçük harften kaynaklanablecek hataları ortadan
kaldırmak çn ya her farklı l yazımı kombnasyonu çn farklı br case oluşturulur -çok fazla kombnasyon olacağından
bu aslında hç de efektf olmayan br çözümdür - ya da Python kodu aşağıdak gb değştrleblr .


Kullanıcı şehr adını grdkten sonra, ne yazarsa yazsın grdğ metn.upper() le büyük harflere çevrlr ve sehrAd
değşkenne atanır . case-lerde de sadece büyük harfl şehr adı kontrolü sağlanır . Böylece hatalı br durumla karşı karşıya
kalınmaz.
Örnek 8: Bast br hesap maknes programı gelştrlecektr .Grlen operatöre (+, -, *, /) göre gerekl şlemn yapılmasını
sağlayan ve şlem sonucu ekrana yazdıran, belrlenen koşulların dışında br durum oluşursa “ Geçersz şlem veya sayı
grş. Lütfen tekrar deneynz. ” mesajını ekrana yazdıran Python programını match-case ve f yapılarını kullanarak
yazınız.
Çözüm:  Aşağıdak kod bloğunun lk satırında slem, s1 ve s2 değşkenlerne sırasıyla +, 20 ve 30 değerler atanmıştır .
Çözüm yolu toplama şlem üzernden anlatılacaktır . Programın farklı senaryolarının da nceleneblmes çn yorum satırı
olarak dört farklı kod satırı daha eklenmştr . Okuyucu, yorum satırını kaldırarak teker teker kod bloğunu çalıştırablr .
match yapısında slem değşkennn farklı durumları kontrol edlmektedr . İlk caseslem değşkennn + olması durumu
çn oluşturulmuştur . Bu durum çn, eğer s1 ve s2 nt ya da float se s1 ve s2’nn toplamı snc değşkenne atanacaktır ve
ardından ekrana 20 + 30 = 50 yazdırılacaktır . Dğer case’lerde de sırasıyla -, * ve / çn benzer kontrol şlemler
sağlanmıştır . Hatta / şlem çn lave olarak bölenn sıfırdan farklı olup olmadığı kontrol edlmştr . Eğer slem çn
case’lerde verlen hçbr fade sağlanmazsa ekrana “ Geçersz şlem veya sayı grş. Lütfen tekrar deneynz. ”
yazdırılacaktır .


Örnek 9: Br kşnn yaşına göre, oy kullanıp kullanamayacağı durumunu ekrana yazdıran Python programını short-hand
f-else  kullanarak yazınız.
Çözüm:  Programda short-hand f-else  kullanarak kşnn oy kullanma yaşının üzernde m (f tarafı), yoksa altında mı
(else tarafı) olduğu kontrol edlmektedr . İlk kod satırında yas değşken 55 değern almıştır . Bu nedenle yas >= 18
koşulu True döndüreceğnden durum değşken uygundur değern alır . Ardından prnt() fonksyonu yardımıyla Kş oy
vermek çn uygundur . ekrana yazdırılmaktadır .
Eğer yas değşken değernn klavyeden grlmes beklenrse program kodu aşağıdak bçmde revze edleblr .
Örnek 10:  Klavyeden grlen br sayının 1-100 arasında olup olmadığını kullanarak kontrol eden Python programını
short-hand f-else  kullanarak yazınız.
Çözüm:  Programa klavyeden grlecek sayının alınması le başlanmaktadır . Bunun çn br say değşken tanımlanır .
Ardından short-hand f-else  kullanarak br sayının 1-100 arasında olup olmadığı kontrol edlr . f bloğunda 1 <= say <=
100 gb brleşk br kontrol fades yazılmıştır . Eğer sayı 1-100 aralığında se durum değşken “ aralığındadır ” olarak,
belrlenen aralıkta değlse “ aralığında değldr ” şeklnde değer alır . Sonrasında prnt() çnde sayının durumu le lgl
blg ekrana yazdırılır .
Örnek 1 1: Klavyeden grlen boy (m) ve kloya (kg) göre hastanın Vücut Ktle İndeksn (VKİ) hesaplayan, aşağıda
verlen aralıkları kullanarak hastanın at olduğu kategory hesaplanan VKİ blgs le ekrana yazdıran Python programını
short-hand f-else  kullanarak yazınız.
Çözüm Yolu: Vücut Ktle İndeksn (VKİ) hesaplamak çn aşağıdak formül kullanılablr
(https://sbn.saglk.gov .tr/BKndeks.aspx ):
• 18.5 kg/m2’nn altında se zayıf
• 18.5-24.9 kg/m2 arasında se normal klolu
• 25-29.9 kg/m2 arasında se fazla klolu
• 30-34.9 kg/m2 arasında se I. Derece obez
• 35-39.9 kg/m2 arasında se II. Derece obez
• 40 kg/m2 üzernde se III. Derece morbd obez


Çözüm: Program kodu yazılmaya başlanırken öncelkle klavyeden grlmes gereken boy ve klo blgs kullanıcıdan
alınmaktadır . Bu değerler küsuratlı olableceğnden nput() fonksyonu yardımı le ger döndürülen değer float ver tpne
çevrlmştr . Ardından VKİ hesaplanmıştır (vk). Sonrasında, vkye göre hastanın hang kategorde olduğunun (durum)
belrlenmes çn kontrol şlemlerne başlanmıştır . Verlen aralıklara göre vk kontrolü çn f-elf-else yapısı kullanılmıştır .
Sonrasında se hastanın VKİ le VKİ’ye göre belrlenen durumu ekrana yazdırılmıştır . prnt() fonksyonu çnde
vkround() fonksyonu yardımıyla vr gülden sonra 2 basamak yuvarlanarak ekrana yazdırılmıştır .

**Bölüm Özet**

Bu bölümde, programlamanın yapı taşlarından br olan f koşul fadesne odaklanılmıştır . Koşul fadeler, belrl br
durumun doğru veya yanlış olmasına göre blgsayarın farklı kod bloklarının çalıştırılmasını sağlamaktadır . İlk olarak, f
yapısının en sade, tekl kullanımı ve nasıl çalıştığı açıklanmıştır . Ardından f-else, f-elf-else yapıları örneklerle
anlatılmıştır . Sonrasında, koşul fadelernn ç çe geçmş hal le match-case kullanımına yer verlmştr . Programlama
süreçlernde karar mekanzmalarının nasıl oluşturulacağını anlamak steyenler çn öneml br konu olup, kavramların
daha y anlaşılablmes çn konu örneklerle desteklenmştr .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.


GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html


Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :


Br hastanın kan şekernn (kanSeker) 70’den düşük olması durumunda “Uyarı !” mesajı döndürülmek stenyor . Bu
durum aşağıdak seçeneklern hangsnde uygun bçmde sağlanmaktadır .
(Çoktan Seçmel)
(A) f kanSeker<70= prnt("Uyarı !")
(B) f kanSeker<70: prnt("Uyarı !")
(C) f kanSeker>70: prnt("Uyarı !")
(D) elf kanSeker<70: prnt("Uyarı !")
(E) felse kanSeker<70: prnt("Uyarı !")
Cevap-1 :
f kanSeker<70: prnt("Uyarı !")
Soru-2 :
Br restoran sahb müşternn sparş verdğ yemeklern fyatlarını kontrol etmek styor . Eğer belrl br yemek çn
ödeme yapmadan önce bakye yeterszse, müşterye uygun br mesaj döndürülecektr . Aşağıdak seçeneklerden hangs bu
durumu en doğru şeklde ele alır?
(Çoktan Seçmel)
(A) 
(B) 
(C) 
(D) 
(E) 
Cevap-2 :
Soru-3 :


Aşağıda br öğrenc not hesaplama programı oluşturulmak, programda kullanıcının grdğ puanı alarak bu puana göre
hang harf notunu aldığı belrlenmek stenmştr .
Verlen kod bloğu başında puan = 75 değern alırsa, aşağıdak seçeneklerden hangs kullanıcıya döndürülür?
(Çoktan Seçmel)
(A) A
(B) B
(C) C
(D) D
(E) F
Cevap-3 :
C
Soru-4 :
Aşağıda verlen seçeneklerden hangs soruda verlen kod bloğu le aynı ş yapar?
(Çoktan Seçmel)
(A) 
(B) 
(C) 
(D) 
(E) 


Cevap-4 :
Soru-5 :
Br eğtm platformunda eğer kullanıcı tarafından grlen yaş 18 le 25 arasında se ve öğrencnn bldğ programlama dl
Python se lgl öğrencnn seçmel ders Makne Öğrenmes olarak yapılacaktır . Bunun çn f bloğuna aşağıdak
seçeneklerden hangsndek koşul grlmeldr?
(Çoktan Seçmel)
(A) 
(B) 
(C) 
(D) 
(E) 
Cevap-5 :
Soru-6 :
x, y, z = 20, "15", 25 verlyor . Buna göre aşağıdak kod bloğu çalıştırıldığında hang seçenek döndürülür?
(Çoktan Seçmel)
(A) 0
(B) 1
(C) 2
(D) 3
(E) 4


Cevap-6 :
2
Soru-7 :
Aşağıda seçeneklerden hangsnde verlen kod bloğunun yaptığı ş en y bçmde açıklanmıştır?
(Çoktan Seçmel)
(A) Kullanıcının 1 le 7 arasında grdğ sayılara göre lgl sayının hafta ç m yoksa hafta sonu br günü mü temsl ettğ
blgsn vermektedr . 1-7 aralığı dışında br değer grlrse uyarı mesajı döndürülmektedr .
(B) Kullanıcının grdğ sayıya göre [1,2,3,4,5] ve [6,7] gb k farklı lstey ekrana yazdıran programdır . 1-7 aralığı
dışında br değer grlrse uyarı mesajı döndürülmektedr .
(C) Verlen kod bloğu çalışmaz, çünkü nput() fonksyonundan ger metnsel fade döndürülür . Bu da match-case’ te
yapılan kontrol çn uygun olmaz.
(D) Kod bloğu çalıştırıldığında her durumda “Lütfen uygun br sayı değer grnz ve tekrar deneynz.” mesajı
döndürülür .
(E) match-case çnde f kullanılmayacağı çn kod bloğu çalışmaz.
Cevap-7 :
Kullanıcının 1 le 7 arasında grdğ sayılara göre lgl sayının hafta ç m yoksa hafta sonu br günü mü temsl ettğ
blgsn vermektedr . 1-7 aralığı dışında br değer grlrse uyarı mesajı döndürülmektedr .
Soru-8 :
Aşağıdak kod bloğu verlyor . Kullanıcının klavyeden grdğ değerlere lşkn ekran görüntüsü verlyor . Buna göre f
satırından tbaren kod bloğu çalıştırıldığında elde edlen sonuç çn hang seçenek doğru olur?
(Çoktan Seçmel)
(A) 2.3


(B) 230
(C) 2300
(D) 23000
(E) Hatalı grnt sebebyle hata mesajı döndürülür .
Cevap-8 :
Hatalı grnt sebebyle hata mesajı döndürülür .
Soru-9 :
Aşağıdak kod bloğu çalıştırıldığında seçeneklerden hangs döndürülür?
(Çoktan Seçmel)
(A) FLOA T
(B) <class 'float'>
(C) INTEGER
(D) <class 'nteger'>
(E) Kod bloğu çalışmaz.
Cevap-9 :
<class 'float'>
Soru-10 :
Aşağıdak kod bloğu çalıştırıldığında ekrana False yazdırılması çn soru şaretl yere aşağıdak seçeneklerden hangs
ekleneblr?
(Çoktan Seçmel)
(A) 0
(B) False
(C) 0 and 0
(D) 1


(E) False or False
Cevap-10 :
1


# 5. DÖNGÜLER


**Bölümle İlgl Özlü Söz**

Programlama kod yazarak öğrenlr .
Bran Kernghan , Blgsayar Programcısı

**Kazanımlar**

1. for ve whle döngülernn yapısı ve çalışma mantığını öğrenr , teratf şlem gerektren görevlerde bu k döngüden
hangsnn kullanımının daha yernde olacağına karar vereblr .
2. contnue ve break deymlern for ve whle döngüler uygun bçmde kullanablr .
3. for döngüsü le br lste elemanlarına nasıl ulaşacağını blr .
4. for döngüsü le enumerate() deymn kullanablr .
5. whle döngüsü le enumerate() deymn kullanablr .
6. İç çe for döngüsü kullanımını blr .
7. Bast problemler çözmek çn döngülern nasıl kullanılacağı örneklerle pekştrr .

**Brlkte Düşünelm**

1. for döngüsü ve whle döngüsü arasındak temel fark nedr? Hang durumlarda hang döngü yapısını terch etmek
mantıklı olablr?
2. Br lste çndek elemanları for döngüsü kullanarak nasıl ulaşılablr? Aynı şlem whle döngüsü kullanarak yapmak
mümkün müdür?
3. range fonksyonu nedr? Br dz sayıyı ardışık olarak üretmek neden bazen kullanışlı olablr?
4. Br sayının faktöryeln hesaplayan br program yazılmak stensn. Bu problemn çözümü çn hang döngü yapısı
kullanılablr? Neden?
5. Br kullanıcıdan poztf br tam sayı grmesn steyen ve kullanıcının bu koşul dışında br değer grmes durumunda
tekrar farklı br sayı grmesn steyen br program nasıl tasarlanır? Hang döngü yapısı kullanılablr?
6. Br döngü çnde “break” ve “contnue” fadeler nasıl kullanılır? Bu fadelern ne zaman ve neden kullanılması
mantıklı olablr?
7. 2x2'lk br matrsn elemanları matrs formun şekl korunarak yazdırılmak stenyor . Bunun çn hang formda br
döngü yapısı kullanılablr?
8. Br sayının asal olup olmadığını kontrol eden br program yazılmak stensn. Bu problemn çözümü çn hang tür
döngü yapısı terch edleblr? Çözüm çn nasıl br yol zleneblr?
9. Br kullanıcının stedğ sayıda yıldızla kare desen çzen br program nasıl tasarlanablr?
10. Hang tür problemlern çözümünde döngüler vazgeçlmezdr? Neden?

**Başlamadan Önce**

Bu bölüm, programlamanın yapı taşlarından br olan döngülern anlaşılmasını ve Python le etkl br şeklde
kullanılmasını sağlamayı amaçlar . Döngüler , teratf (tekrarlı) şlemler çn kodun daha verml ve dnamk hale
getrlmesne mkân tanır . for ve whle döngüler, bu bölümde ele alınan başlıca konular arasında yer almıştır . for
döngüsü, özellkle lste veya belrl sayı aralıklarının üzernde geznmek çn kullanılırken, whle döngüsü belrl br


koşulun sağlandığı sürece tekrarlanır . Döngülern çnde kontrolü sağlayan break ve contnue le döngü akışını
yönlendrmenn yöntemler de bu bölümde ncelenmştr . Ayrıca, karma örnekler aracılığıyla döngülern pratk
uygulamalarını görmek ve döngülern farklı senaryolardak kullanımını anlamak da mümkündür . Bu bölüm,
programlamaya grş yapan herkes çn teratf şlem gerektren durumları Python dln kullanarak kodlanma becerlern
güçlendrmeye fırsat sunar .

## 5.1. Pr ogramlamada Döngüler

Programın çalışırken geçen süres ve kullanılan değşkenlern bellekte kapladığı yer , programlamada dkkat edlen en
öneml unsurlardandır . Eğer ele alınan problem teratf/tekrarlı şlemler çermekte se, her defasında aynı ş yapan kod
satırlarının alt alta yazılması uygun olmayacaktır . Bu nedenle, programlamada tekrarlı şlemlern yapılablmes çn
döngüler  (loops ) kullanılmaktadır . Müşterlern aynı sütunda yer alan ad ve soyadlarını ayırarak farklı sütunlara
kaydedlmes, br lstede yer alan smlern yazdırılması, sayıların toplanması, çarpım tablosunun yazdırılması gb
görevler döngüler kullanılarak gerçekleştrleblr . Döngülern kullanımı, ortaya çıkacak hataların azaltılması ve
zamandan tasarruf anlamına da gelmektedr . Problemde ana şlem tek br defaya mahsus olmak üzere yazılır , ardından
aynı şlem brden fazla kere uygulanablr .
Programlarda yapılması gereken belrl sayıda şlemn olduğu veya şlenen/üretlen değerlern sayıldığı durumlarda br
sayaç/ döngü değşken  (counter ) kullanılır . Döngünün lk ynelemesne başlamadan önce döngü değşkenne lk
değerler atanır . Döngü koşulu (loop condton ), döngü gövdesnn yürütülüp yürütülmeyeceğn veya ne zaman
duracağını belrlemek çn her ynelemenn başında hesaplanan br bool ( True/False ) fadedr . Döngü gövdes (loop
body ), her tekrarda ver şlemek çn gerekl şlemlern gerçekleştrldğ döngünün temel kısmıdır . Döngü gövdesnde tek
satır kod olableceğ gb brden fazla satır da yer alablr . Döngünün tekrarlarını kontrol etmek çn döngü
değşkenlernde artırma/azaltma şlemler gerçekleştrlr . Bazı döngü yapılarında bu şlem otomatk bçmde
gerçekleştrlr .
Bu bölümde Python dlndek k temel döngü tp olan for ve whle le döngülerle sıkça kullanılan range, break, contnue,
enumerate, zp gb Python deymler ele alınmıştır .

## 5.2. for  Döngüsü

Python dlnde for döngüsünün temel söz dzm aşağıda bast br örnekle açıklanmıştır . Döngüye for anahtar kelmesnn
yazımı le başlanır . Ardından döngü değşken ve döngü aralığı blgs gelr . Python söz dzm gereğ grntye mutlaka
dkkat edlmeldr . Döngü çnde kalması stenen kod bloğu for ’dan daha çerde br şeklde yazılmalıdır . Zaten “Enter”
tuşu le alt satıra geçldğnde Python edtörü otomatk olarak bu grnty oluşturmaktadır . Bu örnekte, döngü aralığı
range() şlev le verlmştr . Döngü çalıştırıldığında 0 le 9 arasındak sayıları alt alta ekrana yazdırılmaktadır . Döngü
değşken/sayacı ’dr . range() şlevnn başlangıç değer varsayılan 0'dır ve yne varsayılan şeklde döngü 1’er 1’er
artırılır . Dolayısıyla, döngü değşken sırasıyla , 0 le parantez çnde yer alan 10 arasındak değerler alır , 10 dâhl
edlmez.
Eğer sayılar yan yana yazdırılmak stenrse prnt() fonksyonu çne end=” “ parametres eklenr .
Bu döngünün tek satır halnde yazılması da mümkündür . Netcede aynı ekran görüntüsü elde edlecektr .
range()’nbaşlangıç değern br parametre ekleyerek belrtmek mümkündür . range(5, 20), 5 le 20 arasındak değerler
anlamına gelr; ancak 20 harç tutulur . range() varsayılan olarak ortaya çıkan dzy 1 artırır; ancak üçüncü br parametre
ekleyerek artış değern belrtmek mümkündür . range(5, 20, 2), 5 le 20 arasındak değerler 2’şer artırılır anlamına gelr;
20 harç tutulur (V anderPlas, 2016d).


Döngü değşken her zaman artırılmak zorunda değldr . Km durumda azaltılarak da şlemler yapılablr , tıpkı aşağıdak
örnekte verldğ gb. Döngü değşken bu kez 20’den 0’a 5’er 5’e azalmaktadır . İterasyona 20 dâhl, 0 dâhl değldr .
Örnek: for le br lstenn çnde dolaşmak.
for döngüsü yalnızca range() le kullanılmak zorunda değldr . Örneğn; haftanın günlernn tutulduğu gunler adında br
lste olsun. Aşağıda verlen for döngüsünde döngü değşken gundür ve her br terasyonda n anahtar kelmes sırasıyla
gunler lstesnn elemanlarını alır .
Örnek: for le enumerate() kullanımı.
Br öncek örnekte, yalnızca lstedek elemanların kendsne erşm sağlanmıştır . Döngü değşken sırasıyla bu
değerlerden brn almıştır; ancak bazı durumlarda elemanın kends kadar ndeks değer de önemldr . Bunun çn
enumerate() kullanılır .
Örnek: for le break deym kullanımı.
break deym döngünün sonlandırılması/btrlmes yan döngüden çıkmak çn kullanılır . Yukarıdak örnekte yalnızca
hafta çndek günler yazdırılmak stenrse for bloğuna f-else koşul fades eklenr . Eğer gun=="Cmt" se döngüden
çıkılacaktır; aks halde gun döngü değşken değer ekrana yazdırılacaktır .
Örnek: for le contnue deym kullanımı.


contnue deym le döngünün mevcut döngü değşken çn çalışması atlanır ve br sonrak değer le devam edlr . Eğer
yukarıdak kod bloğunda break yerne contnue kullanılırsa bu kez  Cmt  harç haftanın günlernn tümü ekrana
yazılacaktır , çünkü gun=="Cmt" se döngü değşken br sonrak değer alacaktır ve mevcut terasyon yapılmayacaktır .
Örnek: for döngüsünü takben else deym kullanımı.
Br for döngüsünü takben kullanılan else anahtar sözcüğü, döngü bttğnde yürütülecek br kod bloğunu belrtmektedr .
Bu nedenle for döngüsünü takben kullanılan else deym, döngü çnde br koşul sağlanmadığında belrl br kod
bloğunun yürütülmes stendğ senaryolar çn yararlı olacaktır . Aşağıdak örnektek for bloğunda, saylar lstesndek
sayılar çnde say değşken değer 240 sırasıyla aranacaktır . 240 lstede yer almadığından, döngü sonunda ekrana Sayı
bulunamadı!  yazdırılacaktır . Eğer döngü break deym le sonlanırsa, else bloğu çalışmaz. Örneğn, say=24 se ekrana
yalnızca Sayı bulundu!  yazdırılacaktır .
Örnek:  İç çe for döngüsü kullanımı.
İsmler ve soyadların yer aldığı k lste tanımlanmakta, bu lsteler kullanılarak aynı ndekste yer alan ad ve soyadları
brleştrlmeye ve ekrana yazdırılmaya çalışılmaktadır . Her k lste üzernden de lerleme gerektğnden ç çe k farklı
for döngüsü kullanılmıştır . 'nn j’ye eşt olduğu durumda f bloğu çndek prnt() çalıştırılacaktır .
Örnek: for döngüsü le zp() kullanımı.
Verlen örnek ç çe for döngüsü yerne, tek br for döngüsünde brden fazla lste üzernde eş zamanlı tekrar yapmayı
sağlayan zp() kullanılarak da gerçekleştrleblr . Aşağıdak kod bloğu çalıştırıldığında da yukarıdakyle aynı sonuç elde
edlecektr .
Koşul fadelernde olduğu gb for döngüsü de boş geçlmez; ancak herhang br şlemn yapılmayacağı durumlarda pass
deym kullanılablr .


Örnek:  Tek satırlık for döngüsü le br lste oluşturma.
Aşağıdak kod satırında 0’dan 9’a kadar olan sayılardan oluşan lstem adında br lste oluşturulmuştur . Ardından lste
ekrana yazdırılmıştır .

## 5.3. whle Döngüsü

whle döngüsü for döngüsüne benzer şeklde C, C++, C# gb dğer programlama dllernde kullanılan br döngü çeşddr .
Döngünün kaç kere çalışacağının blnmedğ durumlarda whle döngüsü kullanılır . Temel söz dzm se for döngüsünden
farklılık gösterr . Aşağıda bast br örnekle whle söz dzm açıklanmaya çalışılmıştır . whle döngüsünde for ’da olduğu
gb döngü değşken döngü çnde otomatk olarak tanımlanmaz. Döngü öncesnde tanımlanması gerekr . Burada döngü
değşken sayac lk değer 0 olarak tanımlanmıştır . whle döngüsüne whle anahtar kelmes le başlanır ve ardından döngü
koşulu gelr . Bu koşul doğru olduğu müddetçe whle bloğu çnde kalan şlemler tekrar eder . Yan sayac değşkennn lk
değer sıfırdı. sayac < 10 fades doğru olduğu sürece döngü çalışmaya devam eder . for döngüsünde olduğu gb döngü
değşken otomatk olarak artırılmaz ya da azaltılmaz. Son satırda görüleceğ gb whle bloğu sonunda döngü değşkenne
stenen artırma/azaltma şlem uygulanır . Sayacın son değer 10’dur; döngü koşulu sağlanmadığından döngüden çıkılır .
sayac Ekrana Yazdırılan Değer
0 0
1 1
2 2
… …
9 9
10 -
Br başka örnekte de döngü değşkennn azaltılması durumu ele alınsın. Bu kez, sayac 9’dan başlatılmıştır . sayac
değşken sıfıra büyük ve eşt olduğu sürece döngü şlemler tekrar edlecektr . Genellkle döngü değşkennn
artırma/azaltma durumlarında sayac += 1 ve sayac -= 1 kısa yazımı terch edlr .


Örnek: whle le sonsuz döngü.
İlk örnekte whle döngüsünde, döngü değşken otomatk artırılmadığı/azaltılmadığından mutlaka döngü çnde amaca
göre değernn değştrlmes gerektğ fade edlmşt. Aks takdrde, döngü değşkennn değer hep lk atanan değer
olarak kalacağından döngü koşulu her zaman sağlanacaktır . Bu nedenle de döngü sonsuz döngüye grecektr . Aşağıda
böyle br duruma örnek verlmştr .
Örnek: whle döngüsü le contnue deym kullanımı.
Aşağıdak örnekte a adlı br sayı lstes verlyor . Amaç se whle döngüsü le tek sayıları ekrana yazdırablmektr . Döngü
değşken  sıfırdan başlatılmıştır . Döngü,  nds değernn a lstes uzunluğundan (8) küçük olduğu sürece devam
edecektr . whle döngüsü çnde tek ve çft sayıları ayırt edeblmek çn f-else yapısı kullanılmıştır . Buna göre; eğer a[]
(lk terasyonda 2, knc terasyonda 27, üçüncüde 35, …) 2’ye bölündüğünde sıfır kalıyorsa bu o sayının çft sayı
olduğunu gösterr . Bu nedenle f bloğu çnde sadece döngü değşken artırılır ve contnue deymnden faydalanılır . Bu
döngünün başa dönmesn sağlayacaktır . Eğer f koşulu sağlanmazsa, yan sayı tekse, bu durumda sayı ekrana
yazdırılacak, döngü değşken 1 artırılarak döngü başa dönmüş olacaktır . İşlemler =8 olana kadar sürdürülür .
Aynı problem çn farklı br çözüm de şu bçmde gelştrleblr . Döngüye grldğnde döngü değşken 1 artırılır .
Ardından lstenn başından başlamak adına a[-1] kontrol edlr . Çft sayı se döngü başa döner , tek sayı se a[-1] ekrana
yazdırılır ve döngü başa döner .  değşkennn son değer 8’dr .


Ekrana Yazdırılan Değer  a[-1]
1-
227
335
……
811
Örnek: whle döngüsü le break deym kullanımı.
Bu örnektek amaç, a lstes çnde çft sayıya denk geldğnde döngünün sonlandırılmasıdır . Döngü değşkennn
başlangıç değer sıfırdır . , a lstesnn uzunluğundan küçük olduğu sürece döngü devam ettrlecektr; ancak bu kez f
bloğundak koşulun sağlanması durumunda break deym mevcuttur . Bu da döngünün verlen döngü koşulundan daha
erken sonlandırılableceğn göstermektedr . Eğer a[] çftse, döngüden çıkılacaktır .
Ekrana Yazdırılan Değer  a[]
011
127
235
3-
Örnek: whle döngüsünü takben else deym kullanımı.
for döngüsündek lste çnde sayı bulma örneğ whle döngüsü çn uyarlanacak olursa, öncelkle br döngü değşken
(sayac) tanımlanacaktır . sayac, saylar lstes uzunluğundan (5) küçük olduğu sürece döngü çalışmaya devam eder; ancak
bu örnekte de break deym kullanıldığından döngü koşulun sağlanmasından önce de btrleblr .
240 sayısı, saylar lstes çnde aranmaktadır . Dolayısıyla, döngü çndek her br elemanın (saylar[sayac] lk terasyonda
10, kncde 25, üçüncüde 33, …) 240’a (say) eşt olup olmadığı kontrol edlmektedr . Eşt olduğunda saylar[sayac] ==
say, True br fade döndürür . Bu da ekrana Say bulundu!  yazdırılır ve döngü sonlandırılır; ancak lste baştan sona kontrol
edlrse f bloğundak koşulun hçbr zaman True döndürmeyeceğ ortadadır . Dolayısıyla sayac son değer olarak 5’ alır
ve döngü btrlr . Bundan sonra else bloğundak Sayı bulunamadı!  ekrana yazdırılır ve program sonlanır .

## 5.4. Döngülerle lgl Karma Örnekler

Bu bölümde, br öncek bölümde açıklanan for ve whle döngüler le lgl karma örneklere yer verlmştr .
Örnek 1:  1’den klavyeden grlen br n sayısına kadar olan (n dâhl) tüm sayıları toplamını bulan Python programını hem
for hem de whle döngüsü kullanarak yazınız.


Çözüm:  Klavyeden grlen sayı tamsayı (nt) ver tpne dönüştürülerek n değşkennde tutulmaktadır . Kullanıcıya 1’den
n’e kadar olan sayıların toplamı döndürüleceğnden toplam adında br değşken tanımlanmış ve lk değer sıfır olarak
belrlenmştr . for döngüsünden farklı olarak whle döngüsünde, döngü dışında br  döngü değşken tanımlanmıştır .
Döngü çnde döngü değşken değernn 1 artırılması çn lgl kod yazılmıştır ( += 1). Döngü boyunca döngü değşken
 sırasıyla 1, 2, …, n değerlern almaktadır . Döngünün her terasyonunda , toplam değşkenne eklenmektedr . Son
toplam değer ekrana yazdırılmaktadır .
Örnek 2:  Klavyeden grlen 5 sayının mutlak değern ekrana yazdıran Python programını for döngüsü kullanarak
yazınız.
Çözüm:  Sayıların mutlak değerlernn tutulması çn mutlak_deger lstes tanımlanmıştır . Br sayının mutlak değern
bulurken sayı (x) sıfırdan küçükse mutlak değer -x olarak bulunur; aks halde mutlak değer x olarak kalacaktır . Buna
stnaden, for döngüsü çnde f-else bloğu tanımlanmıştır . Her br terasyonda klavyeden grlen sayının mutlak değer
bulunacak ve mutlak_deger lstesne eklenecektr . Programın sonunda lste ekrana yazdırılmaktadır .
Çalışmada mutlak değer kontrolü klask yoldan gerçekleştrlmştr; ancak Python dlnde bu amaçla kullanılan abs()
fonksyonu bulunmaktadır . Yan program kodu aşağıdak gb yenden yazılablr .
Örnek 3:  Br A = [-5, 1, 10, 20, -90, -1 11, 9, -25] lstes verlyor . Lstedek sayıların şaretlern bulan ve ekrana lste
şeklnde yazdıran Python programını whle döngüsü kullanarak yazınız.


Çözüm: Öncelkle A lstes ve döngü değşken (sayac) tanımlanmıştır . Ardından bu lstede yer alan sayıların şaretlern
tutulması çn saretler lstes boş br şeklde tanımlanmıştır . whle döngüsünün çnde sayının şaretn short-hand-f
kullanılarak kontrol edlmektedr . Sayı sıfırdan küçükse “-“, aks halde “+” şaret saretler lstesne eklenmektedr .
Programın sonunda sayıların şaretler ekrana yazdırılmaktadır .
Örnek 4:  Br a sayısının faktöryeln bulan ve ekrana yazdıran Python programını for ve whle döngüsü kullanarak
yazınız.
Çözüm: Her k çözüm çn de br a sayısı ve ardından sayının faktoryelnn tutulacağı br a değşken ve faktoryel
değşken tanımlanmıştır . Br a sayısının faktöryel 1’den a’ya kadar (a dâhl) sayıların çarpımıdır . Döngü değşken for
ve whle döngülernde 1’den grlen a sayısına kadar tanımlıdır . faktoryel değşken her terasyonda br öncek değer le
’nn çarpımına eşt olacaktır . Döngüler tamamlandıktan sonra ekrana 720 yazdırılacaktır .
Faktoryel Değer (faktoryel)
11
22
36
424
5120
6720
Örnek 5:  Klavyeden poztf br sayı grlene kadar yen br sayı steyen ve bu sayının karesn döndüren Python
programını whle döngüsü kullanarak yazınız.
Çözüm: Programın başında nput() fonksyonu yardımıyla kullanıcının klavyeden br sayı grmes sağlanmakta ve grlen
sayı n değşkenne atanmaktadır . Eğer klavyeden sıfırdan büyük br sayı grlrse, whle döngüsüne grlmeyecektr; ancak


aks halde n<=0 olduğundan whle döngüsüne grlecektr ve bu koşul bozulmadan da döngüden çıkılmayacaktır . Grlen
sıfırdan büyük sayının kares sonuc değşkenne atanacak ve ekrana yazdırılacaktır .
Bu problemn çözümü çn for döngüsü le alternatf çözümler gelştrleblr; ancak sonuca whle döngüsü le olduğu
kadar etkn br bçmde ulaşılamayacaktır , çünkü for döngüsünde döngü değşken çn belrl br alt ve üst sınır
gerekmektedr . Oysa kullanıcının ne zaman sıfırdan büyük br sayı greceğ blnmemektedr . Bu nedenle de döngü
değşken çn belrl br üst sınır konamaz.
Örnek 6:  Aşağıda verlen şekl for döngüsü yardımı le ekrana yazdıran Python programını yazınız.
Çözüm: Soruda verlen ekran görüntüsünün oluşturulablmes çn satır ve sütun boyutunda düşünülmeldr; ancak bu tek
br for döngüsüyle değl, ç çe for döngüsü kullanılarak yazdırılablr .  döngü değşkennn yer aldığı for satır , j döngü
değşennn yer aldığı çtek for se sütun temelnde şlem yapacaktır . Yıldızların sırayla artmasını sağlayan j çn
tanımlanmış olan döngü değşkennn üst sınırıdır . Br satır şlem çte yer alan for döngüsü tarafından tamamlanır ,
ardından br sonrak satıra \r yardımıyla geçlr .
Örnek 7:  Aşağıda verlen şekl for döngüsü yardımı le ekrana yazdıran Python programını yazınız.
Çözüm: Br öncek örnekten farkı satır sayısı ve * yerne sayıların ekrana yazdırılmasıdır . Bunu sağlamak çn br öncek
örneğn Python kodu aşağıdak gb yenden yazılmıştır . Yazdırılan sayıların ardışık br bçmde lerlemes çn döngünün
başında lk değer 0 atanan say değşken tanımlanmıştır . Satır sayısı 4 olduğu çn dıştak for döngüsündek range(1,5)
olarak belrlenmştr . Buna lâveten, prnt() fonksyonunda * yern say değşkenne bırakmıştır .
Örnek 8:  Blgsayar tarafından 1-100 arasında tutulan br sayıyı “Aşağı!”, “Y ukarı!” şeklndek yönlendrmelerle
kullanıcının tahmn etmeye çalıştığı, sonunda kaç denemede hang sayının tahmn edldğn ekrana yazdıran Python
programını yazınız.


Çözüm: Bu örnekte, blgsayar tarafından 1-100 arasında br sayı tutulması planlandığından, programda bu şn rastgele
yapılması çn öncelkle random modülü eklenmektedr . random.randnt(1, 100) komutu le rastgele br sayı seçlr ve say
değşkenne atanır . Kullanıcı tahmnnn saklanması çn tahmn değşken tanımlanmıştır ve buna lk değer ataması
yapılmamıştır . Bunun yerne None olarak tanımlanmıştır . Son olarak kullanıcının deneme sayısının saklanması çn
deneme değşken başlangıç değer 0 olarak tanımlanmıştır . Program açılırken “ Sayı T ahmn Oyununa Hoşgeldnz!!!”
Karşılama cümlesyle başlamaktadır . Döngü çnde klavyeden kullanıcının tahmnn grmes sağlanır , deneme
değşkennn değer 1 artırılır . Eğer sayı tahmnden büyükse “ Aşağı ”, küçükse “ Yukarıı! ” yönlendrmes yapılır . Kullanıcı
tahmn le tutulan sayı brbrne eşt olduğunda hang sayının kaç denemede bulunduğuna lşkn mesaj ekrana
yazdırılacak, döngü, dolayısıyla program sonlandırılacaktır .

**Bölüm Özet**

Bu bölümde, programlamanın temel yapı taşlarından br olan döngüler Python dl le temel br perspektften ele
alınmıştır . Başlangıç olarak for döngüsü konseptne odaklanılarak, lste ver yapısı elemanları arasında etkl br şeklde
dolaşması örneklenmştr . Ardından, whle döngüsüyle koşullu teratf şlemlern nasıl gerçekleştrleceğ ayrıntılı br
şeklde açıklanmıştır . contnue, break, enumerate ve zp gb yardımcı deymlerle döngülern kullanımı daha da
zengnleştrlmştr . Ayrıca, sonsuz döngü kavramına da değnlmştr . Bölümde yer alan karma örnekler sayesnde
öğrenclern döngülern gerçek dünya uygulamalarını daha y anlamalarını sağlaması, problem çözme yeteneklern
gelştrmelerne yardımcı olması hedeflenmştr .

**Kaynakça**


Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.


Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.


VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Aşağıda verlen kod bloğu çalıştırıldığında aşağıdak seçeneklerden hangs döndürülür?
(Çoktan Seçmel)
(A) 22’den -2’ye kadar olan tüm çft sayılar ekrana alt alta yazdırılır (22 ve -2 dâhl).
(B) 22’den 2’ye kadar olan tüm çft sayılar ekrana alt alta yazdırılır (22 ve 2 dâhl).
(C) 22’den -2’ye kadar olan tüm çft sayılar ekrana yan yana yazdırılır (22 ve -2 dâhl).
(D) 22’den 2’ye kadar olan tüm çft sayılar ekrana yan yana yazdırılır (22 ve 2 dâhl).
(E) 22’den 4’e kadar olan tüm çft sayılar ekrana alt alta yazdırılır (22 ve 4 dâhl).
Cevap-1 :
22’den 4’e kadar olan tüm çft sayılar ekrana alt alta yazdırılır (22 ve 4 dâhl).
Soru-2 :
Aşağıdaklerden hangs 5 adet ondalıklı sayı ekrana yazdırır?
(Çoktan Seçmel)
(A) 
(B) 
(C) 


(D)
(E) 
Cevap-2 :
Soru-3 :
Aşağıdak seçeneklerden hangs verlen for kod satırı, whle kod bloğu le aynı çıktıyı döndürür?
(Çoktan Seçmel)
(A) for say n range(0,103,3): prnt(say)
(B) for say n range(-3,102,1): prnt(say)
(C) for say n range(-3,100,3): prnt(say)
(D) for say n range(3,100,-3): prnt(say)
(E) for say n range(0,103,1): prnt(say)
Cevap-3 :
for say n range(0,103,3): prnt(say)
Soru-4 :
Aşağıda smler adında br lste tanımlanıyor ve ardından for döngüsü kodları verlyor . Buna göre aşağıdak
seçeneklerden hangsnde for döngüsünün görev doğru br bçmde açıklanmıştır?
(Çoktan Seçmel)
(A) smler lstesnn lk elemanı kontrol edlr . Eğer “E”ye eştse lk eleman yazdırılmaz. Lstenn dğer tüm elemanları
alt alta yazdırılır .
(B) smler lstesnn lk elemanı kontrol edlr . Eğer “E”ye eştse döngüden çıkılır . Bu nedenle de ekrana herhang br şey
yazdırılmaz.
(C) smler lstesnn her elemanı kontrol edlr . Eğer lste elemanı “E”ye eştse yazdırılmaz. Lstenn dğer tüm elemanları
alt alta yazdırılır .


(D) smler lstesnn her elemanı kontrol edlr . Eğer lste elemanının lk harf “E”ye eştse yazdırılmaz. Lstenn dğer
tüm elemanları alt alta yazdırılır .
(E) smler lstesnn her elemanı kontrol edlr . Eğer lste elemanının lk harf “E”ye eştse döngüden çıkılır .
Cevap-4 :
smler lstesnn her elemanı kontrol edlr . Eğer lste elemanının lk harf “E”ye eştse yazdırılmaz. Lstenn dğer tüm
elemanları alt alta yazdırılır .
Soru-5 :
Aşağıda verlen kod bloğu çalıştırıldıktan sonra toplam değşkenn değer ne olur?
(Çoktan Seçmel)
(A) 15
(B) 25
(C) 40
(D) 75
(E) 175
Cevap-5 :
40
Soru-6 :
Aşağıda verlen Python kod bloğuna göre ekrana hang sayılar yazdırılır?
(Çoktan Seçmel)
(A) 10 20 30 80
(B) 20 30 80
(C) 55 45 101
(D) 55 45 101 6


(E) 10 55 45 101 6
Cevap-6 :
20 30 80
Soru-7 :
Aşağıdak şekln elde edleblmes çn kod bloğu aşağıdak seçeneklerden hangs le tamamlanmalıdır?
(Çoktan Seçmel)
(A) for j n range(,6):
(B) for j n range(1,6):
(C) for  n range(,6):
(D) for j n range(+1,6):
Cevap-7 :
for j n range(,6):
Soru-8 :
Aşağıdak ekran görüntüsünün elde edleblmes çn nokta le belrtlen boşluk aşağıdak seçeneklerden hangs le
tamamlanmalıdır?
(Çoktan Seçmel)
(A) sm, yas s lst(zp(a, b)):
(B) sm, yas n zp(lst(a, b)):
(C) sm, yas n lst(zp(a, b)):
(D) sm, yas enumerate(zp(a, b)):


(E) sm, yas zp(a, b):
Cevap-8 :
sm, yas n lst(zp(a, b)):
Soru-9 :
Aşağıdak ekran görüntüsünün elde edleblmes çn üç nokta le belrtlen boşluk aşağıdak seçeneklern hangs le
tamamlanmalıdır?
(Çoktan Seçmel)
(A) enumerate(a)
(B) enumerate()
(C) enumerate(j)
(D) enumerate(zp(a))
(E) zp(enumerate(a))
Cevap-9 :
enumerate(a)
Soru-10 :
Aşağıdaklerden hangs sonsuz döngü değldr?
(Çoktan Seçmel)
(A) 
(B) 
(C) 


(D)
(E) 
Cevap-10 :


# 6. FONKSİYONLAR


**Bölümle İlgl Özlü Söz**

Programlama, algortma tasarlama ve hatalı kodda hata ayıklama sanatıdır .
Ellen Ullman , Blgsayar Programcısı

**Kazanımlar**

1. Fonksyonların programlamadak rolünü ve fonksyonların kodun or ganzasyonunda ve tekrar kullanılablrlkte nasıl
yardımcı olduğunu anlar .
2. def anahtar kelmes kullanarak fonksyonlar oluşturablr .
3. Parametrelerle fonksyonları nasıl tanımlayacağını ve çağıracağını blr , br fonksyonun varsa dönüş değer(ler)n
kullanablr .
4. lambda fades le oluşturulan fonksyonların nasıl tanımlanıp kullanılacağını blr .
5. map() ve flter() gb Python dlnde yer alan sık kullanılan yardımcı fonksyonların nasıl kullanılacağını blr .
6. Fonksyonları kullanarak karmaşık şlemler nasıl gerçekleştreceğn blr .

**Brlkte Düşünelm**

1. Fonksyonlar programlama neden önemldr?
2. Br programın daha y or ganze edlmesne nasıl yardımcı olablrler?
3. Fonksyonların kullanımı, kodun daha okunablr hale gelmesne nasıl katkı sağlar?
4. Fonksyonların tekrar kullanılablrlğ hang tür programlar çn önemldr?
5. Python le br fonksyonu nasıl tanımlarsınız?
6. Parametrelern fonksyonlara eklenmesnn avantajları nelerdr?
7. Br fonksyon nasıl çağrılır ve çağrıldığında ne tür şlemler gerçekleştrr?
8. Br fonksyonun dönüş değer nedr ve neden önemldr?
9. lambda fonksyonları nedr ve hang durumlarda kullanılır?
10. lambda fadesyle bast br fonksyon tanımlayablr msnz?
11. map() ve flter() fonksyonlarının kullanımına lşkn brer örnek vereblr msnz?

**Başlamadan Önce**

Bu bölümde yne programlamada öneml br yere sahp olan fonksyonların temel yapısı ve Python programlamadak
rolü fade edlmektedr . Bu bölüm fonksyonların etkl br şeklde kullanmanın temeln atmaya yardımcı olur .
Fonksyonlar , programlamada yazılan kodun or ganzasyonunu gelştrmek, kodu daha anlaşılır hale getrmek ve tekrar
kullanılablrlğ artırmak çn güçlü br araçtır . Bu bölüm, temel blglern yanı sıra def fades le fonksyon tanımlama,
lambda fonksyonları, map() ve flter() gb bazı yardımcı fonksyonlar ve en sonunda farklı karma örnekler çerr . Hem
programlamadak hem de Python dlndek bu öneml araçları kavramak, kod yazma becerlernn öneml ölçüde
gelşmesn de sağlayacaktır .

## 6.1. Pr ogramlamada Fonksyonlar


Programlamanın temel yapı taşlarından br de fonksyonlardır . Elbette sadece Python değl dğer programlama dllernde
de programcılar tarafından sıkça kullanılmaktadır . Br fonksyon  (functon , alt pr ogram, yor dam, pr osedür  ya da metot ),
“br ana pr ogram ya da alt pr ogram tarafından çağrılan ve kend çnde br bütün oluşturan (yan belrl br ş yapan)
program parçacığıdır ” şeklnde tanımlanır (Çobanoğlu, 2021). Br öncek bölümde ele alınan döngü kavramı nasıl k
belrl br şn tekrarı söz konusu olduğunda teratf şleme mkân tanıyarak avantaj sağlıyorsa, fonksyonların da öneml
faydaları bulunmaktadır . Tanımdan hareketle bunlardan lknn modülerlk olduğu söyleneblr . Fonksyonların kend
çnde br bütünlük oluşturması, aynı ya da farklı kod dosyaları (programlar) çnde farklı tek br yer ya da farklı brçok
yerden çağrılablmelerne zn verr . Böyle br yapı le çalışmak hem programın daha anlaşılır olmasını sağlar hem de
program çndek br hatanın daha kolay bulunmasını ve düzeltleblmesne olanak tanır .
Fonksyonlar terche göre grd alablen ve değer döndüreblen yapılardır . Fonksyonların grd değşkenlerne parametr e
(parameter ), parametrel br fonksyon çağrılırken gönderlen değerlere se argüman  (argument ) adı verlmektedr . Değer
döndüren fonksyonlarda return anahtar kelmes kullanılır .
Python dlnde standart ya da ek kütüphanelern çnde kullanıma sunulan brçok hazır fonksyon ( bullt-n functons )
bulunmaktadır . Örneğn; sum(), abs(), mn(), max(), vb. Ayrıca, kullanıcıların da kend fonksyonlarını tanımlamalarına
zn verlmektedr . Fonksyonlarla çalışılırken unutulmaması gereken en öneml özellk, fonksyon tanımının hyerarşk
yapıda fonksyonun çağırıldığı yerden önce yapılmasıdır . Python dl le kullanıcı tanımlı fonksyonlar  (user defned
functons ) k temel yolla oluşturulablmektedr . Bunlardan lk def deymnn kullanımı kncs se lambda fonksyonu
şeklnde tanımlamadır .

## 6.2. def le Fonksyon Tanımlama

def anahtar kelmes kullanılarak tanımlanan fonksyonların genel yapısı aşağıdak gbdr . Fonksyon tanımına def
deym le başlanır . Ardından fonksyon amacına uygun belrlenen br fonksyon adı yazılır . Eğer fonksyon grd
alacaksa, fonksyon adını fonksyon parametres ya da parametreler zler . Alt satıra geçldğnde bu blok artık fonksyon
gövdesdr . Yne fonksyon amacına göre uygun şlemler burada sıralanır . Fonksyonun gerye belrl br değer ya da
değerler döndürmes planlanmışsa, fonksyon gövdesnn en sonunda return le bu sağlanır .
Aşağıda ekrana “ Merhaba ” yazdıran br fonksyon tanımlanmıştır . Fonksyon adı selamV er’dr. Fonksyon herhang br
parametre almamakta ve herhang br değer döndürmemektedr .
İlgl kod bloğu çalıştırıldığında, Console-da yazdırılan herhang br şey olmadığı fark edlecektr . Bunun neden üsttek
kod satırları le yalnızca fonksyonun tanımlanmış olmasıdır . Oysa, fonksyonun çalışması çn bu yeterl değldr .
Fonksyonun tanımlanmasından sonra görevn yerne getrmes çn çağrılması gerekmektedr . Herhang br parametre
almayan fonksyon aşağıdak gb çağrılablr ve ardından ekrana Merhaba!  yazdırıldığı görülecektr .
Eğer klavyeden grlen sme göre Merhaba! yazdırılmak stenrse bu defa fonksyonun sm parametre olarak alması
yernde olacaktır . Aşağıda fonksyon adından sonra yuvarlak parantezler arasına sm adında br parametre eklenr .
Fonksyon br öncekndek gb 
  şeklnde çağrılırsa hata alınacaktır , çünkü bu fonksyonun br
adet parametres vardır ve çağrılırken br değer almalıdır .


Bu hatanın gderleblmes çn sm parametresne değer grlmeldr . Aşağıda verlen her k kod satırı da fonksyonun
doğru br şeklde çalışmasını sağlayacaktır . Fonksyonun brden fazla parametre alması durumunda grlen ar gümanların
karışmaması adına lk kullanım terch edleblr .
Br fonksyonun brden fazla parametre alması durumunda da (eğer yalnızca sm değl, fonksyona soysm de parametre
olarak verlrse) aşağıdak örnekte olduğu gb Python edtörü parametrelern neler olduğunu programcıya gösterecektr .
Aşağıda verlen her k kod satırı da aynı çıktıyı döndürecektr .
Bu noktaya kadar parametre alan ve almayan fonksyon örnekler ele alınmıştır; ancak br fonksyonun br ya da daha
fazla döndürdüğü değer olablr . Bu konunun anlaşılması adına k sayıyı parametre olarak alan (say1, say2) ve k
sayının toplam değern (say1+say2) döndüren br toplam fonksyonu aşağıdak gb tanımlansın. toplam(3, 5) şeklnde
fonksyonu çağırdıktan sonra, Console-da k sayının toplamının 8 olarak yazdırıldığı görüleblr . Ayrıca, fonksyonun
döndürdüğü değer farklı br değşkene (sonuc) de atanablr .
Demetler anlatılırken, demetlern br fonksyonun ger döndürdüğü değerlern ver yapısı olarak kullanılmakta olduğu
söylenmşt. Eğer yukarıdak fonksyonun, k sayının hem toplamını hem de farkını döndürmes stenrse dönüş ver
yapısı olarak demet kullanılablr . Eğer fonksyonun döndürdüğü değer sonuc gb tek br değşkene atanırsa, sonucun
demet olduğu görüleblr . Eğer br fonksyonun kaç adet değer döndürdüğü blnyorsa fonksyonun ger dönüş değerler
ayrı ayrı da karşılanablr , tıpkı sonuc_toplam ve sonuc_fark değşkenlernde olduğu gb.


Aşağıda belrl sayıda çft sayının döndürülmesn sağlayan br fonksyon tanımlanmıştır . Örneğn; cftSaylarGetr(10)
çalıştırıldığında 10 adet çft sayı döndürülecektr , yan ekrana [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] yazdırılacaktır . Fonksyona
saylar adında boş br lste tanımı le başlanmıştır . Ardından çft sayıların başlatılacağı nokta çn bas değşken
tanımlanmıştır . Ardından whle döngüsünde sayıların tek/çft kontrolü yapılarak saylar lstesne teker teker atanması
sağlanmıştır . Fonksyonda stenen n adet çft sayının döndürülmes olduğundan saylar lstesnn uzunluğu n’e eşt
olduğunda (len(saylar) = n) döngüden çıkılacaktır . Fonksyon saylar lstesnn döndürülmesyle sonlandırılır .
Genellkle br fonksyon tanımlanırken, fonksyonun çoğu zaman kullanmasını stedğmz belrl değerler mevcuttur;
ancak bu noktada kullanıcıya braz esneklk de tanınablr . Bu gb durumlarda, bağımsız değşkenler çn varsayılan
değerler kullanablr (V anderPlas, 2016c). Br öncek örnekte kullanıcının çft sayıların başlangıç değern stedğ gb
değştreblmesne zn verlmes çn fonksyon aşağıdak gb yenleneblr . Fonksyon hala cftSaylarGetr(5) çn
çalışacaktır; ancak kullanıcı çft sayıların başlangıç değern belrlemek sterse bunun çn kullanıcının fonksyonun
varsayılan değern 0 kabul ettğ bas parametresne değer ataması gerekecektr: cftSaylarGetr(5, 20)

## 6.3. lambda Fonksyonu


Lambda anahtar kelmes kullanılarak tek satırlık fonksyonlar yazılablr .
Örneğn; br öncek bölümde k sayının toplamını döndüren fonksyon lambda fonksyonu olarak aşağıdak şeklde fade
edleblr . Fonksyon çağrıldıktan sonra Consoleda 210 yazdırılacaktır .
Aşağıda se verlen sayının 10 katını döndüren lambda fonksyonu tanımlanmıştır . Fonksyonun adı kat_10’dur . Ardından
lambda anahtar kelmes kullanılmıştır . Fonksyon yalnızca a parametresn almakta ve ger anın 10 katını
döndürmektedr .
Br sayının tek olup olmadığını boolean değer olarak döndüren lambda fonksyonu se aşağıdak gb tanımlanmıştır .
Fonksyonda, sayının tek olup olmadığı short-hand-f  kullanımı le gerçekleştrlmştr . tek_m fonksyonundan a sayısı
tek se True, çftse False döndürülmektedr .

## 6.4. Bazı Yardımcı Fonksyonlar

map() fonksyonu, lste, dz gb br grup verye belrl br fonksyonun uygulanmasını ve elde edlen sonucun
döndürülmesn sağlar . flter() fonksyonu se lste, dz gb br grup verye uygulandığında br fonksyon le tanımlanan
koşulun True döndürüldüğü değerlern ger döndürülmesn sağlar (Çobanoğlu, 2021). Bu k öneml fonksyonun daha
y anlaşılablmes çn aşağıdak kod bloğunda br A lstes tanımlanarak map() ve flter() fonksyouna lşkn farklı
örneklere yer verlmştr . İlknde br öncek bölümde tanımlanan kat_10lambda fonksyonu kullanılmıştır . Bu fonksyon
A’nın elemanlarına map() yardımıyla uygulanmıştır . Bu şlemn sonucunda gerye dönen sonuçlar lsteye çevrlerek
ekrana yazdırılmıştır . İknc örnekte se yne br öncek bölümde tanımlanan tek_m fonksyonu kullanılmıştır . flter()
fonksyonu le A lstesnde fltreleme şlem gerçekleştrlmş, br dğer fade le A lstesnn çnden tek_m fonksyonu
koşullarını sağlayan elemanlar çeklmş ve ardından map() fonksyonundakne benzer şeklde lsteye çevrlerek ekrana
yazdırılmıştır .


## 6.5. Karma Örnekler

Bu bölümde, fonksyonlar le lgl örnek problemlere, açıklamalarına ve ekran görüntülerne yer verlmştr .
Örnek 1:  Br sayının asal olup olmadığı blgsn boolean ver tp olarak ger döndüren Python fonksyonunu yazınız.
Çözüm: En küçük asal sayı 2’dr . Eğer br sayının 1’den ve kendsnden başka bölen yoksa sayı asaldır . Bu blg
doğrultusunda, asal_m adında br fonksyon tanımlanmıştır . Fonksyon, asal olup olmadığı kontrol edlecek br sayıyı
(say) parametre olarak almaktadır . Ardından bu sayının 2’den küçük olup olmadığı kontrol edlr . Eğer grlen sayı 2’den
küçükse sayı asal değldr , bu nedenle de False döndürülür . Aks durum çn; 2’den başlayıp (say-1)’e kadar olan tüm
sayılar çnde say-y tam bölen br  olup olmadığına bakılır . Eğer böyle br  bölen varsa, sayı asal değldr demektr ,
False döndürülür . Aks halde, sayı asaldır , True döndürülür . Fonksyon; 5, 2, 221 ve 10 çn çalıştırıldığında sırasıyla True,
True, False, False döndürülecektr .
Örnek 2:  Verlen k sayının yern değştrerek değerler döndüren Python fonksyonunu yazınız.
Çözüm: x1 ve x2 gb k sayı tanımlansın. Tanımlanacak fonksyon adı degstr olarak belrlenmş olup, fonksyonun n1
ve n2 şeklnde k adet parametres bulunmaktadır . Fonksyon gövdesnde y adında geçc br değşkene n1, n1’e n2 ve
ardından y değer n2’ye atanır . Yen değerler br demet yapısında kullanıcıya döndürülür .
Örnek 3:  Verlen br metnn tersn döndüren Python fonksyonunu yazınız.


Çözüm: Metn tersne çevrecek olan programın adı tersCevr olarak belrlenmştr . Fonksyonun metn adında br
parametres bulunmaktadır . Fonksyon çnde öncelkle metnn tersn tutacak olan ters adında br strng değşken
tanımlanmıştır . Ardından for döngüsü metn değşkennn sonundan başlayarak lk karaktere kadar ters değşkenne
eklenmektedr . Sonunda, ters değşken döndürülmektedr . Fonksyonun farklı değerlerle çalıştırılmasından elde edlen
ekran görüntüsü aşağıda yer almaktadır .
Örnek 4:  Verlen br metnn çndek sesl harf sayısını döndüren Python fonksyonunu yazınız.
Çözüm: Verlen br metnn çndek sesl harf sayısını bulan programın adı seslHarfSays olarak belrlenmştr .
Fonksyon metn adında br parametre almaktadır . Fonksyon gövdesnde büyük ve küçük harflerden oluşan br
seslHarfler strng değşken tanımlanmıştır . Strng fade de karakterlere dar br çeşt taşıyıcı yapı, br koleksyondur .
Sesl harflern sayısını tutmak çn lk değer 0 olan say adında br değşken tanımlanmıştır . for döngüsünde metnn
çnde yer alan her br harfn sesl harfler (seslHarfler) arasında yer alıp almadığı kontrol edlmektedr . Eğer sesl
harflern çnde yer alıyorsa say değşken 1 artırılacaktır . Döngü sona erdğnde say döndürülecektr . Fonksyona k
farklı örnek metn verlmş ve sonuçların yer aldığı ekran görüntüler paylaşılmıştır .
Örnek 5:  Verlen br metnde tekrar eden karakterler kaldırarak metn yen haln ger döndüren Python fonksyonunu
yazınız.
Çözüm: Verlen br metnde tekrar eden karakterler kaldırarak metn yen haln ger döndürecek fonksyon adı
tekrarlar_kaldr olarak belrlenmştr . Fonksyon metn adında br parametre almaktadır . Ardından fonksyon gövdes
fonksyondan döndürülecek yen metnn tutulacağı değşkenn (yen_metn) tanımlanması le başlamaktadır . for döngüsü
boyunca parametre olarak grlen metnn karakterler kontrol edlr ve daha önce hç karşılaşılmayanlar yen_metn
değşkenne eklenr . Döngü tamamlandığında yen_metn fonksyon tarafından döndürülür . Aşağıdak kod bloğunun
sonunda fonksyon kullanımına lşkn br örnek verlmştr .


Örnek 6:  İk kenarı verlen br dkdörtgenn çevre ve alanını döndüren Python fonksyonunu def ve lambda le yazınız.
Çözüm:  Çevre ve alan hesabı yapacak fonksyon def kullanılarak tanımlanırken, fonksyon parametre olarak kenar
uzunluklarını tutacak olan a ve b parametrelern almıştır . return çnde dkdörtgenn çevres ve alanı sırasıyla
hesaplanarak ger döndürülmektedr . Benzer br tanımlama lambda kullanılarak da yapılablmektedr . Her k fonksyon
da aynı değerler döndürmektedr .
Örnek 7:  Grlen sayı kadar Fbonacc sers elemanını döndüren Python fonksyonunu yazınız.
Çözüm:  Fbonacc sers lk k elemanı 0 ve 1 olmak üzere, sernn br elemanı kendnden önce gelen k elemanın
toplamı şeklnde hesaplanmaktadır . Fonksyon adı fbonaccSers olarak tanımlanmıştır . Fonksyon grlen sayı kadar
eleman döndüreceğnden, parametre olarak br n sayısını almaktadır . Fbonacc sers elemanları dz adındak lstede
tutulacaktır . Sernn lk k elemanı da a ve b şeklnde tanımlanmıştır . whle döngüsü dz uzunluğu n’e eşt olduğunda
tamamlanacaktır , çünkü bu aynı zamanda belrlenen n sayısı kadar eleman dz lstesne eklend demektr . Döngüde her
terasyonda, a eleman olarak eklenecektr , ardından br sonrak terasyon çn a+b br öncek, b se k öncek eleman
pozsyonuna gelecektr . Döngü tamamlandığında dz fonksyon tarafından ger döndürülür .


Örnek 8:  Verlen br lstenn tüm elemanlarının tam sayı ya da kayan ondalıklı sayı olup olmadığını kontrol eden, lste
koşulu sağlıyorsa lste elemanlarının toplamını, sağlamıyorsa -1 ger döndüren Python fonksyonunu yazınız.
Çözüm:  Örnekte verlen fonksyonun adı lsteKontrol olarak belrlenmştr . Fonksyonda br lstenn elemanları kontrol
edleceğnden, parametre olarak lstem adlı br değşken almaktadır . Lste elemanları tam sayı ya da kayan ondalıklı sayı
se sonuçta lstedek elemanların toplamı döndürülmek stendğnden bu toplamın tutulacağı toplam adında lk değer sıfır
olan br değşken tanımlanmıştır . for döngüsü br lstenn elemanlarını dolaşacak bçmde oluşturulmuştur . Yan, eleman
lk terasyonda verlen lstem[0], knc terasyonda lstem[1], üçüncüde lstem[2], … olacaktır . for döngüsü çnde f-else
le lstem lstesnn her br elemanı sırayla kontrol edlr . Eğer , eleman tam sayı ya da kayan ondalıklı sayı se
(type(eleman) n (nt, float) koşulu True dönerse) eleman her sefernde toplam değşkenne eklenecektr . Tek br eleman
ble bu koşulu sağlamazsa -1 döndürülecek ve döngü sonlandırılacaktır .
Fonksyon tanımlandıktan sonra k örnek lste tanımlanarak fonksyona grd olarak verlmştr . İlk lste olan A’da tüm
elemanlar koşulu sağladığından gerye elemanların toplamı olan 220.0 döndürülecektr . İknc lste B’de se her ne kadar
tüm elemanlar kurala uygun gb gözükse de B[3] = “80.5” br strngdr . Bu nedenle de type(eleman) n (nt, float) koşulu
False döner . Netcede, fonksyon -1 döndürür .
Fonksyonun çndek for döngüsü çn alternatf br başka çözüm aşağıdak gbdr .


Örnek 9:  Verlen br lstenn en büyük ve en küçük elemanlarını döndüren Python fonksyonunu yazınız.
Çözüm:  Örnektek fonksyonun adı enBuy_enKuc olarak belrlenmştr . Eğer fonksyona verlen lste boşsa (len(A) == 0)
None döndürülecektr . Ardından eğer lstenn uzunluğu sıfırdan farklı se, başlangıçta lstenn maksmumu (mn_A) da
mnmumu (max_A) da lstenn lk elemanı olacak şeklde belrlenmştr . Eğer lstede bu elemandan daha küçük br
eleman bulunursa yen mnmum o eleman, eğer lstede bu elemandan daha büyük br eleman bulunursa yen maksmum
o eleman olarak belrlenr . Fonksyon sonunda, lstenn mnmumu ve maksmumu olarak bulunan elemanlar döndürülür .
Fonksyon tanımlandıktan sonra örnek br B lstes tanımlanarak fonksyona grd olarak verlmştr . Fonksyondan dönen
değerler sırasıyla mn_B ve max_B değşkenlerne atanmıştır . Ardından sırasıyla, fonksyona verlen B lstes, B lstesnn
enBuy_enKuc() fonksyonu yardımı le bulunan en küçük ve en büyük elemanları yazdırılmıştır .
Örnek 10:  Yarıçapı grlen br çembern çevres ve alanını hesaplarken p değern varsayılan olarak 3.14 alan; ancak
kullanıcının p değern dledğ gb ayarlamasına zn veren Python fonksyonunu yazınız.
Çözüm:  Örnekte hesapla adında br fonksyon tanımlanmıştır . Fonksyon, yarıçapı grlen br çembern çevres ve alanı
hesaplanacağından, yarıçap çn r parametresn almaktadır . Ayrıca, p değern varsayılan olarak 3.14 alması; aynı
zamanda kullanıcının p değern dledğ gb ayarlaması çn dğer br parametres p=3.14 olarak verlmektedr .
Ardından fonksyon sırayla çevre ve alan blgsn döndürmektedr .
hesapla(5) olarak verlen lk kullanımda, yalnızca yarıçap çn 5 ar gümanı verlmştr . Bu nedenle, fonksyonun p çn
varsayılan parametres 3.14 alınmış, çevre ve alan buna göre hesaplanmıştır . Dğer yandan, hesapla(5,3) olarak verlen
knc örnek kullanımda p’nn varsayılan değer yerne 3 olarak kullanıcı tarafından belrlenen değer hesaplamalarda
kullanılmıştır .


**Bölüm Özet**

Bu bölümde, Python programlama dlnde fonksyon kavramı en temel ve yalın hal le ele alınmıştır . Ardından, hazır
fonksyonların yanı sıra kullanıcı tanımlı fonksyonlara da yer verlmştr . def anahtar kelmes kullanılarak fonksyonların
nasıl tanımlandığı öğretlrken, fonksyonların tekrar kullanılablrlğ ve kodun modülerlğn artırmada nasıl öneml br
rol oynadığı vur gulanmıştır . Aynı zamanda, lambda fonksyonlarıyla daha kısa ve şlevsel br yaklaşımın nasıl sağlandığı
fade edlmştr . Buna ek olarak, map() ve flter() gb yardımcı fonksyonlarla ver üzernde dönüşüm ve fltreleme
örneklerle sunulmuştur . Fonksyonlarla lgl karma örnekler , öğrenclere farklı senaryolarda fonksyonların nasıl
kullanılableceğn göstererek pratk becerler kazandırmayı amaçlamaktadır .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html


Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134


Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Verlen fonksyonla lgl aşağıdak seçeneklerden hangs doğrudur?
(Çoktan Seçmel)
(A) Parametre alan, ger değer döndüren br fonksyondur .
(B) Parametre almayan, ger değer döndüren br fonksyondur .
(C) Parametre alan, ger değer döndürmeyen br fonksyondur .
(D) Parametre almayan, ger değer döndürmeyen br fonksyondur .
(E) Fonksyonu çağırmak çn fonk() yazmak yeterldr .
Cevap-1 :
Parametre alan, ger değer döndüren br fonksyondur .
Soru-2 :


Verlen kod bloğunda akışı bozan nedr?
(Çoktan Seçmel)
(A) Fonksyon parametre almaması gerektğ halde say1 ve say2 le çağrılmaya çalışılmaktadır . toplama() şeklnde
çağrılması yeterldr .
(B) Fonksyon ger değer döndürmedğ halde, fonksyon çağrılırken toplam değşkenne atanmıştır . Bu atama
kaldırılmalıdır .
(C) Fonksyon çnde return fades kullanılamaz, slnmeldr .
(D) Fonksyonun çağırıldığı yerden önce tanımlanması gerekldr . toplam = toplama(say1, say2) kod satırı bloğun
sonuna alınmalıdır .
(E) Fonksyon çn 10 ve 20.5 ar gümanları doğrudan verlmeldr . say1 ve say2 değşkenler tanımlanmamalıdır .
Cevap-2 :
Fonksyonun çağırıldığı yerden önce tanımlanması gerekldr . toplam = toplama(say1, say2) kod satırı bloğun sonuna
alınmalıdır .
Soru-3 :
Aşağıda br satıcının müşternn ödeme mktarına göre varsayılan %10 ndrm yaptığı ve nha ödeme tutarının
hesaplandığı br fonksyon tanımlanmaktadır . Verlen kod bloğu çalıştırıldığında aşağıdak seçeneklerden hangs doğru
olur?
(Çoktan Seçmel)
(A) Herhang br ndrm yapılmaz, çünkü ndrm parametresne değer grlmemştr .
(B) %500 ndrm uygulanır .
(C) %10 ndrm uygulanır ve ger 450.0 döndürülür .
(D) Fonksyon tanımında br parametres değer almazken dğerne varsayılan değer tanımlanmıştır . Bu nedenle verlen
kod bloğu çalışmaz.
(E) %100 ndrm uygulanır ve ger 0 döndürülür .
Cevap-3 :
%10 ndrm uygulanır ve ger 450.0 döndürülür .
Soru-4 :
Aşağıda verlen fonksyonun görev seçeneklerden hangsnde eksksz br bçmde verlmştr?


(Çoktan Seçmel)
(A) Kullanıcı tarafından grlen br sayının 10 le bölünüp bölünmedğn kontrol eder , eğer bölünüyorsa bölüm değern
döndürür .
(B) Kullanıcı tarafından grlen sayıların sıfırdan büyükse ve 10 le bölünüyorsa bs lstesne atar , bölünmeyen sayıları
döndürür .
(C) Kullanıcı tarafından grlen sayıların sıfırdan büyükse ve 10 le bölünüyorsa bs lstesne atar , bs lstesn döndürür .
(D) Kullanıcı tarafından grlen br sayının basamaklarını ayırır ve bu basamakları br demet ( tuple ) çnde döndürür .
(E) Kullanıcı tarafından grlen br sayının basamaklarını ayırır , basamakları tek tek br lsteye atar ve bu lstey döndürür .
Cevap-4 :
Kullanıcı tarafından grlen br sayının basamaklarını ayırır , basamakları tek tek br lsteye atar ve bu lstey döndürür .
Soru-5 :
Br metn çnde belrl br karaktern kaç kez geçtğn sayan br fonksyon tanımlanıyor . Noktalarla belrtlen boşluk
aşağıdak seçeneklerden hangs le tamamlanablr?
(Çoktan Seçmel)
(A) def kacT ane(metn, karakter)
(B) def kacT ane(metn, karakter):
(C) def kacAdet(metn, karakter):
(D) defne kacT ane(metn, karakter):
(E) defne kacAdet(metn, karakter):
Cevap-5 :
def kacT ane(metn, karakter):
Soru-6 :
def le tanımlanan fonksyonun lambda le fades aşağıdak seçeneklerden hangsnde verlmştr?


(Çoktan Seçmel)
(A) carp = lambda s1 s2 s3: s1*s2*s3
(B) carp = lambda s1, s2, s3: s1*s2*s3
(C) carp = lambda s1*s2*s3: s1, s2, s3
(D) carp = lambda s1*s2*s3
(E) carp = lambda: s1*s2*s3
Cevap-6 :
carp = lambda s1, s2, s3: s1*s2*s3
Soru-7 :
Aşağıdak seçeneklerden hangsnde grlen br metn büyük harfe çevren br lambda fonksyonu verlmştr?
(Çoktan Seçmel)
(A) cevr = lambda x = x.upper
(B) cevr = lambda: x: x.upper()
(C) cevr = lambda x - x.upper()
(D) cevr = lambda x: x.upper()
(E) cevr(lambda x: x.upper())
Cevap-7 :
cevr = lambda x: x.upper()
Soru-8 :
metnler = ["Merkür", "vEnüS", "DünyA", "MArs"] lstes verlyor . Aşağıdak seçeneklern hangs lstedek tüm
elemanları büyük harfe çevrerek lste bçmnde döndürür?
(Çoktan Seçmel)
(A) lst(map(lambda x: x.upper(), metnler))
(B) lst(map(lambda x= x.upper , metnler()))
(C) map(lst(lambda x: x.upper(), metnler))
(D) lambda(map x: x.upper(), metnler)
(E) lambda x: x.upper(metnler)
Cevap-8 :
lst(map(lambda x: x.upper(), metnler))
Soru-9 :


Aşağıdak kod bloğu çalıştırıldığında ekrana ne yazdırılır?
(Çoktan Seçmel)
(A) ['İlkm']
(B) ['Elf', 'İlkm', 'Zek']
(C) ['Elf', 'İlkm']
(D) ['Önay', 'Zek', 'Utku']
(E) ['Elf']
Cevap-9 :
['Elf', 'İlkm']
Soru-10 :
Python dlnde br fonksyonun ar gümanlarını (parametrelern) brbrnden ayırmak çn hang sembol kullanılır?
(Çoktan Seçmel)
(A) .
(B) ,
(C) ;
(D) <-
(E) []
Cevap-10 :
,


# 7. NESNEYE YÖNELİMLİ PROGRAMLAMA


**Bölümle İlgl Özlü Söz**

Öğrenebleceğnz en fec şey , lk programlama dlnzdr .
Alan Kay , Blgsayar Programcısı

**Kazanımlar**

1. Nesneye yönelml programlamanın temel prensplern anlar .
2. Sınıf ve nesne kavramlarını kavrar ve kullanablr .
3. Nesneye yönelml programlamanın avantajlarını blr .
4. Python le sınıf ve nesne oluşturablr .
5. Sınıfların özellklern ( attrbutes ) ve metodlarını ( methods ) tanımlayablr ve kullanablr .
6. Sınıflar arasındak mras lşksn anlar ve kullanablr .
7. Çok bçmllk ( polymorphsm ) kavramını anlar ve uygulayablr .
8. Aynı metot adı le farklı sınıflar arasında farklı metodlar tanımlamayablr , bu tür br tanımlamanın avantajlarını ve
kullanımını anlar .
9. Kapsülleme ( encapsulaton ) prensplern anlar ve uygular .
10. Sınıf üyelerne erşm kontrolü uygulayablr .

**Brlkte Düşünelm**

1. Nesneye yönelml programlama nedr ve neden önemldr? Nesneye yönelml programlamanın temel prenspler
nelerdr?
2. Python le br sınıfın nasıl tanımlandığını ve br nesnenn nasıl oluşturulduğunu açıklayınız.
3. Br nesnenn özellkler ( attrbutes ) ve metodları ( methods ) arasındak fark nedr? Br örnekle açıklayınız.
4. Nesneye yönelml programlamanın avantajları nelerdr ve hang tür uygulamalar çn uygundur?
5. En az k farklı özellk ve metoda sahp br sınıf oluşturunuz. Bu sınıfa at 2 farklı nesne yaratınız.
6. Mras alma/kalıtım ( nhertance ) nedr ve neden kullanılır? Hang durumlarda mras alma kullanışlıdır?
7. Python dlnde br alt sınıf ( subclass ) br üst sınıftan ( super class ) nasıl türetleblr?
8. Çok bçmllk ( polymorphsm ) nedr ve neden önemldr? Hang avantajlar sunar?
9. Python dlnde çok bçmllğ nasıl uygularsınız? Örnekler vererek açıklayınız.
10. Kapsülleme ( encapsulaton ) nedr ve neden kullanılır? Ne gb avantajlar sunar?
11. Python le kapsülleme nasıl uygulanır?

**Başlamadan Önce**

Nesneye yönelml programlamanın ( Object Orented Pr ogrammng- OOP ), brçok modern programın temeln
oluşturan br yaklaşımdır ve programların daha düzenl, modüler ve anlaşılır hale getrmey sağlar . Ayrıca, program


kodunun yenden kullanılmasını ve sürdürüleblr kılınmasına yardımcı olur . Özellkle, büyük ve karmaşık projelern
daha kolay yönetlmesne yardımcı olacak güçlü br programlama yaklaşımıdır . Bu bölümde, nesneye yönelml
programlamanın temel kavramlarına, Python programlama dlnde nasıl uygulandığına ve genel programlama
çerçevesnde nesneye yönelml programlamanın neden öneml br unsur olduğuna dar temel blgler bulunmaktadır .
Python programlama dlnde sınıf ve nesne kavramlarını anlatılarak, verler ve fonksyonların nasıl gruplanableceğ ve
düzenlenebleceğne lşkn örnekler ve açıklamalar yer almaktadır .
Sınıf ve nesne kavramlarının ardından, mras alma/kalıtım ( nhertence ), çok bçmllk ( polymorphsm ) ve kapsülleme
(encapsulaton ) gb nesneye yönelml programlamanın ler düzey konuları şlenmştr . Böylelkle, program kodunun
daha esnek, özelleştrleblr , güvenl ve sürdürüleblr hale geleblecektr . Bu bölümün sonunda, Python programları
nesneye yönelml programlamanın prensplerne uygun bçmde tasarlanablecek ve gelştrleblecektr .

## 7.1. Nesneye Yönelml Pr ogramlama

Nesneye Yönelml Programlama ( Object Orented Pr ogrammng - OOP ), özellklern ve davranışların ayrı ayrı nesneler
(objects ) halnde paketlenmes çn programları yapılandırmanın br yolunu sağlayan br programlama paradgmasıdır
(Amos, 2018). Java, C#, Python, PHP , JavaScrpt, Ruby ve Perl nesneye yönelml programlama dller arasındadır .
Nesneye yönelml programlama mantığı gerçek dünyadak (canlı/cansız) nesnelern programlama ortamına taşınması
gb düşünüleblr . Örneğn; ad, soyad, yaş, telefon ve adres gb özellklere ve yürüme, konuşma, nefes alma ve koşma
gb eylemlere sahp br kşy temsl eden br nesne oluşturulablr . Daha özel br örnek verlmek stenrse; alıcı lstes,
konu başlığı ve gövde gb özellklere ve ek ekleme ve gönderme gb eylemlere sahp br e-postayı temsl eden br nesne
olablr . Programlamada yer alan dğer br paradgma se, br görev tamamlamak çn sırayla akan fonksyon ve kod
blokları bçmnde br dz adım sağlaması açısından br programı br tarf gb yapılandıran prosedürel programlamadır
(Amos, 2018). Python dlnde nesneler , nesne yönelml programlamanın merkeznde yer alır , prosedürel programlamada
olduğu gb yalnızca very değl, programın genel yapısında da very temsl eder .
Nesneye yönelml programlamada k öneml unsur yer almaktadır . Bunlardan lk kalıtım  (nhertance ), dğer se
kompozsyon dur ( composton ). Bu k unsur hakkında somut örnekler verleblr (Lutz, 2009): Eğer br pzzacıda pzza
yapan robotlar kullanılmakta se, pzza yapan robotlar , normal robot türlerdr . Dolayısıyla, normal robot özellklerne
halhazırda sahplerdr . Nesneye yönelml programlama bakış açısıyla değerlendrldğnde, tüm robotların genel
kategorsnden özellklern pzza robotları tarafından mras alındığı söyleneblr . Bu ortak özellklern genel durum çn
yalnızca br kez uygulanması gerekr ve gelecekte nşa edebleceğmz tüm robot türler tarafından yenden kullanılablr .
Pzza yapan robotlar , gerçekten br ekp olarak brlkte çalışan bleşenlern brer koleksyonudur . Örneğn, robotun verlen
görev başarıyla tamamlamasında kollara, motorlara vb. htyacı olablr . Yne nesneye yönelml programlama bakış
açısıyla, pzza yapan robot br kompozsyon örneğdr; görev yerne getrmek çn dğer nesneler çerr . Her bleşen,
kend davranışını ve lşklern tanımlayan br sınıf (class ) olarak kodlanablr .

## 7.2. Sınıf ve Nesne

Sınıf  (class ), kullanıcı tanımlı br ver yapısı oluşturmak çn kullanılmaktadır (Amos, 2018). Br sınıftan brden fazla
nesne türetleblr (Çobanoğlu, 2021). Br sınıfın nesnesn oluşturma şlemne örnekleme  (nstantaton ) denr . Sınıflar ,
sınıftan oluşturulan br nesnenn versyle gerçekleştrebleceğ özellk ve eylemler tanımlayan yöntem  (method ) adı
verlen fonksyonları tanımlar . Br şey nasıl tanımlanmak stenyorsa onun çatısı oluşturulur . Eğer br “kş” sınıfı
yaratılacaksa, ad, soyad, yaş, telefon ve adres gb özellklere, yürüme, konuşma, nefes alma ve koşma gb eylemlere
sahp olacağı belrlenr . “kş” sınıfından oluşturulan br örnek se artık gerçek ver çeren br yapıdır , br taslak ya da çatı
ya da plan bçmnde değldr . Adı Elf, soyadı Kartal, yaşı 36, … şeklnde. Sınıf, boş br form olarak düşünüleblr ,
üzernde standart sorular mevcuttur (Amos, 2018). Dğer yandan, örnek artık bu anketn dolu haldr , herkes kend adına
anket doldurablecektr . Dolayısıyla bu, br sınıftan brden fazla örnek türetleblr düşüncesn de destekler .
Python le sınıf oluşturulurken aşağıdak özellkler dkkate alınır (GeeksforGeeks, 2016):
• Sınıflar , class anahtar kelmesyle oluşturulur .
• Özellkler , br sınıfa at değşkenlerdr .
• Özellkler her zaman geneldr ve nokta (.) operatörü kullanılarak erşleblr . Örn.: Sınıfım.Özellk gb.
Aşağıda evclHayvanPasaportu adında br sınıf tanımlanmıştır .


evclHayvanPasaportu sınıfına at br nesne yaratılmak stenrse, yaratılacak bu nesneye at üç temel özellk mevcut
olacaktır (GeeksforGeeks, 2016):
• Durum  (State ): Br nesnenn özellkler le temsl edlr .
• Eylem  (Behavour ): Br nesnenn metotları le temsl edlr .
• Kmlk  (Identty ): Br nesneye benzersz br ad verr ve br nesnenn dğer nesnelerle etkleşme grmesn sağlar .
Pasaport sınıfına at br nesne aşağıdak kod satırı yardımı le oluşturulablr . Nesnenn oluşturulablmes çn
evclHayvanPasaportu sınıfının yaratılması gerekmekte olduğu unutulmamalıdır .
Öncek örneklerde sınıfın çnde herhang br özellk ya da metot tanımlanmadığından herhang br şlem de
gerçekleştrlememştr . Aşağıdak sınıf çn br de tur adında br özellk tanımlanmıştır . Br sınıftan türetlen nesneler sınıf
özellklerne de sahptr . Ayrıca, daha sınıfın örneğ oluşturulurken, kednn adını steyecek br sınıf oluşturulsun.
__nt__, evclHayvanPasaportu sınıfının br örneğn başlatan özel yapıcı  (constructor ) br metottur . İk parametre alır:
İlk parametre self, oluşturulan örneğe atıfta bulunurken, ad ked adını temsl eder . Sınıf tanımlama şlemnn ardından
pp_msk, pp_safyuz ve pp_ccero adında bu sınıfın üç farklı örneğ oluşturulmuştur . Bu şlem sırasında her br çn br
ad alındığı unutulmamalıdır . Sınıfa at bu örneklern adına ve sınıf özellğne nasıl erşldğ her üçü çn de gösterlmştr .
İlgl ekran görüntüsüne se kod bloğundan sonra yer verlmştr .
Verlen sınıfa br de metot dâhl edlrse mevcut sınıf aşağıdak bçmde yenden yazılablr . Bu sayede
evclHayvanSınıfınakısaBlg adında br metot eklenmş olur . Bu metot, yne self aracılığı le oluşturulan örneğe atıfta
bulunur . İlgl Python kod bloğuna ve elde edlen ekran görüntüsüne aşağıda yer verlmştr .


Şmd de yen br Market sınıfı tanımlansın. Market sınıfının ad, konum ve urunler olmak üzere üç özellğ
bulunmaktadır . Sınıfa at br örnek tanımlanırken başlangıçta muhakkak ad ve konum özellklerne ver grş yapılması
gerekmektedr . Sınıfın çnde urun_ekle(), urun_sl() ve urunler_lstele() adı verlen metotlar tanımlanmıştır . urun_ekle()
metodunda br ürün adı grlmes beklenmektedr . Bu doğrultuda boş br lste olan urunler özellğne append() le atama
yapılması sağlanır . Eğer stoktak br ürünün slnmes söz konusu se urun_sl() kullanılacaktır . Adı verlen ürün, urunler
lstesnden kaldırılmış olur , eğer lgl ürün stokta bulunamazsa “ … stokta bulunamadı. ” uyarısı döndürülür .
urunler_lstele() le stoktak ürün adları yazdırılır .
Market sınıfının örnek uygulamasında marketm adında br örnek türetlmştr . Ardından çeştl ürünler urun_ekle()
yardımıyla sırasıyla market stoğuna eklenmş ve stoktak ürünler urunler_lstele() le lstelenmştr . “Domates” ürünü
stokta olmadığından bu ürün urun_sl() yardımıyla stoktan slnmeye çalışıldığında uyarı döndürülecektr . “Peynr” se
stoktan kaldırılacaktır . Tüm stok ürünler yenden lstelendğnde stoğun son durumu yazdırılmış olur .


## 7.3. Mras Alma/Kalıtım ( Inhertence )

Nesneye yönelml programlamanın öneml özellklernden br de kalıtım/mras alma ( nhertence ) d. Yukarıda
evclHayvanPasaportu adında br sınıf ve bu sınıfa at örnekler oluşturulmuştur . Bu bölümde se br sınıf anasınıf (parent)
olarak yern alırken dğer ondan mras alan  (chld ) konumda olacaktır . Aşağıda verlen örnektek hayvanPasaportu ana
sınıf, evclHayvanPasaportu se hayvanPasaportu’ndan mras alan sınıftır . Mras almak le kastedlen, mras alan sınıf
tarafından br üst sınıfa ( super class ) at özellk ve metotlar kullanılablr ve br üst sınıfın metotları değştrleblr .
Aşağıda öncelkle hayvanPasaportu sınıfı tanımlanmıştır . ad, tur ,rk, cnsyet, dogumT arh ve renk özellkler le
ksaBlg ve detaylBlg metotlarını çermektedr .


Sonrasında da hayvanPasaportu sınıfını mras alan evclHayvanPasaportu sınıfı tanımlanmıştır . evclHayvanPasaportu
sınıfında hayvanPasaportu sınıfından farklı olarak cpNo, sahpAd ve sahpSoyad şeklnde üç farklı özellk ve br yen
sahp metodu daha mevcuttur . Ayrıca, kısaBlg metodu mras alan sınıf çnde değştrlmştr . Dkkat edlmes gereken,
mras alan sınıf çnde hayvanPasaportu sınıfına özel yapıcı fonksyon çağrılmıştır .
Bu k sınıf tanımlandıktan mras alan sınıf olan evclHayvanPasaportu sınıfının msk_pp adında br örneğ yaratılmıştır .
İlk kod satırından da görüleceğ gb bu örnek hem mras alınan sınıfın (hayvanPasaportu) özellkler hem de
evclHayvanPasaportu sınıfının özellkler le oluşturulmuştur . ksaBlg(), detaylBlg() ve sahp() metotlarından
döndürülen vernn bulunduğu ekran görüntüsü aşağıda verlmştr .


Şmd de aşağıda tanımlanan Agac sınıfı le Agac sınıfından mras alan MeyveAgac le YaprakDokmeyenAgac sınıfları
ncelensn. Agac sınıfının tur ve boy adında k özellğ vardır ve sınıfa at örnek oluşturulurken bu blglern de grlmes
gerekr . Ağacın boyuna grlecek olan büyüme mktarının (buyume) lâve edldğ uzat() metodu le ağaç hakkında genel
blgnn görüntülenmesn sağlayan blg() metodu bulunmaktadır .
Agac sınıfından mras alan sınıflardan br MeyveAgac sınıfıdır . Bu sınıfta laveten meyve özellğ ve ağacın meyvesnn
görüntülenmesn sağlayan meyves() metodu bulunmaktadır . Dğer alt sınıf ( subclass ) olan YaprakDokmeyenAgac se
Agac sınıfından farklı olarak gneT uru özellğn çermektedr . Ayrıca, blg() metodu le lstelenenlere gneT uru özellğ
de eklenmştr .
Sınıfların örnek kullanımı çn önce temel sınıf olan Agac sınıfının sonrasında da MeyveAgac ve YaprakDokmeyenAgac
sınıflarının brer örneğ oluşturulmuş ve bu örnekler üzernden sınıfların özellkler ve metotlarına erşm sağlanmıştır .
Ekran görüntülerne kod bloğunun altında yer verlmştr .


## 7.4. Çok Bçmllk ( Polymorphzm )

Br temel sınıfın br metodunun, alt sınıflar tarafından kend kullanım amaçlarına göre değştrlmesne çok bçmllk
(polymorphzm  ya da method overrdng ) adı verlmektedr . Çok bçmllğ örneklemek çn evclHayvanPasaportu
sınıfının yanı sıra vahsHayvanPasaportu sınıfı tanımlanmıştır . Temel sınıf ve alt sınıflar ncelendğnde ksaBlg
metodunun değşk bçmlerde kullanıldığı görüleblecektr . Bu metot, hayvanPasaportu sınıfında yalnızca hayvan türü ve
adını döndürürken, evclHayvanPasaportu sınıfında çp numarası, hayvan türü ve adını, vahsHayvanPasaportu sınıfında
se kıta, bolge ve ad blglern döndürmektedr .


Çok bçmllk çn başka br örnek vermek gerekrse, Sekl sınıfı ve bu sınıftan türetlen Kare ve Dkdortgen sınıfları
nceleneblr . Ana sınıfta yer alan alan ve cevre metotları Kare ve Dkdortgen sınıflarında farklı hesaplamalar yaparak
farklı değerler döndürmektedr . İlgl alt sınıfın alan() ve cevre() formüller geçerl olmaktadır .


## 7.5. Kapsülleme ( Encapsulaton )

Kapsülleme, tek br sınıfın çne özellklern ve metotların gömülmes şlemdr . Kapsülleme, özellklern ve metotların
tek br sınıf çnde paketlenmesn fade eder . Dış sınıfların br sınıfın özellk ve metotlarına erşmesn ve bunları
değştrmesn de engeller , ver gzlemeye yardımcı olur (programz.com, 2023). Python dlnde, dğer bazı programlama
dllernde olduğu gb özel (prvate ) br değşken tanımlamak çn prvate  sözcüğü kullanılmaz. Bunun yerne Python
sınıf özellkler çft altçzg (__) ön ek yardımı le tanımlanır .


Aşağıda Calsan adında br sınıf tanımlanmıştır . Bu sınıfın, KurumID özellğ ve f1() metodu özel ( prvate )
tanımlanmıştır . Yan, eğer sınıfın br örneğ oluşturulursa ve ardından KurumID ve f1() metoduna erşlmek stenrse
sınıfın bu şeklde tanımlanmış olan özellğ ya da metodu yoktur şeklnde hata mesajı döndürülür . Sınıfın çndek f2()
özel şeklde tanımlanmamıştır . Dolayısıyla, sınıfın br örneğ üzernden f2 çağrılablr . KurumID ve f1() çn erşm f2()
üzernden sağlanmıştır . Bu nedenle de kod bloğunun son satırı çalıştırıldığında, özel değşkenlern görüleblmes
sağlanmış olur .
Örneğn; aşağıdak gb br Snav sınıfı olsun. Bu sınıfın çnde gecmeNotu özel ( prvate ) şeklnde tanımlansın. Bu
özellğn değern gösterecek br metot br de değer atama çn kullanılan setGecmeNotu() metodu tanımlanmıştır . Snav
sınıfının br s örneğ yaratılmıştır . Goster metodu çağrıldığında __gecmeNotu değernn 75 olduğu görülecektr . Bu
değşkene dışarıdan br atama yapılmaya çalışılırsa, bu değşkenn değern değştrmeyecektr . Değern hala 75 olduğu
görüleblr . Tanımlanan bu özel değşken değer ancak setGecmeNotu çağrılırsa değştrlecektr .


Python le kapsülleme üzerne başka br örnek de Flm sınıfı üzernden verlsn. Sınıf oluşturulurken br flme özgü
başlık, tür ve puan gb bazı özellkler özel (prvate ) tanımlanmıştır . Dolayısıyla, sınıfın örneğ oluşturulduktan sonra bu
özellklerne erşm sağlanamayacak, değerler değştrlemeyecektr . Bu nedenle, her br özellğn değern göreblmek
get_baslk(), get_tur() ve get_puan() metotları, her br özellğe değer atayablmek çnse set_baslk(), set_tur() ve
set_puan() metotları oluşturulmuştur . set_puan() metodunda ekstra olarak puanın 1 le 10 arasında olup olmadığı kontrol


edlmştr . Eğer puan olarak atanan değer uygunsa atama şlem gerçekleştrlecek, aks takdrde metot uyarı mesajı
döndürecek şeklde ayarlanmıştır .
Bu sınıfın örnek kullanımında Flm sınıfının br örneğ olan m1 baslk, tur ve puan değerler sırasıyla “ Buz Devr 3:
Dnazorların Şafağı ”, “Çzg Flm ” ve 9.5 olacak şeklde tanımlanmıştır . Ardından bu değerler; get_baslk(), get_tur() ve
get_puan() metotları yardımı le yazdırılmıştır . Ardından m1’n 9.5 olan puanı 10 olarak değştrlmştr . m1’n yen puan
değer ekrana yazdırılmıştır . Son satırda, puan özellğnn set_puan metodunda kontrol edlen değer aralığı kapsamı
dışında br değer grlmştr . Buna karşılık bekleneceğ gb Lütfen 1-10 arasında geçerl br puan grnz.  uyarısı
döndürülmüştür . Eğer dğer m1’n başlık ya da türü değştrlmek stenrse set_baslk() ve set_tur() metotları
kullanılablecektr .


**Bölüm Özet**

Bu bölümde, nesneye yönelml programlamaya odaklanılmaktadır . İlk olarak, sınıf ve nesne kavramları ayrıntılı br
şeklde açıklanarak, nesneye yönelml programlamanın temeln oluşturan bu yapılar anlatılmıştır . Ardından, mras
alma/kalıtım konusu ele alınarak, sınıflar arasındak hyerarşk lşklern nasıl kurulableceğ ve özellklern nasıl
paylaşılableceğ ncelenmştr . Çok bçmllk ve kapsülleme konuları le nesneye yönelml programlama konusunda
daha dern br anlayış kazandırmak hedeflenmştr . Her br özel kavram le lşkn örnek uygulamalar sayesnde,
okuyucular hem nesneye yönelml programlamanın temel prensplern anlama fırsatı bulmakta hem de Python dlnde bu
prenspler nasıl uygulayableceklern öğrenme şansını elde etmektedr .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.
GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/


Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html
Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python


Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :
Python le br sınıf oluşturulmak stenrse bunun ç Python dlndek hang özel kelme kullanılır?
(Çoktan Seçmel)
(A) def
(B) defne
(C) class
(D) sınıf


(E) functon
Cevap-1 :
class
Soru-2 :
Aşağıda br Araba sınıfı tanımlanmaktadır . Buna göre verlen seçeneklerden hangs bu sınıfa at br özellk ( attrbute )
değldr?
(Çoktan Seçmel)
(A) marka
(B) model
(C) motor_gucu
(D) yakt_turu
(E) blgler_goster
Cevap-2 :
blgler_goster
Soru-3 :
Aşağıdaklerden hangs verlen Dkdörtgen sınıfına at br metottur ( method )?
(Çoktan Seçmel)
(A) en
(B) boy
(C) self
(D) alan_hesapla


(E) Dkdörtgen
Cevap-3 :
alan_hesapla
Soru-4 :
Ogrenc sınıfının br nesnes aşağıdak seçeneklerden hangsnde doğru br bçmde oluşturulmuştur?
(Çoktan Seçmel)
(A) o1 = Ogrenc("Elf", "Kartal", "12345678")
(B) o1 = Ogrenc(Elf, Kartal, 12345678)
(C) o1 = def: Ogrenc("Elf", "Kartal", "12345678")
(D) o1 = öğrenc("Elf", "Kartal", "12345678")
(E) o1 = Ogrenc(self.ad="Elf", self.soyad="Kartal", self.numara="12345678")
Cevap-4 :
o1 = Ogrenc("Elf", "Kartal", "12345678")
Soru-5 :
Ogrenc sınıfı çnde bulunan blgler_goster adlı metot ne şe yarar?
(Çoktan Seçmel)
(A) Ogrenc sınıfının tüm özellklern kaydeder .
(B) Ogrenc sınıfının tüm özellklern ekrana yazdırır .
(C) Ogrenc sınıfının adını ve soyadını ekrana yazdırır .
(D) Ogrenc sınıfının numara özellğn ekrana yazdırır .
(E) Ogrenc sınıfının oluşturulmasında kullanılan Python program kodlarını ekrana yazdırır .
Cevap-5 :
Ogrenc sınıfının tüm özellklern ekrana yazdırır .
Soru-6 :
Calsan sınıfının br nesnesnn oluşturulablmes çn hang blgler gerekecektr?


(Çoktan Seçmel)
(A) Yalnızca ad.
(B) ad ve soyad.
(C) ad ve maas.
(D) soyad ve maas.
(E) ad, soyad ve maas.
Cevap-6 :
ad, soyad ve maas.
Soru-7 :
Aşağıdak seçeneklerden hangsnde mras alma/kalıtım doğru br şeklde açıklanmıştır?
(Çoktan Seçmel)
(A) Mras alma/kalıtım, br sınıfın başka br sınıftan özellklern ve yöntemlern alması şlemdr .
(B) Mras alma/kalıtım, br sınıfın tüm özellklern ve yöntemlern kaybetmes şlemdr .
(C) Mras alma/kalıtım, yalnızca Python programlama dlnde kullanılablen br özellktr .
(D) Mras alınan sınıfa alt sınıf ( subclass ), mras alan sınıfa se üst sınıf ( super class ) denr .
(E) Mras alma/kalıtım, br sınıfın özellklern ve yöntemlern tamamen değştrmes şlemdr .
Cevap-7 :
Mras alma/kalıtım, br sınıfın başka br sınıftan özellklern ve yöntemlern alması şlemdr .
Soru-8 :
Aşağıdak seçeneklerden hangsnde çok bçmllğn/polmorfzmn doğru br tanımı verlmektedr?
(Çoktan Seçmel)
(A) Polmorfzm, br sınıfın kendsne at metotları kullanmasıdır .
(B) Polmorfzm, br sınıfın başka br sınıfa at özellkler mras almasıdır .
(C) Polmorfzm, farklı sınıfların aynı sml metodları farklı şekllerde uygulamasıdır .
(D) Polmorfzm, sınıflar arasında özellklern ve yöntemlern tamamen paylaşılmasıdır .
(E) Polmorfzm, sadece Python programlama dlnde kullanılablen br özellktr .
Cevap-8 :
Polmorfzm, farklı sınıfların aynı sml metodları farklı şekllerde uygulamasıdır .


Soru-9 :
Aşağıdaklerden hangs kapsülleme (encapsulaton) çn doğrudur?
(Çoktan Seçmel)
(A) Br sınıfın, başka br sınıfa at tüm özellklern ve yöntemlern kullanmasıdır .
(B) Belrl sınıf üyelerne erşm kısıtlamak çn özellk ve metotları br araya getrmey sağlar .
(C) Yalnızca Python dlne özgü br uygulamadır .
(D) Yukarıdaklern heps.
(E) Yukarıdaklern hçbr.
Cevap-9 :
Belrl sınıf üyelerne erşm kısıtlamak çn özellk ve metotları br araya getrmey sağlar .
Soru-10 :
Aşağıdak seçeneklerden hangs çalıştırılırsa hata mesajı döndürülür?
class Ogrenc:
   def __nt__(self, ad, soyad, numara, telefon, adres):
     self.__ad = ad
     self.soyad = soyad
     self.numara = numara
     self.telefon = telefon
     self.adres = adres
def get_ad(self):
   return self.__ad
def set_ad(self, yen_ad):
    self.__ad = yen_ad
ogr = Ogrenc("Elf", "Kartal", "12345678", "000 000 00 00", "Yeditepe Üniversitesi")
(Çoktan Seçmel)
(A) ogr .ad
(B) ogr .soyad
(C) ogr .numara
(D) ogr .telefon
(E) ogr .adres
Cevap-10 :
ogr.ad


# 8. NUMPY VE PANDAS KÜTÜPHANELERİ İLE ÇALIŞMA

ÇALIŞMA

**Bölümle İlgl Özlü Söz**

Br programın en öneml özellğ, kullanıcısının amacını gerçekleştrp gerçekleştrmedğdr .
Tony (C.A.R.) Hoar e, Blgsayar Programcısı

**Kazanımlar**

1. NumPy kütüphanes le çok boyutlu dz ve matrslern oluşturulması, matematksel ve statstksel bazı hesaplamalar
gb temel ver şlemlern öğrenerek ver analz becerlern gelştrme fırsatı bulur .
2. pandas kütüphanes'ndek Sere'ler yardımı le verlern etketl br şeklde nasıl şlenebleceğ ve depolanableceğn
anlar .
3. pandas kütüphanes'ndek DataFrame'ler le tablo benzer ver yapılarını anlar ve DateFrame'lern oluşturulması ve
DataFrame'ler üzernde şlem yapma yeteneklern gelştrr . Vernn nasıl düzenleneceğ, brleştrleceğ vb. şlemler
detaylarıyla öğrenr .
4. Python le vernn farklı formatlarda (CSV , Excel vb.) nasıl kaydedlebleceğn öğrenerek vernn dosyaya yazılması
becerlern gelştrr . Aynı şeklde, pandas kütüphanes le farklı kaynaklardan (dosya, ver tabanı vb.) ver okuma
yetenekler kazanır .
5. loc[] ve loc[] sayesnde br DataFrame'de verye erşmdek esneklğ kavrar , vernn br bölümüne nasıl erşleceğn
ve spesfk hücrelern nasıl şlenebleceğn blr .
6. Yapılan karma örnekler sayesnde NumPy ve pandas kütüphaneler le çalışma konusunda pratk kazanır .

**Brlkte Düşünelm**

1. NumPy kütüphanesnn temel amacı nedr ve neden ver analz sürecnde sıkça terch edlr?
2. NumPy kütüphanes çnde çok boyutlu dzlern oluşturulmasının avantajları nelerdr?
3. E adında tek boyutlu 10 elemanı olan br NumPy dzs nasıl oluşturulablr?
4. pandas kütüphanesndek “Serler” (Seres) nedr ve nasıl oluşturulur?
5. Seres ver tpnde br A değşken brbrnden farklı ver türlern çereblr m?
6. DataFrame nedr ve br tabloyu nasıl temsl eder?
7. Gerçek br ver setn DataFrame olarak okuyup, ardından ver setnde satır/sütun bazında eleman çağırma şlem nasıl
gerçekleştrleblr?
8. Verlen br DataFrame'n br sütununa at değerler nasıl toplanablr?
9. pandas kütüphanesyle br .csv dosyasına nasıl ver yazılablr?
10. Br .csv dosyası br DataFrame olarak nasıl okunablr?
11. pandas kütüphanesyle br Excel dosyasına nasıl ver yazılablr?
12. Br .csv dosyası br DataFrame olarak nasıl okunablr?
13. loc[] ve loc[] nedr ve ne şe yarar? Aralarındak farklar nelerdr?


14. DataFrame çndek verlere loc[] ve loc[] kullanarak erşeblrsnz? Hang durumlarda hang ndeksleme yöntem
terch edlmeldr?

**Başlamadan Önce**

Günümüzde klask programlama blgsnn yanı sıra ver analzne lşkn becerlern kazanılması da oldukça önemldr .
Ver analz ve daha gelşmş yapay zekâ, makne öğrenmes ve ver madenclğ gb alanlarda ver okuma/yazma, ver
üzernde şlem yapma, ver analz çn vernn uygun formatta hazırlanması gb pek çok htyaç ortaya çıkmaktadır . İşte
ktabın bu bölümünde, özellkle ver analznde araştırmacılar tarafından sıkça kullanılan NumPy ve pandas
kütüphanelerne yer verlmştr .
Bu bölümde öncelkle NumPy  kütüphanes, bu kütüphanede yer alan NumPy dzler  (ndarray) ve bu dzlerle
gerçekleştrleblecek farklı şlemlere yer verlmştr . Ardından se pandas  kütüphanes ve pandas’ ta yer alan Seres ve
DataFrame gb k öneml ver yapısı anlatılmıştır . NumPy’da olduğu gb pandas’ ta da adı geçen ver yapılarına lşkn
öneml temel özellkler , eleman çağırma, vb. örneklere yer verlmştr . Özellkle DataFrame’ler ver analz konusunda
ön plana çıktığından, br ver set üzernde temel br ncelemenn nasıl yapılacağı konusunda açıklamalı örnekler
okuyucuya sunulmuştur . Bu bölümde yer alan her br konu başlığı, okuyucuların makne öğrenmes, ver madenclğ
gb ler düzey ver analz çeren konulara daha kolay geçş yapablmesn sağlamak çn okuyuculara sağlam br temel
oluşturmayı hedefler .

## 8.1. NumPy ve Pandas Kütüphanelernn Tanıtımı

NumPy  ve pandas , Python dlnde özellkle ver blm çalışmalarında sıkılıkla kullanılan kütüphanelerdendr . NumPy
(Num ercal Python), Python le çok boyutlu dzler saklamak ve şlemek çn etkl br yol sağlar ( https://numpy .org/)
(Harrs et al., 2020). NumPy , vektörlern, matrslern ve daha yüksek boyutlu ver setlernn verml br şeklde
depolanmasına ve şlenmesne zn veren br ndarray  yapısı sağlar . Ayrıca bast eleman bazında artmetkten daha
karmaşık doğrusal cebrsel şlemlere kadar bu verler üzernde çalışmak çn okunablr ve verml br sözdzm sağlar .
pandas se NumPy'dan çok daha yen br paket olup, aslında pandas üzerne nşa edlmştr ( https://pandas.pydata.or g/)
(McKnney , 2010; team, 2020). pandas, R ve benzer dllern kullanıcılarının aşna olduğu br DataFrame  nesnes
bçmnde çok boyutlu verlere yönelk etketl br arabrm sunmaktadır . İşte bu bölümde, her k kütüphanenn öneml
özellkler örnekler eşlğnde sunulmuştur . Daha fazla detaylı blg çn bknz. (Brownlee, 2016; Jeevan, 2022; McKnney ,
2012; VanderPlas, 2016e)

## 8.2. NumPy Kütüphanes

Eğer NumPy kütüphanes le çalışmak stenyorsa, tıpkı daha önce math, random ve os modüllernde yapıldığı gb mport
anahtar kelmes kullanılarak NumPy’ın çağrılması gerekmektedr . Aşağıdak kod yardımı le bu sağlanablr; ancak kod
satırını çalıştırıldığında hata alınablr .


Ekran görüntüsünden de anlaşılableceğ gb henüz maknenzde NumPy adlı br modül bulunmamaktadır . NumPy 3.
part modüller arasında yer almaktadır , Python dlnn standart kurulumu le gelmez. Bu nedenle de Wndows’ ta CMD
açılarak aşağıdak kodlar yardımı le NumPy kurulablr .
Ardından Spyder ekranına dönerek NumPy tekrar mport edlrse, bu kez lgl kod satırı düzgün çalışacaktır . NumPy
çalışmalarda sıklıkla kısa adı/takma adı np olarak çağrılır , bu nedenle bu bölümde de NumPy çn np terch edlmştr .
Tek boyutlu, çok boyutlu NumPy dzler araştırmacılar tarafından çokça terch edlen Python nesnelerndendr . Aşağıda
tam sayılardan oluşan br NumPy dzs yer almaktadır .
NumPy dzs tek br ver tpndek elemanları tutablmektedr . Üstün gelen ver tp dğerlern de kend ver tpne
dönüştürecektr . Örneğn; lk kod satırındak tüm elemanlar strng, knc satırdakler float olacaktır . Elemanların ver
tpnn yazılarak da dönüştürülmes söz konusudur . İlgl örneğe son satırda yer verlmştr . Elbette farklı ver tpler de
dtype parametresne verleblecektr . Bunun çn NumPy’a at detaylı dokümantasyon nceleneblr .
Br NumPy dzsnde elemanlar çeştl yollarla fltreleneblr . Örneğn; A’nın 50’ye eşt olan elemanları aşağıdak kod
satırları yardımı le bulunablr . np.where() fonksyonu le A==50 koşulunun sağlanması halnde (T rue dönen)
elemanların ndsler dönecektr . B br demet olarak tanımlanacaktır . np.asarray() fonksyonu yardımı le NumPy dzsne
dönüştürüleblr . A ve B’nn son halne lşkn ekran görüntüsü aşağıda verlmştr .
NumPy’da sayısal hesaplamalar çn bazı hazır formlar tanımlanmıştır . Aşağıda sırasıyla (1) sıfırlardan oluşan br dz, (2)
sıfırlardan oluşan 2x2’lk br matrs, (3) brlerden oluşan 2x3’lük br dz, (4) 3x3’lük brm dz, (5) 3x3’lük 10’lardan
oluşan br dz oluşturulmuştur . Fonksyonlara lk değer olarak verlen değern dz boyutu le lşkl olduğu görüleblr .
Bu gb tanımlamalar gerçekleştrlrken dtype le sayıların ver tp de belrleneblmektedr .


random modülünde olduğu gb NumPy le de rastgele değerler elde etmek ve sorasında yen br dz yaratmak
mümkündür . Aşağıdak kod bloğunda lk satırda verlen np.random.seed() fonksyonu çndek sayı üretlecek rastgele
sayıların br başlangıç değern belrler . Bu seed değer çn 1, 12, 123, 1000000 ya da farklı farklı değerler verleblr .
Dolayısıyla sürekl aynı rastgele değerlern elde edlmes stenrse bu seed değer değşmemeldr . İknc satırda yer alan
kod, rastgele sayılar kullanarak 3x3’lük br dz oluşturur . Son örnek se sayılarını normal dağılımdan alan 2x3’lük br
dz üretr .
np.empty() fonksyonu le o an bellekte bulunan sayılardan oluşan belrlenen boyutta br dz üretlr .
Aşağıda verlen lk örnekte, 3’e kadar sayılar rastgele seçlerek 10 elemanlı br a dzs oluşturulur . b ve c de benzer
şeklde yorumlanablr .


b dzs yenden ele alınırsa, dzlere has brtakım özellkler şu şeklde açıklanablr . ndm tahmn edleceğ üzere dznn
boyutunu, shape dznn boyutlarında yer alan eleman sayısını, sze toplamda kaç elemanlı olduğunu, dtype se dznn
elemanlarının ver tpn döndürür .
Lstelerdek elemanlara erşm ve br lstenn parçalara ayrılması şlemler NumPy dzler çn de geçerldr . Bunun çn
aşağıdak kod bloğu nceleneblr . A smnde yen br NumPy dzs tanımlanmıştır . A ekrana yazdırıldıktan sonra
sırasıyla,
(1) A’nın 0 ndekste bulunan lk elemanı: 50,
(2) A’nın 3. ndekste bulunan dördüncü elemanı: 200,
(3) A’nın son elemanı: 993,
(4) A’nın sondan 5. elemanı (unutulmamalıdır k sondan başlarken ndeks de -1’den başlamaktadır): 500,
(5) A’nın 0. ve 5. ndeks değerler arasındak elemanları (5 dâhl değl): array([ 50, 100, 107, 200, 207]),
(6) A’nın 5. ndeksten başlamak üzere dz sonuna kadar olan tüm elemanları: array([ 500, 1010, 2035, 88, 993]),
(7) A’nın tersten -5. ndeksten başlamak üzere dz sonuna kadar olan tüm elemanları: array([ 500, 1010, 2035, 88, 993]),
(8) – (9) A’nın 0. ndeksten başlayıp dz sonuna kadar her sefernde 5’er 5’er lerleyerek döndürdüğü elemanlar: array([
50, 500]) ,
(10) A dzsn ters çevrr: array([ 993, 88, 2035, 1010, 500, 207, 200, 107, 100, 50])


Bu şlemler tek boyutlu br dz üzernde gösterlmştr . Benzer düşünce yapısı 2, 3 ve çok boyutlu NumPy dzler çn de
düşünüleblr .
np.arange() le stenlen boyutta sayı dzler üretmek mümkündür . Örneğn; aşağıdak kod bloğunun başında tanımlanan
C, 1’den 15’e kadar (15 dâhl değl) olan sayıları çeren br NumPy dzsdr . Eleman seçm ve dzy bölme le lgl
kodlar ve ekran görüntüler aşağıda verlmştr .


Verlen br NumPy dzsnn boyutlarında yer alan eleman sayıları değştrleblr; ancak yen şeklnn toplamdak eleman
sayısı le uyumlu olması gerekmektedr . Aks halde hata mesajı döndürülecektr . Örneğn; 20 elemanlı br numpy dzs
ele alınsın. 2x10, 4x5, 5x4, 2 adet 5x2 ve 20x1 yen oluşturulacak dznn şekl çn uygun tanımlamalardır; ancak en son
kod satırı çalıştırıldığında hata mesajı döndürülecektr . Çünkü 2x2’lk br şekl, 20 elemanlı br dz çn uygun değldr .
Tüm ekran görüntüler aşağıda paylaşılmıştır .


Tanımlanan k NumPy dzs, eksenler boyunca brleştrleblmektedr . Örneğn; a ve b NumPy dzler ele alınsın.
Verlen lk örnekte tanımlanan a ve b dzs varsayılan bçmde x-eksen boyunca brleştrlmştr . Bu şlem çn
np.concatenate() fonksyonu kullanılmaktadır .
a ve b benzer bçmde y-eksen boyunca brleştrlmeye çalışırsa (axs=1) hata döndürülecektr; çünkü a ve b tek boyutlu
dzler olduğundan ancak yanana eklenebleceklerdr . Dğer seçenek 2 boyutlu dzlerde deneneblr .
Dğer eksen seçenekler le 2 ve daha fazla boyuttak dzler kullanılarak çalışılablr .


NumPy le çalışılırken, dzlern bölünmesne de zn verlmektedr . Bunun çn, np.splt() fonksyonu kullanılmaktadır .
Aşağıda verlen kod bloğunda 0-3 ndeksler arasındak elemanlar A1’de (3. İndeks dâhl değl), 3-5 ndeksler arasındak
elemanlar A2’de ve kalanlar da A3’te yer alacaktır .
NumPy dzsnn bölünmes gerçekleştrldkten sonra elde edlen A1, A2 ve A3 dzlernn ekran görüntüsü aşağıda
verlmştr .
Verlen br NumPy dzsnn transpozesn almak çn .T  kullanılmaktadır . Örneğn; aşağıda tanımlanan 2x5’lk A dzs
transpozes alındıktan sonra 5x2’lk hale dönüşmüştür .
np.vsplt() fonksyonu br NumPy dzsn dkey ( vertcal ), np.hsplt() fonksyonu se yatay ( horzontal ) bçmde bölmek
çn kullanılablr . Br öncek örnekte yer alan A NumPy dzs np.vsplt() ve np.hsplt() fonksyonları le sırasıyla
bölünmüştür . Bu fonksyonların döndürdüğü parçalar da a1, a2, a3 ve a4 olarak tanımlanmıştır .


NumPy dzler le temel matematksel şlemler yapablmek mümkündür . Aşağıda yer alan kod bloğu şu şeklde
nceleneblr:
np.arange() kullanılarak 20 elemanlı tanımlanmış olan a NumPy dzs çn aşağıda açıklamalı bçmde örnekler
sıralanmıştır . Öncelkle dz prnt() le ekrana yazdırılır .
a = [ 0 1 2 3 4 5 6 7 8 9 10 1 1 12 13 14 15 16 17 18 19]
Ardından sırasıyla gelen lk k satırda dznn tüm elemanlarına np.add() le 5 eklenmştr: array([ 5, 6, 7, 8, 9, 10, 1 1, 12,
13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]). Toplama çn operatör ve fonksyon le verlen örnek kullanım dğer
matematksel şlemler çn de mevcuttur (np.substract() gb).
Dznn tüm elemanlarından 5 çıkarılmıştır: array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1 1, 12, 13, 14]).
Dznn tüm elemanları 5’e bölünmüştür: array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 3.2,
3.4, 3.6, 3.8]).
// sembolü kullanılarak gerçekleştrlen bölme şlemnde sonuçlar en yakın tam sayıya yuvarlanarak verlmektedr:
array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3], dtype=nt32).
Br dznn ters şaretl haln bulmak çn -a ya da np.negatve() fonksyonu kullanılablr: array([ 0, -1, -2, -3, -4, -5, -6,
-7, -8, -9, -10, -1 1, -12, -13, -14, -15, -16, -17, -18, -19]).
Dzdek elemanların ters şaretlsnn mutlak değer np.abs() le bulunur: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1 1, 12, 13,
14, 15, 16, 17, 18, 19]).
Dz elemanlarının kuvvetn bulmak çnse np.pow() fonksyonu kullanılır array([ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
121, 144, 169, 196, 225, 256, 289, 324, 361], dtype=nt32).


Son örnekte se dz elemanlarının 2 tabanında eksponansyeln göstermektedr . Elemanların kare kökü se np.sqrt() le
bulunablmektedr .
Eksponansyel ve logartmk şlemler çn tanımlanmış çeştl fonksyonlar bulunmaktadır .
Ayrıca dz elemanlarının topluca değerlendrlmes gereken dznn mnmum (np.mn() = 0) ve maksmum (np.max() =
19) elemanlarının ve ndeks değerlernn (np.ar gmn() = 0, np.ar gmax() = 19) bulunması, elemanların toplanması
(np.sum() = 190), ortalamasının alınması (np.mean() = 9.5), ortanca değern elde edlmes (np.medan() = 9.5),
elemanların varyans (np.var() = 33.25) ve standart sapmalarının (np.std() = 5.766281297335398) hesaplanablmes çn
aşağıdak fonksyonlar kullanılablmektedr .
Br ondalıklı sayının vr gülden sonra kaç basamak yuvarlanacağı se np.round() fonksyonu yardımıyla elde edlr .
Aşağıdak kod satırları çalıştırıldığında sırasıyla 3.797 le 3.8 değerler bulunur .
Örneğn; a dzsnn sıfırdan farklı elemanlarının sayısını hesaplamak çn klask programlama mantığı le
düşünüldüğünde aşağıdak gb br çözüm getrleblr . Sıfırdan farklı elemanların sayısını tutacak br say değşken
tanımlanır . Ardından , a dzsnn elemanlarını dolaşacak şeklde, eğer  != 0 koşulu sağlanırsa her terasyonda say
değşkenne 1 eklenr . Böylelkle kod bloğunun sonunda ekrana 19 yazdırılır .
Yukarıdak kod bloğu yerne aynı görev yapmak çn np.count_nonzero() fonksyonu kullanılablr .
Br başka örnek olarak, a dzsnn 5’ ten büyük elemanlarının toplamını bulmak düşünülsün. Bu örnek çn de
yukarıdakne benzer klask programlama mantığı le br çözüm gelştrleblr . Elemanların toplamını tutacak br toplam
değşken tanımlanması le kodlamaya başlanır . Ardından , a dzsnn elemanlarını dolaşacak şeklde, eğer  > 5 koşulu


sağlanırsa her terasyonda toplam değşkenne ’nn o terasyondak değer eklenr . Böylelkle kod bloğunun sonunda
ekrana 175 yazdırılır .
Oysa, Python le aynı örnek tek satırda çözüleblr . Bunun çn aşağıdak kod satırı kullanılablr .
Verlen kod satırımı çten dışa doğru okuyacak olursak a > 5 boolean br fade döndürür , yan a dzsnn elemanlarından
5’ten büyükler çn True, küçük eşt olanlar çnse False.
a[a > 5] se a dzsnn köşel parantezler çnde yer almakta olan boolean fadeden True dönen elemanlarını
döndürecektr .
Son olarak np.sum(a[a > 5]) çalıştırıldığında 175 döndürülür .
Aşağıda a dzsnn boolean fadeler le kullanıldığı farklı örneklere yer verlmştr . İlk örnekte, a dzsnn 10’dan küçük
olan elemanlarının toplamı 45 elde edlr . Brleşk mantıksal fadeler kullanılarak da br dz fltreleneblr . Aynı anda hem
(a > 5), hem de (a < 10) koşulunu sağlayan a dzs elemanlarının toplamı 30’dur . Altındak örnekte se (a > 5) & (a < 10)
koşulunun tersne örnek verlr (~ ((a > 5) & (a < 10))). Tersn alınması demek True’ların False, False’ların se True
olması demektr . Bunun çn ~ smges kullanılmıştır .
Son k örnek se daha öncek bölümlerde yer verlen any() ve all() fonksyonları le benzerlk gösterr . np.any()
fonksyonu le eğer a dzsnn herhang br elemanı 100’den küçük se True, aks halde False döner . np.all() fonksyonu
le eğer a dzsnn tüm elemanları 100’den büyük se True, aks halde False döner . Verlen bu örnek çn a dzsnn tüm
elemanları (en az br koşulu sağlanır) 100’den küçüktür . Bu nedenle True döner . En sondak kod satırında se a dzsnn
elemanlarının hçbr 100’den büyük olmadığından False döner .


a dzsndek elemanların sıralanması da öncek bölümlerde verlen örneklere benzer şekldedr; yalnızca kullanılan
fonksyon NumPy kütüphanesnden çağrılmaktadır . np.random.randnt() fonksyonu le 0-30 arasındak sayılar
kullanılarak (30 dâhl değl) 30 adet tamsayı elemanı olan dz adlı br NumPy dzs tanımlanıyor ve prnt() le ekrana
yazdırılıyor . Ardından, np.sort() fonksyonu le dz varsayılan olarak artan düzende sıralanıyor; ancak bu orjnal dznn
kendsnde herhang br değşklk yaratmamaktadır . Oysa, dz.sort() kod satırı çalıştırılırsa, artık dz artan sırada
sıralanmış br dz olacaktır . Aşağıda lgl ekran görüntüler paylaşılmıştır .

## 8.3. pandas Kütüphanes - Seres

pandas kütüphanes NumPy gb 3. part br modüldür ve mevcut Python modüller le blgsayara yüklenmemektedr . Bu
nedenle de Wndows’ ta CMD komut ekranına yazılan aşağıdak kod satırı yardımıyla pandas kütüphanes yüklenr .
Bu bölümün başında da belrtldğ gb pandas kütüphanes Seres de pandas le gelen ver yapıları arasındadır , tek
boyutlu etketl özel br dzdr . Ayrıca DataFrame adı verlen oldukça kullanışlı br ver yapısı sunmaktadır . Aşağıda kod
dosyasına hem NumPy hem de pandas modüllernn çağrılmasıyla başlanmıştır . NumPy’ın np şeklnde kısa adı le
çağrılması gb pandas çn kullanılan yaygın takma ad pd’dr . Dolayısıyla, bu tanımlama yapıldıktan sonra pandas
çnden çağrılacak her türlü unsur çn pd. kısaltması kullanılmalıdır . NumPy ve pandas modüller çağrıldıktan sonra a
adlı, tamsayı ver tpnde br pandas sers tanımlanmıştır . a tanımlanırken ndex parametresne de 0’dan 8’e kadar (8 dâhl
değl) değer atanmıştır .


a sersnn k öneml özellğ bulunmaktadır . İlk elemanların ndeks değerler, kncs se elemanların değerlerdr .
Aşağıda br sernn elemanlarını çağırmak çn kullanılan kod satırları yer almaktadır .
a[0], 0. ndekste bulunan elemanı döndürür: 2
a[3], 3. ndekste bulunan elemanı döndürür: 7
a[1:3], 1.’den 3. ndekste bulunan elemana kadar olan değerler döndürür . 3. İndekstek eleman dâhl edlmez.
a[0:5], 0’dan 5. ndekste bulunan elemana kadar olan değerler döndürür . 5. ndekstek eleman dâhl edlmez.
a[5:], 5. ndekste yer alan elemandan sernn sonunda bulunan elemana kadar tüm elemanları döndürür .
a[:-1], sernn başından sonuncu elemana kadar (-1. ndekste bulunan eleman) tüm elemanları döndürür , son eleman dâhl
edlmez.


a[-1:], sernn son elemanını ndeks değer le döndürür .
a[0:5:2], 0. ndeksten 5. ndekse kadar 2’şer ndeks lerleyerek elemanları döndürür .
a[::5] ve a[0:a.sze:5] aynı şlem yapar . Sernn başından sonuna kadar 5’er ndeks lerleyerek elemanları döndürür .
a[::-1], sernn tersten yazdırılmasını sağlar .
Her zaman br sernn ndeks değerler sayısal olmak zorunda değldr . Metnsel br fade de olablr .
Eğer br sözlükten ser oluşturulmak stenrse aşağıdak kod satırları kullanılablr .
Br serye ve sernn ndeks değerlerne brer ad tanımlanablr .


Sernn elemanlarının değer değşeblr; ancak ndeks değerler değştrlemezdr . İndeks değernn değştrlmes stenrse
hata mesajı döndürülür .
Br sernn elemanları farklı ver tpnde olablr . Aşağıdak örnekte e sersnn lk elemanı tam sayı (nt), knc
elemanının metnsel br fade (str), son elemanının se bool olduğu görüleblr .

## 8.4. pandas Kütüphanes – DataFrame

DataFrame, pandas kütüphanesnde tanımlanan k boyutlu özel br dz türüdür . Aşağıda takmaAd, cns ve renk
sütunlarından oluşan k satırlık br DataFrame tanımlanmıştır . DataFrame’n satırlarına değerler pd.concat() fonksyonu


le atanmıştır .
Aşağıda da öncelkle stock adında br sözlük tanımlanmıştır . Sonrasında pd.DataFrame() kullanılarak DataFrame’e
çevrlmştr . Br DataFrame’n sütunlarına ve hücrelernde yer alan elemanlara ulaşmak çn farklı yollar kullanılablr .
Örneğn; dataframeadı[“sütunadı”] ve dataframeadı.sütunadı şeklnde çağrılablr . Br DataFrame’n sütunlarına erşme ve
hücredek değerler çağırma konusunda temel brkaç örneğe aşağıda yer verlmştr .
DataFrame’e yen br sütun eklemek çn aşağıdak kod satırı kullanılablr . Aşağıda da görüleceğ gb DataFrame’n
halhazırda 4 satırı olduğundan yen eklenecek sütunun da 4 satırdan oluşması beklenr . Eğer satır sayıları uyuşmazsa hata
mesajı döndürülecektr . Serlerdekne benzer şeklde br DataFrame’n ndeksne ve sütunlarına brer ad verleblr .


ver DataFrame’ndek değerler görmek çn values özellğnden yararlanılablr . Ayrıca .T  le br DataFrame’n
transpozes alınablr .
Br DataFrame’n ndeks değerler, sütun değerler ya da sütun adları arasında herhang br değern olup olmadığı
aşağıdak kod satırları le kontrol edleblr . Aşağıdak kod satırları sırasıyla False, True, True, False, False, True döndürür .
Br DataFrame’n ndeks değerler değştrleblr ve farklı ndeks değerne göre DataFrame yazdırılablr . Bu yen düzen
yenden atama yapılmadığı sürece satırların sırasını yalnızca raporlamada değştrecektr .

## 8.5. Dosya Okuma

Bu bölümde farklı dosya formatlarını okuma üzerne üç farklı örneğe yer verlmştr .


Örnek 1:  Br .csv dosyasından ver okuma.
Örnek olarak kullanılacak ver set .csv formatında https://data.mendeley .com/publc-
fles/datasets/4r3cvfk6g4/fles/794232f3-f f14-40d9-a4e6-7140b29eecb7/fle_downloaded  bağlantsında bulunmaktadır .
Öncelkle “Irs” ver set ndrlerek çalışma klasörüne kopyalansın (Snghal, 2017). Very okumak çn pandas-tan
read_csv() fonksyonu kullanılacaktır . Kodların yazıldığı Python betk dosyasının ve ver setnn çalışma klasöründe
olması durumunda, very okuyacak olan pd.read_csv() fonksyonuna dosya yolu eklenmesne gerek kalmayacaktır .
Aşağıda verldğ gb yalnızca ver dosyası adının yazılması yeterl olacaktır .
Br DataFrame’den br sütunun ya da sütunların çıkarılması stenrse aşağıdak kod satırları terch edleblr . Alternatf
yollar da aşağıda sıralanmıştır .
Örnek 2:  Br Excel dosyasından ver okuma.
pandas le br Excel dosyası okunablmes çn eğer yüklü değlse openpyxl modülü yüklenmeldr (CMD ekranından pp
nstall openpyxl). Br öncek örnekte .xlsx uzantısı le ndrlen ver set Excel formatında yne aynı dosya konumuna
kaydedlsn. Sonrasında, aşağıdak kod satırları yardımı le ver set okunablr . Bu örnekte usecols parametres le ver
okunurken lk sütun harç dğer sütunlar alınmıştır .


Örnek 3:  İnternettek br dosyadan ver okuma.
İnternette yer alan br ver dosyasını okumak çn vernn yer aldığı bağlantı (URL= https://data.mendeley .com/publc-
fles/datasets/4r3cvfk6g4/fles/794232f3-f f14-40d9-a4e6-7140b29eecb7/fle_downloaded ) gerekldr . Eğer yüklü değlse
requests modülü yüklenmel (CMD ekranından pp nstall requests) ve çağrılmalıdır . Sonrasında lgl bağlantıda yer alan
rs ver setnn okunması çn aşağıdak kod satırları kullanılablr . Br öncek örnekte olduğu gb usecols parametres le
ver okunurken lk sütun harç dğer sütunlar alınmıştır .

## 8.6. Dosyaya Yazma

Br öncek bölümde üzernde çalışılan ver DataFrame’ .csv dosyası olarak kaydedlmek stenrse .to_csv() fonksyonu
kullanılablr . encodng parametres çn verlen değer (utf-8-sg), .csv dosyasında meydana geleblecek olası Türkçe
karakter sorununun ortadan kaldırılablmes çndr . Benzer kod satırı br Excel dosyasına ver yazmak çn de geçerldr;
ancak bu kez kullanılması gereken fonksyon .to_excel() olacaktır .


## 8.7. Br  DataFrame le Temel İşlemler

rs ver set okunduğunda Spyder edtöründe Varable Explor er panelndek rs nesnesne çft tıklanırsa, ver aşağıdak
bçmde görüleblecektr . Ver set rs ççeğne lşkn çanak ve taç yaprak uzunluk ve genşlğ le türlern çeren beş
farklı değşken tutmaktadır . Okunduğu hal le değşken adları/sütun adlarının İnglzces (SepalLengthCm,
SepalWdthCm, PetalLengthCm, PetalWdthCm, Speces) mevcuttur .
Sütun adlarının öncelkle lstelenmes, sonra da değştrleblmes çn aşağıdak kod satırları kullanılmaktadır . Ardından
sütun adları yenden lstelendğnde sütun adlarının değştrldğ görüleblecektr .
Ver setndek ndeks değerler değştrleblr . 150 satırdan oluşan ver setnde varsayılan ndeks değerler 0’dan 149’a
kadar olan sayılardır . Bunun yerne I1, I2, …, I150 şeklnde br dz atayablmek çn aşağıdak kod bloğu kullanılablr .


Önce lgl ndeks dzs for döngüsü yardımı le oluşturulmuş, ardından da rs çn ndeks değerler yerne atanmıştır .
Bu şlem sonrasında ver setnn lk 5 satırını döndürmek çn DataFrame’n head() fonksyonu kullanılır . Parametre
olarak baştan kaç satır döndürüleceğ blgsn almaktadır . tal() fonksyonu se tahn edleceğ gb ver setnn sondan 7
satırını döndürür .
nfo() fonksyonu le DataFrame’n özet blgs elde edleblr . Buna göre, rs ver setnn satır ve sütun sayısı, ndeks
değerler sütunların ver tp ve eksk değer çerp çermedğ görüleblr . Sütunların ver tp .dtypes le de lsteleneblr .
İlgl kodlar ve ekran görüntüler aşağıda verlmştr .
.shape, .sze ve .ndm se sırasıyla satır ve sütun boyutlarını (150, 5), eleman sayısını (750) ve DataFrame’n boyutunu (2)
döndürür .
Eğer herhang br sütunda yer alan değerler değştrlmek stenyorsa aşağıdak kod bloğu kullanılablr . Bunun çn rs
ver setndek tur sütunu ele alınsın. " Irs-setosa ", "Irs-verscolor ", "Irs-vr gnca " olan kategorler sırasıyla " setosa ",
"verscolor ", "vrgnca " olacak şeklde değştrlmştr . İlgl kod satırının öncesnde ve sonrasında kategorlere at
frekans dağılımlarını bulmak mümkündür .


Ver setne lşkn br başka özet tablo se .descrbe() foksyonu le elde edlr . Bu özet daha çok temel açıklayıcı brtakım
statstk blglerden oluşur . Aşağıdak kod satırı çalıştırıldığında ekran görüntüsünden nceleneblecek olan sayısal
sütunların sayısı (count), ortalaması (mean), standart sapması (std), mnmum (mn) ve maksmumu (max) le 1., 2. ve 3.
kartl değerler (sırasıyla 25%, 50%, 75%) elde edlr . Br nesne (object) ver tpnde gözüken tur sütununun da özet
tabloda yer alablmes çn descrbe() fonksyonu nclude=”all” parametres le kullanılmalıdır . Son halde özet tabloya tur
sütunundak tekl değer/kategor sayısı (unque), frekans dağılımı en fazla olan kategornn adı (top) ve sayısı (freq) da
eklenr . Eklenen bu yen blgler sayısal sütunlar çn hesaplanmaz.

## 8.8. DataFrame le loc[] ve loc[] Kullanımı

Br DataFrame’n satır ve sütun şlemlern gerçekleştrrken loc[] ve loc[] kullanılablmektedr . İk fadenn
benzerlklernn yanı sıra farklılıkları da mevcuttur (sparkbyexamples.com, 2023): loc[] br DataFrame’den ver seçlrken
etket tabanlı şlem gerçekleştrmektedr . Seçlmek stenen satır veya sütunun adının letlmes gerekmektedr . loc[]
kullanılırken loc[]'tan farklı olarak, çnde belrtlen aralığın son öğesn de çerr . Ayrıca yne loc[], loc[]'tan farklı
olarak boolean vers kabul eder . loc[] br DataFrame’den ver seçlrken ndeks tabanlı şlem gerçekleştrmektedr .
Seçlmek stenen satır veya sütunun tamsayı şeklnde fade edlmes gerekr . Bu yöntem, loc[] aksne, çnde belrtlen
aralığın son öğesn çermez, boolean vers kabul etmez.
İşlem loc loc
Tek satır seçmek rs.loc[“E2”] rs.loc[1]
Tek sütun seçmek rs.loc[: , “canakUz”] rs.loc[: , 0]
Çoklu satır seçmek rs.loc[[“I2”, “I3”]] rs.loc[[1 , 2]]
Çoklu sütun seçmek rs.loc[: , [“canakUz”, “tacGen”] ] rs.loc[:, [0 , 3]]
Belrl br aralıktak satırları seçmek rs.loc[“I1” : “I3”] rs.loc[0 : 3]


Belrl br aralıktak sütunları seçmek rs.loc[: , “canakUz” : “tacGen”] rs.loc[ : , 0 : 4]
Farklı satırları seçmek rs.loc[“I1” : “I7”: 2] rs.loc[0 : 8 : 2]
Farklı sütunları seçmek rs.loc[:, "canakUz" : "tacGen" : 2] rs.loc[:, 0 : 4 : 2]
Koşul le kullanım rs.loc[ rs[“tacUz”] > 3.2 ] rs.loc[lst(rs[“tacUz”]>3.2)]
Aşağıdak komut satırları I6 ndeks numarasına sahp satırı döndürür .
Aşağıdak komut satırları çalıştırıldığında; I1, I2 ve I5 ndeks numaralı satırlar döndürülür .
Aşağıdak komut satırları çalıştırıldığında; tur sütunu döndürülür .
Aşağıdak komut satırları çalıştırıldığında; I6, I7, …, I15 satırları döndürülür .
Aşağıdak komut satırları çalıştırıldığında; I6 ndeks numaralı satırın taç yaprak uzunluğu (tacUz) döndürülür .
Aşağıdak komut satırları çalıştırıldığında; çanak yaprak genşlğ (canakGen) le tur sütunları döndürülür .
Aşağıdak komut satırları çalıştırıldığında; I1, I2, …, I5 ndeks numaralı satırların çanak yaprak genşlğ (canakGen), tac
yaprak uzunluğu (tacUz) ve taç yaprak genşlğ (tacGen) değerler döndürülür .
Aşağıdak komut satırları çalıştırıldığında; ver setndek lk 5 satır döndürülür .
Aşağıdak komut satırları çalıştırıldığında; ver setndek son 5 satır harç I1, I2, …, I145 döndürülür .
Ayrıca çeştl koşullar yardımı le daha spesfk özellktek satır/sütun şlemler gerçekleştrleblr .
Örnek 1:  Aşağıda taç yaprak uzunluğu (tacUz) 1.5’ ten küçük olan satırlar lstelenmştr . loc[] ve loc[] kullanım farkına
dkkat edlmeldr . Satırların ks de aynı lstey döndürecektr .


Örnek 2:  Aşağıda çanak yaprak uzunluğu (canakUz) 7’den büyük ve çanak yaprak genşlğ (canakGen) küçük olan
satırlar lstelenmştr . Bu örnekte de loc[] ve loc[] kullanım farkına dkkat edlmeldr . Satırların ks de aynı lstey
döndürecektr .
Örnek 3:  Aşağıda türü (tur) “setosa” olan veya çanak yaprak genşlğ (canGen) 4’ ten büyük olan satırların uzunluğu
sırası le a ve b değşkenlerne atanmıştır . Sonuçta her k değşkenn değer de 50 olur .
Örnek 4:  Aşağıda verlen örnekte farklı fltreler uygulanarak A, B ve C adında 3 yen DataFrame oluşturulmuştur . Bu
DataFrame’lern satır ve sütunlarının boyutu .shape le lstelenmştr .
Ardından pd.concat() fonksyonu yardımı le A, B, C alt alta gelecek şeklde (yatay) brleştrlmştr . axs parametres 0
değern almıştır . Son durumda D, 15 satır ve 3 sütundan oluşmaktadır .
Sonrasında aşağıdak satır yardımı le D’nn satır sayısı kadar rastgele sayı üretlmştr ve bunlar br pandas sers şeklnde
D’nn olcum1 sütunu olarak (yen br sütun olarak) D’ye atanmıştır .
Yen br sütun ataması şlem pd.concat le de gerçekleştrleblr . Aşağıda D’nn satır sayısı kadar rastgele sayılarla a adlı
br pandas sers tanımlanmıştır . pd.concat() fonksyonunun axs parametres 1 alınarak aD2’nn son sütunu olarak
atanmıştır . Atama sırasında DataFrame’n sütun adı olarak olcum2 olması terch edlmştr . D’nn son halne lşkn
Spyder edtöründek “V arable Explorer” panelnden alınan ekran görüntüsü aşağıda paylaşılmıştır .


Örnek 5: DDataFrame’nde tur sütununun ver tp object yerne kategor ( category ) olarak da belrleneblr . Bunun çn
aşağıdak kod satırı çalıştırılmalıdır . İlgl sütun çağrıldıktan sonra sütuna .astype(“category”) denlerek bu sağlanır .
Sonrasında D.dtypes le ver tp kontrol edldğnde ver tpnn kategor olarak değştğ görüleblr . Kategor ver
tpndek br değşkenn kategorlern görmek çn sütun çağrıldıktan sonra .cat.categores deymnden faydalanılır . Bu
yolla kategor adları .cat.rename_categores() fonksyonu le sağlanır . Parametre olarak sütuna yen kategor adlarının
verlmes gerekmektedr .

**Bölüm Özet**

Bu bölümde, Python dln özellkle ver blm le uğraşan araştırmacıların kullandığı, ver le lgl şlemlerde güçlü
araçlar sunan NumPy  ve pandas  kütüphanelerne odaklanılmıştır . İlk olarak, NumPy  kütüphanesyle başlayarak, çok
boyutlu dzlern oluşturulması, matematksel şlemler ve ver analz çn sağladığı temel yetenekler detaylandırılmıştır .
Ardından, pandas  kütüphanesne geçlerek, pandas  kütüphanesnn sunduğu Sere ve DataFrame le nesnelern nasıl
oluşturulacağı ve vernn nasıl etkl br şeklde şlenebleceğ ncelenmştr . DataFrame konusunda, tablo benzer ver
yapılarının nasıl oluşturulup, bu yapılar le çalışılableceğ gösterlmştr . Vernn .csv veya Excel  gb formatlarda nasıl
kaydedlebleceğ le bu ve benzer dosya formatlarından (ver kaynaklarından) nasıl okunableceğ ele alınmıştır . Temel
şlemler kısmında, DataFrame çndek vernn fltrelenmes, brleştrlmes gb şlemler detaylı örneklerle anlatılırken,
loc[] ve loc[] yöntemleryle verlere nasıl erşleceğ ve şleneceğ açıklanmıştır .

**Kaynakça**

Amos, D. (2018). Object-Orented Pr ogrammng (OOP) n Python 3 . https://realpython.com/python3-object-orented-
programmng/
Breuss, M. (2017). Python V rtual Envr onments: A Prmer . RealPython. https://realpython.com/python-vrtual-
envronments-a-prmer/
Brownlee, J. (2016, May 10). How To Load Machne Learnng Data n Python. MachneLearnngMastery .Com .
https://machnelearnngmastery .com/load-machne-learnng-data-python/
Bureau, I. (2019). Dffer ence between Compler and Interpr eter. Busness Insder .
https://www .busnessnsder .n/df ference-between-compler -and-nterpreter/artcleshow/69523408.cms
Çobanoğlu, B. (2021). Herkes İçn Python  (3rd ed.). Pusula 20 Teknoloj ve Yayıncılık A.Ş.
Costa, C. D. (2020, November 23). Top 16 Python Applcatons n Real-W orld. Medum.
https://towardsdatascence.com/top-16-python-applcatons-n-real-world-a04041 11ac23
Detel, H. M., & Detel, P . J. (2010). C ve C++  (M. Zavrak, E. Aksoy , & H. N. Karaca, Trans.; 3rd ed.). Sstem
Yayıncılık.


GeeksforGeeks. (2016, May 16). Python OOPs Concepts. GeeksforGeeks . https://www .geeksfor geeks.or g/python-oops-
concepts/
GeeksforGeeks. (2020, January 18). How to Install PIP  on Wndows ? GeeksforGeeks .
https://www .geeksfor geeks.or g/how-to-nstall-pp-on-wndows/
geeksfor geeks.or g. (2020). Memory Management n Python . https://www .geeksfor geeks.or g/memory-management-n-
python/
geeksfor geeks.or g. (2021, October 22). Top 10 Python Applcatons n Real World. GeeksforGeeks .
https://www .geeksfor geeks.or g/top-10-python-applcatons-n-real-world/
Gupta, A. (2023). Top 10 Python IDEs n 2023: Choosng The Best One . Smpllearn.Com.
https://www .smpllearn.com/tutorals/python-tutoral/python-de
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E., Taylor , J., Ber g,
S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A., Río, J. F . del, Webe, M.,
Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e, 585(7825), 357–362.
https://do.or g/10.1038/s41586-020-2649-2
Hjelle, G. A. (2020). Python mport: Advanced T echnques and T ps. https://realpython.com/python-mport/
python.or g. (2023). Makng kernels for IPython—IPython 3.2.1 documentaton . https://python.or g/python-
doc/3/development/kernels.html
Jeevan, M. (2022). How to Select Rows and Columns n Pandas Usng [ ], .loc, loc, .at and .at . KDnuggets.
https://www .kdnuggets.com/how-to-select-rows-and-columns-n-pandas-usng-loc-loc-at-and-at.html
Jones, L. (2019). Ponters n Python: What’ s the Pont? – Real Python . https://realpython.com/ponters-n-python/
Kodan, K. (2021, July 15). Dffer ence Between Python Modules, Packages, Lbrares, and Frameworks .
LearnPython.Com. https://learnpython.com/blog/python-modules-packages-lbrares-frameworks/
Lutz, M. (2009). Learnng Python  (4th ed.). O’Relly Meda.
Lutz, M. (201 1). Programmng Python  (4th ed.). O’Relly . https://www .orelly .com/lbrary/vew/programmng-python-
second/0596000855/ch01s02.html
Mathew , S. T. (2021). Python Fundamentals for Everybody—T ype Converson vs T ype Coer con.
https://medum.com/analytcs-vdhya/python-fundamentals-for -everybody-type-converson-vs-type-coercon-
34234e99c9c4
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. In S. van der Walt & J. Mllman (Eds.),
Proceedngs of the 9th Python n Scence Confer ence (pp. 56–61). https://do.or g/10.25080/Majora-92bf1922-00a
McKnney , W. (2012). Python for Data Analyss: Data W ranglng wth Pandas, NumPy , and IPython  (1st ed.). O’Relly
Meda.
Mcrosoft. (2022). How to cr eate and manage Python envr onments n V sual Studo . https://learn.mcrosoft.com/en-
us/vsualstudo/python/managng-python-envronments-n-vsual-studo?vew=vs-2022
Panwar , P. (2022). Use exstng Python packages wth Spyder 5 . https://puneetpanwar .com/use-exstng-packages-
spyder5/
Pérez, F ., & Granger , B. E. (2007). IPython: A System for Interactve Scentfc Computng. Computng n Scence and
Engneerng , 9(3), 21–29. https://do.or g/10.1 109/MCSE.2007.53
Pozo Ramos, L. (2023). Python’ s del: Remove Refer ences Fr om Scopes and Contaners . https://realpython.com/python-
del-statement/
programz.com. (2023). Python Object Orented Pr ogrammng . https://www .programz.com/python-programmng/object-
orented-programmng
pynstaller .org. (2023). PyInstaller Manual—PyInstaller 5.8.0 documentaton . https://pynstaller .org/en/stable/
Python Software Foundaton. (2023a). IDLE . Python Documentaton. https://docs.python.or g/3/lbrary/dle.html


Python Software Foundaton. (2023b). Python a pr ogrammng language changes the world Fnal Pr oducton Content
Case Studes & Success Stores . https://brochure.getpython.nfo/meda/releases/prerelases/psf-python-brochure-vol-1-
fnal-content-prevew
Python.or g. (2023a, February 15). Free Python T utoral For Begnners: Learn Python . Python Land.
https://python.land/python-tutoral
Python.or g. (2023b, February 15). Welcome to Python.or g. Python.Or g. https://www .python.or g/
Sawant, S. (2021, February 17). Semcolon n Python—AskPython . https://www .askpython.com/python/semcolon-n-
python
Snghal, B. (2017). Irs Dataset . Mendeley Data, V1. https://data.mendeley .com/datasets/4r3cvfk6g4/1
sparkbyexamples.com. (2023). Pandas Dffer ence Between loc[] vs loc[] . Sparkbyexamples.Com.
https://sparkbyexamples.com/pandas/pandas-df ference-between-loc-vs-loc-n-dataframe/?expand_artcle=1
spyder -de.or g. (2022). Home—Spyder IDE . https://www .spyder -de.or g/
Statsta. (2022). Most used languages among softwar e developers globally 2022 . Statsta.
https://www .statsta.com/statstcs/793628/worldwde-developer -survey-most-used-languages/
team, T. pandas development. (2020). pandas-dev/pandas: Pandas  (latest) [Computer software]. Zenodo.
https://do.or g/10.5281/zenodo.3509134
Uğuz, S. (2021). Makne Öğr enmes: T eork Yönler ve Pyhton Uygulamaları İle Br Y apay Zeka Ekolü  (2nd ed.). Nobel
Akademk Yayıncılık.
Uzun, E. (2023). Temel Operatörler . https://erdncuzun.com/python/4-temel-operatorler/
VanderPlas, J. (2016a). Basc Python Semantcs: Varables and Objects. In Whrlwnd T our of Python . O’Relly Meda,
Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816//Index.pynb
VanderPlas, J. (2016b). Bult-In Data Structures. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/06-Bult-n-
Data-Structures.pynb
VanderPlas, J. (2016c). Defnng and Usng Functons. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/08-Defnng-
Functons.pynb
VanderPlas, J. (2016d). Iterators. In Whrlwnd T our of Python . O’Relly Meda, Inc.
https://gthub.com/jakevdp/WhrlwndT ourOfPython/blob/6f1daf714fe52a8dde6a288674ba46a7feed8816/10-
Iterators.pynb
VanderPlas, J. (2016e). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.). O’Relly Meda.
VanTol, A. (2019). Memory Management n Python – Real Python . https://realpython.com/python-memory-management/
vegbt. (2023). Type Coer con Vs T ype Castng In Python . https://vegbt.com/type-coercon-vs-type-castng-n-python/
w3schools.com. (2023). W3schools.com . https://www .w3schools.com/python/gloss_python_escape_characters.asp
wk.python.or g. (2023a). Begnners Gude/Overvew—Python W k.
https://wk.python.or g/mon/BegnnersGude/Overvew
wk.python.or g. (2023b). Python Implementatons . https://wk.python.or g/mon/PythonImplementatons

**Ünte Soruları**

Soru-1 :


dz adında br NumPy dzs şöyle verlmektedr .
Buna göre aşağıdak seçeneklerden hangsnde np.mn(dz[1:8:3]) şlemnn sonucu doğru br şeklde verlmektedr?
(Çoktan Seçmel)
(A) array([0.6 , 0.03, 0.49, 0.56, 0.09, 0.2 , 0.36])
(B) array([0.6 , 0.56, 0.36])
(C) 0.03
(D) 0.36
(E) 0.9
Cevap-1 :
0.36
Soru-2 :
dz adında br NumPy dzs şöyle verlmektedr .
Buna göre, array([0.03, 0.49, 0.56])  ekran görüntüsünü elde edeblmek çn aşağıdak seçeneklerden hangs
kullanılmalıdır?
(Çoktan Seçmel)
(A) dz[2:5]
(B) dz[2:4]
(C) dz[3:4]
(D) dz[1:4]
Cevap-2 :
dz[2:5]
Soru-3 :
Aşağıdak kod bloğu le aynı görev yapan seçenek hangsdr?
(Çoktan Seçmel)
(A) lst=np.negatve(lst)


(B) lst=lst(np.negatve(lst))
(C) lst=lst(np.any(lst))
(D) lst=lst(np.all(lst))
(E) lst=np.sort(lst)
Cevap-3 :
lst=lst(np.negatve(lst))
Soru-4 :
dz adında br NumPy dzs şöyle verlmektedr .
Buna göre, (0.7, 0.9) aralığındak sayıların toplamının elde edlmes çn gerekl olan kod satırı hang seçenekte doğru br
bçmde fade edlmştr?
(Çoktan Seçmel)
(A) np.sum(dz[(dz >= 0.7) & (dz <= 0.9)])
(B) np.total(dz[(dz > 0.7) & (dz < 0.9)])
(C) np.sum(dz[(dz > 0.7) & (dz < 0.9)])
(D) np.total(dz[(dz > 0.7) %&% (dz < 0.9)])
(E) np.sum(dz[(dz > 0.7) , (dz < 0.9)])
Cevap-4 :
np.sum(dz[(dz > 0.7) & (dz < 0.9)])
Soru-5 :
pandas’ ta br DataFrame oluşturmak çn hang seçenek kullanılablr?
(Çoktan Seçmel)
(A) pd.create_df()
(B) pd.DataFrame()
(C) pd.make_df()
(D) pd.new_df()
(E) pd.def_df()
Cevap-5 :
pd.DataFrame()
Soru-6 :
pandas'da verler br DataFrame'den belrl br sütuna göre nasıl seçeblrsnz?


(Çoktan Seçmel)
(A) df.select_column()
(B) df.get_column()
(C) df.extract("sütun_adı")
(D) df.select("sütun_adı")
(E) df["sütun_adı"]
Cevap-6 :
df["sütun_adı"]
Soru-7 :
Br ver.csv adlı .CSV  dosyası pandas le br DataFrame'e kaydedlmek stenyor . Bunun çn aşağıdak seçeneklerden
hangs kullanılablr?
(Çoktan Seçmel)
(A) df = pd.read_csv("ver.csv")
(B) df = pd.load("ver.csv")
(C) df = pd.read_excel("ver.csv")
(D) df = pd.mport_fle("ver.csv")
(E) df = pd.create_dataframe("ver.csv")
Cevap-7 :
df = pd.read_csv("ver.csv")
Soru-8 :
Aşağıdaklerden hangs ya da hangler pandas’a özgü ver yapılarındandır?
(Çoktan Seçmel)
(A) DataFrames
(B) DataFrames, Seres ve Tuples
(C) Seres ve Dctonares
(D) DataFrames ve Seres
(E) Tuples, Seres ve Dctonares
Cevap-8 :
DataFrames ve Seres
Soru-9 :
Br DataFrame’n lk ve son satırlarını döndüreblmek çn aşağıdak seçeneklerde verlen hang k fonksyon
kullanılablr?


(Çoktan Seçmel)
(A) head()-tal()
(B) start()-stop()
(C) begn()-end()
(D) read()-tal()
(E) head()-end()
Cevap-9 :
head()-tal()
Soru-10 :
Br ver DataFrame’nde belrl br hücrenn seçm aşağıdak seçeneklerden hangsnde doğru şeklde gerçekleştrlmştr?
(Çoktan Seçmel)
(A) ver.get_cell(2, 3)
(B) ver.loc[2, 3]
(C) ver.loc[2, 3]
(D) ver.select(2, 3)
(E) ver.loc[2][3]
Cevap-10 :
ver.loc[2, 3]