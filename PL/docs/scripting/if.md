# If
Możesz użyć if, elif i else, aby uruchomić kod warunkowo.

`if warunek1:
	do_a_flip()
elif warunek2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Składnia
Instrukcje `if` pozwalają uruchomić kod tylko wtedy, gdy jakiś warunek jest `True`. Są jak pętla `while`, która się nie zapętla.
`if` przyjmuje warunek, tak jak pętla `while`, i wykonuje blok kodu `if`, jeśli warunek jest `True`:

`#zrób fikołka, jeśli warunek jest True
if condition:
	do_a_flip()`

Możesz także dodać `else` po `if`, które definiuje kod do wykonania, jeśli warunek jest `False`.

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
