# If
Ты можешь использовать if, elif и else, чтобы задать условия выполнения кода.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Синтаксис
`if` позволяет выполнять код, только если какое-то условие равно `True`. Похоже на цикл `while`, только не повторяется.
`if` принимает условие так же, как и цикл `while`, и выполняет блок кода `if`, если условие равно `True`:

`#сделать сальто, если условие True
if condition:
	do_a_flip()`

Ты можешь добавить `else` после if. Эта инструкция определяет код, выполняющийся при условии, равном `False`.

Сделать сальто, если `condition` равно `True`, иначе — собрать урожай.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` — это сокращение от else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

Можно сократить до:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
