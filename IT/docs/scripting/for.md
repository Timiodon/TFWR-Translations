# Ciclo For
Il ciclo `for` funziona come in Python. (Chiamato ciclo foreach in alcuni linguaggi, da non confondere con il ciclo for in stile C, che è una cosa diversa).

`for i in sequence:
	#fai qualcosa con i`

Simile al ciclo `while`, anche il ciclo `for` chiama ripetutamente un blocco di codice. Invece di ciclare in base a una condizione, esegue il corpo del ciclo una volta per ogni elemento in una sequenza.

## Sintassi
Un ciclo for si presenta così:

`for nome_variabile in sequenza:
	#blocco di codice`

`nome_variabile` può essere qualsiasi nome tu scelga. È una variabile che memorizza l'elemento corrente nella sequenza. `sequenza` deve essere un valore che può essere iterato come un range o dei numeri. Il blocco di codice viene eseguito per ogni elemento con la variabile del ciclo assegnata a quell'elemento.

## Sequenze
[Range](functions/range)      <unlock=lists>[Liste](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuple](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dizionari](docs/scripting/dicts.md)      </unlock><unlock=sets>[Set](docs/scripting/sets.md)</unlock>

## Esempio
`for i in range(5):
    harvest()`

Questo ciclo esegue il corpo un numero fisso di volte. È essenzialmente la stessa cosa di scrivere

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