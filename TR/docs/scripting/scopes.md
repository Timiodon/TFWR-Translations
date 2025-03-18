# İsim Kapsamları

Kapsamlar, hangi değişkenlerin nereden erişilebileceğini belirler. Bir kapsam, esasen isimlerden değerlere bir eşlemedir.
Python'da olduğu gibi çalışırlar.

Bir global kapsam vardır ve her fonksiyonun lokal bir kapsamı vardır.
Bir değişken tanımladığınızda, mevcut kapsama eklenir.
Bir fonksiyon tanımının dışındaki her şey global kapsamın parçası olarak kabul edilir.

`x = 1`
`x` ismine global kapsamda `1` değeri atanır.

Bu `def` ifadesi, bir fonksiyonu global kapsamda `f` ismine atar.
`def f():
    ``f` fonksiyonunun lokal kapsamında `y` ismine `1` değeri atayın.`
    y = 1

    ``f` fonksiyonunun lokal kapsamına `g` ismine bir fonksiyon atayın.`
    def g():
        pass`

`f()`
Global kapsamdan `f` içinde saklanan fonksiyonu alır ve çağırır.

`print(y)`
Global kapsamda bu print ifadesi bir hata fırlatır çünkü `y` global kapsamda asla tanımlanmadı, bu yüzden burada okunamaz.
Sadece `f`'nin lokal kapsamı içinde vardı.

## global anahtar kelimesi

Varsayılan olarak, fonksiyonlardaki tüm değişkenler, aynı isimde bir değişken global kapsamda bile varsa, lokal kapsama bağlanır.

`x == 0

def f():
    x = 1
f()
print(x)`

Bu kod `0` yazdırır çünkü `f` içindeki lokal `x`, global `x` ile aynı değişken değildir, bu yüzden global `x` değişmeden kalır. Bu önemlidir çünkü aksi takdirde, bir fonksiyon çağrısı sadece bir rastlantı sonucu o fonksiyonun lokal değişkeniyle aynı isme sahip global bir değişkeni yanlışlıkla değiştirebilir.

Eğer bir global değişkene yazmak istiyorsanız, bunu açıkça `global` anahtar kelimesini kullanarak yapmalısınız.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

Bu örnekte, `global x` yukarıda tanımlanan global `x` değişkenine `x` bağlar. Bu da artık `1` yazdırır.
Not: global değişkenleri değiştirmek genellikle her kısmın programın diğer kısımlarını etkilediği spagetti koduna giden ilk adımdır, bu yüzden aşırı kullanmayın.

## Döngüler ve dallar

Döngüler ve dallar kendi kapsamlarını oluşturmaz, bu yüzden içinde tanımlanan her şey dışarıda da kullanılabilir.

`for i in range(3):
    pass
print(i)`

Bu, `2` yazdırır çünkü `for` döngüsünün son yinelemesi `i`'ye `2` atamıştır.