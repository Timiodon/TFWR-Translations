# Fonksiyonlar
Yeni bir fonksiyon tanımlamak için `def` anahtar kelimesini kullan:
`def f(arg1, arg2 = False):
	#fonksiyon kodu`

Fonksiyonu çağırmak için çağrı operatörünü `()` kullanabilirsin:
`f(42)`

Fonksiyonlardaki yerel ve küresel değişkenler hakkında bilgi edinmek için [Scopes](docs/scripting/scopes.md) kısmına da göz at.

## Giriş
`harvest()` gibi yerleşik fonksiyonları zaten gördün. Kendi fonksiyonlarını da tanımlayabilirsin, bu da kodunu modüler bir şekilde yapılandırmana olanak tanır. Temelde, kod bloğuna bir isim verir ve istediğin yerden çağırmanı sağlar.

## Fonksiyon Tanımları
Örneğin, drone'u birkaç kez hareket ettiren bir fonksiyon tanımlayabilirsin.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` anahtar kelimesi bunun bir fonksiyon tanımı olduğunu belirtir.
`move_n_dir` fonksiyonun bağlı olduğu isimdir. Bu, herhangi bir geçerli değişken ismi olabilir ve fonksiyonu çağırmak için kullanılır.
`n` ve `dir` parametrelerdir. Bu değişkenler, fonksiyona aktarılan değerleri tutar (Bu değerlere argüman da denir). Bir fonksiyon tanımına istediğin kadar parametre ekleyebilirsin.
`:`'dan sonra, fonksiyon çağrıldığında çalışacak olan kod bloğu gelir.

Yukarıdaki tanımla, bu kod drone'u `10` kare `North` ve `2` kare `West` hareket ettirir.

`move_n_dir(10, North)
move_n_dir(2, West)`

`def function():` gördüğünde bunu şöyle bir değişken ataması gibi düşünmelisin:
`function = create_new_function_object()`
Tüm atamalarda olduğu gibi, atanmadıkça değişkeni kullanamazsın!
`def` ifadesi, herhangi bir fonksiyon çağrısından önce çalıştırılmalıdır.
Bu kod bir hata verecektir:

`func()
def func():
	pass`

## Geri Dönüş Değerleri
Bir fonksiyonun bir değer döndürmesini sağlamak için `return` anahtar kelimesini kullan. Örneğin, aşağıdaki fonksiyon özel veya işlemini tanımlar. Özel veya, bir değer `True` ve diğeri `False` olduğunda `True` döndürür:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) birden fazla değer döndürmeyi sağlar.

## Varsayılan Argümanlar
Geçerli bir argüman verilmezse kullanılacak varsayılan değerler de atayabilirsin.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Varsayılan değere sahip bir argümanın ardından varsayılan değeri olmayan bir argüman gelemez.

## Gelişmiş Fonksiyon Kullanımı
Fonksiyonlar, tıpkı diğer değerler gibi değerlendirilebilir ve `def` ifadesi, fonksiyonu verdiğin isime atayan bir atama ifadesi gibi davranır.
Bu durum, aşağıdaki gibi şeyler yapmayı mümkün kılar:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Burada `f()`, yeni bir `d` fonksiyonu tanımlayıp döndüren `f` fonksiyonunu çağırır. İkinci `()` daha sonra döndürülen fonksiyonu çalıştırır ve flip gerçekleştirir.
(Bu tür şeyleri yapmak genellikle iyi bir fikir değildir çünkü ne olduğunu görmek zor olabilir)

Diğer fonksiyonları argüman olarak alan fonksiyonlar, gerçekten yaratıcı olmanı sağlar:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Bu kod drone'u `North` yönünde 10 kez hareket ettirir ve ardından 10 kez gübre kullanır.