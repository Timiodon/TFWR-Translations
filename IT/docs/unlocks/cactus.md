# Cactus
Come le altre piante, i [cactus](objects/cactus) possono essere coltivati sulla terra e raccolti come al solito.

Tuttavia, esistono in varie dimensioni e hanno uno strano senso dell'ordine.

Se raccogli un cactus completamente cresciuto e tutti i cactus vicini sono in ordine, raccoglierà ricorsivamente anche tutti i cactus vicini.

Un cactus è considerato in ordine se tutti i cactus vicini a `Nord` ed `Est` sono completamente cresciuti e di dimensioni maggiori o uguali, e tutti i cactus vicini a `Sud` e `Ovest` sono completamente cresciuti e di dimensioni minori o uguali.

Il raccolto si propagherà solo se tutti i cactus adiacenti sono completamente cresciuti e in ordine.
Questo significa che se un quadrato di cactus cresciuti è ordinato per dimensione e ne raccogli uno, raccoglierà l'intero quadrato.

Un cactus completamente cresciuto apparirà marrone se non è ordinato. Una volta ordinato, tornerà verde.

Riceverai un numero di cactus pari al quadrato del numero di cactus raccolti. Quindi se raccogli `n` cactus contemporaneamente, riceverai `n**2` `Items.Cactus`.

La dimensione di un cactus può essere misurata con `measure()`.
È sempre uno di questi numeri: `0,1,2,3,4,5,6,7,8,9`.

Puoi anche passare una direzione a `measure(direction)` per misurare la casella vicina in quella direzione del drone.

Puoi scambiare un cactus con il suo vicino in qualsiasi direzione usando il comando `swap()`.
`swap(direction)` scambia l'oggetto sotto il drone con l'oggetto a una casella di distanza nella `direzione` del drone.

## Esempi
In ognuna di queste griglie, tutti i cactus sono in ordine e il raccolto si propagherà su tutto il campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In questa griglia, solo il cactus in basso a sinistra è in ordine, il che non è sufficiente per far propagare il raccolto:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostra suggerimento 1>
Se le righe sono già ordinate, ordinare le colonne non le disordinerà.
</spoiler>
<spoiler=mostra suggerimento 2>
Se non hai familiarità con gli algoritmi di ordinamento, potresti cercarli online e pensare a quali potrebbero essere adattati a questo problema. Tieni presente che non tutti funzionano perché puoi scambiare solo cactus vicini.
</spoiler>