# If
Du kannst if, elif und else benutzen, um Code bedingt auszuführen.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntax
`if`s erlauben es dir, Code nur dann auszuführen, wenn eine Bedingung `True` ist. Sie sind wie eine `while`-Schleife, die nicht schleift.
Das `if` nimmt eine Bedingung wie die `while`-Schleife und führt den if-Codeblock aus, wenn die Bedingung zu `True` ausgewertet wird:

`#mache einen Salto, wenn die Bedingung True ist
if condition:
	do_a_flip()`

Du kannst auch ein `else` nach dem if hinzufügen, das Code definiert, der ausgeführt wird, wenn die Bedingung zu `False` ausgewertet wird.

Mache einen Salto, wenn `condition` True ist, andernfalls ernte.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` ist die Abkürzung für else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

kann verkürzt werden zu:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
