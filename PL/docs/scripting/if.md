# If
Możesz używać if, elif i else, aby uruchamiać kod warunkowo.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Składnia
Instrukcje `if` pozwalają na uruchomienie kodu tylko wtedy, gdy jakiś warunek jest `True`. Są jak pętla `while`, która się nie zapętla.
`if` przyjmuje warunek, tak jak pętla `while`, i wykonuje blok kodu `if`, jeśli warunek jest `True`:

`#wykonaj obrót, jeśli warunek jest True
if condition:
	do_a_flip()`

Możesz także dodać `else` po `if`, które definiuje kod do wykonania, jeśli warunek jest `False`.

Wykonaj obrót, jeśli `condition` jest `True`, w przeciwnym razie zbierz plon.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` to skrót od else if (w przeciwnym razie, jeśli).

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