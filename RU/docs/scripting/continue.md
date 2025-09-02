# Continue
`continue` позволяет остановить текущую итерацию цикла и перейти к следующей итерации самого внутреннего цикла.

`for i in range(10):
	continue
    print("это никогда не будет напечатано")`

Этот код выполняет все `10` итераций цикла, но инструкция `print` после `continue` всегда пропускается.

Это также работает с циклами `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Этот код вызывает `harvest()` только тогда, когда `can_harvest()` `True`. 
Он имеет тот же эффект, что и

`while True:
	if can_harvest():
		harvest()`

Во вложенных циклах `continue` всегда влияет на самый внутренний цикл.

`for i in range(10):
	for j in range(10):
	    print("это напечатается 100 раз")
		continue
		print("это никогда не будет напечатано")
	print("это напечатается 10 раз")`