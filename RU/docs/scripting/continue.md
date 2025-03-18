# Continue
continue позволяет остановить текущую итерацию цикла и перейти к следующей итерации самого внутреннего цикла.

`for i in range(10):
	continue
    print("this is never printed")`

Этот код выполняет все `10` итераций цикла, но оператор `print` после `continue` всегда пропускается.

Он также работает с циклами `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Этот код вызывает `harvest()` только когда `can_harvest()` равно `True`. 
Это имеет такой же эффект, как и

`while True:
	if can_harvest():
		harvest()`

Вложенные циклы `continue` всегда влияют на самый внутренний цикл.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`