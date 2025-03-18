# If
Вы можете использовать if, elif и else, чтобы выполнять код при определенных условиях.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Синтаксис
`if` позволяет выполнять код только в том случае, если условие `True`. Они похожи на цикл `while`, который не зацикливается.
`if` принимает условие аналогично циклу `while` и выполняет блок кода if, если условие оценивается как `True`:

`#выполнить переворот, если условие истинно
if condition:
	do_a_flip()`

Вы также можете добавить `else` после if, чтобы определить код для выполнения, если условие оценивается как `False`.

Выполните переворот, если `condition` истинно, иначе соберите урожай.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` это сокращение от else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

можно сократить до:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`