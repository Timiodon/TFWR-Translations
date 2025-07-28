# Funzioni
Usa la parola chiave `def` per definire una nuova funzione:
`def f(arg1, arg2 = False):
	#codice della funzione`

Puoi usare l'operatore di chiamata `()` per chiamare la funzione:
`f(42)`

Vedi anche [Scope](docs/scripting/scopes.md) per imparare sulle variabili locali e globali nelle funzioni.

## Introduzione
Hai già visto funzioni predefinite come `harvest()`.
Puoi anche definire le tue funzioni, il che ti permette di strutturare il tuo codice in modo modulare. Fondamentalmente ti permette di dare un nome a un blocco di codice in modo da poterlo chiamare da dove vuoi.

## Definizioni di Funzione
Ad esempio, potresti definire una funzione che muove il drone più volte.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

La parola chiave `def` segnala che questa è una definizione di funzione.
`move_n_dir` è il nome a cui la funzione viene associata. Può essere qualsiasi nome di variabile valido e sarà usato per chiamare la funzione.
`n` e `dir` sono parametri. Sono variabili che contengono i valori passati alla funzione (questi valori sono anche chiamati argomenti). Puoi aggiungere quanti parametri vuoi a una definizione di funzione.
Dopo i `:` viene il blocco di codice che verrà eseguito quando la funzione viene chiamata.

Con la definizione di cui sopra, il codice seguente sposta quindi il drone di `10` caselle a `Nord` e di `2` caselle a `Ovest`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quando vedi `def function():` dovresti pensarlo come un'assegnazione di variabile come questa:
`function = create_new_function_object()`
Come per tutte le assegnazioni, non puoi usare la variabile prima che sia stata assegnata!
L'istruzione `def` deve essere eseguita prima di qualsiasi chiamata di funzione.
Questo codice genererà un errore:

`func()
def func():
	pass`

## Valori di Ritorno
Usa la parola chiave `return` per fare in modo che una funzione restituisca un valore.
Ad esempio, la seguente funzione definisce l'operazione di or esclusivo. L'or esclusivo restituisce `True` se un valore è `True` e l'altro è `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Le [Tuple](docs/scripting/tuples.md) permettono di restituire più valori.

## Argomenti di Default
Puoi anche assegnare valori predefiniti che verranno utilizzati se non vengono passati argomenti.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argomento che ha un valore predefinito non può essere seguito da un argomento che non ha un valore predefinito.

## Uso Avanzato delle Funzioni
Le funzioni sono valori come qualsiasi altro valore, e l'istruzione `def` agisce semplicemente come un'istruzione di assegnazione, assegnando la funzione a qualsiasi nome tu le dia.
Questo permette di fare cose come questa:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Qui `f()` chiama la funzione `f` che definisce e restituisce una nuova funzione `d`. Il secondo `()` esegue quindi la funzione restituita ed esegue il flip.
(Fare questo tipo di cose di solito non è una buona idea perché è difficile vedere cosa sta succedendo)

Le funzioni che accettano altre funzioni come argomenti ti permettono di essere davvero creativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Questo codice sposta il drone a `Nord` 10 volte e poi usa il fertilizzante 10 volte.