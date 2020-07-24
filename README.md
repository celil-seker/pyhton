# pyhton
# Karakter Dizilerine Giriş


```python

"celil"

```




    'celil'




```python
"celil"+"seker"

```




    'celilseker'




```python
"celil"+" "+"seker"
```




    'celil seker'



+işareti 2 veya daha fazla karekterin birleştirilmesi işlemini yapar.


```python
type("celil")

```




    str



type() adlı fonksiyon o verinin tipini sorgular.
parentez içersinde yazılan paremetredir.


```python
"w"*3
```




    'www'




```python
"yavaş"*2
```




    'yavaşyavaş'




```python
"-"*5
```




    '-----'



*işareti karekterin istenilen sayıda tekrarlanarak tek bir karekter içerisinde yazılması işlemini yapar.

*: tekrarlamak
+:birleştirmek

# Sayılara Giriş

pyhtonda farklı sayı türleri vardır.tamsayılar,kayan noktalı sayılar,karmaşık sayılar...


```python
23
45567
```




    45567



Yukarıdaki örnekler arasında geçen 23 ve 4567 birer tamsayıdır.İngilizcede bu tür sayılara integer adı verilir. 


```python
2.3
```




    2.3




```python
(10+2j)
```




    (10+2j)



Noktalı sayılarda basamak ayracı olarak virgül değil,nokta işareti kullandığımız adikkat edin. 
En sonda gördüğümüz 10+2j sayısı ise bir karmaşık sayıdır (complex). 
Ancak eğer matematikle yoğun bir şekilde uğraşmıyorsanız karmaşık sayılar pek karşınıza çıkmaz.



```python
5+2
7/3
8*2
16-5
```




    11



İşleç   Görevi 
+       toplama 
-       çıkarma 
*       çarpma 
/       bölme

Yukarıdaki örneklerde bir şey dikkatinizi çekmiş olmalı:
    Karakter dizilerini tanımlarken tırnak işaretlerinikullandık.
    Ancak sayılarda tırnak işareti yok.
    Daha öncede dediğimiz gibi,tırnak işaretleri karakter dizilerinin ayırt edici özelliğidir.


```python
type(34657)

```




    int



Buradaki‘int’ ifadesi İngilizce “integer”,yani tamsayı kelimesinin kısaltmasıdır. Demekki 34657 sayısı bir tamsayı imiş.


```python
type("34657")
```




    str



Gördüğünüz gibi,34657 sayısını tırnak içine aldığımızda bu sayı artık sayı olma özelliğini yitiriyor ve bir karakter dizisi oluyor. 


```python
45 +"45"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-42-b625be99d149> in <module>
    ----> 1 45 +"45"
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


Gördüğünüzgibi,yukarıdaki kodlar hata veriyor.Bunun sebebi bir sayı(45) ile bir karakter dizisini(“45”)birbiriyle toplamayav çalışmamızdır. Asla unutmayın,aritmetik işlemler ancak sayılar arasında yapılır.Karakter dizileri ile herhangi bir aritmetik işlem yapılamaz.

# Değişkenler

len() Bu fonksiyonun görevi ise karakter dizilerinin (ve ileri de göreceğimi zgibi,başka veri tiplerinin) uzunluğunu ölçmektir.


```python
"rT%65#$hGfUY56123"
```




    'rT%65#$hGfUY56123'




```python
len("rT%65#$hGfUY56123")
```




    17



Nasıl type() fonksiyonu bize, kendisine verdiğimiz parametrelerin tipini söylüyorsa, len() fonksiyonu da kendisine verdiğimiz parametrelerin uzunluğunu söyler. 

sisteme girilen kullanıcıadı ve şifre toplamı 40 karekteri aşmamalı kullanıcı adı "celil_1995") Şifre:"rT%65#$hGfUY56123" 


```python
 len("celil_1995") + len("rT%65#$hGfUY56123") 
```




    27



Buradan alacağımız sonuç 27  olacaktır.Demekki kullanıcı 40 karakterlimitini aşmamış.O halde programımız bu kullanıcıadı ve parolayı kabuledebilir.


```python
 type(len("celil_1995"))

```




    int



Peki nedir budeğişken dediğimiz şey? Python’da bir program içinde değerlere verilen isimlere değişkendenir. Hemen bir örnek verelim: 


```python
n=5
```

Burada 5 sayısını bir değişkene atadık. Değişkenimiz ise n. Ayrıca 5 sayısını bir değişkene atamak için = işaretinden yararlandığımızada çok dikkat edin.Buradan, = işaretinin Python programlama dilinde değer atama işlemleri için kullanıldığı sonucunu çıkarıyoruz. n = 5 gibi bir komut yardımıyla 5 değerini n adlıdeğişkene atamamız sayesinde artık ne zaman 5 sayısına ihtiyaç duysak bundeğişkenini çağırmamız yeterli olacaktır.


```python
n+5
```




    10




```python
n*10
```




    50




```python
n/5
```




    1.0



Gördüğünüz gibi, 5 değerini bir değişkene atadıktan sonra, bu 5 değerini kullanmamız gereken yerlerde sadece değişkenin adını kullandığımızda değişkenin değerini Python otomatikolarakyerinekoyabiliyor.Yani n = 5 komutuyla n adlı bir değişken tanımladıktan sonra,artık nezaman 5 sayısına ihtiyaç duysak n değişkenini çağırmamız yeterli olacaktır. Python o 5 değerini otomatik olarak yerine koyar. 


```python
pi = 3.14 
```


```python
pi+n
```




    8.14



# Değişken Adı Belirleme Kuralları

Python programlama dilinde, değişken adı olarak belirleyebileceğimiz kelime sayısı neredeyse sınırsızdır. Yani hemen hemen her kelimeyi değişken adı olarak kullanabiliriz. Ama yinede değişken adı belirlerken dikkatetmemiz gereken bazı kurallar var.Bu kuralların bazıları zorunluluk,bazıları ise yalnızca tavsiye niteliğindedir.

1. Değişken adları bir sayı ile başlayamaz.Yani şu kullanım yanlıştır:


```python
 3_kilo_elma = "5 TL" 
```


      File "<ipython-input-53-8f2472e93ebc>", line 1
        3_kilo_elma = "5 TL"
         ^
    SyntaxError: invalid token
    


2. Değişken adları aritmetik işleçlerle başlayamaz.Yani şu kullanım yanlıştır: 


```python
 +değer = 4568
```


      File "<ipython-input-54-53e025623b01>", line 1
        +değer = 4568
                     ^
    SyntaxError: can't assign to operator
    


3. Değişken adları y abir alfabe harﬁyle yada _ işaretiyle başlamalıdır: 


```python
 _değer = 4568 
```

4.Aşağıdaki kelimeleri değişken adı olarak kullanamazsınız:
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 

5. Yukarıdaki kelimeler dışında, Python programlama diline ait fonksiyon ve benzeri araçları nadlarınıda değişken adı olarak kullanmamalısınız.Örneğin yazdığınız programlarda değişkenlerinize type veya len  adı vermeyin. Çünkü‘type’ve‘len’Python’aaitikiönemli fonksiyonunadıdır. Eğer mesela bir değişkene type adını verirseniz,o programda artık type()fonksiyonunu kullanamazsınız: 


```python
 type = 3456 
```


```python
type("elma")

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-57-4cfbf307abac> in <module>
    ----> 1 type("elma")
    

    TypeError: 'int' object is not callable


Gördüğünüz gibi,artık type()fonksiyonu çalışmıyor.Çünkü siz‘type’kelimesini bir değişken adı olarak kullanarak,type()fonksiyonunu kullanılamaz hale getirdiniz. Bu durumdan kurtulmak için etkileşimli kabuğu kapatıp tekraraçabilirsiniz. Ya daeğer etkileşiml ikabuğu kapatmak istemiyorsanız şukomut yardımıyla type değişkenini ortadan kaldırmayıda tercih edebilirsiniz: 


```python
del type
```

6. Değişken adlarını belirlerken, değişkeni oluşturan kelimeler arasında boşluk bırakılamaz. Yani şu kullanım yanlıştır: 


```python
kullanıcı adı = "istihza" 
```


      File "<ipython-input-59-b38c29387418>", line 1
        kullanıcı adı = "istihza"
                    ^
    SyntaxError: invalid syntax
    


Yukarıdaki değişkeni şu şekilde tanımlayabiliriz:


```python
kullanıcı_adı = "istihza" 
```

Yada şöyle: 


```python
kullanıcıAdı = "istihza" 
```

7. Değişken adları belirlerken, değişken adının, değişkenin değerini olabildiğince betimlemesine dikkatetmemiz kodlarımızın okunaklılığını artıracaktır.


```python
 personel_sayısı = 45
```

Yukarıdaki,tanımladığı değere uygun bir değişkenadıdır.Şu ise kurallara uygun bir değişken adı olsada yeterince betimleyici değildir:


```python
 sayı = 45 
```

8. Değişkenadları neçok kısa,nede çok uzun olmalıdır. Mesela şu değişkenadı,kodları okuyan kişiye,değişken değerinin anlamı konusunda pek ﬁkirvermez:


```python
a = 345542353 
```

Şudeğişkenadıisegereksizyereuzundur: 


```python
türkiye_büyük_millet_meclisi_milletvekili_sayısı = 550 
```

     Uygulamalar

Pekiyabirsayınınmeselabeşincikuvvetinihesaplamakistersekneyapacağız?Osayıyıbeş kezkendisiylemiçarpacağız?Bunekadarvasatbiryöntem,değilmi? Elbettebirsayınınherhangibirkuvvetinihesaplamakiçinosayıyıkendisiylekuvvetince çarpmayacağız. Python’dabutür‘kuvvethesaplamaları’içinayrıbirişleç(vefonksiyon) bulunur. Önceliklekuvvethesaplarınıyapmamızısağlayanişleçtensözedelim. Python’da** adlıbirişleçbulunur. Buişlecingörevibirsayınınkuvvetinihesaplamamızı sağlamaktır. Örneğinbirsayının2. kuvvetini,yadabaşkabirdeyişlekaresinihesaplamak istersekşöylebirkodyazabiliriz: 


```python
12 ** 2

```




    144



Buişleciherhangibirsayınınherhangibirkuvvetinihesaplamakiçinkullanabilirizelbette. Mesela23sayısınınküpünü(yani3.kuvvetini)hesaplayalım: 


```python
23 ** 3

```




    12167



Dahaönceöğrendiğimizfonksiyonlarıtekbirparametreilebirliktekullanmıştık. pow() fonksiyonuisetoplamüçfarklıparametrealır. Amagenelliklebufonksiyonyalnızcaiki parametreilekullanılır. Bufonksiyonuşöylekullanıyoruz: 


```python
pow(12, 2)

pow(23, 3)

pow(144, 0.5)

```




    12.0



Gördüğünüzgibi,pow()fonksiyonununilkparametresiasılsayıyı,ikinciparametresiisebu sayınınhangikuvvetinihesaplamakistediğimizigösteriyor. Buarada,fonksiyonunparantezleriiçindebelirttiğimizparametreleribirbirindenvirgülile ayırdığımızıgözdenkaçırmayın. Dediğimizgibi, pow() fonksiyonu,pekkullanılmayanüçüncübirparametredahaalır. Bu fonksiyonunüçüncüparametresişöylekullanılır.Dikkatlicebakın: 


```python
pow(16, 2, 2)
```




    0



Bukomutşuanlamagelir: 16sayısının2‘ncikuvvetinihesaplaveçıkansayıyı2‘yebölüp,bölmeişleminden kalansayıyıgöster! 16sayısının2.kuvveti256sayısıdır.256sayısını2‘yeböldüğümüzde,bölmeişlemininkalanı 0‘dır.Yani256sayısı2‘yetambölünür.

                                   Değişkenlere Dair Bazı İpuçları

1. AynıDeğereSahipDeğişkenlerTanımlama

Şimdisizeşöylebirsorusormamaizinverin: Acabaaynıdeğeresahipikideğişkeninasıl tanımlayabiliriz?Yanimeseladeğeri4sayısıolanikifarklıdeğişkeninasılbelirleyeceğiz? Aklınızaşöylebirçözümgelmişolabilir


```python
a = 4 
b = 4
```

geçerlibiryöntemdir.AncakPython’dabuişlemiyapmanındahakolaybiryoluvar.Bakalım: 


```python
 a = b = 4
```

2. DeğişkenlerinDeğeriniTakasEtme

Diyelimki,işyerinizdekipersonelinunvanlarınıtuttuğunuzbirveritabanıvarelinizde. Bu veritabanındaşunabenzerilişkilertanımlı


```python
osman = "Araştırma Geliştirme Müdürü" 
mehmet = "Proje Sorumlusu"
```

lerleyenzamandaişvereninizsizdenOsmanveMehmet’inunvanlarınıdeğiştirmenizitalep edebilir.YaniOsman’ıProjeSorumlusu,Mehmet’ideAraştırmaGeliştirmeMüdürüyapmanızı isteyebilirsizden. PatronunuzunbuisteğiniPython’daçokrahatbirbiçimdeyerinegetirebilirsiniz. Dikkatlice bakın: 


```python
osman, mehmet = mehmet, osman 
```


```python
osman
```




    'Proje Sorumlusu'



# EtkileşimliKabuğunHafızası

Etkileşimlikabukta_adlıişaret(altçizgiişareti),yapılansonişleminveyagirilensonöğenin değerinitutmaişlevigörür.Yani


```python
2345 + 54355
```




    56700




```python
_
```




    56700



# Print()

print()fonksiyonunungöreviekranaçıktıvermemizisağlamaktır.Hemenbununlailgilibir örnekverelim


```python
 print("Python programlama dili")

```

    Python programlama dili
    


```python
dil ="Python programlama dili" 
print(dil)
```

    Python programlama dili
    

Buarada,hemşimdiverdiğimiz,hemdedahaönceyazdığımızörneklerdebirşeydikkatinizi çekmişolmalı. Şimdiyekadarverdiğimizörneklerdekarakterdizilerinihepçifttırnakla gösterdik. Amaaslındatekseçeneğimizçifttırnakdeğildir. Pythonbizeüçfarklıtırnak seçeneğisunar: 

1.Tektırnak(‘‘) 2.Çifttırnak(””) 3.Üçtırnak(“””“””) Dolayısıylayukarıdakiörneğiüçfarklışekildeyazabiliriz: 


```python
print('Python programlama dili')

print("Python programlama dili")

print("""Python programlama dili""")

```


```python
print("Python programlama dilinin adı "piton" yılanından gelmez")
```


```python
Eğerbucümleyiçifttırnaklariçindegösterirsekprogramımızhataverecektir
```


```python
 print('Python programlama dilinin adı "piton" yılanından gelmez')

```


```python
AncakPython’dakarakterdizileritanımlanırkengenellikletektırnakveyaçifttırnakişaretleri kullanılır. Üçtırnakişaretlerininasılkullanımyeriisefarklıdır. Pekinedirbuüçtırnak işaretlerininasılkullanımyeri? Üçtırnakişaretlerinihertürlükarakterdizisiylebirliktekullanabiliyorolsakda,butırnak tipiçoğunluklasadecebirdenfazlasatırayayılmışkarakterdizilerinitanımlamadakullanılır.
```


```python
print(""" ... [H]=========HARMAN========[-][o][x] ... | | ... | Programa Hoşgeldiniz! | ... | Sürüm 0.8 | ... | Devam etmek için herhangi | ... | bir düğmeye basın. | ... | | ... |=================================| ... """)
```

print()fonksiyonu,tıpkıpow()fonksiyonugibi,birdenfazlaparametrealabilir: 


```python
print('Fırat', 'Özgül')

```

# print() Fonksiyonunun Parametreleri 

1. sep

sep ifadesi, İngilizcede separator (ayırıcı, ayraç) kelimesinin kısaltmasıdır. 
Dolayısıyla print() fonksiyonundaki bu sep parametresi, ekrana basılacak öğeler arasına hangi karakterinyerleştirileceğinigösterir. Buparametreninöntanımlıdeğeribiradetboşluk karakteridir(”“). Yanisizbuözelparametrenindeğerinibaşkabirşeyledeğiştirmezseniz, Pythonbuparametrenindeğerinibiradetboşlukkarakteriolarakalacakveekranabasılacak öğeleribirbirindenbirerboşluklaayıracaktır.Ancakeğerbizistersekbusepparametresinin değerinideğiştirebiliriz.BöylecePython,karakterdizilerinibirleştirirkenarayaboşlukdeğil, bizimistediğimizbaşkabirkarakteriyerleştirebilir. 
Gelin şimdibuparametrenindeğerini nasıldeğiştireceğimizigörelim.


```python
print("http://", "www.", "istihza.", "com", sep="")

```

Gördüğünüzgibi,karakterdizilerinibaşarıylabirleştirip,geçerlibirinternetadresieldeettik. Buradayaptığımızşeyaslındaçokbasit.Sadecesepparametresinin‘biradetboşlukkarakteri’ olanöntanımlıdeğerinisilip,yerine‘boşbirkarakterdizisi’değeriniyazdık.Buikikavramın birbirindenfarklıolduğunusöylediğimizihatırlıyorsunuz,değilmi? Gelinbirörnekdahayapalım


```python
print("T", "C", sep=".")

```

2. end

Birazöncededediğimizgibi,bukoduyazıpEntertuşunabastığımızandaprint()fonksiyonu ikifarklıişlemgerçekleştirir: 1.Önceliklekarakterdizisiniekranayazdırır. 2.Ardındanbiraltsatırageçipbize>>>işaretinigösterir. Bununnedemekolduğunuanlamakiçinendparametresinindeğerinideğiştirmemizyeterli olacaktır: 


```python
 print("Bugün günlerden Salı", end=".")

```


```python
 print("Bugün günlerden Salı", end=".\n")

```

3. ﬁle

print()fonksiyonunun,çıktılarınıekranadeğil,birdosyayayazdırmasını dasağlayabiliriz.Meselabizşimdiprint()fonksiyonunundeneme.txtadlıbirdosyayaçıktı vermesinisağlayalım. Bununiçinsırasıyla


```python
dosya = open("deneme.txt", "w") 
print("Ben Python, Monty Python!", file=dosya)
dosya.close()
```

Oluşturduğumuzbudeneme.txtadlıdosya,oandabulunduğunuzdiziniçindeoluşacaktır. Budizininhangisiolduğunuöğrenmekiçinşukomutlarıverebilirsiniz: 


```python
import os 
os.getcwd() 
```

Bukomutunçıktısındahangidizininadıgörünüyorsa, deneme.txt dosyasıdaodizinin içindedir.Meselabendekiçıktı/home/istihza/Desktop.Demekkioluşturduğumdeneme.txt adlıdosyamasaüstündeymiş. BenbukomutlarıUbuntuüzerindeverdim. EğerWindows üzerindeverseydimşunabenzerbirçıktıalacaktım:C:\Users\istihza\Desktop 

                           Pratik Bilgiler

adanelerdöndüğünüazçoktahminettiğinizizannediyorum.Sonörnektedegördüğünüz gibi,“Galatasaray”karakterdizisininbaşınaeklediğimizyıldızişareti;“Galatasaray”karakter 6.5. BirkaçPratikBilgi 65
Python3içinTürkçeKılavuz,Sürüm3 dizisininherbiröğesiniparçalarınaayırarak,bunlarıtektekprint()fonksiyonunayolluyor. Yanisankiprint()fonksiyonunuşöyleyazmışızgibioluyor


```python
print(*"Galatasaray")
```

# Kaçış Dizileri

Kaçışdizileri,Python’daözelanlamtaşıyanişaretveyakarakterleri,sahipolduklarıbuözel anlamdışındabiramaçlakullanmamızısağlayanbirtakımaraçlardır. Meselayukarıdada örnekleriniverdiğimizgibi,tırnakişaretleriPythonaçısındanözelanlamtaşıyanişaretlerdir. NormaldePythonbuişaretlerikarakterdizilerinitanımlamakiçinkullanır. Amaeğersiz meselabirmetiniçindebutırnakişaretlerinifarklıbiramaçlakullanacaksanızPython’ıbu durumdanhaberdaretmenizgerekiyor. İştekaçışdizileri,Python’ıböylebirdurumdan haberdaretmemizeyarayanaraçlardır

1. TersTaksim(\)

yukarıdaverdiğimizörneklerde,çifttırnaklagösterdiğimizkarakterdizilerininiçindedeçift tırnakişaretikullanabilmekiçinbirkaçfarklıyöntemdenyararlanabildiğimiziöğrenmiştik. Bunagöre,eğerbirkarakterdizisiiçindeçifttırnakişaretigeçiyorsa,okarakterdizisinitek tırnakla;eğertektırnakgeçiyorsadaokarakterdizisiniçifttırnaklatanımlayarakbusorunun üstesindengelebiliyorduk. Amadahaöncedesöylediğimizgibi,‘kaçışdizileri’adıverilen birtakımaraçlarıkullanarak,meselaiçindeçifttırnakgeçenkarakterdizileriniyineçifttırnakla tanımlayabiliriz. Dilerseniz, kaçışdizisikavramınıaçıklamayageçmedenöncebununlailgilibirkaçörnek verelim.Busayedeneilekarşıkarşıyaolduğumuz,zihnimizdebirazdahabelirginleşebilir: 


```python
print('Yarın Adana\'ya gidiyorum.')

```


```python
print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.")

```


```python
 Bukaçışdizisini, uzunkarakterdizilerinibölmekiçinde kullanabiliriz.
```


```python
print("Python 1990 yılında Guido Van Rossum \ 
... tarafından geliştirilmeye başlanmış, oldukça \ 
...güçlü ve yetenekli bir programlama dilidir.")
```

2. SatırBaşı(\n) 

başkakarakterlerlebirleşerek,farklıişlevleresahipyenikaçışdizilerideoluşturabilir.Aslında buolguyayabancıdeğiliz. Öncekisayfalardabudurumabirörnekvermiştik. Hatırlarsanız print()fonksiyonunuanlatırkenendparametresininöntanımlıdeğerinin\n,yanisatırbaşı karakteriolduğunusöylemiştik


```python
 print("birinci satır\nikinci satır\nüçüncü satır")

```


```python
başlık = "Türkiye'de Özgür Yazılımın Geçmişi"
print(başlık, "\n", "-"*len(başlık), sep=""
```


```python
open("C:\\nisan\\masraflar") 
```

3. Sekme(\t)


```python
print("abc\tdef")

```

Burada \t adlıkaçışdizisi,“abc”ifadesindensonrasankiTab(sekme)tuşunabasılmışgibibir etkioluşturarak“def”ifadesinisağadoğruitiyor.Birdeşuörneğebakalım: 

print("bir", "iki", "üç", sep="\t")



```python
print("C:\\nisan\\masraflar\\toplam_masraf.txt") 
```

4. ZilSesi(\a) 


```python
print("\a")

```

5. AynıSatırBaşı(\r)


```python
 print("Merhaba\rZalim Dünya!")

```

ancakeğerkarakterdizisininherhangibiryerine\radlıkaçışdizisiniyerleştirirsek,bukaçış dizisininbulunduğukonumdanitibarenaynısatırınbaşınadönülecekve\rkaçışdizisinden sonragelenbütünkarakterlersatırbaşındakikarakterlerinüzerineyazacaktır.Şuörnekdaha açıklayıcıolabilir: 


```python
print("Merhaba\rDünya")

```

# Yorum İşareti

 Sizinyazdığınızkodlarınasılbaşkalarıokurken zorlanıyorsa,kendiyazdığınızkodlarıokurkensizbilezorlanabilirsiniz.Özellikleuzunsüredir ilgilenmediğinizeskiprogramlarınızıgözdengeçirirkenböylebirsorunlakarşılaşabilirsiniz. Programıniçindekibirkodparçası, programınilkyazılışınınüzerinden5-6aygeçtikten sonrasizeartıkhiçbirşeyifadeetmiyorolabilir. Kodlarabakıp,‘Acababuradaneyapmaya çalışmışım?’ diyedüşündüğünüzzamanlardaolacaktır. İştebutürsıkıntılarıortadan kaldırmakveyaenazaindirmekiçinkodlarımızınarasınaaçıklayıcınotlarekleyeceğiz

Python’da yorumlar # işareti ile gösterilir


```python
#merhaba dünya
#degişken..... şudur.
```

# input() Fonksiyonu 

Buprogramıyazıpkaydettiktensonrabuprogramınsimgesiüzerineçifttıkladığımızdasiyah birkomutekranınınçokhızlıbirşekildeaçılıpkapandığınıgörürüz. Aslındaprogramımız çalışıyor,amaprogramımızyapmasıgerekenişiyaptıktanhemensonrakapandığıiçinbiz programpenceresinigörmüyoruz. Programımızınçalıştıktansonrahemenkapanmamasınısağlamakiçinsonsatırabirinput() fonksiyonuyerleştirmemizgerektiğinibiliyoruz: 


```python
#!/usr/bin/env python3
kartvizit = """ İstihza Anonim Şirketi Fırat Özgül Tel: 0212 123 23 23 Faks: 0212 123 23 24 e.posta: kistihza@yahoo.com """
print(kartvizit)
input() Bu say
```

Bu sayede programımız kullanıcıdan bir giriş bekleyecek ve o girişi alana kadar da kapanmayacaktır.ProgramıkapatmakiçinEnterdüğmesinebasabiliriz

Görüyorsunuz ya, tıpkı daha önce gördüğümüz fonksiyonlarda olduğu gibi, input() fonksiyonundadaparanteziçinebirparametreyazıyoruz.Bufonksiyonaverilenparametre, kullanıcıdanverialınırkenkullanıcıyasorulacaksoruyugösteriyor


```python
yaş = input("Yaşınız: ")
print("Demek", yaş, "yaşındasın.") 
print("Genç mi yoksa yaşlı mı olduğuna karar veremedim.") 
```


```python
Kullanıcıdan dairenin çapını girmesini istiyoruz. çap = input("Dairenin çapı: ")
#Kullanıcının verdiği çap bilgisini kullanarak #yarıçapı hesaplayalım. Buradaki int() fonksiyonunu #ilk kez görüyoruz. Biraz sonra bunu açıklayacağız yarıçap = int(çap) / 2
#pi sayımız sabit pi = 3.14159
#Yukarıdaki bilgileri kullanarak artık #dairenin alanını hesaplayabiliriz alan = pi * (yarıçap * yarıçap)
#Son olarak, hesapladığımız alanı yazdırıyoruz print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")
```

Ancak burada, daha önce öğrenmediğimiz bir fonksiyon dikkatinizi çekmiş olmalı. Bu fonksiyonunadıint(). Buyenifonksiyondışında,yukarıdakibütünkodlarıanlayabilecek kadarPythonbilgisinesahibiz. int()fonksiyonununneişeyaradığınıanlamakiçinistersenizilgilisatırıyarıçap = çap / 2 şeklindeyazarakçalıştırmayıdeneyinbuprogramı. Dediğimgibi,eğerosatırdakiint()fonksiyonunukaldırarakprogramıçalıştırdıysanızşuna benzerbirhatamesajıalmışolmalısınız

# Tip Dönüşümleri

iyelimkikullanıcıdanaldığısayınınkaresinihesaplayanbirprogramyazmakistiyoruz. Öncelikleşöylebirşeydeneyelim


```python
sayı = input("Lütfen bir sayı girin: ")
#Girilen sayının karesini bulmak için sayı değişkeninin 
2. #kuvvetini alıyoruz. Aynı şeyi pow() fonksiyonu ile de #yapabileceğimizi biliyorsunuz. Örn.: pow(sayı, 2) 
print("Girdiğiniz sayının karesi: ", sayı ** 2) 
```

Bukodlarıçalıştırdığımızzaman,programımızkullanıcıdanbirsayıgirmesiniisteyecek,ancak kullanıcıbirsayıgiripEntertuşunabastığındaşöylebirhatamesajıylakarşılaşacaktır


```python
#Kullanıcıdan herhangi bir veri girmesini istiyoruz sayı = input("Herhangi bir veri girin: ")
#Kullanıcının girdiği verinin tipini bir #değişkene atıyoruz tip = type(sayı)
#Son olarak kullanıcının girdiği verinin tipini #ekrana basıyoruz. print("Girdiğiniz verinin tipi: ", tip)

```

Pekiyukarıdakigibidurumlarlakarşılaşmamakiçinneyapacağız? İştebunoktadadevreyetipdönüştürücüadınıverdiğimizbirtakımfonksiyonlargirecek

1. int() 

Dediğimiz gibi, input() fonksiyonundan gelen veri her zaman bir karakter dizisidir. Dolayısıyla bu fonksiyondan gelen veriyle herhangi bir aritmetik işlem yapabilmek için önceliklebuveriyibirsayıyadönüştürmemizgerekir. Budönüştürmeişlemiiçin int() adlıözelbirdönüştürücüfonksiyondanyararlanacağız


```python
karakter_dizisi = "23"  
sayı = int(karakter_dizisi)
print(sayı)

```

Buradaöncelikle“23”adlıbirkarakterdizisitanımladık. Ardındandaint()fonksiyonunu kullanarak bu karakter dizisini bir tamsayıya (integer) dönüştürdük. İsminden de anlayacağınızgibiint()fonksiyonuİngilizceinteger(tamsayı)kelimesininkısaltmasıdırve bufonksiyonungörevibirveriyitamsayıyadönüştürmektir. Ancak burada dikkat etmemiz gereken bir şey var. Herhangi bir verinin sayıya dönüştürülebilmesiiçinoverininsayıdeğerlibirveriolmasıgerekir.Örneğin“23”,sayıdeğerli birkarakterdizisidir.Amamesela“elma”sayıdeğerlibirkarakterdizisideğildir.Buyüzden “elma”karakterdizisisayıyadönüştürülemez: 

2. str() 

 Yanikarakterdizisiolmayanverileri karakterdizisinedönüştürmemizdemümkündür. Buişlemiçin str() adlıbaşkabirtip dönüştürücüdenyararlanıyoruz: 


```python
sayı = 23 
kardiz = str(sayı) 
print(kardiz)
print(type(kardiz))
```

Gördüğünüzgibi,birtamsayıolan23‘üstr()adlıbirfonksiyondanyararlanarakkarakter dizisiolan“23”ifadesinedönüştürdük.Sonsatırdada,eldeettiğimizşeyinbirkarakterdizisi olduğundaneminolmakiçintype()fonksiyonunukullanarakverinintipinidenetledik. 

bildiğinizgibi,len()fonksiyonu,şuanakadaröğrendiğimizveritipleriiçindesadecekarakter dizileri üzerinde işlem yapabiliyor


```python
len(str(12343423432))
```

3. ﬂoat() 

İşteeğerbirtamsayıyıveyasayı değerlibirkarakterdizisinikayannoktalısayıyadönüştürmekistersek float() adlıbaşka birdönüştürücüdenyararlanacağız: 


```python
>>> a = 23 >>> type(a)
<class 'int'>
>>> float(a
```

4. complex() 

Sayılardan söz ederken, eğer matematikle çok fazla içli dışlı değilseniz pek karşılaşmayacağınız, ‘karmaşık sayı’ adlı bir sayı türünden de bahsetmiştik. Karmaşık sayılarPython’da‘complex’ifadesiylegösteriliyor.Meselaşununbirkarmaşıksayıolduğunu biliyoruz: 


```python
complex(15)

```

# eval()ve exec()Fonksiyonları 

İngilizcedeevaluatediyebirkelimebulunur.Bukelime,‘değerlendirmeyetabitutmak,işleme sokmak,işlemek’gibianlamlartaşır.İşteeval()fonksiyonundakievalkelimesibuevaluate kelimesininkısaltmasıdır. Yanibufonksiyonungörevi,kendisineverilenkarakterdizilerini değerlendirmeyetabitutmakyadaişlemektir.Pekibutamolarakneanlamageliyor? Aslındayukarıdakiörnekprogramıçalıştırdığımızdabusorununyanıtınıkendikendimize verebiliyoruz. Buprogramıçalıştırarak,“İşleminiz: “ ifadesindensonra,örneğin, 45 * 76 yazıpEnter tuşunabasarsakprogramımızbize3420 çıktısıverecektir. Yaniprogramımız hesapmakinesiişleviniyerinegetirip45 sayısıile76 sayısınıçarpacaktır. Dolayısıyla, yukarıdakiprogramıkullanarakhertürlüaritmetikişlemiyapabilirsiniz. Hattabuprogram, sonderecekarmaşıkaritmetikişlemlerinyapılmasınadahimüsaadeeder. Pekiprogramımızbuişlevinasılyerinegetiriyor? İstersenizkodlarınüzerindentektek geçelim. Öncelikleprogramımızınenbaşınakullanımkılavuzunabenzerbirmetinyerleştirdikvebu metniprint()fonksiyonuyardımıylaekranabastık.
11.3. eval()veexec()Fonksiyonları 123
Python3içinTürkçeKılavuz,Sürüm3 Daha sonra kullanıcıdan alacağımız komutları veri adlı bir değişkene atadık. Tabii ki kullanıcıylailetişimiherzamanolduğugibiinput()fonksiyonuyardımıylasağlıyoruz. Ardından, kullanıcıdan gelen veriyi eval() fonksiyonu yardımıyla değerlendirmeye tabi tutuyoruz. Yanikullanıcınıngirdiğikomutlarıişlemesokuyoruz. Örneğin,kullanıcı46 / 2 gibibirverigirdiyse,bizeval()fonksiyonuyardımıylabu46 / 2komutunuişletiyoruz.Bu işleminsonucunudahesapadlıbaşkabirdeğişkeniçindedepoluyoruz. Eğerburadaeval()fonksiyonunukullanmazsak,programımız,kullanıcınıngirdiği45 * 76 komutunuhiçbirişlemesokmadandümdüzekranabasacaktır.Yani: 


```python
print(""" Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama - çıkarma * çarpma / bölme
Yapmak istediğiniz işlemi yazıp ENTER tuşuna basın. (Örneğin 23 ve 46 sayılarını çarpmak için 23 * 46 yazdıktan sonra ENTER tuşuna basın.) """)
veri = input("İşleminiz: ")
print(veri) 
```


```python
n eval() fonksiyonubirkarakterdizisiiçindekideğişkentanımlamaişleminiyerine getiremez.Yanieval()ileşöylebirşeyyapamazsınız
```


```python
eval("a = 45") 
```

Amaexec()ileböylebirişlemyapabilirsiniz: 


```python
 exec("a = 45") 
```

eval() ve exec() fonksiyonları özellikle kullanıcıdan alınan verilerle doğrudan işlem yapmakgerekendurumlardaişinizeyarar. Örneğinbirhesapmakinesiyaparken eval() fonksiyonundanyararlanabilirsiniz. AynışekildemeselainsanlaraPythonprogramlamadiliniöğretenbirprogramyazıyorsanız exec()fonksiyonunuşöylekullanabilirsiniz:


# format()Metodu

biraz önce karakter dizisi birleştirme yöntemini kullanarak gerçekleştirdiğimiz işlemi, çok daha basit bir yolla gerçekleştirme imkanı sunuyor bize buformat()denenaraç... 


```python
print("{} ve {} iyi bir ikilidir".format("Python", "Django"))
'Python ve Django iyi bir ikilidir'
>>> print("{} {}'yi seviyor!".format("Ali", "Ayşe"))
'Ali Ayşe'yi seviyor!'
>>> print("{} {} yaşında bir {}dur".format("Ahmet", "18", "futbolcu"))
'Ahmet 18 yaşında bir futbolcudu
```

# KoşulDeyimleri

Python programlama dilinde koşullu durumları belirtmek için üç adet deyimden yararlanıyoruz: • if • elif • else İstersenizönceifdeyimiilebaşlayalım... 


```python
if n > 10:
```

Buradasayının10’danbüyükolupolmadığınabakıyoruz. Burada gördüğümüz > işaretinin ne demek olduğunu açıklamaya gerek yok sanırım. Hepimizinbildiği‘büyüktür’işaretiPython’dadaaynenbildiğimizşekildekullanılıyor.Mesela ‘küçüktür’demekisteseydik,<işaretinikullanacaktık.İstersenizhemenşuradaarayagiripbu işaretleriyenidenhatırlayalım: İşleç Anlamı > büyüktür < küçüktür >= büyükeşittir <= küçükeşittir == eşittir != eşitdeğildir Gördüğünüzgibihiçbiribizeyabancıgelecekgibideğil. Yalnızcaensondaki‘eşittir’(==)ve ‘eşitdeğildir’(!=)işaretleribirazdeğişikgelmişolabilir.Burada‘eşittir’işaretinin=olmadığına dikkatedin.Python’da=işaretinideğeratamaişlemleriiçinkullanıyoruz.==işaretiniiseiki adetdeğerinbirbirineeşitolupolmadığınıdenetlemekiçin...Mesela


```python
a=26
```

Buradadeğeri26 olanaadlıbirdeğişkenbelirledik. Yaniadeğişkeninedeğerolarak26 sayısınıatadık.Ayrıcaburada,değeratamaişlemininardındanEntertuşunabastıktansonra Pythonhiçbirşeyyapmadanbiraltsatırageçti.Birdeşunabakalım


```python
 a == 26

```

komutunuverdiktensonraPythonbizeTruediyebirçıktıverdi. Buçıktınınanlamınıbiraz sonraöğreneceğiz.Amaşimdiistersenizkonuyudahafazladağıtmayalım.Bizşimdiliksadece =ve==işaretlerininbirbirindentamamenfarklıanlamlarageldiğinibilelimyeter


```python
if n > 10: 
print("sayı 10'dan büyüktür!") 
```


```python
sayı = int(input("Bir sayı giriniz: "))
if sayı > 10: print("Girdiğiniz sayı 10'dan büyüktür!")
if sayı < 10: print("Girdiğiniz sayı 10'dan küçüktür!")
if sayı == 10: print("Girdiğiniz sayı 10'dur!") 
```

2. elif 


```python
yaş = int(input("Yaşınız: "))
if yaş == 18: print("18 iyidir!")
elif yaş < 0: print("Yok canım, daha neler!...")
elif yaş < 18: print("Genç bir kardeşimizsin!")
elif yaş > 18: print("Eh, artık yaş yavaş yavaş kemale eriyor!") 
```


```python
Yukarıdakiörneğişöyleyazmayıdadeneyebilirsiniz: 
```


```python
yaş = int(input("Yaşınız: "))
if yaş == 18: print("18 iyidir!")
if yaş < 0: print("Yok canım, daha neler!...")
if yaş < 18: print("Genç bir kardeşimizsin!")
if yaş > 18: print("Eh, artık yaş yavaş yavaş kemale eriyor!")
```

Buikiprogramındaaynıişlevigördüğünüdüşünebilirsiniz.Ancakilkbakıştapekbelliolmasa da,aslındayukarıdakiikiprogrambirbirindenfarklıdavranacaktır.Örneğinikinciprogramda eğerkullanıcıeksideğerlibirsayıgirersehemif yaş < 0bloğu,hemdeif yaş < 18bloğu çalışacaktır.İstersenizyukarıdakiprogramıçalıştırıp,cevapolarakeksideğerlibirsayıverin. Nedemekistediğimizgayetnetanlaşılacaktır. Budurumifileelifarasındakiçokönemlibirfarktankaynaklanır.Bunagöreifbizeolası bütünsonuçlarılisteler,elifisesadecedoğruolanilksonucuverir.Busoyuttanımlamayı birazdahasomutlaştıralım: 


```python
a = int(input("Bir sayı giriniz: "))
if a < 100: print("verdiğiniz sayı 100'den küçüktür.")
if a < 50: print("verdiğiniz sayı 50'den küçüktür.")
if a == 100: print("verdiğiniz sayı 100'dür.")
if a > 100: 
print("verdiğiniz sayı 100'den büyüktür.")
if a > 150: print("verdiğiniz sayı 150'den büyüktür.") 
```

Gördüğünüzgibi,elifdeyimlerinikullandığımızzaman,ekranayalnızcadoğruolanilksonuç veriliyor.

3. else 

if falanca: bu işlemi yap
if filanca: şu işlemi yap 

ifileelifarasındakifarkıbiliyoruz.Eğerifdeyimleriniartardasıralayacakolursak,Python doğruolanbütünsonuçlarılisteleyecektir. Amaeğer if deyimindensonra elif deyimini kullanırsak,Pythondoğruolanilksonuculistelemekleyetinecektir

eğer böyle bir durum varsa: bunu yap
eğer şöyle bir durum varsa: şunu yap
eğer filancaysa: şöyle git
eğer falancaysa: böyle ge


```python
soru = input("Bir meyve adı söyleyin bana:")
if soru == "elma": print("evet, elma bir meyvedir...")
elif soru == "karpuz": print("evet, karpuz bir meyvedir...")
elif soru == "armut": 
    print("evet, armut bir meyvedir...")
else: print(soru, "gerçekten bir meyve midir?") 
```


```python
if soru == "armut": print("evet, armut bir meyvedir...")
else: print(soru, "gerçekten bir meyve midir?"
```

# İşleçler

Türkçedeişleçyerineoperatör,işlenenyerinedeoperantdendiğinetanıkolabilirsiniz
1.Aritmetikİşleçler 2.Karşılaştırmaİşleçleri 3.Boolİşleçleri 4.DeğerAtamaİşleçleri 5.Aitlikİşleçleri 6.Kimlikİşleçleri


```python
Dedikki, sağındavesolundabulunandeğerlerarasındabirilişkikuranişaretlereişleç (operator)adıverilir.
```

+ toplama - çıkarma * çarpma / bölme ** kuvvet 

Öncekiderslerdegördüğümüzveyukarıdadatekrarettiğimizdörtadettemelaritmetikişlece şuikiaritmetikişlecideekleyelim: % modülüs // tabanbölme 

Burada02sayısıbölmeişlemininkalanıdır.İştemodülüsdenenişleçdebölmeişleminden kalanbudeğerigösterir.Yani


```python
 30 % 4

```


```python
round(2.55)
```

Gördüğünüzgibi,round()fonksiyonunaparametreolarakbirsayıveriyoruz.Bufonksiyonda bizeosayınınyuvarlanmışhalinidöndürüyor


```python
round(2.55, 1)
```

Buradaikinciparametreolarak1 sayısınıverdiğimiziçin,noktadansonrakibirbasamak görüntüleniyor.Birdeşunabakalım


```python
 round(2.68, 1)
```

Şimdiyekadaröğrendiğimizveyukarıdakitablodaandığımızbirbaşkaaritmetikişleçde kuvvetişleci(**)idi. Meselabuişlecikullanarakbirsayınınkaresinihesaplayabileceğimizi biliyorsunuz


```python
 25 ** 2

```

2. Karşılaştırmaİşleçleri 

== eşittir != eşitdeğildir > büyüktür < küçüktür >= büyükeşittir <= küçükeşitti


```python
parola = "xyz05"
soru = input("parolanız: ")
if soru == parola: print("doğru parola!")
elif soru != parola: print("yanlış parola!")
```

3. Boolİşleçleri 

Bilgisayarbilimiikiadetdeğerüzerinekuruludur: 1 ve0. YanisırasıylaTrue veFalse. BilgisayarbilimindeherhangibirşeyindeğeriyaTrue,yadaFalse‘tur.İştebuTrueveFalse olarakifadeedilendeğerlerebooldeğerleriadıverilir(GeorgeBooleadlıİngilizmatematikçi veﬁlozofunadından).Türkçeolaraksöylemekgerekirse,TruedeğerininkarşılığıDoğru,False değerininkarşılığıiseYanlış‘tır


```python
 a == 1
```

Bool işleçleri sadece yukarıda verdiğimiz örneklerdeki gibi, salt bir doğruluk-yanlışlık sorgulamayayarayanaraçlardeğildir. Bilgisayarbilimindeherşeyinbirbooldeğerivardır. Bununlailgiligenelkuralımızşu:0değeriveboşveritipleriFalse‘tur.Bunlardışındakalan herşeyiseTrue‘dur. Budurumubool()adlıözelbirfonksiyondanyararlanarakteyitedebiliriz


```python
 bool(3)

```

Pekiandişlecininçalışmamantığınedir?Dediğimgibi,andTürkçede‘ve’anlamınageliyor. Buişlecidahaiyianlayabilmekiçinşucümlelerarasındakifarkıdüşünün: 1.ToplantıyaAliveVelikatılacak. 2.ToplantıyaAliveyaVelikatılacak. İlkcümlede‘ve’bağlacıkullanıldığıiçin,bucümleningereğininyerinegetirilebilmesi,hem Ali’ninhemdeVeli’nintoplantıyakatılmasınabağlıdır. SadeceAliveyasadeceVeli’nin toplantıyakatılmasıdurumundabucümleningereğiyerinegetirilememişolacaktır. İkincicümledeisetoplantıyaAliveVeli’denherhangibirisininkatılmasıyeterlidir.Toplantıya sadeceAli’ninkatılması, sadeceVeli’ninkatılmasıveyaherikisininbirdenkatılması, bu cümleningereğininyerinegetirilebilmesiaçısındanyeterlidir. İştePython’dakiandişlecideaynıbuşekildeişler.Şuörneklerebirbakalım


```python
 a = 23  
    b = 10 
    a == 23

b == 10

a == 23 and b == 10

```

Gelelimorişlecine... Tıpkıandgibibirboolişleciolanor‘unTürkçedekarşılığı‘veya’dır. Yukarıda‘ToplantıyaAli veyaVelikatılacak.’ cümlesinitartışırkenaslındabuorkelimesininanlamınıaçıklamıştık. HatırlarsanızandişlecininTrueçıktısıverebilmesiiçinbuişleçlebağlananbütünönermelerin True değerine sahip olması gerekiyordu. or işlecinin True çıktısı verebilmesi için ise orişleciylebağlananönermelerdenherhangibirininTrueçıktısıvermesiyeterliolacaktır. Söylediğimizbuşeyleribirkaçörneküzerindesomutlaştıralım


```python
 a = 23 >>>
    b = 10 >>>
    a == 23
True
>>> b == 10
True
>>> a == 11
False
>>> a == 11 or b == 10
True
```

Son bool işlecimiz not. Bu kelimenin İngilizce’deki anlamı ‘değil’dir. Bu işleci şöyle kullanıyoruz


```python
>>> a = 23 >>> not a
False
>>> a = "" >>> not a
True 
```

4. DeğerAtamaİşleçleri


```python
a=23
```

Burada=işleciadeğişkenine23değeriniatamaişlevigörüyor.

                    +=işleci


```python
 a += 5
print(a)

```

                    -=işleci


```python
a = 23 
a -= 5 
print(a)

```

                        /=işleci


```python
a = 30 
a /= 3
print(a)
```

                       *=işleci


```python
 a = 20 >>> 
    a *= 2 
    >>> print(a)

```

                      %=işleci 


```python
>>> a = 40 >>> a %= 3 >>> print(a
```

                    **=işleci


```python
>>> a = 12 >>> a **= 2 >>> print(a)
```

                    //=işleci 
  Değeratamaişleçlerininsonuncusuolan//= işleciningöreviisetabanbölmeişleminin sonucunuaynıdeğişkeneatamaktır


```python
 a = 5 >>> a //= 2 >>> print(a
```

5. Aitlikİşleçleri 

itlik işleçleri, bir karakter dizisi ya da sayının, herhangi bir veri tipi içinde bulunup bulunmadığınısorgulamamızısağlayanişleçlerdir. Python’dabirtaneaitlikişlecibulunur.Buişleçdeinişlecidir.Buişlecişöylekullanıyoruz


```python
 a = "abcd" 
"a" in a

"f" in a

```

6. Kimlikİşleçleri

Python’daherşeyin(yadabaşkabirdeyişlehernesnenin)birkimliknumarası(identity) vardır. Kabacasöylemekgerekirse,bukimliknumarasıdenenşeyesasındaonesnenin bellektekiadresinigösterir

Pekibirnesneninkimliknumarasınanasılulaşırız? Python’dabuişiyapmamızısağlayacakid()adlıbirfonksiyonbulunur(İngilizcedekiidentity (kimlik) kelimesinin kısaltması). Şimdi bir örnek üzerinde bu id() fonksiyonunu nasıl kullanacağımızabakalım


```python
a = 100
id(a)

```

YukarrıdakidurumugörebileceğimizbaşkabiryöntemdePython’dakiisadlıkimlikişlecini kullanmaktır


```python
 a is 1000
```

olupolmadığınısorgularken,==işleciadeğişkeninintuttuğuverinin1000olupolmadığını denetliyor.Yaniisişlecininyaptığışeykabacaşuoluyor




# while Döngüsü


```python
a = 1
while a == 1: 
```

Buradaaadlıbirdeğişkenoluşturduk.Budeğişkenindeğeri1.Birsonrakisatırdaisewhile a == 1: gibibirifadeyazdık.Enbaştadasöylediğimizgibiwhilekelimesi,‘...iken,olduğu sürece’gibianlamlartaşıyor.Pythonprogramlamadilindekianlamıdabunaoldukçayakındır. Buradawhile a == 1ifadesiprogramımızaşöylebiranlamkatıyor: adeğişkeninindeğeri1olduğusürece... Gördüğünüzgibicümlemizhenüzeksik. Yanibellikibununbirdedevamıolacak. Ayrıca whileifadesininsonundaki:işaretindenanladığımızgibi,bundansonrageleceksatırgirintili yazılacak.Devamedelim


```python
a = 1
while a == 1: print("bilgisayar çıldırdı!")
```

BuradaPython’aşuemrivermişolduk: adeğişkeninindeğeri1olduğusürece,ekrana‘bilgisayarçıldırdı!’yazısınıdök
BuprogramıçalıştırdığımızdaPythonverdiğimizemresadakatleuyacakveadeğişkeninin değeri 1 olduğu müddetçe de bilgisayarımızın ekranına ‘bilgisayar çıldırdı!’ yazısını dökecektir.Programımızıniçindeadeğişkeninindeğeri1olduğuvebudeğişkenindeğerini değiştirecekherhangibirşeybulunmadığıiçinPythonhiçsıkılmadanekrana‘bilgisayar çıldırdı!’ yazısınıbasmayadevamedecektir. Eğersizdurdurmazsanızbudurumsonsuza kadardevamedebilir. BuçılgınlığabirsonvermekiçinklavyenizdeCtrl+C veyaCtrl+Z tuşlarınabasarakprogramıdurmayazorlayabilirsiniz. Buradaprogramımızısonsuzbirdöngüyesokmuşolduk(inﬁniteloop). Esasındasonsuz döngülergenelliklebirprogramhatasınaişareteder. Yaniçoğudurumdaprogramcının arzuettiğişeybudeğildir.Oyüzdendoğruyaklaşım,döngüyesoktuğumuzprogramlarımızı durduracakbirölçütbelirlemektir. Yaniöylebirkodyazmalıyızki,adeğişkeninin1 olan değeribirnoktadansonraartık1olmasınveböyleceonoktayaulaşıldığındaprogramımız dursun.KullanıcınınCtrl+Ctuşlarınabasarakprogramıdurdurmakzorundakalmasıpekhoş olmuyor.Gelinistersenizbusoyutifadeleribirazsomutlaştıralım. 


```python
a = 1
while a < 10: 
```

whileileverdiğimizilkörnektewhile a == 1gibibirifadekullanmıştık.Buifade; a‘nındeğeri1olduğumüddetçe... gibibiranlamageliyordu. while a < 10ifadesiise; a‘nındeğeri10‘danküçükolduğumüddetçe... anlamınagelir.İşteburadaprogramımızınsonsuzdöngüyegirmesiniengelleyecekbirölçüt koymuşolduk.Bunagöre,adeğişkenininşimdikideğeri1‘dir.Biz,a‘nındeğeri10‘danküçük olduğumüddetçebirişlemyapacağız.Devamedelim: 


```python
a = 1
while a < 10: print("bilgisayar yine çıldırdı!") 
```


```python
a = 1
while a < 10: a += 1 print("bilgisayar yine çıldırdı!")
```


```python
a = 1
while a < 10: a += 1 print(a) 
```


```python
while True: 
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
if soru == "q": print("çıkılıyor...") 
    break 
```


```python
giriş = """ (1) topla (2) çıkar (3) çarp (4) böl (5) karesini hesapla (6) karekök hesapla """
print(giriş)
while True: soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
if soru == "q": print("çıkılıyor...") break
elif soru == "1": sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: ")) sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: ")) print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
elif soru == "2": sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: ")) sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: ")) 
   print(sayı3, "-", sayı4, "=", sayı3 - sayı4)
elif soru == "3": sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: ")) sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: ")) print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
elif soru == "4": sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: ")) sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: ")) print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
elif soru == "5": sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: ")) print(sayı9, "sayısının karesi =", sayı9 ** 2)
elif soru == "6": sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: ")) print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)
else: 
    print("Yanlış giriş.") 
    print("Aşağıdaki seçeneklerden birini giriniz:", giriş)  
```

whileTrueifadesişöylebiranlamagelir: Trueolduğumüddetçe... PekineTrueolduğumüddetçe? BuradaneyinTrueolmasıgerektiğinibelirtmediğimiziçin, aslındabukodparçasışuanlamageliyor: Aksibelirtilmediğisüreceçalışmayadevamet! Eğeryukarıdakiaçıklamayıbirazbulanıkbulduysanızşuörneğiinceleyebilirsiniz


```python
while True: 
print("Bilgisayar çıldırdı!") 
```


```python
if soru == "q": 
    print("çıkılıyor...") break 
```

# 2 For Döngüsü

for da tıpkı while gibi bir döngüdür. Yani tıpkı while döngüsünde olduğu gibi, programlarımızınbirdenfazlasayıdaçalışmasınısağlar.Ancakfordöngüsüwhiledöngüsüne göre biraz daha yeteneklidir. while döngüsü ile yapamayacağınız veya yaparken çok zorlanacağınızşeylerifordöngüsüyardımıylaçokkolaybirşekildehalledebilirsiniz. Yalnız,söylediğimizbucümleden, fordöngüsününwhiledöngüsünebiralternatifolduğu sonucunuçıkarmayın. Evet,whileileyapabildiğinizbirişlemiforiledeyapabilirsinizçoğu zaman,amabudöngülerin,bellivakalariçintekseçenekolduğudurumlardavardır.Zirabu ikidöngününçalışmamantığıbirbirindenfarklıdır. Şimdigelelimfordöngüsününnasılkullanılacağına... Dikkatlicebakın:


```python
tr_harfler = "şçöğüİı"
for harf in tr_harfler: 
print(harf)
```


```python
for değişken_adı in değişken: yapılacak_işlem 
```

değişken içindeki herbir öğeyi değişken_adı olarak adlandır: ve bu öğelerle bir işlem yap. 


```python
izinli_karakterler = "0123456789+-/*= "
for s in veri:
    if s not in izinli_karakterler: 
    print("Neyin peşindesin?!") quit()
hesap = eval(veri) 
```

# İlgiliAraçlar

1. rangeFonksiyonu

rangekelimesiİngilizcede‘aralık’anlamınagelir. BizPython’darange()fonksiyonunubelli biraralıktabulunansayılarıgöstermekiçinkullanıyoruz


```python
 for i in range(0, 10): 
        print(i)
```

range(ilk_sayı, son_sayı) 

Eğer range() fonksiyonununilkparametresi0 olacaksa,buparametreyibelirtmesekde olur.Yanimesela0‘dan10‘akadarolansayılarılisteleyeceksekrange()fonksiyonunuşöyle yazmamızyeterliolacaktır: 


```python
 for i in range(10):
        print(i) 
```

Kısacası,eğerrange()fonksiyonununkaçarkaçarsayacağınıdabelirtmekistiyorsak,parantez içinde,gereklibütünparametreleribelirtmeliyiz. Gördüğünüzgibi,range()fonksiyonunukullanarakbelirlibiraralıktakisayılarıalabiliyoruz. Pekibusayılarıterstenalabilirmiyiz?Elbette


```python
for i in range(10, 0, -1):
print(i)
```

2. passDeyimi


```python
 BizbudeyimiPyhon’da‘görmezdengel,hiçbirşeyyapma’ anlamındakullanacağız. 
```


```python
while True: sayı = int(input("Bir sayı girin: "))
if sayı == 0: break
elif sayı < 0: pass
else: 
print(sayı)
```

Buradaeğerkullanıcı0sayısınıgirerseprogramımızsonaerer(breakdeyiminibirazsonra inceleyeceğiz). Eğerkullanıcı0‘danküçükbirsayıgirerse, yanikullanıcınıngirdiğisayı eksideğerliise,passdeyiminininetkisiyleprogramımızhiçbirşeyyapmadanyolunadevam eder.Bukoşullarındışındakidurumlardaiseprogramımızkullanıcınıngirdiğisayılarıekrana yazdıracaktır

Yukarıdaanlatılandurumlarındışında, pass deyiminikodlarınızhenüztaslakaşamasında olduğuzamandakullanabilirsiniz. Örneğin,diyelimkibirkodyazıyorsunuz. Programın gidişatınagöre,birnoktadayapmanızgerekenbirişlemvar,amahenüzneyapacağınıza kararvermediniz.Böylebirdurumdapassdeyimindenyararlanabilirsiniz.Meselabirtakım ifdeyimleriyazmayıdüşünüyorolun


```python
if .....: böyle yap
elif .....: şöyle yap
else: pass
```

3. breakDeyimi

Budeyimyardımıyla,devamedenbirsürecikesintiye uğratabiliriz.Budeyiminkullanıldığıbasitbirörnekverelim


```python
 while True: 
        parola = input("Lütfen bir parola belirleyiniz:") 
         
        if len(parola) < 5:
         
            print("Parola 5 karakterden az olmamalı!")
            
            else: 
            
                print("Parolanız belirlendi!") 
                break 
```

Burada,eğerkullanıcınıngirdiğiparolanınuzunluğu5karakterdenazsa,Parola5karakterden azolmamalı!uyarısıgösterilecektir.Eğerkullanıcı5karakterdenuzunbirparolabelirlemişse, kendisine‘Parolanızbelirlendi!’ mesajınıgösterip, break deyimiyardımıylaprogramdan çıkıyoruz. Gördüğünüz gibi, break ifadesinin temel görevi bir döngüyü sona erdirmek. Buradan anlayacağımızgibi,breakifadesininherzamanbirdöngüiçindeyeralmasıgerekiyor. Aksi haldePythonbizeşöylebirhataverecektir

4. continueDeyimi


```python
while True: s = input("Bir sayı girin: ") if s == "iptal": break
if len(s) <= 3: continue
print("En fazla üç haneli bir sayı girebilirsiniz.") 
```


```python
if s == "iptal": break 
```

# örnek uygulama


```python
d1 = open("isimler1.txt") # dosyayı açıyoruz 
d1_satırlar = d1.readlines() # satırları okuyoruz
d2 = open("isimler2.txt") d2_satırlar = d2.readlines()
for i in d2_satırlar: 
    if not i in d1_satırlar: print(i)
d1.close()
d2.close() 
```

# hata yakalama

1.ProgramcıHataları(Error) 2.ProgramKusurları(Bug) 3.İstisnalar(Exception) 

Programcıdan kaynaklanan hatalar doğrudan doğruya programı yazan kişinin dikkatsizliğinden ötürü ortaya çıkan bariz hatalardır. Örneğin şu kod bir programcı hatasıiçerir


```python
print "Merhaba Python!" 
```

rBu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından veya en basit şekildeprogramcınınyaptığıyazımhatalarındankaynaklanır.Programcınınhatalarıgenellikle SyntaxErrorşeklindeortayaçıkar

Programkusurları,başkabirdeyişlebug‘lariseçokdahakarmaşıktır. Kusurluprogramlar çoğuzamanherhangibirhatavermedençalışır.Ancakprogramınürettiğiçıktılarbeklediğiniz gibideğildir. Örneğinyazdığınızprogramdabirformülhatasıyapmışolabilirsiniz. Bu durumda programınız hiçbir şey yokmuş gibi çalışır, ancak formül hatalı olduğu için hesaplamalarınsonuçlarıyanlıştır

Gelelimüçüncükategoriolanistisnalara(exceptions)... İstisnalar,adındandaazçokanlaşılacağıgibi,birprogramınçalışmasısırasındaortayaçıkan, normaldenfarklı,istisnaidurumlardır.Örneğinşuprogramabakalım:


```python
ilk_sayı = input("ilk sayı: ") 
ikinci_sayı = input("ikinci sayı: ")
ilk_sayı = int(ilk_sayı) ikinci_sayı = int(ikinci_sayı)
print(ilk_sayı, "/", ikinci_sayı, "=", ilk_sayı / ikinci_sayı)
```

yapabilir.Amaburadahesabakatmamızgerekenikişeyvar: 1.Kullanıcısayıyerine,sayıdeğerliolmayanbirveritipigirebilir.Meselailksayıyakarşılık 23,ikincisayıyakarşılık‘fdsfd’gibibirşeyyazabilir
2.Kullanıcıbirsayıyı0‘abölmeyeçalışabilir. Meselailksayıyakarşılık23,ikincisayıya karşılık0yazabilir. 

ştebuikiörnektegördüğümüz ValueError ve ZeroDivisionError bireristisnadır. Yani kullanıcıların,kendilerindensayıbeklenirkensayıdeğerliolmayanverigirmesiveyabirsayıyı 0’abölmeyeçalışmasıistisnaibirerdurumdurveyazdığımızprogramlarınexception(istisna) üretmesineyolaçar

2. try...except... 



```python
Biröncekibölümdehatalardanvehatalarıyakalamaktansözettik. Pekibuhatalarınasıl yakalayacağız
```


```python
ilk_sayı = input("ilk sayı: ") 
ikinci_sayı = input("ikinci sayı: ")
print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
try: sayı1 = int(ilk_sayı) sayı2 = int(ikinci_sayı) 
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2) 
    except ValueError: 
    print("Lütfen sadece sayı girin!") 
```

Biliyoruz ki, bir veriyi sayıya dönüştürmek istediğimizde eğer kullanıcı sayı değerli bir veriyerineharfdeğerlibirverigirerseprogramımızçöker. Dolayısıyla int(ilk_sayı) ve int(ikinci_sayı)kodları,kullanıcınıngireceğiveritürünegörehataüretmepotansiyeline sahiptir.Oyüzden,buradahatavereceğinibildiğimizokodlarıtrybloğuiçinealdık. Yinebildiğimizgibi,veridönüştürmeişlemisırasındakullanıcınınuygunolmayanbirveri girmesihalindeüretilecekhatabirValueError‘dır.Dolayısıylaexceptbloğuiçineyazacağımız hatatürününadıdaValueErrorolacaktır.OyüzdenValueErroradlıhatayıyakalayabilmek içinşusatırlarıyazdık: 
    
        



```python
except ValueError: print("Lütfen sadece sayı girin!") 
```

BuradabukodlarlaPython’aşuemrivermişolduk: EğertrybloğuiçindebelirtilenişlemlersırasındabirValueErrorilekarşılaşırsan bunu görmezden gel ve normal şartlar altında kullanıcıya göstereceğin hata mesajını gösterme. Onun yerine kullanıcıya Lütfen sadece sayı girin! uyarısınıgöster. YukarıdaTürkçeyeçevirdiğimizemriPythoncadanasılifadeettiğimizedikkatedin. Temel olarakşöylebiryapıylakarşıkarşıyayız: 


```python
try: hata verebileceğini bildiğimiz kodlar 
except HataAdı: hata durumunda yapılacak işlem 
```


```python
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ") 
try: sayı1 = int(ilk_sayı) sayı2 = int(ikinci_sayı) 
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2) 
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
```

türünüyakalamayolunagidiyoruz.Böylecekullanıcıyaanlamsızvekarmaşıkhatamesajları göstermekvedahadakötüsü,programımızınçökmesinesebepolmakyerinedahaanlaşılır mesajlarüretiyoruz. Yukarıdakikodlardaözelliklebirnoktadikkatiniziçekmişolmalı:Dikkatedersenizyukarıdaki kodlaraslındabirdeğilikifarklıhataüretmepotansiyelinesahip.Eğerkullanıcısayıdeğerli veriyerineharfdeğerlibirverigirerse ValueError,eğerbirsayıyı0‘abölmeyeçalışırsa da ZeroDivisionError hatası alıyoruz. Peki aynı kodlarda iki farklı hata türünü nasıl yakalayacağız? 


```python
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try: 
    sayı1 = int(ilk_sayı) 
    sayı2 = int(ikinci_sayı) 
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!") 
        except ValueError:
            print("Lütfen sadece sayı girin!")
```

3. try...except...as... 


```python
ValueError: invalid literal for int() with base 10: 'f' 
```

Burada‘ValueError’hatatürününadı,‘invalidliteralforint()withbase10: ‘f”isehatanın açıklamasıdır. Eğer istersek, yazdığımız programda bu hata açıklamasına erişebiliriz. Dikkatlicebakın


```python
ilk_sayı = input("ilk sayı: ") 
ikinci_sayı = input("ikinci sayı: ")
try: 
    sayı1 = int(ilk_sayı) 
    sayı2 = int(ikinci_sayı) 
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ValueError as hata: 
    print(hata) 
```

4. try...except...else... 


```python
try: 
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
    print(bölünen/bölen)
except ValueError: 
print("hata!") 
```

Buradaeğerkullanıcısayıyerineharfgirerse ValueError hatasıalırız. Buhatayı except ValueError: ifadesiyleyakalıyoruzvehataverildiğindekullanıcıyabirmesajgöstererek programımızınçökmesiniengelliyoruz.Amabiliyoruzki,bukodlarıçalıştırdığımızdaPython’ın verebileceğitekhataValueErrordeğildir.Eğerkullanıcıbirsayıyı0’abölmeyeçalışırsaPython 
roDivisionErroradlıhatayıverecektir.Dolayısıylabuhatayıdayakalamakiçinşöylebir şeyyazabiliriz:


```python
try: bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: ")) 
    print(bölünen/bölen) 
    except ValueError:
        print("Lütfen sadece sayı girin!") 
        except ZeroDivisionError: 
            print("Bir sayıyı 0'a bölemezsiniz!")
```

BuşekildehemValueErrorhatasınıhemdeZeroDivisionErrorhatasınıyakalamışoluruz. Bukodlarınözelliği,except... bloklarınıntekbirtry... bloğunutemelalmasıdır.Yanibiz buradabütünkodlarımızıtekbirtry...bloğuiçinetıkıştırıyoruz.Bublokiçindegerçekleşen hatalarıdadahasonratektek except... bloklarıyardımıylayakalıyoruz. Amaeğerbiz istersekbukodlardaverilebilecekhatalarıgruplamayıdatercihedebiliriz


```python
try: bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: ")) 
    except ValueError: 
        print("Lütfen sadece sayı girin!")
        else: try: print(bölünen/bölen)
                except ZeroDivisionError:
                    print("Bir sayıyı 0'a bölemezsiniz!") 
```

Buradayaptığımızşeyşu:İlktry... except... bloğuyardımıylaöncelikleint(input()) fonksiyonuilekullanıcıdangelecekverininsayıolupolmadığınıdenetliyoruz. Ardından bir else... bloğuaçarak, bununiçindeikinci try... except... bloğumuzudevreye sokuyoruz.Buradadabölmeişleminigerçekleştiriyoruz.Kullanıcınınbölmeişlemisırasında 0 sayısınıgirmesiihtimalinekarşıda except ZeroDivisionError ifadesiyardımıylaolası hatayıgöğüslüyoruz. Buşekildebirkodlamanınbizegetireceğiavantaj,hatalarüzerinde bellibirkontrolsağlamamızayardımcıolmasıdır. Yukarıdakikodlarsayesindehatalarabir nevi‘tekertekergelin!’ mesajıvermişoluyoruz. Böylelikleherblokiçindesadecealmayı beklediğimizhatayıkarşılıyoruz.Meselayukarıdailktry...bloğuiçindekidönüştürmeişlemi yalnızcaValueErrorhatasıverebilir. else: bloğundansonrakitry... bloğundayeralan işlemiseancak ZeroDivisionError verecektir. Bizyukarıdakullandığımızyapısayesinde herbirhatayıtektekveyerigeldiğindekarşılıyoruz. Budurumunaksine,bölümünilk başındaverdiğimiztry... exceptbloğundahemValueErrorhemdeZeroDivisionError hatalarınıngerçekleşmeihtimalibulunuyor. Dolayısıylabizoradabütünhatalarıtekbir try...bloğuiçinesıkıştırmışoluyoruz.İşteelse:bloğubusıkışıklığıgidermişoluyor.Ancak sizibirkonudauyarmakisterim:Buyapı,heraklageldiğindekullanılacakbiryapıdeğildir. Büyük programlarda bu tarz bir kullanım kodlarınızın darmadağın olmasına, kodlarınız üzerindekidenetimitamamenkaybetmenizedeyolaçabilir. Sonundadaelinizdebölük pörçükbirkodyığınıkalabilir.Zatenaçıkçasöylemekgerekirsetry... except... else... yapısınınçokgenişbirkullanımalanıyoktur.Buyapıancakçoknadirdurumlardakullanılmayı gerektirebilir.Dolayısıylabuüçlüyapıyıhiçkullanmadanbirömrürahatlıklageçirebilirsiniz

5. try...except...ﬁnally... 


```python
try: ...bir takım işler...
    except birHata: ...hata alınınca yapılacak işlemler... 
        finally: ...hata olsa da olmasa da yapılması gerekenler... 
```

6. raise


```python
bölünen = int(input("bölünecek sayı: "))
if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")
bölen = int(input("bölen sayı: "))
print(bölünen/bölen)
```

Buradaeğerkullanıcı23sayısınıgirerse,kullanıcıyabirhatamesajıgösterilipprogramdan çıkılacaktır.BizbukodlardaExceptionadlıgenelhatamesajınıkullandık.BuradaException yerineheristediğimiziyazamayız.YazabileceklerimizancakPython’datanımlıhatamesajları olabilir.ÖrneğinNameError,TypeError,ZeroDivisionError,IOError,vb... 


```python
tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")
for i in parola: if i in tr_karakter: raise TypeError("Parolada Türkçe karakter kullanılamaz!") 
        else: pass
print("Parola kabul edildi!") 
```

ukodlarçalıştırıldığında,eğerkullanıcı,içindeTürkçekaraktergeçenbirparolayazarsa kendisineTypeErrortipindebirhatamesajıgösteriyoruz. EğerkullanıcınınparolasıTürkçe karakteriçermiyorsahiçbirşeyyapmadangeçiyoruzvebirsonrakisatırdakendisine‘Parola kabuledildi!’mesajınıgösteriyoruz

7. BütünHatalarıYakalamak 


```python
try:
birtakım işler
except: 
hata mesajı
```

Ayrıca,eğerkendimizbirprogramgeliştirirkensürekliolarakbutarzbiryazımıbenimsersek, kendikodlarımızdakihatalarıdamaskelemişoluruz. Dolayısıyla,Pythonyukarıdakigeniş kapsamlı except... bloğu nedeniyle programımızdaki bütün hataları gizleyeceği için, programımızdakipotansiyelaksaklıklarıgörmeimkanımızolmaz. Dolayısıylabutürbir yapıdanolabildiğincekaçınmaktafaydavar.Ancakelbetteböylebirkodyazmanızıgerektiren birdurumladakarşılaşabilirsiniz.Örneğin


```python
try: 
    birtakım kodlar
    except ValueError: 
        print("Yanlış değer") 
        except ZeroDivisionError: 
            print("Sıfıra bölme hatası")
            except:
                print("Beklenmeyen bir hata oluştu!")
```

Burada olası bütün hata türlerini yakaladıktan sonra, bunların dışında bizim o anda öngöremediğimiz bir hatanın oluşması ihtimaline karşı except: kodunu kullanarak kullanıcıyagenelbirhatamesajıgöstermeyitercihedebiliriz.Böylecebeklenmeyenbirhata meydanagelmesidurumundadaprogramımızçökmekyerineçalışmayadevamedebilecektir. 

# Karakter Dizilerinin Öğelerine Erişmek


```python
kardiz = "Python"
```


```python
 kardiz[0]

```

Belkifarkındasınız,belkidedeğilsiniz,amaaslındaşunoktadakarakterdizilerininçokönemli birözelliğiilekarşıkarşıyayız.Gördüğünüzgibi,yukarıdabahsettiğimizsırakavramısayesinde Python’dakarakterdizilerininbütünöğelerinetektekveherhangibirsıragözetmeksizin erişmemizmümkün.Meselayukarıdakiilkörnektekardiz[0]gibibiryapıkullanarakkarakter dizisininsıfırıncı(yaniilk)öğesini,nesne[1]gibibiryapıkullanarakdakarakterdizisininbirinci (yaniaslındaikinci)öğesinialabildik. Buyapınınmantığınıkavramakiçinşuörnekleridikkatliceinceleyin: 


```python
 kardiz = "Python"
>>> kardiz[0]
'P'
>>> kardiz[1]
'y'
>>> kardiz[3]
'h'
>>> kardiz[5]

```

karakter_dizisi[öğe_sırası]


```python
 nesne = "123456789" 
    int(nesne[1]) * 2

```

# KarakterDizileriniDilimlemek


```python
 site = "www.istihza.com" 
 
 site[4:11]
site[12:16]

 site[0:3]

```

karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası] 


```python
>>> karakter_dizisi = "istanbul" 
>>> karakter_dizisi[0:3]
'ist
```

Buradaalacağımızilköğeninsıranumarası0. Yani“istanbul”karakterdizisindeki‘i’harﬁ. Alacağımızsonöğeninsıranumarasının1fazlasıise3. Yani2. sıradaki‘t’harﬁ. İşte karakter_dizisi[0:3]dediğimizde,Python0. öğeile3. öğearasındakalanbütünöğeleri bizeverecektir.Bizimörneğimizdebuaralıktakiöğeler‘i’,‘s’ve‘t’harﬂeri.DolayısıylaPython bize‘istanbul’kelimesindeki‘ist’kısmınıdilimleyipveriyor. Bubilgilerikullanarakşöylebiruygulamayazalım: 


```python
site1 = "www.google.com" 
site2 = "www.istihza.com" 
site3 = "www.yahoo.com" 
site4 = "www.gnu.org"
for isim in site1, site2, site3, site4: 
print("site: ", isim[4:-4]) 
```

# KarakterDizileriniTersÇevirmek 

Eğeramacınızbirkarakterdizisinitersçevirmek,yanikarakterdizisiiçindekiherbiröğeyi terstenyazdırmaksabirazönceöğrendiğimizdilimlemeyönteminikullanabilirsiniz.Dikkatlice bakın: 


```python
 kardiz[::-1]

```

Gördüğünüz gibi, “Sana Gül Bahçesi Vadetmedim” adlı karakter dizisi içindeki bütün karakterlersondanbaşadoğruekranadizildi. AslındabukomutlaPython’aşöylebiremirvermişoluyoruz: kardiz değişkeniiçindekibütünkarakterleri,ensonkarakterdenilkkaraktere kadarsondanbaşadoğrutektekekranayazdır! Bildiğinizgibi,eğeralmakistediğimizkarakter,diziiçindekiilkkaraktersebukarakterindizi içindekisırasınıbelirtmemizegerekyok. Aynışekilde,eğeralmakistediğimizkarakter,dizi içindekisonkarakterse,bukarakterindediziiçindekisırasınıbelirtmemizegerekyok. İşte yukarıdakiörnektebukuraldanyararlandık. Eğer bir karakter dizisinin tamamının değil de, sadece belli bir kısmının ters çevrilmiş halinieldeetmekistiyorsanızelbetteyapmanızgerekenşey,almakistediğinizilkveson karakterlerinsırasınıparanteziçindebelirtmekolacaktır.Meselayukarıdakikarakterdizisinde sadece‘Gül’kelimesinitersçevirmekistersekşöylebirşeyyazabiliriz: 


```python
 kardiz[7:4:-1]

```

Gül ters yazdık

kardiz[ilk_karakter:son_karakter:atlama_sayısı] 

# KarakterDizileriniAlfabeSırasınaDizmek

Python’dakarakterdizilerininöğelerinetektekulaşma,öğeleridilimlemevetersçevirmenin yanısıra,buöğelerialfabesırasınadizmekdemümkündür. Bununiçin sorted() adlıbir fonksiyondanyararlanacağı


```python
sorted("kitap")

```

# KarakterDizileriÜzerindeDeğişiklikYapmak


```python
 meyve = "elma" 
```


```python
"E" + meyve[1:]
```

Belkifarkındayız,belkidedeğiliz,amaaslındayukarıdakiörneklerkarakterdizilerihakkında bizeçokönemlibirbilgiveriyor. Dikkatettiysenizyukarıdakiörneklerdekarakterdizileri üzerindebirdeğişiklikyapmışızgibigörünüyor. Esasındaöylededenebilir. Ancakburada önemlibirayrıntıvar. Yukarıdakiörneklerdegördüğümüzdeğişikliklerkalıcıdeğildir. Yani aslındabudeğişikliklerinorijinalkarakterdizisiüzerindehiçbiretkisiyoktu

# dir() 

 BumetotbizePython’dakibir nesneninözelliklerihakkındabilgiedinmeimkanıverecek. Meselakarakterdizilerininbize hangimetotlarısunduğunugörmekiçinbufonksiyonuşöylekullanabiliriz


```python
 dir(str)

```

İngilizcede‘karakterdizisi’ninkarşılığınınstring,bukelimeninkısaltmasınında‘str’olduğunu hatırlıyor olmalısınız. İşte dir() fonksiyonuna parametre olarak bu ‘str’ kelimesini verdiğimizde,Pythonbizekarakterdizilerininbütünmetotlarınılisteliyor. Karakterdizileridışında, şimdiyekadaröğrendiğimizbaşkabirveritipidesayılar. Biz Python’dasayılarıntamsayılar(integer),kayannoktalısayılar(ﬂoat)vekarmaşıksayılar (complex)olaraküçeayrıldığınıdabiliyoruz.Örnekolmasıaçısındandir()fonksiyonunubir desırasıyla,tamsayılar,kayannoktalısayılarvekarmaşıksayılarüzerindedeuygulayalım


```python
 dir(int)
>>> dir(float)
>>> dir(complex) 
```

# enumerate() 

Eğer yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız gerekiyorsa Python’ınsizesunduğuçoközelbirfonksiyondanyararlanabilirsiniz. Bufonksiyonunadı enumerate().


```python
 enumerate("istihza")

```

Tıpkıreversed()fonksiyonununbir‘reversed’nesnesivermesigibi,bufonksiyonundabize yalnızcabir‘enumerate’nesnesiverdiğinigörüyorsunuz

Enumerate kelimesi İngilizcede ‘numaralamak, numaralandırmak’ gibi anlamlara gelir. Dolayısıylaenumerate()fonksiyonu,kendisineparametreolarakverilendeğerhakkındabize ikifarklıbilgiverir:Biröğevebuöğeyeaitbirsıranumarası.Yukarıdakiçıktıdagördüğünüz şeydeişteherbiröğeninkendisiveoöğeyeaitbirsıranumarasıdır.


```python
sayaç = 0

```


```python
for i in dir(""):
    if "_" not in i[0]:
        sayaç += 1 
        print(sayaç, i) 
```


```python
for sıra, metot in enumerate(dir("")): 
    print(sıra, metot) 
```


```python
for sıra, metot in enumerate(dir("")): ... 
    print(metot, sıra) ... 
    
```

# help()

Python’lailgiliherhangibirkonudayardımaihtiyacınızolduğunda,internettenaraştırma yaparakpekçokayrıntılıbelgeyeulaşabilirsiniz. Amaeğerherhangibirnesnehakkında hızlıbirşekildeveİngilizceolarakyardımalmakistersenizhelp()adlıözelbirfonksiyondan yararlanabilirsiniz. Bufonksiyonuikifarklışekildekullanıyoruz. Birinciyöntemde,etkileşimlikabuğa help() yazıpEnterdüğmesinebasıyoruz: 


```python
help> dir
```

# Karakter Dizilerinin Metotları


```python
bumetodukullanarakbirkarakterdizisi içindekikarakterleribaşkakarakterlerledeğiştirebileceğiz
```


```python
kardiz.replace("e", "E")

```

Gördüğünüzgibi,replace()sondereceyararlıvekullanımıoldukçakolaybirmetot.Buarada builkmetodumuzsayesindePython’dakimetotlarınnasılkullanılacağıkonusundadabilgi edinmişolduk.Yukarıdakiörneklerinbizegösterdiğigibişöylebirformüllekarşıkarşıyayız

karakter_dizisi.metot(parametre) 

Metotlarkarakterdizilerindennoktaileayrılır.Python’dabuyönteme‘noktalıgösterim’(dot notation)adıverilir. Buaradametotlarıngörünüşvekullanımolarakfonksiyonlaranekadarbenzediğinedikkat edin.Tıpkıfonksiyonlardaolduğugibi,metotlardabirtakımparametreleralabiliyor. Yukarıdakiörnekte,replace()metodununikifarklıparametrealdığınıgörüyoruz.Bumetoda verdiğimizilkparametredeğiştirmekistediğimizkarakterdizisinigösteriyor.İkinciparametre isebirinciparametredebelirlediğimizkarakterdizisininyerinenekoyacağımızıbelirtiyor.Yani replace()metoduşöylebirformülesahiptir: 


```python
karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi) 
```


```python
 kardiz = "memleket" 
    >>> kardiz.replace("ket", "KET")
 
```

Buradareplace()metodunuüçüncübirparametreilebirliktekullandık.Üçüncüparametre olarak1sayısınıverdiğimiziçinreplace()metodusadecetekbir“e”harﬁnisildi. Buüçüncüparametreyi,silmekistediğinizharfsayısıkadarartırabilirsiniz.Mesela: 


```python
>>> kardiz.replace("e", "", 2)
'mmlket'
>>> kardiz.replace("e", "", 3)
'mmlkt'
```

Karakterdizilerikonusununilkbölümünde‘değiştirilebilirlik’(mutability)üzerinesöylediğimiz şeylerinburadadageçerliolduğunuunutmayın.Oradadasöylediğimizgibi,karakterdizileri değiştirilemeyenveritipleridir.Dolayısıylaeğerbirkarakterdizisiüzerindedeğişiklikyapmak istiyorsanız,okarakterdizisinibaştantanımlamalısınız.Örneğin


```python
 meyve = "elma" >>> 
    meyve = meyve.replace("e", "E")
    >>> meyve

```

# split(),rsplit(),splitlines() 

Şimdisizeşöylebirsorusorduğumudüşünün:Acabaaşağıdakikarakterdizisindeyeralan bütünkelimelerinilkharﬁninasılalırız? 


```python
kardiz = "İstanbul Büyükşehir Belediyesi"
```


```python
print(kardiz[0], kardiz[9], kardiz[20], sep="")

```


```python
kardiz = "İstanbul Büyükşehir Belediyesi" 
>>> kardiz.split()

```

Buradakullanıcıhangikurumadınıgirersegirsin, bukurumadınınherkelimesininilk harﬁekranadökülecektir. Örneğinkullanıcıburada“TürkiyeBüyükMilletMeclisi”ifadesini girmişsesplit()metoduönceliklebuifadeyialıpşuşekledönüştürür

['Türkiye', 'Büyük', 'Millet', 'Meclisi'] 

rsplit() metodununpekyaygınkullanılanbirmetotolmadığınıbelirterek splitlines() metodunageçelim. Bildiğiniz gibi, split() metodunu bir karakter dizisini kelime kelime ayırabilmek için kullanabiliyoruz. splitlines() metodunuisebirkarakterdizisinisatırsatırayırmakiçin
 kullanabiliriz. Meselaelinizdeuzunbirmetinolduğunuveamacınızınbumetiniçindeki herbirsatırıayrıayrıalmakolduğunudüşünün.İştesplitlines()metoduylabuamacınızı gerçekleştirebilirsiniz.Hemenbirörnekverelim


```python
metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz."""
print(metin.splitlines()) 
```


```python
print(metin.splitlines(True)) 
```

# lower() 


```python
kişi = input("Aradığınız kişinin adı ve soyadı: ") 
kişi = kişi.lower()
if kişi == "ahmet öz": print("email: aoz@hmail.com") 
    print("tel : 02121231212")
    print("şehir: istanbul")
elif kişi == "mehmet söz": 
    print("email: msoz@zmail.com")
    print("tel : 03121231212") 
    print("şehir: ankara")
elif kişi == "mahmut göz":
    print("email: mgoz@jmail.com")
    print("tel : 02161231212") 
    print("şehir: istanbul")
else:
    print("Aradığınız kişi veritabanında yok!") 
    
```


```python
>>> kardiz = "ELMA" >>> kardiz.lower()
'elma'
>>> kardiz = "arMuT" >>> kardiz.lower()
'armut'
>>> kardiz = "PYTHON PROGRAMLAMA" >>> kardiz.lower()

```

İşteverdiğimizörnekprogramdada lower() metodununbuözelliğindenyararlandık. Bu metotsayesinde,kullanıcınetürbirkelimegirersegirsin,bukelimelerherhalükardaküçük harfeçevrileceğiiçin,ifbloklarıkullanıcıdangelenveriyiyakalayabilecektir

# upper()

Hatırlarsanız lower() metoduyardımıylakarakterdizileriiçindekiharﬂeriküçültüyorduk. upper()metoduisebuharﬂeribüyütmemizisağlar


```python
 kardiz = "istanbul" >>> kardiz.upper()
'ISTANBUL' 
```

lower()metoduTürkçe’deki‘I’harﬁni‘i’şeklindeküçültüyordu.upper()metoduise‘i’harﬁni yanlışolarak‘I’şeklindebüyütüyor.Elbettebusorundaçözülemeyecekgibideğil.Buradada lower()metoduiçinuyguladığımızyönteminbirbenzeriniuygulayacağız


```python
iller = "istanbul, izmir, siirt, mersin"
iller = iller.replace("i", "İ").upper() 
print(iller) 
```

# islower(),isupper()

karıda öğrendiğimiz lower() ve upper() adlı metotlar karakter dizileri üzerinde bazı değişiklikleryapmamızayardımcıoluyor. Karakterdizileriüzerindebirtakımdeğişiklikler yapmamızısağlayanbutürmetotlara‘değiştiricimetotlar’adıverilir. Butürmetotların dışında bir de ‘sorgulayıcı metotlar’dan söz edebiliriz. Sorgulayıcı metotlar, değiştirici metotların aksine, bir karakter dizisi üzerinde değişiklik yapmamızı sağlamaz. Bu tür metotlarıngörevikarakterdizilerinindurumunusorgulamaktır.Sorgulayıcımetotlaraörnek olarakislower()veisupper()metotlarınıverebiliriz

 islower()metoduisebirkarakterdizisinintamamenküçükharﬂerdenoluşup oluşmadığınısorguluyor.


```python
 kardiz = "Ankara" >>> kardiz.islower()

```


```python
veri = input("mesajınız: ") böl = veri.split()
for i in böl: 
    if i.isupper():
        print("Tamamı büyük harflerden oluşan kelimeler kullanmayın!")
```

# endswith() 

endswith() metodukarakterdizileriüzerindeherhangibirdeğişiklikyapmamızı sağlamaz.Bumetodungörevikarakterdizisinindurumunusorgulamaktır


```python
 kardiz.endswith("z")
```

# startswith() 

Bumetot,birazöncegördüğümüz endswith() metodununyaptığıişintamtersiniyapar. Hatırlarsanız endswith() metodubirkarakterdizisininhangikarakterveyakarakterlerle bittiğinidenetliyordu. startswith()metoduisebirkarakterdizisininhangikarakterveya karakterlerlebaşladığınıdenetler


```python
 kardiz = "python" >>> kardiz.startswith("p")
True
>>> kardiz.startswith("a")
```

# capitalize()

imdigöreceğimiz capitalize() metoduda upper() ve lower() metotlarınabenzemekle birlikte onlardan biraz daha farklı davranır: capitalize() metodunun görevi karakter dizilerininyalnızcailkharﬁnibüyütmektir.


```python
 a = "python"
a.capitalize()

```

# title() 

Bu metot biraz önce öğrendiğimiz capitalize() metoduna benzer. Bildiğiniz gibi capitalize()metodubirkarakterdizisininyalnızcailkharﬁnibüyütüyordu.title()metodu dakarakterdizilerininilkharﬁnibüyütür. Ama capitalize() metodundanfarklıolarak bumetot,birdenfazlakelimedenoluşankarakterdizilerininherkelimesininilkharﬂerini büyütür. 


```python
 a.title()
```

# swapcase() 

swapcase()metodudabüyük-küçükharﬂeilgilibirmetottur. Bumetotbirkarakterdizisi içindekibüyükharﬂeriküçükharfe;küçükharﬂeridebüyükharfedönüştürür


```python
>>> kardiz = "python" 
>>> kardiz.swapcase()

```

# casefold() 

Bumetotişlevolaraklower()metodunaçokbenzer. HattaTürkçeaçısından,bumetodun lower()metodundanhiçbirfarkıyoktur. Ancakbazıbaşkadillerde,bumetotbazıharﬂer içinlower()metodununverdiğindenfarklıbirçıktıverir. ÖrneğinAlmancadaki‘ß’harﬁbu durumabirörnekolabilir: 


```python
 "ß".lower() 'ß'
>>> "ß".casefold()
 
```

Gördüğünüzgibi,lower()vecasefold()metotlarıbuharfefarklıdavranıyor. Türkçedekiİ-isorunubumetotiçindeaynengeçerlidir

# join()

Hatırlarsanızşimdiyekadaröğrendiğimizmetotlararasındasplit()adlıbirmetotvardı.Bu metodunneişeyaradığınıvenasılkullanıldığınıbiliyorsunuz: 


```python
>>> kardiz = "Beşiktaş Jimnastik Kulübü" 
>>> bölünmüş = kardiz.split() 
>>> print(bölünmüş)
# ['Beşiktaş', 'Jimnastik', 'Kulübü']
```

Gördüğünüzgibi split() metodubirkarakterdizisinibelliyerlerdenbölerekparçalara ayırıyor.Bunoktadainsanınaklınaşöylebirsorugeliyor:Diyelimkielimizdeböylebölünmüş birkarakterdizisigrubuvar.Bizbugrupiçindekikarakterdizilerinitekrarbirleştirmekistersek neyapacağız? Şimdişukodlaraçokdikkatlicebakın: 


```python
" ".join(bölünmüş)
```

# count() 

ıpkıdahaönceöğrendiğimizsorgulayıcımetotlargibi,count()metodudabirkarakterdizisi üzerindeherhangibirdeğişiklikyapmamızısağlamaz.Bumetodungörevibirkarakterdizisi içindebellibirkarakterinkaçkezgeçtiğinisorgulamaktır. Bununlailgilihemenbirörnek verelim: 


```python
>>> şehir = "Kahramanmaraş" >>> şehir.count("a")
```

# index(),rindex()

Örneğin“python”adlıkarakterdizisinde ‘p’harﬁninsırası0‘dır.Aynışekilde‘n’harﬁninsırasıise5‘tir.Karakterlerin,birkarakterdizisi içindehangisıradabulunduğunuöğrenmekiçinindex()adlıbirmetottanyararlanabiliriz. Örneğin


```python
>>> kardiz = "python" >>> kardiz.index("p")
0
>>> kardiz.index("n")

```

Eğersırasınısorguladığımızkarakter,okarakterdizisiiçindebulunmuyorsa,budurumda Pythonbizebirhatamesajıgösterir: 

Hatırlarsanız, bundanönce count() adlıbirmetotöğrenmiştik. Ometotdatoplam3 parametrealıyordu. count()metodundakullandığımız2. ve3. parametreleringörevlerini hatırlıyorolmalısınız. İşte index() metodunun2. ve3. parametrelerideaynen count() metodundaki gibi çalışır. Yani Python’ın sorgulama işlemini hangi sıra aralıklarından gerçekleştireceğinigösterir.Meselayukarıdakiörnektebiz“adana”karakterdizisinin1.ve3. sıralarıarasındaki‘a’harﬂerinisorguladık.YaniyukarıdakiörnektePython‘a’harﬁniaramaya 1. konumdanbaşladıvearamayı3. konumdakesti. Böylece“adana”karakterdizisinin2. sırasındaki‘a’harﬁninkonumunubizebildirdi. Gördüğünüz gibi, index() metodu bize aradığımız karakterin yalnızca ilk konumunu bildiriyor. Pekibizmesela“adana” karakterdizisiiçindekibütün‘a’harﬂerininsırasını öğrenmekistersekneyapacağız? Buisteğimiziyerinegetirmekiçinkarakterdizisininherbirsırasınıtektekkontroletmemiz yeterliolacaktır.Yanişöylebirşeyyazmamızgerekiyor: 


```python
kardiz = "adana"
print(kardiz.index("a", 0))
print(kardiz.index("a", 1)) 
print(kardiz.index("a", 2))
print(kardiz.index("a", 3)) 
print(kardiz.index("a", 4)) 
```

# ﬁnd,rﬁnd() 

find() ve rfind() metotlarıtamamen index() ve rindex() metotlarınabenzer. find() ve rfind() metotlarınıngörevidebirkarakterdizisiiçindekibirkarakterinkonumunu sorgulamaktır: 


```python
>>> kardiz = "adana" >>> kardiz.find("a")
0
>>> kardiz.rfind("a")
```

# center() 

Centerkelimesiİngilizce’de‘orta,merkez,ortalamak’gibianlamlaragelir.Buanlamauygun olarak,center()metodunukarakterdizileriniortalamakiçinkullanabilirsiniz


```python
for metot in dir(""): print(metot.center(15)) 
```


```python
>>> kardiz = "python" 
kardiz.center(10)
```

# rjust(),ljust()

Bumetotlardatıpkıbirönceki center() metodugibikarakterdizilerinihizalamavazifesi görür.rjust()metodubirkarakterdizisinisağayaslarken,ljust()metodukarakterdizisini solayaslar.Meselaşuikikodparçasınınçıktılarınıinceleyin: 


```python
>>> for i in dir(""):
    ... print(i.ljust(20))
>>> for i in dir(""):
    ... print(i.rjust(20)) 
```

# zﬁll() 

Bumetotkimiyerlerdeişimiziepeykolaylaştırabilir. zfill() metoduyardımıylakarakter dizilerininsoltarafınaistediğimizsayıdasıfırekleyebiliriz: 


```python
>>> a = "12" 
>>> a.zfill(3)
```


```python

```


```python

```
