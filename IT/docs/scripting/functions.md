# Funzioni
Usa la parola chiave `def` per definire una nuova funzione:
`def f(arg1, arg2 = False):
	#codice della funzione`

Puoi usare l'operatore di chiamata `()` per chiamare la funzione:
`f(42)`

Consulta anche [Scope](docs/scripting/scopes.md) per saperne di più sulle variabili locali e globali nelle funzioni.

## Introduzione
Hai già visto funzioni integrate come `harvest()`.
Puoi anche definire le tue funzioni, il che ti consente di strutturare il tuo codice in modo modulare. In pratica, ti permette di dare un nome a un blocco di codice in modo da poterlo chiamare da qualsiasi parte tu voglia.

## Definizioni di Funzione
Per esempio, potresti definire una funzione che sposta il drone più volte.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

La parola chiave `def` indica che questa è una definizione di funzione. 
`move_n_dir` è il nome assegnato alla funzione. Questo può essere qualsiasi nome di variabile valido e verrà utilizzato per chiamare la funzione.
`n` e `dir` sono parametri. Sono variabili che contengono i valori passati alla funzione (questi valori vengono anche chiamati argomenti). Puoi aggiungere quanti parametri vuoi a una definizione di funzione.
Dopo il `:` segue il blocco di codice che verrà eseguito quando la funzione verrà chiamata.

Con la definizione precedente, il seguente codice sposta il drone di `10` celle verso `North` e di `2` celle verso `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quando vedi `def function():` dovresti pensarlo come un'assegnazione di variabile, come:
`function = create_new_function_object()`
Come per tutte le assegnazioni, non puoi usare la variabile prima che sia stata assegnata!
Il comando `def` deve essere eseguito prima di qualsiasi chiamata di funzione.
Questo codice restituirà un errore:

`func()
def func():
	pass`

## Valori di Ritorno
Usa la parola chiave `return` per far restituire un valore a una funzione. 
Ad esempio, la seguente funzione definisce l'operazione di esclusione o. L'esclusione o restituisce `True` se un valore è `True` e l'altro è `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

I [Tuples](docs/scripting/tuples.md) permettono di restituire più valori.

## Argomenti di Default
Puoi anche assegnare valori di default che verranno usati se non vengono passati argomenti.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argomento che ha un valore di default non può essere seguito da un argomento che non ha un valore di default.

## Uso Avanzato delle Funzioni
Le funzioni sono valori proprio come qualsiasi altro valore, e l'istruzione `def` funziona come un'istruzione di assegnazione, assegnando la funzione al nome che gli dai.
Questo permette di fare cose come:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Qui `f()` chiama la funzione `f` che definisce e restituisce una nuova funzione `d`. Il secondo `()` quindi esegue la funzione restituita ed esegue il flip.
(Fare queste cose di solito non è una buona idea perché è difficile capire cosa sta succedendo)

Le funzioni che prendono altre funzioni come argomenti ti permettono di essere davvero creativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Questo codice muove il drone `North` 10 volte e poi utilizza il fertilizzante 10 volte.