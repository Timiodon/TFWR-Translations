# Break
`break`, bir döngüyü erken durdurmanı sağlar. `break` ifadesine ulaşıldığında hemen en içteki döngüden çıkılır ve döngüden sonraki kod çalıştırılmaya başlar.

`for i in range(10):
	break
print(i)`
Bu, `0`'ı yazdırır çünkü döngünün ilk iterasyonunda `i` `0`'dır ve ardından break ifadesi döngüyü sonlandırır.

Bu ifade `while` döngülerinde de çalışır.

`while True:
	if can_harvest():
		break`

Bu kod, `can_harvest()` `True` olana kadar `while` döngüsünü çalıştırır.
Aynı etkiye sahiptir:

`while not can_harvest():
	pass`

İç içe geçmiş döngülerde, `break` her zaman en içteki döngüden çıkar.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`