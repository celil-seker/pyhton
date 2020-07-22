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


```python

```
