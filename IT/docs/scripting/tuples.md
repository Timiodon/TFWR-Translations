# Tuples
I tuples sono un ottimo modo per combinare più valori in un unico valore.
Per creare un tuple, basta separare i valori con le virgole:

`tuple = 1, 2`

Puoi anche spacchettarli di nuovo in diverse variabili. Nel codice seguente, il tuple `(1,2)` è spacchettato in due variabili `a` e `b`.

`a, b = 1, 2`

I tuples possono essere indicizzati come le liste, ma sono immutabili e non possono essere modificati dopo la creazione.

`tuple = 1, 2`

`print(tuple[1])`
stampa `2`

`tuple[0] = 3`
provoca un error
<unlock=dicts>
A differenza delle liste, i tuples possono essere usati come chiavi nei dictionaries.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`stampa` (4,5)</unlock>

Possono anche essere utili per restituire più valori in una funzione.

`def f():
    return 1, 2

a, b = f()`