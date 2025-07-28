# Break
`break`, bir döngüyü erken durdurmaya olanak tanır. `break` ifadesine ulaşıldığında, hemen en içteki döngüden çıkar ve döngüden sonraki kodu çalıştırmaya başlar.

`for i in range(10):
	break
print(i)`
Bu, `0` yazdırır çünkü `i`, döngünün ilk yinelemesinde `0`'dır ve ardından break ifadesi döngüyü sonlandırır.

`while` döngülerinde de çalışır.

`while True:
	if can_harvest():
		break`

Bu kod, `can_harvest()` `True` olana kadar `while` döngüsünü çalıştırır. 
Şu kodla aynı etkiye sahiptir:

`while not can_harvest():
	pass`

İç içe döngülerde `break` her zaman en içteki döngüden çıkar.

`for i in range(10):
	for j in range(10):
		break
		print("bu asla yazdırılmaz")
	print("bu 10 kez yazdırılır")`