# Cactus
Come altre piante, i [cactus](objects/cactus) possono essere coltivati sulla terra e raccolti normalmente.

Tuttavia, esistono in varie dimensioni e hanno uno strano senso dell'ordine.

Se raccogli un cactus completamente cresciuto e tutti i cactus vicini sono in ordine, raccoglierà anche tutti i cactus vicini ricorsivamente.

Un cactus è considerato in ordine se tutti i cactus vicini a `Nord` e `Est` sono completamente cresciuti e di dimensioni maggiori o uguali e tutti i cactus vicini a `Sud` e `Ovest` sono completamente cresciuti e di dimensioni minori o uguali.

Il raccolto si estenderà solo se tutti i cactus adiacenti sono completamente cresciuti e in ordine.
Questo significa che se un quadrato di cactus cresciuti è ordinato per dimensione e ne raccogli uno, verrà raccolto l'intero quadrato.

Riceverai un numero di cactus pari al quadrato del numero di cactus raccolti. Quindi, se raccogli `n` cactus contemporaneamente, riceverai `n**2` `Items.Cactus`.

La dimensione di un cactus può essere misurata con `measure()`.
È sempre uno di questi numeri: `0,1,2,3,4,5,6,7,8,9`.

Puoi anche passare una direzione in `measure(direction)` per misurare la tessera vicina in quella direzione dal drone.

Puoi scambiare un cactus con il suo vicino in qualsiasi direzione usando il comando `swap()`.
`swap(direction)` scambia l'oggetto sotto il drone con l'oggetto a una tessera nella `direzione` del drone.

## Esempi
In ognuna di queste griglie, tutti i cactus sono in ordine e il raccolto si diffonderà su tutto il campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In questa griglia, solo il cactus in basso a sinistra è in ordine, il che non è sufficiente perché si diffonda:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostra suggerimento 1>
Se ogni colonna e ogni riga del campo è ordinata, allora l'intero campo è ordinato.
</spoiler>
<spoiler=mostra suggerimento 2>
Se non sei familiare con gli algoritmi di ordinamento, potresti volerli cercare online e pensare a quali potrebbero essere adattati a questo problema.
</spoiler>