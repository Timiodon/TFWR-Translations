# Funzioni
Usa la parola chiave `def` per definire una nuova funzione:
`def f(arg1, arg2 = False):
	#codice della funzione`

Puoi usare l'operatore di chiamata `()` per chiamare la funzione:
`f(42)`

Vedi anche [Scope](docs/scripting/scopes.md) per imparare le variabili locali e globali nelle funzioni.

## Introduzione
Hai già visto funzioni integrate come `harvest()`.
Puoi anche definire le tue funzioni, il che permette di strutturare il codice in modo modulare. In pratica, ti consente di dare un nome a un blocco di codice in modo da poterlo chiamare da dove vuoi.

## Definizioni di Funzioni
Ad esempio, potresti definire una funzione che muove il drone più volte.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

La parola chiave `def` segnala che questa è una definizione di funzione.
`move_n_dir` è il nome a cui la funzione viene associata. Può essere qualsiasi nome di variabile valido e sarà usato per chiamare la funzione.
`n` e `dir` sono parametri. Sono variabili che contengono i valori passati alla funzione (questi valori sono anche chiamati argomenti). Puoi aggiungere quanti parametri vuoi a una definizione di funzione.
Dopo i `:` viene il blocco di codice che verrà eseguito quando la funzione viene chiamata.

Con la definizione sopra, il seguente codice sposta il drone di `10` caselle a `North` e di `2` caselle a `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quando vedi `def function():`, dovresti pensarci come a un'assegnazione di variabile del tipo:
`function = create_new_function_object()`
Come per tutte le assegnazioni, non puoi usare la variabile prima che sia stata assegnata! L'istruzione `def` deve essere eseguita prima di qualsiasi chiamata alla funzione.
Questo codice genererà un errore:

`func()
def func():
	pass`

## Valori di Ritorno
Usa la parola chiave `return` per far sì che una funzione restituisca un valore.
Ad esempio, la seguente funzione definisce l'operazione di OR esclusivo. L'OR esclusivo restituisce `True` se un valore è `True` e l'altro è `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Le [Tuple](docs/scripting/tuples.md) permettono di restituire più valori.

## Argomenti Predefiniti
Puoi anche assegnare valori predefiniti che verranno usati se non vengono passati argomenti.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argomento con un valore predefinito non può essere seguito da un argomento che non ha un valore predefinito.

## Uso Avanzato delle Funzioni
Le funzioni sono valori come qualsiasi altro valore, e l'istruzione `def` agisce semplicemente come un'istruzione di assegnazione, assegnando la funzione al nome che le dai.
Questo permette di fare cose come questa:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Qui `f()` chiama la funzione `f` che definisce e restituisce una nuova funzione `d`. Il secondo `()` esegue quindi la funzione restituita ed esegue un flip.
(Fare questo tipo di cose di solito non è una buona idea perché è difficile capire cosa sta succedendo)

Le funzioni che prendono altre funzioni come argomenti ti permettono di essere molto creativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Questo codice muove il drone `North` 10 volte e poi usa il fertilizzante 10 volte.