# If
Puoi usare if, elif ed else per eseguire codice in modo condizionale.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Sintassi
Gli `if` ti permettono di eseguire codice solo se una certa condizione è `True`. Sono come un ciclo `while` che non cicla.
L'`if` prende una condizione proprio come il ciclo `while` ed esegue il blocco di codice if se la condizione valuta a `True`:

`#fai un flip se la condizione è True
if condition:
	do_a_flip()`

Puoi anche aggiungere un `else` dopo l'if che definisce il codice da eseguire se la condizione valuta a `False`.

Fai un flip se `condition` è True, altrimenti raccogli.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` è l'abbreviazione di else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

può essere abbreviato a:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`