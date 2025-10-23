# If
Můžeš použít `if`, `elif` a `else` pro podmíněné spouštění kódu.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntaxe
`if` umožňuje spustit kód pouze tehdy, pokud je určitá podmínka `True`. Je to podobné jako smyčka `while`, která se ale neopakuje.
Příkaz `if` bere podmínku stejně jako smyčka `while` a provede blok kódu pouze tehdy, když se podmínka vyhodnotí jako `True`:

`#udělej otočku, pokud je podmínka True
if condition:
	do_a_flip()`

K příkazu `if` můžeš také přidat část `else`, která určuje, co se má provést, pokud se podmínka vyhodnotí jako `False`.

Udělej otočku, pokud je `condition` True, jinak sklízej.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` je zkratka pro **else if**.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

Lze zkrátit na:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
