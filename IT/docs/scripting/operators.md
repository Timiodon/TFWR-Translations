# Operatori
operatori aritmetici: `+, -, *, /, //, %, **`
operatori di confronto: `==, !=, <=, >=, <, >`
operatori booleani: `not, and, or`

Nota: Tutti i numeri nel gioco sono numeri floating point. Quindi tutti gli operatori aritmetici sono operatori floating point.
`//` è definito per arrotondare per difetto il numero dopo la divisione.

Per gli operatori di assegnazione devi sbloccare lo sblocco "Variabili".

## Introduzione
Gli operatori ti permettono di confrontare, modificare e combinare i valori.
Gli operatori aritmetici `+, -, *, /, //, %, **` vengono usati per eseguire operazioni matematiche comuni sui numeri.
Gli operatori di confronto `==, !=, <=, >=, <, >` vengono usati per confrontare i valori. Il risultato è sempre either `True` o `False`.
Gli operatori logici (anche chiamati operatori booleani) `not, and, or` vengono utilizzati per combinare valori di verità.

## Operatori Aritmetici
`+` e `-` vengono usati per l'addizione e la sottrazione.

`2 + 3` ritorna `5`
`3 - 2` ritorna `1`

`*`, `/` e `//` vengono usati per la moltiplicazione e la divisione.

`2 * 3` ritorna `6`
`5 / 2` ritorna `2.5`

`//` fa la stessa operazione di `/` ma il risultato è arrotondato per difetto al numero intero più vicino.

`5 // 2` ritorna `2`

`%` è l'operatore modulo, anche conosciuto come operatore del resto. Divide essenzialmente i due numeri e poi ritorna il resto. Puoi pensarci anche come sottrarre ripetutamente il numero a destra dal numero a sinistra fino a quando il resto è inferiore al numero a destra.

`4 % 2` ritorna `0`
`5 % 2` ritorna `1`
`6 % 2` ritorna `0`
`2 % 6` ritorna `2`
`1.5 % 1` ritorna `0.5`

`**` è l'operatore di potenza.

`2**2` ritorna `4`
`(-5)**3` ritorna `-125`

## Operatori di Confronto
`==` e `!=` vengono usati per verificare se due valori sono "uguali"(`==`) o "non uguali"(`!=`). Possono essere utilizzati su tutti i tipi di valori.

`2 == 2` ritorna `True`
`Entities.Bush != Entities.Bush` ritorna `False`
`3 != 3 + 1` ritorna `True`

`<=, >=, <, >` possono essere utilizzati solo sui numeri. Verificano se il numero a sinistra è "minore o uguale"(`<=`), "maggiore o uguale"(`>=`), "minore" (`<`) o "maggiore" (`>`) del numero a destra.

`1 <= 1` ritorna `True`
`2 >= 3` ritorna `False`
`-2 < -1` ritorna `True`
`6 > 6` ritorna `False`

## Operatori Logici
`not` inverte semplicemente il valore:

`not False` ritorna `True`
`not True` ritorna `False`

`and` ritorna `True` solo se entrambi i valori sono `True`

`True and True` ritorna `True`
`True and False` ritorna `False`
`False and False` ritorna `False`

`or` ritorna `True` se almeno uno dei valori è `True`

`True or True` ritorna `True`
`True or False` ritorna `True`
`False or False` ritorna `False`