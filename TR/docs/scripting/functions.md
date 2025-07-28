# Fonksiyonlar
Yeni bir fonksiyon tanımlamak için `def` anahtar kelimesini kullan:
`def f(arg1, arg2 = False):
	#fonksiyon kodu`

Fonksiyonu çağırmak için `()` çağrı operatörünü kullanabilirsin:
`f(42)`

Fonksiyonlardaki yerel ve global değişkenler hakkında bilgi edinmek için ayrıca [Kapsamlar](docs/scripting/scopes.md)'a bak.

## Giriş
`harvest()` gibi yerleşik fonksiyonları zaten gördün.
Kodunu modüler bir şekilde yapılandırmanı sağlayan kendi fonksiyonlarını da tanımlayabilirsin. Temel olarak, bir kod bloğuna bir isim vermeni sağlar, böylece onu istediğin yerden çağırabilirsin.

## Fonksiyon Tanımları
Örneğin, drone'u birkaç kez hareket ettiren bir fonksiyon tanımlayabilirsin.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` anahtar kelimesi bunun bir fonksiyon tanımı olduğunu belirtir. 
`move_n_dir`, fonksiyonun bağlandığı isimdir. Bu, herhangi bir geçerli değişken adı olabilir ve fonksiyonu çağırmak için kullanılacaktır.
`n` ve `dir` parametrelerdir. Bunlar, fonksiyona geçirilen değerleri tutan değişkenlerdir (Bu değerlere argüman da denir). Bir fonksiyon tanımına istediğin kadar parametre ekleyebilirsin.
`:` işaretinden sonra, fonksiyon çağrıldığında çalışacak olan kod bloğu gelir.

Yukarıdaki tanımla, aşağıdaki kod drone'u `10` kare `North` ve `2` kare `West` hareket ettirir.

`move_n_dir(10, North)
move_n_dir(2, West)`

`def function():` gördüğünde, bunu gerçekten şöyle bir değişken ataması olarak düşünmelisin:
`function = create_new_function_object()`
Tüm atamalarda olduğu gibi, değişkeni atanmadan önce kullanamazsın!
`def` ifadesi, herhangi bir fonksiyon çağrısından önce çalışmalıdır.
Bu kod bir error verir:

`func()
def func():
	pass`

## Dönüş Değerleri
Bir fonksiyonun bir değer döndürmesini sağlamak için `return` anahtar kelimesini kullan. 
Örneğin, aşağıdaki fonksiyon özel veya işlemini tanımlar. Özel veya, bir değer `True` ve diğeri `False` ise `True` döndürür:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuple'lar](docs/scripting/tuples.md) birden fazla değer döndürmeye izin verir.

## Varsayılan Argümanlar
Argüman geçilmediğinde kullanılacak varsayılan değerler de atayabilirsin.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Varsayılan değeri olan bir argümanı, varsayılan değeri olmayan bir argüman takip edemez.

## İleri Düzey Fonksiyon Kullanımı
Fonksiyonlar, diğer herhangi bir değer gibi değerlerdir ve `def` ifadesi, fonksiyonu verdiğin herhangi bir isme atayan bir atama ifadesi gibi davranır.
Bu, bunun gibi şeyler yapmaya izin verir:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Burada `f()`, `f` fonksiyonunu çağırır, bu da yeni bir `d` fonksiyonu tanımlar ve döndürür. İkinci `()` daha sonra döndürülen fonksiyonu yürütür ve takla atar.
(Bu tür şeyler yapmak genellikle iyi bir fikir değildir çünkü ne olup bittiğini görmek zordur)

Argüman olarak başka fonksiyonlar alan fonksiyonlar, gerçekten yaratıcı olmanı sağlar:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Bu kod, drone'u 10 kez `North` yönüne hareket ettirir ve ardından 10 kez gübre kullanır.