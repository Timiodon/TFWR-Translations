# Continue
continue, bir döngünün mevcut iterasyonunu durdurup en içteki döngünün bir sonraki iterasyonuna geçmeyi sağlar.

`for i in range(10):
	continue
    print("this is never printed")`

Bu, döngünün tüm `10` iterasyonunu çalıştırır, ancak `continue` sonrasındaki `print` ifadesi her zaman atlanır.

Ayrıca `while` döngülerinde de çalışır.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Bu kod, yalnızca `can_harvest()` `True` olduğunda `harvest()` fonksiyonunu çağırır.
Bu, şu kodla aynı etkiye sahiptir:

`while True:
	if can_harvest():
		harvest()`

İç içe döngülerde, `continue` daima en içteki döngüyü etkiler.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`