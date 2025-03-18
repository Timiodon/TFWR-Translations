# If
Du kannst if, elif und else verwenden, um Code bedingt auszuführen.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntax
`if` erlaubt es dir, Code nur dann auszuführen, wenn eine Bedingung `True` ist. Sie sind wie ein `while`-Loop, der nicht wiederholt.
Der `if` nimmt eine Bedingung genau wie der `while`-Loop und führt den if-Codeblock aus, wenn die Bedingung zu `True` ausgewertet wird:

`#do a flip if condition is True
if condition:
	do_a_flip()`

Du kannst auch ein `else` nach dem if hinzufügen, das den Code definiert, der ausgeführt wird, wenn die Bedingung zu `False` ausgewertet wird.

Mach einen Salto, wenn `condition` True ist, sonst ernte.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` ist die Kurzform für else if.

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