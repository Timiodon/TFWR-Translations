# If
Вы можете использовать if, elif и else для условного выполнения кода.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Синтаксис
`if` позволяет вам выполнять код, только если какое-то условие `True`. Это как цикл `while`, который не повторяется.
`if` принимает условие так же, как и цикл `while`, и выполняет блок кода if, если условие вычисляется как `True`:

`#сделать сальто, если условие True
if condition:
	do_a_flip()`

Вы также можете добавить `else` после if, который определяет код для выполнения, если условие вычисляется как `False`.

Сделать сальто, если `condition` равно `True`, иначе собрать урожай.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` — это сокращение от else if.

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