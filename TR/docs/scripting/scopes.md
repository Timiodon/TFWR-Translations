[<- Fonksiyonlar](docs/scripting/functions.md)
---
# Ad Kapsamları
Kapsamlar, değişkenlere nereden erişilebileceğini belirler. Bir kapsam temelde adları değerlerle eşleyen bir yapıdır.
Python'dakine çok benzer şekilde çalışırlar.

Bir global kapsam vardır ve her fonksiyonun da kendi yerel kapsamı vardır.
Bir değişken tanımladığında, o değişken geçerli kapsama eklenir.
Bir fonksiyon tanımının dışındaki her şey global kapsamın parçası sayılır.

`x = 1`
Global kapsamda `x` adına `1` değerini atar.

Bu `def` komutu, global kapsamda `f` adına bir fonksiyon atar.
`def f():
    `Burada `f` fonksiyonunun yerel kapsamında `y` adına `1` değeri atanır.`
    y = 1

    `Burada `f` fonksiyonunun yerel kapsamında `g` adına bir fonksiyon atanır.`
    def g():
        pass`

`f()`
Global kapsamdan `f` içinde saklanan fonksiyonu alır ve çağırır.

`print(y)`
Global kapsamdaki bu `print` komutu hata verir, çünkü `y` global kapsamda hiç tanımlanmadı, bu yüzden onu burada okuyamayız.
O yalnızca `f` fonksiyonunun yerel kapsamında vardı.

## global Anahtar Kelimesi
Varsayılan olarak, global kapsamda aynı adda bir değişken olsa bile fonksiyonlardaki tüm değişkenler yerel kapsama bağlanır.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x = 0

def f():
    x = 1
f()
print(x)
}}

Bu kod `0` yazdırır, çünkü `f` içindeki yerel `x`, global `x` ile aynı değişken değildir; bu yüzden global `x` değişmeden kalır. Bu önemlidir, çünkü aksi halde bir fonksiyon çağrısı, sırf o fonksiyonun yerel değişkenlerinden biriyle aynı ada sahip olan bir global değişkenin üzerine yanlışlıkla yazabilirdi.

Bir global değişkene yazmak istiyorsan bunu `global` anahtar kelimesiyle açıkça belirtmen gerekir.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x = 0

def f():
    global x
    x = 1
f()
print(x)
}}

Bu örnekte `global x`, `x` adını yukarıda tanımlanan global `x` değişkenine bağlar. Artık kod `1` yazdırır.
Unutma: Global değişkenleri değiştirmek genellikle spagetti koda giden ilk adımdır. Spagetti kodda programın her parçası diğer tüm parçaları etkiler; o yüzden bunu aşırıya kaçırma.

## Döngüler ve Dallanmalar
Döngüler ve dallanmalar kendi kapsamlarını oluşturmaz, bu yüzden içlerinde tanımlanan her şey dışarıda da kullanılabilir.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(3):
    pass
print(i)
}}

Bu kod `2` yazdırır, çünkü `for` döngüsünün son yinelemesi `i` değişkenine `2` değerini atamıştır.

---

[Değişkenler](docs/scripting/variables.md)      [Fonksiyonlar](docs/scripting/functions.md)      [Import](docs/scripting/import.md)      [Mega Çiftlik](docs/unlocks/megafarm.md)
