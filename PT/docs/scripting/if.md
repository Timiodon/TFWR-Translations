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
`if` permite que você execute código apenas se alguma condição for `True`. Eles são como um loop `while` que não repete.
O `if` recebe uma condição assim como o loop `while` e executa o bloco de código if se a condição for avaliada como `True`:

`#faça um flip se a condição for True
if condition:
	do_a_flip()`

Você também pode adicionar um `else` após o if que define o código a ser executado se a condição for avaliada como `False`.

Faça um flip se `condition` for True, caso contrário, colha.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` é a forma curta de else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

pode ser encurtado para:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`