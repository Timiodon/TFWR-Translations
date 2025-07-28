# İsim Kapsamları (Scope)
Scope'lar, hangi değişkenlere nereden erişilebileceğini belirler. Bir scope temel olarak isimlerden değerlere bir eşlemedir.
Temel olarak Python'daki gibi çalışırlar.

Bir global scope vardır ve her fonksiyonun bir local scope'u vardır.
Bir değişken tanımladığında, mevcut scope'a eklenir.
Bir fonksiyon tanımının dışındaki her şey global scope'un bir parçası olarak kabul edilir.

`x = 1`
Global scope'taki `x` ismine `1` değerini atar.

Bu `def` ifadesi, global scope'taki `f` ismine bir fonksiyon atar.
`def f():
    `'f'nin local scope'undaki 'y' ismine '1' değerini ata.`
    y = 1

    `'f'nin local scope'undaki 'g' ismine bir fonksiyon ata.`
    def g():
        pass`

`f()`
Global scope'tan `f` içinde saklanan fonksiyonu alır ve onu çağırır.

`print(y)`
Global scope'taki bu print ifadesi bir error verir çünkü `y` global scope'ta hiç bildirilmedi, bu yüzden onu burada okuyamayız.
Sadece `f`'in local scope'unda mevcuttu.

## global anahtar kelimesi
Varsayılan olarak, fonksiyonlardaki tüm değişkenler, global scope'ta aynı isimde bir değişken olsa bile, local scope'a bağlanır.

`x = 0

def f():
    x = 1
f()
print(x)`

Bu kod `0` yazdırır çünkü `f` içindeki local `x`, global `x` ile aynı değişken değildir, bu yüzden global `x` değişmeden kalır. Bu önemlidir çünkü aksi takdirde bir fonksiyon çağrısı, yanlışlıkla o fonksiyonun bir local değişkeniyle aynı isme sahip bir global değişkenin üzerine yazabilir.

Eğer bir global değişkene yazmak istiyorsan, bunu açıkça `global` anahtar kelimesini kullanarak yapmalısın.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Bu örnekte, `global x`, `x`'i üzerinde tanımlanan global `x` değişkenine bağlar. Bu şimdi `1` yazdıracaktır.
Global değişkenleri değiştirmenin genellikle spagetti koda doğru ilk adım olduğunu unutma; bu kodda programın her parçası diğer her parçasını etkiler, bu yüzden aşırı kullanma.

## Döngüler ve dallanmalar
Döngüler ve dallanmalar kendi scope'larını oluşturmaz, bu yüzden içlerinde tanımlanan her şey dışarıda da kullanılabilir.

`for i in range(3):
    pass
print(i)`

Bu, `2` yazdıracaktır çünkü `for` döngüsünün son yinelemesi `i`'ye `2` atamıştır.