# Tuple
Le tuple sono un ottimo modo per combinare più valori in un unico valore.
Per creare una tupla, basta separare i valori con delle virgole:

`tuple = 1, 2`

Puoi anche spacchettarle di nuovo in più variabili. Nel codice qui sotto, la tupla `(1,2)` viene spacchettata in due variabili `a` e `b`.

`a, b = 1, 2`

Le tuple possono essere indicizzate come le liste, ma sono immutabili e non possono essere modificate dopo la creazione.

`tuple = 1, 2`

`print(tuple[1])`
stampa `2`

`tuple[0] = 3`
genera un errore
<unlock=dicts>
A differenza delle liste, le tuple possono essere usate come chiavi nei dizionari.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`stampa` (4,5)</unlock>

Possono anche essere utili per restituire valori multipli da una funzione.

`def f():
    return 1, 2

a, b = f()`