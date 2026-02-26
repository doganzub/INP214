# MAKİNE ÖĞRENMESİ - eKitap

**Züber Doğan**
Yeditepe Üniversitesi Meslek Yüksek Okulu

---

## İÇİNDEKİLER

1. Yapay Zekâ, Makine Öğrenmesi ve İlişkili Temel Kavramlar
2. Makine Öğrenmesi Süreci
3. Python ile Veri Görselleştirme
4. Python ile Veri Ön-İşleme
5. K-Ortalamalar Algoritması
6. Basit ve Çoklu Doğrusal Regresyon Analizi
7. K-En Yakın Komşu Algoritması
8. Naive Bayes Algoritması
9. Karar Ağaçları
10. Yapay Sinir Ağları

---


İstanbul Üniv ersitesi
Açık v e Uz aktan Eğim F akült esi


MAKİNE ÖĞRENME Sİ
Züber Doğan


# 1. Yapay Zekâ, Makine Öğrenmesi ve İlşkl Temel

Kavramlar

**Özlü Söz**

Tıpkı 100 yıl önce elektrğn neredeyse her şey dönüştürdüğü gb, yapay zekânın önümüzdek brkaç yıl
çnde dönüştüremeyeceğ br endüstry düşünmekte gerçekten zorlanıyorum.
Andr ew Ng , (DeepLearnng.AI Kurucusu, Landng AI Kurucusu ve CEO'su, AI Fund Genel Ortağı,
Coursera Yönetm Kurulu Başkanı ve Kurucu Ortağı ve Stanfor d Ünverstes Blgsayar Blmler
Bölümünde Y ardımcı Pr ofesör )


**Kazanımlar**

1. Farklı yapay zekâ türlernn genel tanım ve özellkler hakkında temel anlayışa sahp olur .
2. Yapay zekâ türlernn kullanımına lşkn fkr sahbdr .
3. Makne öğrenmesnn temel prenspler ve şleyş mekanzmasını anlar .
4. Makne öğrenmesnn gerçek dünya uygulamalarında nasıl kullanılableceğne dar örnekler kavrar .
5. Geleneksel programlama ve makne öğrenmes arasındak temel farkları anlar .
6. Klask programlamanın sınırlılıkları ve makne öğrenmesnn esneklğ hakkında fkr sahb olur .
7. Danışmanlı, danışmansız ve pekştrmel öğrenme stratejlernn gündelk hayattan farklı senaryolarda nasıl
kullanılableceğne dar blg sahb olur .
8. Danışmanlı öğrenmenn ne olduğu, nasıl çalıştığı ve gerçek dünya problemlerne nasıl uygulanableceğn
öğrenr .
9. Danışmansız öğrenmenn temel prensplern kavrar .
10. Pekştrmel öğrenmenn temel kavramları ve örnek uygulama senaryolarının anlar .
11. Ver madenclğ kavramının önem ve gerçek dünya ver setlernde nasıl uygulanableceğnn öğrenr .
12. Açıklayıcı, tahmnsel ve kuralcı ver analtğnn önemn ve nasıl kullanılableceğn anlar .


**Brlkte Düşünelm**

1.   Yapay zekâ nedr? Günlük hayatta karşılaştığınız bazı yapay zekâ uygulamaları nelerdr?
2.   Yapay zekânın hayatımızdak rolü hakkında ne düşünüyorsunuz? Olumlu ve olumsuz yanları neler
olablr?
3.   Makne öğrenmes kavramını daha önce duydunuz mu? Tanımlayablr msnz?
4.   Hang durumlarda ve neden danışmanlı öğrenme terch edlr?
5.   Danışmansız öğrenme algortmalarına günlük hayattan kullanım örnekler vereblr msnz?
6.   Makne öğrenmes algortmaları gerçek hayat problemlernn çözümünde hang alanlarda kullanılablr?
7.   Geleneksel programlamaya göre makne öğrenmesnn avantajları nelerdr?
8.   Klask programlama le makne öğrenmes uygulamaları arasındak temel farklar nelerdr?
9.   Danışmanlı öğrenme algortmalarının eğtlmes çn hang tür verlere htyaç vardır?
10. Danışmansız öğrenme algortmalarının gerçek dünyadak kullanım alanları nelerdr?
11. Hang durumlarda pekştrmel öğrenme stratejs daha etkl olablr?
12. Pekştrmel öğrenme le br oyun veya smülasyon ortamında nasıl br model gelştrleblr?
13. Ver madenclğ teknkler le br şletmenn müşter memnunyetn artırableceğ senaryolar neler
olablr?
14. Br ver setn anlama sürecne açıklayıcı ver analtğ nasıl yardımcı olablr?
15. Tahmnsel ver analtğ nedr? Hang durum(lar)da kullanılır?
16. Kuralcı ver analtğ nedr? Hang durum(lar)da kullanılır?


**Başlamadan Önce**

Yapay zekâ  (artfcal ntellgence ) ve makne öğr enmes  (machne learnng ), günümüzde teknolojnn
öneml k kolu olarak öne çıkmaktadır . Yapay zekâ, nsan zekâsının maknelere aktarılması düşüncesnden
esnlenlerek blgsayarlara nsan gb düşünme, öğrenme ve problem çözme yetenekler kazandırmayı
hedeflemektedr . Makne öğrenmes se yapay zekânın alt kategorlernden brdr ve nsan gb karar
vereblen sstemlern gelştrlmes çn algortmalar le ver setler üzernden öğrenme ve çıkarımlar yapma
yeteneğ sağlar .
Yapay zekâ ve makne öğrenmes brçok sektörde oldukça öneml değşklklere yol açmıştır . Sağlık, fnans,
eğtm, üretm, spor ve daha brçok alanda yapay zekâ ve makne öğrenmes teknolojlernn etkler
görüleblr . Bu tür sstemler nsanların karar alma süreçlerne olumlu yönde katkılar sunmaktadır . Örneğn
doktorlar çn hastalık teşhsnde kullanılan yapay zekâ uygulamaları sayesnde daha doğru ve hızlı sonuçlar
elde edleblmektedr . Bu teknolojlern hızlı gelşm, geleceğ yapay zekâ ve makne öğrenmes
teknolojlernn şekllendreceğn düşündürmektedr . Akıllı chazlardan otomasyona, robotk sstemlerden
kşsel asstanlara kadar pek çok alanda daha fazla benmseneceğ ve hayatımızı şekllendreceğ


edlmektedr . Bu nedenle bu teknolojlere lşkn temel blgler ednmek ve bu alanlarda gerçekleşen
gelşmeler takp etmek, geleceğn teknolojsne hazırlanmaya yardımcı olacaktır .
Bu bölüm yapay zekâ, makne öğrenmes ve lşkl temel kavramlar konusunda okuyuculara rehberlk etmey
amaçlamaktadır . Öncelkle yapay zekâ kavramının genel tanımı verlerek okuyuculara farklı yapay zekâ
türler ve bu alandak temel blgler aktarılmıştır . Ardından makne öğrenmes konusu dernlemesne ele
alınmıştır . Makne öğrenmesnde öneml yer olan danışmanlı  (supervsed ), danışmansız  (unsupervsed ) ve
pekştrmel  (renfor cement ) öğrenme  stratejler hakkında blgler verlmştr . Her br öğrenme stratejsne
lşkn gerçek dünya örnekler verlerek konunun daha y anlaşılması sağlanmaya çalışılmıştır . Aynı zamanda
geleneksel programlama le makne öğrenmes arasındak temel farklar ortaya konmuştur . Ayrıca makne
öğrenmes le yakından lşkl ver madenclğ konusunda temel tanım ve blgler sunulmuş, Verden blg
keşf  (Knowledge Dscovery fr om Data - KDD ) sürecne değnlmştr . Son olarak açıklayıcı  (descrptve ),
tahmnsel  (predctve ) ve kuralcı  (prescrptve ) ver analtğ  konularında okuyuculara temel br alt yapı
sağlanmıştır .
Düzenleneblr  komut dosyalarına aşağıdak bağlantıdan erşeblrsnz:
https://drve.google.com/fle/d/1b_xrFTdUgJLBmrWxO8lm3oY9T -sWoz1/vew?usp=drve_lnk

## 1.1. Yapay Zekâ

Yapay zekâ  (artfcal ntellgence ), “br blgsayarın veya blgsayar denetml br maknenn, genellkle
nsana özgü ntelkler olduğu varsayılan akıl yürütme, anlam çıkartma, genelleme ve geçmş deneymlernden
öğrenme gb yüksek sevyel zhnsel sür eçler e lşkn gör evler yerne getrme yeteneğ ” olarak
tanımlanmaktadır (Nabyev , 2005). Kısaca, yapay zekâ “ makneler e zekâ kazandırmaya adanmış etknlk ”
olarak tanımlanablr; zekâ br varlığın kend ortamında doğru düzgün ve olan bten öngörerek şlev
görmesn sağlayan ntelktr (Nlsson, 2018). Günümüzde yapay zekâ hayatın pek çok alanında varlığını
göstermektedr; öyle k çeştl yapay zekâ teknolojler ş hayatından gündelk hayata çeştl kullanıcı
arayüzler, web/mobl uygulamaları, elektronk chazlara gömülü olarak vb. kullanıma sunulmaktadır . Yapay
zekâ; görsel algı, konuşma tanıma, karar verme ve dller arası çevr gb normalde nsan zekâsı gerektren
görevler yerne getreblen blgsayar sstemlernn teors ve gelştrlmes olarak tanımlanablr
(Rouhanen, 2018).
Yapay zekâ denldğnde akla lk olarak robotlar gelse de “robotk” yapay zekânın çalışma alanlarından
yalnızca brsdr . Yapay zekânın robotk dışında; doğal dl şleme, görüntü/nesne tanıma, ses tanıma ve bu
ktabın odak noktasında olan makne öğrenmes gb çok çeştl uygulama alanları bulunmaktadır . Son
yıllarda br kşnn fotoğrafının hareketlendrlmes, br vdeoda br kşnn yüzünün farklı br kşnn dudak
hareketleryle senkron hale getrlmes, br kşnn ses kaydını kullanarak daha önce söylemedğ metnlern
seslendrlmes, her alandan farklı sorulara yüksek doğrulukla cevap veren ChatGPT  gb Büyük Dl
Modeller ( Large Language Models - LLM ) en yen yapay zekâ teknolojler olarak sayılablr . Yapay zekâ
alanındak baş döndürücü lerleme bazı endşeler de berabernde getrmektedr (Gherheș, 2018; Schank &
Baress, 2021). Bunlardan en blnen “Y a yapay zekâ (robotlar) br gün dünyayı ele geçrrse?” sorusudur
(Kartal, 2022). Termnatör gb Hollywood flmlernn etks br yana bu kaygının en öneml nedenlernden
br yapay zekâ teknolojler hakkındak blg eksklğ, br dğer se konuyla lgl karamsar ya da yanıltıcı
haberler olablr (Kartal, 2022). Toplumdak bu endşenn ortadan kaldırılablmes adına “yapay zekâ” yerne
ver blm  (data scence ) denlmes fkr ortaya sürülmüştür; ancak bu tür yaygın br kullanım söz konusu
değldr . Ver blm veya ver analtğ  (data analytcs ), ham verye dayalı olarak enformasyon ve blg
çıkarımı sağlayan ve bunları karar süreçlernde kullanan genş br çalışma alanını kapsamaktadır .
Yapay zekâ, ünlü yapay zekâ araştırmacılarından Andrew Ng tarafından günümüzün “ yen elektrğ ” olarak
da anılmaktadır (Rouhanen, 2018). Yan elektrk keşfedldğnde hem breylern yaşamında hem de sanayde
nasıl br etk meydana getrdyse, bugün yapay zekânın da benzer katma değer/etky meydana getrdğ
savunulmaktadır . Yapay zekâ ve teknoloj brbrn karşılıklı olarak beslemektedr . Daha yüksek kapastede ve
daha ucuza ver saklama mkânı, daha hızlı hesaplama yapablen şlemc ve ekran kartlarının üretlmes gb


Ayrıca bu alanda gelştrlen ler düzey algortmalar sayesnde daha güçlü ve yen teknolojler
kullanılablmektedr .
IBM'n yapay zekâ alanındak başarılardan en blnen IBM Deep Blue'nun 1997’de satranç şampyonu Garry
Kasparov’u yenmesdr . İkncs se, IBM Watson'ın 201 1'de Amerkan yarışma programı Jeopardy'de en
başarılı k nsan rakbne karşı üstünlük sağlamasıdır . Br yanda Deep Blue yalnızca 8x8’lk br satranç
tahtasındak tüm olası hamleler değerlendreblmektedr . Dğer yanda br uygulamaya veya servse yapay
zekâ şlevsellğnn eklenmes, çeştl dllerdek metnlern sese dönüştürülmes gb pek çok şlem IBM
Watson le gerçekleştrleblmektedr . Deep Blue ve Watson’un bahsedlen özellkler göz önüne alındığında
Watson’un daha gerçek br yapay zekâ olduğu düşünüleblr , hatta Deep Blue küçümseneblr; ancak her k
sstemn gelştrlmş olduğu zaman dlm ve buna bağlı olarak kullanılan teknolojler brbrnden farklıdır .
Bu nedenle bu bölümde yapay zekâ tarh öneml kş ve olaylar dahl edlerek kısaca ele alınmıştır .
İnsanların yapageldğ bell başlı şlern nsan dışı brtakım el yapımı alet/düzeneklerce gerçekleştrleblmes
fkr antk çağa kadar uzanmaktadır . Bast aletlern harcnde temelnde nsan hayatını kolaylaştıran
düzenekler kullanılarak şölen masalarında yemek/su kram eden çeştl mekank catlardan ( artfact )
bahsedlmektedr . Blndğ anlamda yapay zekânın ortaya çıkış sürecndek mhenk taşlarından br lk defa
Alan Turng tarafından “Makneler düşüneblr m?” sorusunun ortaya atılmasıdır . İknc dünya savaşı
yıllarında özellkle şfre çözme konusunda oldukça ünlü olan Alan Turng, Turng Testn gelştrmştr .
Turng Test br nsan denek, kendsnden farklı odalarda bulunan br blgsayar ve br başka nsan
katılımcıdan oluşmaktadır . İnsan denek, farklı odalarda bulunan yapay zekâ sstem (blgsayara) ve nsana
sorular yöneltmekte ve cevaplar almaktadır . İnsan denekten bu cevapların br makneden m yoksa br
nsandan mı geldğn belrlemes stenr . Eğer nsan denek doğru cevap veremezse yan makne nsanı
kandırırsa yapay zekânın test geçtğ kabul edlmektedr . Böylesne sade tasarlanan br test br yapay zekâ
sstemnn geçp geçmedğ hala tartışma konusudur .

### 1.1.1. Yapay Zekânın Kısa Tarh

Tarhte yapay zekânın gelşm sürec temel olarak üçe ayrılablr (Delpetrev vd., 2020):
1950-1970: Yapay zekâ temellernn atıldığı yıllardır . John McCarthy yapay zekânın sm babası dır. 1956
yılında Dartmouth konferansında Yapay Zekâ term lk kez kullanılmış ve yapay zekâ bu tarhten sonra br
blm dalı olarak anılmaya başlanmıştır . Bu dönemdek çalışmalar daha çok matematksel problemlern
çözümlerne odaklanan sstemler çermektedr . Checkers, The Logc Theorst, yapay snr ağlarının temel
perceptron (lkel yapay snr hücres), ELIZA, Shakey vb. teknolojler bu döneme attr . Marvn Mnsky 1970
yılında “ 3 la 10 yıl çnde ortalama br nsan zekâsına sahp br makne elde edlecektr ” şeklnde br
öngörüde bulunsa da ne yazık k bu beklent belrtlen tarhlerde karşılanamamıştır .
1974-1980:  Bu dönem lk yapay zekâ kışı olarak blnmektedr . Marvn Mnsky ve Seymour Papert,
gelştrlen temel snr hücres modelnn lneer olmayan problemlern çözümünde (XOR problem) başarısız
olduğunu belrtmştr . Bu dönemde blm nsanları arasında beklentler karşılayamayan yapay zekâya olan
lg le yapay zekâ çalışmalarına ayrılan destek mktarı azalmıştır .
1970-1990:  Blg-tabanlı ya da uzman sstemler ( expert systems ) olarak da blnen sembolk yapay zekâ
sstemlernn gelştrldğ dönemdr . Bu dönemde gelştrlen yapay zekâ sstemlernn altında yatan temel
düşünce, nsana at uzman blgsnn blgsayar sstemnde elde etmek ve bunu br program aracılığı le brçok
kşsel blgsayara yaymaktır . Lsp ve Prolog temel sembolk programlama dllerne örnektr . 1980 yılında
Hans Moravec tarafından Moravec Paradoksu  ortaya konmuştur . Moravec Paradoksu’na göre;
“Blgsayarların zekâ testlernde veya dama oynamada yetşknler düzeynde performans göstermesn
sağlamak nspeten kolaydır; algı ve har eket söz konusu olduğunda onlara br yaşındak br çocuğun
becerlern kazandırmak zor veya mkansızdır .” (Sung vd., 2020). 80’l yıllarda ortaya atılan bu paradoksun
günümüzde hala yapay zekâ ve makne öğrenmes alanlarında yapılan çalışmaların tetkleycs olduğu
söyleneblr . Paradoksta nsan çn zor sayılablecek zhnsel süreçler blgsayarlar tarafından kolaylıkla
gerçekleştrlrken, blgsayarların performansının annesnn sesn duyduktan sonra onu tanıyan ve ona doğru
hareket eden br yaşındak br çocuğun yapableceğ şlerden daha sınırlı olduğu belrtlmektedr (Kartal &
Schwartz, 2022). Bu dönemde gelştrlen geleneksel makne öğrenmes modeller çoğu zaman nesne tanıma,


1987-1994:  Bu dönem se knc yapay zekâ kışı olarak adlandırılmıştır . Lsp pazarı, dğer br fade le
üzernde yapay zekâ sstemlernn çalıştırıldığı pazar çökmüş, DARP A yapay zekâ araştırmalarına ayırdığı
desteğ kesmş, uzman sstemlernn yönetm ve yen blgy şlemede yetersz kalması gb olumsuz
durumlarla karşılaşılmıştır .
1990-Günümüz:  1990'lı ve 2010'lu yıllarda yapay zekâ, ver madenclğ, endüstryel robotk, lojstk, ş
zekâsı, bankacılık yazılımı, tıbb teşhs, öner sstemler ve arama motorları da dahl olmak üzere farklı
uygulama alanlarında faydalı çözümler sunan karmaşık sorunları ele alınmıştır . Bu dönemde makne
öğrenmes le dern öğrenme ön planda yer almıştır . Özellkle 201 1-2020 arasındak dönemde dern öğr enme
(deep learnng ) algortmalarının yapay zekâ sstemler üzerndek etks oldukça önemldr (SAS, 2023).
Günümüzdek yapay zekâ çalışmaları se üretken yapay zekâ  (Generatve AI) olarak adlandırılmaktadır
(SAS, 2023). Günümüzde yapay zekâ teknolojlernn geldğ noktada metn, resm, müzk, tasarım ve dğer
çerkler üretme yeteneğ yapay zekâ sstemlerne kazandırılmıştır . Çalışmalarda kullanılan vernn metn,
görüntü, ses gb formlarda olmasına göre yapay zekâ sstemlernn uygulama alanları farklılık
göstermektedr .
• Roman, makale, şr ya da stenlen amaçta otomatk metn oluşturmak ( https://machneswsdom.com/ ):
“There s nothng so full of pan and uncertanty as the uncertanty surr oundng an unfulflled dr eam.”
Machne Wsdom (GPT -2)
• Resm, llüstrasyon ya da grafkler otomatk oluşturmak ve rastgele resmler üretmek (bknz.
https://thesecatsdonotexst.com/  (Şekl 1), https://ths-person-does-not-exst.com/en ),


Şekl 1: thesecatdonotexst.com tarafından üretlen ked görseller.
• Şarkı, ses efekt ya da kayıtlarını otomatk oluşturmak (bknz. https://soundraw .o/),
• Sınırlı mktardak ver setn büyütmek.
Yapay zekânın kullanıldığı bazı teknolojler şöyle sıralanablr:
• Blgsayarlı görü  (computer vson ), br resm veya vdeoda ne olduğunu tanımak çn örüntü tanıma ve
dern öğrenmey kullanır . Görüntü şleme sstemler sayesnde gerçek zamanlı olarak görüntü veya vdeo


• Doğal dl şleme  (Natural Language Pr ocessng- NLP ), blgsayarların konuşma da dâhl olmak üzere nsan
dln analz etme, anlama ve cevap verme yeteneğdr . Günümüzde yalnızca yapay zekâ araştırmacıları
arasında değl hemen hemen her kesm tarafından kullanılan ChatGPT  doğal dl şleme çalışmalarına güzel
br örnek teşkl etmektedr . ChatGPT , OpenAI tarafından gelştrlen konuşma tabanlı yapay zekâ
sstemlernden brdr . ChatGPT , GPT  (Generatve Pr e-traned T ransformer ) model alesnn br üyesdr ve
büyük metn verler le eğtlmş br dl modeldr ( LLM ). Bu model, kullanıcılarla doğal dlde sohbet etme
yeteneğne sahptr ve genellkle metn tabanlı soruları yanıtlama, metn oluşturma ve genel metn tabanlı
etkleşmler çn kullanılmaktadır . ChatGPT’nn rakpler arasında yer alan ve Google tarafından gelştrlen
Gemn, BER T (Bdr ectonal Encoder Repr esentatons fr om T ransformers ) altyapısını kullanmaktadır
(Devln vd., 2019).
• Grafksel şlem brmler  (Graphcal Pr ocessng Unts- GPUs ) yapay zekânın temel donanımı olarak
görülmektedr; çünkü ynelemel şleme çn gereken yoğun blg şlem gücünü sunar .
• Nesnelern nternet  (Internet of Thngs- IoT ), brbrleryle ve sunucuyla kablosuz ağlar (W-F) vasıtasıyla
letşm kuran chazlardan büyük mktarda ver üretlmektedr . Gelştrlen yapay zekâ sstemler le vernn
gerçek zamanlı şlenmes verden daha çok katma değer sağlayacaktır .
• Daha fazla vernn daha hızlı ve brden çok sevyede analz edlmes çn özel algortmalar  ve yöntemler
gelştrlmektedr .
• API'ler, uygulama programlama arayüzler ( applcaton pr ogrammng nterfaces ), mevcut ürün ve yazılım
paketlerne yapay zekâ şlevsellğnn entegrasyonunu sağlayan taşınablr kod paketlerdr .

### 1.1.2. Yapay Zekâ Türler

Günümüzde yapay zekâ sstemler üç ana başlıkta toplanmaktadır (Delpetrev vd., 2020):
Dar Yapay Zekâ:  Genellkle "Zayıf" yapay zekâ olarak da anılan Dar Yapay Zekâ ( Weak Artfcal
Intellgence ), günümüzde çoğu yapay zekâ sstemnn dâhl olduğu br kategordr . Dar yapay zekâ sstemler
br veya brkaç özel görev yaparlar fakat bunun harcndek herhang br görev yerne getremezler . Dar
yapay zekâ, genelleme yeteneğnden yoksundur . Br başka fade le öğrenlen blgnn farklı alanlar arasında
yenden kullanılma yeteneğ yoktur . Örneğn görüntü tanıma yeteneğne sahp dar yapay zekâ bu blgsn
konuşma tanıma alanına aktaramayacaktır . Bu sebeple genelleme sorunu hâlâ açık br sorudur (Hernández-
Orallo, 2017).
Güçlü Yapay Zekâ:  “Güçlü” yapay zekâ olarak da anılan Genel Yapay Zekâ ( Strong Artfcal Intellgence ),
nsan zekâsı ser gleyen makneler fade eder . Başka br deyşle güçlü yapay zekâ, br nsanın yapableceğ
her türlü entelektüel görev yerne getrmey amaçlamaktadır . Güçlü yapay zekâ genellkle blm kur gu
flmlernde nsanların blnçl, duyarlı, duygulu ve öz farkındalıkla yönlendrlen maknelerle etkleşme
grdğ durumlarla resmedlmektedr .
Süper  Yapay Zekâ:  Süper yapay zekâ ( super artfcal ntellgence ), neredeyse tüm lg alanlarında
nsanların blşsel performansını büyük ölçüde aşan herhang br zekâ olarak tanımlanmaktadır (Bostrom,
2016). Good (1965) tarafından önerlen süper yapay zekâ le lgl klask hpoteze göre, kend tasarımını
anlayacak kadar akıllı br yapay zekâ, kendsn yenden tasarlayablr veya daha akıllı br ardıl sstem
oluşturablr; bu sstem daha sonra daha da akıllı olmak çn kendn yenden tasarlayablr ve bu süreç olumlu
br ger bldrm döngüsünde devam edeblr (Bostrom & Yudkowsky , 2014). Süper yapay zekânın her açıdan
(üretm, genel blgelk ve problem çözme vb.) nsan zekâsını aşması beklenmektedr . Bu da pek çok
araştırmacının süper yapay zekâ konusunda endşel olmasına neden olmaktadır . Şmdlk süper yapay
zekânın yalnızca blm kur gu flmlerne at br kavram olduğu söyleneblr .

## 1.2. Makne Öğr enmes

Öğrenmek Türk Dl Kurumu tarafından blg ednmek; bellemek, yetenek, becer kazanmak bçmnde
tanımlanmaktadır (TDK, 2023). İnsanlarda öğrenme sürec üzerne örnek vermek stenrse, okul yıllarında br


problemle lk kez karşılaşılmışsa br öğretmene, ebeveynlerden brne ya da br arkadaşa sorarak ya da br
ktaptak benzer sorular ncelenerek/çözülerek lgl problem çn nasıl çözüm elde edlebleceğ öğrenleblr .
Ya da daha önce hç blnmeyen br oyunun öğrenme sürec hatırlanablr . Oyunu oynayanlar gözlemlenerek
oyunun nasıl oynandığı/kuralları hakkında blg sahb olunablr . Sonrasında se oyuna grleblr . İnsanlar
blmedğ br şey öğrendğnde/duyduğunda klo almaz, çünkü blgnn br kütles yoktur; ancak hçbr blg
parçası br mktar madde veya enerj olmadan kend başına var olamaz (Say , 2020). Yen br şey
öğrenldğnde beyndek snr hücreler (nöronlar) arasındak bağlantılar değşmektedr ve yen bağlantılar
oluşmaktadır , öğrenme beyn fzksel olarak değştrmektedr (Balkuv , 2020). Makneler (ya da blgsayarlar)
se, karmaşık ve yüksek boyutlu ver oluşturma süreçlern modelleyeblr , mlyonlarca model
konfgürasyonunu tarayablr ve ardından yen blglere yanıt olarak modeller sağlam br şeklde
değerlendrp düzelteblr (Dhar , 2013; Dxon vd., 2020). O halde nsanlardak byolojk ve kompleks
öğrenme sürec maknelerde nasıl gerçekleşmektedr?
Smon (1984) göre öğrenme " br sstemn aynı gör ev knc kez yapmasına veya aynı popülasyon çn
oluşturulan yen br gör evde daha y performans göstermesne neden olacak her hang br değşklk " olarak
tanımlanmaktadır . Makne öğrenmes, örnek verler veya geçmş deneymler kullanarak belrl br
performans krtern optmze etmek çn blgsayarları programlamaktır (Alpaydın, 2014). Mohr ve dğ.
(2012), makne öğrenmes kavramını “etkl ve hatasız tahmn yapablen algortmaların tasarlanması” olarak
tanımlarken, Mtchell (1997) makne öğrenmes alanını “deneym le otomatk olarak gelşen blgsayar
programlarının nasıl oluşturulableceğ le lglenmekte olduğunu” fade etmştr (Kartal, 2015).
Yne Mtchell (1997)’a at kapsamlı makne öğrenmes tanımlarından br şu şekldedr: “ Eğer br blgsayar
programının G gör evlernde P  le ölçülen performansı, deneym D le artıyorsa, o blgsayar pr ogramının
bazı G gör evlernn sınıflarına ve performans ölçüsü P’ye gör e deneym D’den öğr endğ söylenmektedr ”
(Balaban & Kartal, 2018). Mtchell (1997) tarafından yapılan bu tanım ncelendğnde makne öğrenmesnde
dört temel unsurun yer aldığı görüleblr:
1)   Görev (Task): Günümüzde kullanılan çoğu yapay zekâ sstem özel görev - alan ( doman ) tabanlı
çalışmaktadır . Dolayısıyla maç sonucu tahmn etmes stenen br yapay zekâ sstemnden kanser teşhs
yapmasını beklemek yanlış olacaktır . Bu sebeple öncelkle ele alınan problem/görev belrlenmeldr . Kalp
hastalarının amelyat sonrası hayatî rskn öngörülmes, şüphel bankacılık şlemlernn tespt, maç
sonucunun tahmn edlmes, müşter segmentasyonu, vb. örnek olarak verleblr .
2)   Deneym (Experence ): Br konu hakkında nsanlardakne benzer br deneymn maknelere
kazandırılması çn “ver” kullanılmaktadır . Buradan hareketle makne öğrenmes modellern “verden
öğrenen modeller” olarak tanımlamak yanlış olmayacaktır . Günümüzde “ver” artık “büyük ver” olarak
anılmaktadır; ancak termdek “büyük” kavramı yalnızca yüksek mktarda/hacmce olan büyüklüğü fade
etmez. Lteratürde büyük vernn hacm ( volume ), çeştllk ( varety ), hız ( velocty ) ve güvenlrlk ( veracty )
özellkler büyük vernn 4V ’s olarak anılmaktadır (Özen, Kartal, & Emre, 2017). Elektronk ortamda ver
br ver tabanı çnde yapısal  (structur ed) olarak veya metn, görsel, ses, web veya sosyal medya vers gb
yapısal olmayan  (unstructur ed) şeklde olablr . Makne öğrenmes modellernn gelştrlmes sürecne tek
tp ya da brden fazla tpte ver dahl edleblr . Çöp-grd çöp-çıktı  (Garbage-In Garbage-Out- GIGO ),
makne öğrenmes çalışmalarında vernn önemn vur gular . Bu nedenle eğer ver güvenlr değlse, yanlı
(based ) se, eksk/hatalı değerler varsa vb. elde edlecek analz sonuçlarına da bu durum yansıyacaktır .
Analzler sonucunda güvenlr olmayan tahmn/öngörüler ve katma değer sağlamayacak çıktılar üretleblr .
Çöp-grd çöp-çıktı deym ktabın lerleyen bölümlernde daha kapsamlı br bçmde yenden ele alınacaktır .
Özetle ver, makne öğrenmes modellernn öğrenmey sağlayan deneym altyapısını oluşturmaktadır . Bu
nedenle ver kaltesnn makne öğrenmes sürec çn oldukça öneml olduğu söyleneblr .
3)   Algortma (algorthm ): Makne öğrenmes şn sağlayan esas unsur kullanılan makne öğrenmes
algortmasıdır . Algortma kavramsal olarak br problemn çözümü çn adım adım zlenen yol şeklnde
tanımlanmaktadır . Lteratürde farklı öğrenme stratejlern kullanan brçok farklı makne öğrenmes
algortmaları bulunmaktadır (bknz. k-En Yakın Komşu Algortması, Nave Bayes Sınıflandırıcı, Yapay Snr
Ağları, k-Ortalamalar Algortması, vb.). Bu öğrenme stratejler üç ana başlıkta toplanablr:
• Danışmanlı/denetml/gözetml öğrenme ( supervsed learnng ).


• Pekştrmel öğrenme ( renfor cement learnng ).
Bu öğrenme stratejlernn detaylarına Bölüm 1.4’ te yer verlmştr .
4)   Performans  (performance ): Makne öğrenmes çn belrlenen G görev doğrultusunda makne
öğrenmes algortmaları elde edlen ver setne uygulanmaktadır . Bu noktada elde edlen makne öğrenmes
modelnn gerçekten öğrenp öğrenmedğ ya da ne kadar öğrendğnn belrlenmes gerekr . Bunun çn kl
ayırma ( hold-out ) ve çapraz geçerleme ( cross-valdaton ) gb çeştl model performans değerlendrme
yöntemler ve doğruluk ( accuracy ), belrleyclk ( specfcty ), kesnlk ( precson ) gb çeştl model
performans değerlendrme ölçütler tanımlanmıştır . Ele alınan öğrenme stratejs gereğnce uygun performans
değerlendrme yöntem ve ölçütü kullanılarak model performans değerlendrmes gerçekleştrleblr .

## 1.3. Klask Pr ogramlama ve Makne Öğr enmes

Gerek blgsayar programlamada gerekse yapay zekâ çalışmalarında algortmalardan faydalanılmaktadır;
ancak bu k kavram arasında benzerlkler olduğu kadar farklılıklar da mevcuttur . Algortmalar br problemn
çözümü çn tasarlanmıştır , verlen grd ya da grdlerden belrl br çıktı ya da çıktıların üretlmesn
sağlarlar ve çlernde br takım matematksel ve hesaplamalı süreçler barındırırlar . Ayrıca her k algortma
türü de mantıksal br akışa sahptr . Geleneksel programlama algortmaları net, önceden belrlenmş br
talmat dzsne sahpken; makne öğrenmes algortmaları eğtm ve tahmn/öngörü aşamalarında belrl br
sürec takp etmektedr . Bu k grup arasındak farklılıklara Tablo 1’de yer verlmştr .
Tablo 1: Geleneksel programlama ve makne öğrenmes algortmalarının farklılıkları.
Özellk Klask Pr ogramlama Makne Öğr enmes
Kodlama Açık, kural tabanlı br dz talmatlar
gerektrr .Verye dayalı br öğrenme yaklaşımı mevcuttur .
Uyarlanablrlk Statktr , nsan müdahalesne dayalı
kod güncellemeler olmadan yen
durumlara uyum sağlamaz.Uyarlanablrdr , verdek kalıpları
genelleştreblme yetenekler bulunur .
Verye Bağlılık Verye htyaç duymaz. Kural ve
talmatları yürütürler .Deneym altyapıları çn verye htyaç duyarlar .
Ver kaltes öğrenme süreçlernde öneml br
rol oynar .
Görev Türü Sıralama, arama gb kural tabanlı
determnstk görevler çn uygundur .Görüntü tanıma, doğal dl şleme gb örüntü
tanıma, tahmn/öngörüde bulunma ve
sınıflandırma gb görevlerde kullanılırlar .
İnsan Müdahales Tamamen nsanlar tarafından kontrol
edlr ve tasarlanırlar . Herhang br
değşklk söz konusu olduğunda
yenden nsan müdahalesne htyaç
duyarlar .Daha fazla ver sağlandıkça otomatk olarak
uyum sağlayablr ve gelşeblr , böylece sürekl
manuel müdahale htyacı azalır .
Yorumlanablrlk Sonuçlar daha yorumlanablrdr ,
çünkü tüm sürece lşkn mantık
kodda açıkça tanımlanmıştır .Özellkle kara-kutu ( black-box ) olarak blnen
makne öğrenmes algortmaları le elde edlen
sonuçlar daha az yorumlanablr olarak
değerlendrlr . Bu da kararlara nasıl
ulaşıldığının anlaşılmasını zorlaştırır .

Klask programlamada br programlama dlnn söz dzmyle programlar kodlanır ve problemler programlar
aracılığıyla çözüme kavuşturulur . Başlangıçta belrlenen amaca göre ver şlenerek çıktıya dönüştürülür . Br
başka fade le br programcı, blgsayardan çıktı olarak br cevap/yanıt almak amacıyla ver grşlern
şlemek çn gereken kuralları belrleyen blgsayar kodunu yazmaktadır (Annon vd., 2018).
Makne öğrenmes se blg şlemde paradgmatk br değşm temsl etmektedr; br makne öğrenmes
sstem açıkça programlanmak yerne eğtlr (Şekl 2) (Annon vd., 2018). Makne öğrenmesndek öğrenme


sunulması gerekmektedr . Sonucunda karar almaya yardımcı olacak tahmn, öngörü ya da kural benzer
çıktıları elde etmek mümkündür .


Şekl 2: Klask programlama ve makne öğrenmes (Annon vd., 2018).

## 1.4. Makne Öğr enmes Stratejler

Makne öğrenmesnde kullanılan öğrenme stratejler danışmanlı öğrenme, danışmansız öğrenme ve
pekştrmel öğrenme olmak üzere temelde üç grupta nceleneblr .

### 1.4.1. Danışmanlı Öğrenme

Danışmanlı öğrenme, öğrenenn eğtm vers olarak br dz etketlenmş örneğ aldığı ve daha önce
görmedğ örnekler/noktalar çn tahmnde bulunduğu br öğrenme şekldr (Kartal, 2015; Mohr vd., 2012).
Danışmanlı öğrenme, grd-çıktı çftlerne dayalı olarak br grdy br çıktıyla eşleştren ( mappng ) br
fonksyonun öğrenlmes görevdr (Han vd., 201 1; Sarker , 2021). Danışmanlı öğrenmede amaç, ver
setndek grd değşkenler/tahmn edc ntelkler/bağımsız değşkenler  (nput varables/ndependent
varables /predctor featur es/pr edctve attrbutes ) kullanarak etket dağılımını veren esaslı br model
oluşturablmektr (Kartal, 2015; Kotsants vd., 2006). Çalışmalarda genellkle bağımsız değşkenler br  
  matrs le temsl edlr . Danışmanlı öğrenme adından da anlaşılacağı gb makne öğrenmes algortmasına
öğrenme sürecnde danışmanlık eden br yardımcı le gerçekleştrlmektedr . Bu danışman, ver setndek
çıktı değşken/bağımlı değşken/hedef ntelk  (output varable/dependent varable/tar get attrbute ) olarak
düşünüleblr . Çalışmalarda genellkle hedef ntelk  
   vektörü le temsl edlmektedr . Br danışmanlı
öğrenme algortması 

 bçmnde br eşleme/hartalama yapar .
Danışmanlı öğrenme br fonksyonun çıkarımını yapmak çn etketlenmş ( labeled ) eğtm verlern ve br
dz eğtm örneğn kullanır (Sarker , 2021). Danışmanlı öğrenme kapsamında en yaygın olarak
sınıflandırma  (classfcaton ) ve regresyon  (regresson ) problemler ele alınmaktadır . Etketlenmş ver
denldğnde akla yalnızca kategork hedef ntelk gelmemeldr . Ver setnde hedef ntelk bazı görevler çn
kategork bazı görevler çnse nümerk olablr . Örneğn; br e-tcaret şrketnn müşter ver setnde “müşter
sadakat” hedef ntelk olarak tanımlanablr . Bu hedef ntelk, müşterler “Y en”, “Düzenl” ve “Sadık” gb
kategorlere ayırmak çn kullanılablr . Dğer br örnek olarak br perakende mağazasının ürünlern
sınıflandırmak çn kullanılan br ver set düşünüleblr . Hedef ntelk, ürün türlern temsl eden “Elbse”,


konutun tahmn fyatını belrlemek çn kullanılan br ver set ele alınsın. Hedef ntelk, evlern tahmn
değern temsl eden br sürekl br nümerk değer çereblr , “2.000.000 TL”, “5.000.000 TL” gb. Ya da br
hsse senednn gelecektek fyatının tahmn edldğ modelde ver setnde hedef ntelk olarak sürekl
nümerk değerler kullanılablr (örneğn 150, 500, 250 gb). Kısaca eğer ver setndek hedef ntelk
kategorkse sınıflandırma, nümerkse regresyon gerçekleştrlr . Tahmn sağlayan ntelklern ver tp
konusunda se herhang br koşul söz konusu değldr , kategork ya da nümerk olablr .
Danışmanlı öğrenme stratejsn kullanan makne öğrenmes algortmalarının genel anlamda eğtm ve test
olmak üzere k temel aşaması bulunur . Orjnal ver setnn belrl br kısmı algortmanın eğtm, ger kalanı
se makne öğrenmes modelnn ne kadar y öğrendğnn test edlmes yan model performansının
değerlendrlmes çn kullanılmaktadır . Bununla lgl detaylı blglere Bölüm 2.7’de yer verlmştr .
Algortmanın eğtm aşamasında eğtm ver setnde yer alan örnekler/gözlemler  (samples/observatons )
teker teker algortmaya grd-çıktı çftler bçmnde sunulmaktadır . Makne öğrenmes modelnde kullanılan
algortma eğtm aşamasında hem tahmn sağlayan ntelkler hem de buna karşılık gelen çıktı değern yan
hedef ntelğ görmüş olacaktır . Danışmanlı öğrenmede, hang grd değerne karşılık hang çıktı değernn
geldğ blnmektedr .
Sınıflandırma
Sınıflandırma problemlernde sınıfı blnmeyen br örnek ( unlabeled sample ) k ya da daha fazla kategorden
oluşan sınıf etketler arasından brne atanmaya çalışılır . Sınıflandırma görevlernde hedef ntelk
kategorktr . Örneğn; yaşı 30 olan, İstanbul’da yaşayan, … özellklerne sahp olan banka müştersnn kred
rsk “düşük”, yaşı 60 olan, Sakarya’da yaşayan, … özellklerne sahp olan banka müştersnn kred rsk
“yüksek” gb.
Br sınıflandırma problem çn danışmanlı makne öğrenmes algortmaları, kategork sınıf etketnn ( 
  )
ölçüleblr özellklerden oluşan br vektöre ( 
  ) bağımlılığını öğrenmek çn eğtm örneklern çeren ver
setn 

 alır ve tüm ver setndek hatayı en aza ndrmey hedefler (Jan vd., 2009). Hata, modeln tahmn ya da
öngörülernn gerçek değerlerden ne kadar uzak olduğunun br ölçüsüdür .
Aşağıdak tabloda danışmanlı öğrenmede kullanılablecek örnek br sınıflandırma ver set yer almaktadır
(Tablo 2). Br banka müştersnn kred puanı, aylık gelr, bankaya olan borcu, başka bankadan kred alıp
almadığı, … ve kred süres ntelkler kullanılarak yaptığı kred başvuru durumu sonucu öngörülmek
stensn. Hedef ntelkte ( 

) onaylanmış/onaylanmamış gb sınıf etketler tutulmaktadır .


Algortmanın eğtmnden sonra makne öğrenmes model test edleblr . Model Tablo 3’ te verldğ gb yen
br müşternn başvuru onay durumu öngörüsünde bulunulablr .
Tablo 3: Sınıflandırmada etket blnmeyen br örnek.

Sınıflandırma çıktı uzayındak her br elemana br sınıf (class ), sınıflandırma problemn çözen algortmaya
se sınıflandırıcı  (classfer ) adı verlmektedr (Camastra & Vncarell, 2008). Sınıflandırmada kategor
sayısına göre farklı adlandırmalar kullanılır . Eğer hedef ntelğn kategorler az/çok, evet/hayır , var/yok,
hasta/sağlıklı gb k kategorden oluşmakta se buna kl sınıflandırma  (bnary classfcaton ), eğer
kategor sayısı az/orta/çok, düşük/normal/yüksek gb kden fazla kategorden oluşuyorsa buna çoklu-sınıflı
sınıflandırma  (mult-class classfcaton ) denr (Sokolova & Lapalme, 2009). Eğer verlen grd brbryle
örtüşmeyen  

 adet sınıftan brkaç tanesne atse çoklu-etketl sınıflandırma , brbryle alt sınıflara ayrılan ya da üst
sınıflara gruplanablen sınıflardan yalnızca brne atse buna da hyerarşk sınıflandırma  adı verlr
(Sokolova & Lapalme, 2009).
Aşağıda bazı sınıflandırma problem örneklerne yer verlmştr .
• Spam Fltr es: E-posta letlern stenmeyen ( spam ) veya normal e-posta olarak almak çn sınıflandırma
kullanılır . Spam fltreler, gelen e-postaları otomatk olarak k kategorye ayırır .
• Hastalık Teşhs:  Tıbb görüntüler veya hastalık belrtler üzernde çalışan br sınıflandırma model,


• Araç Tanıma:  Görüntülerdek araçları dğer nesnelerden ayıran br sınıflandırma model, otonom araçlar
veya trafk zleme sstemlernde kullanılablr .
• Dl Tanıma:  Br metn veya ses kaydının hang dlde olduğunu tespt etmek çn sınıflandırma modeller
kullanılablr . Bu tür br sınıflandırma, çok dll metn analz veya konuşma tanıma sstemlernde yaygın
olarak kullanılır .
• Ürün İncelemeler Duygu Analz:  Müşter yorumlarını poztf, negatf veya nötr gb duygu kategorlerne
ayırmak çn sınıflandırma kullanılır . Duygu analzler, şrketlern ürün veya hzmetler hakkında ger
bldrmler değerlendrmelerne yardımcı olur .
Regr esyon
Regresyonda amaç; br bağımlı değşkenn (nümerk br değşken), br veya daha fazla bağımsız değşkenle
olan (nümerk veya kategork olablr) lşksn anlamak ve bu lşky modellemektr . Regresyon
görevlernde hedef ntelk sürekl değerler alan nümerk br ntelktr . Örneğn; sgara çen, alesnde kanser
öyküsü olan, … özellklerne sahp br hastanın kanser olma olasılığı yüzde “90”, sgara çmeyen, alesnde
kanser öyküsü olmayan, … özellklerne sahp br hastanın kanser olma olasılığı yüzde “20” gb.
Tablo 4’ te danışmanlı öğrenmede kullanılablecek örnek br regresyon ver set yer almaktadır . Br otel
müştersnn otele ödeyeceğ br gecelk fyatın tahmn edlmes amacıyla oda tp, oda boyutu, konum
uzaklığı (km), sosyal medya puanı, … ntelklernn kullanıldığı örnek br ver set yer almaktadır . Hedef
ntelk  

, 2500, 2000, 8000 gb nümerk sınıf değerlern tutmaktadır .
Tablo 4: Regresyon çn kullanılan örnek ver set.


Algortmanın eğtmnden sonra makne öğrenmes model Tablo 5’ te verldğ gb yen br müşter çn
verlecek gecelk oda konaklama fyatı tahmnnde kullanılablr .


Aşağıda bazı regresyon problem örneklerne yer verlmştr .
• Emlak Fyat Tahmn:  Br evn özellklern (metrekare, oda sayısı, konum vb.) kullanarak evn fyatını
tahmn etmek çn regresyon kullanılablr .
• Hsse Sened Fyat Tahmn: Geçmş hsse sened fyatları, ekonomk göster geler ve dğer faktörler
kullanılarak gelecektek hsse sened fyatlarını tahmn etmek amacıyla regresyon analz yapılablr .
• Hava Durumu Tahmn: Hava durumu tahmnnde sıcaklık, rüzgâr hızı, nem gb meteorolojk verler
kullanarak belrl br bölgedek sıcaklık veya yağış mktarı gb sürekl değşkenlern tahmn edlmes çn
regresyon modeller kullanılablr .
• Pazarlama Malyet ve Satış İlşks:  Pazarlama harcamaları le satışlar arasındak lşky anlamak ve
gelecektek satışları tahmn etmek çn regresyon kullanılablr . Bu, pazarlama stratejlernn etkllğn
değerlendrmeye yardımcı olablr .
• Öğrenc Başarı Tahmn:  Öğrenclern sınav sonuçlarına, öğrenme süreçlerne ve dğer faktörlere dayalı
olarak gelecektek akademk başarılarını tahmn etmek çn regresyon analz yapılablr .

### 1.4.2. Danışmansız Öğrenme

Danışmansız öğrenmede ver setnde herhang br hedef ntelk bulunmaz. Danışmansız öğrenme yöntem
ver setndek desenler, örüntüler, şablonları, gzl grupları ya da blgler ortaya çıkarmak çn
kullanılmaktadır . Danışmansız öğrenme yöntem üretken ( generatve ) özellklern çıkarılması, anlamlı
eğlmlern ve yapıların belrlenmes, sonuçlardak gruplama ve keşf amaçları çn yaygın olarak kullanılır
(Sarker , 2021). Danışmansız öğrenme; kümeleme ( clusterng ), yoğunluk tahmn ( densty estmaton ), ntelk
öğrenme ( featur e learnng ), boyut azaltma ( dmensonalty r educton ), brlktelk kurallarını ( assocaton
rules ) bulma, anormallk tespt ( anomaly detecton ) gb alanları kapsar .
Kümeleme Analz
Kümeleme analz, ver setnde bulunan örneklern brbrne olan benzerlkler/benzemezlkler ya da
uzaklıkları temel alarak ver setn gruplara ayırmak amacıyla kullanılmaktadır (Şekl 3). Örneğn müşterler
alışverş terchlerne göre gruplamak veya sosyal medya verlern kullanarak kullanıcıları lg alanlarına göre
sınıflandırmak çn kümelemeden faydalanılablr . Br şrket, müşterlernn alışverş terchlerne veya
davranışlarına göre müşterlern gruplandırmak steyeblr . Böylelkle belrl ürün kategorlerne veya
ndrmlere lg gösteren müşterlern belrlenmes sağlanır . Bu örnekte olduğu gb müşterlern
gruplandırılması sektörde müşter segmentasyonu olarak adlandırılmaktadır . Br başka örnek olarak trafkte
kameralar ve sensörler yardımı le trafğ zlemek ve benzer trafk desenlern tanımlamak verleblr . Böylece
trafk akışı optmze edleblr ve trafk kazalarına karşı önlem alınablr .

### 1.4.3. Pekştrmel Öğrenme

Pekştrmel öğrenme, ödül-ceza mekanzmasına dayalı ger bldrm sağlayan br öğrenme


gelştrlmştr . Gelecektek ödülün değern optmze etmek amacıyla pozsyonları/hamleler ve lgl ger
bldrmler değerlendrerek yen hamleler seçmektedr . AlphaGo'da araştırmacılar , blgsayar programının
kendsnn farklı versyonlarına karşı oynamasını sağlayarak pekştrmel öğrenme yoluyla hatalarından ders
almasını sağlamıştır (Kartal & Schwartz, 2022; Slver vd., 2017). Bu öğrenme stratejs daha çok oyun
teors, robotk, otonom sürüş, çeştl yapay zekâ oyunları, fnansal tcaret ve benzer alanlara uygundur .
Pekştrmel öğrenmenn daha y anlaşılablmes çn mobl br robotun çöp toplamak çn odalara grmes le
pln şarj etmek çn uygun br alan bulması arasında seçm yapması durumu örnek olarak verleblr (Kartal,
2015; Sutton & Barto, 1998).


Şekl 3: Ülkelern belrl ntelklern dkkate alarak kümelenmes örneğ (Kartal vd., 2021).
Pekştrmel öğrenmede bazı özel kavramlar yer almaktadır:
• Ajan (agent ): Ajan, kararlar veren ve etkleşmde bulunan varlıktır . Örneğn br otonom araç, br robot veya
br yapay zekâ programı br ajan olablr .
• Çevr e (envr onment ): Çevre, ajanın etkleşmde bulunduğu ve çevresel koşulların gelştğ yerdr . Çevre
fzksel br ortam, br oyun alanı veya br yazılım smülasyonu olablr .
• Eylemler  (actons ): Ajan, çevres üzernde farklı eylemler gerçekleştrr . Bu eylemler ajanın yapableceğ
şlemler temsl eder .
• Ödül  (rewar d): Her eylemn sonucunda ş yapan ajan, br ödül  veya ceza (punshment ) alır. Ödül yalnızca
olumlu ger bldrm temsl etmes dışında olumsuz gerbldrm (cezayı) çeren genel br başlık halnde de
kullanılmaktadır . Kısaca, ajanın olayı ne kadar y veya kötü gerçekleştrdğn yansıtan br ger bldrmdr .
• Poltka  (polcy ): Poltka, ajanın belrl br durumda hang eylem gerçekleştrmes gerektğn tanımlar .
Poltka, ajanın ödüller maksmze etme stratejlern belrlemektedr .
• Durum  (state ): Çevrenn anlık durumunu temsl etmektedr . Ajan, durumu değerlendrdkten sonra br


Pekştrmel öğrenme algortmalarının çoğu dern snr ağlarını ( deep neural networks ) kullanır . Pekştrmel
öğrenme algortmaları, ortamda mevcut durum ve eylem türlernn sayısına göre üç ana kategorye ayrılmıştır
(AlMahamd & Grolnger , 2021): 1) sınırlı sayıda durum ve ayrık eylemler , 2) sınırsız sayıda durum ve ayrık
eylemler ve 3) sınırsız durum sayısı ve sürekl eylemler . Deep Q-Networks (DQN), Deep SARSA
pekştrmel öğrenme algortmalarına örnek olarak verleblr .

## 1.5. Ver Madenclğ

Toprak yığınları arasında değerl taşlar , metaller bulmak madenclk olarak adlandırıldığı gb büyük ver
çnde saklı değerl blgnn keşfedlmes de ver madenclğ ( data mnng ) olarak adlandırılmıştır . Ver
madenclğ “büyük ölçekl verler arasından blgy elde etme ş” olarak tanımlanmaktadır (Özkan, 2008).
Ver madenclğ büyük ver tabanlarında, ver ambarlarında, web sayfalarında, dğer büyük blg depolarında
veya ver akışlarında örtülü olarak depolanan veya yakalanan blgy temsl eden kalıpların otomatk veya
uygun şeklde çıkarılmasıdır (Han & Kamber , 2006). Ver madenclğ sayesnde şletmeler karar verme
süreçlern gelştreblr ve rekabet avantajı sağlayablr .
Ver madenclğ ve verden blg keşf ( Knowledge Dscovery fr om Data - KDD ) kavramları km
kaynaklarda brbrlernn yerne kullanılsa da ver madenclğ verden blg keşf sürecnn br adımıdır (Han
& Kamber , 2006). Sürece başlarken tıpkı makne öğrenmes sürecnde olduğu gb br görev , problem veya
hedefn tanımlanması gerekmektedr . Bu, analzler sonucunda ne tür blglern keşfedlmes ve hang
sonuçların elde edlmes gerektğnn anlaşılmasını sağlayacaktır . Makne öğrenmes sürecnde olduğu gb
verden blg keşf sürecnde de sahp olunması gereken en öneml unsur yne “ver”dr . Ele alınan probleme
uygun ver elde edldkten sonra ver temzleme, ver bütünleştrme, ver seçm, ver dönüştürme, ver
madenclğ, örüntü değerlendrme ve blg gösterm adımları sırasıyla gerçekleştrleblr (Şekl 4) (Han &
Kamber , 2006):
1)   Ver Temzleme  (Data Cleanng ): Verlern temzlenmes ve düzenlenmes aşamasıdır . Bu aşamada
eksk, yanlış veya tutarsız verler düzeltlr veya çıkarılır . Ver temzleme aşaması ver kaltesn artırma,
doğru ve güvenlr sonuçlar elde etmek çn önemldr .
2)   Ver Bütünleştrme  (Data Integraton ): Ver bütünleştrme, farklı kaynaklardan gelen verlern
brleştrlmesn fade eder . Verler aynı format ve yapıya getrlr veya farklı ver kaynaklarından gelen
verler uyumlu br şeklde brleştrleblr .
3)   Ver Seçm  (Data Selecton ): Ver seçm, sürece dahl edlecek verlern belrlenmesn çerr . İhtyaca
uygun verlern seçlmes analz süresnn kısaltılması ve analz sonuçlarının yleştrlmes gb avantajlar
sağlayablr .
4)   Ver Dönüştürme  (Data T ransformaton ): Ver dönüştürme, verlern analz çn uygun br forma
getrlmesn çerr . Bu aşamada verlern ölçeklendrlmes/normalzasyonu veya yen özellklern
oluşturulması gb şlemler gerçekleştrlr .
5)   Ver Madenclğ  (Data Mnng ): Ver madenclğ, gzl ve değerl örüntü ve şablonların verden
çıkarılması çn algortmaların ver setne uygulanması aşamasıdır . Makne öğrenmes ve statstksel
teknkler kullanılarak verler analz edlr , modellemeler yapılır ve gzl blglere ulaşılır .
6)   Örüntü Değerlendrme  (Pattern Evaluaton ): Örüntü değerlendrme aşaması, ver madenclğ analz
sonuçlarının ncelenmes ve değerlendrlmesn fade eder .
7)   Blg Gösterm  (Knowledge Pr esentaton ): Son aşama elde edlen analz sonuçlarının raporlanmasını
çerr . Blglern anlaşılır şeklde sunulması hedeflenr . Blg gösterm aşamasında çeştl raporlar , grafkler
veya faydalı dğer farklı formatlar aracılığıyla sunulablr . Böylelkle tüm süreçten elde edlen sonuçlar
anlamlı br bçmde karar verclere sunulablecektr .
Verden blg keşf sürekl br süreç olarak değerlendrleblr . Yan blg çıkarımından ver toplamaya kadar
gerek duyulan adımlarda ger dönüş sağlanarak ş htyaçları ve verlern değşen doğasına yönelk çeştl


Ver madenclğ çok dsplnl br çalışma alanıdır . Bu noktada ver madenclğ le doğrudan lşkl statstk,
matematk, blgsayar blmler gb alanların yanı sıra sektör temelnde şe yarar blg brkmn sağlayacak
olan sosyoloj, pskoloj, ekonom, syaset, tıp, sağlık vb. pek çok farklı alandan da araştırmacıların ş brlğ
çnde çalışmalarına htyaç duyulablr .
Ver madenclğ ve makne öğrenmes, ver analz ve blg çıkarma süreçleryle yakından lşkl k
kavramdır . Her k alan da ver analz le lgldr ve kullanılan algortmaların çoğu ortaklık göstermektedr;
ancak odak ve süreçlernde bazı farklılıklar bulunmaktadır .


Şekl 4: Verden blg keşf (Han & Kamber , 2006).
Ver madenclğ büyük ver setler çndek desenlern, lşklern ve anlamlı blglern keşfedlmesn
hedefler . Odak noktası daha önce blnmeyen anlamlı ver şablonları/örüntüler ortaya çıkarablmektr . Ver
madenclğ genellkle keşfsel br süreç olarak görülür . Makne öğrenmes, çeştl algortmaların ve öğrenme
stratejlernn kullanıldığı yapay zekânın br alt çalışma alanıdır . Temelde verden öğrenme şnn
gerçekleştrleblmesn ve sonucunda geleceğe yönelk modeller oluşturmayı amaçlar .
Ver madenclğ ve makne öğrenmes süreçler bağlamında belrl br görevn tanımlanması, ver ön-şleme,
algortmaların ver setne uygulanması ve model değerlendrmes aşamalarının her k yöntemde de benzerlk
gösterdğ görüleblr . Ver madenclğ, büyük ver çndek gzl şablon ve örüntülern keşfne odaklanırken
makne öğrenmesnde odak, model oluşturma ve eğtme aşamalarında yoğunlaşır . Nhayetnde kend kendne


Ver madenclğ sürecnn çıktıları verdek desenler ve lşkler tanımlayan çeştl özet ve görselleştrmeler
çereblr . Bu çıktılar daha fazla analz veya ş kararları almak çn kullanılablr . Makne öğrenmes çıktıları
se tahmn, sınıflandırma ya da örüntü tanıma kablyetlern çerr . Öğrenlen modeller , yen verler
değerlendrmek ve gelecektek olayları tahmn etmek çn kullanılır .

## 1.6. Açıklayıcı, Tahmnsel ve Kuralcı Ver Analtğ

Açıklayıcı ( descrptve ), tahmnsel ( predctve ) ve kuralcı ( prescrptve ) analz ver analtğnn üç öneml
yaklaşımıdır . Açıklayıcı ver analtğ nde blg keşf ve mevcut vernn karakterstk ve özellklernn
anlaşılması amaçlanırken, tahmnsel ver analtğnde  gelecektek olayların tahmn ya da öngörüsüne
odaklanılarak model oluşturulmaktadır . Açıklayıcı ver analtğ mevcut blglern anlaşılmasına,
açıklanmasına ve yorumlanmasına yardımcı olurken; tahmnsel analz gelecektek kararları ve eylemler
destekler .
Açıklayıcı ver analtğ, ver setndek desenler ve lşkler açığa çıkarmak ve mevcut very yorumlamak
çn kullanılmaktadır . Bunları gerçekleştreblmek çn çeştl statstksel özet, grafk, tablo ve dğer ver
görselleştrme yöntemler kullanılarak ver set analz edlr . Ortalama, medyan, varyans, standart sapma,
kartl değerler gb temel statstksel ölçütler sıklıkla kullanılır . Örneğn pazar araştırması ncelemes, br
şletmeye at geçmş performans analz, demografk verlern ncelenmes vb.
Tahmnsel ver analtğ, adından da anlaşılacağı gb gelecektek olayları tahmn etme ya da belrl br sonuca
ulaşma hedefn taşımaktadır . Verye dayalı öngörülerde bulunmak ve olası sonuçları tahmn etmek çn
kullanılır . Makne öğrenmes ve statstksel modeller tahmnsel analz yöntemler arasındadır . Örneğn
borsada hsse sened fyatlarının gelecektek durumlarının tahmn, müşter satın alma davranışlarının
öngörüsü, hava durumu tahmn vb.
Kuralcı  ver analtğ , tahmnler ve geçmş verlere dayanarak spesfk br hedefe veya belrl br sonuca
ulaşmak çn nasıl br eylem planı oluşturulması konusunda önerler sunar . Kuralcı ver analtğ, genellkle
karar destek sstemlernde veya stratejk planlama süreçlernde kullanılır . Bu analz türü, daha etkl ve
optmze edlmş kararların alınmasına yardımcı olur .


**Bölüm Özet**

Bu bölüm yapay zekâ ( artfcal ntellgence ) le lgl temel konseptlern verlmesyle başlamıştır . Yapay
zekânın kısa tarhne odaklanarak, bu alanın nasıl evrmleştğ ve günümüzdek öneml klometre taşları
ncelenmştr . Blgsayarların düşünme yeteneğ kazanma çabalarının nasıl başladığı ve zaman çnde bu
çalışmaların nasıl gelştğ ele alınmıştır . Yapay zekânın temel türler tanımlanmış ve genel blgler
verlmştr .
Bölümde makne öğrenmes ( machne learnng ) kavramı açıklanmıştır . Bu bölümde maknelern yan
blgsayarların deneymlerden öğrenme kapastesne sahp olmasının altında yatan temel prenspler
açıklanmıştır . Geleneksel programlama ve makne öğrenmes arasındak farklar vur gulanmıştır . Klask
programlamanın sınırlamaları ele alınmış, makne öğrenmesnn esnek ve adaptf yapısına odaklanılmıştır .
Makne öğrenmesnde kullanılan temel stratejlere genel br bakış sunulmuştur . Danışmanlı ( supervsed ),
danışmansız ( unsupervsed ) ve pekştrmel ( renfor cement ) öğrenme stratejlernn temel prenspler ele
alınmıştır . Danışmanlı öğrenmede sınıflandırma ve regresyon görevler, danışmansız öğrenmede se
kümeleme görev üzernde durulmuştur .
Yne bölüm kapsamında ver madenclğnn temel unsurları açıklanmıştır . Büyük ver setler çndek
desenler ortaya çıkarma ve verden blg keşf ( Knowledge Dscovery fr om Data- KDD ) sürecne
değnlmştr . Son olarak açıklayıcı ( descrptve ), tahmnsel ( predctve ) ve kuralcı ( prescrptve ) ver analtğ
kavramları açıklanmış, bu üç kavram arasındak farklar ve her brnn uygulama alanları hakkında blgler


**Kaynakça**

AlMahamd, F ., & Grolnger , K. (2021). Renforcement learnng algorthms: An overvew and classfcaton.
2021 IEEE Canadan Confer ence on Electrcal and Computer Engneerng (CCECE) , 1-7.
Alpaydın, E. (2014). Introducton to Machne Learnng . MIT  Press.
Annon, A., Benczur , P., Bertold, P ., Delpetrev , B., De Prato, G., Fejoo, C., Fernandez Macas, E., Gomez
Guterrez, E., Iglesas Portela, M., Junklewtz, H., Lopez Cobo, M., Martens, B., Fgueredo Do Nascmento,
S., Natv, S., Polvora, A., Sanchez Martn, J. I., Tolan, S., Tuom, I., & Vesnc Alujevc, L. (2018). Artfcal
Intellgence: A European Perspectve  (EUR 29425 EN). Publcatons Of fce of the European Unon.
https://publcatons.jrc.ec.europa.eu/repostory/handle/JRC1 13826
Balaban, M. E., & Kartal, E. (2018). Ver Madenclğ ve Makne Öğr enmes T emel Algortmaları ve R Dl le
Uygulamaları  (2. bs). Çağlayan Ktabev.
Balkuv , E. (2020). Beynnz Hayatınızı Nasıl Şekllendrr?  (1. bs). Müptela Yayınları.
Bostrom, N. (2016). The control problem. Excerpts from superntellgence: Paths, dangers, strateges.
Scence Fcton and Phlosophy: Fr om T me T ravel to Superntellgence , 308-330.
Bostrom, N., & Yudkowsky , E. (2014, Hazran). The ethcs of artfcal ntellgence . The Cambrdge
Handbook of Artfcal Intellgence; Cambrdge Unversty Press.
https://do.or g/10.1017/CBO9781 139046855.020
Camastra, F ., & Vncarell, A. (2008). Machne Learnng for Audo, Image and V deo Analyss: Theory and
Applcatons . Sprnger .
Delpetrev , B., Tsnarakl, C., & Kostc, U. (2020). Hstorcal Evoluton of Artfcal Intellgence  (EUR
30221EN). Publcatons Of fce of the European Unon. https://op.europa.eu/en/publcaton-
detal/-/publcaton/6264ac29-2d3a-1 1eb-b27b-01aa75ed71a1/language-en
Devln, J., Chang, M.-W ., Lee, K., & Toutanova, K. (2019). BERT : Pre-tranng of Deep Bdr ectonal
Transformers for Language Understandng  (arXv:1810.04805). arXv .
https://do.or g/10.48550/arXv .1810.04805
Dhar , V. (2013). Data scence and predcton. Communcatons of the ACM , 56(12), 64-73.
https://do.or g/10.1 145/2500499
Dxon, M. F ., Halpern, I., & Blokon, P . (2020). Machne Learnng n Fnance: Fr om Theory to Practce  (1st
ed. 2020 edton). Sprnger .
draw .o. (2023). Draw .o. https://app.dagrams.net/
Gherheș, V. (2018). Why are we afrad of Artfcal Intellgence (AI)? European Revew Of Appled
Socology , 2286-2102.
Good, I. J. (1965). Speculatons Concernng the Frst Ultrantellgent Machne. Içnde F . L. Alt & M.
Rubnof f (Ed.), Advances n Computers  (C. 6, ss. 31-88). Elsever . https://do.or g/10.1016/S0065-
2458(08)60418-0
Han, J., & Kamber , M. (2006). Data Mnng: Concepts and T echnques  (2. bs). Mor gan Kaufmann
Publshers.


Hernández-Orallo, J. (2017). Evaluaton n artfcal ntellgence: From task-orented to ablty-orented
measurement. Artfcal Intellgence Revew , 48, 397-447.
Jan, P ., Garbald, J. M., & Hrst, J. D. (2009). Supervsed machne learnng algorthms for proten structure
classfcaton. Computatonal Bology and Chemstry , 33(3), 216-223.
https://do.or g/10.1016/j.compbolchem.2009.04.004
Kartal, E. (2015). Sınıflandırmaya Dayalı Makne Öğr enmes T eknkler V e Kar dyolojk Rsk
Değerlendrmesne İlşkn Br Uygulama  [Doktora Tez]. İstanbul Ünverstes, Fen Blmler Ensttüsü.
Kartal, E. (2022). A Comprehensve Study on Bas n Artfcal Intellgence Systems: Based or Unbased AI,
That’ s the Queston! Internatonal Journal of Intellgent Informaton T echnologes (IJIIT) , 18(1), 1-23.
https://do.or g/10.4018/IJIIT .309582
Kartal, E., Balaban, M. E., & Bayraktar , B. (2021). Küresel COVID-19 Salgınının Dünyada ve Türkye’de
Değşen Durumu ve Kümeleme Analz. İstanbul Tıp Fakültes Der gs, 84(1), 9-19.
https://do.or g/10.26650/IUITFD.2020.0077
Kartal, E., & Schwartz, O. (2022). What Is Deep Learnng and How Has It Helped the COVID-19 Pandemc?
İçnde Ş. Omerak Çekrdekc, Ö. İngün Karakış, & S. Gönültaş (Ed.), Handbook of Resear ch on
Inter dscplnary Perspectves on the Thr eats and Impacts of Pandemcs  (1. bs, ss. 337-360). IGI Global;
10.4018/978-1-7998-8674-7.ch018. https://www .g-global.com/chapter/what-s-deep-learnng-and-how-has-
t-helped-the-covd-19-pandemc/291927
Kotsants, S. B., Zaharaks, I. D., & Pntelas, P . E. (2006). Machne learnng: A revew of classfcaton and
combnng technques. Artfcal Intellgence Revew , 26(3), 159-190. https://do.or g/10.1007/s10462-007-
9052-3
Mtchell, T. M. (1997). Machne Learnng  (1st Edton). McGraw-Hll Scence/Engneerng/Math.
Mohr, M., Rostamzadeh, A., & Talwalkar , A. (2012). Foundatons of Machne Learnng . The MIT  Press.
Nabyev , V. V. (2005). Yapay zeka: Pr oblemler -yöntemler -algortmalar  (2. bs). Seçkn Yayıncılık.
Nlsson, N. J. (2018). Yapay zekâ geçmş ve geleceğ  (M. Doğan, Çev .). Boğazç Ünverstes Yayınev.
Özen, Z., Kartal, E., & Emre, İ. E. (2017). Eğtmde Büyük Ver. İçnde H. F . Odabaşı, B. Akkoyunlu, & A.
İşman (Ed.), Eğtm T eknolojler Okumaları 2017  (1. bs, ss. 183-204). Pegem Akadem.
http://www .tojet.net/e-book/eto_2017.pdf
Özkan, Y. (2008). Ver madenclğ yöntemler . Papatya Yayıncılık Eğtm.
Rouhanen, L. (2018). Artfcal Intellgence: 101 Thngs Y ou Must Know T oday About Our Futur e.
CreateSpace Independent Publshng Platform.
Sarker , I. H. (2021). Machne Learnng: Algorthms, Real-W orld Applcatons and Research Drectons. SN
Computer Scence , 2(3), 160. https://do.or g/10.1007/s42979-021-00592-x
SAS. (2023). Artfcal Intellgence (AI): What t s and why t matters .
https://www .sas.com/en_us/nsghts/analytcs/what-s-artfcal-ntellgence.html
Say, C. (2020). Yen Dünya, Y en Ağ (1. bs). Destek Yayınları.
Schank, R., & Baress, R. (2021). What Are You Afrad Of? AI Doesn’ t Kll People; People Kll People.
AIofAI’21: 1st W orkshop on Adverse Impacts and Collateral Effects of Artfcal Intellgence T echnologes .
Slver , D., Schrttweser , J., Smonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker , L., La,
M., Bolton, A., Chen, Y., Lllcrap, T., Hu, F ., Sfre, L., van den Dressche, G., Graepel, T., & Hassabs, D.
(2017). Masterng the game of Go wthout human knowledge. Natur e, 550(7676), Artcle 7676.


Smon, H. A. (1984). Why should machnes learn? İçnde R. S. Mchalsk, J. G. Carbonell, & T. M. Mtchell
(Ed.), Machne learnng: An artfcal ntellgence appr oach  (ss. 25-37). Sprnger .
Sokolova, M., & Lapalme, G. (2009). A systematc analyss of performance measures for classfcaton tasks.
Informaton Pr ocessng & Management , 45(4), 427-437.
Sung, S. W., Baek, H., Sm, H., Km, E. H., Hwangbo, H., & Jang, Y. J. (2020, Temmuz 9). Breakng
Moravec’ s Paradox: Vsual-Based Dstrbuton n Smart Fashon Retal. arXv:2007.09102 [Cs, Eess] . The
ffth nternatonal workshop on fashon and KDD (KDD 2020), San Dago, CA.
http://arxv .org/abs/2007.09102
Sutton, R. S., & Barto, A. G. (1998). Renfor cement Learnng: An Intr oducton  (1st Edton). MIT  press.
http://webdocs.cs.ualberta.ca/~sutton/book/chapter1.pdf
TDK. (2023). Öğrenmek . https://sozluk.gov .tr/


**Ünte Soruları**

Soru-1 :
Yapay zekânın sm babası kmdr?
(Çoktan Seçmel)
(A) Andrew Ng
(B) Marvn Mnsky
(C) John McCarthy
(D) Alan Turng
Hans Moravec
Cevap-1 :
John McCarthy
Soru-2 :
Aşağıdaklerden hangs ya da hangler yapay zekâ türler arasındadır?
I. Dar yapay zekâ
II. Güçlü yapay zekâ
III. Süper yapay zekâ
IV. İler yapay zekâ


(A) Yalnız I
(B) Yalnız II
(C) I ve II
(D) II ve IV
(E) I, II, III
Cevap-2 :
I, II, III
Soru-3 :
Aşağıdaklerden hangs makne öğrenmes konusunda öneml dört unsur arasında yer almaz ?
(Çoktan Seçmel)
(A) Görev
(B) Ver
(C) Algortma
(D) Programlama Dl
Performans
Cevap-3 :
Programlama Dl
Soru-4 :
Aşağıdaklerden hangs ya da hangler makne öğrenmes algortmalarının özellklernden br değldr ?
(Çoktan Seçmel)
(A) Verye dayalıdır .
(B) Verdek kalıpları genelleştreblme yetenekler bulunur .
(C) Kara-kutu olarak adlandırılan teknklern daha az yorumlanablrlk özellğ vardır .
(D) Ver kaltes öğrenme sürecn etkler .
(E) Kural tabanlı determnstk görevler çn uygundur .
Cevap-4 :
Kural tabanlı determnstk görevler çn uygundur .
Soru-5 :


(Çoktan Seçmel)
(A) Br e-tcaret platformunda, kullanıcıların öncek alışverş geçmş ve terchler temel alınarak müşterlere
özel ürün önerler sunar .
(B) Br sağlık uygulaması, kullanıcının günlük aktvtelern takp eder ve uzman br doktorun önerlerne
dayanarak kşye özel egzersz programları oluşturur .
(C) Sürücüsüz br araç, trafk durumunu sürekl olarak değerlendrr ve bu blglere dayanarak anlık rota
değşklkler yapar .
(D) Br dl öğrenme uygulaması, kullanıcının dl becerlern sürekl olarak değerlendrr ve buna göre özel
dl pratkler sunar .
Br haber öner uygulaması, kullanıcının okuma alışkanlıkları ve tıklama geçmşne dayanarak özelleştrlmş
haber önerler sunar .
Cevap-5 :
Sürücüsüz br araç, trafk durumunu sürekl olarak değerlendrr ve bu blglere dayanarak anlık rota
değşklkler yapar .
Soru-6 :
Aşağıdaklerden hangs danışmansız öğrenme kapsamında ncelenr?
(Çoktan Seçmel)
(A) Br fotoğraf tanıma uygulamasının ver setnde etketlenmemş büyük br fotoğraf koleksyonunu analz
ederek benzer özellklere sahp fotoğrafları kümelemes.
(B) Yen br e-postanın stenmeyen m yoksa öneml br let m olduğunun belrlenmes.
(C) Tıbb görüntülern etketlenmş verler le hastalıkların teşhs.
(D) Br fotoğraf tanıma uygulamasının br fotoğrafta hang nesnelern bulunduğunu sınıflandırması.
Etketl el yazısı örnekler kullanılarak el yazısının daha y tanınması.
Cevap-6 :
Br fotoğraf tanıma uygulamasının ver setnde etketlenmemş büyük br fotoğraf koleksyonunu analz
ederek benzer özellklere sahp fotoğrafları kümelemes.
Soru-7 :
Aşağıdaklerden hangs pekştrmel öğrenme kapsamındak öneml termler arasına grmez ?
(Çoktan Seçmel)
(A) Ajan
(B) Çevre


(D) Ödül
(E) Suç
Cevap-7 :
Suç
Soru-8 :
Aşağıdaklerden hangs verden blg keşf sürec adımlarından br değldr ?
(Çoktan Seçmel)
(A) Ver temzleme
(B) Ver toplama
(C) Ver bütünleştrme
(D) Ver madenclğ
Blg gösterm
Cevap-8 :
Ver toplama
Soru-9 :
Br şrket, satışlarını ncelemek ve belrl br kampanyanın etksn değerlendrmek styor . Bunun çn şrkette
hazır br ver set bulunuyor . Hang analz türü mevcut vernn karakterstk ve özellklernn anlaşılması çn
daha uygundur?
(Çoktan Seçmel)
(A) Tahmnsel ver analtğ
(B) Gözlemsel ver analtğ
(C) Karşılaştırmalı ver analtğ
(D) Açıklayıcı ver analtğ
Kuralcı ver analtğ
Cevap-9 :
Açıklayıcı ver analtğ
Soru-10 :
Aşağıdak seçeneklern hangsnde tahmnsel ve açıklayıcı ver analtğ doğru tanımlanmıştır?


(A) Tahmnsel ve açıklayıcı analzler vernn karakterstk ve özellklernn anlaşılmasına odaklanır .
(B) Tahmnsel ve açıklayıcı analzler gelecektek olayların tahmn ya da öngörüsünde kullanılır .
(C) Tahmnsel ve açıklayıcı analzler tahmnler ve geçmş verlere dayanarak belrl br sonuca ulaşmak çn
nasıl br eylem planı oluşturulması konusunda önerler sunar .
(D) Açıklayıcı analzler vernn karakterstk ve özellklernn anlaşılmasına odaklanır , tahmnsel analzler se
gelecektek olayların tahmn ya da öngörüsünde kullanılır .
Tahmnsel analzler vernn karakterstk ve özellklernn anlaşılmasına odaklanır , açıklayıcı analzler se
gelecektek olayların tahmn ya da öngörüsünde kullanılır .
Cevap-10 :
Açıklayıcı analzler vernn karakterstk ve özellklernn anlaşılmasına odaklanır , tahmnsel analzler se


# 2. Makine Öğrenmesi Sür ec


**Özlü Söz**

Geleceğ tahmn etmek shr değl, yapay zekâdır .
Prof. Dave Waters , Oxfor d Unversty , St Cr oss College Emekl Öğr etm Üyes


**Kazanımlar**

1.   Makne öğrenmes sürecnn genel kapsamını anlar .
2.   Makne öğrenmes sürecnn aşamalarını sıralayablr .
3.   Br problemn makne öğrenmes bağlamında nasıl tanımlanacağını blr .
4.   Ver elde etme sürecnn önemn kavrar , farklı ver kaynaklarından ver toplayablr .
5.   Ver türlern ayırt edeblr .
6.   Ver anlama şlemlern gerçekleştreblr .
7.   Very özetleme ve görselleştrme teknklern blr .
8.   Boyut azaltma yöntemlern anlayablr .
9.   Ver temzleme sürecn blr .
10. Aykırı değer tespt çn yöntemler öğrenp uygulayablr .
11. Temel eksk değerler tamamlama yöntemlern anlar .
12. Ver normalzasyonu konseptn kavrar .
13. Yapay ( dummy ) kodlama kullanarak kategork verlern nasıl şleneceğn blr .
14. Very ayrıklaştırma yöntemlern anlar .
15. Temel makne öğrenmes algortmalarını blr .
16. Model performansını değerlendrmek çn kullanılan yöntemler blr ve uygular .
17. İkl-sınıf sınıflandırma, çoklu-sınıf sınıflandırma ve regresyon problemlernde kullanılan temel bazı
performans değerlendrme yöntemlern blr .


19. Eğtlmş makne öğrenmes modeln gerçek dünya problemlerne uygulamak çn çeştl alternatf yollar
blr.


**Brlkte Düşünelm**

1.   Makne öğrenmes sürecnde hang aşamalar yer alır?
2.   Br makne öğrenmes projesnde problemn nasıl tanımlanması gerektğne lşkn nelere dkkat
edlmeldr?
3.   Ver elde etme sürecnn önem nedr? Makne öğrenmes analzlernde hang ver kaynakları
kullanılablr?
4.   Ver elde etme aşamasında karşılaşılablecek zorluklar nelerdr?
5.   Ver türlern anlamak br makne öğrenmes projes çn neden krtktr?
6.   Ver hazırlama aşamasında hang teknkler kullanılablr? Örnek vererek açıklayınız.
7.   Very anlama ve hazırlama sürecnde yapılan hatalar modeln performansını nasıl etkleyeblr?
8.   Makne öğrenmes algortması ve makne öğrenmes model kavramları brbrlernn yerne kullanılablr
m, kullanılamazsa aralarındak farklar nelerdr?
9.   İkl ve çoklu-sınıf sınıflandırma performansının değerlendrlmes çn hang yöntemler kullanılablr?
10. Kümeleme kaltesnn değerlendrlmes çn hang yöntemler kullanılablr?
11. Eğtlmş br modeln gerçek dünya problemlerne uygulanması nasıl gerçekleştrleblr?


**Başlamadan Önce**

Makne öğrenmes, günümüzde brçok alanda büyük br etk oluşturmuş ve ver odaklı problemler çözmek
çn güçlü br araç halne gelmştr . Bu bölümde makne öğrenmes sürecn adım adım anlamak ve başarıyla
uygulamak çn gerekl temel kavramlar anlatılmıştır . Makne öğrenmes sürec, Ver Madenclğ çn
Çapraz Endüstr Standard Sür eç Model  (CRoss-Industry Standar d Process for Data Mnng – CRISP-
DM) adımları le ele alınmıştır .
Sürecn lk adımında br makne öğrenmes problemnn nasıl tanımlanması gerektğne odaklanılmıştır .
Ardından makne öğrenmes projelernn temel malzemes olan “ver”nn nasıl elde edleceğ ele alınmıştır .
Very anlama başlığı altında bu amaçla kullanılan temel kavramlar detaylı br şeklde açıklanmıştır . Ver
hazırlama adımı vernn modelleme aşamasına hazırlanması çn yapılan şlemler kapsamaktadır . Bu
bölümde; ver ayrıklaştırma  (data dscr etzaton ), aykırı değer  tespt  (outler detecton ), eksk değerlern
tamamlanması  (mssng data mputaton ), ver normalzasyonu  (data normalzaton ) gb çeştl ver
hazırlama şlemler üzernde durulmuştur . Modelleme başlığında br makne öğrenmes modeln oluşturan
temel elemanlardan söz edlmştr . Sonrasında kl ayırma  (hold-out ), tabakalı örnekleme  (stratfed
samplng ), çapraz geçerleme  (cross-valdaton ) performans değerlendrme yöntemler ve farklı performans
değerlendrme ölçütler detaylı br şeklde açıklanmıştır . Ayrıca kümeleme analz sonucunda en y küme


drsek ( elbow ) yöntem, Slhouette katsayısı kavramlarına değnlmştr . Son olarak modeln uygulamaya
geçrlmes ele alınmıştır .


## 2.1. Makne Öğr enmes Sür ec Kapsamı

Br öncek bölümde makne öğrenmes stratejlerne değnlerek danışmanlı, danışmansız ve pekştrmel
öğrenme gb üç temel öğrenme türü detaylarıyla açıklanmıştı. Danışmanlı öğr enme de, makneye deneym
olarak sunulacak ver setnde tahmn sağlayan (tahmn edc) ntelklern yanı sıra kategork veya nümerk
br hedef ntelk de yer almaktadır . Örneğn; e-posta spam fltres bu öğrenme türüne örnek olarak verleblr .
E-postalar çnde gerçekte spam olan ve spam olmayanlar etketlenerek (bu blg hedef ntelk sütununda
tutulur) makne öğrenmes algortması eğtlr . Eğtm aşaması tamamlandıktan sonra gelen yen e-postalar
“spam” veya “spam değl” olarak öngörüleblr . Danışmansız öğr enme  yöntemnde se ver setnde br hedef
ntelk bulunmaz, yalnızca tahmn sağlaya ntelkler le öğrenme sürec tamamlanır . Örneğn br perakende
şrket geçmş satın alma şlem hareketlernden yola çıkarak müşterlern bell başlı gruplara ayırmak
steyeblr; ancak bunun çn danışmanlı öğrenmede olduğu gb daha önceden etketlenmş verye htyaç
duymaz. Danışmansız öğrenme algortmaları, tahmn sağlayan ntelklerden yola çıkarak (yaş, cnsyet, gelr
durumu, vb.) benzer alışverş alışkanlıklarına/davranışlarına sahp müşterler kümeleyeblr . Pekştrmel
öğrenme  se, öğrenme şn gerçekleştren ajanın (algortma) çevreyle etkleşm sayesnde aldığı poztf ya
da negatf ger bldrmler sonucunda öğrenme sürecn tamamlar . Örneğn br otonom araç tarafından
kullanılan navgasyon, araç çevresn algılayablr ve tanımlanan hedef noktaya güvenl br bçmde ulaşmak
çn nasıl yolculuk yapacağını kend deneymlerne dayalı olarak öğrenr .
Tanımlanan br görev makne öğrenmesnden faydalanarak yerne getreblmek çn lteratürde brbrne
yakın sayılablecek yaklaşımlar bulunmaktadır . Bu ktapta sstematk br yaklaşım olarak makne öğrenmes
sürecnde Ver Madenclğ çn Çapraz Endüstr Standard Sür eç Model  (CRoss-Industry Standar d
Process for Data Mnng – CRISP-DM ) adımları ele alınmıştır (Şekl 5) (Balaban & Kartal, 2018; Shearer ,
2000; Wrth & Hpp, 2000). CRISP-DM; problemn tanımlanması ( busness understandng ), very anlama
(data understandng ), ver hazırlama ( data pr eparaton ), modelleme ( modelng ), modeln değerlendrme ve
seçm ( evaluaton ) ve modeln uygulamaya geçrlmes ( deployment ) olmak üzere altı aşamadan


Şekl 5: CRISP-DM adımları (Balaban & Kartal, 2018; Shearer , 2000; Wrth & Hpp, 2000).

## 2.2. Pr oblemn Tanımlanması

Makne öğrenmesnde problem çerçevesnn belrlenmes  (problem framng ), arkadaşının yaklaşan doğum
günü çn lezzetl br pasta pşrmeye karar veren We'nn hkayes le lteratürde somut hale getrlmeye
çalışılmıştır (quanthub, 2023). Daha önce pasta yapmamış olan We başlangıçta tam olarak ne tür br pasta
yapmak stedğne karar verme aşamasındadır . Bu lk karar verme adımı, makne öğrenmes sürecndek
problem çerçevesnn belrlenmesnn tam adı olarak tanımlanmaktadır . Br ressam da br tualn başına
geçerek gelş güzel tüm boyaları fırçayla tuale sürerek resm yapmaya başlamaz. Öncelkle yapmak stedğ
resmn neye benzeyeceğn tanımlaması/hayal etmes gerekr . Br doğa resm m, portre m yoksa farklı türde
br resm m yapmak stemektedr? Bu oldukça öneml br aşamadır , çünkü bu lk karar seçeceğ renklerden
kullanacağı tual boyutuna ve çeşdne kadar daha sonrak tüm sürece etk edecektr . Benzer şeklde makne


doğru “renklern” veya vernn elde edlmes ve bunları “karıştırmak” veya şlemede en uygun yöntemlern
seçmnde rehberlk edecektr .
Özetle makne öğrenmes sürecnde y tanımlanmış br öğrenme problemnn ortaya konması makne
öğrenmes sürecnn başarıya ulaşması çn temel br adım olarak görülmektedr . Bu aşama aynı zamanda
CRISP-DM’nn dğer adımlarının da genel çerçeveler le ortaya konmasını sağlayacaktır . Problemn
tanımlanması aşamasında makne öğrenmes projesnn ne amaçla yapıldığı ve hedeflern ne olduğu açıkça
tanımlanır . Aşağıda farklı makne öğrenmes problemlerne örnekler verlmştr:
• Br hastanın amelyat sonrası ölüm rsknn öngörüsü.
• X ışınları veya MRI taramaları gb tıbb görüntülerden hareketle hastalıkların teşhs.
• Br otomobln sürüş sırasında kaza rsk tahmn.
• Br şehrdek trafk yoğunluğunun tahmn.
• Meteoroloj versne göre gelecektek hava koşullarının tahmn.
• Müşterlere, lg duyablecekler ürünlern öners.
• Br şrket çalışanlarına at performans tahmn.
• Öğrencler çn kşselleştrlmş öğrenme planı öners.
• Kütüphane zyaretçlernn geçmş okuma alışkanlıklarına göre onlara yen ktap tavsyelernde bulunma.
• Geçmş zleme alışkanlıklarına göre yen flm önerme.
Makne öğrenmes problem tüm detaylarıyla ortaya konduktan sonra CRISP-DM’nn br sonrak adımı olan
very anlama aşamasına geçleblr .

## 2.3. Vernn Elde Edlmes

Ver, makne öğrenmes sürecnn odağında yer almaktadır . Bölüm 1.2’de Mtchell (1997)’ın “deneym”
olarak tarf ettğ ver, makne öğrenmes modellernn öğrenme sürec çn gerekmektedr . Bu sebeple
öncelkle makne öğrenmes çn htyaç duyulan vernn elde edlmes  (data gatherng ) gerekr .
Makne öğrenmes çalışmaları çn ver farklı yapılarda bulunablr . Yapılandırılmış ver  (structur ed data )
belrl br formata uygun, düzenl ve kolay şleneblecek türdek verlerdr . Yapılandırılmış ver genellkle br
tablo (satır/sütun) veya matrs formundadır . Yapılandırılmış ver denldğnde ver tabanları, elektronk
tablolar (MS Excel ya da CSV  dosyaları) örnek verleblr . Örneğn hasta ver tabanında hastaların ad, soyad,
e-posta adres, telefon numarası, şeker , tansyon, kan sayımı gb hastaneye geldğnde yaptırdığı testlere
lşkn belrl ntelklern yer aldığı br tablo düşünüleblr .
Yapılandırıl mamış ver  (unstructur ed data ), yapılandırılmış vernn aksne belrl br forma sahp olmayan,
düzensz yapıdak verlerdr . Yapılandırılmamış ver denldğnde metn belgeler, ses kayıtları, görüntüler ,
sosyal medya gönderler örnekleneblr . Örneğn br doktorun hastasına lşkn aldığı notlar , sosyal
medyadak metn, resm ya da vdeo gönderler vb.
Analzlerde kullanılacak ver mktarı le modeln performansı arasında kesn br çıkarımda bulunmak
mümkün değldr . Ver arttıkça makne öğrenmes modelnn de performansının artacağı garant edlmez;
ancak statstksel çalışmalarda olduğu gb modeln genelleştreblme yeteneğnn daha y olablmes çn o
popülasyona lşkn yeternce (ya da olabldğnce çok) örnek görmüş olması beklenr . Öte yandan üzernde
çalışılacak konuyla lgl elde herhang br ver yoksa ver temn konusunda nasıl br yol zleneblr?
Bu soruya verleblecek en uygun cevaplardan br kamuya açık erşml ver setlernden ( publc datasets )
faydalanmak olur . Bu tür ver setler belrl br araştırma kapsamında çeştl web steler ya da platformlara


poltkalarına rayet edlerek kullanılablmektedr . Aşağıda kamuya açık ver setlernn yer aldığı bazı popüler
kaynaklar sıralanmıştır .
UCI Makne Öğr enmes Ver Deposu  (UCI Machne Learnng Repostory ) (https://archve.cs.uc.edu ):
UCI, makne öğrenmes çn en esk ve en yaygın kullanılan ver havuzlarından brdr (Şekl 6). Ver setler,
web stesne herhang br üyelk gerekmeden doğrudan ndrleblmektedr . Sınıflandırma, regresyon,
kümeleme gb çeştl makne öğrenmes görevler çn kullanılablecek genş br ver set koleksyonu çerr .
Web stesne grldğnde farklı araştırmacılar tarafından kullanıma sunulan farklı alanlardan brçok ver
setne erşm sağlanablr . Ver setler görev , kullanım alanı, ver tp, anahtar kelme, çerdğ ntelkler ,
örnekler gb farklı seçenekler yardımı le fltreleneblmektedr . Her br ver setne lşkn dernlemesne
blglere de yne web stes aracılığı le ulaşılablmektedr .


Şekl 6: UCI Makne Öğrenmes Ver Deposu web stesnden br görünüm.
Kaggle Ver Setler (https://www .kaggle.com/datasets ): Kaggle, ver blm ve makne öğrenmes yarışmaları
çn popüler br platformdur (Şekl 7). Bu platform, dünyanın çeştl ülkelernden araştırmacılar le ver
sahplern br araya getrmekte ve ödüllü makne öğrenmes yarışmaları düzenlemektedr . Platformda makne
öğrenmes çn kullanılablecek çok sayıda ver set koleksyonu bulunmaktadır . Kaggle web stesne ücretsz
üye olunduktan sonra ver setlernn ndrlmes mümkündür . Ayrıca yne dünyanın çeştl ülkelernden
araştırmacıların makne öğrenmes alanında R ve Python dllernde gelştrdğ kod dosyaları


Şekl 7: CRISP-DM adımları (Balaban & Kartal, 2018; Shearer , 2000; Wrth & Hpp, 2000).
Google Ver Set Arama  (Google Dataset Sear ch): Google Ver Set Arama, kullanıcıların çevrmç olarak
yayınlanmış ver setlern bulmasına olanak tanıyan br arama motorudur . Çeştl alanlardan genş br ver set
yelpazes çermektedr . Bknz. https://datasetsearch.research.google.com/
OpenML:  OpenML, makne öğrenmes ver setlern ve uygulamalarını paylaşmaya ve keşfetmeye yönelk
açık br platformdur . Bknz. https://www .openml.or g
data.gov : data.gov , ABD hükümet tarafından sağlanan halka açık ver setlernn yer aldığı depo platformdur .
İklm, sağlık, eğtm ve ulaşım gb çeştl alanlardan ver setlern çerr . Bknz. https://data.gov/
Amazon Web Servces ( AWS) Açık Erşml  Ver Setler : AWS, makne öğrenmes ve dğer ver analz
görevler çn kullanılablecek br genel ver set koleksyonu sağlar . Bu ver setler genom, astronom ve
ulaşım gb çeştl alanlardan verler çerr . Bknz. https://aws.amazon.com/opendata/
Ayrıca görüntü şleme ( mage pr ocessng ) ve blgsayarlı görü ( computer vson ) alanlarında makne
öğrenmes modellern eğtmek ve test etmek çn yalnızca görüntüye odaklanan bazı ünlü ver setler
bulunmaktadır . Bunların arasında en popüler olanlardan ImageNet, CIF AR 10, CIF AR 100 ve MNIST
hakkında açıklamalara aşağıda yer verlmştr .
ImageNet:  ImageNet, mlyonlarca görüntüden oluşan ve çeştl nesneler ve sahneler çeren br görüntü ver
tabanıdır . Dünya çapındak araştırmacılara büyük ölçekl nesne tanıma modellernn eğtm çn görüntü
verler sağlamaya yönelk devam eden br araştırma çalışmasıdır . Ayrıca ImageNet, çeştl nesne
kategorlern çeren büyük br etket koleksyonuna sahptr . ImageNet, görüntü sınıflandırma ve nesne
tanıma modeller gelştrmek çn sıkça kullanılır . Bknz. https://mage-net.or g/
CIFAR-10  ve CIFAR-100:  CIFAR-10 ve CIF AR-100, 80 mlyon küçük görüntü ver setnn etketl alt
kümelerdr . CIF AR-10 yalnızca 10 farklı nesne sınıfında yer alan örnekler çerrken, CIF AR-100 daha fazla
kategorde örneklerden oluşmaktadır . Bknz. https://www .cs.toronto.edu/~krz/cfar .html
MNIST : El yazısıyla yazılmış rakamlardan oluşan bu ver set, 60.000 örnekten oluşan br eğtm ve 10.000
örnekten oluşan br test ver setne sahptr . NIST'ten temn edleblen daha büyük br kümenn alt kümesdr .
Rakamların boyutu normalleştrlmş ve sabt boyutlu br görüntüde ortalanmıştır . Bknz.


Bu ver kaynakları dışında blmsel der gler makalelerde kullanılan ver setlernn paylaşılması çn makale
yazarlarını ver paylaşımı çn desteklemektedr (Bknz. Elsever (2023)). Bu nedenle özellkle makne
öğrenmes çalışmalarında makale oluşturulurken kullanılan verye erşm sağlanması mümkündür . Sentetk
ver ür etme  (data augmentaton ) özellkle görüntü versnn sınırlı olduğu durumlarda kullanılmaktadır . Bu
yöntemde mevcut ver döndürme, çevrme, yenden ölçeklendrme gb şlemlere tab tutulur ve yapay olarak
ver üretlr .

## 2.4. Very Anlama

Ver elde edldkten sonra vernn anlaşılması ve analzlere hazır hale getrlmes gerekr . Bu aşamada hem
yapılandırılmış hem de yapılandırılmamış ver çn Bölüm 1.2’de de değnlen “çöp-grd, çöp-çıktı”
prensbnn anlaşılması oldukça önemldr . Bu prensp, gelştrlen makne öğrenmes modelnn ve
nhayetnde üretlecek çıktının kaltesnn kullanılan grdye yan ver kaltesne doğrudan bağlı olduğunu
fade etmektedr . Bu çerçevede gerçekleştrlecek makne öğrenmes analzlernn boşa gtmemes çn ver
kaltesne (vernn doğru, eksksz ve güvenlr) olmasına dkkat edlmeldr . Bu nedenle makne öğrenmes
sürecnde doğrudan algortmaların verye uygulanması yerne öncelkle vernn anlaşılması ve htyaç
duyulursa vernn analzlere hazır hale getrlmes gerekr . Böylelkle modelleme öncesnde lteratürde ver
ön-şleme ( data pr e-processng)  olarak adlandırılan adım tamamlanmış olur (Şekl 8).


Şekl 8: Ver ön-şleme sürec.

### 2.4.1. Ver Türler

Analzler çn kullanılacak ver setndek ntelkler farklı türlerde olablr . İstatstkte olduğu gb makne
öğrenmes sürecnde de ver setndek ntelklern ver tpnn doğru tanımlanması oldukça önemldr , çünkü
bunlara bağlı olarak makne öğrenmes algortması seçlecektr . Ver türler genel anlamda sayısal/nümerk
(numerc ) ve kategork  (categorcal ) olarak kye ayrılablr (Şekl 9).
Sayısal ver kend çnde ayrık  (dscr ete) ve sürekl (contnuous ) olarak k gruba ayrılablr . Ayrık sayısal
ver, sadece belrl ve brbrnden ayrık olan değerler temsl eder . Bu değerler sıklıkla sayılablr ve belrl br
aralıkta sonsuz olasılıklara sahp değldr . Ayrık verler genellkle sayılablr öğeler , kategor veya olaylarla
lşklendrlr . Br aledek çocukların sayısı (1, 2, 3, vb.), br hanedek evcl hayvan sayısı (0, 1, 2, vb.), br
şrketn belrl br dönemde aldığı şkayetlern sayısı (10, 100, vb.) ayrık sayısal verye örnek olarak
verleblr .
Sürekl sayısal ver  se, belrl br aralıkta her değer alablen ve yüksek hassasyetle ölçüleblen değerlerdr .
Bu tür verde k nokta arasında sonsuz sayıda olası değer mevcuttur . Sürekl ver genellkle gerçek sayılar
(real numbers ) olarak fade edleblen ölçümler ve ncelklerle lşklendrlr . Sıcaklık okumaları (25.5°C,
86.2°F , vb.), boy ölçüsü (150.2cm, 160.5cm, vb.), gelr değerler (20000TL, 30000TL, vb.) sürekl sayısal
verye örnek olarak verleblr .
Kategork ver de kend çnde kl (bnary ) kategork, sıralı  (ordered) kategork ve nomnal  kategork
şeklnde üç gruba ayrılablr . İkl kategork ver , sadece k farklı kategor ya da sınıfın bulunduğu very
fade eder . Örneğn “evet/hayır”, “doğru/yanlış”, “var/yok” gb. Sıralı kategork ver , kategorler arasında


gerçekleştrlemez. Örneğn eğtm sevyes (lkokul, lse, ünverste), müşter memnunyet (düşük, orta,
yüksek). Nomnal kategork ver , kategorler arasında herhang br sıra veya derecelendrme çermeyen
verdr . Sıralı kategork verde olduğu gb matematksel şlemler gerçekleştrlemez. Örneğn renkler
(kırmızı, mav, yeşl), şehr smler (İstanbul, Sakarya, Kastamonu), meyve türler (elma, çlek, mandalna).


Şekl 9: Ver türler.

### 2.4.2. Very Anlama İşlemler

Ver set temn edldkten sonra, ver hakkında ön blg ednmek çn bazı temel
açıklayıcı (exploratory ) statstksel hesaplamalar  yapmak vernn anlaşılmasında yardımcı olacaktır . Ver
setndek ntelklern ver türüne uygun şeklde maksmum, mnmum, mod, medyan, ortalama ya da kartl
hesaplamaları yapılablr . Elde edlen açıklayıcı statstksel bulgular ver görselleştrme le destekleneblr .
Ver görselleştrme  (data vsualzaton ), makne öğrenmesnde hem very anlama hem de sonuçların
raporlanmasında kullanılablmektedr . Ver setndek ntelkler kutu grafğ ( box and whsker  plot), hstogram,
sütun ve pasta grafkler, serplme/saçılım dyagramlarıyla ( scatter plot ) görselleştrleblr .
Özellkle sınıflandırma algortmaları le çalışılırken hedef ntelğn kategorler arasındak dengenn kontrol
edlmes de önemldr . Çünkü gerçek hayattak ver setlernde örneğn br hastalığın varlığı ve yokluğu
durumuna lşkn yarı yarıya br örneklem elde edeblmek zor olablr . Sınıf dengeszlğ ya da dengesz ver
set (mbalanced dataset ) durumu yanıltıcı performans değerlernn elde edlmesne neden olacaktır (Kartal
vd., 2019; Kartal & Özen, 2017).
Son yıllarda yapay zekânın etk boyutu da araştırmacıların lgsn çeken br konu olmuştur . Ver setndek
yanlılık  (bas) performans sonuçlarına da etk edeceğnden vernn anlaşılması aşamasında vernn yanlılığı
kontrol edlmeldr . Analze dahl edlen gruplardan her brnn ver setnde yeternce temsl edldğnden
emn olunmalıdır . Bunların dışında ver setndek olası;
• hatalı ver grş,
• aykırı/uç değerler ( outlers ),
• eksk değerler ( mssng values ),
• tekrar eden örnek/gözlem değerler ( duplcates ),
• ntelklern brbrler arasındak lşkler ( correlaton ) ve
• analze alınması planlanan ntelkler
kontrol edleblr (Kartal, 2015; Ronaghan, 2019).

## 2.5. Ver Hazırlama

Ver hazırlama aşamasında Very Anlama Bölümü’nde tespt edlen durumlara uygun bçmde ver set


• ver özetleme,
• ver görselleştrme,
• boyut azaltma,
• ver temzleme (hatalı yazılan kayıtların düzeltlmes, aykırı değer tespt, eksk değerlern tamamlanması,
ver setndek tekrar eden kayıtların gderlmes, vb.),
• ver normalzasyonu,
• yapay ( dummy ) kodlama,
• ver ayrıklaştırma.

### 2.5.1. Ver Özetleme ve Ver Görselleştrme

Ver özetleme  (data summarzaton ), ver setnn daha kısa ve anlamlı br bçmde sunulmasıdır . Bunun çn
brtakım temel açıklayıcı statstksel değerler ve ver görselleştrme kullanılablr . Ver setn özetlemek çn
örnekleme yöntemler kullanılarak orjnal ver setnden temsl br alt küme seçleblr . Ver özetleme ve
görselleştrme konularına br öncek bölümde (Bölüm 2.4) değnlmştr .

### 2.5.2. Boyut Azaltma

Ver setnde fazla sayıda ntelk olması, kompleks br makne öğrenmes modelnn ortaya çıkmasına ya da
analzlern uzun sürmesne sebep olablr . Bellman (1957) tarafından lteratüre kazandırılan “çok
boyutluluğun lanet” ( the curse of dmensonalty ) kavramı hesaplamada meydana gelecek üstel artış, alan
srafı ve yetersz/zayıf görselleştrme gb olumsuz etkler fade etmektedr (V enkat, 2018). Bu sebeple ver
setnde çok boyutluluğun azaltılablmes çn çeştl boyut azaltma  (dmenson r educton ) yöntemlernden
faydalanılablr .

### 2.5.3. Ver Temzleme

Ver temzleme  (data cleanng/cleansng ) aşamasında ver setnde bulunan her türlü hata, yanlışlık vb.
değerlern belrlenmes ve düzeltlmes şlemler yapılır . Ver temzleme, mevcut verlere müdahale etmeden
ver setnn doğruluğunu en üst düzeye çıkarmanın br yolunu bulmakla lgldr (Dey , 2021). Ver temzleme
şlemler kapsamında hatalı kayıtların düzeltlmes başta olmak üzere aykırı değer tespt, eksk değerlern
tamamlanması, ver setndek tekrar eden kayıtların gderlmes gb şlemler gerçekleştrlr .

### 2.5.4. Aykırı Değer Tespt

Aykırı değer  (outler ) genellkle ana kütley oluşturan gözlemlerden öneml ölçüde uzak olan gözlem olarak
kabul edlr (Benatt, 2018). Br ver setndek değşkenler genellkle brbrleryle kısmen lşkl olduğundan
br aykırı değer , n adet ntelkten oluşan br ver setnde ( n boyutlu br uzayda) dğerlernden daha uzakta
bulunan ver olarak değerlendrlr . Aykırı değerler bazı modellern performansını olumsuz yönde
etkleyebleceğnden ver hazırlama aşamasında ncelenmeldr . Bu sebeple verde aykırı değerlern tespt
edlmes amacıyla uzaklık-tabanlı algortmalar , kutu grafğ le vernn görselleştrlmes gb statstksel
brtakım yöntemler , yoğunluk-tabanlı algortmalar ve kümeleme teknkler kullanılablr (Falah vd., 2023).

### 2.5.5. Eksk Değerlern Tamamlanması

Gerçek hayat ver setler km zaman eksk ver çereblr . Böyle br durumda model performansının olumsuz
etklenmemes çn eksk değerlern tamamlanması  (mssng data mputaton ) gerekr . Belrl br ntelğe at
eksk değerler;
(1) eğer ntelk nümerk se ntelğn ortalaması ( mean ) ya da (eğer aykırı değerler fazla se) ortanca değer


(2) eğer ntelk kategork se ntelğn frekans değer en yüksek olan kategor le
tamamlanablmektedr .

### 2.5.6. Ver Normalzasyonu

Ver normalzasyonu  (data normalzaton ), nümerk verlern standart br aralığa dönüştürülmes olarak
tanımlanablr . Ver normalzasyonu, ntelkler hang aralıkta olursa olsun modele eşt katkıda bulunmasını
sağlamak çn yapılır . Aşağıda mn-maks normalzasyon  teknğnn formülü verlmştr (Balaban & Kartal,
2018).


Br dğer ver normalzasyon teknğ olan z-scor e standartlaştırma  formulü aşağıda verlmştr .

  Örneğn Tablo 6’dak gb yaş ntelğnde 10 adet değer
olsun. Bu değerler mn-maks  teknğ kullanılarak  

 aralığına normalze edlmştr . İlk örneğn hesaplaması formül üzernde aşağıda verlmştr .

  Tablo 6: Yaş ntelğnn mn-maks
yöntem le normalzasyonu.
yaşnormalze edlen yaş
200.032
550.597
400.355
280.161
550.597
300.194
250.113
801
180
330.242

Verlen bu ver normalzasyon teknkler dışında ntelk değern ortalamaya bölme, standart sapmaya bölme,
maksmuma bölme, aralığa bölme ( 

) gb yöntemler de kullanılablr (W alesak & Dudek, 2020).

### 2.5.7. Yapay (Dummy) Kodlama

Yapay kodlama  (dummy codng ), kategork ntelkler nümerk hale getrme şlemdr . Bu k yolla
yapılablr:
1.   Eğer kategorler arasında sıralı br bağlantı varsa sıra gözetlerek kategorlern artan sayısal değerlere


2.   Yapay kodlamanın sıralı olmayan veya sıralı ancak aralarında artmetk lşk bulunmayan kategork
değşkenler çn daha uygun olduğu fade edlmektedr . Ntelklere at kategorler kl (0, 1) değerlere
dönüştürülmektedr . Örneğn sgara tüketm ntelğ çn Var/Yok kategorler 0/1 olarak kodlanablr . 0 ve 1
değerler lgl kaydın o kategorye at olma olasılığını gösterecektr (T ablo 7).
Tablo 7: Sgara tüketm ntelğ çn yapay kodlama


Ntelkte kden fazla ( n sayıda ) kategornn olması durumunda, eğer örnek bu kategorlerden sadece ve
sadece brne at se n-1 sütun kullanılablr (T ablo 8). Örneğn aşağıdak tabloda meslek ntelğnde
akademsyen ve veterner olma olasılığının sıfır olduğu yerlerde lgl kaydın doktor kategorsne at olma
olasılığı 1 olacaktır .
Tablo 8: Meslek ntelğ çn yapay kodlama.


### 2.5.8. Ver Ayrıklaştırma

Ver ayrıklaştırma  (data dscr etzaton ), sürekl sayısal ntelklern ayrı kategorlere ayrılması şlemdr . Br
dğer fadeyle ver ayrıklaştırma nümerk ntelklern kategork hale getrlmes şlemdr . Çeştl ver
ayrıklaştırma yöntemler bulunmaktadır . Örneğn ver aralığı sabt sayıda eşt boyutlu bölmelere ya da her
bölme yaklaşık olarak aynı sayıda gözlem olacak bçmde kategorlere ayrılablr . Bunun dışında belrl alt ve


## 2.6. Modelleme

Flach (2012) br görevn ntelklerle tanımlanan very çıktılara uygun htyaç duyduğu hartalamayı model
olarak tanımlamış, öğrenme problemlernn modeller üreten öğrenme algortmaları tarafından çözüldüğünü,
görevlern se modeller tarafından yönlendrlmekte olduğunu belrtmştr (Flach, 2012; Kartal, 2015).
Makne öğrenmes model, verden öğreneblen br sstemn matematksel br temsl olarak düşünüleblr
(Şekl 10) (Kartal, 2015). Model, kendne sunulan eğtm vers le eğtldkten sonra gelecek yen verler çn
tahmnlerde/öngörülerde bulunmak veya kararlar almak çn kullanılablr .


Şekl 10: Makne öğrenmes model (Kartal, 2015).
Tüm modellern kümes  
   olsun. Amaç, makne öğrenmes problem çn
alternatf modeller arasından en ysn seçmektr . Aynı öğrenme model, farklı parametre ayarları veya
hperparametre ( hyperparameter ) kombnasyonları le deneneblr . Örneğn k-En Yakın Komşu Algortması
farklı k değerleryle, Yapay Snr Ağları farklı katman ya da nöron sayılarıyla ya da Destek Vektör Makneler
farklı çekrdek ( kernel ) fonksyonları le çalıştırılablr . Veya farklı makne öğrenmes modeller  

 kümesnn br parçası olarak kullanılablr . Örneğn br problemn çözümü çn Nave Bayes Sınıflandırıcı,
Yapay Snr Ağları, k-En Yakın Komşu Algortması, Destek Vektör Makneler, Karar Ağaçları gb farklı
sınıflandırma veya regresyon algortmaları kullanılablr .
Tpk br makne öğrenmes model aşağıda sayılan bleşenlerden oluşmaktadır:
• Ver: Modeln öğrenme çn kullanacağı ver set.
• Eğtm vers:  Ver setnn br alt kümesdr , model eğtmek çn kullanılır .
• Test vers:  Ver setnn ayrı br alt kümesdr , modeln performansını değerlendrmek çn kullanılır .
• Ntelkler : Modeln tahmnde/öngörüde bulunmak ya da kararlar almak çn kullandığı ver alanlarıdır .
• Algortma : Modeln verden öğrenmek çn kullandığı br dz matematksel kural ve talmatlardır .
• Algortma Parametr eler:  Modeln performansını artırmak çn eğtm sırasında öğrendğ ve ayarladığı
hperparametrelerdr ( hyperparameters ).
Farklı makne öğrenmes stratejlerne özgü farklı algortmalar kullanılmaktadır:
• k-en yakın komşu algortması, Nave Bayes Algortması, logstk regresyon, karar ağaçları (ID3, C4.5, C5.0
gb), yapay snr ağları, destek vektör makneler gb algortmalar danışmanlı öğrenme algortmalarına örnek


• k-ortalamalar , bulanık c-ortalamalar , CURE, BIRCH, DBSCAN, k-medods, apror vb. algortmalar
danışmansız öğrenme algortmaları arasındadır .
• Son olarak q-learnng, dern q-learnng algortmaları pekştrmel öğrenme algortmalarına örnek olarak
verleblr .

## 2.7. Model Değerlendrme Sür ec

Kurulan makne öğrenmes modelnn verlen görev öğrenp öğrenmedğn anlayablmek çn modeln
performansı ölçülmeldr . Bunun çn çeştl performans değerlendrme yöntemler ve performans
değerlendrme ölçütler gelştrlmştr . Sınıflandırma, regresyon ve kümeleme görevlerne göre kullanılan
yöntem ve ölçütler farklılık göstereblmektedr .

### 2.7.1. Model Performans Değerlendrme Yöntemler

Model performans değerlendrme yöntemler, ver setnn eğtm ve test olarak ayrılması şlemlern çerr . Bu
aşamada dkkat edlmes gereken bazı unsurlar şöyle sıralanablr (Kartal & Özen, 2017):
• Eğtm ver setndek örneklern sayıca test ver setndek örneklerden fazla olması beklenr . Olabldğnce
örnek görmesnn modeln genelleştrme yeteneğne olumlu yönde katkıda bulunacağı düşünülmektedr .
• Eğtm ve test ver set ayrımında rastgele örnekleme yapılması önemldr . Örneklere yapılacak manuel br
müdahale yanlı sonuçların elde edlmesne yol açablr .
• Ver setnn eğtm ve test ver set olarak bölünmes sırasında hedef ntelğe at sınıfın eğtm ve test ver
setlerndek dağılımına özen gösterlmeldr . Br sınıfa at örneklern eğtm ya da test ver setnde hç
bulunmaması sorun olacaktır . Dolayısıyla hem eğtm hem de test ver setnde ana ver setndek her br sınıfa
at örnekler bulunmalıdır .
Danışmanlı öğrenme modellernn performans değerlendrmes çn blnmes gereken bazı temel yöntemler
aşağıda sıralanmıştır .
İkl Ayırma (Hold-out) : İkl ayırma yöntem lteratürde en sık kullanılan yöntemlerden brdr ve ver setn,
eğtm ve test ver set olmak üzere k bölüme ayırmaya dayanan br yaklaşımdır (Şekl 1 1). Genellkle belrl
br yüzde oranına göre (örneğn %70 eğtm ve %30 test veya %80 eğtm ve %20 test veya %90 eğtm ve
%10 test vb.) ver set k bölüme ayrılır . Örneklern büyük br kısmı eğtm çn kullanılırken ger kalan
örnekler test çn kullanılır . Bu nedenle bu yönteme kl ayırma  adı verleblr .


Şekl 11: İkl ayırma yöntem.
Tabakalı İkl Ayırma (Stratfed Hold-out ): Tabakalı kl ayırma yöntemnn kl ayırma yöntemnden
farkı, ver setnn sınıflarına göre dengel br şeklde bölünmesn sağlamasıdır (Şekl 12). Bu ayırma yöntem


Covd-19 hastası olan br ver set %70 eğtm ve %30 test olacak şeklde tabakalı örnekleme le ayrılmak
stensn. Bu durumda 60 grp hastasının %70’ eğtme ve %30’u teste, 40 Covd-19 hastasının %70’ eğtme
ve %30’u test ver setne gtmeldr . Son durumda eğtm ver setnde 42 grp ve 28 Covd-19 hastası; test ver
setnde se 18 grp ve 12 Covd-19 hastası olmalıdır .
Tekrarlı kl ayırma:  Tekrarlı kl ayırma, kl ayırma şlemnn brden çok kere tekrarlandığı br
yöntemdr . Böylelkle ver setnn farklı rastgele bölünmeler elde edlerek brden çok modeln eğtlmes ve
test edlmes sağlanır . Bu sayede elde edlen sonuçlar statstksel olarak daha güvenlr hale geleblecektr .
Örneğn 4 kere kl ayırma yapıldığında her br çn ayrı ayrı performans değerlendrme ölçütler hesaplanır .
Tek br performans değerlendrme ölçütü çn elde edlen P1, P2, P3 ve P4 gb 4 farklı değern ortalaması le
nha performans değerne ulaşılmaktadır .


Şekl 12: Tekrarlı kl ayırma yöntem.
Üçlü-A yırma  (Three-way Splt ): Üçlü-ayırma ver setnn üç bölüme ayrıldığı br yöntemdr . Bu üç bölüm
genellkle eğtm, doğrulama ( valdaton ) ve test verlern temsl eder (Şekl 13). Eğtm vers modeln
öğrenmes çn kullanılırken doğrulama vers modeln ayarlarının kontrol edlmes çn kullanılır . Test vers


Şekl 13: Üçlü ayırma yöntem.
Çapraz Geçerleme (Cross-V aldaton ): Çapraz geçerleme, ver setn farklı alt kümeler/katlar ( folds ) halnde
yne rastgele bçmde böler ve modeln brden çok kez eğtlp test edlmesn sağlar . En sık kullanılan çapraz
geçerleme yöntemler arasında k-kat çapraz geçerleme  ve brn dışarıda bırakan  çapraz geçerleme
(Leave-One-Out Cr oss-V aldaton- LOOCV ) bulunur .
k-kat çapraz geçerlemede her br kat br kez test, dğer  

 kat eğtm ver set olacak şeklde analzler tekrar edlr . Örneğn 5-kat çapraz geçerleme yapıldığında P1, P2,
P3, P4 ve P5 olmak üzere beş farklı performans değerlendrme ölçütü (örneğn; 5 farklı doğruluk değer) elde
edlr (Şekl 14). Nha performans se bu değerlern ortalaması olacaktır . LOOCV’de se her br örnek en az
br kere test ver set, kalan n-1 örnek se eğtm ver set olacak şeklde analzler n defa tekrar edlr . Analz
sonunda modeln nha performansı bu n adet performans değernn ortalaması olacaktır . Çapraz geçerleme


Şekl 14: 5-kat çapraz geçerleme yöntem.

### 2.7.2. İkl Sınıflandırma Performansının Değerlendrlmes

İkl-sınıf sınıflandırma performansı çn Tablo 9’da verlen kontenjans tablosu/karmaşıklık matrs
(contgnency table/confuson matrx ) kullanılır . Bu tablo test ver setndek hedef ntelk (gerçek değerler) le
model öngörülernn karşılaştırılması sonucunda oluşturulur . Kontenjans tablosunda dört temel eleman
bulunmaktadır: TP, TN, FP  ve FN aşağıdak gb tanımlanmıştır .
• TP: Doğru sınıflandırılan COVID-19 hastalarının sayısı, doğru poztfler .
• TN: Doğru sınıflandırılan GRİP  hastalarının sayısı, doğru negatfler .
• FP: Yanlışlıkla COVID-19 olarak sınıflandırılan GRİP  hastalarının sayısı, yanlış poztfler .
• FN: Yanlışlıkla GRİP  olarak sınıflandırılan COVID-19 hastalarının sayısı, yanlış negatfler .
Tablo 9: Kontenjans tablosu.


Tabloda yer alan tahmn ve gerçek değerlernn yer lteratürde bu ktapta olduğu gb satır -sütun ya da sütun-
satır düzennde verleblmektedr (yerler değşeblr). Bu nedenle TP, FP, FN ve TN değerlernn yernn
ezberlenmemes , bunun yerne satır ve sütunlarda hang değerlern olduğu (tahmn ya da gerçek) göz önüne
alınarak TP, FP, FN ve TN değerlernn tabloya yerleştrlmes tavsye edlmektedr . Karmaşıklık matrsnn
oluşturulmasına lşkn Tablo 10’da verlen örnek nceleneblr:
Tablo 10: Test ver setndek hedef ntelğn model tahmnler le karşılaştırılması.

Tablo 1 1: Kontenjans tablosu.
GERÇEK
Covd-19 Grp Toplam  
TAHMİNCovd-19 4 2 6  
Grp 1 3 4  
Toplam 5 5 10  

Tablo 1 1’dek kontenjans tablosu elde edldkten sonra bu tabloya lşkn performans değerlendrme ölçütler
hesaplanablecektr (Balaban & Kartal, 2018; Kartal, 2015):
Doğruluk  (accuracy ), doğru tahmn edlen örneklern toplam örnek sayısına oranını fade eder .


Hata oranı  (error rate ), yanlış tahmn edlen örneklern toplam örnek sayısına oranını fade eder .


Duyarlılık  (senstvty , recall, T rue Postve Rate-TPR ), gerçek poztf (TP) tahmnlern toplam poztf örnek
sayısına oranını fade eder . Duyarlılık, poztf sınıfın doğru tahmn edlme başarısını ölçer .


Belrleyclk  (specfcty , True Negatve Rate- TNR ), gerçek negatf (TN) tahmnlern toplam negatf örnek
sayısına oranını fade eder . Belrleyclk, negatf sınıfın doğru tahmn edlme başarısını ölçer .


Yanlış Negatf Oranı  (Mss rate,  False Negatve Rate- FNR ), gerçek poztf (TP) tahmnlern toplam poztf
örnek sayısına (pos) oranını fade eder . FNR, poztf sınıfın yanlış tahmn edlme oranını ölçer .


Yanlış Poztf Oranı  (Fall-out, False Postve Rate- FPR ), gerçek negatf (TN) tahmnlern toplam negatf
örnek sayısına (neg) oranını fade eder . FPR, negatf sınıfın yanlış tahmn edlme oranını ölçer .


Kesnlk  (Postve Pr edctve V alue- PPV , precson ), gerçek poztf (TP) tahmnlern toplam poztf tahmnler
(tpos) sayısına oranını fade eder . Kesnlk, poztf olarak tahmn edlen örneklern ne kadarının gerçekten
poztf olduğunu ölçer .


Negatf Öngörü Değer ( Negatve Predctve V alue- NPV ), gerçek negatf (TN) tahmnlern toplam negatf
tahmnler (tneg) sayısına oranını fade eder . NPV , negatf olarak tahmn edlen örneklern ne kadarının
gerçekten negatf olduğunu ölçer .


F-Ölçüsü  (F1-Scor e, F-Measur e), kesnlk ve duyarlılık metrklernn harmonk ortalamasıdır . Kapsayıcı ve
bu k metrğn dengeleyc br ölçüsünü sunar . F-Ölçüsü, özellkle dengesz sınıflandırma problemlernde
kullanılır ve hem yanlış poztfler hem de yanlış negatfler dkkate alır .


### 2.7.3. Çoklu-Sınıf Sınıflandırma Performansının Değerlendrlmes

Çoklu-sınıf sınıflandırmada, hedef ntelğn kategorler/sınıf etketler kden fazladır . Bu nedenle kl
sınıflandırmada olduğu gb yalnızca poztf ve negatf şeklnde ntelendrlen k sınıf bulunmamaktadır .
Çoklu-sınıf sınıflandırma çn oluşturulan örnek br kontenjans tablosu Tablo 12’de verlmştr .
Tablo 12: Çoklu-sınıf sınıflandırma çn kontenjans tablosu.
RİSKGERÇEK
Yüksek Orta Düşük
TAHMİNYüksek 40 2 9
Orta 7 20 4


Bu tabloya göre doğruluk ve hata değerler kl sınıflandırmada olduğu gb hesaplanır .


Sınıfa bağlı dğer performans değerlendrme ölçütler hesaplanırken “brne karşı dğerler” ( one vs. all )
yaklaşımı kullanılmaktadır . Yan her br sınıf çn ayrı ayrı TP, FP, FN ve TN değerler hesaplanır . Örneğn
Tablo 13’ te Yüksek sınıfı çn TP = 40, FP  = 11, FN = 10 ve TN = 39’dur .
Tablo 13: Çoklu-sınıf sınıflandırma çn kontenjans tablosu.


Tablo 14’ te yüksek sınıfına at hesaplamalar çn kontenjans tablosunun nasıl “brne karşı dğerler”
yaklaşımı kullanılarak kl sınıflandırmaya benzer br şekle dönüştürüldüğü görüleblr . Yüksek çn yapılan
bu benzetm dğer sınıf etketler çn de yapılarak gerekl hesaplamalar elde edlmektedr .
Tablo 14: Çoklu-sınıf sınıflandırma çn kontenjans tablosu.


Böylelkle sınıfa dayalı performans değerlendrme ölçütler her br sınıf etket çn şu şeklde
hesaplanacaktır:


Modeln son performansının bulunması çn makr o ortalama  (macr o averagng ) ve mkr o ortalama  (mcro
averagng ) yöntemler kullanılablr . Makr o ortalama da her sınıfın performansını ayrı ayrı hesaplanmakta
ve daha sonra bu sınıfların performanslarının ortalaması alınmaktadır . Mkr o ortalama  se tüm sınıfların
toplam doğru ve yanlış tahmnlern toplamakta ve bu toplamlar üzernden performans hesaplamaktadır . Her
br örneğn veya tahmnn eşt şeklde ağırlıklandırılması gerektğnde mkro ortalamanın kullanılması;
sınıflandırıcının en sık kullanılan sınıf etketlerne lşkn genel performansını değerlendrmek çn tüm
sınıfların eşt şeklde ele alınması gerektğnde se makro ortalamanın kullanılması tavsye edlmektedr .


Sınıf sayısının k olması durumunda da performans ölçütler çn makro ve mkro ortalama hesaplamaları
yapılablmektedr .

### 2.7.4. Regresyon Performansının Değerlendrlmes

Danışmanlı öğrenmede hedef ntelğn ver türü sayısal olması sebebyle regresyon görevlernde veya
sınıflandırmada olduğu gb br kontenjans tablosu oluşturulamaz; ancak yne de model tahmnler le gerçek
değerler brbryle karşılaştırılablr . Sonrasında da regresyon model performansının değerlendrleblmes
çn farklı performans değerlendrme ölçütler hesaplanablmektedr . Bu bölümde aşağıda sıralanan beş farklı
performans değerlendrme ölçütü hakkında blg verlmştr (Shmuel vd., 2018). Ver setnde yer alan br  

örneğ çn öncelkle hata 
   bulunur . Hata, gerçek değer ( 
  ) le tahmn değer ( 

) arasındak farktır .

  Ver setndek örnek sayısı 

 olmak üzere;


Ortalama Mutlak Hata  (Mean Absolute Err or- MAP ): Ortalama mutlak hatanın büyüklüğünü verr .


Ortalama Yüzde Hata  (Mean Per centage Err or- MPE ): Hatanın yönünü dkkate alarak tahmnlern gerçek
değerlerden (ortalama olarak) ne kadar saptığına lşkn yüzdelk br puan verr .


Ortalama Mutlak Yüzde Hata  (Mean Absolute Per centage Err or- MAPE ): Tahmnlern gerçek değerlerden
ne kadar (ortalama olarak) saptığına lşkn yüzdelk br puan verr .


Ortalama Kar esel Hatanın Kar ekökü  (Root-Mean-Squared-Error - RMSE): Doğrusal regresyondak
standart tahmn hatasına benzer; tek farkı, eğtm vers yerne test vers üzernden hesaplanmasıdır .
Ortalama Karesel Hata (Mean Squared Error - MSE),


olmak üzere, Ortalama Karesel Hatanın Karekökü aşağıdak gbdr .


Örneğn Tablo 15’ te verlen test ver setndek hedef ntelk sütunu (gerçek) le model tahmnler kullanılarak
yukarıda bahsedlen performans değerlendrme ölçütler hesaplanmıştır .


### 2.7.5. En Uygun Küme Sayısının Belrlenmes

Kümeleme görevlernde ver setnn kaç kümeye ayrılacağının tespt edlmesne yan en uygun küme
sayısının ( 

) belrlenmesne yardımcı olacak bazı yöntemler aşağıda verlmştr .
Uzmanlık Öngörüsü:  Bazı durumlarda kümeleme problemne lşkn uzmanlık blgs kullanılablr . Örneğn
farklı ççek türlernden oluşan br ver set kümelenrken üç farklı türün olduğu blnyorsa  


seçleblr . Ya da şrket müşterlernn genel olarak dört farklı grupta olduğu blnyorsa 

 seçleblr .
Drsek Yöntem: Drsek yöntem ( elbow method ), küme sayısının br fonksyonu olarak küme ç varyansın
veya uzaklıkların karelernn toplamının ( Sum of Squar ed Err ors- SSE/W thn Cluster Sum of Squar es-
WCSS ) çzlmesn gerektrr . SSE değerler ( y-eksen) farklı  
   küme sayıları ( x-eksen) çn br çzg grafğ
le gösterleblr .  
  küme sayısı arttıkça SSE azalma eğlmndedr . Bunun neden olarak daha fazla küme
ver setne daha y uyum sağlayablr; ancak bell br noktadan sonra azalma hızı yavaşlar ve olay ör güsünde
drsek benzer br bükülme meydana gelr . İşte bu bükülmeye karşılık gelen 

 değer y br seçm olarak kabul edlr (Şekl 15).
SSE, ver setndek her br örnek çn kendne en yakın küme merkezne olan mesafe şeklnde
tanımlanablr .  
  küme sayısı, 
   se 
   kümesnn merkez, 

  kümesne at br örnek ve 
  ’n 

 kümesne uzaklığı olmak üzere SSE aşağıdak gb hesaplanır (Ççekl, 2023).


Şekl 15: Drsek yöntem.
Slhouette Katsayısı:  Slhouette ndeks değer/katsayısı/puanı, kümeleme teknğnn ylğn/kümeleme


• Slhouette katsayısı = 1 se, kümelern brbrnden oldukça ayrı olduğu ve açıkça ayırt edldğ anlamına
gelr (y ayrılmış kümeler).
• Slhouette katsayısı = 0 se, kümelern kayıtsız olduğu anlamına gelr veya kümeler arasında mesafe farkı
olmadığı (örtüşen kümeler olduğu) söyleneblr .
• Slhouette katsayısı = -1 se, kümelern hatalı şeklde atandığı anlamına gelr (yanlış küme ataması).
Ver setndek tüm örnekler çn Slhouette katsayıları hesaplanır . Bunlar kullanılarak kümeleme yapıldıktan
sonra, örneğn 3 küme elde edldkten sonra, her br kümeye at ortalama Slhouette katsayısı bulunablr .
İstenrse farklı  

 küme sayıları çn ortalama Slhouette katsayısı hesaplanablr ve en yüksek ortalama Slhouette katsayısına
sahp olan küme sayısı, en uygun küme sayısı olarak seçleblr .
•  
  , ortalama küme ç mesafe, yan 
   le aynı 

 kümesndek dğer tüm ver noktaları arasındak ortalama mesafe,
•  
  , 

 le herhang br başka kümedek tüm ver noktaları arasındak en küçük ortalama mesafe
olmak üzere br  
   kümesne at 

 gözlem değernn Slhouette katsayısı aşağıdak gb hesaplanablr (Rousseeuw , 1987) (Şekl 16):


Tüm ver noktaları çn genel Slhouette katsayısı, ver noktaları çn ayrı ayrı hesaplanan Slhouette
katsayılarının ortalaması alınarak bulunur . Daha yüksek ortalamaya sahp Slhouette katsayısı daha y


Şekl 16: Slhouette katsayısının hesaplanması.
Not:  Şekl 16 çzmnde GeoGebra (2023) kullanılmış ve Bhardwaj (2020) tarafından verlen şeklden
faydalanılmıştır .

## 2.8. Modeln Uygulamaya Geçrlmes

Modeln uygulamaya geçrlmes, alternatf makne öğrenmes modeller arasından en y performansa sahp
olan(lar)ın seçlp kullanıma sunulduğu aşamadır . Bu süreçte model(ler) br web arayüzü, mobl chaz, robot
ya da br elektronk chaza entegre edleblr .
Makne öğrenmes çalışmaları çn çeştl programlama dller (Python, R, Jula, Java, C++ vb.), ücretl
(MATLAB, SAS, RapdMner , IBM SPSS, vb.) ve ücretsz yazılım ve gelştrme araçları (W eka, KNIME,
Orange, RStudo, Spyder , Jupyter Notebook vb.), bulut blşm platformları (Amazon Web Servces- AWS,
Mcrosoft Azure, Google Cloud Platform- GCP , IBM Cloud, vb.) kullanılmaktadır (Şekl 17).


Bu ders kapsamındak tüm makne öğrenmes analzlernde Python programlama dl (versyon 3.1 1.6) ve
Spyder (versyon 5.5.0) ( Scentfc PYthon Development EnvRonment ) Bütünleşk Gelştrme Ortamı
(Integrated Development Envr onment- IDE ) kullanılmıştır .
Spyder edtörü, bağımsız yükleyc yardımı le https://www .spyder -de.or g/ adresnden ndrleblr . Spyder
kend Python sürümü le yüklenmektedr; ancak daha güncel Python sürümler le çalışmak çn
https://www .python.or g/ adresnden şletm sstemne uygun Python sürümü seçlerek blgsayara ndrleblr
ve sonrasında Spyder ’da lgl Python yorumlayıcısı seçleblr .


**Bölüm Özet**

Bu bölümde makne öğrenmes sürec, sstematk br yaklaşım olarak Ver Madenclğ çn Çapraz
Endüstr Standard Sür eç Model  (CRoss-Industry Standar d Process for Data Mnng- CRISP-DM ) adımları
le ele alınmıştır . Makne öğrenmes sürecnn lk adımı, problemn amacını ve kapsamını anlamaktır . Bu
başlık altında problemn doğru br şeklde tanımlanması ve belrlenmesne odaklanılmıştır . Doğru ve
güvenlr vernn elde edlmes başarılı br modeln temeln oluşturacağından ver toplama sürec de ayrı br
başlık olarak ncelenmştr . Ardından ver anlama ve ver hazırlama adımları açıklanmıştır . Bu kapsamda; ver
özetleme, görselleştrme, boyut azaltma, temzleme, aykırı değer tespt, eksk ver yönetm ve
normalzasyon gb konular hakkında blg verlmştr . Modelleme başlığında makne öğrenmesndek model
kavramına yer verlerek, farklı öğrenme stratejler çn kullanılan farklı algortmalara örnekler verlmştr .
Model performansının değerlendrlmes ve en uygun modeln seçlmes başlığı altında kl sınıflandırma,
çoklu sınıf sınıflandırma, regresyon ve kümeleme çn farklı performans değerlendrme yöntemler ve
ölçütler detaylı bçmde ele alınmıştır . Son olarak br makne öğrenmes modelnn gerçek dünya
uygulamalarına entegre edlmes ve kullanıma geçrlmesne lşkn tavsyeler sunulmuştur .


**Kaynakça**

Balaban, M. E., & Kartal, E. (2018). Ver Madenclğ ve Makne Öğr enmes T emel Algortmaları ve R Dl le
Uygulamaları  (2. bs). Çağlayan Ktabev.
Bellman, R. (1957). Dynamc programmng, prnceton unv . Press Prnceton, New Jersey .
Benatt, N. (2018). A machne learnng appr oach to outler detecton and mputaton of mssng data . Nnth
IFC Conference on “Are post-crss statstcal ntatves completed?”, Basel.
https://www .bs.or g/fc/publ/fcb49_48.pdf
Bhardwaj, A. (2020, Mayıs 27). Slhouette Coeffcent: V aldatng clusterng technques . Medum.
https://towardsdatascence.com/slhouette-coef fcent-valdatng-clusterng-technques-e976bb81d10c
Ççekl, İ. (2023). Clusterng . https://web.cs.hacettepe.edu.tr/~lyas/Courses/VBM684/lec10_Clusterng.pdf
Dey, V. (2021, Eylül 12). Understandng the Importance of Data Cleanng and Normalzaton . Analytcs
Inda Magazne. https://analytcsndamag.com/understandng-the-mportance-of-data-cleanng-and-
normalzaton/
Elsever . (2023). Sharng r esear ch data for journal authors | Elsever . www .Elsever .Com.
https://undefned/researcher/author/tools-and-resources/research-data
Falah, T., Nasserddne, G., & Youns, J. (2023). Detectng Data Outlers wth Machne Learnng. Al-Salam


Flach, P . (2012). Machne Learnng: The Art and Scence of Algorthms that Make Sense of Data  (1st bs).
Cambrdge Unversty Press.
GeoGebra. (2023). GeoGebra—100 mlyondan fazla öğr enc ve öğr etmen tarafından kullanılan ücr etsz
matematk araçları . GeoGebra. https://www .geogebra.or g/
Kartal, E. (2015). Sınıflandırmaya Dayalı Makne Öğr enmes T eknkler V e Kar dyolojk Rsk
Değerlendrmesne İlşkn Br Uygulama  [Doktora Tez]. İstanbul Ünverstes, Fen Blmler Ensttüsü.
Kartal, E., & Özen, Z. (2017). Dengesz Ver Setlernde Sınıflandırma. İçnde O. Torkul, S. Gülseçen, Y.
Uyaroğlu, G. Çağıl, & M. K. Uçar (Ed.), Mühendslkte Y apay Zeka ve Uygulamaları  (1. bs, ss. 109-131).
Sakarya Ünverstes Kütüphanes Yayınev.
Kartal, E., Özen, Z., Özyaprak, M., Şmşek, İ., Köse Bber , S., Bber , M., & Can, T. (2019). Dengesz Verden
Öğrenme: Üstün Zekalı ve Yetenekl Öğrenclern Sınıflandırılması. İçnde M. E. Balaban & E. Kartal (Ed.),
Ver Madenclğ ve Makne Öğr enmes T emel Kavramlar , Algortmalar , Uygulamalar  (1. bs, ss. 349-389).
Çağlayan Ktabev.
Mtchell, T. M. (1997). Machne Learnng  (1st Edton). McGraw-Hll Scence/Engneerng/Math.
quanthub. (2023, Eylül 18). Understandng the Machne Learnng Pr ocess thr ough Pr oblem Framng - .
https://www .quanthub.com/understandng-the-machne-learnng-process-through-problem-framng/
Ronaghan, S. (2019, Eylül 19). Data Understandng for Machne Learnng: Assessment & Exploraton .
Medum. https://towardsdatascence.com/data-understandng-for -machne-learnng-assessment-exploraton-
aca1aadc1cb6
Rousseeuw , P. (1987). Rousseeuw , P.J.: Slhouettes: A Graphcal Ad to the Interpretaton and Valdaton of
Cluster Analyss. Comput. Appl. Math. 20, 53-65. Journal of Computatonal and Appled Mathematcs , 20,
53-65. https://do.or g/10.1016/0377-0427(87)90125-7
Shearer , C. (2000). The CRISP-DM model: The new blueprnt for data mnng. Journal of data war ehousng ,
5(4), 13-22.
Shmuel, G., Bruce, P . C., Yahav, I., Patel, N. R., & Lctendahl, K. C. (2018). Data Mnng for Busness
Analytcs  (1. bs). Wley .
Venkat, N. (2018). The curse of dmensonalty: Insde out. Plan (IN): Brla Insttute of T echnology and
Scence, Plan, Department of Computer Scence and Informaton Systems , 10.
Walesak, M., & Dudek, A. (2020). The Choce of Varable Normalzaton Method n Cluster Analyss. İçnde
K. S. Solman (Ed.), Educaton Excellence and Innovaton Management: A 2025 V son to Sustan Economc
Development Durng Global Challenges  (ss. 325-340). Internatonal Busness Informaton Management
Assocaton (IBIMA).
Wrth, R., & Hpp, J. (2000). Crsp-dm: Towards a standard process model for data mnng. Proceedngs of
the 4th Internatonal Confer ence on the Practcal Applcatons of Knowledge Dscovery and Data Mnng , 1,
29-40.


**Ünte Soruları**


Aşağıdaklerden hangs Ver Madenclğ çn Çapraz Endüstr Standard Süreç Model ( CRoss-Industry
Standar d Process for Data Mnng - CRISP-DM ) adımlarından br değldr ?
(Çoktan Seçmel)
(A) Very anlama
(B) Ver hazırlama
(C) Ver normalzasyonu
(D) Modelleme
Problemn tanımlanması
Cevap-1 :
Ver normalzasyonu
Soru-2 :
Makne öğrenmes sürecnde “çöp grd-çöp çıktı ( garbage-n garbage-out )” kavramı le lgl aşağıda
verlenlerden hangs doğrudur?
(Çoktan Seçmel)
(A) Makne öğrenmes sürecnde kullanılan vernn kaltesz olması, modeln performansını olumsuz etkler .
(B) Gelştrlen modeln karmaşıklığının artması, makne öğrenmes sürecndek çöp grd-çöp çıktı lkesn
açıklar .
(C) Ver özetleme ve görselleştrme şlemler, çöp grd-çöp çıktı lkesne aykırıdır .
(D) Modeln uygulamaya geçrlmes aşamasında ortaya çıkan problemler , çöp grd-çöp çıktı lkesyle
lşkldr .
Yalnızca aykırı değerlern tespt kullanılarak çöp grd-çöp çıktı lkes açıklanablr .
Cevap-2 :
Makne öğrenmes sürecnde kullanılan vernn kaltesz olması, modeln performansını olumsuz etkler .
Soru-3 :
Aşağıdak seçeneklerden hangs sıralı kategork verye örnek verleblr?
(Çoktan Seçmel)
(A) Cnsyet (erkek, kadın).
(B) Renkler (kırmızı, mav, yeşl).
(C) Hayvan türler (köpek, ked, kuş).
(D) Telefon numaraları.


Cevap-3 :
Oylama çn kullanılan yıldız puanları (1 yıldız, 2 yıldız, 3 yıldız, 4 yıldız, 5 yıldız).
Soru-4 :
Aşağıdaklerden hangs ver hazırlama aşamasında kullanılan teknklerden br değldr ?
(Çoktan Seçmel)
(A) Ver ayrıklaştırma
(B) Ver toplama
(C) Boyut azaltma
(D) Ver temzleme
Ver normalzasyonu
Cevap-4 :
Ver toplama
Soru-5 :
Kategork br ntelğn makne öğrenmes analzlernde sayısal bçmde kullanılablmes çn aşağıdak
yöntemlerden hangs terch edleblr?
(Çoktan Seçmel)
(A) Yapay ( dummy ) kodlama
(B) Ver ayrıklaştırma
(C) Ver normalzasyonu
(D) Eksk değer tamamlama
Aykırı değer tespt
Cevap-5 :
Yapay ( dummy ) kodlama
Soru-6 :
Aşağıdak tabloda beş örneğe at yaş vers yer almaktadır . Eğer yaş ntelğ mnmum-maksmum
normalzasyon teknğ kullanılarak 0-1 aralığına ndr genmek stenrse ver setndek Örnek 1’n normalze
edlmş yaş değer aşağıdak seçeneklerden hangsnde doğru verlmştr?
Örnek Yaş
Örnek 1 25
Örnek 2 50
Örnek 3 35
Örnek 4 10


(Çoktan Seçmel)
(A) 0
(B) 0.25
(C) 0.375
(D) 0.5
1
Cevap-6 :
0.375
Soru-7 :
Aşağıda verlen kontenjans tablosuna göre soru şaretl yer aşağıdak kavramlardan hangs le temsl edlr?
(Çoktan Seçmel)
(A) True postves (doğru poztfler)
(B) True negatves (doğru negatfler)
(C) False negatves (yanlış negatfler)
(D) False postves (yanlış poztfler)
True postve rate (doğru poztf oranı)
Cevap-7 :
False postves (yanlış poztfler)
Soru-8 :
Regresyon analz sonucunda aşağıdak tabloda verlen değerler elde edlyor . Tablodak değerlere göre


Gerçek Değerler Tahmnler
50 50
90 88
77 79
53 52
83 80
(Çoktan Seçmel)
(A) - 0.5
(B) 0.5
(C) 0.6
(D) 0.7
(E) 0.8
Cevap-8 :
0.8
Soru-9 :
Farklı küme sayısı denemeler çn hesaplanan Slhouette katsayıları seçeneklerde yer almaktadır .
Seçeneklerde verlen Slhouette katsayılarına göre hang küme sayısının seçlmes en uygundur?
(Çoktan Seçmel)
(A) Küme Sayısı=2, Slhouette Katsayısı= 0.8
(B) Küme Sayısı=3, Slhouette Katsayısı= 0.7
(C) Küme Sayısı=4, Slhouette Katsayısı= 0.6
(D) Küme Sayısı=5, Slhouette Katsayısı= 0.5
Küme Sayısı=6, Slhouette Katsayısı= 0.4
Cevap-9 :
Küme Sayısı=2, Slhouette Katsayısı= 0.8
Soru-10 :
Aşağıdaklerden hangs makne öğrenmes analzlernde kullanılan bulut blşm platformlarından br
değldr ?
(Çoktan Seçmel)
(A) Amazon Web Servces
(B) Python


(D) Google Cloud Platform
IBM Cloud
Cevap-10 :


# 3. Python ile Veri Görselleştirme


**Özlü Söz**

Br resm bn kelmeye bedeldr .
Anonm


**Kazanımlar**

1.   Ver görselleştrmenn önemn anlar , farklı görselleştrme teknklernn projelerde nasıl
kullanılableceğn blr .
2.   Çzg grafğnn ( lne chart ) kullanım alanlarını anlar , Python programlama dl le htyaç duyulan çzg
grafğn çzeblr .
3.   Sütun grafğ ( bar chart ) kullanarak kategork verler nasıl görselleştrebleceğn anlar , Python
programlama dl le htyaç duyulan sütun grafğn çzeblr .
4.   Pasta grafğnn ( pe chart ) oranları ve yüzdeler nasıl temsl ettğn anlar , Python programlama dl le
htyaç duyulan pasta grafğn çzeblr .
5.   Serplme/saçılım dyagramının ( scatter plot ) k değşken arasındak lşky nasıl görselleştrdğn anlar ,
aykırı değerler serplme dyagramı le tespt edeblr , korelasyon ve dağılım analz yapablme yeteneğ
kazanır , Python programlama dl le htyaç duyulan serplme dyagramını çzeblr .
6.   Hstogramın ver setndek frekans dağılımını nasıl gösterdğn anlar , ntelklern dağılımını ve
yoğunluğunu görsel olarak analz edeblr , Python programlama dl le htyaç duyulan hstogramı çzeblr .
7.   Kutu grafğ ( box and whskers plot ) le br ntelğ görsel olarak fade edeblr aykırı değerler kutu
grafğ le tespt edeblr , farklı gruplar arasındak karşılaştırmaları kutu grafğ üzernden yapablr , Python
programlama dl le htyaç duyulan kutu grafğn çzeblr .
8.   Voln grafğn kutu grafğ le karşılaştırablr , br ntelğn dağılımını ve yoğunluğunu voln grafğ le
nasıl görselleştrebleceğn blr , Python programlama dl le htyaç duyulan voln grafğn çzeblr .
9.   Isı hartasının ( heatmap ) matrs şeklndek very kullanarak nasıl görselleştrdğn anlar , ntelkler
arasındak lşkler ısı hartası le görsel olarak analz edeblr , Python programlama dl le htyaç duyulan
ısı hartasını çzeblr .


1.   Makne öğrenmes sürecnde ver görselleştrmenn hang aşamalarda kullanılması faydalı olablr?
2.   Sürekl br ntelk çzg grafğ le görselleştrleblr m?
3.   Hang durumlarda sütun grafğnn terch edlmes mantıklı olablr? Hang ver tpndek ntelğ
kullanmak uygun olur?
4.   Öğrenclern sene sonu harf notu (AA, BA, BB, BC, CC, DD, FF) yüzde dağılımı Python programlama
dl kullanılarak pasta grafğ le nasıl görselleştrleblr?
5.   Serplme dyagramı le k ntelk arasındak lşk görselleştreblr m? Br örnek le açıklayınız.
6.   Hstogram, br ntelğn dağılımını görselleştreblr m?
7.   Kutu grafğ le ntelğe lşkn temel tanımlayıcı statstk blglere ulaşmak mümkün müdür?
8.   Kategork br ntelğn kutu grafğ çzleblr m?
9.   Sütun grafğ ve kutu grafğ arasında temel farklar nelerdr?
10. Hang grafk türler le aykırı değerler tespt edleblr?
11. Hang grafk türler le ntelğn dağılımı konusunda fkr sahb olunur?
12. Hang durumlarda Voln grafğ terch edleblr?
13. Python le ısı hartası kullanarak ntelkler arasındak lşkler nceleneblr m? Ntelklern hang ver
tpnde olması uygun olur?


**Başlamadan Önce**

Ver görselleştrme  (data vsualzaton ), very anlama ve raporlamada öneml br araçtır . Dolayısıyla
makne öğrenmes sürec çn de öneml br rol oynamaktadır . Bu bölüm, ver görselleştrmede kullanılan bazı
temel ve gelşmş grafk türler hakkında teork blglern yanı sıra her br grafğn Python programlama dl
kullanılarak çzm ve yorumlanmasını çerr .
Çzg grafğ  (lne chart ), sütun grafğ  (bar chart ), pasta grafğ  (pe chart), serplme dyagramı  (scatter
plot), hstogram , voln grafğ  ve ısı hartası  (heatmap ) bu bölümde ele alınan grafk türler arasındadır .
Grafklern temel kullanımının yanı sıra farklı grafk türler üzernden ntelkler arasındak lşklern
görselleştrlmes, aykırı değer tespt, ntelğn dağılımının grafkler üzernden keşfedlmes gb konulara yer
verlmştr . Bu kapsamda Python’da ver görselleştrmede sıklıkla kullanılan Matplotlb  ve Seaborn
kütüphanelernden faydalanılmıştır . Dğer tüm hesaplamalarda da Numpy  ve Pandas  kütüphaneler
kullanılmıştır .
Bu bölümden tbaren ele alınan konuların Python kodları verldğnden okuyuculara bu bölüme başlanmadan
önce Bölüm 2.8’de anlatılan gerekl kurumların tamamlanması tavsye edlmektedr . Bu ktapta
gerçekleştrlen analzlerde Python pr ogramlama dl  (versyon 3.1 1.6) ve Spyder  (versyon 5.5.0)
(Scentfc PYthon Development EnvRonment ) Bütünleşk Gelştrme Ortamı ( Integrated Development
Envr onment- IDE ) kullanılmıştır .
Bu bölüm le ver görselleştrme üzerne kazanılan tecrübenn pekştrleblmes çn okuyuculara, kamuya
açık ya da uzmanlık alanlarına göre seçecekler farklı ver setler üzernde çalışmaları  tavsye edlmektedr .


## 3.1. Ver Görselleştrmeye Genel Bakış

Bazen “ tek br r esm bnler ce sözcüğe bedeldr ” denlr (Shmuel vd., 2018). Br düşünce ya da fkr
sayfalarca metnle açıklamak yerne tek br görselle fade etmek metnden çok daha fazla şey
anlatablmektedr . Ver blm çalışmalarında analzlere başlamadan önce very anlama, analzler sırasında
elde edlen sonuçları yorumlama ve analzler sonrasında karar vercler çn rapor hazırlama aşamalarında
ver görselleştrme nn (data vsualzaton ) sağladığı avantajlardan yararlanılmaktadır .
Bu bölümde Python programlama dln kullanılarak bazı temel ve ler düzey ver görselleştrme yöntemler
Matplotlb  (Hunter , 2007) ve Seaborn  (Waskom, 2021) sml k öneml ver görselleştrme kütüphanes
uygulamalarıyla açıklanacaktır . Analzler sırasında NumPy  (C. R. Harrs vd., 2020) ve Pandas  (McKnney ,
2010) kütüphanelernden faydalanılmıştır . Bu sebeple Python’da bu sayılan kütüphaneler yüklü değlse
kodlamaya geçlmeden önce yüklenmeldr .
CMD komut stem ekranı ( console ) (Şekl 18), Apple ve Lnux şletm sstemlernde Termnal ekranı veya
Spyder ’da sağ alt pencerede yer alan “T ermnal” aracılığı le (Şekl 19) aşağıdak kod bloğunda lk dört kod
satırını kullanarak bu kütüphaneler yükleneblr ( Öneml Not:  Spyder ’ın 5.5.0 versyonunda Termnal
mevcut değldr). Kütüphaneler yüklendkten sonra bu kütüphanelern fonksyonlarını, ver setlern vb.
Python kodunda kullanablmek çn mport  sözcüğü le çalışmaya dâhl edlmeldr . NumPy , Pandas ,
Matplotlb.pyplot  ve Seaborn  en sık kullanılan kısa adları olan np, pd, plt ve sns le çağrılmıştır .


Şekl 18: CMD komut stem ekranı le kütüphanelern yüklenmes.


matplotlb.pyplot as plt  kod satırı, Matplotlb  kütüphanesnn matplotlb.pyplot  modülünü plt takma smyle
koda dahl etmek çn kullanılır . Böylece plt sm çağrıldığında matplotlb.pyplot  modülündek fonksyonlar
kullanablecektr . matplotlb.pyplot  modülü grafkler oluşturmak, ver görselleştrmek ve çeştl grafk
özellklern ayarlamak çn kullanılmaktadır .
Bu bölümde ele alınan uygulamada br sağlık sgortası şrketne at müşter vers ( nsurance.csv )
kullanılmıştır (kaggle, 2018): https://www .kaggle.com/bmarco/health-nsurance-data?select=nsurance.csv .
Ver setnde toplamda 1338 adet örnek ( observaton/sample ), 7 adet ntelk ( attrbute ) bulunmaktadır (T ablo
16). Ver set br Pandas  DataFrame  olarak saklanmıştır .
Tablo 16: Sgorta ver set.

Çalışma klasörünün oluşturulması ve Spyder ’da hazırlık:  Ver görselleştrme teknklernn detaylarına
geçmeden önce ver set, ver kaynağından blgsayara ndrlmeldr . Çalışmalarda kolaylık olması çn
blgsayarda br çalışma klasörü  (workng dr ectory ) oluşturulması ve ardından Spyder ’da sağ üst köşede yer
alan klasör smges ( 

browse a workng dr ectory ) le çalışma klasörü konumunun belrlenmes ve son olarak kodların yazıldığı
Python betk dosyası le blgsayara ndrlen nsurance.csv  ver set dosyasının aynı çalışma klasöründe yer
alması gerekmektedr .
Çalışma klasörüne kopyalanan nsurance.csv  dosyasını okumak çn Pandas  kütüphanesnden pd.read_csv()
fonksyonu kullanılmıştır . Bu fonksyona yalnızca “ nsurance.csv ” argümanı verlmştr . Herhang br dosya
yolu belrtlmemştr . Çünkü zaten üzernde çalışılan Python betk dosyası le ver set aynı klasör çnde


Ver set okunduktan sonra ntelk adları Türkçeleştrlmştr . Yan age yerne yas, sex yerne cnsyet , …
kullanılmıştır .


Ver analzlernde olduğu kadar ver görselleştrmede de dkkat edlmes gereken unsurlardan br ntelklern
ver türüne uygun grafklern seçlmesdr . Bu nedenle ver setndek ntelklern ver tpn kontrol etmek ve
gerekyorsa uygun ver tp dönüşümünü yapmak önemldr . Cnsyet ( sex), sgara çme durumu ( smoker ) ve
bölge ( regon ) kategork ntelkler olduğundan ver tpler category  ver tpne dönüştürülmüştür .
Dönüştürme şlem öncesnde ve sonrasında verSet.dtypes  kodu kullanılarak ntelklern ver tp kontrol
edlmştr (Şekl 20).


Şekl 20: Ver tp dönüşümü önces ve sonrasında ntelklern durumu.
Ver setnde cnsyet , sgaraDurum  ve bolge  ntelklernn kategorler Türkçeleştrlmştr . Örneğn; aşağıda
yer alan Python kod bloğunun lk satırında cnsyet ntelğndek male , female  kategorler yerne sırasıyla
erkek , kadın  atanmıştır . sgaraDurum  ve bolge  ntelklernn kategorler de benzer mantıkla


Ver setnn descrbe()  fonksyonu le elde edlen özet Şekl 21’de verlmştr .


Şekl 21: Ver set özet.
Şekl 21’e dkkat edlrse ver set özetnde sadece nümerk ntelkler yer almaktadır . Eğer tüm ntelkler
görüntülenmek stenrse descrbe()  fonksyonuna nclude="all"  parametres eklenmeldr . Ayrıca yan yana
gösterlecek sütun sayısı dsplay .max_columns  le 20 olarak ayarlanmıştır . Elde edlen son ekran görüntüsü


Şekl 22:  Ver set özet.

## 3.2. Çzg Grafğ

Ver görselleştrmede terch edlen yardımcı en temel yöntemlerden br çzg grafğ dr (lne chart ). Örneğn
lk 10 müşternn yaşlarının çzg grafğ aşağıdak kod bloğu le elde edlmştr (Şekl 23). Matplotlb
kütüphanesnn grafk çzmek çn kullanılan en temel fonksyonu plot()  fonksyonudur . plot()
fonksyonunun lk parametres grafğn x-eksennde, knc parametre se y-eksennde yer alacak değerler
almaktadır . x-eksennde müşterlern 1’den 10’a kadar ndeks numaralarını (ID) göstereblmek çn range()
le br dz tanımlanarak x değşkenne atanmıştır . y değşkenne se ver setnn yas ntelğne at lk 10 değer
atanmıştır . Grafktek ver noktalarının kırmızı yuvarlaklar le göstermn sağlayan se "o:r"  değerdr .


Şekl 23:  İlk 10 müşter yaşlarının çzg grafğ le gösterm- 1.
Aynı grafk her br ver noktasında syah üçgenler yer alacak şeklde aşağıdak kod yardımı le çzdrleblr
(Şekl 24).


Şekl 24:  İlk 10 müşter yaşlarının çzg grafğ le gösterm- 2.
Aşağıdak kodda plot()  fonksyonda lnestyle  parametresyle çzg tp, color  parametresyle çzg reng,
lnewdth  parametresyle çzg genşlğ ayarlanmış ve elde edlen grafğn ekran görüntüsü Şekl 25’ te
verlmştr .


Şekl 25:  İlk 10 müşter yaşlarının çzg grafğ le gösterm- 3.
İlk yrm ve knc yrmde yer alan müşterlern vücut ktle ndeks değerlernn ( vk) çzg grafğ üzernde
karşılaştırılablmes çn aşağıdak kodlar kullanılablr (Şekl 26). Aşağıdak kod bloğunda, özellkle grafk
çzmne lşkn (plt le bağlantılı) kod satırlarının tümünün seçlmes ve aynı anda çalıştırılması
gerekmektedr . Aks halde, grafk düzgün br bçmde görüntülenemeyecektr . plt.xtcks(x1)  kod satırı le


Şekl 26:  İlk ve knc 20’dek müşterlern çzg grafğ le vücut ktle ndeks karşılaştırması- 3.
Şekl 27’de lk 50 müşternn yaşı çzg grafğ le gösterlmektedr . xlabel()  fonksyonuyla x-eksennn adı,
ylabel()  le y-eksennn adı verlmektedr . Grafğn x ve y eksenlerne ızgara  (grd) eklemek çn plt.grd()
kullanılablr . İstenrse sadece x-eksenne yatay ya da sadece y-eksenne de dkey çzgler ekleneblr . Bunu
sağlayan kodlar yorum satırı olarak verlmştr . Bu yorum satırları kaldırılarak nceleme yapılablr .


Şekl 27:  İlk 50 müşternn yaşlarının çzg grafğ üzernde gösterm.
Bazı durumlarda aynı grafk alanında brden fazla grafğn görüntülenmes steneblr (Şekl 28). Örneğn; lk
yrm ve knc yrmde yer alan müşterlern yaşlarını alt alta k farklı çzg grafğnde elde edeblmek çn
aşağıdak kod bloğu kullanılablr . Burada dkkat edlmes gereken plt.subplot()  fonksyonudur .
plt.subplot(2, 1, 1)  grafk alanının 2 satır ve 1 sütun olarak ayarlandığını ve lk grafkle lgl tanımlamaların
yapıldığını söylemektedr . plt.subplot(2, 1, 2) se grafk alanının 2 satır ve 1 sütun olarak ayarlandığını ve
knc grafkle lgl tanımlamaların yapıldığını söylemektedr . plt.supttle()  le tüm grafğn başlığı verlr .
plt.tght_layout()  fonksyonundak pad parametres, aynı çerçevede lstelenen grafklern brbrleryle olan
mesafesn ayarlamak çn kullanılır . Bu parametre kullanılmadığında lk grafğn x-eksenne at etketler le
knc grafğn başlığı ç çe geçmektedr .


Yukarıdak kod bloğunda k adet yorum satırı mevcuttur .
• plt.subplot(2, 1, 1)  satırının yorumu kaldırılıp yerne plt.subplot(1, 2, 1)  satırının başına yorum eklenrse
• plt.subplot(2, 1, 2)  satırının yorumu kaldırılıp yerne plt.subplot(1, 2, 2)  satırının başına yorum eklenrse
ve aynı kod bloğu yenden çalıştırılırsa bu kez de grafk alanı 1x2 şeklnde kullanılmış olur ve Şekl 29 elde
edlr .


Şekl 29: Grafk alanının 1x2 şeklnde kullanılması.
Elde edlen son grafkte (Şekl 29) x-eksenndek etketlern ç çe geçmş olduğu görüleblr . Bu nedenle,
grafk alanı bçmlendrmes öneml br konudur . plot()  fonksyonuna at brçok parametre bulunmaktadır .
Bunlar help(plt.plot)  le nceleneblr .

## 3.2. Sütun Grafğ

Sütun grafğ  (bar chart ) sıkça kullanılan grafk türler arasında yer almaktadır . Sütun grafğ, dkey veya
yatay eksendek sütunların boylarına göre very yorumlamak çn kullanılır . Python programlama dlnde
plt.bar()  fonksyonu yardımıyla sütun grafğ çzleblr . Ver setnde yer alan müşterlern sgara çme
durumuna ( sgaraDurum ) göre sgorta şrketne ödenen ortalama mktar ( odemeMktar ) araştırılmak
stensn. Sütun grafğ çzlmeden önce ver setne groupby()  fonksyonu yardımıyla sgara çp çmeme
durumuna göre ortalama ödeme mktarı ozet sersne atanmıştır . Ardından sgara çp çmeme durumları
(evet/hayır) x eksennde ( x parametres), ortalama ödeme mktarları da y eksennde ( heght  parametres)
olacak bçmde sütun grafğ elde edlmştr . Grafğ görsel açıdan zengnleştrmek çn htyaca yönelk farklı


Şekl 30:  Müşterlern sgara çme durumlarına göre ortalama ödeme mktarı- 1.
Şekl 30’da yer alan sütun grafğnde her br sütunun üzerne sgara çen ve çmeyenlern ortalama ne kadar
ödeme yaptığını gösteren ver etket eklemek çn aşağıdak kullanıcı tanımlı Python fonksyonu
kullanılablr . Bu fonksyon sırasıyla x ve heght  parametrelerne gelen very almaktadır . Ortalama ödeme
mktarının grafğn üzernde fazla yer kaplamaması çn .round(2)  fonksyonu le vr gülden sonra k
basamak yuvarlanmıştır . Elde edlen grafk Şekl 31’de verlmştr .


Şekl 31: Müşterlern sgara çme durumlarına göre ortalama ödeme mktarı- 2.
Şekl 31’de verlen sütun grafğne göre sgara çen müşterlern sgortaya yaptığı ortalama ödeme mktarı


Eğer plt.bar()  yerne plt.barh()  fonksyonu kullanılırsa dkey sütun yerne yatay sütun grafğ elde
edlecektr . Bu durumda, x ve heght  parametrelernn yern sırasıyla y ve wdth  parametrelernn alacağı
unutulmamalıdır (Şekl 32).


Şekl 32:  Sütun grafğnn yatay bçmde elde edlmes.
plt.bar()  fonksyonunda wdth  parametres, plt.barh()  fonksyonunda heght  parametres sütunlar arasında
kalan boşluğu belrlemektedr . Aşağıda verlen kod satırları çalıştırıldığında Şekl 33 elde edlecektr .


Şekl 33:  Sütun grafğnde sütunlar arası boşluğun ncelenmes.

## 3.3. Pasta Grafğ

Tıpkı sütun grafğ gb pasta grafğ  (pe chart ) de y blnen ve çokça terch edlen grafkler arasındadır .
Frekans ve yüzde değerlernden yola çıkılarak kategork br ntelk pasta grafğ le kolaylıkla fade edleblr .
Örnek olarak müşterlern bölgelere göre sgortaya yaptığı toplam ödeme mktarının yüzdes plt.pe()
fonksyonuyla pasta grafğ bçmnde verlmştr (Şekl 35). Grafk oluşturulmadan önce bölgelere ( bolge )
at kategorlern her br çn toplam ödeme mktarı ( odemeMktar ) groupby()  fonksyonu yardımı le


Şekl 34:  ozet sers.
Sonrasında bu ozet verden hareketle pasta grafğnn üzernde yer alacak ver etketler ( etketler ), grafk
oluşturulurken kullanılan ortalama ödeme mktarları ( degerler ), sns kütüphanesnde yer alan vrds  renk
paletnden dört farklı renk ( renkler ) ve pasta dlmlernn dışa doğru ayrılma oranları ( secm ) tanımlanmıştır .
Ardından plt.pe()  fonksyonu kullanılarak pasta grafğ çzlmştr . Grafğn üzernde yüzdelern gösterlmes
çn autopct  kullanılmaktadır . Grafğn üzernde % şaret başta yer alacaktır , bunun çn %%  olmak üzere
k adet yan yana yüzde şaret kullanılmıştır . Ondalıklı sayının ( float ) vrgül dahl toplam 4 karakter ,
vrgülden sonra tek basamak gösterlmes çn 4.1f kullanılmıştır . Pasta grafğ başlangıcının x eksennden
saat yönünün tersne bçmde döndürüldüğü açı startangle=360  olarak belrlenmştr (Şekl 35).
Ver görselleştrmede renklern önem de yadsınamazdır . Brbryle zıt ya da uyumlu renklern seçleblmes
çn bu örnekte olduğu gb brçok farklı renk palet bulunmaktadır . Örneğn vrds, nferno, magma, cefr e,
Spectral, Reds, summer , vb. Renk paletler konusunda daha fazla blg çn bknz. (HolyPython.com, 2023).


Şekl 35:  Müşterlern bölgeye göre toplam ödeme mktarı yüzdesn gösteren pasta grafğ.
Şekl 35’ te yer alan pasta grafğne göre sgortaya yapılan toplam ödeme mktarının bölgeler arasında
yüzdesel dağılımı ncelendğnde güneydoğu bölges %30.2 le en büyük dlme sahptr . Ardından %24.5 le


## 3.4. Serplme Dyagramı

İk değşken arasındak lşky belrlemek çn serplme dyagramı  (scatter plot ) kullanılablr . Serplme
dyagramında br ntelk x eksennde dğer ntelk y eksennde verleblr . Şekl 36’dak serplme
dyagramında müşter yaşlarına ( yas) göre vücut ktle ndekslernn ( vk) dağılımı görüleblr . Dyagramın
üzerndek her br nokta x ve y eksenlernde yer alan ntelklere göre ver setndek her br gözlem temsl
etmektedr . Dyagram plt.scatter()  fonksyonu le kolayca çzleblmektedr . x ve y eksenlernde kullanılacak
ntelkler le eksen adları belrlenerek en temel grafk görünümü elde edleblr (Şekl 36).


Şekl 36:  Müşterlern yaşlarına göre vücut ktle ndekslernn verldğ serplme dyagramı.
Serplme dyagramındak noktalar soldan sağa doğru yokuş yukarı br grafk çzyorsa x ve y eksenlerndek
ntelkler arasında poztf yönlü br  lşk olduğu anlamına gelr . Yan x arttığında y de artma eğlmndedr
(Bknz. Şekl 37). Eğer noktalar soldan sağa doğru yokuş aşağı br grafk çzyorsa bu durumda da x ve y
eksenlerndek ntelkler arasında  negatf yönlü br  lşk  olduğu söylenr . Yan x arttığında y azalma


Şekl 37: Müşterlern yaşlarına göre ödeme mktarlarının verldğ serplme dyagramı.
Şekl 37’de yer alan serplme dyagramının çzm çn gereken Python kodları aşağıda verlmştr .


Serplme dyagramıyla k ntelk arasında doğrusal br lşknn olup olmadığı gözlemleneblr . Böyle br
durumda gözlemler yokuş yukarı ya da yokuş aşağı yönde br doğru boyunca uzanır . Şekl 37’de ver
setnden alınan 10 gözleme at yaş le ödeme mktarının serplme dyagramı çzdrlmştr . Dyagram, 10
gözlem çn yaş ve ödeme mktarı ntelkler arasında doğrusal br lşk olduğunu göstermektedr; ancak bu
ödeme mktarındak br artışın yaşta artışa neden olduğu anlamına gelmemektedr . Buradan hareketle
serplme dyagramları k ntelk arasındak olası bağlantı  (assocaton ) veya lşk y (relatonshp ) gösterr;
ancak bu bağlantı k ntelk arasında br neden-sonuç lşksnn olduğu anlamına gelmez (Rumsey , 2021a).
Bu durum şu örnekle açıklanablr: Her gün C vtamn alan kşlern daha az COVID-19’a yakalandığı
gözlemlenmş olsun. O halde C vtamnnn COVID-19’u önledğ söyleneblr m? Bu sorunun cevabı “her
zaman değl” olmalıdır . Çünkü COVID-19’dan korunmak çn maske takma, dğer kşlerle mesafel olma,
sık sık el yıkama gb pek çok önlem faktörü mevcuttur . COVID-19’dan korunmak ve bağışıklığını
güçlendrmek steyen nsanlar her gün C vtamn alıyor olablrler; ancak yukarıda bahsedlen faktörlere de
aynı zamanda dkkat etmş olablrler . Gerçekten C vtamnnn COVID-19 hastalığı üzerndek etks
araştırılmak stenyorsa dğer faktörlern sabtlendğ ya da dışarıda tutulduğu y br deney tasarımına htyaç
duyulacaktır .
Ver setnde bulunan kategork ntelkler serplme dyagramında farklı renklerde gösterleblr , yan grafğe
üçüncü br boyut ekleneblr . Yaşa göre müşterlern sgortaya ödeme mktarlarını sgara çp çmeme
durumları tüm ver setndek gözlemler dkkate alınarak Şekl 38’de verlmştr . Bu gösterm çn


Şekl 38:  Müşterlern yaşlarına göre ödeme mktarlarının verldğ serplme dyagramı- 2 (renklendrme
sgara çme durumuna göre yapılmıştır).
Şekl 38’e göre genel olarak sgara çmeyen müşterlern sgortaya ödedkler mktarın çenlere göre daha alt
br aralıkta (0-20000) seyrettğ görülmektedr . Ayrıca, sgara çen ve çmeyen müşterlerde yaş arttıkça
yapılan ödeme mktarı da artmıştır .
Serplme dyagramı üç-boyutlu da çzleblr . Örneğn sgortaya yapılan ödemenn yaşa göre ncelendğ
serplme dyagramına vücut ktle ndeks ntelğ üçüncü boyut olarak eklenrse Şekl 39 elde edlr . Öncelkle
çzlecek grafğn boyutları belrlenmştr . Ardından grafkte 3-boyutlu br çzmn yapılacağı projecton
="3d"  le fade edlmştr . Sonrasında ax.scatter()  fonksyonuna x, y ve z eksenlernde yer alacak ntelkler
sırasıyla yaş ( yas), ödeme mktarı ( odemeMktar ) ve vücut ktle ndeks ( vk) olarak verlmştr . Her br
eksenn etket atanmış; yalnızca z-eksennn etketnn dkey bçmde yazdırılablmes çn rotaton=90
kullanılmıştır . Ayrıca z eksen etketnn grafğn üzernde olması çn dolgu seçeneğ ( labelpad ) -0.7 olarak


Şekl 39:  3-boyutlu serplme dyagramı.
Pandas  kütüphanesnde yer alan pd.plottng.scatter_matrx()  fonksyonu, belrlenen ntelklere at serplme
dyagramının matrsn verr . Bu matrs yardımıyla tüm nümerk ntelkler arasında çzleblecek olası tüm
serplme dyagramlarının görüntülenmesnn yanı sıra matrsn köşegennde ntelklere at hstogramlara da


Şekl 40:  Serplme dyagramı matrs.

## 3.5. Hstogram

Genellkle sütun grafğne benzeyen ver görselleştrme yöntemlernden br de hstogramlardır; ancak
aralarındak en öneml farklardan br yatay eksende sütun grafğnde kategork br ntelk yer alırken
hstogramda sürekl  değerl br ntelk kullanılır (Y au, 2014). Ayrıca sütun grafğnde yalnızca sütunun
yükseklğ yorumlanırken hstogramda sütuna at hem yükseklk hem de genşlk değerlendrmeye alınır .
Hstogram, her sınıfa özgü oluşturulan dkdörtgenlerden oluşturulur (Ünver vd., 2021). Dkdörtgenlere ya da
her aralığa düşen gözlemlern sayısı sayılır ve br frekans dağılım grafğ elde edlr (NCSS Statstcal
Software, 2023): Dkey eksen frekansı, yatay eksen se ver değerlernn olası aralığını temsl eder .
Hstogramlar , tek br sürekl ntelğn normal dağılıma (Gauss dağılımına) uyup uymadığı (normallğ), sağa
ya da sola çarpık olma ya da ortaya toplanmış olma durumu hakkında blg verr .
Örneğn müşterlern vücut ktle ndeksler ncelenmek stensn. Aşağıda sns.hstplot()  fonksyonu le dkey
ve yatay k hstogram çzlmştr . Ver setnde hstogramı çzlecek olan ntelğn adı, lk dkey hstogramda


Şekl 41:  Dkey ve yatay hstogramlar .
Hstogramın en öneml parametrelernden br eşt genşlkl dkdörtgenlern ya da bölmelern sayısını
belrleyecek olan bns parametresdr . Varsayılan olarak bunu sns.hstplot()  fonksyonu otomatk olarak
belrlemektedr; ancak bns belrl sayısal değerler de alablr .


Şekl 42:  Farklı bölme sayıları kullanarak çzlen vücut ktle ndeks hstogramları.
Şekl 42’dek sarı hstogram ele alınsın. Grafkte 8 adet bölme ortaya çzdrlmştr . İlk bölmede vücut ktle
ndeks yaklaşık 16 le 21 arasında olan 50 müşter yer alırken, knc bölme vücut ktle ndeks 21 le 26
arasında olan 200 kşnn olduğuna şaret etmektedr . Grafğn en sağ tarafında yer alan bölmedek müşterler
uç nokta olarak düşünüleblr . Çünkü vücut ktle ndeks 48 ve üzernde oldukça az sayıda müşter mevcuttur .
Ntelğn ver dağılımı smetrk olduğunda hstogram da smetrk bçmde elde edlr . Sağ ve sol kuyruklar


küme elde edlmş ve bu alt kümelerde de müşterlere at vücut ktle ndeksler kullanılarak Şekl 43’ te yer
alan k farklı hstogram çzlmştr . Hstogramların adlarından da görülebleceğ gb elde edldkler alt
kümelern lknde ntelğn dağılımı sağa çarpık (poztf çarpıklık), kncsnde se sola çarpıktır (negatf
çarpıklık). Dağılım sağa çarpık olduğunda;
• ortalama ortanca değerden büyüktür ,
• sağ kuyruk sol kuyruktan daha uzundur ,
• ortanca değer brnc kartl ( quartle ) değerne daha yakındır .
Dağılımın sola çarpık olması durumunda yukarıda sayılan durumların aks meydana gelmektedr .


Şekl 43:  Hstogram örnekler.

## 3.6. Kutu Grafğ

Kutu-bıyık grafğ  (box and whsker plot ) ya da kısaca kutu grafğ brden fazla grubun dağılımını brbryle
karşılaştırmak çn sıklıkla kullanılan grafk türlernden brdr . Örnek olarak öncelkle aşağıdak kod bloğu
le vücut ktle ndeks özet ncelenrse en küçük değern 15.96, en büyük değern 53.13, ortalamanın 30.66,
ortanca değern ( medan ) 30.40, 1. kartl değern 26.30 ve 3. kartl değern 34.69 olduğu görüleblr (Şekl
44).


Şekl 44:  Ver setnde odemeMktar değşkennn özet blgs.
Aşağıdak kodlar yardımı le vücut ktle ndeks ( vk) ntelğnn kutu grafğ çzleblr . plt.boxplot()
fonksyonu yardımıyla elde edlen kutu grafğ Şekl 45’ te verlmştr . vert parametres grafğn dkey
çzleceğn gösterr . Kutu grafğ üzernde ortalamanın ve ortalama çzgsnn de gösterleceğ sırasıyla


sırasıyla ortanca değer ve ortalama çzglerne at özellkler göstermektedr . Kutu grafğne çentk eklemek
çn notch  parametres kullanılmaktadır . Ntelğn ortanca değerne lşkn güven aralığını gösteren kutu
grafğndek bu çentk, varsayılan olarak %95'lk br güven aralığını temsl etmektedr .


Şekl 45:  Ver setnde vücut ktle ndeks ntelğnn kutu grafğ.
Grafkte bıyık çzgsnn üstünde yer alan ve nokta olarak temsl edlen gözlem değerler vücut ktle ndeks
ntelğnn ( vk) aykırı değerlerdr ( outlers ). Ntelğe at en büyük ve en küçük değerler sırasıyla 53.13 ve
15.96 olarak görüleblr .
Kutu grafğnde kutunun br kısmının dğernden daha uzun olması o tarafın daha fazla ver çerdğ anlamına
gelmez. Çünkü bu gösterm örnek boyutunun kendsne değl, örnek boyutunun yüzdelerne dayanır
(Rumsey , 2021b). Br dğernden daha uzunsa bu bölümdek ver değerler daha genş br aralığı gösterr ,
dğer br fadeyle ver daha dağınıktır (Rumsey , 2021b). 1. çeyreklk kısım (Q1) vernn %25’n, 3. çeyreklk
kısım (Q3) se vernn %75’n kapsar . 2. çeyrek değer aynı zamanda ver setnn ortanca ( medan ) değerdr
(30.40). Ortalama değer ( mean ), ortanca değern hemen üzernde 30.66 yer almıştır . IQR bçmnde gösterlen
se çeyrekler  arası aralık tır (nterquartle range ) ve vernn orta %50’lk kısmını kapsar . Bu aralık ne kadar
büyük olursa ver set de o kadar değşkendr (Rumsey , 2021b).
Hstogramda olduğu gb kutu grafğnden de ver dağılımının (normal dağılıma göre) durumu, smetrs, sağa
ya da sola çarpık (poztf ya da negatf çarpık) olduğu belrleneblmektedr (Şekl 46). Smetrnn şeklnn
tespt çn yalnızca kutu grafğne bağlı kalınmaması ve analzlerde kutu grafğ le brlkte hstogramın da


Şekl 46:  Ver dağılımının ncelendğ kutu grafğ örnekler.
Şekl 47’de yer alan tüm yazılar , oklar ve değerler kutu grafğnn R dl (cran.r -project.or g, 2023) le
çzmnden sonra draw .o (2021) le eklenmştr .


Şekl 47: Kutu grafğ.
Şekl 45 ve Şekl 47’den görüleceğ gb vücut ktle ndeksne lşkn aykırı değerler 34.69’dan büyük olan
gözlem değerler olarak belrlenmştr . Hatta ntelktek en büyük değer de br aykırı değerdr (53.13); ancak
nokta bçmnde verlen dğer aykırı değerlern ne olduğu bu halde açıkça görülememektedr .
Kutu grafğne lşkn aşağıda verlen örnekte se müşterlern sgara çp çmeme durumlarına göre sgortaya
ödedkler mktarlar karşılaştırılmıştır (Şekl 48). Bu örnek sns.boxplot()  fonksyonu le çzlmştr . Yatay br
kutu grafğ elde edlmek stendğ çn sürekl ntelk olan ödeme mktarı ( odemeMktar ) x parametres,
farklı grupları/kategorler temslen sgara çme durumu ntelğ se ( sgaraDurum ) y parametres olarak


Şekl 48:  Grupların karşılaştırıldığı kutu grafğ.
Şekl 48’de verlen kutu grafğ ncelendğnde, sgara çenlern ödeme mktarının çmeyenlere göre daha
genş ve yüksek değerlerdek br aralıkta seyrettğ görüleblr . Sgara çen grupta ödeme mktarı sola
çarpıklık göstermektedr . Dğer br deyşle sgara çenlern çnde çok ödeme yapanlar az ödeme yapanlara
göre brbrne daha yakındır . Sgara çmeyenlerde ödenen en yüksek mktar 22000 cvarındadır; bunun
üzerndekler aykırı değer olarak görülmüştür .
Ayrıca br gruba at kutu grafğnn ortanca değer çzgs dğer grubun kutu grafğnn kutusu dışında kalırsa,
k grup arasında fark olması muhtemeldr dye düşünülmektedr . Şekl 48’de de sgara çenlern ortanca
değer çzgs sgara çmeyen grubun kutusunun dışındadır . Yan sgortaya yapılan ödemeler dkkate
alındığında sgara çenler ve çmeyenler arasında fark olması muhtemeldr denlr .

## 3.7. Voln Grafğ

Kutu grafğnn Kernel yoğunluk fonksyonuyla ( Kernel densty functon ) brleştrlmesyle oluşturulan
Voln grafğ Python’da sns.volnplot()  fonksyonu yardımıyla çzdrlmektedr (Şekl 49). Voln grafğnn
k ana unsuru bulunmaktadır . Bunlardan lk, ver setnn dağılımını temsl eden Voln görsel, kncs se
kutu grafğdr . Bu nedenle Şekl 49’da elde edlen grafk Şekl 48 le benzerlk göstermektedr . Ek olarak
kategorlere göre sgortaya yapılan ödemenn (frekans) dağılımı da grafk üzernde gösterlmştr .
Voln grafğ, kutu grafğnden elde edleblecek sonuçlara ek olarak sayısal br ntelğn genel dağılımını,


Şekl 49:  Voln grafğ.

## 3.8. Isı Hartası

Isı hartası ntelkler arasındak lşky belrlemek maksadıyla kullanılır . Ver setnde yer alan dört adet
sayısal ntelk arasındak lşklern (korelasyon) cor()  fonksyonu le hesaplanması ve sonrasında ısı hartası
(heat map ) le görselleştrlmes vernn anlaşılablmes açısından faydalı olacaktır (Şekl 51). Öncelkle
corr()  fonksyonu le Pearson korelasyon katsayılarının tutulduğu korelasyon  adlı DataFrame  elde
edlmştr . Pearson korelasyon katsayısı yalnızca nümerk ntelkler arasında hesaplandığından, verlen kod
satırında ver setnde yalnızca nümerk ntelkler seçlmştr . Pearson korelasyon katsayısı -1 le +1 arasında
değerler almaktadır . Eğer katsayı 1’e yakınsa k ntelk arasında poztf yönde güçlü br lşk, -1’e yakınsa
negatf yönde güçlü br lşk var denr . Katsayı sıfıra yaklaştıkça ntelkler arasındak lşk azalır , zayıflar .


Şekl 50’de verlen korelasyon matrs smetrktr . Tek br ntelğn kend kendne lşksnden söz
edlemeyeceğnden köşegende yer alan 1 değerler yorumlanmaz. Şekl 50 ncelendğnde müşterlern yaşı
ve sgortaya yaptığı ödeme mktarı arasındak Pearson korelasyon katsayısının 0.299 olduğu görülecektr . Bu
k ntelk arasında çok güçlü br lşkden söz edlemez; ancak lşk yönü poztftr (br artarken dğernn de


Şekl 50: Korelasyon matrs.
Isı grafğ Seaborn kütüphanesnde sns.heatmap()  fonksyonu yardımıyla çzleblr . Fonksyona sırasıyla
korelasyon matrs le annot  parametres sayesnde ısı hartası üzernde gösterlecek olan sayısal değerler
eklenr . Isı hartasındak her br bölmenn kare olarak gösterleblmes çn squar e=True olarak seçlmştr .
Bu parametreye False  değer verlp aynı kodlar tekrar çalıştırılırsa fark daha kolay görüleblecektr .


Şekl 51 ncelenecek olursa poztf yönde belrlenen en yüksek lşk yaş ve sgortaya ödenen mktar
arasındadır . Genel anlamda ntelkler arası lşkler poztf yöndedr; ancak kuvvetl değldr . İlşklern
negatf yönde olması durumunda Pearson korelasyon katsayısı da negatf değer alacak ve bu durum grafkte
kırmızı ve tonları şeklnde gösterlecektr .


Şekl 51: Ntelkler arasındak lşklern ısı hartasıyla gösterlmes.


**Bölüm Özet**

Bu bölüm, Python le ver görselleştrme  (data vsualzaton ) üzerne hem teork hem de uygulamalı blgler
çermektedr . Bu kapsamda Python dlnde ver görselleştrmede kullanılan Matplotlb  ve Seaborn
kütüphanelernden faydalanılmıştır . Bu bölümde öğrenlenler hem vernn anlaşılması hem de makne
öğrenmes projesnn sonuçlarının sunulması adımlarında kullanılablecektr .
Çzg, sütun ve pasta grafkler neredeyse lkokul yıllarından ber çok y blnen temel grafk türlerdr ve bu
grafklern Python'da nasıl çzdrleceğ anlatılmıştır . Grafklern çzmnde ver setnde bulunan ntelklern
sahp olması gereken doğru ver türüne dkkat çeklmştr .
Bu bölümde ayrıca daha gelşmş sayılablecek serplme dyagramı ( scatter plot ), hstogram, kutu grafğ
(box and whsker plot ), Voln grafğ ve ısı hartası ( heatmap ) grafklerne de yer verlmştr . Python le
temel ve gelşmş grafkler oluşturmanın pratk örnekler ve kullanım alanlarına yer verlmştr . Bunun yanı
sıra grafklern elde edldkten sonra yorumlanmasına lşkn açıklamalar okuyucuya sunulmuştur . Bu
bölümde kazanılan tecrübenn pekştrlmes çn okuyuculara farklı ver setler üzernde denemeler
yapmaları  önerlmektedr .


**Kaynakça**

draw .o. (2021). Draw .o. https://app.dagrams.net/
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
HolyPython.com. (2023). Colors wth Python . HolyPython.Com. https://holypython.com/python-
vsualzaton-tutoral/colors-wth-python/
Hunter , J. D. (2007). Matplotlb: A 2D graphcs envronment. Computng n Scence & Engneerng , 9(3), 90-
95. https://do.or g/10.1 109/MCSE.2007.55
kaggle. (2018). Health Insurance Data . https://www .kaggle.com/bmarco/health-nsurance-data?
select=nsurance.csv
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
NCSS Statstcal Software. (2023). Chapter 143 Hstograms . https://www .ncss.com/wp-
content/themes/ncss/pdf/Procedures/NCSS/Hstograms.pdf
Rumsey , D. J. (2021a). How to Interpret a Scatterplot. Dummes .
https://www .dummes.com/educaton/math/statstcs/how-to-nterpret-a-scatterplot/
Rumsey , D. J. (2021b). What a Boxplot Can Tell You about a Statstcal Data Set. Dummes .


Shmuel, G., Bruce, P . C., Yahav, I., Patel, N. R., & Lctendahl, K. C. (2018). Data Mnng for Busness
Analytcs  (1. bs). Wley .
Ünver , Ö., Gamgam, H., & Altunkaynak, B. (2021). Temel İstatstk Yöntemler Olasılık—Hpotez T estler—
Regr esyon Analz  (10. bs). Seçkn Yayıncılık.
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021
Yau, N. (2014, Şubat 27). How to Read and Use Hstograms n R. FlowngData .
https://flowngdata.com/2014/02/27/how-to-read-hstograms-and-use-them-n-r/
VanderPlas, J. (2016). Python Data Scence Handbook: Essental T ools for W orkng W th Data  (1st ed.).
O’Relly Meda.


**Ünte Soruları**

Soru-1 :
Aşağıdaklerden hangs Python’da ver görselleştrme üzerne özelleşmş kütüphaneler arasındadır?
(Çoktan Seçmel)
(A) Pandas
(B) NumPy
(C) Matplotlb
(D) random
Sckt-learn
Cevap-1 :
Matplotlb
Soru-2 :
Matplotlb kütüphanesnde temel çzm fonksyonlarına ulaşablmek çn aşağıda verlen boşluğa
seçeneklerden hangs gelmeldr?
matplotlb ________________ as plt
(Çoktan Seçmel)
(A) .pyplot
(B) .pltplot


(D) .py
.plt
Cevap-2 :
.pyplot
Soru-3 :
Aşağıdak kod satırlarına göre, seçeneklerden hangs kesnlkle doğrudur?
(Çoktan Seçmel)
(A) x-eksennde çalışma yılı sayısı, y-eksennde se toplam gelr gösterlmektedr .
(B) x-eksennn adı Toplam Gelr , y-eksennn adı se Çalışma Yılı Sayısı olarak belrlenmştr .
(C) x-eksennn adı Çalışma Yılı Sayısı, y-eksennn adı se Toplam Gelr olarak belrlenmştr .
(D) Grafkte x ve y-eksenlernn adı yazdırılmaz.
Grafkte ızgara ( grd) bulunur .
Cevap-3 :
x-eksennn adı Toplam Gelr , y-eksennn adı se Çalışma Yılı Sayısı olarak belrlenmştr .
Soru-4 :
Br futbol maçı öncesnde, k takımın toplam pas yüzdeler karşılaştırılmak stenmektedr . Bunun çn
aşağıdak grafklerden hangsnn seçm daha uygun olur?
(Çoktan Seçmel)
(A) Isı hartası
(B) Kutu grafğ
(C) Hstogram
(D) Serplme dyagramı
(E) Sütun grafğ
Cevap-4 :
Sütun grafğ
Soru-5 :


(Çoktan Seçmel)
(A) plt.pe()
(B) plt.bar()
(C) plt.scatter()
(D) plt.plot()
plt.boxplot()
Cevap-5 :
plt.pe()
Soru-6 :
Aşağıdak grafk türlernden hangs ya da hangler br ntelğn dağılımı hakkında blg verr?
I. Serplme dyagramı
II. Hstogram
III. Kutu grafğ
IV. Voln grafğ
V. Isı hartası
(Çoktan Seçmel)
(A) I ve II
(B) II ve III
(C) I ve III
(D) II, III ve IV
III ve IV , V
Cevap-6 :
II, III ve IV
Soru-7 :
Kutu grafğ çzmnde plt.boxplot()  fonksyonundak notch  parametres ne çn kullanılır?
(Çoktan Seçmel)
(A) Kutu grafğndek ortanca değern ( medan ) güven aralığını temsl eder .
(B) Kutu grafğndek ortalama değern (mean) güven aralığını temsl eder .


(D) Kutu grafğndek en küçük değern ( mnmum ) güven aralığını temsl eder .
Kutu grafğndek aykırı değerlern ( outlers ) güven aralığını temsl eder .
Cevap-7 :
Kutu grafğndek ortanca değern ( medan ) güven aralığını temsl eder .
Soru-8 :
Matrs türündek br vernn aşağıdak grafk türlernden hangs le görselleştrlmes daha uygundur?
(Çoktan Seçmel)
(A) Serplme dyagramı
(B) Hstogram
(C) Kutu grafğ
(D) Voln grafğ
(E) Isı hartası
Cevap-8 :
Isı hartası
Soru-9 :
Seaborn  kütüphanes le yaş değşkenne at yatay  br hstogram çzlmes stenyor . Bu durumda aşağıdak
Python kod satırında boş bırakılan yere aşağıdak seçeneklerden hangs getrleblr?
sns.hstplot(data=ver, _____ )
(Çoktan Seçmel)
(A) x="yas"
(B) y="yas"
(C) z="yas"
(D) vert="yas"
hor="yas"
Cevap-9 :
y="yas"
Soru-10 :
Hstogram le lgl aşağıdak seçeneklerde verlen blglerden hangs yanlıştır ?


(A) Br ntelğn frekans dağılımı kullanılarak oluşturulan grafk türüdür .
(B) Hstogramı oluşturan her br dkdörtgen kutunun hem en hem de boyu blg verr .
(C) İk ntelk arasındak poztf ya da negatf yönlü lşk gözlemleneblr .
(D) Ntelğn dağılımının sağa (poztf çarpıklık) ya da sola çarpık olduğu keşfedleblr .
Ver dağılımının smetrs hakkında blg sahb olunablr .
Cevap-10 :


# 4. Python ile Veri Ön-İşleme


**Özlü Söz**

Bast br şeklde açıklayamıyorsanız, yeternce y anlamamışsınız demektr .
Albert Ensten


**Kazanımlar**

1.   Temel ver ön-şleme adımlarını Python kullanarak gerçekleştreblr .
2.   Ver setndek ntelklern ver tp dönüşümlern gerçekleştreblr .
3.   Eksk verler tespt edeblr ve uygun yöntemlerle tamamlayablr .
4.   Ver ayrıklaştırmanın ( data dscr etzaton ) ne olduğunu blr ve Python le gerçekleştreblr .
5.   Ver setnn özet blgsn alablr ve yorumlayablr , ver gruplandırma şlemlern gerçekleştreblr .
6.   Ver setndek tekrarlanan gözlemler ( duplcates ) belrleyeblr ve bu değerlere nasıl müdahale
edleceğn anlar .
7.   Aykırı değerler ( outlers ) tanımlayablr ve bu değerlere nasıl müdahale edleceğn anlar .
8.   Python dln kullanarak ver setnden rastgele örneklemeler ( random samplng ) oluşturablr .
9.   Tabakalı örneklemenn ( stratfed samplng ) ne olduğunu anlar ve Python le uygular .
10. Yapay ( dummy ) kodlamanın ne olduğunu blr ve Python le gerçekleştreblr .
11. Ver normalzasyonunun ( data normalzaton ) ne olduğunu blr ve Python le gerçekleştreblr .


**Brlkte Düşünelm**

1.   Python'da ver tp dönüşümler çn hang fonksyonlar kullanılır?
2.   Eksk verler ( mssng values ) tespt etmek ve tamamlamak çn hang yöntemler terch edlr?


4.   Kategork verler sayısal formata dönüştürmek çn Python'da hang teknkler uygulanır?
5.   Python le ver setnn temel statstksel özet nasıl oluşturulur?
6.   Very belrl krterlere göre gruplandırma ve bu gruplar üzernde şlemler yapma konusunda Python'da
hang fonksyonlar kullanılır?
7.   Python'da ver setnde tekrar eden gözlemler ( duplcates ) tespt etmek ve bu gözlemlerle başa çıkmak
çn hang yollar zleneblr?
8.   Aykırı değerler ( outlers ) belrleme ve bu değerlere müdahale etme süreçler Python le nasıl
gerçekleştrlr?
9.   Python'da rastgele örnekleme ( random samplng ) ve tabakalı örnekleme ( stratfed samplng ) çn hang
kütüphane ve fonksyonlar kullanılır?
10. Yapay kodlama ( dummy codng ) nasıl yapılır? Python'da bu şlem gerçekleştrmek çn hang yöntemler
terch edlr?
11. Ver normalzasyonu ( data normalzaton ) nedr? Python'da ver normalzasyonu şlemler nasıl yapılır?


**Başlamadan Önce**

Makne öğrenmes sürecnde deneym olarak algortmaya sunulan gerçek dünya versnn analzlerde
başarıyla kullanılablmes çn ver ön-şleme adımları hayat önem taşımaktadır . Ver ön-şleme üzerne
teork blglere Bölüm 2.5’ te yer verlmştr . Ktabın bu bölümü, Bölüm 2.5’ te söz edlen bazı ver ön-şleme
teknklernn Python le uygulamalı şeklde anlatımını çermektedr . Bu nedenle htyaç duyulması halnde
lgl bölüm gözden geçrlerek blgler tazeleneblr . Bu bölümde yapılan analzlerde araç özellklerne lşkn
UCI Makne Öğrenmes Ver Deposu’nda ( UCI Machne Learnng Repostory ) auto-mpg.data  ver set
kullanılmıştır . Bu nedenle bu bölümdek uygulamalara başlamadan önce okuyucuların bölümün başında
belrtldğ gb ver setn blgsayarına ndrmes gerekmektedr . Ayrıca bu bölümde Python'da makne
öğrenmes analzlernde sıklıkla kullanılan Sckt-learn  kütüphanes de kullanılmıştır .
Ktabın bu bölümü, okuyucuların sıklıkla karşılaşableceğ düşünülen aşağıda sıralanan ver ön-şleme
sürecndek temel adımları Python programlama dln kullanarak uygulamalı bçmde sunmaktadır .
• Ver tp dönüşümü ve eksk vernn tamamlanması ( mssng data mputaton ).
• Sürekl ntelkler belrl aralıklara bölmek ve kategork verye dönüştürmek amacıyla gerçekleştrlen ver
ayrıklaştırma ( data dscr etzaton ).
• Ver set özetleme ve ntelklern belrl krterlere göre gruplandırılması.
• Ver setndek tekrar eden gözlemlern ( duplcates ) tespt edlmes.
• Aykırı değerlern tespt edlmes ( outler detecton ).
• Rastgele örnekleme ( random samplng ) ve tabakalı örnekleme ( stratfed samplng ).
• Kategork ntelkler sayısal formata dönüştürmede kullanılan yapay kodlama ( dummy codng ).
• Farklı ölçeklerdek ntelkler aynı ölçeğe getrmey sağlayan ver normalzasyonu ( data normalzaton ).


## 4.1. Python le Temel Ver Ön-şleme Teknkler

Öncek bölümlerde de vur gulandığı üzere makne öğrenmes sürecnn öneml unsurlarından br verdr .
Makne öğrenmes sürec verden öğrenen modeller oluşturulmasını çerr . Makne öğrenmes
algortmalarının verye uygulanmasından önce htyaç duyulması halnde brtakım ver ön-şleme
yöntemlernden faydalanılması gerekeblr . Ktabın bu bölümünde Python programlama dl le ver tp
dönüşümü, eksk vernn tamamlanması, ver ayrıklaştırma, ver set özet ve ver gruplandırma, tekrar eden
gözlemlern bulunması, aykırı değerlern tespt, rastgele örnekleme ve tabakalı örnekleme, yapay ( dummy )
kodlama ve ver normalzasyonu ver ön-şleme yöntemlerne lşkn örneklere yer verlmştr .
Bu bölümde analzlerde araç özellklerne lşkn br ver set ( auto-mpg.data ) kullanılmıştır (Qunlan, 1993):
https://archve.cs.uc.edu/dataset/9 . Ver setnde 3 ayrık, 5 sürekl nümerk ntelk le 1 adet metn tpnde
ntelk bulunmaktadır . Ver setndek lk ntelk, galon başına ml cnsnden şehr çnde yakıt tüketm
versdr ( mpg) (Tablo 17). Br öncek bölümde olduğu gb bu bölümde de NumPy  (C. R. Harrs vd., 2020)
ve Pandas  (McKnney , 2010) kütüphaneler kullanılmış ve lave olarak özellkle makne öğrenmes analzler
çn oldukça popüler br kütüphane olan Sckt-learn  kullanılmıştır (Pedregosa vd., 201 1). Rastgele br sayı
elde etmek, lsteden rastgele br öğe seçmek, öğeler rastgele karıştırmak vb. gb rastgelelk le lgl şlemler
gerçekleştreblmek çn random  modülü çağrılmıştır . Ek olarak grafk çzm çn Seaborn  kütüphanesnden
faydalanılmıştır (W askom, 2021). Eğer bu kütüphaneler yüklü değlse Bölüm 3.1’de açıklandığı gb
termnalden kurulmalıdır . Kurulma şlem yapılmışsa öncelkle aşağıdak kod satırları Python koduna dahl
edlmeldr .

Tablo 17: auto-mpg ver set.
Ntelk Türkçes Kısaltma Ver Tp
mles per gallon (mpg) ml cnsnden şehr çndek yakıt tüketm (galon başına ml) mpg Sürekl
cylnders slndrler cylnders Ayrık
dsplacement motor deplasmanı dsplacement Sürekl
horsepower beygr gücü horsepower Sürekl
weght ağırlık weght Sürekl
acceleraton hızlanma acceleraton Sürekl
model year model yılı model_year Ayrık
orgn menşe orgn Ayrık
car name araba adı car_name Metn

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm 3.1’dek
şlemlern bu bölüm kapsamında da yapılması önerlmektedr . UCI Makne Öğrenmes Ver Deposu’nda
(UCI Machne Learnng Repostory ) bulunan ver set, sıkıştırılmış (. zp) dosya olarak ndrlmektedr . Bu
.zp dosyasında yer alan auto-mpg.data  dosyası dkkate alınmalıdır . Aşağıda verlen Python kod bloğu


Ver setn okumak çn pd.read_csv()  fonksyonu kullanılmıştır . Fonksyon, öncelkle dosya adını (" auto-
mpg.data ") parametre olarak almıştır . sep parametres ver dosyasında sütunların (ntelklern) brbrnden
nasıl ayrıldığını belrten parametredr . "\s+"  değer, verlern br veya daha fazla boşluk karakteryle
ayrıldığını belrtmek çn kullanılmıştır . Ver dosyasında sütun adları bulunmadığından header  = None  olarak
alınmıştır . Sütun adlarının verldğ names  parametresne lk satırda ntelk smlernn saklandığı
ntelkAdlar  sml değşken verlmştr . decmal  parametresyle de verdek nümerk ntelklern ondalıklı
sayı ayıracı olarak nokta (.) olduğu belrtlmştr . Ver set okunduktan sonra Spyder ’da sağ üst bölümde yer
alan “ Varable Explor er” penceresne bakılırsa, ver setnn 398 adet örnek ( observaton/sample ), 9 adet
ntelkten oluştuğu görüleblr . Bu pencerede verSet  üzerne k kere tıklanarak Şekl 52 elde edleblr .


Şekl 52: auto_mpg ver set.
verSet.dtypes komutuyla ver setnde bulunan ntelklern ver tp nceleneblr . Şekl 53’ te cylnders ,
model_year , orgn  gb ayrık değerler çn nt64 , mpg , dsplacement , weght , accleraton  gb sürekl
değerler çn de float64  ver tp kullanıldığı görüleblr .


object  ver tp Pandas  kütüphanesnde metn veya karışık sayısal ve sayısal olmayan değerler çn
kullanılmaktadır . Ver setnde br tek horsepower  ve car_name  ntelkler object  olarak okunmuştur , oysak
horsepower  ondalıklı değerler çerdğnden bu ntelğn de float64 olması gerekmektedr . Aslında bu durum
horsepower  ntelğ çndek eksk değerlern verde (?) le gösterlmesnn sonucudur (Şekl 54).


Şekl 54: horsepower ntelğndek eksk değerler .

## 4.2. Ver Tp Dönüşümü ve Eksk Vernn Tamamlanması

Genellkle ver setndek eksk verler Python’da nan (not a number ) le gösterlmektedr . Bu nedenle
horsepower ntelğndek soru şaret (?) le verlen değerler yerne np.nan  atanmıştır . Ardından horsepower
ntelğnn ver tp DataFrame  nesnesne özgü .astype()  fonksyonu yardımı le float64 ’e dönüştürülmüştür .
float64  dışında object , nt64 , bool, category  gb ver tpler de htyaca uygun bçmde terch edleblr .


Hang ntelkte kaç adet eksk değer var görmek çn aşağıdak kod satırı kullanılablr . Çıktı ncelendğnde
yalnızca horsepower  ntelğnde 6 adet eksk değer olduğu görüleblecektr (Şekl 55).


horsepower  ntelğndek eksk vernn tamamlanması çn fllna()  fonksyonu kullanılablr . horsepower
sürekl br ntelk olduğundan ntelktek eksk ver, o ntelğn ortalaması le doldurulablecektr . Ortalama
atanırken ntelkte yer alan dğer değerler le uyumu açısından vr gülden sonra 0 adet basamak olacak şeklde
atama yapılması stenmştr . Eksk değerler tamamlandıktan sonra yne eksk değer kontrolü yapılırsa ver


Şekl 55:  Ver setnde her br ntelğe at eksk değerlern sayısı.
Aşağıdak kod satırı yardımı le de benzer şlem gerçekleştrleblr .


Örneğn ver setnde renk gb br kategork ntelk olsaydı ve eksk değerler çerseyd bu durumda aşağıdak
kod satırında olduğu gb ntelkte en sık tekrar eden değer eksk değerlern yerne atanablecektr .


## 4.3. Ver Ayrıklaştırma

Nümerk br ntelğn kategork hale getrlmes şlem ver ayrıklaştırma  (data dscr etzaton ) olarak
blnmektedr . auto-mpg  ver setnde yalnızca nümerk ntelkler mevcuttur . Ver set özetnde kategork br
değşkenn durumunu da görmek adına ver setnn sonuna durum  adında yen br sütun eklensn. Aşağıdak
kod satırları kullanarak durum  sütununa mpg  değer 23.5’ ten düşükse “Düşük”, 23.5 le 30 arasında se
“Orta”, aks halde “Yüksek” değerler yazılsın. Pandas  kütüphanesnn  astype("category")  fonksyonu


Benzer şlem pd.cut()  fonksyonu le aşağıdak bçmde de yapılablr . Fonksyon lk olarak ayrıklaştırılmak
stenen mpg  ntelğn almaktadır . bns parametres kategorlern alt ve üst sınırlarıdır ( bolmeler ) (alt sınır
dahl edlmez, üst sınır dahl edlr ). Örneğn mpg  ntelğnde 8’den büyük ve 23.4 dâhl tüm değerler
“Düşük” kategors olarak belrlenr . 23.4’ ten büyük ve 29.9 dâhl tüm değerler “Orta” kategors olarak
belrlenr . 29.9’dan büyük ve 46.6 dâhl tüm değerler “Yüksek” kategors olarak belrlenr . labels
parametresne se kategor adları ( bolmeKategorler ) verlr . Böylelkle kullanıcı tarafından belrlenen alt ve
üst sınırlar çerçevesnde ver ayrıklaştırma yapılmış olur (Şekl 56).


Şekl 56: Kullanıcı tarafından belrlenen alt ve üst sınırlar kullanılarak elde edlen mpg ntelğnn
kategorler.


Bunun dışında ver ayrıklaştırma çn eşt fr ekans  (equal fr equency ) yöntem de kullanılablr . Her aralıkta
yaklaşık eşt sayıda örneğn yer almasına odaklanılır . Bu şlem çn pd.qcut()  fonksyonu kullanılablr . Bu
fonksyon, kategork hale getrlmes stenen very ve bölme sayısını alır . Ardından elde edlen durum_ef
ntelğnn frekans tablosu Şekl 57’de verlmştr .


Eşt aralık  (equal nterval ) br başka ver ayrıklaştırma yöntemdr . Bu yöntemde her aralığın boyunun eşt
olması sağlanır , aralıktak örneklern sayıları dkkate alınmaz. Bu şlem çn de lk örneğe benzer şeklde
pd.cut()  fonksyonu kullanılablr . Bu fonksyon, kategork hale getrlmes stenen very ve aralık sayısını
alır. Ardından elde edlen durum_ea  değşkennn frekans tablosu Şekl 58’de verlmştr .


Şekl 58: Eşt aralık ver ayrıklaştırma yöntem uygulamasından sonra mpg ntelğnn kategorler.

## 4.4. Ver Set Özet ve Ver Gruplandırma

Ver setnn özet değerlern görmek çn descrbe()  fonksyonu kullanılablr . Aşağıdak kodlar yardımı le
elde edlen ekran görüntüsü Şekl 59’da verlmştr . descrbe()  fonksyonunun çıktısı dkkatle ncelenrse
nümerk ntelkler çn; 
kaç adet örnek olduğu ( count ), 
ortalama ( mean ), 
standart sapma ( std), 
mnmum değer ( mn), 
kartl ( 25% ), 
kartl/ortanca değer ( 50%  ya da medan), 
kartl ( 75% ) ve 
maksmum değer ( max)
verlmştr . Kategork ntelkler çn se; 
kaç adet örnek çerdğ ( count ), 
kaç kategorye sahp olduğu ( unque ),
en yüksek frekansa sahp olan kategornn adı ( top),
ver setnde o kategorye sahp kaç örnek olduğu ( freq) 
blgler verlmştr . Bu blglerden faydalanılarak ntelklerdek olası bazı hatalar tespt edleblecektr .
pd.set_opton("dsplay .max_columns", 20)
verSet.descrbe(nclude="all")


Şekl 59: Ver set özet.
Ver özet ncelemes tamamlandıktan sonra ver setnde farklı ntelkler kullanılarak gruplandırma
(aggregaton ) şlem gerçekleştrleblr . Ktabın ver görselleştrme bölümünde sütun ve pasta grafğ
çzlrken ver gruplandırma şlemnden faydalanılmıştır . Örneğn aşağıdak Python kod satırlarının
döndürdüğü sonuçlar aynıdır . Yan mpg  ntelğnn durum kategorsne göre ortalaması alınırsa “Düşük”
kategorsndeklern ortalaması 17.26, “Orta” kategorsndeklern 26.34, “Yüksek” kategorsndeklern
ortalaması se 34.63’ tür. Fark se döndürdükler ver tplerdr . A değşken DataFrame  ken B değşken
Seres  nesnesdr (Şekl 60).
A = verSet[["mpg", "durum"]].groupby("durum").mean()
B = verSet.groupby("durum")["mpg"].mean()
Şekl 60: A ve B nesnesn çeren ekran görüntüsü.
Ortalama alma dışında kategorlere göre toplam, frekans, en küçük değer , en büyük değer , standart sapma
gb değerler de aşağıdak kodlar yardımı le bulunablr . En son satırdak descrbe()  fonksyonuna lşkn


verSet[["mpg", "durum"]].groupby("durum").sum()
verSet[["mpg", "durum"]].groupby("durum").count()
verSet[["mpg", "durum"]].groupby("durum").mn()
verSet[["mpg", "durum"]].groupby("durum").max()
verSet[["mpg", "durum"]].groupby("durum").std()
verSet[["mpg", "durum"]].groupby("durum").descrbe()
Şekl 61: Gruplandırmada descrbe() le elde edlen ekran görüntüsü.

## 4.5. Tekrar  Eden Gözlemlern Bulunması

Ver setnde eğer farklı satırlarda tamamen aynı değerler mevcutsa tekrar eden gözlemler/örnekler ortaya
çıkar . Bunun gb tekrar eden gözlemlern bulunablmes çn duplcated()  fonksyonu kullanılablr .
keep="frst"  parametres, tekrar edlen gözlem değer harç bu gözlemden sonra tekrar eden dğer
gözlemler True olarak şaretler , dğer gözlemler False  olarak şaretler . keep="last"  se bunun tam tersn
yapar , yan son tekrar eden gözlem harç bu gözlemden önce tekrar eden dğer gözlemler True olarak
şaretler , ger kalanlar False  olur (Şekl 62).


Şekl 62:  tekrarlar_f değşken yazdırıldığında elde edlen ekran görüntüsü.
Tekrar eden tüm gözlemler göreblmek çn aşağıdak Python kodları kullanılablr . Kullanılan ver setnde


Şekl 63:  Ver setnde tekrar eden gözlem değerlernn lstes.
Eğer ver setnde tekrar eden gözlemler bulunsaydı, fazla olanları ver setnden çıkarmak çn aşağıda verlen
Python kodu kullanılablrd. Bu kod yardımı le verSet  DataFrame’nde yer alan tekrar gözlemler
çıkarılacak ve son hal le verSet2  olarak kaydedlecektr .


## 4.6. Aykırı Değerlern Tespt

Aykırı değerler verde dğerlerne göre daha uzak br noktada olan ver noktalarına verlen smdr . Aykırı
değerler , ver görselleştrme bölümünde de bahsedldğ gb saçılım dyagramı ve kutu grafğ le tespt
edleblr . Bu bölümde verlen örnekte, horsepower  ntelğne at aykırı değerler kutu grafğne lşkn temel
statstksel değerler yardımı le elde edlmştr . İk farklı yol sunulmaktadır .
I. Yol:
horsepower  ntelğne at aykırı değerler kutu grafğnn de çzmnde kullanılan çeyrekler arası aralık ( Inter
Quartle Range - IQR ) hesaplamadan faydalanılarak tespt edlecektr (geeksfor geeks.or g, 2021). Bunun çn
1. kartl ve 3. kartl değerler ( q1 ve q2) le çeyrekler arası aralık ( IQR ) hesaplanmıştır . Buradan hareketle, 1.
kartln br buçuk IQR katı aşağı noktası alt ( alt) sınır; 3. kartln br buçuk IQR katı yukarı noktası üst ( ust)
sınır olarak belrlenmştr .


Böylece artık ver setnde horsepower  ntelğ belrlenen alt ve üst sınırlar dışında olan değerler aykırı değer
olarak kabul edlecektr . Aşağıda üst sınırın üzernde ve alt sınırın altında kalan değerlere sahp örnekler
sırasıyla ust_aykrDegerInd  ve alt_aykrDegerInd  değşkenlerne atanmıştır .


Şekl 64’ ten de görüleceğ üzere horsepower  ntelğnde yalnızca üst sınırın üzernde olan aykırı değerler
mevcuttur (Örneğn, 6, 7, 8, … ndeks numaralı örnekler). Alt sınırın altında kalan hçbr değer
bulunamamıştır .


Şekl 64: Aykırı değerler lstes.
Bu durum aşağıdak kodlar yardımı le oluşturulan kutu grafğnden de görüleblr (Şekl 65). Üst bıyık
çzgsnn üzerndek dareler aykırı değerler temsl etmektedr . Oysa alt bıyık noktasının altında dare
yoktur .


Şekl 65: horsepower ntelğne at kutu grafğ.
Eğer aykırı değerler ver setnden kaldırılmak stenrse aşağıdak Python kodları çalıştırılablr .


Aykırı değerlern tespt ve aykırı değerlere sahp örneklern ver setnden çıkarılablmes çn knc yol
olarak aşağıdak kod bloğu kullanılablr . Matplotlb  kütüphanesnn cbook  modülünden boxplot_stats()
fonksyonu çağrılmıştır . Yalnızca boxplot_stats(verSet.horsepower)  kodu çalıştırılırsa kutu grafğne
lşkn temel statstksel blgler yazdırılır (Şekl 66). Bu blglern detayları çn Spyder ’da Help penceresne
boxplot_stats yazılablr . Bu blgler arasında flers , ntelğe at aykırı değerler vermektedr: 220, 215, 225,
… Bu aykırı değerlere at örneklern ndeks numaraları se aykrDegerIndeksler  değşkenne atanmıştır .
aykrDegerIndeksler  yazdırılırsa yukarıdakne benzer şeklde Index([6, 7, 8, 13, 25, 26, 27, 67, 94, 95,
116], dtype='nt64') elde edlr . verSet.dr op() le lgl ndeks numarası verlen aykırı değerlern bulunduğu
örnekler (satırlar axs=0  le belrtlmştr) ver setnden slneblr .


Şekl 66: horsepower kutu grafğne lşkn temel statstksel blgler .


## 4.7. Rastgele Örnekleme ve Tabakalı Örnekleme

Örnekleme ( samplng ), br popülasyon çnden belrl br grup temslcnn seçm olarak tanımlanablr .
Danışmanlı öğrenme algortmaları le çalışılırken ver setn bastçe eğtm ve test ver set olarak kye
ayırmak gerekmektedr . Bu bölümde eğtm ve test ver setlerne örneklern rastgele seçmnn nasıl
yapılacağı ve nelere dkkat edleceğ sorularına yanıt aranacaktır . Python’da rastgele yapılacak şlemler çn
random  modülü ve random  modülü çnden sample  fonksyonu çağırılmıştır . Ardından lstem  adlı çnde
1’den 20’ye kadar olan sayıların yer aldığı br lste tanımlanmıştır . Bu lste çnden rastgele 10 örnek
seçlmek stendğnde sample() fonksyonu kullanılmıştır . Ardından bu şlem knc kere tekrar edlmştr .
Şekl 67’de sample()  fonksyonunun brnc kez ve knc kez çalıştırıldığında elde edlen ekran görüntülerne
sırasıyla yer verlmştr . Sonuçlar ncelenrse sample()  fonksyonunun her sefernde farklı rastgele sayıları
döndürdüğü görülecektr . Ayrıca döndürdüğü değerler çnde tekrar eden sayı mevcut değldr . Örneğn; 2, 3,


Şekl 67: sample() fonksyonu 1. ve 2. kez çalıştırıldığında elde edlen ekran görüntüsü.
Eğer her sefernde aynı rastgele sayıların üretlmes stenrse random.seed()  fonksyonu kullanılmalıdır .
random.seed(123)  fonksyonu rastgelelk çeren kodun öncesne yazılarak kodun her sefernde aynı rastgele
sayıları üretmes sağlanmıştır (Şekl 68). random.seed()  fonksyonuna 123 yazılması da zorunlu değldr ,
herhang br sayı yazılablr . Öneml olan her sefernde aynı rastgele seçmn elde edleblmes çn seed()
çnde aynı sayının kullanılmasıdır (Şekl 68 ve Şekl 69).


Şekl 68: sample() fonksyonu seed() le yenden peş peşe çalıştırıldığında elde edlen ekran görüntüsü.


Şekl 69: seed() çnde farklı br sayı kullanılarak sample() fonksyonu yenden çalıştırıldığında elde edlen
ekran görüntüsü.
Seçm yapılırken br sayının brden fazla kere seçleblmesne zn vermek çn random.choces()  fonksyonu
kullanılablr (Şekl 70).


Şekl 70: random.choces() fonksyonu çalıştırıldığında elde edlen ekran görüntüsü.
auto-mpg  ver set ( verSet ) rastgele %70’ eğtm, %30’u da test ver set olacak şeklde kye ayrılmak
stenrse sample()  fonksyonu kullanılablr . frac=0.7  öncelkle ver setnden %70’lk br bölümün
alınacağını, replace=False  se yapılan seçmde her örneğn yalnızca br kere görülebleceğn söyler .
random_state  parametres öncek örneklerde kullanılan random.seed()  le benzer görev görür . Her
defasında aynı rastgele örneklern eğtm ver setnde olmasını sağlar . İlk satır kullanılarak eğtm ver set
(egtm ) elde edlmş olur . Sonrasında verSet.ndex.sn(egtm.ndex)  le ver setndek tüm örnekler
eğtm ver setne atanmış mı dye kontrol edlr . Eğer atanmışsa nd değşken o ndeks değernde yer alan
örnek çn True, aks halde de False  değern alır . Sonrasında test ver setne ( test), eğtmde yer alan
örneklern ndeks değerne sahp olmayan tüm örnekler atanır . Bunun çn ver setnde köşel parantezler
arasında nd değşkennden önce tlda  (~) şaret kullanılmıştır ( verSet[~nd] ). Son durumda eğtm ver
setnde toplamda 279, test ver setnde se toplamda 1 19 örnek olacak şeklde auto-mpg  ver set %70’e %30
oranında kye ayrılmıştır . Bunu sağlayan Python kodu aşağıda verlmştr .


auto-mpg  ver setn ( verSet ) rastgele %70’ eğtm ve %30’u test ver set olarak kye ayrılırken aynı
zamanda durum ntelğnn eğtm ver setnde %70 ve test ver setnde %30 oranlarında dağılması çn
tabakalı kl ayırma yöntem  kullanılmalıdır . Bunun çn Sckt-learn  kütüphanes model_selecton  modülü
çnden tran_test_splt()  fonksyonu çağrılablr .
tran_test_splt()  fonksyonundak lk ar güman ver setdr ( verSet ). Ardından tran_sze  parametresne
eğtm ver setnn hang oranda olacağı blgs verlr . Böylelkle ger kalan da test ver setne ayrılmış olur .
stratfy  parametres hang ntelk kullanılarak tabakalı örneklemenn yapılacağını gösterr . Bu örnekte
durum  ntelğ kullanılmıştır . Fonksyon gerye aynı anda hem eğtm hem de test ver setn
döndürdüğünden çoklu atama şlemne uygundur . Bu nedenle fonksyonun döndürdüğü değerler sırasıyla
egtm1  ve test1  olarak atanmıştır .


Bu yolla elde edlen eğtm ( egtm1 ) ve test ( test1 ) ver setlernde sırasıyla 278 ve 120 adet örnek yer
almaktadır . Burada durum ntelğne at Düşük ve Yüksek kategorlernn arasındak oranın eğtm ve test ver
setlernde de korunduğuna dkkat edlmeldr . Bu aşağıdak Python kodlarının çalıştırılması le


Şekl 71 ncelenrse tüm ver setlernde kategorler arasındak oranın korunduğu görüleblr . Yan 208 adet
düşük, 98 adet orta ve 92 adet yüksek kategorsndek örneklerden rastgele %70’ eğtm %30’u test ver
setne atanmıştır .


Şekl 71:  Eğtm ve test ver setlerndek durum ntelğ kategorlernn frekans dağılımının orjnal ver set
le karşılaştırılması.

## 4.8. Yapay (Dummy) Kodlama

Ver setndek kategork ntelklern nümerk hale getrlerek analzlerde kullanılması mümkündür . Bu gb
durumlarda nümerk olarak anlam taşımayan yapay ( dummy ) kodlamadan faydalanılablr . Pandas
kütüphanesndek get_dummes()  fonksyonuyla yapay ( dummy ) kodlama yapılmaktadır .
Bölüm 2.4’ te bahsedldğ üzere yapay kodlama k farklı şeklde gerçekleştrleblr . Bunlardan lk durum
ntelğnde olduğu gb kategorler arasında sıralı br bağlantı varsa sıra gözetlerek kategorler artan sayısal
değerlere dönüştürüleblr . Bunun çn aşağıdak Python kod satırı kullanılablr . durum  ntelğnde
.cat.codes  yardımı le “Düşük” çn 0, “Orta” çn 1, “Yüksek” çn de 2 değerler fonksyon tarafından


Şekl 72: durum ntelğnn sayısal değerler le fade edlmes- 1.
Kategorlern bu örnektek gb sıralı olmadığı varsayılsın. Bu gb durumlarda ntelklere at kategorler kl
(0, 1) değerlere dönüştürüleblr . Aşağıda verlen kod bloğundak lk satırda durum  ntelğ
pd.get_dummes()  fonksyonu yardımı le kl-matrs forma dönüştürülmüş olur . dtype=nt  eklenmedğ
takdrde değerler 0/1 yerne True/False bçmne dönüştürmektedr . Ardından pd.concat()  fonksyonu le
durum ntelğnn 0 ve 1’lerden oluşan 398 satır 3 sütunluk matrs formu durum_s2  ver setne ( verSet )
eklenmştr (Şekl 73). pd.concat() fonksyonundak axs=1  kullanımı, eklemenn sütun bazında olduğunu
söylemektedr . 0 se satır brleştrmes çn kullanılır .


Şekl 73: durum ntelğnn sayısal değerler le fade edlmes- 2.
Bu şlem sonrasında elde edlen tüm ntelklern kullanılması doğru olmaz. durum  ntelğ yerne ya
durum_s1  kullanılablr , ya da Düşük, Orta ve Yüksek kategorlerne at ntelklerden seçlecek olan k
tanes kullanılablr (br örneğn yalnızca kategorlerden brne at olduğu varsayılmıştır).
Pandas  kütüphanes dışında benzer şlemler Sckt-learn  kütüphanesnde preprocessng  modülündek
LabelEncoder  ve OneHotEncoder  fonksyonlarıyla da gerçekleştrleblr . Bunun çn bknz.


## 4.9. Ver Normalzasyonu

Ver setnde yer alan nümerk ntelklern brbrnden çok ayrı aralıklarda seyretmes durumunda bu
değerlern özellkle uzaklık ya da benzerlk tabanlı yapılan analzler domne edeceğ ve nümerk ntelklern
normalzasyon yöntemler Bölüm 2.4.6’da açıklanmıştır .
Bu bölümde auto-mpg  ver setndek nümerk ntelklern normalzasyonuna lşkn k örnek verlmştr .
Aşağıda Python kodu verlen lk örnekte ver setndek nümerk ntelkler (lk 7 sütun) mn-maks
normalzasyon yöntem le 0-1 aralığında normalze edlmştr . Bunun çn öncelkle Sckt-learn
kütüphanesnde preprocessng  modülünden MnMaxScaler  fonksyonu çağrılmıştır . Ardından normalze
edlecek ntelkler ver smnde br DataFrame nesnesne atanmıştır . MnMaxScaler ’e at scaler  adında br
örnek oluşturulmuştur . Önce ft() sonra da transform()  fonksyonları yardımı le normalzasyon şlem
gerçekleştrlmştr . En son satırda bu normalze ver set ( n_verSet ) sütun adları ver DataFrame’n sütun
adları olacak şeklde DataFrame ’e dönüştürülmüştür . Şekl 74 ncelendğnde tüm ntelklern en büyük
değernn 1, en küçük değernn 0 olduğu görülecektr .


Şekl 74: Mn-maks normalzasyon yöntem uygulandıktan sonra ver setnden br ekran görüntüsü.
Aşağıda Python kodu verlen knc örnekte nümerk değer çeren lk 7 sütuna standardzasyon olarak blnen
z-Scor e yöntem uygulanmıştır . Bunun çn öncelkle Sckt-learn  kütüphanesnde preprocessng  modülünden
StandardScaler  çağrılmıştır . Ardından normalze edlecek ntelkler ver smnde br DataFrame nesnesne
atanmıştır . StandardScaler ’e at scaler  adında br örnek oluşturulmuştur . Bu kez doğrudan ft_transform()
foksyonu yardımı le standardzasyon şlem gerçekleştrlmştr . En son satırda bu normalze ver set
(n_verSet ) sütun adları ver DataFrame’n sütun adları olacak şeklde DataFrame ’e dönüştürülmüştür


Şekl 75: Standardzasyon yöntem uygulandıktan sonra ver setnden br ekran görüntüsü.
Burada unutulmamalıdır k; her k örnek çn de ya ft() ve transform()  gb k fonksyon ya da
ft_transform()  gb tek br fonksyon le şlem gerçekleştrmek mümkündür . Analzlerde normalze edlmş
ver setnn kullanılacağı unutulmamalıdır .

**Bölüm Özet**

Bu bölümde Python le makne öğrenmes sürecnde sıkça faydalanılan bazı ver ön-şleme  (data pr e-
processng ) teknkler arabalara at çeştl ntelklern yer aldığı br ver set üzernde ele alınmıştır . Öncelkle
ver tp dönüşümler ve eksk vernn uygun şeklde tamamlanması ( mssng data mputaton ) çn kullanılan
Python fonksyonları hakkında blgler verlmştr . Sayısal br ntelğ kategork halde kullanablmeye mkân
tanıyan ver ayrıklaştırmanın ( data dscr etzaton ) temel prenspler ve Python uygulamalarına yer verlmştr .
Ver özetleme ve gruplama konuları örneklerle açıklanmıştır . Ver setnde tekrar eden gözlemler ( duplcates )
bulma ve aykırı değer tespt ( outler detecton ) uygulamaları yapılmıştır . Br ver setnden rastgele örneklem
alablme üzerne çeştl örnekler sunulmuştur . Ayrıca kategork değşkenler sayısal değerlere dönüştürmek
çn kullanılan yapay ( dummy ) kodlama teknkler ve son olarak farklı ölçeklerdek verlerle başa çıkmak çn
ver normalzasyonu ( data normalzaton ) konuları örneklenmştr .


**Bölüm Özet**

Ver setnn özet değerlern görmek çn descrbe()  fonksyonu kullanılablr . Aşağıdak kodlar yardımı le
elde edlen ekran görüntüsü Şekl 59’da verlmştr . descrbe()  fonksyonunun çıktısı dkkatle ncelenrse
nümerk ntelkler çn;
• kaç adet örnek olduğu ( count ),
• ortalama ( mean ),
• standart sapma ( std),


• kartl ( 25% ),
• kartl/ortanca değer ( 50%  ya da medan),
• kartl ( 75% ) ve
• maksmum değer ( max)
verlmştr . Kategork ntelkler çn se;
• kaç adet örnek çerdğ ( count ),
• kaç kategorye sahp olduğu ( unque ),
• en yüksek frekansa sahp olan kategornn adı ( top),
• ver setnde o kategorye sahp kaç örnek olduğu ( freq)
blgler verlmştr . Bu blglerden faydalanılarak ntelklerdek olası bazı hatalar tespt edleblecektr .


Şekl 59:  Ver set özet.
Ver özet ncelemes tamamlandıktan sonra ver setnde farklı ntelkler kullanılarak gruplandırma
(aggregaton ) şlem gerçekleştrleblr . Ktabın ver görselleştrme bölümünde sütun ve pasta grafğ


döndürdüğü sonuçlar aynıdır . Yan mpg  ntelğnn durum kategorsne göre ortalaması alınırsa “Düşük”
kategorsndeklern ortalaması 17.26, “Orta” kategorsndeklern 26.34, “Yüksek” kategorsndeklern
ortalaması se 34.63’ tür. Fark se döndürdükler ver tplerdr . A değşken DataFrame  ken B değşken
Seres  nesnesdr (Şekl 60).


Şekl 60: A ve B nesnesn çeren ekran görüntüsü.
Ortalama alma dışında kategorlere göre toplam, frekans, en küçük değer , en büyük değer , standart sapma
gb değerler de aşağıdak kodlar yardımı le bulunablr . En son satırdak descrbe()  fonksyonuna lşkn
ekran görüntüsü Şekl 61’de verlmştr .


Şekl 61:  Gruplandırmada descrbe() le elde edlen ekran görüntüsü.


**Kaynakça**

geeksfor geeks.or g. (2019). One Hot Encodng n Machne Learnng. GeeksforGeeks .
https://www .geeksfor geeks.or g/ml-one-hot-encodng-of-datasets-n-python/
geeksfor geeks.or g. (2021). Detect and Remove the Outlers usng Python. GeeksforGeeks .
https://www .geeksfor geeks.or g/detect-and-remove-the-outlers-usng-python/
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Qunlan, R. (1993). Auto MPG  [dataset]. UCI Machne Learnng Repostory .
https://do.or g/10.24432/C5859H
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021


**Ünte Soruları**

Soru-1 :
15.000, 10.000, 20.000 sürekl değerlernn bulunduğu maaş ntelğnde eksk değerlern de olduğu tespt
edlmştr . Aşağıda verlen seçeneklerden hangs maaş ntelğnde yer alan eksk değerlern
tamamlanablmes ( mssng data mputaton ) çn en uygun yöntem olacaktır?
(Çoktan Seçmel)
(A) Eksk değerler yerne ntelğn en büyük değern atamak.
(B) Eksk değerler yerne ntelğn en küçük değern atamak.
(C) Eksk değerler yerne en sık görülen maaş değern atamak.
(D) Eksk değerler yerne ntelğn ortalamasını atamak.
Eksk değerler yerne sıfır (“0”) atamak.
Cevap-1 :
Eksk değerler yerne ntelğn ortalamasını atamak.


Aşağıdak fonksyonlardan hangs ver ayrıklaştırma ( data dscr etzaton ) çn kullanılablr?
(Çoktan Seçmel)
(A) qcut()
(B) slced()
(C) parted()
(D) dvded()
dscretzed()
Cevap-2 :
qcut()
Soru-3 :
Tekrar eden gözlemler ver setnden çıkarmak çn aşağıdak fonksyonlardan hangs kullanılablr?
(Çoktan Seçmel)
(A) duplcates()
(B) drop_duplcates()
(C) del_duplcates()
(D) rem_duplcates()
clr_duplcates()
Cevap-3 :
drop_duplcates()
Soru-4 :
Aşağıdak seçeneklern hangsnde random.seed()  fonksyonu hatalı kullanılmıştır?
(Çoktan Seçmel)
(A) random.seed(1)
(B) random.seed(123)
(C) random.seed(123456)
(D) random.seed(1000)
(E) random.seed(random)
Cevap-4 :


Soru-5 :
Br öğrenc ver set ( ogrenc) DataFrame olarak tanımlanmıştır . Öğrenclern okulu borakıp bırakmama
durumlarına (Evet/Hayır) lşkn kategork ntelk ( ogrDurum ) analzlerde hedef ntelk olarak
kullanılacaktır . Ayrıca, tabakalı kl ayırma  (stratfed hold-out ) yöntem le eğtm ve test ver setlernde,
ogrDurum  ntelğnn kategorler arasındak oranın korunması stenmektedr . Bu blgler ışığında, vernn
Aşağıdak seçeneklern hangsnde ogrenc ver set %80 eğtm ( egtm ), %20 test ( test) ver set olacak
şeklde tabakalı kl ayırma ( stratfed hold-out ) yöntem le doğru br bçmde oluşturulmuştur?
(Çoktan Seçmel)
(A)
(B)
(C)
(D)
Cevap-5 :
Soru-6 :
Br yarışmanın jür puanlarının yer aldığı ver setnde çok kötü, kötü, orta, y, çok y  gb değerlendrmelern
bulunduğu nomnal kategork br sonuc  ntelğ bulunmaktadır . Bu ntelğn kategorlernn 0, 1, 2, 3, 4 gb
sayısal hale dönüştürüleblmes çn aşağıdaklerden hangs kullanılablr?
(Çoktan Seçmel)
(A) ver["sonuc"].tont


(C) ver["sonuc"].pd.get_dummes
(D) sonuc["ver"].cat.codes
sonuc["ver"].pd.get_dummes
Cevap-6 :
ver["sonuc"].cat.codes
Soru-7 :
Aşağıdak kod satırı ne amaçla kullanılır?
(Çoktan Seçmel)
(A) Ver ayrıklaştırma
(B) Ver gruplama
(C) Ver normalzasyonu
(D) Ver tamamlama
Ver özetleme
Cevap-7 :
Ver normalzasyonu
Soru-8 :
Araç renklernn ( renk) ve fyatlarının ( fyat ) yer aldığı br ver setnde araba renklerne göre ortalama araç
fyatları bulunmak stenyor . Buna göre aşağıda son tarafı boş bırakılan Python kod satırı aşağıdak
seçeneklerden hangs le uygun bçmde tamamlanır?
(Çoktan Seçmel)
(A) groupby("renk").sum()
(B) verSet("renk").mean()
(C) groupby("renk").mean()
(D) groupby("renk").count()
("renk").mean()
Cevap-8 :


Soru-9 :
Br ver setnde, eksk verler ( mssng data ) analzler çn aşağıda verlen seçeneklerden hangs le daha
uygun şeklde temsl edleblr?
(Çoktan Seçmel)
(A) np.nan
(B) 0
(C) -
(D) "mssng data"
"eksk ver"
Cevap-9 :
np.nan
Soru-10 :
Br Pandas  DataFrame  olarak saklanan arşv ( arsv ) ver setnn özetnn alınablmes çn aşağıdak
fonksyonlardan hangs kullanılablr?
(Çoktan Seçmel)
(A) arsv .summary()
(B) arsv .get()
(C) arsv .prnt()
(D) arsv .descrbe()
arsv .output()
Cevap-10 :


# 5. K-Ortalamalar Algoritması


**Özlü Söz**

Hepmzn yapması gereken yapay zekâyı nsanlığın zararına değl, nsanlığın yararına olacak şeklde
kullandığımızdan emn olmaktır .
Tm Cook , Apple


**Kazanımlar**

1.   Danışmansız öğrenme ( unsupervsed learnng ) kavramını, temel çalışma prensbn ve uygulama
alanlarını blr .
2.   Kümeleme analz ( clusterng analyss ) kavramını blr .
3.   k-Ortalamalar ( k-Means ) algortmasının çalışma prensplern kavrar .
4.   k-Ortalamalar algortmasını uygulayablr , elde edlen sonuçları yorumlayablr ve deal küme sayısını
belrlemek çn kullanılan yöntemler blr .
5.   Python programlama dln kullanarak gerçek dünya ver set üzernde k-Ortalamalar algortmasını
uygulayablr , kümeleme performansını değerlendreblr ve elde edlen analz sonuçlarını yorumlayablr .


**Brlkte Düşünelm**

1.   Danışmansız öğrenme ( unsupervsed learnng ) nedr? Hang durumlarda kullanılableceğ hakkında
örnekler vereblr msnz?
2.   Kümeleme analz ( clusterng analyss ) nedr? Hang durumlarda kümeleme analz kullanmak
mantıklıdır?
3.   k-Ortalamalar ( k-Means ) algortmasının adımları nelerdr?
4.   İdeal küme sayısını belrlemek çn kullanılan yöntemler açıklayarak, bu yöntemlern avantajlarını ve
dezavantajlarını sıralayablr msnz?
5.   Python programlama dln kullanılarak k-Ortalamalar algortması br ver setne nasıl uygulanablr?
6.   Kümeleme performansını değerlendrmek çn hang metrkler kullanılablr? Bu metrkler nasıl


**Başlamadan Önce**

Danışmansız öğr enme  (unsupervsed learnng ), ver setlerndek desenler ve yapıları anlamak, öğrenmek ve
tanımlamak çn kullanılan br konsepttr . Kümeleme analz  (clusterng analyss ), ver setnde benzer
özellklere sahp olan gözlemler gruplayarak ver çndek çeştl yapıları ortaya çıkarmayı amaçlayan br
teknktr . Bu bölümde danışmansız öğrenme ve kümeleme analz kavramlarına lşkn temel blgler kısa br
grşle okuyuculara sunulacaktır .
Bu bölümün ana odağında kümeleme algortmalarından br olan k-Ortalamalar  algortması  (k-means
algorthm ) yer almaktadır . Python programlama dln kullanarak gerçek br ver set üzernde k-Ortalamalar
algortmasının nasıl uygulanacağı adım adım açıklanmaktadır . Bu bölümdek Python uygulaması
çerçevesnde ver ön-şleme bölümünde olduğu gb Python'da makne öğrenmes çalışmalarında terch edlen
Sckt-learn  kütüphanesnden faydalanılmıştır . Ver görselleştrme çn Seaborn  ve Matplotlb
kütüphanelernn yanı sıra özellkle kümeleme analz sonuçlarının görselleştrlmes çn yellowbrck
kütüphanes kullanılmıştır .
Bölümdek uygulamada Sckt-learn  kütüphanesnn datasets  modülünde yer alan Irs ççeğ ver set
kullanılmıştır . Bu ver set ayrıca UCI Makne Öğrenmes Ver Deposu’nda ( UCI Machne Learnng
Repostory ) da bulunmaktadır . Irs ver set hem sınıflandırma hem de kümeleme çalışmalarında kullanılablr
fakat bu bölümde kümeleme amacıyla kullanılmıştır . Bu bölümde k-Ortalamalar algortmasının teors ve
uygulaması brlkte verlecektr . Okuyuculara k-Ortalamalar algortmasını pratk olarak pekştreblmeler çn
farklı ver setler üzernde de çalışmaları tavsye edlmektedr .


## 5.1. Danışmansız Öğr enme

Danışmansız öğrenme ( unsupervsed learnng ), ktabın brnc bölümünde de fade edldğ gb sınıf
etketlerne br dğer fadeyle önceden tanımlanmış br hedef ntelğe htyaç duymadan verdek kalıpları,
örüntüler, grupları veya lşkler keşfetmey ve ortaya çıkartmayı amaçlar .
Danışmansız öğrenme yöntemnde ver setnde sadece tahmn sağlayan ntelkler (bağımsız değşkenler)
kullanılır . Danışmansız öğrenme algortmaları ver setndek örneklern brbrne yakınlığı, uzaklığı veya
benzerlğ gb vernn doğasında olan özellklerden ve karakterstklerden faydalanarak öğrenmeye odaklanır .
Danışmansız öğrenmenn kullanıldığı farklı uygulama alanları vardır (Şekl 76). Bunlardan br tanes ve bu
bölümde de Python programlama dl le uygulaması yapılan kümeleme  (clusterng ) problemdr . Kümeleme
algortmaları, ver noktalarını benzerlklerne veya yakınlıklarına (ya da uzaklıklarına) göre gruplandırmayı
amaçlar . Kümeleme algortmalarına; k-Ortalamalar algortması ( k-Means algorthm ), bulanık c-Ortalamalar
(fuzzy c-means ), k-medods, DBSCAN ( Densty-Based Spatal Clusterng of Applcatons wth Nose ),
OPTICS ( Orderng Ponts to Identfy the Clusterng Structur e) BIRCH ( Balance Iteratve Reducng and
Clusterng usng Herar ches ) örnek olarak verleblr (Özen & Kartal, 2023). Danışmansız öğrenme


Şekl 76: Danışmansız öğrenmenn kullanıldığı bazı alanlar .
Boyut Azaltma/İndrgeme:  Boyut azaltma/ndr geme yöntemnde vernn temel yapısı korunurken grd
ntelklernn sayısı azaltılır . Bu yöntem yüksek boyutlu verlern görselleştrlmes, gürültünün veya
fazlalığın ortadan kaldırılması ve sonrak analzlern bastleştrlmes çn kullanılır . Temel Bleşen Analz -
TBA  (Prncpal Component Analyss- PCA ) yaygın olarak kullanılan br boyut azaltma algortmasıdır .
Kümeleme analzler sonucunda elde edlen kümelern görsel açıdan ncelenmes ve yorumlanmasında
TBA ’dan faydalanılmaktadır .
Anormallk Tespt : Anormallk tespt ( anomaly detecton ) algortmaları, verdek olağandışı veya anormal
kalıpların tanımlanmasını sağlar . Anormallk tesptne verlecek en blndk örneklerden br e-postalar arasına
karışan stenmeyen e-postalardır ( spam  mal). Br dğer örnek olarak bankacılık sektöründek dolandırıcılık
tespt ( fraud detecton ) verleblr . Kşlern kred kartı le gerçekleştrdğ şlemlerde alış-verş çn terch
ettğ şletmeler ve web steler, harcama ve satın alma alışkanlıkları gb belrl br ör gü mevcuttur .
Anormallk tespt algortmaları bu kalıbın dışına çıkan dolandırıcı/sahte şlemlern tespt amacıyla
kullanılmaktadır . Örneğn daha önce yurtdışında hç şlem yapılmayan kred kartı le Amerka Brleşk
Devletler’nden yapılan br alış-verşn dolandırıcılık olup olmadığının tespt edlmes çn bu yöntemle
çalışan algortmalar kullanılır . Bu algortmalar normalden ya da olağandan öneml ölçüde farklı olan ver
noktalarını veya örnekler tanımlamayı amaçlarlar . Ayrıca anormallk tespt ver ön-şleme bölümünde
bahsedlen aykırı değerlern tespt çn de farklı br yol sunar . Tek-Sınıf Destek Vektör Makneler ( One-
Class Support V ector Machnes ) ve otomatk kodlayıcılar ( autoencoders ) anormallk tespt çn popüler
yöntemler arasındadır .
Brlktelk Kuralları:  Brlktelk kuralı madenclğ ( assocaton rule mnng ) olarak da blnen bu yöntem,
ver setndek ntelkler arasındak lgnç lşk ( relatons ) veya brlktelklern ( assocatons ) keşfedlmesn
sağlar . Tavsye ( recommendaton ) sstemlernn gelştrlmesnde brlktelk kuralları algortmaları
kullanılmaktadır . Gündelk hayatta e-tcaret stelernde karşımıza çıkan “ A ürününü alan B ve C’y de aldı.
Sz de satın almayı düşünür müsünüz? ” ya da “X ve Y ürününü alana Z ürünü hedye!” ya da müzk dnleme,
flm zleme platformlarında “ Szn çn seçtğmz şarkılar/flmler… ” gb tavsyeler çn çoğunlukla
brlktelk kuralları analzler kullanılmaktadır . Ver setnde sık görülen öge kümelern ( frequent temsets )
veya kalıplarını tanımlamaya ve kurallar oluşturmaya yardımcı olur . Apror ve Eclat yaygın olarak kullanılan
brlktelk kuralı algortmalarına örnek verleblr .

## 5.2. Kümeleme Analz

Danışmanlı öğrenmede sınıf etketlern çeren hedef ntelğe sahp ver set kullanılırken, kümeleme
analzlernn yapıldığı ver setnde herhang br sınıf değer (hedef ntelk) olmaz (Han & Kamber , 2006).
Brbrne daha çok benzeyen örnekler aynı kümede olacak bçmde ver setndek tüm örnekler gruplandırılır .
Örneğn br perakende şrket, müşterlern harcama alışkanlıklarına göre gruplara/segmentlere ayırmak
stesn. Harcama mktarı, alışverş sıklığı ve alışverş yapılan kategorlere göre müşterler farklı kümelere
ayrılablr . Kümeleme analzler sonucunda; düşük, orta ve yüksek harcama grupları oluşturulablr ve
böylelkle her küme çn özel pazarlama stratejler ve hzmetler belrleneblr . Br başka örnekte br


gelştreceğ düşünülsün. Bunun çn analzlerde hastaların gösterdğ semptomlarla lgl ver kullanılacaktır .
Kümeleme algortmaları le hastalar gösterdğ semptomlara göre kümelere ayrılır . Böylelkle her küme çn
özel tedav stratejler ve takp planları belrleneblr .
Şekl 77’de küresel COVID-19 salgınının dünyada ve Türkye'dek değşen durumuna bağlı olarak ülkelern
kümeleme analz sonuçları görüleblr (Kartal vd., 2021). Analz kapsamında doğrusal değşm oranı, üstel
büyüme katsayısı ve vak’a sayısının kye katlanması çn gereken gün sayısı gb yen değşkenler
hesaplanmış ve yen değşkenlerle güçlendrlen ver set k-Ortalamalar Algortmasına uygulanarak ülkeler
gruplandırılmıştır . Bu maksatla COVID-19'u verye dayalı olarak tanımlamak çn çevrmç br R-Shny
uygulaması gelştrlmştr . Uygulamaya şu adresten erşleblr: https://elfkartal.shnyapps.o/covd19/ .
Shny le R ya da Python programlama dllern kullanarak farklı uygulamalar oluşturablrsnz (detaylar çn
bknz. https://shny .post.co/ ).


Şekl 77: Ülkelern COVID-19 pandemsne lşkn ver kullanılarak kümelenmes.
Kümeleme analzler; müşter segmentasyonu, gruplandırma, görüntü sıkıştırma, belgelern tasnflenmes ve
anormallk tespt gb problemlern çözümünde de kullanılmaktadır .

## 5.3. k-Ortalamalar  Algortması

k-Ortalamalar algortması ( k-means algorthm ),  
   adet ver noktasını 

 farklı kümeye bölmey amaçlar; burada her ver noktası, kendsne en yakın küme merkezne sahp kümeye
atanır . Br küme merkez  (centr od), lgl kümede bulunan gözlemlern ortalaması olarak tanımlanablr . k-
Ortalamalar algortmasının adımlarına aşağıda yer verlmştr (Shmuel vd., 2018):
1.  

 küme sayısı seçlr . Eğer ver setndek gruplara lşkn ön blg varsa, bu blg oldukça yardımcı olacaktır;
ancak böyle br blg yoksa br başlangıç küme sayısı seçlerek analzlere başlanır .
2. Bu adımda her gözlem kendsne “en yakın” küme merkezne sahp kümeye atanır . Noktalar arasındak
mesafey ölçmek çn genellkle Eucldean uzaklık fonksyonu başta olmak üzere çeştl uzaklık fonksyonları


3. Yen eleman(lar) kazanan ve mevcut eleman(lar)ını kaybeden kümelern merkezler yenden hesaplanır ve
Adım 2'ye dönülür .
4. Küme merkezler Adım 2 ve Adım 3 le yapılan terasyonlar (tekrarlar ya da ynelemeler) sonrasında artık
değşmedğnde veya önceden belrlenen maksmum terasyon sayısına ulaşıldığında sonlandırılır . Bu durum
yakınsama  (conver gence ) olarak da blnmektedr . Algortma yakınsadığında son merkezler küme
merkezlern temsl eder ve her ver noktası ya da gözlem değer kendne en yakın merkeze sahp kümeye
atanmış olur .
k-Ortalamalar algortmasının çalışma prensbn daha y anlamak çn şu bağlantı zyaret edleblr (N.
Harrs, 2014): https://www .naftalharrs.com/blog/vsualzng-k-means-clusterng/ . Örneğn gözlemler k
boyutlu uzayda Şekl 78’dek lk grafkte (I) olduğu gb verlsn ve bu ver setndek gözlemler k-
Ortalamalar algortması yardımı le 3 kümeye ayrılmak stensn. Başlangıçta II numaralı şekldek gb
rastgele 3 farklı küme merkez seçlsn. III numaralı grafkte olduğu gb her br gözlem kendsne en yakın
küme merkezne atanacaktır . Eğer küme merkezler güncellenrse görülecektr k bazı kümelere yen
gözlemler grerken bazı kümeler gözlemlern kaybedecektr (bknz. IV). V numaralı grafkte verldğ gb
gözlemlern kümelere yenden atanması tamamlandığında küme merkezler de güncellenecektr (bknz. VI).
Benzer şeklde artık kümeler arasından gözlemler yer değştrmeynceye kadar (ya da maksmum terasyon


Şekl 78:  k-Ortalamalar algortması le kümeleme.
Şekl 78’dek örnekte başlangıç küme merkezler rastgele  seçlmştr . Bunun yanı sıra br başka yöntem
olarak, başlangıçta küme merkezler rastgele seçleblr ve sonrak j. terasyonda br öncek merkeze en fazla
en yakın ver noktası da seçleblr ( farhest heurstc ) (N. Harrs, 2014). Ayrıca, k-means++  yöntem j.nc
küme merkezn, kendsnden öncek en yakın merkeze olan mesafenn karesyle orantılı br olasılığa dayalı
bçmde seçmektedr .


İdeal küme sayısı, en genel anlamda ver setndek örneklern küme ç ve küme dışındak uzaklıklarına ve
benzerlklerne göre belrleneblr . En uygun küme sayısının bulunablmes ya da kümeleme performansının
değerlendrleblmes çn teork açıklamaları ktabın 2.7.5 numaralı bölümünde verlen ve aşağıda kısaca
sayılan yöntemler kullanılablr:
• Uzmanlık blgsnn kullanılması.
• Drsek ( elbow ) yöntem: Küme ç Kareler Toplamı ( Wthn Cluster Sum of Squar es- WSS ) (her küme çn
aynı kümede bulunan gözlemlern küme merkezne olan uzaklıklarının kareler toplamı kullanılarak).
• Slhouette katsayısının hesaplanması.

## 5.5. Python Uygulaması

Bu çalışmada Irs ççeğ le lgl ntelklern yer aldığı Irs ver set kullanılmıştır . Ver setnde 4 adet tahmn
sağlayan ntelk ve tablonun sonunda gr renkle vur gulanmış olan 1 adet hedef ntelk bulunmaktadır . Ver set
150 örnekten oluşmaktadır . Irs ççeğnn çanak ve taç yaprak uzunluk ve genşlkler le örneğn hang sınıfa
at olduğu blgs ( setosa, verscolor , vrgnca ) verlmştr . Ancak bu çalışmada danışmansız öğrenen k-
Ortalamalar makne öğrenmes algortması kullanılacağından bu sınıf ntelğne htyaç duyulmayacaktır .
Ntelklere lşkn blgler Tablo 18’de verlmştr .
Tablo 18: Irs ver set.


### 5.5.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas, Sckt-learn, Seaborn, Matplotlb  ve yellowbrck  kütüphaneler kullanılmıştır
(Bengfort vd., 2018; C. R. Harrs vd., 2020; Hunter , 2007; McKnney , 2010; Pedregosa vd., 201 1; Waskom,
2021). Eğer bu kütüphaneler yüklü değlse Bölüm 3.1’de açıklandığı gb termnalden kurulmalıdır . Kurulma
şlem yapılmışsa öncelkle aşağıdak kod satırları Python koduna dahl edlmeldr .


### 5.5.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . Sckt-learn  kütüphanesnde bulunan
datasets  modülünde makne öğrenmes çalışmalarında sıklıkla kullanılan ver setler yer almaktadır .
Aşağıdak kod satırı le ver set kolaylıkla okunablr . Veya Irs ver setne UCI Makne Öğrenmes Ver
Deposu’ndan ( UCI Machne Learnng Repostory ) da ulaşılablr (Fsher , 1936):
https://archve.cs.uc.edu/dataset/53/rs


Ktabın öncek bölümlernde bahsedldğ gb Python’dak uygulamalarda tahmn sağlayan ntelkler X,
hedef ntelk se y değşkenlernde tutulmaktadır . Bu nedenle rs.data  X’değşkenne, rs.target  se y
değşkenne atanmıştır . rs.featur e_names  sütun adlarını, rs.target_names  se hedef ntelğn kategor
adlarını döndürmektedr . X ve y brer dzdr (array).


Aşağıda df adında br Pandas  DataFrame tanımlanmıştır . Burada ver setndek ntelklern tamamı (tahmn
sağlayan+hedef ntelk) br arada tutulacaktır . Bunun çn öncelkle X dzs sütun adları da eklenerek br
df DataFrame olarak tanımlanmıştır . Ardından df’nn son sütunu olarak hedef ntelk ( tur) eklenmştr . tur
ntelğnn kategorler varsayılan olarak 0, 1, 2 olarak gelmektedr . Bunların yerne sırasıyla
lst(rs.target_names))  kodu le dönen kategor adları ver tp “ category ” olacak şeklde df’ye atanmıştır .


### 5.5.3. Ver Ön-şleme

Ntelklern brbrler arasındak Pearson korelasyon katsayıları np.corr coef()  komutu le elde edlmştr


Şekl 79: Ver setnde ntelkler arasındak korelasyonun ncelenmes.
Şekl 79’dan hareketle, canakU  ve canakG  değşkenlernn brbrler arasında hesaplanan Pearson
korelasyon katsayısı -0.12’dr . Yan brbrler arasında ters yönde zayıf br lşkden bahsedleblr . Dğer
yandan tacU  ve tacG  ntelkler arasında se poztf yönde güçlü br lşkden bahsedleblr (Pearson
korelasyon katsayısı = 0.96). Sırasıyla zayıf ve güçlü doğrusal lşklern görülebleceğ grafkler aşağıdak
kod satırları le elde edlmştr (Şekl 80). Grafkler , setosa  sınıfına at örneklern verscolor  ve vrgnca
sınıfına at örneklerden daha belr gn bçmde ayrılmış olduğunu göstermektedr .


### 5.5.4. Modelleme

Bu bölümde k-Ortalamalar algortması KMeans()  fonksyonu le ver setne uygulanmıştır . Ver set 3 farklı
kümeye ayrılmak stenmştr . Bu nedenle kumeSays  3 olarak belrlenmştr . k-Ortalamalar algortması
çnde hedef ntelk olmayan ve yalnızca tahmn sağlayan ntelkler barındıran X sml değşken le
çalıştırılacaktır . KMeans()  fonksyonunun parametreler aşağıda sırasıyla açıklanmıştır:
• n_clusters:  Küme sayısı.
• nt: Başlangıç küme merkezlernn atanmasında kullanılacak yöntem (varsayılan değer auto).
• n_nt:  k-Ortalamalar algortmasının farklı küme merkez değerler le çalıştırılma sayısıdır . Nha sonuçlar ,
nerta  açısından n_nt  adet ardışık çalıştırmanın en y çıktısıdır .
• random_state:  Küme merkeznn lk belrlenme aşaması çn rastgele sayı üretmn belrler .
kOrtModel  oluşturulduktan sonra bu modele at ft_pr edct()  fonksyonu X ver setne uygulanmıştır .
ft_pr edct()  fonksyonu gerye 150 gözlemn sırasıyla atandığı küme numarasını döndürmektedr . Aynı
blgye kOrtModel.labels_  kullanılarak da ulaşılablr . Modeln kurulduğu Python kodu ve modeln çıktısı
aşağıda verlmştr .


Modeln çıktısından da görüleceğ üzere ver setndek lk örnek 1 nolu, son örnek 0 nolu kümeye, sondan br
öncek örnek se 2 nolu kümeye atamıştır . Unutulmamalıdır  k; model çıktısındak 0, 1 ve 2 olarak sunulan
küme numaralarının setosa , verscolor  ve vrgnca  kategorlernden hangsn temsl ettğ blnemez . k-
Ortalamalar yalnızca örnekler kümelere atar; ancak kümelern etketn vermez. Analz yapan uzmanın
mutlaka lgl kümelerdek örnekler nceleyerek adlandırma yapması gerekr .
Model çıktısının verdğ örneklern küme numaraları df değşkennn son sütununa ver tp “ category ”


Elde edlen sonuçlara göre ver setnde bulunan 61 örnek 0 nolu kümeye, 50 örnek 1 nolu kümeye, 39 örnek
se 2 nolu kümeye atanmıştır . setosa , verscolor  ve vrgnca  sınıflarından 50’şer adet örnek olduğu
düşünülürse bazı kümelern hatalı belrlenmş olduğu görüleblr .


Elde edlen üç kümenn küme merkezler se kOrtModel.cluster_centers_  le elde edlmektedr
(kümeMerkezler ). Ver 4 boyutlu olduğundan (4 adet ntelk mevcuttur), küme merkezler de 4 boyutlu
bçmde lstelenmştr .


Aşağıda verlen kodlar yardımı le çanak yaprak uzunluğu ve çanak yaprak genşlğ ntelkler kullanılarak k-
Ortalamalar algortması le elde edlen kümeler ve küme merkezler elde edlmştr (Şekl 81).


X[kOrtModel.labels_==0, 0]  kodu X ver setndek 0 nolu kümeye at örneklern çanak yaprak uzunluğunu
(0. ndekste bulunan sütunu) döndürür . plt.scatter()  fonksyonunda ver noktalarının renkler c


Şekl 81: Kümeler ve küme merkezler.
Aşağıdak kod satırları le çanak yaprak uzunluğu ( canakU ) ve taç yaprak uzunluğu ( tacU ) ntelklerne göre,
sırasıyla örneklern at olduğu gerçek kategorler le k-Ortalamalar algortması le elde edlen kümeler
gösterlmştr (Şekl 82). Tek grafk alanında k grafğn gösterlmes çn grafk alanı 1x2 bçmnde
yapılandırılmıştır . sns.set()  çnde elde edlecek grafk büyüklüğü tanımlanmıştır . Verlen her k
sns.scatterplot()  fonksyonunda ax=axes[0]  ve ax=axes[1]  grafklern pozsyonunu belrlemektedr .


Şekl 82 ncelendğnde kabaca 0 nolu kümenn  verscolor , 1 nolu kümenn setosa  ve 2 nolu kümenn
vrgnca  sınıfına daha yakın olduğu görüleblr . Yne de böyle br çıkarım çn yalnızca k ntelk le
değerlendrme yapmak yeterl gelmez. Bu nedenle TBA  gb boyut ndr geme teknklernden faydalanarak
ver görselleştrmes yapmak ya da elde edlen kümelern uzmanlık blgs le ncelenmes ve sonrasında


Şekl 82: Gerçek sınıf değerler ve kümeleme sonucu elde edlen kümeler .

### 5.5.5. Performans Değerlendrme

Küme sayısı k=3 çn kümeleme performansının ortaya konması amacıyla WCSS ve Slhouette katsayısı
hesaplanmıştır . WCSS doğrudan modeln br özellğ olarak elde edlrken ( nerta_ ), Slhouette katsayısının
hesaplanablmes çn slhouette_scor e() fonksyonu kullanılmıştır . Bu fonksyonun aldığı lk parametre X
ver setdr . İknc parametre labels  elde edlen küme etketlerdr ( kOrtModel.labels_ ). Sonuncusu se
uzaklık hesaplama fonksyonu olan metrc  parametresdr ( eucldean ).


Aşağıdak kod bloğunda, SlhouetteVsualzer()  fonksyonu kullanılarak Şekl 83’dek grafk elde edlmştr .
Grafkte k=3 çn verlen Slhouette katsayısı 0.551’e göre (grafkte yer alan kırmızı dkey çzg) her kümede
yer alan örneklern Slhouette katsayıları nceleneblr . k=3 çn elde edlen kümelerdek örnek sayısı
hatırlanacak olursa, 0 nolu kümenn kırmızı (n=61), 1 nolu kümenn yeşl (n=50), 2 nolu kümenn se mav
(n=39) le gösterldğ sonucuna varılablr . Kırmızı le gösterlen 0 nolu kümede bazı örneklern negatf


verlen Slhouette katsayısının üzernde olan yeşl kümede yer alan örnekler , kırmızı ve mav le verlen
kümelere kıyasla daha fazladır .


Şekl 83: Üç kümeye lşkn Slhouette katsayılarının görselleştrlmes.

### 5.5.6. Kümeleme Kaltesnn Belrlenmes

Bu bölümde ele alınan ver setnde hedef ntelk (sınıf değer) mevcuttur . Irs ççekler setosa , verscolor  ve
vrgnca  türlernde 3 sınıfa ayrılmaktadır . Bu nedenle de kümeleme analzler sonucunda 3 kümeye ayırma
fkr lk akla gelen makul seçenektr; ancak gerçek hayatta kümeleme analzlernn gerçekleştrldğ ver
setlernde br hedef ntelk mevcut değldr . Dolayısıyla k-Ortalamalar algortması le çalışırken deal küme
sayısını belrlemek amacıyla k küme sayısı değştrlerek farklı modeller denemek ve modellern kümeleme
kaltesn WCSS ya da Slhouette katsayısı yardımı le kıyaslamak mümkündür .
Drsek Yöntem
Aşağıdak kod bloğunda X ver set kullanılarak k-Ortalamalar algortmasının deal küme sayısının
belrlenmes çn 2’den 20’ye kadar k değerleryle model kurulmuştur . Her br k küme sayısına at WCSS
değer ( kOrtModel.nerta_ ) wcss  dzsne eklenmştr .


Şekl 84:  Farklı küme sayıları çn hesaplanan WCSS değerler.
Şekl 84 ncelenrse, küme sayısının 2’den 3’e çıkması durumunda WCSS değernde belr gn br kırılım
(düşüş) gözlenmektedr . Bu nedenle küme sayısı  

 olarak seçleblr denr .
Slhouette Katsayısı Yöntem
İdeal küme sayısını bulmak çn drsek yöntemndeknn dışında Slhouette katsayısı da kullanılablr . Bu
yöntemde Slhouette katsayısı hesaplanarak slhs  lstesne atanmıştır . Küme sayısına göre hesaplanan


Şekl 85: Farklı küme sayıları çn hesaplanan Slhouette katsayıları.
Slhouette katsayısı çn deal durum olabldğnce 1’e yakın değerler elde edlmesdr . k=2’den k=20’ye
kadar elde edlen Slhouette katsayıları şu şekldedr: 0.681, 0.551, 0.498, 0.461, 0.336, 0.357, 0.36, 0.326,
0.326, 0.313, 0.316, 0.317, 0.302, 0.271, 0.268, 0.261, 0.265, 0.264, 0.265. Şekl 85’den de görülebleceğ
gb en yüksek Slhouette katsayısı k=2 çn (0.681), sonrasında da k=3 çn (0.551) elde edlmştr . Dolayısı
le küme sayısı k=2 ya da k=3 seçleblr .


**Bölüm Özet**

Bu bölüm danışmansız öğr enme (unsupervsed learnng ) alanında kümeleme analz ve k-ortalamalar  (k-
means ) algortması na odaklanmaktadır . İlk olarak danışmansız öğrenme konsept açıklanmış ve ardından
kümeleme kavramlarına değnlmştr . k-Ortalamalar algortması, ver setndek örnekler belrl br sayıda
kümeye ayırmak çn kullanılan etkl br yöntemdr . Algortmanın çalışma prenspler ve uygulama adımları
bu bölümde detaylı br şeklde ele alınmıştır . Ayrıca kümeleme problemlernde deal küme sayısını belrleme


Bölüm kapsamında k-Ortalamalar algortmasının Python le Irs ver set üzernde kümeleme uygulaması
gerçekleştrlmştr . İlk olarak ver set okunmuş ve htyaç duyulan ver ön-şleme teknkler uygulanmıştır .
Ardından k-Ortalamalar model oluşturulmuş ve elde edlen modeln performansı değerlendrlmştr . Son
olarak drsek  (elbow ) yöntem ve Slhouette katsayısı  kullanılarak kümeleme kaltes belrlenmştr . Bu
bölüm okuyuculara hem teork hem de pratk açıdan k-Ortalamalar algortmasını anlama ve kullanma
konusunda temel br deneym sunmaktadır . Bu kazanılan tecrübenn pekştrlmes çn okuyuculara farklı
ver setler le de pratk yapmaları  önerlmektedr .


**Kaynakça**

Bengfort, B., Blbro, R., Danelsen, N., Gray , L., McIntyre, K., Roman, P ., Poh, Z., & others. (2018).
Yellowbrck  (0.9.1) [Software]. https://do.or g/10.5281/zenodo.1206264
Fsher , R. A. (1936). Irs [dataset]. UCI Machne Learnng Repostory . https://do.or g/10.24432/C56C76
Han, J., & Kamber , M. (2006). Data Mnng: Concepts and T echnques  (2. bs). Mor gan Kaufmann
Publshers.
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
Harrs, N. (2014). Vsualzng K-Means Clusterng . https://www .naftalharrs.com/blog/vsualzng-k-means-
clusterng/
Hunter , J. D. (2007). Matplotlb: A 2D graphcs envronment. Computng n Scence & Engneerng , 9(3), 90-
95. https://do.or g/10.1 109/MCSE.2007.55
Kartal, E., Balaban, M. E., & Bayraktar , B. (2021). Küresel COVID-19 Salgınının Dünyada ve Türkye’de
Değşen Durumu ve Kümeleme Analz. İstanbul Tıp Fakültes Der gs, 84(1), 9-19.
https://do.or g/10.26650/IUITFD.2020.0077
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Özen, Z., & Kartal, E. (Ed.). (2023). Denetmsz Makne Öğr enmes Algortmaları: R ve Python
Uygulamaları  (1. bs). Nobel Akademk Yayıncılık.
Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Shmuel, G., Bruce, P . C., Yahav, I., Patel, N. R., & Lctendahl, K. C. (2018). Data Mnng for Busness
Analytcs  (1. bs). Wley .
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021


**Ünte Soruları**

Soru-1 :
Aşağıdaklerden hangs kümeleme algortmaları arasında yer almaz ?
(Çoktan Seçmel)
(A) k-Ortalamalar
(B) Bulanık c-Ortalamalar
(C) k-medods
(D) DBSCAN
(E) Apror
Cevap-1 :
Apror
Soru-2 :
Aşağıdaklerden hangs danışmansız öğrenme algortmalarının kullanıldığı br uygulama alanı değldr ?
(Çoktan Seçmel)
(A) Kümeleme
(B) Boyut Azaltma / İndr geme
(C) Sınıflandırma
(D) Anormallk tespt
Brlktelk kuralları madenclğ
Cevap-2 :
Sınıflandırma
Soru-3 :
Python uygulamasında kullanılan Irs ver set aşağıdak Python kütüphanelernn hangsnn çnde yer
almaktadır?
(Çoktan Seçmel)
(A) Sckt-learn
(B) random


(D) yellowbrck
Seaborn
Cevap-3 :
Sckt-learn
Soru-4 :
rs.target  komutu le aşağıdaklerden hangs elde edlr?
(Çoktan Seçmel)
(A) Irs ver setnn adı
(B) Irs ver setndek tüm ver noktaları
(C) Irs ver setnn hedef ntelğ
(D) Irs ver setnde yer alan aykırı değerler
Irs ver setnn sütun adları
Cevap-4 :
Irs ver setnn hedef ntelğ
Soru-5 :
Bölümdek uygulamada Irs ver setndek ntelkler arasındak Pearson korelasyon katsayıları hesaplanırken
aşağıdak kütüphanelerden hangs kullanılmıştır?
(Çoktan Seçmel)
(A) Sckt-learn
(B) random
(C) yellowbrck
(D) NumPy
Seaborn
Cevap-5 :
NumPy
Soru-6 :
Aşağıdak tabloda verlen Pearson korelasyon katsayısı matrsne göre, aşağıdak seçeneklerde verlen negatf
yönde en yüksek  güçlü lşk  hang kl arasında mevcuttur?
A B CD
A1 -0.50 0.820.90


C0.82 0.78 10.49
D0.90 -0.92 0.491
(Çoktan Seçmel)
(A) A-D
(B) A-B
(C) B-C
(D) D-B
D-C
Cevap-6 :
D-B
Soru-7 :
Aşağıdak seçeneklerden hangs Python’da k-Ortalamalar algortmasını uygulamak çn kullanılan br
fonksyondur?
(Çoktan Seçmel)
(A) k-means()
(B) KMeans()
(C) k-Means()
(D) kOrt()
k-Ort()
Cevap-7 :
KMeans()
Soru-8 :
kOrtModel  adlı br k-Ortalamalar Algortması model oluşturuluyor . Aşağıdak seçeneklerden hangs ver
setndek gözlemlern at olduğu kümelern görüntülenmesn sağlar?
(Çoktan Seçmel)
(A) kOrtModel.clusters
(B) kOrtModel.clusters_
(C) kOrtModel.lbls_
(D) kOrtModel.labels


Cevap-8 :
kOrtModel.labels_
Soru-9 :
Farklı küme sayıları (k) le gerçekleştrlen kümeleme analzler sonucunda elde edlen Slhouette katsayıları
aşağıdak tabloda verlyor . Tabloya göre deal küme sayısı  nedr?
kSlhouette Katsayısı
20.8
30.7
40.5
50.55
60.4
(Çoktan Seçmel)
(A) 2
(B) 3
(C) 4
(D) 5
6
Cevap-9 :
2
Soru-10 :
k-Ortalamalar algortması le lgl aşağıdaklerden hangs yanlıştır ?
(Çoktan Seçmel)
(A) Br kümeleme algortmasıdır .
(B) Küme sayısı (k) algortma çalıştırıldıktan sonra belrlenr .
(C) Br danışmansız öğrenme algortmasıdır .
(D) Küme merkezler başlangıçta rastgele bçmde atanablr .
En y küme sayısına Slhouette katsayısı yardımı le karar verleblr .
Cevap-10 :


# 6. Basit ve Çoklu Doğrusal Regresyon Analizi


**Özlü Söz**

Tahmn etmek zordur - özellkle de gelecek söz konusu olduğunda.
Mark Twan , yazar .


**Kazanımlar**

1.   Bast doğrusal regresyon ( smple lnear r egresson ) ve çoklu doğrusal regresyon ( multple lnear
regresson ) analzlernn temel prenspler ve teork çerçevesn blr .
2.   Bağımlı ve bağımsız değşken kavramlarını anlar .
3.   Regresyon analznn amacı ve nasıl kullanılacağı konusunda blg ednr .
4.   Br bağımlı değşkenn tek br bağımsız değşkenle lşksn modelleme yeteneğ kazanır .
5.   Br ya da brden fazla bağımsız değşkenn/tahmn edc ntelğn br bağımlı değşkenle/hedef ntelkle
lşksn modelleme kablyet gelştrr .
6.    
   katsayılarının br regresyon model çn anlamlılık düzeyn yorumlayablr .
7.   Doğrusal regresyon modellernn ne kadar y olduğunu değerlendrmek çn  
   değernn nasıl
yorumlanacağını blr .
8.   Doğrusal regresyon modellernn performansını değerlendrmek çn gerçek ve tahmn edlen değerler
arasındak farkın nasıl analz edleceğn öğrenr .
9.   Bast ve çoklu doğrusal regresyon analzlern Python programlama dl kullanarak gerçekleştreblr .


**Brlkte Düşünelm**

1.   Bast doğrusal regresyon ( smple lnear r egresson ) ve çoklu doğrusal regresyon ( multple lnear
regresson ) analzlerndek temel prenspler nelerdr?
2.   Bağımlı ( dependent ) ve bağımsız ( ndependent ) değşkenler ne anlama gelmektedr? Regresyon


3.   Regresyon analznn temel amacı nedr?
4.   Bast doğrusal regresyon model nasıl oluşturulablr?
5.   Çoklu doğrusal regresyon model nasıl oluşturulablr?
6.   Çoklu doğrusal regresyon model oluşturmak le bast doğrusal regresyon model oluşturmak arasındak
fark nedr?
7.    
   katsayıları regresyon modelnde ney temsl eder? Bu katsayıların anlamlılığı nasıl değerlendrlr?
8.    
   değer nedr ve regresyon modellernde ney fade eder? Yüksek br  
   değer model çn ne
anlama gelr?
9.   Regresyon modellernn performansını değerlendrmek çn gerçek ve tahmn edlen değerler arasındak
fark nasıl analz edlr? Hang performans değerlendrme ölçütler kullanılır?


**Başlamadan Önce**

Bu bölüm, bast doğrusal r egresyon  (smple lnear r egresson ) ve çoklu doğrusal r egresyon  (multple
lnear r egresson ) analzlernn temel prensplern ve teork çerçevesn ele almaktadır . Regresyon analz
ver blm, makne öğrenmes ve özellkle de statstk alanlarında kullanılan temel araçlar arasındadır .
Bağımlı değşken ve bağımsız değşken kavramları regresyon analznn temeln oluşturmaktadır . Böylece
br değşkenn dğern nasıl etkledğ ve br değşkenn dğer le nasıl lşklendrldğ konusunda temel br
anlayış sunulmaktadır .
Bu bölümde öncelkle bast ve çoklu doğrusal regresyon analzler konusunda temel teork blgler verlmştr .
Ardından doğrusal regresyon modellernn verye ne kadar y uyum sağladığı, bağımsız değşkenlere at  

katsayılarının anlamlılık düzeynn nasıl yorumlanması gerektğ açıklanmıştır . Br doğrusal regresyon
modelnn performansının değerlendrlmes çn gerçek ve tahmn edlen değerler arasındak farkın nasıl
analz edlmes gerektğ le lgl teork blgler Bölüm 2.7.4.’ te yer almaktadır . Bu nedenle bu bölümde
konuyla lgl teork blglere yenden yer verlmemştr . İhtyaç duyulması halnde Bölüm 2.7.4.’ ten
faydalanılablr .
Bast ve çoklu doğrusal regresyon le lgl teork blglern ardından doğrusal regresyon analzlernn Python
programlama dlyle seçlen farklı ver setler üzernde nasıl uygulanacağı adım adım açıklanmıştır . Öncek
bölümlerde de kullanılan NumPy , Pandas , Seaborn  ve Matplotlb  kütüphanelernden bu bölümde de
faydalanılmıştır . Ayrıca, doğrusal regresyon modellernn elde edleblmes çn statsmodels kütüphanesnden
faydalanılmıştır . Bu bölüm hem teork hem de pratk açıdan okuyuculara bast ve çoklu doğrusal regresyon
analzn anlamalarını ve kullanmaları açısından temel br deneym sunmaktadır . Bu bölümde kazanılan
deneymn pekştrleblmes çn okuyuculara farklı ver setler üzernde de pratk yapmaları önerlmektedr .


## 6.1. Bast ve Çoklu Doğrusal Regr esyon Analz

Bast doğrusal r egresyon  (smple lnear r egresson ), br bağımlı değşkenn (sonuç değşken/hedef ntelk/


değşken/grd/ ndependent varable ) lşksnn modellenmes çn kullanılan statstk temell br yöntemdr .
Hedef ntelk sayısaldır . Grd değşken  
   le tek çıktı değşken ( 

) arasındak doğrusal lşk olduğunu varsayar (Brownlee, 2016). Bu k ntelk arasında elde edlen lşk
doğrusal br denklemle fade edleblmektedr (Lander , 2017):

  Regresyon denklemnde verlen 
   (beta) katsayıları aşağıdak gb
hesaplanablmektedr . Aşağıda verlen denklemde  
  , 
  değşkennn ortalamasını, 
   de 

 değşkennn ortalamasını temsl etmektedr .

Çoklu doğrusal r egresyon  (multple lnear regresson ), sayısal  br sonuç değşken  
   (yanıt, hedef veya
bağımlı değşken/ntelk/ dependent varable ) le  

 gb br dz bağımsız değşken  veya eş değşkenler ( covarates  olarak da adlandırılmaktadır) arasındak
lşky uydurmak çn kullanılır (Shmuel vd., 2018).


Çoklu doğrusal regresyonda da amaç, bast doğrusal regresyondakne benzer şeklde katsayılarının
bulunmasıdır . Regresyon denklem katsayıları, En Küçük Kar eler (Ordnary Least Squar es) adı verlen br
yöntem kullanılarak hesaplanablmektedr (Shmuel vd., 2018).

### 6.1.1. Analz Öncesnde Dkkat Edlmes Gereken Temel Varsayımlar

Doğrusal regresyon analzler öncesnde aşağıdak şlemlern yapılması tavsye edlmektedr (Brownlee,
2016):
Doğrusallık varsayımı kontr olü: Doğrusal regresyon, grd(ler) ve çıktı arasındak lşknn doğrusal
olduğunu varsayar . Dolayısıyla lşknn doğrusal olmadığı durumlarda lşky doğrusal hale getreblmek
çn verlern dönüştürülmes gerekeblr (örneğn; üstel br lşk çn logartmk dönüşümün yapılması gb).
Ver setndek gürültünün kaldırılması:  Doğrusal regresyon grd ve çıktı değşkenlernn gürültülü
olmadığını varsayar . Bu aşamada ver temzleme şlemlern kullanmak düşünüleblr . Bu şlem en çok
bağımlı değşken çn önemldr . Bağımlı değşkendek ( 

) aykırı değerlern kaldırılması önerlmektedr .
Eş doğrusallığın ( colnearty ) kaldırılması:  Yüksek korelasyonlu grd değşkenlernn olması durumunda
doğrusal regresyon verye aşırı uyum ( overfttng ) sağlayacaktır . Yan, modeln eğtm sırasında model grd
versn ezberleyerek oldukça yüksek performans gösterecek; ancak öğrendğn genelleştrme yeteneğ
ednmeyecektr . Modeln performansı değerlendrlrken düşük performans sonuçları elde edlecektr . Grd


Normal (Gauss) dağılımı kontr olü: Grd ve çıktı değşkenler Gauss dağılımına sahpse doğrusal regresyon
model daha güvenlr tahmnler yapablr . Ntelklern dağılımını normal dağılım gösterr hale getrmek çn
çeştl dönüşümler (örneğn; log veya BoxCox) kullanılablr .
Grdler yenden ölçeklendrme:  Standardzasyon veya normalzasyon kullanarak grd ntelkler yenden
ölçeklendrlrse, doğrusal regresyon genellkle daha güvenlr tahmnler yapablr .
6.1.2.  

 Katsayılarının Yorumu
Analzler sonucunda doğrusal regresyon modellernn  
   katsayılarının 
  -değerler ( p-values ) de
hesaplanmaktadır . Br  
  -değer, kurulan br hpotezn reddedlp reddedlmeyeceğn ya da kabul edlp
edlmeyeceğn gösterr . Bu durumda 
   hpotez, bağımsız değşkenn regresyon model çn anlamlı
olmadığı, modele katkı sağlamadığı, bağımlı değşken le aralarında br lşk olmadığıdır  (Lander , 2017; Ng,
2023). Regresyon katsayısının gerçekte sıfır olma olasılığı şeklnde de yorumlanablr .  
   hpotez
reddedlrse (genellkle 
   se), 
   katsayılarının at olduğu ntelklern model çn anlamlı
olduğu ve bağımlı değşken le aralarında br lşk olduğu sonucuna varılır . Modele gren bağımsız
değşkenlerden brnn 
   katsayısı statstksel olarak anlamlı değlse; lgl değşkenn modelden çıkarılarak
alternatf modellern üretlmes ya da analzler önces değşkenler özelnde kontrol edlmes gereken
unsurların yenden gözden geçrlmes düşünüleblr . Sabt terme lşkn 
  -değernn anlamlılık durumu ( 

-değer) göz ardı edleblmektedr .

### 6.1.3. Doğrusal Regresyon Modellernn Performans Değerlendrmes-


Br doğrusal regresyon modelnn başarısının değerlendrlmesnde modeln very ne kadar y açıkladığı
dkkate alınmaktadır . Bu amaçla sıklıkla kullanılan ölçülerden br  
   değerdr . Bu ölçü, regresyon model
tarafından açıklanan toplam değşkenlğn oranı le tanımlanmaktadır (Porras, 2022). Genel olarak verye y
uyum sağlayan modeller çn 
   değer 1’e yakındır , aks durumda se 


  hesaplamasında; 
   gözlem sayısı, 
   bağımsız değşken sayısı dkkate alınarak düzeltlmş
(adjusted )  

 değer hesaplanmaktadır:


### 6.1.4. Doğrusal Regresyon Modellernn Performans Değerlendrmes

Blndğ üzere bast ve çoklu doğrusal regresyon modellernde bağımlı değşken (hedef ntelk) sayısaldır .
Br doğrusal regresyon modelnn performansının değerlendrlmes çn öncelkle gerçek değerler ve tahmn
edlen değerler arasındak fark, yan hata ( error) hesaplanmaktadır . Ardından bu hata değerler kullanılarak
Ortalama Hata, Ortalama Mutlak Hata vb. performans değerlendrme ölçütlernn nasıl hesaplanacağı Bölüm
2.7.4.’ te yer almaktadır . Bu nedenle, bu bölümde konuyla lgl teork blgler tekrar edlmemştr . İhtyaç
duyulması halnde Bölüm 2.7.4.’ ten faydalanılablr .

## 6.2. Bast Doğrusal Regr esyon Python Uygulaması

Bu çalışmada kullanılan ver set ( ncome.data.csv ), 500 kşden oluşan hayal br örnekleme attr (Bevans,
2023b, 2023c): https://www .scrbbr .com/wp-content/uploads//2020/02/ncome.data_.zp  Ver setnde üç
ntelk yer almaktadır . Bunlardan lk örneklern numarasını temsl eden ID alanı ( Unnamed: 0 ), kncs 15
bn le 75 bn dolar aralığında değşen gelr  ve sonuncusu se 1 le 10 arasında derecelendrlen mutluluk
puanıdır ( mutluluk ) (Tablo 19). Gelr değerlerne br çeşt normalzasyon uygulanmış, 10.000’e bölünerek
gelr versnn mutluluk puanı ölçeğyle eşleşmes sağlanmıştır . Ver setnde 2$’lık br değer 20.000$’ı, 3$’lık
br değer 30.000$’ı temsl etmektedr .
Bu çalışmanın amacı, gelr le bast doğrusal regresyon model (statstksel olarak anlamlı doğrusal lşk)
kurarak mutluluk puanını tahmn etmektr . Bu nedenle yalnızca gelr  ve mutluluk  ntelkler kullanılacaktır .
Gelr ntelğ bağımsız değşken/tahmn sağlayan ntelk olup, mutluluk se bağımlı değşken yan hedef
ntelktr . Bast doğrusal regresyon model le gelre göre mutluluk puanının değşmn ortaya koyan br
denklem elde edlecektr .
Tablo 19: Mutluluk ver setndek ntelkler .


### 6.2.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas, Seaborn, Matplotlb  ve Sckt-learn  kütüphaneler kullanılmıştır (C. R. Harrs
vd., 2020; Hunter , 2007; McKnney , 2010; Pedregosa vd., 201 1; Waskom, 2021). Regresyon modelnn elde
edleblmes çnse statsmodels  kütüphanes yüklenmştr (Seabold & Perktold, 2010). Eğer bu kütüphaneler
yüklü değlse Bölüm 3.1’de açıklandığı gb termnalden kurulmalıdır . Kurulma şlem yapılmışsa öncelkle
aşağıdak kod satırları Python koduna dahl edlmeldr .


### 6.2.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . ncome.data.csv  dosyasını okumak
çn Pandas  kütüphanesnden pd.read_csv()  fonksyonu kullanılmıştır . verSet.head(6)  le, ver setndek lk
6 satır ekrana yazdırılmıştır .


### 6.2.3. Ver Ön-şleme

Ver setndek lk sütun analzlerde kullanılmayacağı çn ver setnden çıkarılmıştır .


Ver setndek ntelklern adları sırasıyla gelr  ve mutluluk  olacak şeklde değştrlmştr . Ardından ver


gelr  ve mutluluk  ntelkler, serplme dyagramı üzernde ncelenrse aralarında poztf doğrusal br lşknn
varlığı görülecektr (Şekl 86). Ver, köşegen boyunca dağılmıştır . Yan gelr  arttıkça mutluluk  puanı da
artmakta, gelr azaldıkça se mutluluk  puanının da azalmakta olduğu söyleneblr .


Şekl 86: Gelr ve mutluluk ntelklernn serplme dyagramı.
Hedef ntelk kutu grafğ yardımı le ncelenmştr (Şekl 87). Ntelkte herhang br aykırı değer tespt
edlememştr . Kutu grafğnden sonra gelen ekran görüntüsünde flers  bölümünde boş br dz yer aldığı


Şekl 87: Gelr ntelğnn kutu grafğ.


Ver setnde eksk değer kontrolü yapılmış; ancak herhang br eksk değere rastlanmamıştır .

Ntelkler arasındak korelasyon ncelenmştr . Burada tek br bağımsız değşken olduğundan, yalnızca
bağımlı ve bağımsız değşken arasındak korelasyon verleblmştr . Oysa korelasyon ncelemes, brden fazla
bağımsız değşkenn olması durumunda brbryle lşks yüksek olan ntelklern tespt edlmes ve buna
göre bu ntelklerden brnn analzler önces ver setnden çıkarılması açısından önemldr . Bunun çn scpy
kütüphanesnn stats modülünden pearsonr()  fonksyonu kullanılmıştır (Vrtanen ve dğ., 2020). Öncek


katsayısı ( statstc ) le k ntelk arasındak lşknn anlam düzeyn çeren  
  -değern ( pvalue ) de
hesaplıyor olmasıdır . İk ntelk arasındak lşknn anlamlı olablmes çn  
 -değernn genellkle 0.05’ ten
küçük olması beklenr . Elde edlen sonuca göre gelr  ve mutluluk  arasındak Pearson korelasyon katsayısı
0.87’dr . Hesaplanan  
  -değer blmsel gösterm ( scentfc notaton ) bçmnde verlmştr . Yan;
3.956245289952218e-151 değer  
   şeklnde fade
edlmektedr . Buna göre elde edlen p-değer sıfıra oldukça yakın br değerdr . Dolayısıyla gelr le mutluluk
puanı arasında poztf yönde güçlü, anlamlı br lşknn varlığından söz edleblr ( 

).


Hedef ntelğn, normal (Gauss) dağılımına uyup uymadığı se hstogram yardımı le nceleneblr (Şekl 88).
Hstogramdan da görülebleceğ gb vernn dağılımında normal dağılıma (çan eğrsne) benzer br görünüm
söz konusu değldr . Daha ayrıntılı blg çn normal dağılım testlernden yararlanılablr .


Şekl 88: Mutluluk puanının hstogramı.
Son olarak eğtm ve test ver setler oluşturulmuştur . Vernn %70’ eğtm ( egtm ), %30’u se test ver


### 6.2.4. Modelleme

Doğrusal regresyon modelnn ( lr_model ) oluşturulablmes çn smf.ols()  fonksyonu kullanılmıştır . Bunun
çn fonksyonun lk ar gümanı olarak mutluluk ~ gelr  bçmnde bağımlı değşkene karşı bağımsız değşken
olacak bçmde modeln formül gösterm yer almaktadır . Eğtm ver set le model kurulacağından, knc
argüman olarak eğtm ver set ( egtm ) verlmştr . .ft() le model oluşturulmuştur .
Modele at .summary()  metodu le model özet yazdırılmıştır (Şekl 89). Bu özet blg regresyon denklemnn
oluşturulması ve regresyon model ylğnn değerlendrleblmesne lşkn brçok öneml blgy
çermektedr .


Şekl 89: Bast doğrusal regresyon model özet.
Şekl 89’dak regresyon model raporunda coef olarak verlenler model sabt ( Inter cept) ve gelr değşken
katsayısıdır ( gelr ). P > |t| alanında lstelenen değerler se modele gren ntelklere at anlamlılık düzeylern
göstermektedr .  
  değer çok düşük olduğu çn ( 

), sıfır hpotez reddedeblr ve gelrn mutluluk üzernde statstksel olarak anlamlı br etks olduğu


brmlk artışa karşılık mutlulukta 0.7083 brmlk br artış söz konusudur .
Regresyon modelnn sabt ve gelr ntelğne at beta katsayılarına ayrıca ulaşmak çn aşağıdak kod satırı
kullanılablr .


Bu blglerden faydalanarak regresyon denklem  aşağıdak gb yazılablr .

 Elde edlen modeln verye uyumu, Regresyon Model tarafından açıklanan toplam değşkenlğn oranı 

le değerlendrleblmektedr . Hatırlanacak olursa, bu değern 1’e yakın olması, modeln verye y uyum
sağladığını, 0’a yakın olması se zayıf bçmde uyum sağladığını göstermektedr . Aşağıdak kodlar yardımı le
regresyon modeln 

 değer yazdırılablr .

 Şekl 89’da hesaplanan 

 değerne göre ( Adj. R-squar ed) bast doğrusal regresyon modelnn verdek toplam değşkenlğn
%74.8’n açıkladığı söyleneblr .

### 6.2.5. Performans Değerlendrme

Br öncek adımda kurulan regresyon model le test ver setndek örnekler çn tahmnde bulunulacaktır . Bu
hesaplama regresyon denklem le elde edleblr . Örneğn aşağıda verlen test ver setndek lk örneğn gelr
4.98’dr . Bu değer regresyon denklemnde yerne yazılırsa, test ver setndek lk örneğn mutluluk puanı


Tüm örneklern benzer şeklde hesaplanması çn lr_model.pr edct()  fonksyonundan yararlanılablr .
Fonksyona test ver setndek bağımsız değşkenler (bu örnekte gelr  ntelğ) verlr .


Modeln test ver setndek tüm örnekler çn mutluluk puanı tahmnler lr_tahmnler  dzsnde tutulmaktadır .
Tahmn değerler ve gerçek değerlerden lk 5 tanes yazdırılırsa modeln gerçek değerlere ne kadar yakın ya
da uzak tahmnde bulunduğu nceleneblecektr . Örneğn test ver setndek lk örneğn gerçek mutluluk puanı
(mutluluk ) 3.43’dr; lr_model.pr edct()  fonksyonu le de bu değer 3.75 olarak tahmn edlmştr
(lr_tahmnler .loc[0,] ) (hesaplarda sayıların vr gülden sonra kullanılan basamak sayısına göre oldukça küçük
br farklılık çıkmıştır).
Ver setnde bulunan tüm örnekler çn doğrusal regresyon tahmnlernn ( lr_tahmnler ) ve ver setndek


Test ver setndek tüm örnekler çn model tahmn değerler elde edldkten sonra gerçek değerler ve tahmn
edlen değerler performansV ers adlı br DataFrame nesnesne atanmıştır . Bu şlem zorunlu değldr; ancak
gerçek değerler ve model tahmnlern daha y nceleyeblmek ve sonrak performans hesaplamalarında
yardımcı olması çn gerçekleştrlmştr .


Sonrasında performansV ers DataFrame nesnesndek gerçek değerler ve tahmn edlen değerler
kullanılarak öncelkle hata değerler, sonra se hata değerler kullanılarak hesaplanablen ortalama hata ( ME),
ortalama mutlak hata ( MAE ), ortalama yüzde hata ( MPE ), ortalama mutlak yüzde hata ( MAPE ), ortalama
karesel hata ( MSE ) ve ortalama karesel hatanın karekökü ( RMSE ) hesaplanmıştır ( Not:  MSE, RMSE’nn


Elde edlen bu metrklerden MAE , MSE  ve RME  sklearn.metrcs  çndek hazır fonksyonlar kullanılarak da


Şekl 86’da tüm ver setndek örneklern gelr  ve mutluluk  puanı ntelkler kullanılarak çzlen serplme
dyagramı, bu kez test ver setndek gelr  ve mutluluk  puanı ntelkler kullanılarak çzlmş, dyagrama
bast doğrusal regresyon model doğrusu da eklenmştr (mav renkte) (Şekl 90). Doğrunun eğm, gelr
değşken çn elde edlen katsayı 0.708’dr ve 0.228 değer ( Inter cept) x = 0 olduğunda doğrunun y eksenn
kestğ noktadır . Şekl 90’ın elde edleblmes çn aşağıdak kod satırlarının brlkte seçlerek çalıştırılması
gerekmektedr .


Şekl 90: Test ver setnde gelr ve mutluluk puanı ntelklernn serplme dyagramı ve regresyon model
eğrs.

## 6.3. Çoklu Doğrusal Regr esyon Python Uygulaması

Bu çalışmada kullanılan ver set ( heart.data.csv ), 500 kasabadan oluşan hayal br örnekleme attr (Bevans,


yer almaktadır . Bunlardan lk örneklern numarasını temsl eden ID alanı ( Unnamed: 0 ), kncs her gün şe
bskletle gden nsanların yüzdes ( bskletKullanm ), üçüncüsü sgara çen nsanların yüzdes
(sgaraDurum ) ve sonuncusu se kalp hastalığı olan nsanların yüzdesdr ( kalpHastalg ) (Tablo 20).
Bu çalışmanın amacı, her gün şe bskletle gden nsanların yüzdes ve sgara çen nsanların yüzdesn
kullanarak çoklu doğrusal regresyon model le kalp hastalığı olan nsanların yüzdesn tahmn etmektr .
Bskletle gden nsanların yüzdes ve sgara çen nsanların yüzdes bağımsız değşkenler olup, kalp hastalığı
olan nsanların yüzdes se bağımlı değşken yan hedef ntelktr . Çoklu doğrusal regresyon model le,
bsklet kullanımı ve sgara kullanma durumlarına göre kalp hastalığı olan nsanların yüzdesnn değşmn
ortaya koyan br denklem elde edlecektr .
Tablo 20: Kalp ver setndek ntelkler .


### 6.3.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas , Seaborn  ve Matplotlb  kütüphaneler kullanılmıştır (C. R. Harrs vd., 2020;
Hunter , 2007; McKnney , 2010; Pedregosa vd., 201 1; Waskom, 2021). Regresyon modelnn elde
edleblmes çnse statsmodels  kütüphanes yüklenmştr (Seabold & Perktold, 2010). Eğer bu kütüphaneler
yüklü değlse Bölüm 3.1’de açıklandığı gb termnalden kurulmalıdır . Kurulma şlem yapılmışsa öncelkle
aşağıdak kod satırları Python koduna dahl edlmeldr .


### 6.3.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . ncome.data.csv  dosyasını okumak
çn Pandas  kütüphanesnden pd.read_csv()  fonksyonu kullanılmıştır . verSet.head(6)  le ver setndek lk


### 6.3.3. Ver Ön-şleme

Ver setndek lk sütun analzlerde kullanılmayacağı çn ver setnden çıkarılmıştır .


Ver setndek ntelklern adları sırasıyla bskletKullanm, sgaraDurum ve kalpHastalg  olacak şeklde
değştrlmştr . Ardından ver setne at özet blg görüntülenmştr .


Bskletle şe gden nsanların yüzdes ( bskletKullanm ) ve sgara çen nsanların yüzdes ( sgaraDurum )
ntelkler ayrı ayrı kalp hastalığı olan nsanların yüzdes le serplme dyagramı üzernde ncelenmştr .


Şekl 91 ncelendğnde soldak serplme dyagramından bskletle şe gden nsanların yüzdes
(bskletKullanm ) le kalp hastalığı olan nsanların yüzdes ( kalpHastalg ) arasında ters yönde (negatf)
güçlü br lşknn varlığı görüleblr . Yan bskletle şe gden nsanların yüzdes ( bskletKullanm ) arttıkça
kalp hastalığı olan nsanların yüzdes ( kalpHastalg ) azalmakta, bskletle şe gden nsanların yüzdes
(bskletKullanm ) azaldıkça se kalp hastalığı olan nsanların yüzdesnn ( kalpHastalg ) de artmakta
olduğu söylenr . Oysa Şekl 91’de sağ taraftak serplme dyagramında sgara çen nsanların yüzdes
(kalpHastalg ) le kalp hastalığı olan nsanların yüzdes ( kalpHastalg ) arasında poztf ya da negatf yönde
doğrusal br lşk tespt edlememştr .


Şekl 91: bsklet kullanm ve sgaraDurum ntlklernn kalpHastalg bağımlı değşken le serplme
dyagramı.
Ayrıca eş-doğrusallık ( mult-colnearty ) açısından sgara çen nsanların yüzdes ( sgaraDurum ) ve
bskletle şe gden nsanların yüzdes ( bskletKullanm ) ntelklernn kend arasındak lşk de
ncelenmştr . Şekl 92’dek serplme dyagramında sgara çen nsanların yüzdes ( sgaraDurum ) le
bskletle şe gden nsanların yüzdes ( bskletKullanm ) arasında poztf ya da negatf yönde doğrusal br
lşk tespt edlememştr .


Hedef ntelk olan kalp hastalığı olan nsanların yüzdes ( kalpHastalg ) ntelğnn kutu grafğ yardımı le
ncelenmştr (Şekl 93). Ntelkte herhang br aykırı değer tespt edlmemştr . Kutu grafğnden sonra
verlen ekran görüntüsünde flers  bölümünde boş br dz yer aldığı görüleblr .


Şekl 93: Kalp hastalığı olan nsanların yüzdes ntelğnn kutu grafğ.


Ver setnde eksk değer kontrolü yapılmış ancak herhang br eksk değere rastlanmamıştır .

 Ntelkler arasındak korelasyon ncelenmştr . Elde edlen sonuca göre; bskletle şe gden nsanların


güçlü, anlamlı br lşknn varlığından söz edleblr ( 

). Bağımsız değşkenler arasında da lşk zayıf olduğundan eş-doğrusallık meydana getrecek herhang br
durum söz konusu değldr .


Bast doğrusal regresyonda olduğu gb hedef ntelğn normal (Gauss) dağılımına uyup uymadığı se
hstogram yardımı le nceleneblr (Şekl 94).


Şekl 94: Kalp hastalığı olan nsanların yüzdes ntelğnn hstogramı.
Son olarak eğtm ve test ver setler oluşturulmuştur . Vernn %70’ eğtm ( egtm ), %30’u se test ver


### 6.3.4. Modelleme

Çoklu doğrusal regresyon modelnn ( lr_model ) oluşturulablmes çn yne smf.ols()  fonksyonu
kullanılmıştır . Bunun çn fonksyonun lk ar gümanı olarak kalpHastalg ~ bskletKullanm +
sgaraDurum  bçmnde bağımlı değşkene karşı bağımsız değşken olacak bçmde modeln formül
gösterm yer almaktadır . Eğtm ver set le model kurulacağından knc ar güman olarak eğtm ver set
(egtm ) verlmştr . .ft() le model oluşturulmuştur .
Modele at .summary()  metodu le model özet yazdırılmıştır (Şekl 95). Bu özet blg, br öncek
uygulamaya benzer şeklde regresyon denklemnn oluşturulması ve regresyon model ylğnn
değerlendrleblmesne lşkn brçok öneml değer çermektedr .


Şekl 95: Çoklu doğrusal regresyon model özet.
Şekl 95’ te görüleceğ üzere bskletle şe gden nsanların yüzdes ( bskletKullanm ) le kalp hastalığı olan


yüzdesndek her br brmlk artışa karşılık kalp hastalığı olan nsanların yüzdesnde 0.1997 brmlk br
azalış  söz konusudur .
Regresyon model sabt le gelr ntelğne at beta katsayısı değerlerne ayrıca ulaşılmak stenrse aşağıdak
kod satırı kullanılablr .


Bu blglerden faydalanarak regresyon denklem aşağıdak gb yazılablr .

 Şekl 95’ te hesaplanan düzeltlmş 
   değerne göre ( Adj. R-squar ed) bast doğrusal regresyon modelnn
verdek toplam değşkenlğn %98’n açıkladığı söyleneblr .  

 değer se aşağıdak kod satırları yardımı le yazdırılablr .


### 6.3.5. Performans Değerlendrme

Br öncek adımda kurulan çoklu doğrusal regresyon model le test ver setndek örnekler çn tahmnde
bulunulacaktır . Bu hesaplama regresyon denklem le elde edleblr . Örneğn test ver setndek lk örneğn
bskletKullanm  ntelğ 65.13 ve sgaraDurum  ntelğ 2.22’dr . Bu değerler çoklu doğrusal regresyon
denklemnde yerne yazılırsa, test ver setndek lk örneğn kalp hastalığı olan nsanların yüzdes değer 2.33


Tüm örneklern benzer şeklde hesaplanması yerne lr_model.pr edct()  fonksyonundan yararlanılablr .
Fonksyona test ver setndek bağımsız değşkenler verlmştr .


Modeln test ver setndek tüm örnekler çn mutluluk puanı tahmnler lr_tahmnler  dzsnde tutulmaktadır .
Tahmn değerler ve gerçek değerlerden lk 5 tanes yazdırılırsa modeln gerçek değerlere ne kadar yakın ya
da uzak tahmnde bulunduğu nceleneblr . Test ver setndek lk örneğn gerçek kalp hastalığı olan nsanların
yüzdes ( kalpHastalg ) değer 2.85’ tr; lr_model.pr edct()  fonksyonu le de bu değer 2.33 olarak tahmn
edlmştr ( lr_tahmnler .loc[0,] ) (hesaplarda sayıların vr gülden sonra kullanılan basamak sayısına göre
oldukça küçük br farklılık çıkmıştır).
Ver setnde bulunan tüm örnekler çn çoklu doğrusal regresyon tahmnlernn ( lr_tahmnler ) ve ver
setndek gerçek mutluluk puanlarına lşkn lk 5 değer ( test.mutluluk ) aşağıda verlmştr .


Test ver setndek tüm örnekler çn model tahmn değerler elde edldkten sonra gerçek değerler ve tahmn
edlen değerler performansV ers adlı br DataFrame nesnesne atanmıştır . Bu şlem zorunlu değldr ancak
gerçek değerler ve model tahmnlern daha y nceleyeblmek ve sonrak performans hesaplamalarında
yardımcı olması çn gerçekleştrlmştr .


Sonrasında performansV ers DataFrame nesnesndek gerçek değerler ve tahmn edlen değerler
kullanılarak öncelkle hata değerler, sonra se hata değerler kullanılarak hesaplanablen ortalama hata ( ME),
ortalama mutlak hata ( MAE ), ortalama yüzde hata ( MPE ), ortalama mutlak yüzde hata ( MAPE ), ortalama


Elde edlen MAE , MSE  ve RME  metrkler  sklearn.metrcs  çndek hazır fonksyonlar kullanılarak da


**Bölüm Özet**

Bu bölüm ver blm, makne öğrenmes ve statstk alanlarında öneml br rol oynayan bast doğrusal
regresyon  (smple lnear r egresson ) ve çoklu doğrusal r egresyon  (multple lnear r egresson ) analzlernn
temel prensplern ve teork çerçevesn ele almaktadır . Bağımlı değşken ve bağımsız değşken kavramları,
regresyon analznn temeln oluşturarak değşkenler arasındak etkleşm açıklamaktadır . Teork blglern
yanı sıra doğrusal regresyon modellernn uyum sağlama yetenekler, beta ( 
  ) katsayılarının anlamlılığı ve
model performansının değerlendrlmes gb konular da ele alınmıştır .
Bu bölümde bast ve çoklu doğrusal regresyon analzlernn Python programlama dl le nasıl uygulanacağı
adım adım açıklanarak verlmştr . Bu analzler çn NumPy , Pandas, Seaborn, Matplotlb, Sckt-learn  ve
statsmodels  gb kütüphaneler kullanmaktadır . Bu bölüm hem teork hem de pratk açıdan bast ve çoklu
doğrusal regresyon analzn anlamak ve uygulamak steyenlere temel br deneym sunmaktadır . Bu kazanılan
deneymn pekştrlmes çn okuyuculara farklı ver setler üzernde çalışması  önerlmektedr .


**Kaynakça**

Bevans, R. (2023a). Heart Dsease Data Set . https://www .scrbbr .com/wp-
content/uploads//2020/02/heart.data_.zp
Bevans, R. (2023b). Income-Happness Data Set . https://www .scrbbr .com/wp-
content/uploads//2020/02/ncome.data_.zp
Bevans, R. (2023c). Lnear Regr esson n R | A Step-by-Step Gude & Examples . Scrbbr .
https://www .scrbbr .com/statstcs/lnear -regresson-n-r/
Brownlee, J. (2016, Mart 24). Lnear Regresson for Machne Learnng. MachneLearnngMastery .Com .


Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
Hunter , J. D. (2007). Matplotlb: A 2D graphcs envronment. Computng n Scence & Engneerng , 9(3), 90-
95. https://do.or g/10.1 109/MCSE.2007.55
Lander , J. P. (2017). R for Everyone Advanced Analytcs and Graphcs  (2. bs). Pearson Educaton Inc.
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Ng, R. (2023). Evaluatng a Lnear Regr esson Model . rtcheng.gthub.o.
http://www .rtcheng.com/machne-learnng-evaluate-lnear -regresson-model/
Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Porras, E. M. (2022). R Lnear Regr esson T utoral: Lm Functon n R wth Code Examples .
https://www .datacamp.com/tutoral/lnear -regresson-R
Seabold, S., & Perktold, J. (2010). statsmodels: Econometrc and statstcal modelng wth python. 9th
Python n Scence Confer ence.
Shmuel, G., Bruce, P . C., Yahav, I., Patel, N. R., & Lctendahl, K. C. (2018). Data Mnng for Busness
Analytcs  (1. bs). Wley .
Vrtanen, P ., Gommers, R., Olphant, T. E., Haberland, M., Reddy , T., Cournapeau, D., Burovsk, E.,
Peterson, P ., Weckesser , W., Brght, J., van der Walt, S. J., Brett, M., Wlson, J., Mllman, K. J., Mayorov , N.,
Nelson, A. R. J., Jones, E., Kern, R., Larson, E., … ScPy 1.0 Contrbutors. (2020). ScPy 1.0: Fundamental
Algorthms for Scentfc Computng n Python. Natur e Methods , 17, 261–
272. https://do.or g/10.1038/s41592-019-0686-2
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021


**Ünte Soruları**

Soru-1 :
Aşağıdak seçeneklerden hangs br yönü le dğerlernden farklıdır?
(Çoktan Seçmel)
(A) Tahmn sağlayan (tahmn edc) ntelk
(B) Grd değşken


(D) Açıklayıcı değşken
(E) Hedef ntelk
Cevap-1 :
Hedef ntelk
Soru-2 :
Aşağıdaklerden hangs bast ve çoklu doğrusal regresyon modeller le lgl hatalı br fadedr?
(Çoktan Seçmel)
(A) Bast doğrusal regresyonda tek br bağımsız değşken bulunur .
(B) Çoklu doğrusal regresyonda tek br bağımsız değşken bulunur .
(C) Bast doğrusal regresyonda tek br bağımlı değşken bulunur .
(D) Çoklu doğrusal regresyonda tek br bağımlı değşken bulunur .
Bast ve çoklu regresyon modellernde elde edlen 
  katsayıları vardır .
Cevap-2 :
Çoklu doğrusal regresyonda tek br bağımsız değşken bulunur .
Soru-3 :
Aşağıda 
  değerler verlen doğrusal regresyon modellernden hangsn seçmek daha uygun olur?
(Çoktan Seçmel)
(A) Model 1:
(B) Model 2: 
(C) Model 3: 
(D) Model 4: 
Model 5: 
Cevap-3 :
Model 1:


Soru-4 :
Aşağıda ortalama karesel hatanın karekökü ( RMSE ) değerler verlen doğrusal regresyon modellernden
hangsn seçmek daha uygun olur?
(Çoktan Seçmel)
(A) Model 1:
(B) Model 2: 
(C) Model 3: 
(D) Model 4: 
Model 5: 
Cevap-4 :
Model 1:
Soru-5 :
Br kşnn uyku süres le günlük performansı arasındak lşky modellemek ve netcede kşnn
performansını tahmn etmek çn doğrusal regresyon analz gerçekleştrlmştr . Analz sonucu sabt değer (
 ) 70, uyku süresnn 
  katsayısı 1.5 olarak bulunmuştur . Bu blglere göre; elde edlen bast doğrusal
regresyon denklem hang seçenekte doğru olarak verlmştr?
(Çoktan Seçmel)
(A) 
(B) 
(C) 
(D) 
Cevap-5 :


Soru-6 :
Br öğrencnn sınav performansını etkleyen faktörler nceleyen br çoklu doğrusal regresyon model şu
şekldedr:
Regresyon denklemndek katsayılar se 
  şeklnde
hesaplanmıştır . Verlenlere göre, br öğrencnn haftalık çalışma saat 10, devamsızlık oranı 3 ve genel not
ortalaması 85 se, bu öğrencnn tahmn sınav performansı aşağıdak seçeneklerden hangsnde doğru şeklde
verlmştr?
(Çoktan Seçmel)
(A) 250
(B) 375
(C) 450
(D) 475
550
Cevap-6 :
475
Soru-7 :
Br çoklu doğrusal regresyon denklem aşağıdak gb fade edlmştr:
Buna göre aşağıdaklerden hangs doğrudur?
(Çoktan Seçmel)
(A) Reklam harcaması arttıkça satışlar azalır .
(B) Müşter memnunyet arttıkça satışlar artar .
(C) Rakp fyatları arttıkça satışlar artar .
(D) Müşter memnunyet bağımlı değşkendr .
Satış, bağımsız değşkenlerden brdr .
Cevap-7 :


Soru-8 :
Br çoklu doğrusal regresyon modelnde, br değşkenn modele grp grmeyeceğn aşağıdak seçeneklerde
verlen kavramlardan hangs gösterr?
(Çoktan Seçmel)
(A) Bağımlı Değşken
(B) Anlamlılık Düzey (
  -değer)
(C) 
  Değer
(D) Ortalama Karesel Hata (MSE)
Regresyon Katsayısı
Cevap-8 :
Anlamlılık Düzey (
  -değer)
Soru-9 :
Aşağıda elde edlen regresyon analz sonucuna göre aşağıdak seçeneklerden hangs yanlıştır?
(Çoktan Seçmel)


(B) Analzlerde 2 adet bağımsız, 1 adet bağımlı değşken kullanılmıştır .
(C) Regresyon denklem 
  şeklnde fade edleblr .
(D) 
  değer (adjusted) 0.909’dur .
(E) 
  ve 
  ’ye at p-değerler ncelenrse, X1 ve X2 değşkennn modele katkısının olmadığı (model çn
anlamlı olmadığı) sonucu elde edlr .
Cevap-9 :
 ve 
  ’ye at p-değerler ncelenrse, X1 ve X2 değşkennn modele katkısının olmadığı (model çn
anlamlı olmadığı) sonucu elde edlr .
Soru-10 :
Sayısal br bağımlı değşken le yalnızca br bağımsız değşken arasındak lşky nceleyen analz
hangsdr?
(Çoktan Seçmel)
(A) İk Yönlü Regresyon
(B) Çoklu Doğrusal Regresyon
(C) Bast Doğrusal Regresyon
(D) Lojstk Regresyon
Nonparametrk Regresyon
Cevap-10 :


# 7. K-En Yakın Komşu Algoritması


**Özlü Söz**

 “Bana arkadaşını söyle, sana km olduğunu söyleyeym. ”
Atasözü


**Kazanımlar**

1.   k-En Yakın Komşu algortmasının ( k-Near est Neghbor Algorthm, k-NN ) temel prenspler ve çalışma
mantığı hakkında blg sahb olur .
2.   k-NN algortmasının avantajları ve dezavantajlarını anlar .
3.   k-NN algortmasında çoğunluk oylaması ( majorty votng ) ve ağırlıklı oylamanın ( weghted votng ) nasıl
kullanılacağını blr .
4.   k-NN algortmasında komşu sayısı k’nın seçm çn yapılması gerekenler blr .
5.   Br uzaklık fonksyonunun k-NN algortması le lşksn blr .
6.   Tembel öğrenme ( lazy learnng ) hakkında blg sahbdr .
7.   Sınıflandırma modellernn performansını değerlendrme üzerne pratk kazanır .
8.   Sınıflandırmada poztf ve negatf sınıf kavramlarını blr ve performans sonuçlarını uygun şeklde
hesaplar ve yorumlayablr .
9.   Kontenjans tablosu ( contngency table ) oluşturablr .
10. Python programlama dl le k-NN algortması model kurablr ve performansını değerlendreblr .


**Brlkte Düşünelm**

1.   k-En Yakın Komşu algortmasının ( k-Near est Neghbor Algorthm, k-NN ) temel çalışma mantığı nasıl
fade edleblr?
2.   Hang durumlarda k-NN kullanmak uygun olablr , hang durumlarda algortmanın dezavantajları ön


3.   Çoğunluk oylaması ve ağırlıklı oylamanın nasıl çalışır? k-NN le sınıfı blnmeyen br örneğn sınıfını
bulablmek çn bu k yöntem nasıl kullanılablr?
4.   k-NN algortmasında komşu sayısı k nasıl seçlr?
5.   Uzaklık fonksyonunun k-NN algortması le lşks nedr? k-NN algortması le hang uzaklık
fonksyonları kullanılablr?
6.   Tembel öğrenme ( lazy learnng ) nedr?
7.   Hang metrkler kullanarak br sınıflandırma modelnn başarısı ölçüleblr?
8.   Sınıflandırmada poztf ve negatf sınıfların önem nedr? Poztf ve negatf sınıflar değşrse hang
performans değerlendrme ölçütlernn yorumu değşr?
9.   Kontenjans tablosu ( contngency table ) nedr ve nasıl oluşturulur? Bu tabloyu kullanarak br
sınıflandırma modelnn performansın nasıl değerlendrlr?
10. Python programlama dl kullanarak k-NN algortması model nasıl kullanılablr? Hang kütüphanelerden
yararlanılır? Br k-NN sınıflandırıcının performansını değerlendrmek çn hang adımlar takp edlr?


**Başlamadan Önce**

k-En Yakın Komşu Algortması  (k-Near est Neghbor Algorthm, k-NN ), sınıflandırma ve regresyon
problemlernn çözümünde kullanılan uygulaması kolay danışmanlı öğrenme algortmasıdır . k-NN
algortması, “Bana arkadaşını söyle, sana km olduğunu söyleyeym” atasözü le özdeşleştrlmektedr .
Lteratürde araştırmacılar tarafından sıklıkla terch edlen br algortmadır .
k-NN, ver noktaları arasındak uzaklığı ölçmek çn br uzaklık fonksyonu kullanır . Ökld  (Eucldean )
uzaklığı yaygın olarak kullanılan br örnektr; Manhattan, Cosne gb farklı fonksyonlar da uygulanablr;
ancak bu noktada ntelklern ver tp göz ardı edlmemeldr . k-NN algortmasında kullanılacak komşu sayısı
olan  
  ’nın seçm önemldr . Bu değer , modeln performansını etkleyeblr .
Bu bölümde öncelkle k-NN algortması konusunda temel teork blgler verlmştr . Ardından k-NN
algortmasının Python dlnde meme kanser teşhs uygulaması ele alınmıştır . Br k-NN algortması
modelnn performansının değerlendrlmes çn gerçek ve tahmn edlen değerler kullanılarak br kontenjans
tablosunun oluşturulması ve buna bağlı olarak performans değerlendrme ölçütlernn hesaplanması Bölüm
2.7.2.’de yer almaktadır . Bu nedenle bu bölümde konuyla lgl teork blglere yenden yer verlmemştr .
İhtyaç duyulması halnde Bölüm 2.7.2.’den faydalanılablr .
Öncek bölümlerde de kullanılan NumPy , Pandas , Seaborn , Matplotlb  ve Sckt-learn  kütüphanelernden
faydalanılmıştır . Bu bölüm hem teork hem de pratk açıdan okuyuculara k-NN algortmasını anlamalarını ve
kullanmaları açısından temel br deneym sunmaktadır . Bu bölümde kazanılan deneymn pekştrleblmes
çn okuyuculara, kamuya açık ya da uzmanlık alanlarına göre seçecekler farklı ver setler üzernde
çalışmaları önerlmektedr .


## 7.1. k-En Yakın Komşu Algortması

k-En Yakın Komşu Algortması  (k-Near est Neghbor Algorthm, k-NN ) lteratürde sıklıkla kullanılan br
danışmanlı öğrenme algortmasıdır . Yan k-NN algortması le çalışırken ver setnde br hedef ntelğe htyaç


olduğunu söyleyeym ” atasözü le bastçe açıklanablr . Buna göre, sınıf etket blnmeyen br örneğn eğtm
ver setnde yer alan tüm örneklere olan uzaklığı ( dstance ) hesaplanmaktadır . Hesaplanan uzaklıklar ( 
  ),
küçükten büyüğe doğru sıralanır ve eğtm ver setnde sınıfı blnmeyen örneğe en yakın 
   adet örnek
seçlr . Seçlen 

 adet örnek arasında sayıca en çok sınıf etket , sınıf etket blnmeyen örneğe atanmaktadır . Bu yönteme
çoğunluk oylaması  (majorty votng ) adı verlmektedr .
Örneğn Şekl 96’da kırmızılar Covd-19, mavler se grp hastalarını göstersn. Üzernde soru şaret ( ?) olan
yen hastanın se, henüz Covd-19  ya da grp olduğu blnmemektedr . k-NN algortması çn k=1 alınırsa,
soru şaretl hastaya en yakın 1 hastanın sınıf etketne bakılarak soru şaretl hastaya Covd-19  teşhs
konacaktır . k-NN çn k=3 alınırsa, bu kez de soru şaretl hastaya en yakın 3 hastanın sınıf etketne bakılarak
sayıca fazla olması sebebyle soru şaretl hastaya grp teşhs konacaktır .


Şekl 96: Komşu sayısı k=1 ve k=3 çn temsl br gösterm.
k-NN algortması, hem sınıflandırma hem de regresyon  problemlernn çözümünde kullanılablmektedr . Br
başka fade le ver setnde yer alan hedef ntelk hem kategork hem de nümerk olablr . Regresyon
durumunda hedef ntelk sayısal olacağından en sık tekrar eden sınıf etketnn seçlmes yerne en yakın
komşuların hedef ntelğne at değerlern ortalaması alınmaktadır .
Uzaklık hesaplamalarında Eucldean (Ökld), Manhattan, Chebyshev , Cosne, Cty Block, Gower , Jaccard
gb uzaklık fonksyonları (Cha, 2007) kullanılablr . Bazı durumlarda çeştl benzerlk ölçüler ( smlarty
measur es) de hesaplamalarda kullanılmakta, 1-benzerlk ölçüsü  şeklnde hesaplamalarda benzerlk ölçüler
uzaklık/benzemezlk ( dssmlarty ) ölçülerne dönüştürüleblmektedr . k-NN algortması le çalışırken
tahmn sağlayan ntelklern ver tp konusunda da br kısıt mevcut değldr; ancak algortma çn seçlecek
uzaklık fonksyonu ver setndek (tahmn sağlayan) ntelklernn ver tpne göre de şekllenmektedr (Cho
vd., 2010; Dekhtyar , 2009; Gan, 201 1; Kartal, 2015): Örneğn tüm ntelklern sayısal olması durumunda
Ökld uzaklığı çokça terch edlmektedr . 0 ve 1’lerden (kategork ntelk) oluşması durumunda Smple
Matchng ya da Jaccard uzaklıkları kullanılablr . Hem sayısal hem de kategork ntelklern varlığında se
Gower uzaklığı terch edleblr . Ayrıca ntelklerde gerekl ver tp dönüşümü sağlanarak uygun uzaklık
fonksyonu kullanılablmektedr .  
  gözlem sayısı olmak üzere sınıfı blnmeyen br 
   örneğne 


  k-NN algortmasının 
   parametres, ver setne göre ayarlanması
gereken br hperparametr edr (hyperparameter ). Küçük br  
   değer aşırı uyuma ( overfttng ) yol
açablrken, büyük  
   değer yetersz uyuma ( underfttng ) yol açablr . Bu nedenle doğru  
   değern
seçmek y br performans elde etmek çn önemldr . Bu sebeple 

’nın farklı değerler çn analz yapılarak modellere at performans ncelenmel ve nha karar verlmeldr .
k-NN algortmasının anlaşılmasının ve uygulanmasının kolaylığı avantajları arasında sayılablr . Bununla
brlkte yen örnek le tüm eğtm gözlemler arasındak uzaklığın hesaplanması gerektğnden büyük ver
setler çn hesaplama açısından malyetl olablmektedr .

### 7.1.1. k-NN Algortmasının Adımları

k-NN algortmasının grds X_tran , y_tran  ve sınıfı blnmeyen br  

 örneğ olmak üzere, adımları şu şeklde verleblr (Balaban & Kartal, 2018; Han & Kamber , 2006;
Harrngton, 2012):
1. Test örneğ  

 le eğtm ver setndek ( X_tran ) her örnek arasındak uzaklıklar Eucldean (Ökld), Manhattan,
Chebyshev , Cosne, Cty Block, Gower , Jaccard gb br uzaklık fonksyonu yardımı le hesaplanır .
2. Uzaklıklar küçükten büyüğe sıralanır , eğtm ver setndek  

 test örneğne en yakın k örnek seçlr .
3. Test örneğ  
  'e en yakın 

 komşu arasında en fazla olan sınıf etket atanır . Buna çoğunluk oylaması  (majorty votng ) denr (Brdge,
2013).
4. Test örneğ  

 çn tahmn edlen sınıf etket döndürülür .
Not: İkl sınıflandırma durumunda (eğer hedef ntelkte k kategor varsa)  
   çft sayı se, çoğunluk sınıfı
seçlrken br eştlk durumu le karşılaşablr . Örneğn; 

 çn sınıfı blnmeyen örneğn en yakın komşuları 2 adet Covd-19 ve 2 adet grp hastası olablr . Algortma
bu gb durumlarda rastgele br seçm yapablr; bunun yerne ağırlıklı oylama  (weghted votng ) veya dğer


Ağırlıklı oylama stratejsnde, sınıfı blnmeyen örnek ( 
  ) le eğtm ver setndek ( X_tran ) her örnek
arasındak uzaklıklar ( 
  ) hesaplandıktan sonra 
   ya da 
   gb ağırlıklar hesaplanır . Aynı sınıfa
at ağırlıkların toplamı bulunur . Hang sınıfın ağırlığı yüksekse o sınıf etket 

'e atanır . Yan bu durumda br sınıf sayıca br dğerne göre fazla olsa ble, 3 Covd-19, 2 grp gb sayıca az
olan sınıfın ağırlığı yüksek olablr ve bu nedenle de o etket seçleblr .
k-NN algortması eğtm versn kullanarak genel/stabl br model oluşturmak yerne, öğrenme şlemn
gerçek zamanlı olarak yapmaktadır . Sınıflandırma veya regresyon şlem çn her sınıfı blnmeyen örnek
geldğnde eğtm ver setne dönerek uzaklıkları hesaplanması ve algortma adımlarının devam ettrlmes
gerekmektedr . Bu nedenle k-NN algortması br tembel öğr enme  (lazy learnng ) algortması olarak da
blnmektedr . Bu, modeln eğtm aşamasında genel br kural set oluşturmak yerne her tahmnleme veya
sınıflandırma şlem çn gerektğnde o spesfk örnek çn öğrenme şlemn gerçekleştrmes anlamına gelr .

## 7.2. k-NN Algortması le Python Uygulaması

Bu çalışmada kullanılan ver set ( dataR2.csv ), UCI Makne Öğrenmes ver deposundan temn edlmştr
(Patrco & Caramelo, 2018): https://archve.cs.uc.edu/ml/datasets/Breast+Cancer+Combra . Meme kanser
olan 64 hasta ve 52 sağlıklı kontrol grubu hastası çn klnk özellkler gözlemlenmş veya ölçülmüştür (T ablo
21). Tümü sayısal olan 10 tahmn sağlayan ntelk ve meme kansernn varlığını (1 le kodlanmış) ya da
yokluğunu (2 le kodlanmış) gösteren kl kategorden oluşan br hedef ntelk ( Classfcaton )
bulunmaktadır . Bu çalışmanın temel amacı; meme kanser çn k-NN algortması le br öngörü (tahmn)
model oluşturmaktır .
Tablo 21: Meme kanser ver setndek ntelkler .
Ntelk Türkçes Ver Tp
Age (years) Yaş (yıl) Sayısal
BMI (kg/m2) VKİ (kg/m2) Sayısal
Glucose (mg/dL) Glkoz (mg/dL) Sayısal
Insuln (µU/mL) İnsüln (µU/mL) Sayısal
HOMA Homeostatk Model Değerlendrmes Sayısal
Leptn (ng/mL) Leptn Hormonu (ng/mL) Sayısal
Adponectn (µg/mL) Adponektn Hormonu (µg/mL) Sayısal
Resstn (ng/mL) Resstn Hormonu (ng/mL) Sayısal
MCP-1(pg/dL) Monost Kemotaktk Proten Sayısal
Classfcaton Hasta ya da sağlıklı olma durumunu gösteren karar
değşkenKategork


### 7.2.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas  ve Sckt-learn  kütüphaneler kullanılmıştır (C. R. Harrs vd., 2020;
McKnney , 2010; Pedregosa vd., 201 1). Ver görselleştrme çn Seaborn  ve matplotlb  kütüphanelernden
faydalanılmıştır (Hunter , 2007; Waskom, 2021). Eğer bu kütüphaneler yüklü değlse Bölüm 3.1’de
açıklandığı gb termnalden kurulmalıdır . Kurulma şlem yapılmışsa öncelkle aşağıdak kod satırları Python


### 7.2.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . dataR2.csv  dosyasını okumak çn
Pandas  kütüphanesnden pd.read_csv()  fonksyonu kullanılmıştır .


### 7.2.3. Ver Ön-şleme

Öncelkle ver setndek karar değşken olan Classfcaton  Türkçeleştrlerek ntelk adı “ Karar ” olarak
değştrlmştr . Dğer sütunların adı da Türkçeleştrleblr; ancak şlemlerde sütun adları yerne ndeks
numaraları kullanılacağından bu çalışmada tümünün değştrlmesne htyaç duyulmamıştır . Ntelk adı
değşklğ öncesnde ve sonrasında .value_counts()  fonksyonu kullanılarak elde edlen ekran görüntülernde
sırasıyla yer verlmştr .


Hedef ntelk olan “Karar” ntelğnn ver tp category  olarak değştrlmştr . Ardından ver setnn özet


Şekl 97: Ver set özet.
Şekl 98’de ver setndek ntelklern ver tpler nceleneblr .


Şekl 98: Ver setndek ntelklern ver tp.


Hedef ntelk harç dğer tüm ntelkler çeren korelasyon ısı hartası aşağıdak kodlar yardımı le
oluşturulmuştur (Şekl 99).


En yüksek Pearson korelasyon katsayısının HOMA  ve Insuln  ntelkler arasında olduğu tespt edlmştr .
HOMA  ve Insuln  ntelkler arasında poztf yönde güçlü doğrusal br lşknn varlığından söz edleblr .


Şekl 99: Ntelklern ısı hartası.
Sckt-learn  kütüphanesnn model_selecton  modülünden tran_test_splt()  fonksyonu kullanılarak eğtm
ve test ver setler oluşturulmuştur . Vernn %70’ eğtm ( egtm ), %30’u se test ver setnde olacak şeklde
(frac = 0.7 ) rastgele ayrılmıştır .


sklearn.pr eprocessng  modülünden MnMaxScaler  mnmum-maksmum normalzasyon yöntem le ver
setler normalze edlmştr . Bunun çn öncelkle scaler .ft_transform() fonksyonu  X_tran ’e uygulanmış
ve eğtm ver setndek tüm ntelkler 0 le 1 arasında olacak şeklde ayarlanmıştır . Bu aşamada test ver set
normalze edlrken scaler  nesnesnn eğtm ver setnden öğrendğ parametreler
scaler .transform() fonksyonu yardımı le X_test ’e uygulanmıştır . Bu uygulamanın sebeb, test verlernn
modeln daha önce görmedğ yen verler olduğunun varsayılmasıdır  (Raschka, 2023). Normalze edlen


### 7.2.4. Modelleme

k-NN modelnn ( knn_model ) oluşturulablmes çn KNeghborsClassfer()  kullanılmıştır . Bunun çn
fonksyonun lk ar gümanı olarak k komşu sayısı ( n_neghbors ) 5 verlmştr . İknc ar güman olarak se
uzaklık fonksyonu ( metrc ) eucldean  (Ökld) seçlmştr . Ardından knn_model  modelnn ft()
fonksyonuna normalze edlen ver set ve eğtm ver setnn hedef ntelğ verlmştr .


### 7.2.5. Performans Değerlendrme

Test ver setndek örnekler çn oluşturulan k-NN model ( knn_model ) tahmnlernn bulunablmes çn
lr_model.pr edct()  fonksyonundan yararlanılablr . Fonksyona test ver setndek tahmn sağlayan
ntelkler ( X_test_n ) verlr .


Modeln test ver setndek tüm örnekler çn mutluluk puanı tahmnler y_tahmn  dzsnde tutulmaktadır .


setndek gerçek meme kanser kararına lşkn değerlern ( y_test ) lk 5 değer aşağıdak kod yardımı le
ekrana yazdırılmıştır .


y_tahmn  ve y_test  yardımı le kontenjans tablosu oluşturulmuş ve bu tablo kullanılarak doğruluk,
duyarlılık, belrleyclk gb çeştl performans değerlendrme ölçütler hesaplanmıştır . “Kanser” sınıfı poztf
sınıf olarak seçlmş olsun. y_tahmn  ve y_test ’n lk k elemanı şu şeklde yorumlanablr:
• Gerçekte “Kanser”, k-NN model de “Kanser” olarak doğru tahmn etmş, dolayısıyla bu br TP’dr ( true
postve /doğru poztf).
• Gerçekte “Sağlıklı”, k-NN model se “Kanser” olarak yanlış tahmn etmş, dolayısıyla bu br FP’dr ( false
postve /yanlış poztf).
Kontenjans tablosu oluşturmak çn en bast yöntem olarak sklearn.metrcs  modülünden
confuson_matrx()  fonksyonu kullanılablr . y_true  parametresne test ver setndek meme kanser kararını
gösteren gerçek değerler ( y_test ), y_pr ed parametresne se k-NN model tahmnler ( y_tahmn ) verlmştr .
labels  parametresne se ver setnn sınıf değerler (kategorler) olması gereken sırada verlmştr . Eğer
labels  parametresne herhang br değer verlmezse sınıf kategorler alfabetk sıraya göre yazdırılacaktır .


Python’da bu yolla elde edlen kontenjans tablosunda sütunlar tahmn değerlern göstermekteyken satırlar
gerçek değerler göstermektedr . Test ver setnde 23 Kanser ve 12 Sağlıklı kategorsne at örnek yer
almaktadır . Sırasıyla; tn=7 (true negatves ), fp=5 (false postves ), fn=4 (false negatves ), tp=19 ( true
postves ) olarak elde edlmştr .
Kontenjans tablosunun görsel açıdan daha y çıktılanması çn yne sklearn.metrcs  çnden
ConfusonMatrxDsplay()  fonksyonu kullanılablr . Bu fonksyona br öncek aşamada oluşturulan
kontenjans tablosu my_conf  ya da bunun yerne y_true = y_test, y_pr ed = y_tahmn  şeklnde parametreler
verleblr . dsplay_labels  parametres de confuson_matrx() fonksyonunun labels  parametresyle benzer


Kontenjans tablosundak tn, tp, fn, fp değerlernn sırasıyla aynı smlerde tanımlanan değşkenlere
atanablmes çn my_cm.ravel()  kullanılablr .


k-NN modelnn test ver set üzerndek performansı ncelendğnde doğruluk değernn %74.29 olarak elde
edldğ görüleblr . Gerçekte Kanser hastası olanlar arasında doğru şeklde Kanser hastası olarak tahmn
edlen hastaların oranı (duyarlılık) %82.61’dr . Gerçekte Sağlıklı breyler arasında doğru şeklde Sağlıklı
olarak tahmn edlen örneklern oranı (belrleyclk) %58.33’ tür. Kanser hastası olarak tahmn edlen tüm
hastalar arasında model tarafından da kanserl olarak doğru tahmn edlenlern oranı (kesnlk) %79.17’dr .
Duyarlılık ve belrleyclğn harmonk ortalaması olan F-Ölçüsü se %80.85’ tr. Özellkle doğruluk le F-
Ölçüsünün ver setnde dengeszlk durumu olduğunda brlkte değerlendrlmes önerlmektedr . F-
Ölçüsünün çoklu-sınıf sınıflandırma (hedef ntelkte kden fazla kategor) olması durumunda kullanılması
tavsye edlmektedr .
Formüller yardımı le hesaplanan yukarıdak ölçütler , sklearn.metrcs ’dek classfcaton_r eport()


Yukarıda elde edlen performans metrkler raporunun lk k satırında hem Kanser hem de Sağlıklı sınıfının
poztf sınıf alınmasıyla elde edlen metrkler bulunmaktadır . Çünkü; duyarlılık, belrleyclk, kesnlk, F-
Ölçüsü gb ölçütlern değer ve yorumu poztf sınıf değştğnde değşmektedr . Support  değer test ver
setnde lgl sınıflara at kaç örneğn mevcut olduğunu göstermektedr . macr o avg  se Sağlıklı ve Kanser çn
ayrı ayrı elde edlen performans ölçütlernn ortalamasıdır (makro ortalama değerler).
Eğer Sağlıklı kategors poztf sınıf olarak alınmak stenrse aşağıdak kod yardımı le benzer hesaplamalar
yapılablr ( labels  parametresnde kategorlern sırası değştrlmştr).


### 7.2.6. En İy k Komşu Sayısının Belrlenmes

En y  
   komşu sayısının belrlenmes çn 2 le 20 arasında 

 değer aşağıdak kodlar yardımı le denenmştr . Örnek olması çn doğruluk ve duyarlılık değerler her br k-
NN model çn hesaplanarak sırasıyla dogruluk  ve duyarllk  lstelernde saklanmıştır . sklearn.metrcs
çndek accuracy_scor e() ve f1_scor e() fonksyonları kullanılmıştır . Yne poztf sınıfa göre yorumlanan
performans metrkler çn average  ve pos_label  parametreler de kullanılablmektedr . precson_scor e(),


 Farklı 
   sayıları le elde edlen doğruluk ve F-Ölçüsü değerler Şekl 100 ve Şekl 101’de verlmştr .
Performans değerlendrme ölçülernden doğruluk, belrleyclk, kesnlk, negatf öngörü değer ve F-Ölçüsü
değerlernn olabldğnce 1’e yakın olması beklenr . Model seçm yapılırken bu noktaya dkkat edlmeldr .
Grafklerdek noktaların daha y okunablmes çn doğruluk ve hata değerler Tablo 22’de yazdırılmış, önce
doğruluk sonra da F-Ölçüsü değerlerne göre büyükten küçüğe sıralanmıştır . En y başarım 
   çn
elde edlmştr; ancak kl sınıflandırma çn 
  ’nın tek sayı alınması tavsyes göz önünde bulundurularak 
  olarak seçlmştr . Model seçmnn de bu şeklde yapılmasıyla gelecek olan yen örnekte 


**Bölüm Özet**

k-En Yakın Komşu Algortması  (k-Near est Neghbor Algorthm, k-NN ), sınıflandırma ve regresyon
problemlernde kullanılan ve uygulaması kolay br danışmanlı öğrenme algortmasıdır . “Bana arkadaşını
söyle, sana km olduğunu söyleyeym ” atasözü le özdeştrlen k-NN, lteratürde sıklıkla terch edlen br
algortmadır . Ver noktaları arasındak uzaklığı ölçmek çn çeştl uzaklık fonksyonları kullanılablr; ancak
bu noktada ntelklern ver tpne dkkat edlmeldr . k-NN algortmasında kullanılacak komşu sayısı olan  


 ’nın seçm modeln performansını etkler . Bu nedenle, nha performansa karar verlrken farklı  
   komşu
sayıları çn model oluşturulması ve bu modellern performanslarının değerlendrlmes tavsye edlr .
Bu bölümde temel teork blgler verldkten sonra k-NN algortmasının Python dlnde meme kanser teşhs
uygulaması ele alınmış, modeln performansının değerlendrlmes çn kontenjans tablosu  (contngency
table ) oluşturulmuş ve bu bağlamda performans değerlendrme ölçütler hesaplanmıştır . İkl sınıflandırmada
kullanılan performans değerlendrme ölçütlernn nasıl hesaplanacağı detaylı br şeklde açıklanmıştır .
NumPy , Pandas , Seaborn , Matplotlb  ve Sckt-learn  kütüphaneler kullanılarak gerçekleştrlen bu bölüm,
okuyuculara hem teork hem de pratk açıdan k-NN algortmasını anlama ve kullanma konusunda temel br
deneym sunmaktadır . Bu kazanılan deneymn pekştrlmes çn okuyuculara farklı ver setler üzernde
çalışması  önerlmektedr .


**Kaynakça**

Balaban, M. E., & Kartal, E. (2018). Ver Madenclğ ve Makne Öğr enmes T emel Algortmaları ve R Dl le
Uygulamaları  (2. bs). Çağlayan Ktabev.
Brdge, D. (2013). Classfcaton: K Near est Neghbours . www .cs.ucc.e/~dgb/courses/ta/notes/handout4.pdf
Cha, S. (2007). Comprehensve Survey on Dstance/Smlarty Measures between Probablty Densty
Functons | BbSonomy . Internatonal Journal of Mathematcal Models and Methods n Appled Scences ,
1(4), 300-307.
Cho, S.-S., Cha, S.-H., & Tappert, C. C. (2010). A Survey of Bnary Smlarty and Dstance Measures.
Systemcs, Cybernetcs and Informatcs , 8(1), 43-48.
Dekhtyar , A. (2009). CSC 466: Knowledge Dscovery fr om Data—Dstance/Smlarty Measur es.
http://users.csc.calpoly .edu/~dekhtyar/560-Fall2009/lectures/lec09.466.pdf
Gan, G. (201 1). Data Clusterng n C++: An Object-Orented Appr oach . Chapman & Hall/CRC PressCRC
Press.
Han, J., & Kamber , M. (2006). Data Mnng: Concepts and T echnques  (2. bs). Mor gan Kaufmann
Publshers.
Harrngton, P . (2012). Machne Learnng n Acton  (1. bs). Mannng Publcatons Co.
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
Hunter , J. D. (2007). Matplotlb: A 2D graphcs envronment. Computng n Scence & Engneerng , 9(3), 90-
95. https://do.or g/10.1 109/MCSE.2007.55
Kartal, E. (2015). Sınıflandırmaya Dayalı Makne Öğr enmes T eknkler V e Kar dyolojk Rsk
Değerlendrmesne İlşkn Br Uygulama  [Doktora Tez]. İstanbul Ünverstes, Fen Blmler Ensttüsü.
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Patrco, Mguel, Perera, Jos, Crsstomo, Joana, Matafome, Paulo, Sea, Raquel, & Caramelo, F . (2018).


Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Raschka, S. (2023). Why do we need to r e-use tranng parameters to transform test data?  Sebastan
Raschka, PhD. https://sebastanraschka.com/faq/docs/scale-tranng-test.html
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021


**Ünte Soruları**

Soru-1 :
Aşağıdaklerden hangs k-En Yakın Komşu (k-NN) Algortması le lşkl kavramlardan br değldr ?
(Çoktan Seçmel)
(A) Uzaklık ( dstance )
(B) Ağırlıklı oylama ( weghted votng )
(C) Çoğunluk oylaması ( majorty votng )
(D) Karar ağacı ( decson tr ee)
Tembel öğrenme ( lazy learnng )
Cevap-1 :
Karar ağacı ( decson tr ee)
Soru-2 :
Aşağıdaklerden hangs tembel öğrenmey ( lazy learnng ) açıklar?
(Çoktan Seçmel)
(A) Tembel öğrenme model eğtm versn kullanarak genel/stabl br model oluşturmak yerne, öğrenme
şlemn gerçek zamanlı olarak sürdürür .
(B) Tembel öğrenme model, test versn kullanarak genel/stabl br model oluşturmak yerne öğrenme
şlemn gerçek zamanlı olarak sürdürür .
(C) Tembel öğrenme model yen br örnek çn hçbr zaman doğru tahmnde/öngörüde bulunamaz.
(D) Tembel öğrenme model, eğtm ver set çeştlendrlmeden doğru karar veremez.
Tembel öğrenme model, model karmaşıklığını artırmadan öğrenme şlemn sürdürmez.


Tembel öğrenme model eğtm versn kullanarak genel/stabl br model oluşturmak yerne, öğrenme
şlemn gerçek zamanlı olarak sürdürür .
Soru-3 :
Aşağıdaklerden hangs k-NN algortması hakkında yanlış  br blgdr?
(Çoktan Seçmel)
(A) Hem sınıflandırma hem regresyon problemlernn çözümünde kullanılablr .
(B) k-NN algortmasının kullanıldığı ver setnde hedef ntelk bulunmak zorundadır .
(C) k-NN algortmasının kullanıldığı ver setnde hedef ntelk hem sayısal hem de kategork olablr .
(D) k-NN algortması yalnızca kl sınıflandırma problemlernn çözümünde kullanılır .
k-NN algortmasında Ökld uzaklığı seçldğnde, ver setnde tahmn sağlayan ntelkler yalnızca sayısal
halde bulunablr .
Cevap-3 :
k-NN algortması yalnızca kl sınıflandırma problemlernn çözümünde kullanılır .
Soru-4 :
k-NN le yapılan sınıflandırma şlem sonucunda sınıfı blnmeyen örneğe en yakın komşu ver noktalarının
hedef ntelkler “Yüksek, Yüksek, Düşük, Düşük, Yüksek, Çok Yüksek, Çok Düşük, Orta, Orta” olarak
tespt edlmştr . Eğer çoğunluk oylaması  kullanılıyorsa yen örneğn sınıfı olarak aşağıdaklerden hangs
atanır?
(Çoktan Seçmel)
(A) Çok Düşük
(B) Düşük
(C) Orta
(D) Yüksek
Çok Yüksek
Cevap-4 :
Yüksek
Soru-5 :
k-NN le yapılan sınıflandırma şlem sonucunda sınıfı blnmeyen örneğe en yakın komşu ver noktalarının
hedef ntelkler “Syah, Syah, Syah, Beyaz, Beyaz, Kırmızı, Kırmızı” olarak tespt edlmştr . Eğer ağırlıklı
oylama  kullanılıyorsa yen örneğn sınıfı olarak aşağıdaklerden hangs atanır?
(Çoktan Seçmel)


(B) Beyaz
(C) Kırmızı
(D) Beyaz ve Kırmızı
(E) Verlen blgler ağırlıklı oylama le karar vermek çn yeterszdr .
Cevap-5 :
Verlen blgler ağırlıklı oylama le karar vermek çn yeterszdr .
Soru-6 :
Mnmum-maksmum ver normalzasyon yöntemn uygulamak çn MnMaxScaler ’n scaler  adlı br örneğ
oluşturuluyor . Ver normalzasyonunda aşağıdak durumlardan hangsnn terch edlmes dğerlerne göre
daha uygun olarak görülmektedr?
(Çoktan Seçmel)
(A)
(B)
(C)
(D)
Cevap-6 :
Soru-7 :
Br kl sınıflandırma problemnde aşağıdak k değerlernden hangsnn seçm daha uygun olur?
(Çoktan Seçmel)


(B) 4
(C) 5
(D) 6
8
Cevap-7 :
5
Soru-8 :
Aşağıdaklerden hangs br k-NN modelnn performansını değerlendreblmek çn kullanılan
sklearn.metrcs  çndek fonksyonlardan br değldr ?
(Çoktan Seçmel)
(A) accuracy_score()
(B) recall_score()
(C) slhouette_score()
(D) precson_score()
f1_score()
Cevap-8 :
slhouette_score()
Soru-9 :
Aşağıdaklerden hangs k-NN algortmasının br dezavantajı  olarak görüleblr?
(Çoktan Seçmel)
(A) k komşu sayısı seçm
(B) Uzaklık fonksyonu seçm
(C) Ağırlıklı oylama yapılması
(D) Çoğunluk oylama yapılması
(E) Büyük ver setlernde hesaplama malyet
Cevap-9 :
Büyük ver setlernde hesaplama malyet
Soru-10 :
Aşağıda doğruluk ve F-Ölçüsü değerler verlen farklı k-NN algortması modellernden hangsnn seçlmes


(Çoktan Seçmel)
(A) Model A: Doğruluk=0.5, F-Ölçüsü=0.6
(B) Model B: Doğruluk=0.9, F-Ölçüsü=0.8
(C) Model C: Doğruluk=0.9, F-Ölçüsü=0.2
(D) Model D: Doğruluk=0.7, F-Ölçüsü=0.7
Model E: Doğruluk=0.4, F-Ölçüsü=0.3
Cevap-10 :


# 8. Naive Bayes Algoritması


**Özlü Söz**

Gelecek belrszdr , belrszlğ azaltmak önemldr .
M. Erdal Balaban , İstanbul Ünverstes İşletme Fakültes, Sayısal Yöntemler Anablm Dalı Emekl Öğr etm
Üyes


**Kazanımlar**

1.   Bayes Teorem’nn temel prensplern anlar .
2.   Nave Bayes sınıflandırıcının çalışma prensbn kavrar , özellkle bağımsızlık varsayımının ne anlama
geldğn anlar .
3.   Nave Bayes sınıflandırıcı le öngörü model oluşturablr .
4.   Tahmn sağlayan ntelklern kategork ve nümerk olma durumuna göre Nave Bayes sınıflandırıcı çn
gerekl olan olasılık değerlern hesaplayablr .
5.   Nave Bayes sınıflandırıcının performansını değerlendreblr , kontenjans tablosu yadımı le modeln
doğruluk, duyarlılık, kesnlk ve F-Ölçüsü gb performans ölçütlern hesaplayablr .
6.   Tabakalı 5-kat çapraz geçerleme ( stratfed 5-fold cr oss valdaton ) yöntemnn teork temellern kavrar ,
Python dlnde Nave Bayes sınıflandırıcı le uygulama gerçekleştreblr .
7.   Farklı ver setler üzernde Nave Bayes sınıflandırıcının kullanımına yönelk pratk deneym kazanır .


**Brlkte Düşünelm**

1.   Bayes Teorem nedr?
2.   Nave Bayes sınıflandırıcının temel bağımsızlık varsayımı ( ndependence assumpton ) nedr?
3.   Nave Bayes sınıflandırıcı le br öngörü model oluştururken dkkat edlmes gereken temel adımlar
nelerdr?
4.   Tahmn sağlayan ntelklern kategork ve nümerk olma durumuna göre Nave Bayes sınıflandırıcı çn
olasılık değerler nasıl hesaplanır? Kontenjans tablosu kullanarak modeln doğruluk, duyarlılık, kesnlk ve F-


5.   Tabakalı 5-kat çapraz geçerleme yöntem model değerlendrmes açısından hang avantajlara sahptr?
6.   Python dlnde Nave Bayes sınıflandırıcı le tabakalı 5-kat çapraz geçerleme nasıl uygulanır?


**Başlamadan Önce**

Bu bölümde Nave Bayes sınıflandırıcı  le lgl temel kavramlar açıklanacaktır . Nave Bayes
sınıflandırıcının temeln oluşturan Bayes Teorem’ne odaklanılarak, algortmanın neden “naïve” olarak
adlandırıldığı açıklanmıştır . Bu adlandırma, algortmanın çalışma prensplerndek bastlk ve özellkle
tahmn sağlayan ntelkler arasındak bağımsızlık varsayımının etksyle lşkldr . Nave Bayes
sınıflandırıcının gerçek dünya uygulamalarındak rolünün daha y anlaşılması çn bölüm uygulamasında br
hastanın Covd-19/Grp öngörüsü (tahmn) yapılacaktır .
Bölüm kapsamında Python dlnde Nave Bayes sınıflandırıcının müşterlern banka vadel mevduatına abone
olup olmayacağını tahmn etme konusunda nasıl kullanılableceğ ncelenmştr . Bu uygulamada Nave Bayes
sınıflandırıcının oluşturulması ve modeln performansını değerlendrmek çn kontenjans tablosu
kullanılmıştır . Performans değerlendrme ölçütler üzernde durarak, modeln performans değerlendrme
ölçütlernn hesaplama adımları ayrıntılı br şeklde sunulmaktadır .
Ktabın knc bölümünde de ele alınan çapraz geçerleme ( cross-valdaton ), br danışmanlı öğrenme
modelnn genel performansını daha güvenlr br şeklde değerlendrmek çn kullanılan öneml br teknktr .
Son olarak Nave Bayes sınıflandırıcı le tabakalı 5-kat çapraz geçerleme yöntemnn teork temeller
açıklanmıştır ve bu yöntemn Python dlnde nasıl uygulanacağı gösterlmştr .
Öncek bölümlerde de kullanılan NumPy , Pandas ve Sckt-learn  kütüphanelernden ve Nave Bayes
sınıflandırıcı model çn mxed_nave_bayes  kütüphanesnden faydalanılmıştır . Bu bölüm hem teork hem de
pratk açıdan okuyuculara Nave Bayes sınıflandırıcıyı anlamaları ve kullanmaları açısından temel br
deneym sunmaktadır . Bu bölümde kazanılan deneymn pekştrleblmes çn okuyuculara, kamuya açık ya
da uzmanlık alanlarına göre seçecekler farklı ver setler üzernde çalışmaları önerlmektedr .


## 8.1. Nave Bayes Sınıflandırıcı

Nave Bayes, statstksel br sınıflandırma ( classfcaton ) algortmasıdır ve özellkle metn madenclğ ve
doğal dl şleme gb yüksek boyutlu veryle çalışılan alanlarda yaygın olarak kullanılır . Algortmanın temel
Bayes Teorem'ne dayanır . Bayes Teorem, br olayın gerçekleşmş olma olasılığını, olayın öncesnde blnen
başka br olayın gerçekleşme olasılığı üzernden hesaplar . Temel formülü aşağıdak gbdr:

  • 

: B koşulu altında A'nın olasılığı. Br başka fade le B’nn olduğu blnyorsa A’nın gerçekleşme olasılığı.
•  

: A koşulu altında B'nn olasılığı. Br başka fade le A’nın olduğu blnyorsa B’nn gerçekleşme olasılığı.


Nave Bayes sınıflandırıcı adındak “nave” (saf, bast, naf), bu algortmanın sınıflandırma çn kullanılan
tahmn sağlayan ntelkler arasında bağımsızlık varsayımı  (ndependence assumpton ) yapması neden le
verlmştr . Nave Bayes sınıflandırıcı le koşullu olasılıklar hesaplanırken bağımsız değşkenler arasında
olasılık hesabını etkleyen lşknn olmadığı varsayılmaktadır .
Nave Bayes yerne doğrudan Bayes Sınıflandırıcının ( Full Bayes Classfer ) kullanılması durumunda,
sınıflandırılacak yen örneğe at tahmn sağlayan tüm ntelklere (bağımsız değşkenlere) tam olarak
benzeyen tüm kayıtları bulmaya odaklanılır (Shmuel vd., 2018). Fakat bu noktada tahmn sağlayan
ntelklern sayısı arttıkça, sınıfı bulunmak stenen örneklern çoğunda tam eşleşme sağlanamayacaktır .
Örneğn ele alınacak örneklem çnde aşağıdak örnek le brebr özellk gösterenler bulablmek ve bu yolla
müşternn kampanyaya onay ya da ret verme olasılığını hesaplamak oldukça zor görünmektedr .
• Son tatlnde yurtdışına br seyahat gerçekleştrmş,
• Öncek yıl çnde spor etknlklerne katılım sağlamış,
• Günlük spor aktvtelerne düzenl olarak zaman ayıran,
• En son okuduğu ktap br blm kur gu romanı olan,
• Sosyal medyada haftada br kez etkleşmde bulunan,
• Hobler arasında yemek pşrme ve yen tarfler deneme yer alan,
• Meslek olarak teknoloj sektöründe çalışan br yazılım mühends,
• Evcl hayvan olarak br ked besleyen,
• En sevdğ müzk türü rock olan,
• Gönüllü olarak yer aldığı br sosyal sorumluluk projes bulunan,

Nave Bayes algortması le çalışılırken Bayes Teorem’nde olduğu gb sıklıkla koşullu olasılık  (condtonal
probablty ) hesaplamalarından faydalanılmaktadır . Örneğn br hastaneye yaşı 32, öksürüğü olmayan, ateş
olmayan ve koku kaybı belrtler gösteren br hasta gelmş olsun. Bu hastanın Covd-19 ya da grp olduğuna
karar verlmeye çalışılsın. Nave Bayes sınıflandırıcı açısından bu durum formüle edlecek olursa;  
  gb özellkler (tahmn sağlayan ntelkler/bağımsız değşkenler) blnen br örnek
geldğnde amaç bu örneğn verlen 
   sınıflarına at olma olasılığını 
 hesaplamak olacaktır (Shmuel vd., 2018). 
   adet farklı sınıfı çeren 

  adet ntelk, 
   adet örnekten oluşan br 
   ver set göz önünde
bulundurulduğunda, br 
   örneğnn sınıfı Nave Bayes sınıflandırıcı le belrlenmek stenrse 

 olasılıkları hesaplanır (Özkan, 2008).

  Nave Bayes çn kullanılan 
   koşullu olasılıklarının
hesaplanma bçm ncelenrse, yukarıdak örnekte bahsedlen “br hastaneye yaşı 32, öksürüğü olan, ateş


cevap bulmak çn koşullu olasılık fadesnn tersne çevrldğ görüleblr . Yan, 
   termnn
hesaplanablmes çn 

 koşullu olasılıklarının hesaplanması gerekr . Bu yen durumda, “eğer hastanın grp ya da Covd-19 olduğu
blnyorsa, yaşının 32 olma ve öksürüğünün olma ve ateşnn olma ve burun akıntısının olma” olasılığının
hesaplanması gerekecektr . Nave Bayes bağımsızlık varsayımından (örneğn; hastanın yaşının 32 olması
olasılığı, öksürüğünün olması olayından bağımsızdır) bu term aşağıdak gb kolaylıkla
hesaplanablmektedr .


 tüm sınıflar çn eşt olacağından sınıfı blnmeyen örneğn sınıfını bulurken kesrn sadece pay kısmını
hesaplamak ve karşılaştırmak yeterl olmaktadır .


Olasılığı yüksek çıkan sınıf değer, yen örneğn sınıfı olarak atanır . Bu, en büyük sonrasal sınıflandırma
(maxmum a posteror classfcaton ) yöntem olarak blnmektedr .
Ver setne Nave Bayes sınıflandırıcısı uygulanırken kategork ntelkler çn koşullu olasılıklar kolayca
hesaplanmaktadır . Ntelklern ver tpnn sürekl olması durumunda se genel kabul sürekl değerlern
normal dağılıma (Gauss dağılımına) uygun dağıldığıdır (Fern, 2012; Han & Kamber , 2006; John & Langley ,
1995; Öğüdücü, 2023; Özkan, 2008). Bu yolla,  
   ortalama ve 

 standart sapmaya sahp br sürekl ntelğn, normal dağılım çn olasılık yoğunluk fonksyonu ( probablty
densty functon ) aşağıdak gb hesaplanır (Fern, 2012; John & Langley , 1995):


Tam Bayes ( Full Bayes ) sınıflandırıcı ntelkler arasındak bağımlılıkları dkkate alır ve daha doğru sonuçlar
üreteblr; ancak ortak (jont) olasılık dağılımını tahmn etmek büyük mktarda ver gerektrr ve bu da
hesaplama açısından malyetl olablr . Öte yandan Nave Bayes sınıflandırıcı, sınıf etketler göz önüne
alındığında tüm ntelklern koşullu olarak brbrnden bağımsız olduğunu varsayar . Bu se br ntelğn


ortak olasılık dağılımının hesaplanmasını bastleştrr ve Nave Bayes sınıflandırıcıyı tam Bayes
sınıflandırıcıdan daha hızlı ve verml hale getrr; ancak bağımsızlık varsayımı her durumda doğru
olmayablr ve bu da daha düşük doğruluğa yol açablr .
Örnek:  Aşağıdak tabloda 10 adet hastanın ateş, öksürük, burun akıntısı ve yaş blgsne göre “Covd-19” ya
da “Grp” olma durumunu gösteren ver yer almaktadır . Tablodak verden faydalanarak yaşı 32, ateş olan,
öksürüğü olan ve burun akıntısı olan br hastanın sınıfını Nave Bayes sınıflandırıcı le hesaplayınız.
Hasta  Ateş  Öksürük  Burun Akıntısı  Yaş  Durum
1  VAR  VAR  YOK 25  Covd-19
2  VAR  VAR  VAR 30  Covd-19
3  YOK  YOK  VAR 22  Covd-19
4  VAR  YOK  YOK 35  Covd-19
5  YOK  YOK  YOK 28  Grp
6  VAR  VAR  VAR 40  Grp
7  YOK  VAR  YOK 21  Grp
8  YOK  VAR  VAR 32  Grp
9  VAR  VAR  YOK 27  Grp
10  YOK  YOK  VAR 38  Grp

Çözüm:  Hastanın sınıfını Nave Bayes sınıflandırıcı le belrleyeblmek çn;  
  sınıfları çn ayrı ayrı 

 hesaplanmalıdır . Öncelkle öncül olasılık değerler aşağıdak gb hesaplanır:


 Sonrasında se Nave Bayes sınıflandırıcının bağımsızlık varsayımından faydalanılarak 

 olasılıkları hesaplanır:


Bu sebeple; yaşı 32, ateş olan, öksürüğü olan, burun akıntısı olan br hasta Covd-19 sınıfına attr denr .

## 8.2. Nave Bayes Sınıflandırıcı le Python Uygulaması

Bu çalışmada kullanılan ver set ( bank-full.csv ), UCI Makne Öğrenmes ver deposundan temn edlmştr
(Moro vd., 2012): https://archve.cs.uc.edu/dataset/222/bank+marketng  Ver set, Portekzl br bankacılık
kurumunun doğrudan pazarlama kampanyaları le lgldr (T ablo 23). Pazarlama kampanyaları telefon
görüşmelerne dayanmaktadır . Ürüne (banka vadel mevduatı) abone olunup olunmayacağına (“evet” veya
“hayır”) erşmek çn genellkle aynı müşteryle brden fazla temas kurulması gerekmştr .
Bu çalışmanın temel amacı; müşterlern banka vadel mevduatına abone olup olmayacağını öngörmektr .
Ver setnde toplamda 4521 1 adet gözlem, 17 adet ntelk bulunmaktadır . Bunlardan sonuncusu, müştern
banka vadel mevduatına abone olup olmayacağını gösteren hedef ntelktr ( y). “evet” ve “hayır” şeklnde k
adet kategors bulunmaktadır . Dolayısıyla kl sınıflandırma durumu söz konusudur .
Tablo 23: Banka müşterlerne at ver setndek ntelkler .
Ntelk Türkçes Ver Tp
age (years) Yaş Nümerk
job Meslek Kategork
martal Meden durum Kategork
educaton Eğtm sevyes Kategork
default Temerrüde düşmüş kreds var mı? Kategork
balance Yıllık ortalama bakye (A vro) Nümerk
housng Konut kreds var mı? Kategork
loan Breysel kreds var mı? Kategork
contact Müşter le letşm türü Kategork
day Ayın müşter le son temas günü Nümerk
month Yılın müşter le son temas ayı Kategork
duraton Müşter le letşm son temas süres (sn.) Nümerk
campagn Bu kampanya sırasında müşter çn gerçekleştrlen
temas sayısıNümerk
pdays Müşteryle öncek br kampanyadan en son letşme
geçldkten sonra geçen gün sayısıNümerk
prevous Bu kampanyadan önce ve bu müşter çn


poutcome Öncek pazarlama kampanyasının sonucu Kategork
y Müşter vadel br mevduata abone oldu mu? Kategork


### 8.2.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas , Sckt-learn  ve mxed_nave_bayes  kütüphaneler kullanılmıştır (C. R. Harrs
vd., 2020; Karm, 2022; McKnney , 2010; Pedregosa vd., 201 1). Sckt-learn kütüphanes yalnızca nümerk
ver çn ( GaussanNB ) ve yalnızca kategork ver çn ( CategorcalNB ) fonksyon seçenekler sunmaktadır;
ancak bu çalışmadak ver setnde olduğu gb aynı anda hem kategork hem de nümerk ntelkler br arada
bulunablr . mxed_nave_bayes söz edlen bu k farklı tür grubun entegrasyonunu, verye br arada
uygulanablmesn sağlar . Eğer bu kütüphaneler yüklü değlse Bölüm 3.1’de açıklandığı gb termnalden
kurulmalıdır . Kurulma şlem yapılmışsa öncelkle aşağıdak kod satırları Python koduna dahl edlmeldr .


### 8.2.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . bank-full.csv  dosyasını okumak çn
Pandas  kütüphanesnden pd.read_csv()  fonksyonu kullanılmıştır . bank-full.csv dosyasının Python kodunun
kaydedldğ klasörde olması gerektğ unutulmamalıdır .


### 8.2.3. Ver Ön-şleme

Ver set okunduktan sonra hang ntelklern kategork, hanglernn nümerk (sürekl/ayrık) olduğu kontrol
edlmştr .


Aşağıda solda verlen lk ekran görüntüsünde Tablo 23’ te kategork olarak adlandırılan ntelklern “object”
bçmnde okunduğu görülecektr . Ardından mxedNB()  fonksyonunu kullanablmek çn kategork ntelkler
LabelEnceder()  yardımı le ayrık sayısal hale dönüştürülmüştür . Dönüşüm sonrasında tüm ntelklern ver
tp aşağıda sağda verlen ekran görüntüsünden görüleblr . Ayrıca döngünün her br adımında kategork
ntelklern ndeks numaraları kategorkNtelkler  lstesne atanmıştır . Döngü bttkten sonra hedef ntelk bu
lsteden çıkarılmıştır . kategorkNtelkler  lstes mxedNB()  fonksyonunun br ar gümanı olarak


Sckt-learn  kütüphanesnn model_selecton  modülünden tran_test_splt()  fonksyonu kullanılarak eğtm ve
test ver setler oluşturulmuştur . Vernn %70’ eğtm ( egtm ), %30’u se test ver setnde olacak şeklde
(frac = 0.7 ) kye ayırma yöntem le rastgele ayrılmıştır .


### 8.2.4. Modelleme

Nave Bayes sınıflandırıcı modelnn ( nb_model ) oluşturulablmes çn MxedNB()  kullanılmıştır . Bunun
çn ver setndek kategork ntelklern ndeksn çeren kategorkNtelkler  lstes verlmştr
(categorcal_featur es). Ardından nb_model  modelnn ft() fonksyonuna eğtm ver set ve eğtm ver


### 8.2.5. Performans Değerlendrme

Nave Bayes sınıflandırıcı modelnn performansının değerlendrleblmes çn
nb_model.pr edct() fonksyonundan faydalanılmıştır . Modeln tahmnler ve test ver setnn hedef ntelğ
görüntülenrse LabelEncoder()  le sayısal hale dönüştürüldüğü bçmyle yer almakta oldukları görüleblr .
İlgl değerler kategork hale (orjnal halne) döndürmek çn label_encoder .nverse_transform()
kullanılmıştır . Bu adım elde edlecek olan kontenjans tablosunun daha y yorumlanablmesn sağlamak
amacıyla yapılmıştır .


Kontenjans tablosu sklearn.metrcs  çndek confuson_matrx()  le elde edlmştr . “yes”, yan evet sınıfı
poztf sınıf olarak kabul edlmştr . Ardından, kontenjans tablosunun görsel açıdan daha y bçmde


Kontenjans tablosundak tn, tp, fn, fp değerlernn sırasıyla aynı smlerde tanımlanan değşkenlere
atanablmes çn my_cm.ravel()  kullanılmıştır .


Bu blgler ışığında, br öncek bölümde k-NN model performansı değerlendrlrken formüller yardımı le


classfcaton_r eport()  le en temel performans değerlendrme ölçütler elde edlmştr .


Yukarıda elde edlen performans metrkler raporundan Nave Bayes Sınıflandırıcının doğruluğu %87 elde
edlmştr . Raporun lk k satırında hem no hem de yes sınıfının poztf sınıf alınmasıyla elde edlen metrkler
bulunmaktadır . Duyarlılık, belrleyclk, kesnlk, F-Ölçüsü gb ölçütlern değer ve yorumunun poztf sınıf
değştğnde değşmekte olduğundan hang sınıfın poztf sınıf seçldğ ve yorumlandığı oldukça önemldr .
• yes sınıfının poztf sınıf seçlmş olması durumunda ; gerçekte banka vadel mevduatına abone olan
müşterler arasında, modeln doğru şeklde öngördüğü ve gerçekte de banka vadel mevduatına abone olan
müşterlern oranı %53’ tür (duyarlılık/ recall ).
• no sınıfının poztf sınıf seçlmş olması durumunda ; gerçekte banka vadel mevduatına abone olmayan
müşterler arasında, modeln doğru şeklde öngördüğü ve gerçekte de banka vadel mevduatına abone
olmayan müşterlern oranı se %92’ tür (duyarlılık/ recall ).
Sınıfa bağlı kesnlk ve F-Ölçüsü değerler de yukarıdaklere benzer şeklde yorumlanablr .
Hem gerçek hem de tahmn edlen yes sınıfına at müşterler ele alındığında, aslında modeln yes sınıfına at
gözlemler daha az başarı le tahmn ettğ görüleblr . Bunun br neden olarak ver setnde 39922 adet no,
5289 adet se yes sınıfına at örneğn yer alması olablr . Yan modeln eğtm ve testnde no sınıfına at
örneklern sayısı, yes sınıfına at örneklern sayısının yaklaşık 8 katıdır . Model no sınıfına at daha çok örnek
görmüştür ve bu nedenle yes sınıfına at örnekler daha az başarı le tahmn etmes çok şaşırtıcı değldr . İşte
özellkle bu gb sınıf dengeszlğnn olduğu durumlarda her ne kadar doğruluk %87 elde edlmşse de F-
Ölçüsü model performansını belrlemede daha etkldr . yes sınıfının poztf seçlmes durumunda F-Ölçüsü
%49 çıkmıştır . Oysa, poztf sınıfın no seçlmes durumunda F-Ölçüsü %93’ tür. Dolayısıyla sınıflandırıcının
nha performans değernn belrleneblmesnde makro ortalama ( macr o averagng ) performans değerler
etkl olablr . Yan doğruluk %87, duyarlılık %72, kesnlk %70 ve F-Ölçüsü %71 alınablr .

### 8.2.6. Tabakalı 5-kat Tabakalı Çapraz Geçerleme Yöntem le Performansın

Değerlendrlmes
Bu bölüme kadar gerek k-NN algortmasının gerekse Nave Bayes sınıflandırıcının performans
değerlendrmesnde en temel yöntem olarak blnen kye ayırma ( hold-out ) yöntem kullanılmıştır . Bu
bölümde başka br alternatf yol olarak Nave Bayes sınıflandırıcı le tabakalı 5-kat çapraz geçerleme
(stratfed k-fold cr oss-valdaton ) yöntem kullanılarak performans değerlendrmes gerçekleştrlmştr
(teork blg çn bknz. Bölüm 2.7.1).
Tabakalı çapraz geçerlemenn gerçekleştrleblmes çn sklearn.model_selecton  modülündek
StratfedKFold()  fonksyonu kullanılmıştır . n_splts  kaç kat çapraz geçerleme yapılacağını/kaç parçanın


gösteren parametrelerdr . Bu blgler yardımı le cv nesnes oluşturulmuştur . Ardından for döngüsü çnde
eğtm ve testte kullanılacak örneklern ndeks değerler aşağıdak gb yazdırılmıştır . cv.splt()  sırasıyla
tahmn sağlayan ntelkler ( X) le hedef ntelğ ( y) almaktadır . Orjnal ver set brbrne olabldğnce eşt
sayıda 5 parçaya ayrılmaktadır . Her parçanın br test, dğer dördü se eğtm ver setnn oluşturulması çn
kullanılmaktadır . for döngüsünde tran_ndex  ve test_ndex  her br terasyonda sırasıyla eğtm ve test ver
setlernde yer alacak gözlemlern ndeks blgsn tutmaktadır .


Örneğn lk terasyonda 0, 1, 2 …. 45208, 45209 ve 45210 ndeks numaralı örnekler eğtm ver setnde, 6,
12, 28, …, 45199, 45204 ve 45205 ndeks numaralı örnekler se test ver setnde yer alacaktır . Aşağıda 1., 2.
…, 5. terasyona at blgler sırasıyla verlmştr .


5 farklı terasyon olacağından, 5 defa da performans değerlendrme ölçütler yenden hesaplanacaktır
(Örneğn 5 farklı doğruluk, 5 farklı hata, 5 farklı duyarlılık gb). Bu örnek çn doğruluk ve F-Ölçüsünün
hesaplanmasına karar verlmştr . Dolayısıyla doğruluk ve F-Ölçüsü metrklernn her terasyonda
hesaplanacak değerlern tutablmek çn dogruluk  ve F1 adında k lste tanımlanmıştır . Sonrasında cv
nesnes yukarıda detayları verldğ şeklde tanımlanarak for döngüsü yapılandırılmıştır . for döngüsünün her
br terasyonunda X_tran, X_test, y_tran  ve y_test  değşkenler yapılandırılmaktadır . Ardından Nave
Bayes sınıflandırıcı model kurulmakta ( nb_model ), model tahmnler elde edlmekte ( y_tahmn ),
sınıflandırma raporundan ( my_r eport ) doğruluk ve F-Ölçüsü değerler çeklerek sırasıyla dogruluk  ve F1


Doğruluk ve F-Ölçüsü değerler aşağıdak gb elde edlmektedr . Örneğn brnc terasyonda doğruluk 0.878,
F-Ölçüsü se 0.502’dr .


5-kat çapraz geçerlemenn nha performans değerlernn elde edlmes çn doğruluk ve F-Ölçüsü
değerlernn her terasyondak değerlernn ortalaması alınır . Sonuçta Nave Bayes sınıflandırıcının doğruluğu


**Bölüm Özet**

Nave Bayes sınıflandırıcı  Bayes Teorem’ne dayanan br danışmanlı öğrenme algortmasıdır . Algortmanın
“naïve ” (saf, bast) olarak adlandırılmasının neden, tahmn sağlayan ntelkler arasındak bağımsızlık
varsayımıdır ( ndependence assumpton ). Sınıflandırıcının çalışma prensb br hastanın Covd-19/Grp
öngörüsü üzernden anlatılmıştır .
Sonrasında Nave Bayes sınıflandırıcının Python dlnde müşterlern banka vadel mevduatına abone olup
olmayacağı uygulaması ele alınmış, modeln performansının değerlendrlmes çn kontenjans tablosu
(contngency table ) oluşturulmuş ve bu bağlamda performans değerlendrme ölçütler hesaplanmıştır . Ayrıca,
yne Nave Bayes sınıflandırıcı le tabakalı 5-kat çapraz geçerleme  (stratfed k-fold cr oss-valdaton )
performans değerlendrme yöntemnn Python’dak uygulaması açıklanmıştır (teork blg çn bknz. Bölüm
2.7.1). Bu bölüm, okuyuculara hem teork hem de pratk açıdan Nave Bayes sınıflandırıcıyı anlama ve
kullanma konusunda temel br deneym sunmaktadır . Bu kazanılan deneymn pekştrlmes çn okuyuculara
farklı ver setler üzernde çalışması  önerlmektedr .


**Kaynakça**

Fern, X. Z. (2012). CS434 Bayes and Naïve Bayes Classfers .
https://web.engr .oregonstate.edu/~xfern/classes/cs434-18/bayes-classfer -8.pdf
Han, J., & Kamber , M. (2006). Data Mnng: Concepts and T echnques  (2. bs). Mor gan Kaufmann
Publshers.
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
John, G. H., & Langley , P. (1995). Estmatng contnuous dstrbutons n Bayesan classfers. Proceedngs of
the Eleventh confer ence on Uncertanty n artfcal ntellgence , 338-345.
Karm, R. bn. (2022). mxed-nave-bayes: Categorcal and Gaussan Nave Bayes  (0.0.3) [Python; OS
Independent]. https://gthub.com/remykarem/mxed-nave-bayes
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Moro, S., Rta, P ., & Cortez, P . (2012). Bank Marketng .
Öğüdücü, Ş. G. (2023). Ver Madenclğ T emel Sınıflandırma Yöntemler .


Özkan, Y. (2008). Ver madenclğ yöntemler . Papatya Yayıncılık Eğtm.
Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Shmuel, G., Bruce, P . C., Yahav, I., Patel, N. R., & Lctendahl, K. C. (2018). Data Mnng for Busness
Analytcs  (1. bs). Wley .


**Ünte Soruları**

Soru-1 :
Nave Bayes sınıflandırıcının çalışma prensb aşağıdaklerden hangsne dayanmaktadır?
(Çoktan Seçmel)
(A) Bayes Teorem
(B) Nave Bayes Teorem
(C) Nave Teorem
(D) Bağımsızlık Teorem
Olasılık Teorem
Cevap-1 :
Bayes Teorem
Soru-2 :
A: Alede şeker hastalığı olması, B: Hastanın şeker hastası olması gb k olay verlmektedr . Alede şeker
hastalığı olduğu blnyorsa, hastanın şeker hastası olmasını hesaplamaya yarayan koşullu olasılık fades
aşağıdak seçeneklerden hangsnde doğru br şeklde gösterlmektedr?
(Çoktan Seçmel)
(A) 
(B) 
(C) 
(D) 


Cevap-2 :
Soru-3 :
Nave Bayes sınıflandırıcıdak bağımsızlık varsayımı ( ndependence assumpton ) ne anlama gelmektedr?
(Çoktan Seçmel)
(A) Tahmn sağlayan kategork ntelklern brbrnden bağımsız olduğu varsayılmaktadır .
(B) Tahmn sağlayan nümerk ntelklern brbrnden bağımsız olduğu varsayılmaktadır .
(C) Her br gözlemn brbrnden bağımsız olduğu varsayılmaktadır .
(D) Eğtm ver setndek gözlemlern test ver setndek gözlemlerden bağımsız olduğu varsayılmaktadır .
(E) Tahmn sağlayan tüm ntelkler arasında olasılık hesabını etkleyen lşknn olmadığı varsayılmaktadır .
Cevap-3 :
Tahmn sağlayan tüm ntelkler arasında olasılık hesabını etkleyen lşknn olmadığı varsayılmaktadır .
Soru-4 :
 olmak üzere 
  le sınıflar gösterlsn. Nave Bayes sınıflandırıcı le sınıfı blnmeyen br x
örneğnn sınıfı nasıl hesaplanır?
(Çoktan Seçmel)
(A) Ver setnde yalnızca sayıca en az olan sınıfa at olasılıklar değerlendrlmez, bu sınıf dışında kalan
sınıflara at 
  olasılıkları karşılaştırılır , olasılık değer en yüksek hesaplanan sınıf seçlr .
(B) Ver setnde yalnızca sayıca en fazla olan sınıfa at olasılıklar değerlendrlmez, bu sınıf dışında kalan
sınıflara at 
  olasılıkları karşılaştırılır , olasılık değer en yüksek hesaplanan sınıf seçlr .
(C) Tüm sınıflara at
  olasılıkları karşılaştırılır , olasılık değer en yüksek hesaplanan sınıf seçlr .
(D) Tüm sınıflara at 
  olasılıkları karşılaştırılır , olasılık değer en yüksek hesaplanan sınıf seçlr .
Tüm sınıflara at 
  olasılıkları karşılaştırılır , olasılık değer en düşük hesaplanan sınıf seçlr .


Tüm sınıflara at
  olasılıkları karşılaştırılır , olasılık değer en yüksek hesaplanan sınıf seçlr .
Soru-5 :
Nave Bayes sınıflandırıcı le analzler gerçekleştrlrken ntelklern ver tpnn sürekl olması durumunda
sürekl değerler le lgl genel kabul aşağıdak seçeneklerden hangsnde doğru bçmde verlmştr?
(Çoktan Seçmel)
(A) Posson dağılımına uygun dağıldığıdır .
(B) Unform dağılıma uygun dağıldığıdır .
(C) Bnom dağılımına uygun dağıldığıdır .
(D) Normal ( Gauss ) dağılımına uygun dağıldığıdır .
Bernoull dağılımına uygun dağıldığıdır .
Cevap-5 :
Normal ( Gauss ) dağılımına uygun dağıldığıdır .
Soru-6 :
Aşağıdak tabloya göre br kşnn kötü huylu tümöre sahp olma olasılığı nedr?
Tümör  Tp
İy huylu
Kötü huylu
İy huylu
Kötü huylu
Kötü huylu
İy huylu
İy huylu
Kötü huylu
İy huylu
İy huylu
A) 4/10
(Çoktan Seçmel)
(A) 5/10
(B) 6/10
(C) 7/10
10/10
Cevap-6 :


Soru-7 :
Nave Bayes sınıflandırıcı le maç sonucunun tahmn edldğ br analzde aşağıdak tabloya göre
 olasılığı nedr?
Faul Maç Sonucu
VarGalp
YokGalp
YokGalp
YokGalp
YokGalp
VarMağlup
VarMağlup
VarMağlup
YokMağlup
YokMağlup
(Çoktan Seçmel)
(A) 1/10
(B) 9/10
(C) 1/5
(D) 3/5
4/5
Cevap-7 :
3/5
Soru-8 :
5-kat çapraz geçerleme sonucunda elde edlen doğruluk değerler aşağıdak tabloda verlmştr . Buna göre
modeln nha performansı aşağıdak seçeneklerden hangsnde doğru olarak verlmştr?
Kat ( Fold )Doğruluk
1.kat ( fold)0.8
2.kat ( fold)0.8
3.kat ( fold)0.6
4.kat ( fold)0.7
5.kat ( fold)0.7
(Çoktan Seçmel)
(A) 0.6
(B) 0.7
(C) 0.72
(D) 0.8


Cevap-8 :
0.72
Soru-9 :
Python le tabakalı çapraz geçerleme yapablmek çn aşağıdak kod satırlarından hangs çalıştırılmalıdır?
(Çoktan Seçmel)
(A) sklearn.model_selecton mport StratfedKFold
(B) seaborn.model_selecton mport StratfedKFold
(C) pandas.model_selecton mport StratfedKFold
(D) numpy .model_selecton mport StratfedKFold
mxed_nave_bayes.model_selecton mport StratfedKFold
Cevap-9 :
sklearn.model_selecton mport StratfedKFold
Soru-10 :
Hangs Nave Bayes sınıflandırıcı çn doğrudur?
(Çoktan Seçmel)
(A) Ver setn eğtm ve test olarak ayrılmasına gerek duyulmaz.
(B) Kümeleme algortmasıdır .
(C) Hedef ntelk kategorktr .
(D) Koşullu olasılık hesabından faydalanılmaz.
Tahmn sağlayan ntelkler kategork ve nümerk halde br arada kullanılamaz.
Cevap-10 :


# 9. Karar Ağaçları


**Özlü Söz**

Eğer br yapay zekâ stratejnz yoksa, yaklaşmakta olan dünyada öleceksnz.
Devn Weng, Esk eBay CEO'su


**Kazanımlar**

1.   Karar ağaçları ( decson tr ees) le lgl temel tanım ve kavramları blr .
2.   ID3, C4.5, C5.0 ve Sınıflandırma ve Regresyon Ağaçları ( Classfcaton and Regr esson T rees - CART )
gb karar ağacı algortmalarının temel çalışma prensplern blr .
3.   Entrop ( entropy) kavramını blr ve olasılık-entrop lşksn br kl sınıflandırma problem çn
açıklayablr .
4.   Blg kazancı ( nformaton gan ), kazanç oranı ( gan rato ) ve Gn ndeks (delta Gn) gb ntelk seçm
ölçütlern anlar ve verlen br ver set çn bu ntelk seçm yöntemlern kullanarak karar ağacı oluşturablr .
5.   Python programlama dln le CAR T algortmasını br ver setne uygulayablr .
6.   CAR T algortmasının sınıflandırma performansını değerlendreblr , kontenjans tablosu yadımı le
modeln doğruluk, duyarlılık, kesnlk ve F-Ölçüsü gb performans ölçütlern hesaplayablr .
7.   Ver setndek ntelklern tahmn/öngörüdek önem derecelern bulablr .
8.   Karar ağacını grafğnn nasıl oluşturulacağını anlar .
9.   Karar ağacını oluşturan kuralları elde eder ve yorumlayablr .
10. Farklı ver setler üzernde karar ağaçlarının kullanımına yönelk pratk deneym kazanır .


**Brlkte Düşünelm**

1.   Karar ağacı nedr? Hang makne öğrenmes görevler çn kullanılablr?
2.   ID3, C4.5, C5.0 ve Sınıflandırma ve Regresyon Ağaçları ( Classfcaton and Regr esson T rees - CART )
algortmalarının temel çalışma prensplern nelerdr? Bu algortmaların brbrlerne göre avantaj ve


3.   Entrop ( entropy) nedr? Olasılık-entrop lşksn br kl sınıflandırma örneğ üzernden açıklayınız.
4.   Blg kazancı ( nformaton gan ), kazanç oranı ( gan rato ) ve Gn ndeks hang amaçla
kullanılmaktadır?
5.   CAR T algortmasının sınıflandırma performansını değerlendrrken kontenjans tablosu yoluyla elde
edlen doğruluk, duyarlılık, kesnlk ve F-Ölçüsü gb performans ölçütlern kullanmanın önem nedr?
6.   Ver setndek ntelklern tahmn/öngörüdek önem dereceler nasıl belrleneblr?
7.   Python le br karar ağacı grafğ nasıl oluşturulablr?
8.   Br karar ağacını oluşturan kurallar , karar ağacı algortmasının şef faflığı ve anlaşılablrlğ açısından
neden önemldr?


**Başlamadan Önce**

Bu bölümde Karar  Ağaçları  (Decson T rees) konusuna temel br grş yapılmıştır . İlk olarak karar
ağaçlarıyla lgl temel tanım ve kavramlar açıklanarak bu alandak ana prenspler okuyucuya aktarılmıştır .
Ardından öne çıkan karar ağacı algortmaları olan ID3, C4.5 , C5.0  ve Sınıflandırma ve Regr esyon Ağaçları
(Classfcaton and Regr esson T rees, CART ) le lgl temel çalışma prenspler ncelenmştr . Bu
algortmaların ver setn bölme ve sınıflandırma yöntemler kısaca açıklanmıştır .
Bununla brlkte karar ağaçlarında ntelk seçm çn kullanılan öneml ölçütler olan blg kazancı
(nformaton gan ), kazanç oranı  (gan rato ) ve gn ndeks  üzernde durulmuştur . Her br ölçütün ne
anlama geldğ ve nasıl hesaplandığına dar temel blgler küçük ver setler üzernde hesaplamalarla
sunulmuştur .
Öğrenlen teork blglern pratk uygulaması çn, Python’da CAR T algortması kullanılarak hastaların
dyabet test sonuçlarının öngörülmes üzerne br uygulama gerçekleştrlmş ve modeln performansının
değerlendrlmes çn kontenjans tablosu oluşturulmuştur . Temel performans ölçütler, okuyuculara modeln
etknlğ hakkında blg sağlamıştır . Öncek bölümlerde de kullanılan NumPy , Pandas ve Sckt-learn
kütüphanelernden bu bölümde de faydalanılmıştır .
Ayrıca analzler sonucunda elde edlen ntelk önem dereceler ( mportance ) grafkle görselleştrlmş ve
okuyuculara hang özellklern modelde daha etkl olduğunu anlama konusunda rehberlk edlmştr . Karar
ağacı grafğnn oluşturulması ve elde edlen kuralların yazdırılması adımları le modeln ç yapısının
anlaşılablrlğ artırılmıştır .
Bu bölüm hem teork hem de pratk açıdan okuyuculara karar ağaçlarını anlamaları ve kullanmaları açısından
temel br deneym sunmaktadır . Bu kazanılan deneymn pekştrlmes çn okuyuculara farklı ver setler
üzernde çalışması  önerlmektedr .


## 9.1. Karar  Ağaçları

Karar  ağaçları  (decson tr ees), makne öğrenmesnde hem sınıflandırma hem de regresyon görevler çn
kullanılan br danışmanlı öğrenme algortmasıdır . Dolayısıyla analzlerde ver setnde hedef ntelğn
kategork ya da nümerk br bçmde bulunması beklenr . Karar ağaçları çn tahmn sağlayan ntelkler
kategork, nümerk ya da karma halde ver setnde bulunablr . Kullanılan karar ağacı algortmasına göre
tahmn sağlayan ntelklern eğer gerekyorsa ver ayrıklaştırma ya da yapay kodlama gb yöntemlerden
faydalanılarak analzlere uygun hale getrlmes gerekmektedr . Karar ağaçları kullanılarak gerçekleştrlen


Karar ağaçları mantığını kavramak çn sıradan br ağaç düşünülsün. Ağacın kökü toprak altındadır . Ağacın
yerden yükselen gövdes bulunur . Gökyüzüne doğru uzanan dalları ve bu dallarda yaprakları bulunur . Karar
ağaçlarında se bu durum tersnedr . Yan karar ağaçları aşağıdan yukarıya doğru değl yukarıdan aşağıya
doğru dallanır .


Br karar ağacının temel elemanları şu şeklde verleblr:
• Düğüm  (Node ): Karar ağacının temel yapı taşıdır . Düğümler , ver setnde belrl br özellğ temsl eden
çeştl test veya kararları çerr . Düğümler arasında alt-üst  (chld-par ent) lşks bulunur .
• Kök Düğüm  (Root Node ): Karar ağacının en üstünde yer alan tepe düğümüdür .
• İç Düğüm  (Internal Node ): Kök düğüm dışındak ve en az br alt ( chld ) düğüme sahp olan düğümlerdr . İç
düğümler , br ntelğn değerne göre ver setn bölerek kararları temsl eder .
• Dal (Branch ): İç düğümlern alt düğümler ( chld ) arasındak bağlantıyı fade eder . Her dal, br ntelk
değerne karşılık gelr ve br alt düğüme yol açar .
• Yaprak  (Leaf/T ermnal Node ): Karar ağacının en alt düğümlerdr . Yaprak düğümler , br sınıflandırma veya
regresyon sonucunu temsl eder . Yaprak düğümlernde br karar alınmaz; bu düğümler , ver setnn belrl br
bölgesne veya sınıfına at olduğunu gösterr .
Karar ağaçları le sınıflandırmadak amaç; sınıf etketn bulmak çn etketlenmemş br gözlemn
ntelklern test ederek ağaç boyunca br yol (path) bulmaktır (Han vd., 201 1).
Br hastanın Covd-19 mu yoksa Grp m olduğunun öngörüleblmes çn Şekl 102’de br karar ağacı
verlmştr . Karar ağacında Covd19luleT emas  kök düğüm ntelğ olmuştur . Ardından Evet ( Yes)/Hayır ( No)
gb ntelğe at kategorler le dallanmalar oluşturulmuştur . BurunAknts , Cnsyet  ve Yas ç düğümlerdr .
En altta yer alan hedef ntelğn kategorler olan Covd-19 ve Grp’n bulunduğu kısımlar se karar ağacının
yapraklarıdır .
Karar ağaçları netcede EĞER … VE .. İSE … kalıpları kullanılarak çeştl karar kurallarının üretlmesn
sağlamaktadır . Aşağıda verlen karar ağacı çn bazı örnek kurallar şu şeklde sıralanablr:
• EĞER Covd19luleT emas = Evet ( Yes) İSE Hastanın Durumu = Covd-19
• EĞER Covd19luleT emas = Hayır ( No) VE BurunAknts = Evet ( Yes) VE Yas  


Şekl 102: Örnek br karar ağacı.
Karar ağaçları, farklı programlama dller ve bu dllere at farklı kütüphane ve paketler yardımıyla görsel
açıdan zengn çıktı sunmaktadır . Böylelkle verlen br karar oldukça şef faf bçmde raporlanablmekte ve
analz sonuçları kolayca yorumlanablmektedr .

### 9.1.1. Temel Karar Ağacı Algortmaları

Karar ağaçlarında brçok farklı algortma mevcuttur . Bu algortmaların çnde en blnenlernden ID3, C4.5 ve
C5.0 algortmaları J. Ross Qunlan öncülüğünde 1970’lern sonu le 1980’lern başından tbaren
gelştrlmeye başlanmıştır (Han & Kamber , 2006). ID3, C4.5 ve Sınıflandırma ve Regresyon Ağaçları
(Classfcaton and Regr esson T rees, CART ), karar ağaçlarının yukarıdan-aşağıya  (top-down ) özynelemel
(recursve ) böl ve yönet  (dvde and conquer ) şeklnde oluşturulduğu açgözlü  (greedy) br yaklaşım
benmser (Han vd., 201 1; Ledolter , 2013):
• Yukarıdan aşağıya yaklaşım, br eğtm ver set ve bunlarla lşkl sınıf etketler le başlar (regresyon
durumunda sınıf etketlernn yern nümerk değerlern aldığı unutulmamalıdır).
• Ağaç oluşturulurken eğtm ver set özynelemel olarak daha küçük alt kümelere (ver setlerne) bölünür .
Budama  (prunng ), düşük öneme sahp özellkler kullanan dalların çıkarılması şlemdr . Bu şeklde ağacın
karmaşıklığı azaltılır . Böylelkle aşırı uyum ( over-fttng ) azaltılarak modeln tahmn gücü artırılmış olur . Br
ağacın performansı budama le daha da artırılablr .
ID3 algortması  (Iteratve Dchotomser ) en bast karar ağacı algortmalarından brdr . ID3 yalnızca
kategork ntelklerle çalışma yeteneğne sahpken, C4.5 algortması  hem kategork hem de nümerk
(sürekl/ayrık) ntelklerle çalışablmektedr . C4.5 algortması eksk ver ( mssng data ) le çalışablr , aşırı
uyum sorununu genellkle budama olarak blnen aşağıdan-yukarıya teknğ le çözer ve eğtm versndek
ntelklere farklı ağırlıklar uygulanablr . C5.0 algortmasının  C4.5’e göre daha hızlı ve bellek açısından
daha verml olduğu blnmektedr (stackoverflow , 2018). Bu algortmalar değerlendrlrken ID3 en temel
olmak üzere, her br br önceknn br üst versyonu olarak kabul edleblr (Şekl 103). Üç algortma da


Şekl 103: ID3, C4.5 ve C5.0 algortmaları.
Sınıflandırma ve Regr esyon Ağaçları  (Classfcaton and Regr esson T rees, CART ) algortması Breman ve
dğ. (1984) tarafından gelştrlmştr . Tahmn sağlayan ntelkler ve hedef ntelk kategork veya nümerk
olablr . Elbette algortmanın adından da anlaşılacağı gb hedef ntelğn kategork olduğu durumlarda
sınıflandırma, nümerk olduğu durumlarda se regresyon modeller kurulablmektedr (Şekl 104). CAR T, tüm
tahmn sağlayan ntelkler analz eder ve br ntelğn hang kl dallanmasının (bölümünün) hedef
ntelktek sapmayı en y şeklde azalttığını belrleyerek başlar (Breman vd., 1984; Efron & Tbshran,
1991; Venables & Rpley , 1997). İlk bölünme sonrasında elde edlen ver set bölümlernn her br kısmı çn
hyerarşk br ağaç yapısında homojen yapraklar (termnal düğümler) elde edlnceye kadar süreç tekrarlanır
(Lews, 2000).


Şekl 104: Karar ağacı algortmalarının sınıflandırma ve regresyon lşks.
CAR T, yalnızca kl bölme prosedürünü zler . Yan aşağı doğru dallanmalarda br düğümden sadece k kol
çıkablr . Dolayısıyla kden fazla kategorye sahp ntelkler çn brne karşı dğerler ( one vs. all ) yaklaşımı
zleneblmektedr . Örneğn Syah, Beyaz, Kırmızı gb üç kategorye sahp renk ntelğ çn dallar aşağıdak
gb yapılandırılablr .
• {Syah} ve {Beyaz, Kırmızı}
• {Beyaz} ve {Syah, Kırmızı}
• {Kırmızı} ve {Syah, Beyaz}
CAR T algortması kullanılırken karar ağacının oluşturulması sürec şöyle açıklanmaktadır (Stenber g, 2009):
Ağaçlar , durdurma kuralı kullanılmadan maksmum boyuta kadar büyütülür (ver yeterszlğ sebebyle
bölünme gerçekleştrlemeyecek duruma kadar). Sonrasında; artık en yüksek büyüklüğe sahp olan ağaç bu


budanır . Her defasında; eğtm performansına en az katkıda bulunan yalnızca br bölme  budanablmektedr .
CAR T algortmasının hedef yalnızca tek br ağaç ortaya koymak değl, br bakıma her br en uygun ağaç
olmaya aday ç çe geçmş budanmış ağaçlar dzs oluşturmaktır . Doğru ağaç, budama dzsndek her ağacın
tahmn performansının bağımsız test verler üzernde değerlendrlmesyle seçlmektedr . Bu bölümün
Python dl le hazırlanan uygulamasında CAR T algortması kullanılmıştır .

### 9.1.2. Karar Ağaçlarında Temel Ntelk Seçm Ölçütler

Br karar ağacının oluşturulması sırasında ağacı oluşturan ntelkler hang sıraya göre seçlmektedr? Örneğn
Şekl 102’dek ağacın kök düğümü olarak neden Covd19luleT emas  ntelğ seçlmştr? Bu soruların cevabı
karar ağaçlarında kullanılan ntelk seçm ölçütlerdr . Bu bölüm kapsamında entropye dayalı ID3
algortması le kullanılan Blg Kazancı  (Informaton Gan ), C4.5 algortması le kullanılan Kazanç Oranı
(Gan Rato ) ve CAR T le kullanılan Gn ndeks/katsayısı (delta Gn değer) ntelk seçm ölçütler le lgl
örnekler yapılacaktır .
Ayrıca blg kazancı, kazanç oranı ve Gn ndeks gb ntelk seçm ölçütlernn hesaplanması le elde
edleblen en öneml çıktılardan br de ntelklern sonucu elde etmedek önem sıraları/derecelerdr . Yalnızca
karar ağacında kullanılmak üzere değl, farklı algortmalar le analz öncesnde ntelk seçm çn hesaplanan
bu önem sıraları/dereceler göz önünde bulundurulablr .
9.1.2.1.   Entr op
Karar ağaçlarında entrop, br ver setnn belrszlğnn/safsızlığının/rastgelelğnn br ölçüsüdür . Entrop
karar ağacı oluştururken br bölünmenn kaltesn belrlemek çn kullanılmaktadır . Entrop belrl br küme
çndek her sınıftak ver noktalarının oranına göre hesaplanır . Entrop kavramı Claude Shannon’ın Blg
Teors ’ne (Informaton Theory ) dayanmaktadır . Blg teors, verlern kompakt br şeklde temsl edlmes
(ver sıkıştırma veya kaynak kodlama olarak blnen br görev) ve hatalara karşı sağlam br şeklde letlmes
ve depolanması (hata düzeltme veya kanal kodlama olarak blnen br görev) le lgldr (Murphy , 2012).
Düşük entropye sahp br ver setnn, çoğu ver noktasının aynı sınıfa at olduğu yan oldukça homojen
olduğu anlamına gelr . Yüksek entropye sahp br ver setnn, brden fazla sınıfa yayılmış ver noktalarıyla
heterojen olduğu anlamına gelr . Karar ağaçlarında amaç, orjnal ver set le ortaya çıkan alt kümeler
arasında entropde en büyük azalmayı sağlayan bölünmey bularak entropy en aza ndrmek tr.
Şekl 105’ te olasılık ve entrop bağlantısı gösterlmektedr . Olasılık x-eksennde, entrop se y-eksennde yer
almaktadır . Grafk; Covd-19 ve Grp k sınıflarına at örneklern yer aldığı br ver set göz önünde
bulundurularak ncelensn. Br örneğn Covd-19 ve Grp gb k sınıftan brne at olma olasılığı (0,0) ve
(0,1) noktalarında belrszlk çermez. Yan örnek ya Covd-19 sınıfına attr ya da değldr . Olasılık verlen bu
noktalarda 0 ve 1 değern almaktadır . Oysa bu noktalarda; entrop en düşük sevyededr , saflık halnde
düzenszlk 0’dır . Entrop, grafğn tepe noktasında en yüksektr , aşırı düzenszlk haln yansıtır . Örnek
olarak hlesz br paranın havaya atılması olayı ele alınablr . Bu olayda belrszlk en yüksektr çünkü yazı ve
tura gelme htmal 0.5’ tr. İşte bu noktada entrop 1 değern almaktadır . Tepe noktası çn ver setndek
örneklern yarısının Covd-19, yarısının Grp olduğu da düşünüleblr . Böyle br durumda doğru şeklde karar


Şekl 105: Olasılık-entrop lşks GeoGebra (2023).
Örneğn Tablo 24’ tek bast ver set ele alınsın. Ver setnde öğrencnn sınıfı, ders çn çalışma süres ve
derse katılımını gösteren ntelkler le öğrencnn başarı durumunu fade eden hedef ntelk ( Karar )
mevcuttur .
Tablo 24: Örnek ver set.
Sınıf Çalışma Sür esDerse Katılım Karar
A Uzun Yüksek Başarılı
B Kısa Düşük Başarısız
A Orta Düşük Başarılı
B Kısa Düşük Başarısız
A Uzun Düşük Başarısız
B Orta Yüksek Başarılı
A Orta Yüksek Başarılı
B Kısa Düşük Başarısız
A Uzun Düşük Başarısız
B Orta Yüksek Başarısız

Orjnal ver set ya da bu ver setnden elde edlen herhang br bölme/bölüm/parça olmak üzere entrop (D)
hesaplanırken,  
   gözlem sayısı ve 

 se lgl vernn olma olasılığını göstermek üzere aşağıdak formül kullanılarak hesaplanır (Han vd., 201 1;


Hesaplamalarda logartma fonksyonu 2 tabanını kullanır ve entrop brm “ bt”lerdr (Brownlee, 2019c).
Bu formülden hareketle, Tablo 24’ tek hedef ntelk Karar  çn toplam entrop aşağıdak gb hesaplanır:


9.1.2.2.   Blg Kazancı
Ver setnde bulunan br A ntelğ,  
  ’y 
   bölüme veya alt kümeye ayırmak çn kullanılablr ( 
 ). Burada 
  , 
 ’de A’nın 

 sonucuna sahp olan örnekler çerr . Ver set bölündükten sonra kesn br sınıflandırmaya ulaşmak çn daha
ne kadar blgye htyaç olacağı şu şeklde hesaplanır:

  Dolayısıyla, karar ağacı
oluşturulurken kök düğüm ya da ç düğümlere karar verlrken ver setndek her br ntelk çn 

 değerlernn hesaplanması gerekmektedr .
Sınıf  ntelğ  çn hesaplama yapılacak olursa:
KararSınıf
AB
Başarılı 31
Başarısız 24
Toplam 55


Blg kazancı  (gan/nformaton gan ), orjnal blg gereksnm (yan sadece sınıfların oranına dayalı) le
yen gereksnm (yan A ntelğ kullanılarak ver set bölündükten sonra elde edlen) arasındak fark olarak
tanımlanır .

Çalışma Sür es ntelğ  çn hesaplama yapılacak olursa:
KararÇalışma Sür es
Kısa Orta Uzun
Başarılı 0 3 1
Başarısız 3 1 2
Toplam 3 4 3


Blg kazancı  (gan/nformaton gan ), orjnal blg gereksnm (yan sadece sınıfların oranına dayalı) le
yen gereksnm (yan A üzernde bölümleme yapıldıktan sonra elde edlen) arasındak fark olarak tanımlanır .
Blg kazancı, 0 le 1 arasında değşmektedr .
Dolayısıyla toplam entrop hesaplandıktan sonra tüm ntelkler çn ayrı ayrı blg kazançları hesaplanır ve
brbryle kıyaslanır . En yüksek blg kazancına sahp ntelk, karar  ağacı çn bölme ntelğ olarak


Derse Katılım  ntelğ  çn hesaplama yapılacak olursa:
KararDerse Katılım
Düşük Yüksek
Başarılı 1 3
Başarısız 5 1
Toplam 6 4


Blg kazancı  (gan/nformaton gan ), orjnal blg gereksnm (yan sadece sınıfların oranına dayalı) le
yen gereksnm (yan A üzernde bölümleme yapıldıktan sonra elde edlen) arasındak fark olarak tanımlanır .


Tablo 25’ te verldğ üzere çalışma süres ntelğne at blg kazancı en yüksektr . Bu nedenle karar ağacının
kök düğümü olarak Çalışma Sür es seçlr . Karar ağacı tamamlanana kadar şlemler devam ettrlr . Şekl
106’da blg kazancı le kök düğüm elde edldkten sonra karar ağacının lk görüntüsü verlmştr .
Tablo 25: Ntelklern blg kazancının karşılaştırılması.


Şekl 106: Blg kazancı le karar ağacının oluşturulması.
9.1.2.3.   Kazanç Oranı
Kazanç oranı ( gan rato ), karar ağacı algortmalarında çok sayıda olası kategorye sahp ntelklere yönelk
oluşacak önyar gı le başa çıkmak çn kullanılan br ölçüttür . Blg kazancına benzer şeklde hesaplanır; ancak
kazanç oranında her br ntelk çn ntelğn sahp olduğu olası kategorlern (veya ağaçtak dalların) sayısı
dkkate alınır .
Blg kazancı, çok sayıda kategorye sahp ntelklere karşı önyar gılıdır , çünkü bu ntelkler daha fazla olası
bölünmeye sahptr ve bu nedenle şans eser yüksek br blg kazancı üretme olasılığı daha yüksektr . Kazanç
oranı, çok sayıda dala sahp ntelkler çn br nev düzeltme uygular . Bunun sağlanması çn hesaplamalarda
bölme blgs  (splt nformaton ) adında br term hesaplanır . Kazanç oranı, blg kazancının bölme blgsne
bölünmesyle elde edlr .


Kazanç oranı da 0 le 1 arasında değşmektedr . En yüksek kazanç oranına sahp ntelk, karar  ağacı çn
bölme ntelğ olarak seçlr .
Örneğn; Tablo 24’ tek tüm ntelkler çn blg kazancı hesaplanmıştır . Şmd de bu ntelklere at kazanç


Tablo 24’ tek ver set çn blg kazancı dkkate alınarak karar ağacı oluşturulurken kök düğüm Çalışma
Süres ntelğ seçlmştr (T ablo 25). Tüm ntelklern kazanç oranı se Tablo 26’da özetlenmştr . Kazanç
oranı göz önüne alınarak karar ağacı oluşturulmak stenrse, en yüksek kazanç oranına sahp olan Derse
Katılım  ntelğ kök düğüm seçlecek ve karar ağacı tamamlanana kadar şlemler benzer şeklde devam
ettrlecektr (T ablo 26).
Tablo 26: Ntelklern kazanç oranlarının karşılaştırılması.


Şekl 107:  Kazanç oranı le karar ağacının oluşturulması.
9.1.2.4.   Gn İndeks ve Delta Gn Değer
Gn ndeks/katsayısı ( ndex/coeffcent ), br karar ağacı oluşturulurken br ver setndek bölünmenn
kaltesn değerlendrmek çn karar ağacı algortmalarında kullanılan br başka safsızlık ölçütüdür . Gn
ndeks de 0 le 1 arasında değşr; 0 saf (yan tüm gözlemlern aynı sınıfa at olduğu) br ver setn ve 1 se
tamamen saf olmayan br ver setn fade eder .
Delta Gn  değer de Gn ndeks gb karar ağacının bölünmes çn dkkate alınmaktadır . Bölünmeden
öncek ana düğümün Gn ndeksnden, bölünmeden kaynaklanan alt düğümlern Gn ndekslernn ağırlıklı
toplamının çıkarılmasıyla hesaplanır .
Gn ndeks ve delta Gn değer kullanılırken dkkat edlmes gereken en öneml konulardan br de karar
ağacında dallanmanın sadece kl bçmde yapılableceğdr . Dolayısıyla, kden fazla kategorye sahp
ntelklerde brne karşı dğerler  (one vs. all ) yaklaşımı benmsenmektedr . Örneğn; düşük, orta ve yüksek
gb üç farklı kategor olsun. Ağaç; br dalda düşük dğernde orta ve yüksek, br dalda orta dğernde düşük
ve yüksek ya da br dalda yüksek dğer dalda düşük ve orta olacak bçmde dallanablr .
Gn ndeksnn hesaplanmasında kullanılan formüller aşağıda verlmştr .


Safsızlıktak azalmayı en üst düzeye çıkaran (maksmum delta Gn değerne sahp olan veya eşdeğer
olarak mnmum Gn endeksne sahp olan) ntelk, bölme ntelğ olarak seçlr .
Örneğn; Tablo 27’dek ver setnde br frmanın ürünlerne lşkn fyat aralığı ve ürün kategor blgs le
ürün satış blgsnn yer aldığı hedef ntelk mevcuttur .
Tablo 27: Örnek ver set.
Fyat Aralığı Kategor Satış 


Ucuz Ev Gereçler Hayır
Pahalı Gym Evet
Ucuz Ev Gereçler Hayır
Pahalı Elektronk Hayır
Pahalı Gym Evet
Ucuz Gym Evet
Pahalı Ev Gereçler Hayır
Ucuz Elektronk Hayır
Ucuz Gym Hayır

Her br ntelk çn Gn ndeks ve delta Gn değerler aşağıdak gb hesaplanır:
Öncelkle Fyat Aralığı  ntelğ  çn hesaplamalar yapılsın:


Kategor  ntelğnn  ev gereçler, gym ve elektronk gb üç farklı kategors olduğundan kategorler kl
dallanma yapacak şeklde brne karşı dğerler mantığı le ele alınmaktadır . Dolayısıyla; {ev gereçler} ve
{gym, elektronk}, {gym} ve {ev gereçler, elektronk}, {elektronk} ve {ev gereçler, gym} ayrı ayrı


Buradan Kategor  ntelğ çn; Gn değer en düşük (ya da delta Gn değer en yüksek)  
  çıkmıştır . Yan; Kategor  ntelğ kök düğüm seçlrse, bu ntelğ br dalda
gym dğer dalda se ev gereçler ve elektronk kategorler olacak şeklde bölmek en uygundur . Dğer ntelk
le kıyaslama yaparken Kategor  ntelğ çn  

 çn Gn ndeks ve delta Gn değerler dkkate alınacaktır .
Nha değerlendrme Tablo 28’de verlmştr . Gn ndeks en düşük (delta Gn değer en yüksek) Kategor
ntelğdr . Bu nedenle de karar ağacının kök düğümü olarak Kategor ntelğ seçlmştr (Şekl 108). Benzer
şlemler ağaç tamamlanana kadar devam ettrlecektr .
Tablo 28: Ntelklern kazanç oranlarının karşılaştırılması.


Şekl 108: Gn ndeks le karar ağacının oluşturulması.

## 9.2. CAR T le Python Uygulaması

Bu çalışmada kullanılan ver set ( dabetes.csv ), Kaggle’dan temn edlmştr:
https://www .kaggle.com/datasets/mathch/dabetes-data-set?resource=download . Ver set aslen Natonal
Insttute of Dabetes and Dgestve and Kdney Dseases’e attr (Sgllto, 1990). Ver set Pma Kızılderl
kökenl 21 ve üzer yaştak kadınlardan oluşturmaktadır (T ablo 29). Bu çalışmanın temel amacı; dyabet
teşhsne lşkn tanısal brtakım ölçümlerden hareketle, dyabet hastalığı test sonucunun poztf/negatf
şeklde öngörülmesdr .
Ver setnde toplamda 768 adet gözlem ve 9 adet ntelk bulunmaktadır . Hedef ntelk olan Karar  ntelğnde
k kategor mevcuttur . Dolayısıyla kl sınıflandırma söz konusudur .
Tablo 29: Dyabet ver setndek ntelkler .
Ntelk Türkçes Açıklama Ver Tp
Pregnances Gebelkler Gebe kalma sayısı Nümerk
Glucose Glkoz Oral glukoz tolerans testnde 2 saatte plazma
glukoz konsantrasyonuNümerk
BloodPressure KanBasnc Dyastolk kan basıncı (mm Hg) Nümerk
SknThckness DerKalnlg Trseps der kıvrımı kalınlığı (mm) Nümerk
Insuln Insuln 2 Saatlk serum nsüln (mu U/ml) Nümerk
BMI VKI Vücut ktle ndeks (kg cnsnden ağırlık/(m
cnsnden boy)^2)Nümerk
DabetesPedgreeFuncton D_Soyagac Dyabet soyağacı fonksyonu Nümerk
Age Yas Yaş (yıl) Nümerk
Outcome Karar Sınıf değşken
0: Dyabet test sonucu negatf
1: Dyabet test sonucu poztfKategork


### 9.2.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Bu çalışmada NumPy , Pandas , Sckt-learn , Matplotlb  ve Seaborn  kütüphaneler kullanılmıştır (C. R. Harrs
vd., 2020; Hunter , 2007; McKnney , 2010; Pedregosa vd., 201 1; Waskom, 2021). Bu nedenle, eğer Python’da
adı geçen kütüphaneler yüklü değlse, Bölüm 3.1.’de açıklandığı gb bu kütüphaneler yüklenmel, aşağıdak


### 9.2.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . dabetes.csv  dosyasını okumak çn
Pandas  kütüphanesnden pd.read_csv()  fonksyonu kullanılmıştır .


Spyder edtörünün sol üst tarafında yer alan “V arable Explorer” penceresnde bulunan verSet  nesnesne
tıklanarak ver set ayrı br pencerede açılablr ve nceleneblr .


### 9.2.3. Ver Ön-şleme

Ver set okunduktan sonra ntelk adları Türkçeleştrlmştr . Ver setndek ntelk adları sırasıyla;
“Gebelkler , Glkoz, KanBasnc, DerKalnlg, Insuln, VKI, D_Soyagac, Y as, Karar ” olacak şeklde
yenden düzenlenmştr . Ardından; hedef ntelğn 0 ve 1 olarak kodlanan kategorler Negatf ve Poztf
şeklnde değştrlmştr . Elbette bu düzenlemeler br zorunluluk değldr; ancak karar ağacının ve performans
değerlendrmesnn daha anlaşılır olması çn lgl değşklkler yapılmıştır . Son olarak, hedef ntelğn ver


Ver setnn özetnn elde edleblmes çn aşağıdak kod bloğu kullanılmıştır . Tüm ntelklern aynı anda
görüleblmes çn Pandas ’ın dsplay .max_columns parametres 20 olarak belrlenmştr . Aks halde bazı
sütunların IPython Console ’da gösterlemeyeceğ, yerne … geleceğ unutulmamalıdır . Ayrıca .descrbe()
fonksyonunda nclude=all  eklenerek, hem kategork hem nümerk ntelklere lşkn özet blgnn
görüleblmes sağlanmıştır .


Sonrasında ver setndek ntelklern ver tpler lstelenmştr . Ver setnde eksk değerlern kontrolü


tran_test_splt()  fonksyonu yardımı le ver setnn %70’ eğtm, %30’u test ver set olacak şeklde kye
ayrılmıştır . Eğtm ver set çn tahmn sağlayan ntelkler X_tran , hedef ntelk y_tran , test ver setndek
hedef ntelkler X_test , hedef ntelk se y_test  değşkenlerne atanmıştır . random_state  parametres 1 olarak
belrlenmştr; ancak bu br zorunluluk değldr . Her sefernde aynı örneklern aynı ver setnde yer alması
düşünces gözetlmştr . Bu nedenle okuyucu kend random_state  parametresn kend steğne uygun şeklde
belrleyeblr .


### 9.2.4. Modelleme

CAR T sınıflandırıcı modelnn ( cart_model ) oluşturulablmes çn Sckt-learn  kütüphanesnden
DecsonT reeClassfer()  kullanılmıştır . CAR T algortması le çalışmak çn ağaç oluşturulurken Gn ndeks
kullanılmıştır ( crteron ). crteron  parametres ayrıca “entropy” değern de alablmektedr . Analzler
sonucunda daha bast br karar ağacının oluşturulablmes çn ağacın maksmum dernlğ 3 seçlmştr
(max_depth ). Eğer None değer aldıysa, düğümler tüm yapraklar saf olana kadar ya da tüm yapraklar
mn_samples_splt  parametres le belrlenen sayıdan daha az örnek çerene kadar genşletlr .
mn_samples_splt  ç (dahl) br düğümü bölmek çn gereken mnmum örnek sayısını temsl eder .
Ardından cart_model  modelnn ft() fonksyonuna eğtm ver set ve eğtm ver setnn hedef ntelğ
verlmştr .


### 9.2.5. Performans Değerlendrme

CAR T modelnn performansının değerlendrlmes çn cart_model.pr edct() fonksyonundan
faydalanılmıştır .


Ardından confuson_matrx()  fonksyonu le kontenjans tablosu oluşturulmuştur . Burada poztf sınıf olarak
dyabet hastalığı test sonucunun Poztf olmasının seçldğ görüleblr . Daha sonra se
ConfusonMatrxDsplay()  ve .plot()  fonksyonları yardımı le kontenjans tablosunun görüntülenmes
sağlanmıştır .


Kontenjans tablosundak tn, tp, fn, fp değerlernn sırasıyla aynı smlerde tanımlanan değşkenlere


classfcaton_r eport()  le en temel performans değerlendrme ölçütler elde edlmştr .


Yukarıda elde edlen performans metrkler raporuna göre CAR T modelnn doğruluğu %76’dır . Modeln
makro ortalama kullanılarak (her k sınıf çn hesaplanan performans değerlendrme ölçütlernden her br
çn ortalama) nha performansı değerlendrlrse; duyarlılığının %72, kesnlk değernn %75 ve F-
Ölçütünün se %73 olduğu görülecektr . Bu değerlern sınıflara göre yorumu hang sınıfın poztf sınıf olarak
seçldğne göre değşecektr . Elbette performans değerlendrme raporunda her k sınıf çn ayrı ayrı elde
edlen değerler de görüleblr .

### 9.2.6. Ntelklern Önem Dereces

Her br ntelğn dyabet hastalığının öngörüsündek önem dereces cart_model.featur e_mportances_  le


Ntelklern sonucu elde etmedek önemlern gösteren bu blgnn görsel açıdan daha anlamlı bçmde elde
edleblmes çn ntelkOnemDer eces  adlı br DataFrame tanımlanmıştır . Eğtm ver setndek ntelklern
adları ( Ntelkler ) ve ntelk önem dereceler ( Onem ) k farklı sütun halnde bu DataFrame’e atanmıştır .
DataFrame önem derecelerne göre büyükten küçüğe doğru sıralanmıştır . Seaborn  kütüphanes yardımı le
sütun grafğ elde edlmştr (Şekl 109).


Şekl 109 ncelenrse bazı ntelkler çn hesaplama yapılmadığı görüleblr . Aslında hesaplama yapılmayan
ntelkler , karar ağacında yer almayan ntelklerdr . CAR T modelne göre dyabet hastalığı öngörüsü çn en
öneml ntelklern sırasıyla glkoz, vücut ktle ndeks ( VKI ) ve yaş olduğu görüleblr .


Şekl 109: Ntelklern önem dereces.

### 9.2.7. Karar Ağacı Grafğ

Karar ağacı grafğnn elde edleblmes çn aşağıdak kod bloğu kullanılablr . Öncelkle grafk ekranının


model, ver setndek ntelk adları ( featur e_names ), ağaç elde edldğnde üzerndek yazının büyüklüğü
(fontsze ), hedef ntelğn kategorler ( class_names ) ve düğümlern dolgu durumu ( flled ) belrtlmştr .


Şekl 1 10 le verlen karar ağacı detaylı ncelendğnde, kök düğümün Glkoz olarak seçldğ görüleblr .
Karar ağacındak dallanmalar yukarıdan aşağı br düğümden yalnızca k kol çıkacak şeklde oluşmuştur . Her
br düğümde ve yapraklarda gn ndeks değer ( gn), gözlem sayısı ( samples ), hang sınıftan kaç adet
gözlemn bulunduğu ( value ) ve hang sınıfın baskın geldğne lşkn blg ( class ) yer almaktadır .


Şekl 110: Karar ağacı.

### 9.2.8. Karar Ağacından Elde Edlen Kurallar

Br öncek adımda karar ağacı grafğ elde edlrken kuralların IPython Console’a yapılandırılmamış metn
olarak yazdırıldığı görülecektr .


Bu noktada öneml olan elbette elde edlen kuralların doğru br bçmde yorumlanablmesdr (Şekl 1 11).
Aşağıda elde edlen kurallardan ks yer almaktadır:
• Eğer  Glkoz <=129.50 VE VKI <= 26.30 VE VKI <=9.10 İSE KARAR=«Negatf»
• Eğer  Glkoz > 129.50 VE VKI > 27.85 VE Glkoz <= 158.50 İSE KARAR=«Poztf»


Şekl 111: Karar ağacını oluşturan kurallar .
Şeffaf ve anlaşılablr kurallar özellkle tıp, fnans veya dğer krtk karar alma alanlarında kullanılan yapay
zekâ modeller çn önemldr . Bu tür modellern kararları anlaşılablr olduğunda, kullanıcılar ve paydaşlar
modeln mantığını güvenle takp edeblrler . Karar ağacından elde edlen kurallar , karar ağacındak her br
düğümün neye göre bölündüğünü ve hang koşullar altında hang sınıfa yönlendrldğn net br şeklde
açıklamaktadır . Bu durum verlen kararların neden bu şeklde alındığını anlamak steyen karar vercler veya
paydaşlar açısından önemldr .


**Bölüm Özet**

Bu bölümde Karar  Ağaçları  (Decson T rees) le lgl temel tanım ve kavramlara yer verlmş, karar ağacı
algortmalarının temel çalışma prensbnden bahsedlmştr . ID3, C4.5 , C5.0  ve CAR T karar ağacı
algortmaları le blg kazancı  (nformaton gan ), kazanç oranı  (gan rato ) ve gn ndeks  ntelk seçm
ölçütler kısaca açıklanmıştır . Entr op kavramı ve olasılık lşksne dkkat çeklmştr .
Python uygulaması, CAR T algortması le hastaların dyabet test sonucunun öngörülmes üzerne
gerçekleştrlmştr . Modeln performansının değerlendrlmes çn kontenjans tablosu  (contngency table )
oluşturulmuş ve bu bağlamda temel performans değerlendrme ölçütler hesaplanmıştır . Ayrıca, analzler
sonucunda ntelklern önem dereces elde edlmş ve grafkle görselleştrlmştr . Karar ağacı grafğnn nasıl
oluşturulacağı açıklanmış, karar ağacından elde edlen kurallar yazdırılmıştır . Bu bölüm, okuyuculara hem
teork hem de pratk açıdan karar ağaçlarını anlama ve kullanma konusunda temel br deneym sunmaktadır .
Bu kazanılan deneymn pekştrlmes çn okuyuculara farklı ver setler üzernde çalışması  önerlmektedr .


**Kaynakça**

Breman, L., Fredman, J., Stone, C. J., & Olshen, R. A. (1984). Classfcaton and Regr esson T rees. Taylor
& Francs.
Brownlee, J. (2019, Ekm 13). A Gentle Introducton to Informaton Entropy . MachneLearnngMastery .Com .
https://machnelearnngmastery .com/what-s-nformaton-entropy/
Efron, B., & Tbshran, R. (1991). Statstcal data analyss n the computer age. Scence , 253(5018), 390-
395.
GeoGebra. (2023). GeoGebra—100 mlyondan fazla öğr enc ve öğr etmen tarafından kullanılan ücr etsz
matematk araçları . GeoGebra. https://www .geogebra.or g/
Han, J., & Kamber , M. (2006). Data Mnng: Concepts and T echnques  (2. bs). Mor gan Kaufmann
Publshers.
Han, J., Kamber , M., & Pe, J. (201 1). Data Mnng Concepts and T echnques  (3. bs). Mor gan Kaufmann.
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
Hunter , J. D. (2007). Matplotlb: A 2D graphcs envronment. Computng n Scence & Engneerng , 9(3), 90-
95. https://do.or g/10.1 109/MCSE.2007.55
Ledolter , J. (2013). Data Mnng and Busness Analytcs wth R  (1. bs). ohn Wley & Sons, Inc.
Lews, R. J. (2000). An ntroducton to classfcaton and regresson tree (CAR T) analyss. Annual meetng of
the socety for academc emer gency medcne n San Francsco, Calforna , 14.
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a


Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Sgllto, V. (1990). Dabetes Dataset . Natonal Insttute of Dabetes and Dgestve and Kdney Dseases.
https://www .kaggle.com/datasets/mathch/dabetes-data-set?resource=download
stackoverflow . (2018). Dffer ent decson tr ee algorthms wth comparson of complexty or performance .
https://stackoverflow .com/questons/9979461/df ferent-decson-tree-algorthms-wth-comparson-of-
complexty-or -performance
Stenber g, D. (2009). CAR T: Classfcaton and Regresson Trees. İçnde X. Wu & V. Kumar (Ed.), The top
ten algorthms n data mnng . CRC press.
Venables, W. N., & Rpley , B. D. (1997). Modern appled statstc wth s-plus  (Second edton). Sprnger -
Verlag.
Waskom, M. L. (2021). seaborn: Statstcal data vsualzaton. Journal of Open Sour ce Softwar e, 6(60), 3021.
https://do.or g/10.21 105/joss.03021


**Ünte Soruları**

Soru-1 :
Aşağıdaklerden hangs karar ağaçlarında en üstte yer alan düğümün adıdır?
(Çoktan Seçmel)
(A) Kök düğüm
(B) İç düğüm
(C) Yaprak
(D) Dal
Alt düğüm
Cevap-1 :
Kök düğüm
Soru-2 :
Aşağıdaklerden hangs br karar ağacı algortması değldr ?
(Çoktan Seçmel)
(A) ID3


(C) C5.0
(D) D3.5
CAR T
Cevap-2 :
D3.5
Soru-3 :
Aşağıda verlen blglerden hangs yanlıştır ?
(Çoktan Seçmel)
(A) C4.5, ID3 algortmasının gelşmş br versyonudur .
(B) ID3 yalnızca kategork ntelklerle çalışablmektedr .
(C) CAR T hem kategork hem nümerk ntelkler le çalışablmektedr .
(D) C4.5 hem kategork hem nümerk ntelkler le çalışablmektedr .
(E) C5.0 yalnızca kategork ntelklerle çalışablmektedr .
Cevap-3 :
C5.0 yalnızca kategork ntelklerle çalışablmektedr .
Soru-4 :
Br karar ağacı oluşturulurken ağacın hang ntelkle başlayacağı, hang ntelğn ne zaman kullanılacağı
aşağıdak seçeneklern hangs yardımı le belrlenmektedr?
(Çoktan Seçmel)
(A) Ntelk seçm ölçütler
(B) Performans değerlendrme ölçütler
(C) Performans değerlendrme yöntemler
(D) Uzaklık fonksyonları
Kontenjans tablosu
Cevap-4 :
Ntelk seçm ölçütler
Soru-5 :
Ver setndek belrszlğn ölçüsü aşağıdak seçeneklern hangsnde verlmştr?


(A) ID3
(B) C4.5
(C) Entrop
(D) CAR T
C5.0
Cevap-5 :
Entrop
Soru-6 :
Br karar ağacı oluşturulurken ntelk seçm le lgl aşağıdak seçeneklerden hangs yanlıştır ?
(Çoktan Seçmel)
(A) Blg kazancı en yüksek olan ntelk seçlr .
(B) Kazanç oranı en yüksek olan ntelk seçlr .
(C) Gn ndeks en yüksek olan ntelk seçlr .
(D) Delta Gn değer en yüksek olan ntelk seçlr .
Ver setndek entropde en büyük azalmayı sağlayan ntelk seçlr .
Cevap-6 :
Gn ndeks en yüksek olan ntelk seçlr .
Soru-7 :
Aşağıda verlen tablodak Rsk hedef ntelğ çn toplam entrop aşağıdak seçeneklern hangsnde doğru
hesaplanmıştır?
Rsk
Düşük
Düşük
Düşük
Orta
Orta
Orta
Orta
Orta
Yüksek
Yüksek
(Çoktan Seçmel)
(A) 


(B) 
(C) 
(D) 
Cevap-7 :
Soru-8 :
Karar ağaçları le elde edlen kurallardan hangs hatalıdır ?
(Çoktan Seçmel)
(A) Eğer hastanın ateş 38 derece ve üzernde se, “Hasta X hastalığına sahptr ."
(B) Eğer hastanın kan basıncı normal aralıkta değlse ve öncek hastalık öyküsü varsa, “Hasta Y hastalığına
sahptr .”
(C) Eğer hastanın laboratuvar sonuçlarından br normal aralıkta değlse, “Hasta T hastalığına sahptr .”
(D) Eğer hastanın yaşından dolayı rsk faktörü yüksek se, “Hasta P  hastalığına sahptr .”
(E) Eğer “Hasta R hastalığına sahp” se, kan basıncı normal ve trglserd değer yüksek olablr .
Cevap-8 :
Eğer “Hasta R hastalığına sahp” se, kan basıncı normal ve trglserd değer yüksek olablr .
Soru-9 :
Python’da DecsonT reeClassfer()  kullanılarak oluşturulan br CAR T modelnn ağaç oluşturulurken
kullanılan tahmn sağlayan ntelkler çn hesapladığı önem dereces aşağıdak seçeneklern hangs
kullanılarak elde edleblr?
(Çoktan Seçmel)
(A) modelm.feature_mportances_
(B) modelm.mportances_
(C) feature_mportances(modelm)


modelm.mp_
Cevap-9 :
modelm.feature_mportances_
Soru-10 :
Python’da DecsonT reeClassfer()  kullanılarak oluşturulan br CAR T model çn ağacın maksmum
dernlğ 5 olarak seçlecektr . Bunun çn aşağıdak seçeneklerden hangs kullanılablr?
(Çoktan Seçmel)
(A) max_len = 5
(B) max_depth = 5
(C) max_length = 5
(D) max_deep = 5
maxmum_depth = 5
Cevap-10 :


# 10. Yapay Sinir Ağları


**Özlü Söz**

Yapay zekânın oluşturulmasındak başarı, nsanlık tarhndek en büyük olay olacaktır .
Ne yazık k, rsklerden nasıl kaçınacağımızı öğrenmedğmz sürece bu aynı zamanda sonuncusu da olablr .
Stephen Hawkng , Fzkç ve kozmolog


**Kazanımlar**

1.   Byolojk ve yapay snr hücrelernn (nöron) temel yapı ve çalışma prensplern anlar .
2.   Yapay Snr Ağları’nın – YSA  (Artfcal Neural Networks - ANNs ) temel yapısı ve şleyşn kapsamlı br
şeklde keşfeder .
3.   Temel YSA  topolojlern ve YSA  model türlern blr .
4.   Çok katmanlı algılayıcı YSA  yapısını ve gerye yayılım ( back-pr opagaton ) algortmasını blr .
5.   YSA ’nın avantaj ve dezavantajlarını blr .
6.   Python programlama dlnde YSA  algortmasıyla model oluşturablr .
7.   YSA  le sınıflandırma performansını değerlendreblr , kontenjans tablosu yadımı le modeln doğruluk,
duyarlılık, kesnlk ve F-Ölçüsü gb performans ölçütlern hesaplayablr .
8.   Farklı ver setler üzernde YSA  kullanımına yönelk pratk deneym kazanır .
9.


**Brlkte Düşünelm**

1.   Yapay Snr Ağları – YSA  (Artfcal Neural Networks - ANNs ) nedr?
2.   YSA ’nın gelşm sürecndek öneml olaylar nelerdr?
3.   YSA ’nın byolojk snr hücreler le lşks nedr?
4.   Br yapay snr hücresnn (nöron) yapısında hang temel bleşenler bulunur ve görevler nelerdr?


6.   Ağ topolojler nelerdr ve öne çıkan YSA  modeller hanglerdr?
7.   Çok-Katmanlı Algılayıcı Yapay Snr Ağları ( Mult-Layer Per ceptr on Neural Networks - MLPNN ) nedr
ve gerye yayılım algortması ( back-pr opagaton ) nasıl çalışır?
8.   YSA  çn ağırlıkların güncellenmes ne fade eder?
9.   Epoch nedr?
10. Batch boyutu ( batch sze ) nedr?
11. Batch normalzasyon nedr?
12. Drop-out nedr? YSA ’larında drop-out neden kullanılır?
13. Öğrenme oranı ( learnng rate ) ve momentum nedr?
14. YSA  avantajları ve dezavantajları nelerdr?
15. Python dlnde YSA  le çalışırken kullanılan temel kütüphaneler nelerdr?


**Başlamadan Önce**

Bu bölümde Yapay Snr  Ağları ’na – YSA  (Artfcal Neural Networks - ANNs ) dar kapsamlı br keşf
sunularak, okuyuculara bu heyecan verc alanın temellern atmaları çn rehberlk edlmektedr . İlk olarak
byolojk snr hücrelernden lham alınarak tasarlanan yapay snr hücrelernn (nöron) temel prenspler
detaylı br şeklde açıklanmaktadır . YSA ’nın genel yapısı ve şleyş ncelenerek grd, çıktı ve gzl
katmanların roller belrtlmş, toplama ve aktvasyon/transfer fonksyonları anlatılmıştır .
Farklı ağ topolojler ve öne çıkan YSA  modellernn verlmes, okuyuculara bu teknolojnn çeştl yönlern
anlama fırsatı sunmaktadır . Bölümde ayrıca, Çok-Katmanlı Algılayıcı Yapay Snr  Ağları (Mult-Layer
Perceptr on Neural Networks ) mmars le gerye yayılım  (back-pr opagaton ) algortması kapsamlı br
bçmde açıklanmıştır . Epoch , ağırlıklara başlangıç değer atanması  (weght ntalzaton ), batch boyutu
(batch sze ), batch normalzasyon  ve drop-out  gb YSA  le lşklendrlen temel kavramlar temel şeklde
açıklanmıştır . YSA ’nın avantaj ve dezavantajları üzernde durulmuştur .
Öğrenlen teork blglern pratk uygulaması çn, Python’da YSA  model kullanılarak prnç tanelernn
morfolojk özellklernden yararlanarak prnçlern Osmancık/Cammeo şeklnde sınıflandırılması üzerne br
uygulama gerçekleştrlmş ve modeln performansının değerlendrlmes çn kontenjans tablosu
oluşturulmuştur . Temel performans ölçütler, okuyuculara modeln etknlğ hakkında blg sağlamıştır .
Öncek bölümlerde de kullanılan NumPy , Pandas ve Sckt-learn  kütüphanelernden bu bölümde de
faydalanılmıştır . İlaveten Python’da YSA  ve dern öğrenme modeller le çalışılırken kullanılan temel
kütüphaneler olan TensorFlow  ve Keras’ tan faydalanılmıştır .
Bu bölüm hem teork hem de pratk açıdan okuyuculara YSA ’yı anlamaları ve kullanmaları açısından temel
br deneym sunmaktadır . Bu kazanılan deneymn pekştrlmes çn okuyuculara farklı ver setler üzernde
çalışması  önerlmektedr .


## 10.1. Yapay Snr  Ağları

Yapay Snr  Ağları  – YSA  (Artfcal Neural Networks – ANN’ s), bağlantılı ağlar ( connectonst networks ),


da adlandırılmaktadır (Kartal, 201 1; Öztemel, 2006). YSA, nsan beynnn şleyşn, byolojk snr sstemn
taklt etmeye çalışan br makne öğrenmes modeldr . YSA ’da her ne kadar byolojk sstemlerde bulunan
nöronlar arasındak bağlantılardan esnlenlmş olsa da, YSA  gerçek nöronlarla tüylern modern uçaklarla
olan lşksnden daha fazla lşkl değldr (Prddy & Keller , 2005). YSA, nsana özgü blg şleme ve
öğrenme yeteneklern gerçekleştrmeye odaklanan ler düzey kabul edleblecek makne öğrenmes
algortmaları arasındadır . Dğer makne öğrenmes modellernde olduğu gb YSA ’da da matematğn etks
yadsınamazdır . YSA  br grd uzayının çıktı uzayına eşlenmes/hartalanması ( mappng ) olarak tanımlanablr
(Prddy & Keller , 2005). Bu, matematksel br fonksyona benzetleblr . Amaç, grdnn stenen çıktıya
eşlenmesdr .
YSA ’nın tarhsel gelşm sürecnde yer alan öneml olaylar aşağıda kısaca özetlenmştr (A verkn & Yarushev ,
2018; Jalloul vd., 2023; Macukow , 2016; P . B. Pres vd., 2025):
• 1943  yılında nörofzyolog Warren McCulloch ve matematkç Walter Ptts tarafından YSA ’ya lşkn lk
öneml adım atılmıştır (McCulloch & Ptts, 1943). McCulloch ve Ptts beyndek nöronların çalışma şekln
açıklamak çn bast br snr ağı model oluşturmuşlardır . McCulloch-Ptts model, sabt eşklere sahp kl
(bnary) chazlar olarak kabul edlen bast unsurlara dayanmaktadır . Grd ve çıktı değerler 0,1 gb yalnızca
kl değerler kabul etmektedr . Model çıktıları, snrsel aktvtenn “ya hep ya hç” ( all-or -none ) karakterne
sahp bast mantık fonksyonlarıydı.
• 1949  yılında Donald Hebb, snaptk bağlantılardak değşklkler çn öğrenme kuralını formüle etmştr
(Fausett, 1994; Haykn, 1999; Olmsted, 1998). Hebb öğrenme kuralı; eğer k nöron brbrne bağlıysa ve
brnc nöron kncy tekrarlayan br şeklde etknleştrmeye devam edyorsa, o zaman ks arasındak
bağlantının snaptk değer artmalıdır düşüncesne dayanmaktaydı.
• 1958  yılında Amerkalı nörofzyolog Frank Rosenblatt, nsan algılama sürecn smüle eden br chaz şeması
önermş ve buna algılayıcı  (perceptr on) adını vermştr (Rosenblatt, 1958). Algılayıcı, byolojk prensplere
uygun olarak nşa edlmş ve öğrenme yeteneğ göstermştr (bknz. perceptr on learnng rule ).
• 1960  yılında Stanford'dan Bernard Wdrow ve Marcan Hof f tarafından ADALINE ve MADALINE adlı
modeller gelştrlmştr (Wdrow & Hof f, 1960). Ayrıca, ADALINE çn delta kuralı  (delta rule ) veya en
küçük kar eler (least-mean-squar e) kuralı olarak da blnen Wdrow-Hof f öğrenme kuralı gelştrlmştr .
• 1969  yılında Marvn Mnsky ve Seymour Papert, algılayıcı ağlarının sınırlılıklarına şaret etmştr (Mnsky
& Papert, 1969). Rosenblatt'ın temel ler beslemel algılayıcı ağlarının ( feed-forwar d multlayer ed
perceptr ons), yalnızca doğrusal olarak ayrılablr problemlerle başa çıkabldğn; ancak exclusve-OR (XOR)
gb doğrusal olmayan problemlern çözümünde kullanılamayacağını fade etmştr . Bu, YSA  (ve dolayısıyla
yapay zekâ) alanında hayal kırıklığına sebep olmuş, çalışma sayıları ve çalışmalara ayrılan fonlarda düşüş
yaşanmıştır . Bu dönem yapay zekâ kışı ( AI wnter ) olarak da adlandırılmaktadır .
• 1986  yılında çok katmanlı ağlar çn gerye yayılım algortması  (back-pr opagaton algorthm ) adı verlen
br öğrenme yöntemnn keşfedlmesyle YSA'ya olan lg yenden canlanmıştır . Bu algortmanın keşf, 1974
yılında Paul Werbos'a atfedlmektedr; ancak Rumelhart ve dğ. (1986) tarafından yenden keşfedldğ ve o
yıllarda YSA  üzerne çalışan çeştl araştırmacı gruplarının da katkılarıyla kullanımının yaygınlaştığı
söylenmektedr .
Günümüzde YSA ’ya dayalı dern öğrenme modeller pek çok alanda başarılı performansıyla öne çıkmaktadır .
Dern öğr enme , blgsayarların deneymlerden (verlerden) öğrenmesn sağlamak ve dünyayı br kavramlar
hyerarşs açısından anlamak (yan karmaşık kavramları daha bast olanlardan oluşturarak öğrenmek) olarak
görüleblr (Goodfellow vd., 2016; Kartal & Schwartz, 2022). Temsl öğrenme anlamında dern öğrenme,
grdy brden fazla aşamada (dernlemesne) daha doğrusal olarak ayrılablr veya karışık olmayan br çıktıya
dönüştürmek olarak görüleblr (Kartal & Schwartz, 2022; Yamns & DCarlo, 2016). Dern öğrenmede bahs
geçen dernlk, modeldek verlern başarılı temsllernn katman sayısını fade eder . Br dern öğrenme
modelnde onlarca veya yüzlerce ardışık temsl katmanı olablr (Chollet, 2018; Kartal & Schwartz, 2022).
YSA  ve dern öğrenme kavramlarının daha y anlaşılablmes çn br sonrak bölümde byolojk ve yapay


### 10.1.1. Byolojk ve Yapay Snr Hücreler

YSA  byolojk snr ağlarından esnlenlerek gelştrlmş ve nsan beynndek nöronların şleyşn taklt
etmek üzere tasarlanmıştır . YSA, genellkle yapay snr hücres/nöron/şlem brm/düğüm ( artfcal
neuron/neur on/pr ocessng unt/node ) olarak adlandırılan temel brmlerden oluşur . İnsan beynndek snr
hücres olan nöronlar , vücuttak blg letm ve şleme le sorumlu hücrelerdr . Örneğn br snr hücresnn
grds, gözden gelen ışık, kulaktan gelen ses, derden alınan dokunsal blgler olablr . Bunlar şlenerek, dğer
nöronlardan gelen elektrksel ya da salınan nörotransmtterler aracılığıyla taşınan kmyasal snyaller haln
almaktadır . Byolojk br snr hücres dendrt, hücre gövdes, akson ve snaps temel bölümlern çerr (Şekl
112):
• Dendrtler:  Hücre gövdesn çevreleyen ağaç dalına benzeyen uzantılardır . Çevredek dğer nöronlardan
gelen snrsel uyarıları alır . Dğer nöronlarla olan bağlantıyı sağlarlar .
• Hücr e Gövdes (soma):  Dendrtlerden gelen uyarıları toplar ve şler .
• Akson:  Hücre gövdesnden uzanan uzun br yapıdır ve dğer nöronlara snrsel uyarıları letr . Bazı
nöronların aksonları myeln kılıf  (myeln sheath ) adı verlen ve snyallern daha hızlı letmn sağlayan br
zar le kaplıdır . İnsan vücudundak en uzun aksonlar , uzunluğu br metrey aşablen syatk snr
oluşturanlardır (Muzo & Cascella, 2024).
• Snaps:  Aksonun dğer nöronlarla bağlantı kurduğu bölgedr . Burada kmyasal letmle snrsel uyarılar
dğer nöronlara letlr . Snr hücresnn aksonu boyunca letlen elektrksel ya da akson uçlarından salınan
nörotransmtterler  (neurotransmtters ) aracılığıyla dğer nöronlara letlen kmyasal snyaller şlenerek
nhayetnde ortaya br kas hareket, vücudumuz çn htyaç duyulan salgılar veya çeştl düşünceler meydana
getrlr .


Şekl 112: Byolojk snr hücres.
Byolojk br nöronun hücre gövdesnn dentrtk bağlantıları aracılığıyla dış ortamla etkleşm ve nöronun
kend çndek yerel koşullar , nöronun elektrk potansyeln yükseltp alçaltarak sodyum ya da potasyumu
çer ve dışarı pompalamasına neden olur (Prddy & Keller , 2005). Nöronun elektrksel potansyel belrl br
eşk değer ( threshold ) aşarsa nöron ateşlenr ( fres). Dğer br fadeyle br aksyon potansyel ( acton
potental ) oluşturulur ve nöronun aksonundan snapslarına ve dğer nöronlara doğru akışı sağlanır yan blg


aksonu boyunca akson termnallerne doğru yayılmasını sağlayarak br nöron popülasyonu arasındak
letşmde merkez br rol oynar ve daha sonra snapslarda dğer nöronlarla bağlantı kurablr (Ha & Cheong,
2017; Hetler , 2019). Eğer gerlm artışına neden olan uyarıcı ( stmulus ) düşük kalırsa, nöronun ateşlenmes
uzun zaman alır . Eğer yüksek olursa, nöron daha hızlı ateşlenr . Br nöronun ateşleme oranı sıfıra yakın
olduğunda herhang br uyaran yok anlamına gelr . En yüksek sevyede se sanyede 300 snr mpulsu ( pulse )
elde edleblr; k bu da nöronun oldukça hızlı ateşlenmesn sağlar (Prddy & Keller , 2005). Br nöron
fzksel br sstem olduğu çn, ateşlenmesne neden olacak kadar şarj oluşturması zaman alır . Adrenaln bu
noktada öneml rol oynar . Adrenaln, byolojk nöronlar çn bas anlamına gelmektedr . Yan, br uyaranın
varlığında nöronun çok daha muhtemel ateşlenmesn sağlar (Prddy & Keller , 2005).
Grd, tıpkı byolojk snr hücresndek gb dış ortamdan alınan ya da br başka nörondan alınan very fade
eder. Örneğn br görüntünün pkseller, br otonom aracın çevresn algılayan sensörlerden gelen verler brer
grd olablr .
Yapay br nöron se aşağıda verlen temel bleşenlere sahptr (Şekl 1 13):
• Ağırlıklar  (weghts ): Dendrtlere benzetleblr . Genellkle grd verleryle çarpılır ve toplanır .
Örneğn; br yapay snr hücresnn  
  , 
  , 
   gb üç farklı grdsnn olduğu
düşünülsün. Bu grdlere karşılık ağırlıklar 
  , 
   ve 

 olsun. Bu ağırlıklar , toplam fonksyonu yardımıyla net grdnn hesaplanmasında kullanılacaktır .
• Toplama Fonksyonu  (summaton/sum functon ): Net grdnn hesaplanablmes çn kullanılır . Genellkle,
toplam fonksyonu olarak ağırlıklı toplam ( weghted sum ) kullanılmaktadır . Yan grdler ağırlıklarla
çarpılacak ve çarpımlar toplanacaktır .


Ağırlıklı toplam dışında farklı toplama fonksyonları da mevcuttur . Bunlardan bazıları şu şeklde sıralanablr
(Elmas, 2007; Öztemel, 2006):
Çarpım Fonksyonu:


Maksmum Fonksyonu:


Çoğunluk Fonksyonu:


• Aktvasyon/T ransfer  Fonksyonu  (actvaton/transfer functon ): Hücre gövdesnn şlevn taklt eder .
Toplama fonksyonu çıktısı üzernde br eşk değer ( threshold ) belrler ve ancak belrl br uyarı sevyesn
aşan çıktı üretr . Aktvasyon fonksyonu olarak basamak fonksyonu seçldğ varsayılsın. Yukarıda
hesaplanan Net Grd aktvasyon fonksyonuna verlrse:


Basamak fonksyonu dışındak aktvasyon fonksyonlarından bazıları aşağıdak gb sıralanablr (Aggarwal,
2018; GeoGebra, 2023; Özen, 2022):
Lneer/Üyelk (Lnear/ Identty ) Fonksyonu: Lneer (doğrusal) aktvasyon fonksyonu, hedef ntelk reel br


İşaret (Sgnum ) Fonksyonu: İşaret aktvasyonu kl ( bnary ) çıktılar üretlmes gerektğnde uygundur .


Sgmod Fonksyonu: Sgmod aktvasyon (0, 1) aralığında br çıktı üretr ve bu da olasılık olarak


Tanjant Hperbolk ( tanh ) Fonksyonu: Sgmod fonksyonuna benzer br şekle sahptr . Çıktıların hem
poztf hem de negatf olması stendğnde ([-1,1]) tanjant hperbolk fonksyonu sgmod yerne terch edlr .


ReLU ( Rectfed Lnear Unt ) Fonksyonu: ReLU, çok katmanlı snr ağlarının eğtlmesne sağladığı


  • Çıktı  (output ): Br öncek
adımda aktvasyon fonksyonundan elde edlen değer 1’dr . Bu değer yapay snr hücresnn çıktısıdır .
Aktvasyon fonksyonunun çıktısı, dğer nöronlara ya da br YSA ’nın nha çıktısı ( 

) olarak letlr . Çıktı değer, br görüntüde hang nesnenn bulunduğuna lşkn sınıf etket ya da gelecektek
br hsse senednn sayısal değern temsl edeblr . Dolayısıyla hang aktvasyon fonksyonunun hang
aşamada kullanılacağı analz yapan araştırmacı tarafından belrlenr .


Şekl 113: Yapay snr hücres/neuron (Aggarwal, 2018).
Yukarıda lstelenen temel bleşenler dışında bas nör onu da br YSA  çn oldukça önemldr (Şekl 1 13)
(Aggarwal, 2018). Grd değer her zaman 1 olan br ağırlık gb düşünüleblr (Sarkara, 2012). Bas
nöronunun temel görev, YSA ’da bulunan dğer nöronlara ek br esneklk sağlamaktır . YSA, genellkle br
dz grdden ( nputs ) oluşur ve bu grdler üzernden br dz ağırlık ( weghts ) le net grd hesaplanır . Net
grdye aktvasyon fonksyonu uygulanarak çıktı hesaplanır . İşte bu süreçte net grd hesaplanırken (genellkle
ağırlıklı toplam şlemnde) bas nöronu devreye grmektedr . Bas nöronu, br nöronun grdler le ağırlıklı
toplamına ek br sabt değer ( bas) ekler . Bu sayede nöron çıktısını br tür esneklkle ayarlayablr . Modeln,
öğrenme kapastesn artırmasına yardımcı olur . Kısaca bas nöronu, br YSA  modelnn daha genel ve esnek
olmasını sağlar .
Bas nöronu aktvasyon fonksyonu şlemlernde de etkldr . Aktvasyon fonksyonunun eşk değern
belrleyerek nöronun ne zaman “ateşleneceğn” etkler . Örneğn; eğer br nöronun aktvasyon fonksyonu
basamak ( step) fonksyonu se, bas nöronu bu eşğ belrleyerek çıktının ne zaman 1 veya 0 olacağını etkler .


Hem byolojk snr hücreler hem de yapay nöronlar grdler alır , şler ve çıktı üretr . Her ks de bağlantılar
kurarak blg şleme yeteneklern gerçekleştrr . Bunun yanı sıra byolojk snr hücreler çok daha
karmaşıktır ve brçok etkleşmle brbrne bağlıdır . Yapay snr hücreler se genellkle daha bast ve daha
özelleştrleblr yapıdadır . Byolojk snr hücreler kmyasal/elektrksel letm kullanırken, yapay snr
hücreler genellkle sayısal şlemler kullanır . Byolojk snr hücreler genellkle çeştl uyaranlara çok çeştl
şekllerde yanıt vereblrken, yapay snr hücreler genellkle hsse sened tahmn, kanser teşhs gb alan
temell daha spesfk br görev yerne getrmektedr .

### 10.1.2. Yapay Snr Ağlarının Yapısı ve İşleyş

Br YSA, yapay snr hücreler (nöron) olarak adlandırılan tekl brmlerden oluşur . Bu brmler , ağırlıklar le
brbrne bağlanır ve katmanlar halnde düzenlenr , bu yapı da snr ağını oluşturur . Her nöronun ağırlıklı
grds, transfer fonksyonu ve çıktısı vardır . Katmanlara bas nöronu lave edleblr . Snr ağının davranışı,
nöronların transfer fonksyonları, öğrenme kuralı ve ağ mmars tarafından belrlenr (Macukow , 2016).
Ağırlıklar , ağın ayarlanablr parametrelerdr ve bu bağlamda snr ağı, parametrel br sstemdr . Grşlern
ağırlıklı toplamı, nöronun aktvasyonunu oluşturur .
Br YSA  genellkle üç tür parametre tarafından tanımlanır (Macukow , 2016):
1.   Nöron katmanları arasındak bağlantı desen.
2.   Ağırlıkların güncellenmes çn öğrenme sürec.
3.   Br nöronun ağırlıklı grşn çıkış aktvasyonuna dönüştüren aktvasyon fonksyonu.
YSA  brbrnden farklı topolojk yapı da meydana getrleblr (Hrolenok, 2009; Jaeger , 2002; Kresel, 2007;
Krose & van der Smagt, 1996; Macukow , 2016; Özen, Kartal, & Gülseçen, 2017):
İler beslemel  (feed-forwar d) YSA ’nın çalışmasında dışarıdan alınan ver, grd nöronlarından çıktı
nöronlarına doğru ler yönde hareket eder . İler beslemel YSA, gerye doğru bağlantılar çermez. İler
beslemel YSA  mmarlerne örnek olarak algılayıcı, çok katmanlı algılayıcı ( mult-layer per ceptr on) veya
ADALINE verleblr .
Ynelemel  (recurr ent) YSA  se ger bldrm bağlantıları çeren br türdür . Dğer br fade le br nöron
herhang br yol ya da bağlantı le kendsn etkleyeblr yan değern değştreblr . İler beslemel YSA'ların
aksne, ağın dnamk özellkler önemldr . Ağdak br nöron kend çnde, aynı ara katman çnde ya da
katmanlar arasında yneleyeblr . Ynelemel YSA ’lara örnek olarak Elman ağları, Jordan ağları, Kohonen
(SOM) veya Hopfeld tabanlı ağlar gösterleblr .
Tam bağlantılı  (fully-connected ) YSA ’larda se br katmandak her nöron kendnden br öncek ve br
sonrak katmandak dğer tüm nöronlar le bağlantılıdır . Tam bağlantılı ağlar genellkle çok sayıda
parametreye sahp olduğu çn eğtm ve hesaplama açısından malyetldr .
Yukarıda bahsedlen ağ topolojler göz önünde bulundurularak danışmanlı, danışmansız ve pekştrmel
öğrenme stratejlerne uygun YSA  öğrenme model ve algortmaları gelştrlmştr . Bunların çnde y blnen
YSA  türler şu şeklde sıralanablr (Alexander , 2020; P . Pres vd., 2023):
• Çok-Katmanlı Algılayıcı Yapay Snr Ağları ( Mult-Layer Per ceptr on Neural Networks )
• Radyal Taban Fonksyonlu Yapay Snr Ağları ( Radal Bass Functon Neural Networks )
• Hopfeld Yapay Snr Ağı ( Hopfeld Neural Network )
• Hammng Yapay Snr Ağı ( Hammng Neural Network )
• Kohonen Özör gütlemel/Kendn Ör gütlemel Yapay Snr Ağı ( Kohonen Self-Or ganzed Map Neural
Network )


• Zaman Geckmel Yapay Snr Ağları ( Tme Delay Neural Networks )
• Dern İler Beslemel Snr Ağları ( Deep Feed Forwar d Neural Networks )
• Özynelemel Snr Ağları ( Recurr ent Neural Networks )
• Uzun-Kısa Sürel Bellek Snr Ağları ( Long-Short T erm Memory Neural Networks – LSTM )
• Öz-İlşkl Yapay Snr Ağları/Oto-kodlayıcılar ( Auto-assocatve Neural Networks/Auto-encoders)
• Markov Zncr Ağları ( Markov Chans Networks )
• Uyarlanablr Rezonans Teors Ağları ( Adaptve Resonance Theory- ART)
Bu bölüm kapsamında; danışmanlı öğrenme problemler çerçevesnde kullanılan Çok Katmanlı Algılayıcı
YSA  (Mult-Layer Per ceptr on Neural Networks ) le gerye yayılım algortması  (back-pr opagaton
algorthm ) ele alınmıştır .

### 10.1.3. Çok-Katmanlı Algılayıcı Yapay Snr Ağları

Tpk çok-katmanlı algılayıcı YSA  modelnde nöronlar , brbrne bağlı katmanlar halnde
konumlandırılmışlardır . Ağda üç temel katmandan bahsedleblr (Şekl 1 14, Şekl 1 15) (Öztemel, 2006):


1. Grd Katmanı  (Input Layer ): Modeln dış dünyadan aldığı verlern grşn sağlar . Her br grd nöronu,
modeln öğrenme sürecnde kullanılacak ntelkler temsl eder (yaş, cnsyet, gelr durumu gb). Dolayısıyla
ver setnde kaç tane tahmn sağlayan ntelk varsa, grd katmanında da o sayı kadar nöron bulunur . Grd
katmanında herhang br şlem yapılmaz, görev yalnızca aldığı grdy br sonrak katmana letmektr .
2. Ara/Gzl Katmanlar  (Hdden Layers ): Grd katmanından gelen verler şleyen ve modeln
karmaşıklığını artıran katmanlardır . Gzl katman sayısı ve gzl katmanlarda bulunan nöron sayılarının ne
olacağıyla lgl kesn belrlenmş br kural mevcut değldr . Araştırmacılar deneme yanılma yolu le uygun
değerlere ulaşmaktadır; ancak konuyla lgl bazı tavsyeler mevcuttur . Ara katmandak nöron sayısı (Heaton,
2017; Özen, 2016);
• grd ve çıktı katmanı boyutu arasında olmalıdır .
• grd vektörünün ve çıktı vektörünün toplamının 2/3 katı olmalıdır .
• grd katmanı boyutunun k katından daha az olmalıdır .
3. Çıktı Katmanı  (Output Layer ): Model tahmnlernn yapıldığı katmandır . Görevn türüne bağlı olarak çıktı
katmanındak her br nöron br sınıf, br sayı veya başka br çıktıyı temsl edeblr . Çıktı katmanında yalnızca
tek br nöronun bulunması gerekmez, daha fazla sayıda nöron bulunablr .


Şekl 115: YSA  katmanları.
Danışmanlı öğrenme stratejsnden de hatırlanacağı gb (bknz. Bölüm 1.4.1), çok-katmanlı algılayıcı YSA  le
çalışılırken ver setnde probleme uygun oluşturulmuş grd-çıktı kller ( 
  ) bulunur . Grd
vektörlernn her br YSA ’ya gösterldğnde, ağ, ona uygun çıktıyı ( 

) üretr; ancak ne yazık k her sefernde modeln tahmn le gerçek tahmn bre br aynı olmaz, dğer br fade
le %100 tahmn başarısı elde edlemez. Ağın eğtmnde, doğru sonuca ulaşmak çn br sonrak grd ağa
gösterlmeden önce ağırlıklar değştrlr . YSA  öğrenme sürecnn öneml br bölümünü bu ağırlık
güncellemes  şlemler oluşturur . YSA ’nın amacı br bakıma grdlere uygun çıktıları üretecek ağırlıkları
bulmaktır . YSA  model oluşturulduktan sonra (YSA  eğtldkten sonra) ağın performansının test sürecnde
ağırlıklar değştrlmez . YSA'da blg, ağırlık değerlernde saklanır , blgnn dağıtılmış olması, ağdak br
bağlantı kaybında ble ağın çalışmasını sağlar (Kartal, 201 1). Bu özellk, YSA'nın güçlü ve öneml
özellklernden br olarak kabul edlmektedr .

### 10.1.4. Gerye Yayılım Algortması

Gerye yayılım algortması, YSA ’da kullanılan popüler br öğrenme algortmasıdır . Gerye yayılım
algortması, delta kuralının genelleştrlmş haldr ve bazı kaynaklarda genelleştrlmş delta kuralı
(generalzed delta rule ) olarak da adlandırılmaktadır (Sarkara, 2012). Gerye yayılım algortması sürekl


kullanılır . Öğrenme, ortalama kar esel hata  (MSE) ve gradyan nş ne (gradent descent ) dayalı olarak
gerçekleşr .
Gerye yayılım algortması; ler yayılım  (forwar d propagaton ) ve ger yayılım  (backwar d propagaton )
olmak üzere k temel aşamadan oluşur (Kartal, 201 1; Özen, 2016; Özen, Kartal, & Gülseçen, 2017; Öztemel,
2006).
İler Yayılım Aşaması:
• Başlangıçta, ağın ağırlıkları rastgele atanır .
• Eğtm ver setnden br örnek- grd ve hedef çıktı çft ( 

) alınır .
• Grd, ağdak nöronlara ler yönlü ( forwar d) letlr ve ağ tarafından çıktı ( 

) üretlr .
• Bu çıktı, gerçek çıktı- hedef ntelk ( 

)- le karşılaştırılır ve hata/kayıp ( loss) değer hesaplanır . Kayıp, model tahmnlernn gerçek değerlerden ne
kadar uzak olduğunu ölçer (Chng, 2022). Ağın eğtm sırasında bu kaybın azaltılması hedeflenr . Problem
türüne göre farklı kayıp fonksyonları terch edleblr .
Ger Yayılım Aşaması:
• Hata değer, ağın çıktısından başlayarak gerye doğru yayılır .
• Her ağırlık çn, hata değernn o ağırlıkla olan lşksne göre br gradyan hesaplanır ve ağırlıkları
güncellemek çn kullanılır .
İler ve ger yayılım aşamaları tüm eğtm örnekler çn tekrarlanır . Br eğtm ver setnn tamamının ağa br
kez gösterlmes br “epoch”  olarak adlandırılmaktadır . Gdş-dönüş ya da tur sayısı olarak da blnmektedr
(Özen, 2022). Brden fazla epoch, ağın eğtm ver setn brden fazla kez gördüğü anlamına gelr .
Ağırlıklar , belrl br öğrenme oranıyla gradyanın negatf yönde güncellenr . Bu, ağırlıkları kayıp
fonksyonunu mnmze edecek yönde günceller . Bu adım, eğtm setndek tüm örnekler çn tekrarlanır ve
br epoch tamamlanmış olur . Epoch sayısı; önceden belrlenen sabt br eşk değere kadar ya da belrl br
durum gerçekleşene kadar (örneğn; ağ hatası 0.001’den küçük kalıncaya kadar) artırılır .
Ağırlıklara Başlangıç Değerlernn Atanması (Brownlee, 2021) : YSA ’dak nöronlar , grdlern ağırlıklı br
toplamını hesaplamak çn kullanılan ağırlıklar olarak adlandırılan parametrelerden oluşur . YSA  modeller,
br kayıp fonksyonunu ( loss functon ) en aza ndrmek çn ağ ağırlıklarını kademel olarak değştren ve
tahmnler yapablen stokastk gradyan nş  (stochastc gradent descent ) adı verlen br optmzasyon
algortması kullanır . Bu optmzasyon algortması, optmzasyon sürecne başlamak çn olası ağırlık değerler
uzayında br başlangıç noktası gerektrr . Ağırlıklara başlangıç değer atanması ( weght ntalzaton ), br
YSA ’nın ağırlıklarını modeln optmzasyonu (öğrenmes ya da eğtm) çn başlangıç noktasını tanımlayan
küçük rastgele değerlere ayarlama prosedürüdür .
Öğrenme Oranı: Ağın eğtm sırasında, ağırlıklar uygulanırken kullanılan düzeltme mktarına öğrenme
oranı  (learnng rate ) denr (Özen, 2022). Öğrenme oranı ( 

) düşük seçlrse, eğtm çn geçen süre artablr ve ağ yerel mnmuma takılablr veya aşırı uyum
(ezberleme) yüzünden test ver setnde beklenen başarıyı elde edemeyeblr . Eğer öğrenme oranı yüksek


genelleştrme yeteneğ olmaz. Bu nedenle, öğrenme oranının uygun bçmde belrlenmes gerekr . Öğrenme
oranı, modeln performansını etkleyen öneml br parametredr ve optmal br değern bulunması deneme-
yanılma yöntemler veya otomatk hperparametre ayarlama teknkler le belrlenr . Değer genellkle 0 le 1
arasında değşmektedr; ancak farklı değerler de kullanılablmektedr .
Momentum Katsayısı:  Ağın eğtmnde kullanılan br başka kavram se momentum  katsayısı dır.
Momentum, gradyan tabanlı optmzasyon algortmalarında kullanılan br hperparametredr . Momentum
katsayısı, ağırlık güncellemelernde geçmş gradyan değerlern ne kadar dkkate alacağını kontrol eder .
Adından da anlaşılacağı gb, ağırlık güncellemesne br öncek güncelleme yönünde devam etmes çn br
mktar atalet verlr (Sarkara, 2012). Bu, algortmanın daha hızlı ve düzenl br şeklde optmuma doğru
lerlemesne yardımcı olablr . Momentum katsayısının yüksek br değer seçlmes toplam hatanın sıfıra daha
fazla eğmle yaklaştığını fade etmektedr (Elmas, 2007).
YSA ’nın eğtm tamamlandıktan sonra, ağın genelleme yeteneğnn değerlendrlmes çn ayrı br test ver
set kullanılır . Daha önce de fade edldğ gb test sürecnde ağırlıklar değştrlmez, yalnızca ağın
performansı değerlendrlr .
Batch Boyutu (Brownlee, 2022b) : Kısaca ağa tek seferde sunulacak örnek sayısını fade eder . Batch boyutu,
dahl model parametrelernn güncellenmeden önce üzernde çalışılacak örnek sayısını tanımlayan br
hperparametredr . Br batch, br veya daha fazla örnek üzernde ynelenen ve tahmnler yapan br for
döngüsü olarak düşünüleblr . Batch çndek örnekler ağa gösterldkten sonra tahmnler beklenen çıktı
değşkenleryle karşılaştırılır ve br hata hesaplanır . Bu hata, güncelleme algortmasıyla model yleştrmek
çn kullanılır . Eğtm ver set br veya daha fazla partye bölüneblr .
•  

 se Batch Gradyan İnş ( Batch Gradent Descent )
•  

 se Stokastk Gradyan İnş ( Stochastc Gradent Descent )
•  

 se Mn-Batch Gradyan İnş ( Mn-Batch  Gradent Descent )
olarak adlandırılır . Mn-batch gradyan nş durumunda, 32, 64 ve 128 örnek çeren batch boyutları sıklıkla
terch edlmektedr .
Batch Normalzasyon: Normalzasyon, sayısal verler şekln bozmadan ortak br ölçeğe getrmek çn
kullanılan br ver ön şleme teknğdr (Saxena, 2021). Modelleme aşamasından önce normalzasyon
yapılmakta ve ardından makne öğrenmes model ver setne uygulanmaktadır; ancak ne yazık k özellkle
çok fazla ara katmana sahp dern YSA ’larda grd brçok aktvasyon fonksyonundan geçtğ çn son
katmanlara geldğnde grd le aynı ölçekte olmayablr . Grdlern ağdak katmanlara dağılımındak bu
değşklk, teknk adıyla “ç ortak değşken kayması” ( nternal covarate shft ) olarak adlandırılır (Brownlee,
2019a). Batch normalzasyon, br gzl katman le dğer br gzl katman arasına yerleştrlen başka br ağ
katmanıdır . Batch normalzasyonun görev, lk gzl katmandan çıktıları almak ve bunları br sonrak gzl
katmanın grds olarak aktarmadan önce normalze etmektr (Dosh, 2021). Eğtm sırasında ağ her sefernde
br mn ver yığınıyla beslenr . İler geçş sırasında ağın her katmanı bu mn ver yığınını şler .
Drop-out : YSA  modeller çn Srvastava ve dğ. (2014) tarafından önerlen br düzenl hale getrme
(regularzaton ) teknğdr (Brownlee, 2022a). Drop-out le rastgele seçlen nöronlar , ağın eğtm sırasında
göz ardı edlr . Drop-out le ler besleme aşamasında br sonrak katmanda yer alan nöronların aktvasyonuna
katkıları kaldırılmış olur . Ger besleme aşamasında se nörona herhang br ağırlık güncellemes uygulanmaz.
Eğtm sırasında nöronlar rastgele ağdan çıkarılırsa, dğer nöronların devreye grmes ve eksk nöronlar çn


öğrenlen brden fazla bağımsız ç temsl oluşmaktadır . Drop-out le nöronların belrl ağırlıklara daha az
duyarlı hale gelmes mümkün olur . Böylece daha y genelleme yapablen ve eğtm verlerne aşırı uyum
sağlama olasılığı daha düşük br YSA  elde edlmş olur .

### 10.1.5. Yapay Snr Ağlarının Avantaj ve Dezavantajları

YSA ’nın bazı avantaj (+) ve dezavantajları (-) aşağıda verlmştr (Donges, 2019; Lancashre vd., 2009;
Mjwl, 2018; Özen, 2022; Sngh, 2021):
+ Esneklk ve Adaptasyon:  YSA'lar , çeştl ver türlern ve karmaşık lşkler modelleme yeteneğne
sahptr . Gürültülü ve eksk veryle çalışma toleransları bulunmaktadır . YSA'lar , günümüzde görüntü tanıma,
ses tanıma, doğal dl şleme, otomatk sürüş gb brçok farklı alanda kullanılmaktadır .
+ Paralel İşleme:  YSA'lar , brçok yapay snr hücresnden oluşan paralel br yapıya sahp olablrler . Bu
özellk, belrl uygulamalarda hızlı ve etkl hesaplamalara olanak tanır .
+ Doğrusal Olmayan  (Non-Lnear ) İlşkler Modelleme:  YSA'lar , doğrusal olmayan ve karmaşık lşkler
modelleme yeteneğne sahptr . Bu, gerçek dünyadak brçok problem ele almak çn önemldr .
- Verye Duyarlılık:  YSA'lar , eğtm verlerne oldukça duyarlı olablrler . Eğtm verlerndek gürültü veya
hata, modeln nha performansını olumsuz etkleyeblr .
- Hesaplama Malyet:  YSA ’nın öğrenme sürec ağdak ağırlıklar , grd vektörü boyutu, katman ve nöron
sayısı arttıkça uzayacaktır . Bu nedenle de ağın eğtm zaman alablmektedr . Özellkle de dern YSA'lar ,
büyük mktarda very şleme yeteneğ çn yoğun hesaplama gücü gerektrr . Bu sebeple eğtm ve tahmn
aşamalarında CPU’lara nazaran daha hızlı hesaplama yapablen GPU terch edlr .
- Açıklanablrlk Sorunu:  YSA, kara kutu (black-box) yöntemler olarak blnmektedr . Grd-çıktı arasında
kesn br matematksel eşleme olmaması ya da çıktılardan orjnal vernn ger döndürülememes nedenyle
br kararın neden ya da nasıl alındığına dar blg ednmek neredeyse mkânsızdır (Bostrom & Yudkowsky ,
2014; Kartal, 2022; Marshan & Marshan, 2021). YSA ’nın kara kutu yapısı nedenyle, dern öğrenme
sonucunda verlen kararlar kolayca yorumlanamaz (Kartal & Schwartz, 2022). Bu sebeple YSA  modelnn ç
çalışma mekanzmasını açıklamak veya yorumlamak zor olablr .
- Eğtm Aşamasında Verye Duyulan İhtyaç:  YSA, eğtm aşamasında genellkle büyük mktarda verye
htyaç duymaktadır .
- Nümerk Ver le Çalışma:  YSA ’nın br başka öneml özellğ se yalnızca nümerk (sürekl ve ayrık)
ntelklerle çalışablmesdr . Dolayısıyla kategork ntelklern nümerk halde ağa sunulması gerekmektedr .
- Uygun Ağ Yapısının Belrlenmes ve Parametr elern Ayarlanması:  Daha önce de belrtldğ gb
YSA ’dak ara katman sayısının ve ara katmandak nöron sayısının belrleneblmes çn kesn kurallar mevcut
olmayıp, yalnızca çeştl önerler söz konusudur . Bu nedenle problem çn kullanılması gereken ağ yapısı
deneme yanılma yöntem le bulunmaktadır (Kartal, 201 1; Öztemel, 2006). YSA  modelnde çok sayıda
parametre olması (öğrenme oranı, momentum gb) ve bunlara uygun değerlern belrlenmes, toplama ve
aktvasyon fonksyonlarının seçm analz yapan araştırmacı tarafından belrlenr . Bu da halyle zaman
almaktadır .

## 10.2. Yapay Snr  Ağları le Python Uygulaması

Bu çalışmada kullanılan ver set ( Rce_Cammeo_Osmanck.arff ), UCI Makne Öğrenmes ver deposundan
temn edlmştr (Cnar & Koklu, 2019): https://archve.cs.uc.edu/dataset/545/rce+cammeo+and+osmanck .
Ver setnde; Türkye'de yetştrlen sertfkalı prnçler arasından 1997 yılından ber genş br ekm alanına
sahp olan “Osmancık” türü ve 2014 yılından ber yetştrlen “Cammeo” türüne at ntelkler bulunmaktadır
(Tablo 30). Osmancık türünün genel özellklerne bakıldığında genş, uzun, camsı ve mat br görünüme;
Cammeo türünün genel özellklerne bakıldığında se genş ve uzun, camsı ve mat br görünüme sahp olduğu
fade edlmektedr . İk türden prnç tanelernn görüntüsü alınmış, şlenmş ve özellk çıkarımları yapılmıştır .


Bu çalışmanın temel amacı; prnç tanelerne lşkn morfolojk özellkler kullanarak, prnçlern
Osmancık/Cammeo şeklnde sınıflandırılablmesdr . Ver setnde toplamda 3810 adet gözlem, 8 adet ntelk
bulunmaktadır . Hedef ntelk ( Target ) k kategorden meydana gelmektedr . Dolayısıyla kl sınıflandırma
yapılacaktır .
Tablo 30: Prnç ver setndek ntelkler .
Ntelk Türkçes Açıklama Ver Tp
Area Alan Prnç tanesnn sınırları çndek pksel
sayısını verr .Nümerk
Permeter Çevre Prnç tanesnn sınırları etrafındak pkseller
arasındak mesafey hesaplayarak çevrey
hesaplar .Nümerk
Major Axs Length Ana Eksen
UzunluğuPrnç tanes üzerne çzleblecek en uzun
çzgy, yan ana eksen mesafesn verr .Nümerk
Mnor Axs Length Küçük Eksen
UzunluğuPrnç tanes üzerne çzleblecek en kısa
çzg, yan küçük eksen mesafesn verr .Nümerk
Eccentrcty Eksantrklk Prnç tanes le aynı momentlere sahp olan
elpsn ne kadar yuvarlak olduğunu ölçer .Nümerk
Convex Area Dışbükey Alan Prnç tanesnn oluşturduğu bölgenn en
küçük dışbükey kabuğunun pksel sayısını
verr.Nümerk
Extent Kapsam Prnç tanesnn oluşturduğu bölgenn
sınırlayıcı kutu pksellerne oranını verrNümerk
Class (T arget) Sınıf Commeo ve Osmanck. Kategork


### 10.2.1. Çalışma çn Gerekl Kütüphanelern Yüklenmes

Öncek bölümlere benzer şeklde bu bölümde de NumPy , Pandas  ve Sckt-learn  kütüphaneler kullanılmıştır
(C. R. Harrs vd., 2020; McKnney , 2010; Pedregosa vd., 201 1). Ayrıca YSA  le çalışmak çn TensorFlow  ve
Keras  kütüphanelernden faydalanılmıştır (Chollet & others, 2015; Martín Abad vd., 2015). Bu nedenle eğer
Python’da adı geçen kütüphaneler yüklü değlse, Bölüm 3.1.’de açıklandığı gb bu kütüphaneler yüklenmel,
aşağıdak kod bloğu yardımı le çağrılmalıdır .


### 10.2.2. Ver Okuma

Analzler öncesnde çalışma klasörünün oluşturulması ve Spyder ’dak hazırlık sürec le lgl Bölüm
3.1.’dek şlemlern bu bölüm kapsamında da yapılması önerlmektedr . Ver set Python le okunmadan önce
Rce_Cammeo_Osmanck.arff  ver dosyası “Not Defter” gb br metn edtörü le açılmalı ve @DA TA
fades de dahl olmak üzere @DA TA fadesnn üzernde kalan tüm fadeler slnmeldr . Yan


Rce_Cammeo_Osmanck.arff  dosyası Pandas  kütüphanesnden pd.read_csv()  fonksyonu yardımı le
okunmuştur .


Spyder edtörünün sol üst tarafında yer alan “V arable Explorer” penceresnde bulunan verSet  nesnesne
tıklanarak ver set ayrı br pencerede açılablr ve nceleneblr .


### 10.2.3. Ver Ön-şleme

Ver set okunduktan sonra ntelk adları Türkçeleştrlmştr . Ver setndek ntelk adları sırasıyla; “ Alan,
Cevr e, Ana_Eks_Uz, Kuc_Eks_Uz, Eksan, DsBukey_Alan, Kapsam, Snf ” olacak şeklde yenden
düzenlenmştr . Hedef ntelğn sınıflarına at frekans değerler yazdırılmıştır . Buna göre; 2180 adet Osmanck
ve 1630 adet Cammeo türüne at gözlem ver setnde yer almaktadır . Ardından hedef ntelğn Osmanck ve
Cammeo kategorler 0 ve 1 olarak değştrlmştr . Bu değşklğn sebeb YSA ’nın yalnızca nümerk değerler
le çalışablmesdr . Yan lgl örneğn hedef ntelğnn 0 olması o örneğn Osmanck türüne at olduğu, 1
olması se Cammeo türüne at olduğu anlamına gelr . Son olarak, hedef ntelğn frekans dağılımı yenden


Ver setndek ntelklern ver tp ncelendğnde tümünün nümerk olduğu görüleblr (sürekl değer alanlar
float64, tam sayı değer alanlar nt64). Ver setnde eksk değer bulunmamaktadır .


Ver setnn özetnn elde edleblmes çn aşağıdak kod bloğu kullanılmıştır . Br öncek bölümde de
kullanıldığı gb tüm ntelklern aynı anda görüleblmes çn Pandas ’ın dsplay .max_columns  parametres
20 olarak belrlenmştr . Ver set özet ncelendğnde ntelklern farklı aralıklarda değştğ görüleblr .
Örneğn Alan  ntelğnn en yüksek değer 18913 ken Eksen ’n en yüksek değer yaklaşık 0.95’ tr. Bu


tran_test_splt()  fonksyonu yardımı le ver setnn %70’ eğtm, %30’u test ver set olacak şeklde kye
ayrılmıştır . Eğtm ver set çn tahmn sağlayan ntelkler ( verSet.loc[:,0:7] ) X_tran , hedef ntelk
(verSet.loc[:,7] ) y_tran , test ver setndek hedef ntelkler X_test , hedef ntelk se y_test  değşkenlerne
atanmıştır . random_state  parametres 1903 olarak seçlmştr; ancak bu yne br zorunluluk değldr . Her
sefernde aynı örneklern aynı ver setnde yer alması stendğnden böyle yapılmıştır . Okuyucu
random_state  parametresn kend steğne uygun şeklde belrleyeblr .


sklearn.pr eprocessng  modülünden MnMaxScaler  mnmum-maksmum normalzasyon yöntem çn
çağırılmıştır . Normalzasyon çn öncelkle scaler .ft_transform() fonksyonu  X_tran ’e uygulanmış ve
eğtm ver setndek tüm ntelkler 0 le 1 arasında olacak şeklde ayarlanmıştır . Ardından scaler  nesnesnn
eğtm ver setnden öğrendğ parametreler scaler .transform() fonksyonu yardımı le X_test ’e
uygulanmıştır .


### 10.2.4. Modelleme

YSA  modelnn ( ysa_model ) oluşturulablmes çn Keras  kütüphanesnden Sequental()  fonksyonu
kullanılmıştır . Bu fonksyon sıralı katman yapısında ağ kurulmasını sağlamaktadır . Ardından ysa_model
modelne, ysa_model.add() kullanılarak sırayla grd katmanı ( InputLayer ), 2 adet ara katman ( Dense ) ve
çıktı katmanı ( Dense ) eklenmştr . Grd katmanının görev yalnızca grdler sonrak katmana letmektr . Bu
katmanda herhang br hesaplama yapılmamaktadır . Dolayısıyla yalnızca grd katmanında kaç nöronun yer
alacağı blgs ve katman adı tanımlanmıştır . Ardından gelen lk ara katmanda 4, kncsnde 3 nöron yer
alacak şeklde ara katmanlar yapılandırılmıştır . Her k ara katmanın da aktvasyon fonksyonu ReLU
seçlmş, katmanlara smler verlmştr (Ara_Katman_1, Ara_Katman_2). Çıktı katmanında se ağın
çıktısının 0 le 1 arasında br değer alması çn aktvasyon fonksyonu olarak sgmod  kullanılmıştır . Öncek
katmanlarda olduğu gb katman sm tanımlanmıştır (Ckt_Katman). Oluşturulan modeln özet blgs
ysa_model.summary() le elde edlmştr (Şekl 1 16).


Şekl 116: YSA  model.
YSA  modelnn genel yapısı belrlendkten sonra modeln eğtm çn seçleblecek optmzasyon yöntem


performans değerlendrme ölçütü ( bnary_accuracy ) gb bazı parametrelern belrlenmes
ysa_model.comple()  le gerçekleştrlr . Keras’ ta sgd sınıfı modeln ağırlıklarının güncellenmes çn
stokastk gradyan nş yöntemn temsl etmektedr . Momentum ve öğrenme oranı da berabernde
kullanılablmektedr . Bunların varsayılan değer sırasıyla 0.01 ve 0.0’dır . Probleme göre kayıp fonksyonu;
MeanAbsoluteErr or(), MeanSquar edErr or(), BnaryCr ossentr opy() , CategorcalCr ossentr opy() ,
SparseCategorcalCr ossEntr opy()  ya da farklı br fonksyon Keras ’tan seçleblr .


Öğrenme oranı ve momentumun varsayılan parametreler le kullanılmak stenmezse ya da farklı
parametreler le çalışılmak stenrse bu durumda aşağıdak kod bloğu yardımı le parametrelere alternatf
şeklde değer ataması yapılablr (Brownlee, 2019b).


YSA  model aşağıdak kod yardımı le eğtlr . Öncek danışmanlı öğrenme uygulamalarındakne benzer
şeklde, eğtm ver setnde yer alan tahmn sağlayan ntelkler ( X_tran ) ve hedef ntelk ( y_tran ) ağa
sunulur . Ardından eğtm performansının değerlendrleblmes çn eğtm versnn %20’ s doğrulama ver
set ( valdaton_splt ) olarak kullanılacaktır . Yne YSA ’nın terasyon sayısı olan epochs  300 olarak
belrlenmştr . Batch boyutu ( batch_sze ) 32 seçlmştr . Bu değer aynı zamanda batch boyutu çn varsayılan
değerdr . verbose , eğtm sürecnn lerleyşnn her epoch çn nasıl görüleceğne lşkn parametredr .
verbose=1  alınması lerleme çubuğunun ( progress bar ) görüntülenmesn sağlar .


Eğtm süresnce eğtm ve doğrulamada elde edlen doğruluk ve kayıp fonksyonu sonuçları her br epoch


Şekl 117: YSA  modelnn eğtm.
Öneml Not:  YSA ’larında ağırlıkların başlangıç değer rastgele atanmaktadır . Dolayısıyla ağ her
çalıştırıldığında farklı ağırlıklarla başlatılacaktır . Bu sebeple ağın eğtm ve testnde elde edlen performans
değerlendrme sonuçları, çalıştırılan blgsayara göre az da olsa farklı olablecektr .

### 10.2.5. Performans Değerlendrme

YSA  modelnn test ver setndek performansını elde etmek çn aşağıdak kod bloğu kullanılablr . Modeln
doğruluğu %93, kaybı ( loss) da %17 olarak elde edlmştr .


Test ver setndek her br örnek çn modeln tahmn değerler . predct() fonksyonu yardımı le elde
edleblr; ancak elde edlecek tahmn değerler son katmanda kullanılan sgmod fonksyonu nedenyle 0 le 1
arasındak olasılık değerler olacaktır ( y_tahmn_degerler ). Bu değerlern test ver setndek gerçek sınıf
değerler le br karmaşıklık matrs yardımı le değerlendrleblmes çn aşağıdak kod bloğundak gb br
eşk değer (0.5) belrleneblr . Bu değern üzerndekler 1, bu değere eşt ya da bu değerden küçük olanlar se


Ardından confuson_matrx()  fonksyonu le kontenjans tablosu oluşturulmuştur . Burada poztf sınıf olarak
dyabet hastalığı seçlmştr . Daha sonra da ConfusonMatrxDsplay()  ve .plot()  fonksyonları yardımı le
kontenjans tablosunun görüntülenmes sağlanmıştır .


Kontenjans tablosundak tn, tp, fn, fp değerlernn sırasıyla aynı smlerde tanımlanan değşkenlere


classfcaton_r eport()  le en temel performans değerlendrme ölçütler elde edlmştr .


Yukarıda elde edlen performans metrkler raporuna göre YSA  modelnn doğruluğunun %93 olduğu br kez
daha görüleblr . Modeln makro ortalama kullanılarak (Cammeo ve Osmanck türler çn hesaplanan
performans değerlendrme ölçütlernden her br çn ortalama) nha performansı değerlendrlrse; duyarlılık,
kesnlk ve F-Ölçüsünün de %93 olduğu görülecektr . Bu değerlern prnç türlerne göre yorumu se hang
türün poztf sınıf kabul edldğne göre değşecektr . Elbette performans değerlendrme raporunda her k
sınıf çn ayrı ayrı elde edlen değerler de görüleblr .


Bu ktap bölümünde Yapay Snr  Ağları  – YSA  (Artfcal Neural Networks ) çn kapsamlı br grş
sunulmuş, byolojk snr hücrelernden lham alan yapay snr hücrelernn ( neuron) temel bleşenler ve
çalışma prenspler açıklanmıştır . Yapay snr ağlarının yapısı ve şleyş detaylı br şeklde ncelenmş, grş,
çıkış ve gzl katmanların rolü, toplam ve aktvasyon fonksyonları üzernde durulmuştur . Farklı ağ
topolojler le bazı y blnen YSA  mmarlerne değnlmştr . Bölümde ele alınan uygulama gereğ; çok-
katmanlı algılayıcı  YSA  (Mult-Layer Per ceptr on Neural Networks ) le gerye yayılım (back-pr opagaton )
algortması  detaylı bçmde sunulmuştur . Epoch , ağırlıklara başlangıç değer atanması  (weght
ntalzaton ), batch boyutu  (batch sze ), batch normalzasyon  ve drop-out  gb YSA  lşkl kavramları
açıklanmıştır . Ayrıca YSA'nın avantaj ve dezavantajları sayılmış, bu teknolojnn güçlü yönler le karşılaşılan
zorlukları vur gulanmıştır .
Python uygulamasında YSA  le prnç örneklernn Osmancık/Cammeo olarak sınıflandırması
gerçekleştrlmştr . Bu bölüm okuyuculara hem teork hem de pratk açıdan YSA ’yı anlama ve kullanma
konusunda temel br deneym sunmaktadır . Bu kazanılan deneymn pekştrlmes çn okuyuculara farklı
ver setler üzernde çalışması  önerlmektedr .


**Kaynakça**

Aggarwal, C. C. (2018). Neural networks and deep learnng . Sprnger Internatonal Publshng.
Alexander , D. (2020). Neural networks: Hstory and applcatons . Nova Scence Publshers, Incorporated.
Averkn, A., & Yarushev , S. (2018). Evoluton of Artfcal Neural Networks. Открытые с емантиче ские
технологии проек тиров ания инте ллектуальных систе м, 8, 255-259.
Bostrom, N., & Yudkowsky , E. (2014, Hazran). The ethcs of artfcal ntellgence . The Cambrdge
Handbook of Artfcal Intellgence; Cambrdge Unversty Press.
https://do.or g/10.1017/CBO9781 139046855.020
Brownlee, J. (2019a, Ocak 15). A Gentle Introducton to Batch Normalzaton for Deep Neural Networks.
MachneLearnngMastery .Com . https://machnelearnngmastery .com/batch-normalzaton-for -tranng-of-
deep-neural-networks/
Brownlee, J. (2019b, Ocak 24). Understand the Impact of Learnng Rate on Neural Network Performance.
MachneLearnngMastery .Com . https://machnelearnngmastery .com/understand-the-dynamcs-of-learnng-
rate-on-deep-learnng-neural-networks/
Brownlee, J. (2021, Şubat 2). Weght Intalzaton for Deep Learnng Neural Networks.
MachneLearnngMastery .Com . https://machnelearnngmastery .com/weght-ntalzaton-for -deep-learnng-
neural-networks/
Brownlee, J. (2022a, Temmuz 5). Dropout Regularzaton n Deep Learnng Models wth Keras.
MachneLearnngMastery .Com . https://machnelearnngmastery .com/dropout-regularzaton-deep-learnng-
models-keras/
Brownlee, J. (2022b, Ağustos 9). Df ference Between a Batch and an Epoch n a Neural Network.
MachneLearnngMastery .Com . https://machnelearnngmastery .com/df ference-between-a-batch-and-an-
epoch/
Chng, Z. M. (2022, Temmuz 15). Loss Functons n TensorFlow . MachneLearnngMastery .Com .
https://machnelearnngmastery .com/loss-functons-n-tensorflow/
Chollet, F . (2018). Deep learnng wth python . Mannng Publcatons Co.


Cnar , I., & Koklu, M. (2019). Classfcaton of rce varetes usng artfcal ntellgence methods.
Internatonal Journal of Intellgent Systems and Applcatons n Engneerng , 7(3), 188-194.
https://do.or g/10.18201/jsae.2019355381
Donges, N. (2019). 4 Dsadvantages of Neural Networks | Bult In . Bultn. https://bultn.com/data-
scence/dsadvantages-neural-networks
Dosh, K. (2021, Mayıs 29). Batch Norm Explaned V sually—How t works, and why neural networks need
t. Medum. https://towardsdatascence.com/batch-norm-explaned-vsually-how-t-works-and-why-neural-
networks-need-t-b18919692739
Elmas, Ç. (2007). Yapay Zeka Uygulamaları  (1. Baskı). Seçkn Yayıncılık.
Fausett, L. V. (1994). Fundamentals of neural networks: Archtectur es, algorthms and applcatons . Prentce
Hall.
GeoGebra. (2023). GeoGebra—100 mlyondan fazla öğr enc ve öğr etmen tarafından kullanılan ücr etsz
matematk araçları . GeoGebra. https://www .geogebra.or g/
Goodfellow , I., Bengo, Y., & Courvlle, Aaron. (2016). Deep Learnng  (1. bs). MIT  Press.
Ha, G. E., & Cheong, E. (2017). Spke Frequency Adaptaton n Neurons of the Central Nervous System.
Expermental Neur obology , 26(4), 179-185. https://do.or g/10.5607/en.2017.26.4.179
Harrs, C. R., Mllman, K. J., Walt, S. J. van der , Gommers, R., Vrtanen, P ., Cournapeau, D., Weser , E.,
Taylor , J., Ber g, S., Smth, N. J., Kern, R., Pcus, M., Hoyer , S., Kerkwjk, M. H. van, Brett, M., Haldane, A.,
Río, J. F . del, Webe, M., Peterson, P ., … Olphant, T. E. (2020). Array programmng wth NumPy . Natur e,
585(7825), 357-362. https://do.or g/10.1038/s41586-020-2649-2
Haykn, S. (1999). Neural networks: A compr ehensve foundaton  (2nd Edton). Prentce Hall PTR.
Heaton, J. (2017, Hazran 1). The Number of Hdden Layers . Heaton Research.
https://www .heatonresearch.com/2017/06/01/hdden-layers.html
Hetler . (2019). Acton Potentals (Spkes) . https://www .st-
andrews.ac.uk/~wjh/neurosm/T utoralV5_3/Spkes.html
Hrolenok, B. (2009). Recurr ent Neural Networks . https://cs.gmu.edu/~hrolenok/rnn_sldes.pdf
Jaeger , H. (2002). Tutoral on tranng recurrent neural networks, coverng bppt, rtrl, ekf and the"‘echo state
network. Gesellschaft für Mathematk und Datenverarbetung Report , 159.
Jalloul, R., Chethan, H. K., & Alkhatb, R. (2023). A Revew of Machne Learnng Technques for the
Classfcaton and Detecton of Breast Cancer from Medcal Images. Dagnostcs , 13(14), Artcle 14.
https://do.or g/10.3390/dagnostcs13142460
Kartal, E. (201 1). Yapay Snr Ağları le Y azılım Pr ojes Malyet T ahmn  [Yüksek Lsans Tez]. İstanbul
Ünverstes Fen Blmler Ensttüsü.
Kartal, E. (2022). A Comprehensve Study on Bas n Artfcal Intellgence Systems: Based or Unbased AI,
That’ s the Queston! Internatonal Journal of Intellgent Informaton T echnologes (IJIIT) , 18(1), 1-23.
https://do.or g/10.4018/IJIIT .309582
Kartal, E., & Schwartz, O. (2022). What Is Deep Learnng and How Has It Helped the COVID-19 Pandemc?
İçnde Ş. Omerak Çekrdekc, Ö. İngün Karakış, & S. Gönültaş (Ed.), Handbook of Resear ch on
Inter dscplnary Perspectves on the Thr eats and Impacts of Pandemcs  (1. bs, ss. 337-360). IGI Global;
10.4018/978-1-7998-8674-7.ch018. https://www .g-global.com/chapter/what-s-deep-learnng-and-how-has-


Kresel, D. (2007). A bref ntr oducton to neural networks .
http://www .dkresel.com/en/scence/neural_networks
Krose, B., & van der Smagt, P . (1996). An Intr oducton to Neural Networks . The Unversty of Amsterdam.
Lancashre, L. J., Lemetre, C., & Ball, G. R. (2009). An ntroducton to artfcal neural networks n
bonformatcs—Applcaton to complex mcroarray and mass spectrometry datasets n cancer studes.
Brefngs n bonformatcs , 10(3), 315-329.
Macukow , B. (2016). Neural networks–state of art, bref hstory , basc models and archtecture. Computer
Informaton Systems and Industral Management: 15th IFIP  TC8 Internatonal Confer ence, CISIM 2016,
Vlnus, Lthuana, September 14-16, 2016, Pr oceedngs 15 , 3-14.
Marshan, A., & Marshan, A. (2021). Artfcal ntellgence: Explanablty , ethcal ssues and bas. Annals of
Robotcs and Automaton , 5(1), 034-037. https://do.or g/10.17352/ara.00001 1
Martín Abad, Ashsh Agarwal, Paul Barham, Eugene Brevdo, Zhfeng Chen, Crag Ctro, Greg S. Corrado,
Andy Davs, Jef frey Dean, Mattheu Devn, Sanjay Ghemawat, Ian Goodfellow , Andrew Harp, Geof frey
Irvng, Mchael Isard, Ja, Y., Rafal Jozefowcz, Lukasz Kaser , Manjunath Kudlur , … Xaoqang Zheng.
(2015). TensorFlow: Lar ge-Scale Machne Learnng on Heter ogeneous Systems . https://www .tensorflow .org/
McCulloch, W. S., & Ptts, W. (1943). A logcal calculus of the deas mmanent n nervous actvty . The
bulletn of mathematcal bophyscs , 5, 115-133.
McKnney , W. (2010). Data Structures for Statstcal Computng n Python. İçnde S. van der Walt & J.
Mllman (Ed.), Proceedngs of the 9th Python n Scence Confer ence (ss. 56-61).
https://do.or g/10.25080/Majora-92bf1922-00a
Mjwl, M. M. (2018). Artfcal Neural Networks Advantages and Dsadvantages. Mesopotaman Journal of
Bg Data , 29-31. https://do.or g/10.58496/MJBD/2021/006
Mnsky , M., & Papert, S. (1969). Perceptrons An ntroducton to computatonal geometry . Cambrdge tass.,
HIT, 479(480), 104.
Muzo, M. R., & Cascella, M. (2024). Hstology , Axon. Içnde StatPearls . StatPearls Publshng.
http://www .ncb.nlm.nh.gov/books/NBK554388/
Olmsted, D. D. (1998). Hstory and prncples of neural networks . Academc Press.
Özen, Z. (2016). Kmlk Doğrulaması çn T uş Vuruş Dnamklerne Dayalı Br Güvenlk Sstemnn Y apay
Snr Ağları le Gelştrlmes  [Doktora Tez]. İstanbul Ünverstes Fen Blmler Ensttüsü.
Özen, Z. (2022). Yapay Snr Ağları. İçnde N. Bayram Arlı, S. Gürsakal, & M. Engn (Ed.), Denetml
Makne Öğr enmes Algortmaları R ve Python Uygulamaları  (1. Baskı, ss. 215-261). Nobel Akademk
Yayıncılık.
Özen, Z., Kartal, E., & Gülseçen, S. (2017). Yapay Zekâ ve Yapay Snr Ağları. İçnde T. R. Çölkesen & O.
Alefendoğlu (Ed.), Blgsayar Blmne Grş  (1. Baskı, ss. 523-558). Papatya Blm Ktabev.
Öztemel, E. (2006). Yapay snr ağlar  (2. Basım). Papatya Blm.
Pedregosa, F ., Varoquaux, G., Gramfort, A., Mchel, V., Thron, B., Grsel, O., Blondel, M., Prettenhofer , P.,
Wess, R., Dubour g, V., & others. (201 1). Sckt-learn: Machne learnng n Python. Journal of machne
learnng r esear ch, 12(Oct), 2825-2830.
Pres, P . B., Santos, J. D., & Perera, I. V. (2025). Artfcal Neural Networks: Hstory and State of the Art.
Encyclopeda of Informaton Scence and T echnology , Sxth Edton , 1-25.
Pres, P ., Santos, J., & Perera, I. (2023). Artfcal Neural Networks: Hstory and State of the Art.


Prddy , K. L., & Keller , P. E. (2005). Artfcal Neural Networks: An Intr oducton . SPIE Press.
Rosenblatt, F . (1958). The perceptron: A probablstc model for nformaton storage and or ganzaton n the
bran. Psychologcal r evew , 65(6), 386.
Rumelhart, D. E., Hnton, G. E., & Wllams, R. J. (1986). Learnng nternal representatons by error
propagaton. İçnde Arallel Dstrbuted Pr ocessng: Exploratons n the Mcr ostructur e of Cognton  (C. 1, ss.
318-362). MIT  Press.
Sarkara, S. (2012). Backpopagaton . http://courses.ece.ubc.ca/592/PDFfles/Backpropagaton_c.pdf
Saxena, S. (2021, Mart 9). Introducton to Batch Normalzaton. Analytcs V dhya .
https://www .analytcsvdhya.com/blog/2021/03/ntroducton-to-batch-normalzaton/
Sngh, G. (2021, Eylül 6). Introducton to Artfcal Neural Networks. Analytcs V dhya .
https://www .analytcsvdhya.com/blog/2021/09/ntroducton-to-artfcal-neural-networks/
Srvastava, N., Hnton, G., Krzhevsky , A., Sutskever , I., & Salakhutdnov , R. (2014). Dropout: A Smple
Way to Prevent Neural Networks from Overfttng. Journal of Machne Learnng Resear ch, 15(56), 1929-
1958.
Wdrow , B., & Hof f, M. E. (1960). Adaptve swtchng crcuts. IRE WESCON conventon r ecord, 4(1), 96-
104.
Yamns, D. L., & DCarlo, J. J. (2016). Usng goal-drven deep learnng models to understand sensory cortex.
Natur e neur oscence , 19(3), 356


**Ünte Soruları**

Soru-1 :
Aşağıda verlen araştırmacılardan hangsnn Yapay Snr Ağları’na (YSA) doğrudan katkısı olmamıştır ?
(Çoktan Seçmel)
(A) Warren McCulloch
(B) Walter Ptts
(C) Frank Rosenblatt
(D) Davd E. Rumelhart
(E) Claude Shannon
Cevap-1 :
Claude Shannon


Aşağıdaklerden hangs yapay br snr hücresne verlen adlardan br değldr ?
(Çoktan Seçmel)
(A) Snaps
(B) İşlem brm
(C) Yapay nöron
(D) Proses eleman
İşlem elemanı
Cevap-2 :
Snaps
Soru-3 :
Aşağıdaklerden hangs yapay br nöronda kullanılan aktvasyon/transfer fonksyonlarından brdr?
(Çoktan Seçmel)
(A) Ağırlıklı toplam
(B) Çarpım
(C) ReLU
(D) Mnmum
Maksmum
Cevap-3 :
ReLU
Soru-4 :
Aşağıdaklerden hangs ya da hangler YSA ’larının temel topolojler arasındadır?
I. Ger-yayılım
II. İler beslemel
III. Tam bağlantılı
IV. Ynelemel
V. Adelne
(Çoktan Seçmel)
(A) Yalnız I


(C) II ve III
(D) II, III ve IV
III, IV  ve V
Cevap-4 :
II, III ve IV
Soru-5 :
Aşağıdaklerden hangs çok-katmanlı algılayıcı YSA ’da grd katmanının görevdr?
(Çoktan Seçmel)
(A) Vernn ara katmanlara gtmeden önce net grdnn hesaplandığı katmandır .
(B) Herhang br hesaplamanın gerçekleştrlmedğ, vernn yalnızca br sonrak katmana letldğ katmandır .
(C) YSA ’da transfer fonksyonu kullanılan tek katmandır .
(D) YSA ’da toplama fonksyonu kullanılan tek katmandır .
Yalnızca tek br yapay nörona sahp verye toplama ve aktvasyon fonksyonlarının uygulandığı katmandır .
Cevap-5 :
Herhang br hesaplamanın gerçekleştrlmedğ, vernn yalnızca br sonrak katmana letldğ katmandır .
Soru-6 :
Aşağıda verlenlerden kaç tanes YSA  türler/mmarler arasındadır?
• Çok-Katmanlı Algılayıcı YSA
• Radyal Taban Fonksyonlu YSA
• Uzun Kısa Sürel Bellek YSA
• Oto-kodlayıcı YSA
• Öğrenmel Vektör Ncemleme YSA
(Çoktan Seçmel)
(A) 1
(B) 2
(C) 3
(D) 4
(E) 5


5
Soru-7 :
Br YSA  modelnn öğrenmey gerçekleştrmes aşağıdaklerden hangsyle aynı anlamı taşır?
(Çoktan Seçmel)
(A) Ağırlıkların ayarlanması
(B) Epoch sayısı
(C) Batch boyutu
(D) Öğrenme oranı
Aktvasyon fonksyonu
Cevap-7 :
Ağırlıkların ayarlanması
Soru-8 :
YSA  le lgl aşağıda verlen şıklardan hangs doğrudur?
(Çoktan Seçmel)
(A) Br YSA ’da her ara katmanda 5 adet yapay nöron bulunur .
(B) Br YSA ’nın çıktı katmanında yalnızca 1 adet yapay nöron bulunur .
(C) Br YSA  en az 500 epoch le çalıştırılmalıdır .
(D) Br YSA  yalnızca nümerk ntelklerle çalışır .
Br YSA  model yalnızca danışmanlı öğrenme problemlernn çözümünde kullanılablr .
Cevap-8 :
Br YSA  yalnızca nümerk ntelklerle çalışır .
Soru-9 :
Aşağıdaklerden hangs rastgele seçlen nöronların ağın eğtm sırasında göz ardı edlmes amacıyla
kullanılır?
(Çoktan Seçmel)
(A) Batch boyutu
(B) Drop-out
(C) Momentum


Kara-kutu
Cevap-9 :
Drop-out
Soru-10 :
Aşağıdaklerden hangs ya da hangler Python dlnde YSA  model kurulmasını sağlayan
kütüphanelerndendr?
I. Keras
II. Numpy
III. Pandas
IV. TensorFlow
V. Seaborn
(Çoktan Seçmel)
(A) I ve II
(B) I ve III
(C) I ve IV
(D) II, III ve IV
III, IV  ve V
Cevap-10 :
