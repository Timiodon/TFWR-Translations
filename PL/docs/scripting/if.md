# If
Możesz używać if, elif oraz else, aby wykonywać kod warunkowo.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Składnia
`if` pozwala uruchomić kod tylko wtedy, gdy warunek jest `True`. Działa jak pętla `while`, tyle że nie pętli się.
`if` przyjmuje warunek podobnie jak `while` i wykonuje blok kodu if, jeśli warunek zostanie oceniony jako `True`:

`#zrób fikołka, jeśli warunek jest True
if condition:
	do_a_flip()`

Możesz również dodać `else` po if, który określa kod do wykonania, jeśli warunek zostanie oceniony jako `False`.

Zrób fikołka, jeśli `condition` jest True, w przeciwnym razie zbierz plony.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` to skrót od else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

można skrócić do:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`