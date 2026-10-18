[<- Operatörler](docs/scripting/operators.md) <right>[Listeler ->](docs/scripting/lists.md)
<right>[Fonksiyonlar ->](docs/scripting/functions.md)
---
# Değişkenler
Değişkenleri, içinde bir değer tutabilen adlandırılmış kutular gibi düşünebilirsin.
`=` operatörü, bir değişken tanımlamak ve içine bir değer koymak için kullanılır.

`variable_name = value`

Operatörün sol tarafı değişkenin adıdır. Ona istediğin geçerli herhangi bir adı verebilirsin.
Sağ taraf ise sonucu değişkende saklanacak olan bir ifadedir.

`a` adında bir değişken tanımla ve içine `5` değerini koy:
`a = 5`
`b` adında bir değişken tanımla ve içine `can_harvest()` fonksiyonunun dönüş değerini koy:
`b = can_harvest()`

`=` operatörünü `==` operatörüyle karıştırma. 
`==` operatörü iki değerin eşit olup olmadığını kontrol eder ve `True` ya da `False` döndürür.
`=` operatörü ise sağdaki değeri soldaki ada atar.

Bir değişkene değer atadıktan sonra, içerdiği değeri almak için onu kodda kullanabilirsin.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
a = 5
for i in range(a):
	do_a_flip()
}}

Yukarıdaki döngü 5 kez çalışır, çünkü `a` değişkeninin değeri `5`.
`for` döngüsündeki `i` de bir değişkendir. Her yinelemede dizinin o anki değeri ona otomatik olarak atanır. Adının `i` olması gerekmez; ona geçerli herhangi bir değişken adı verebilirsin.

Değişkenler sayesinde aynı şeyi bir while döngüsüyle de yapabilirsin:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

Bu kod, yukarıdaki `for` döngüsüyle aynı şeyi yapar, ama `i`'yi elle artırmamız gerekir.
`i`'yi artırmak için ona o anki değerinin `1` fazlasını atarız. Bir değişkeni önceki değerine göre değiştirmek çok sık yapılan bir şeydir.
Bu işlem şu operatörlerle kısaltılabilir: `+=, -=, *=, /=, %=`

`i = i + 1` ile `i += 1` aynı şeydir
`a = a / 3` ile `a /= 3` aynı şeydir

---

[Operatörler](docs/scripting/operators.md)      [While Döngüsü](docs/scripting/while.md)      [For Döngüsü](docs/scripting/for.md)      [Fonksiyonlar](docs/scripting/functions.md)      [Ad Kapsamları](docs/scripting/scopes.md)
