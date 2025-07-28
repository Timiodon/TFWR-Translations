# Continue
continue, bir döngünün mevcut yinelemesini durdurmaya ve en içteki döngünün bir sonraki yinelemesine atlamaya olanak tanır.

`for i in range(10):
	continue
    print("bu asla yazdırılmaz")`

Bu, döngünün tüm `10` yinelemesini çalıştırır, ancak `continue`'dan sonraki `print` ifadesi her zaman atlanır.

`while` döngülerinde de çalışır.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Bu kod yalnızca `can_harvest()` `True` olduğunda `harvest()`'ı çağırır. 
Şu kodla aynı etkiye sahiptir:

`while True:
	if can_harvest():
		harvest()`

İç içe döngülerde `continue` her zaman en içteki döngüyü etkiler.

`for i in range(10):
	for j in range(10):
	    print("bu 100 kez yazdırılır")
		continue
		print("bu asla yazdırılmaz")
	print("bu 10 kez yazdırılır")`