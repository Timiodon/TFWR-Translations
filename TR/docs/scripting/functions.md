[<- Değişkenler](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)
---
# Fonksiyonlar
Yeni bir fonksiyon tanımlamak için `def` anahtar kelimesini kullan:
`def f(arg1, arg2 = False):
	#function code`

Fonksiyonu çağırmak için çağırma operatörü `()` kullanılır:
`f(42)`

Fonksiyonlardaki yerel ve global değişkenler hakkında bilgi almak için [Kapsamlar](docs/scripting/scopes.md) sayfasına da göz at.

## Giriş
`harvest()` gibi yerleşik fonksiyonları zaten gördün.
Kendi fonksiyonlarını da tanımlayabilirsin; bu sayede kodunu modüler bir şekilde düzenleyebilirsin. Bir fonksiyon, bir kod bloğuna bir ad verir; böylece onu ihtiyaç duyduğun her yerde çağırabilirsin.

## Fonksiyon Tanımları
Örneğin, dronu birkaç kez hareket ettiren bir fonksiyon tanımlayabilirsin.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

`def` anahtar kelimesi bunun bir fonksiyon tanımı olduğunu belirtir. 
`move_n_dir`, fonksiyonun bağlandığı addır. Bu, geçerli herhangi bir değişken adı olabilir ve fonksiyonu çağırmak için kullanılır.
`n` ve `dir` parametrelerdir. Bunlar, fonksiyona aktarılan değerleri tutan değişkenlerdir; bu değerlere argüman da denir. Bir fonksiyon tanımına istediğin kadar parametre ekleyebilirsin.
`:` işaretinden sonra, fonksiyon çağrıldığında çalışacak kod bloğu gelir.

Ardından aşağıdaki kod dronu `2` kare `North` (kuzey) ve `2` kare `East` (doğu) yönünde hareket ettirir.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

`def function():` gördüğünde, bunu aslında şöyle bir değişken ataması gibi düşünmelisin:
`function = create_new_function_object()`
Tüm atamalarda olduğu gibi, değişkeni atanmadan önce kullanamazsın!
`def` ifadesi, fonksiyon çağrılarından önce çalışmalıdır.
Bu kod hata verir:

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
func()
def func():
	pass
}}

## Dönüş Değerleri
Bir fonksiyonun değer döndürmesini sağlamak için `return` anahtar kelimesini kullan. 
Örneğin, aşağıdaki fonksiyon "özel veya" (exclusive OR) işlemini tanımlar. Özel veya, değerlerden biri `True` ve diğeri `False` ise `True` döndürür:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[Tuple'lar](docs/scripting/tuples.md) birden fazla değer döndürmeye olanak tanır.

## Varsayılan Argümanlar
İlgili argümanlar verilmediğinde kullanılacak varsayılan değerler de atayabilirsin.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Varsayılan değeri olan bir argümandan sonra, varsayılan değeri olmayan bir argüman gelemez.

## İleri Düzey Fonksiyon Kullanımı
Fonksiyonlar da diğer tüm değerler gibi birer değerdir ve `def` ifadesi aslında bir atama ifadesi gibi davranır; fonksiyonu ona verdiğin ada atar.
Bu sayede şöyle şeyler yapabilirsin:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Burada `f()`, yeni bir `d` fonksiyonu tanımlayıp döndüren `f` fonksiyonunu çağırır. İkinci `()` ise döndürülen fonksiyonu çalıştırır ve takla attırır.
(Bu tür şeyler yapmak genellikle iyi bir fikir değildir, çünkü neler olup bittiğini anlamak zorlaşır.)

Başka fonksiyonları argüman olarak alan fonksiyonlarla gerçekten yaratıcı olabilirsin:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Değişkenler](docs/scripting/variables.md)      [Ad Kapsamları](docs/scripting/scopes.md)      [Tuple'lar](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
