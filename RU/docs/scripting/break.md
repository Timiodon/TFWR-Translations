# Break
`break` позволяет завершить цикл раньше. Когда команда `break` встречается, она сразу же выходит из самого внутреннего цикла и начинает выполнять код после цикла.

`for i in range(10):
	break
print(i)`
Это выводит `0`, потому что `i` равно `0` в первой итерации цикла, и затем оператор break завершает цикл.

Он также работает в циклах `while`.

`while True:
	if can_harvest():
		break`

Этот код выполняет цикл `while` до тех пор, пока `can_harvest()` не станет `True`. 
Это имеет тот же эффект, что и

`while not can_harvest():
	pass`

В вложенных циклах `break` всегда выходит из самого внутреннего цикла.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`