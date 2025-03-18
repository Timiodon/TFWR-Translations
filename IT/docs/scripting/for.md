# For Loop
Il ciclo `for` funziona come in Python. (Chiamato un ciclo foreach in alcuni linguaggi, da non confondere con il ciclo for in stile C, che è una cosa diversa).

`for i in sequence:
	#do something with i`

Simile al ciclo `while`, anche il ciclo `for` chiama ripetutamente un blocco di codice. Invece di ciclarlo basandosi su una condizione, esegue il corpo del ciclo una volta per ogni elemento in una sequenza.

## Sintassi
Un ciclo for appare così:

`for variable_name in sequence:
	#code block`

`variable_name` può essere qualsiasi nome tu scelga. È una variabile che memorizza l'elemento corrente nella sequenza. `sequence` deve essere un valore che possa essere iterato come un range o numeri. Il blocco di codice viene eseguito per ogni elemento con la variabile del ciclo assegnata a quell'elemento.

## Sequenze
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Esempio
`for i in range(5):
    harvest()`

Questo ciclo esegue il corpo un numero fisso di volte. È essenzialmente lo stesso che scrivere

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Quindi chiama `harvest()` 5 volte.

Vedi anche [Break](docs/scripting/break.md) e [Continue](docs/scripting/continue.md)