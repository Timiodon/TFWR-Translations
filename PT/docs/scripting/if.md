# If
Podes usar if, elif e else para executar código condicionalmente.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Sintaxe
Os `if`s permitem-te executar código apenas se alguma condição for `True`. São como um loop `while` que não faz loop.
O `if` recebe uma condição tal como o loop `while` e executa o bloco de código do if se a condição avaliar para `True`:

`#faz um pino se a condição for True
if condition:
	do_a_flip()`

Também podes adicionar um `else` depois do if que define o código a ser executado se a condição avaliar para `False`.

Faz um pino se a `condition` for True, caso contrário, colhe.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` é uma abreviatura para else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

pode ser abreviado para:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
