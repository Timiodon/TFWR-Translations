# If
Você pode usar if, elif e else para executar código condicionalmente.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Sintaxe
`if`s permitem que você execute código apenas se alguma condição for `True`. Eles são como um loop `while` que não faz loop.
O `if` recebe uma condição, assim como o loop `while`, e executa o bloco de código do if se a condição for avaliada como `True`:

`#dê uma pirueta se a condição for True
if condition:
	do_a_flip()`

Você também pode adicionar um `else` depois do if que define o código a ser executado se a condição for avaliada como `False`.

Dê uma pirueta se `condition` for True, caso contrário, colha.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` é a abreviação de else if.

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
