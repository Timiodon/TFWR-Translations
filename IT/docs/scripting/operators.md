# Operatori
operatori aritmetici: `+, -, *, /, //, %, **`
operatori di confronto: `==, !=, <=, >=, <, >`
operatori booleani: `not, and, or`

Nota: Tutti i numeri nel gioco sono numeri in virgola mobile. Quindi tutti gli operatori aritmetici sono operatori in virgola mobile.
`//` è definito per arrotondare per difetto il numero dopo la divisione.

Per gli operatori di assegnazione è necessario sbloccare lo sblocco "Variabili".

## Introduzione
Gli operatori ti permettono di confrontare, modificare e combinare valori.
Gli operatori aritmetici `+, -, *, /, //, %, **` sono usati per eseguire operazioni matematiche comuni sui numeri.
Gli operatori di confronto `==, !=, <=, >=, <, >` sono usati per confrontare valori. Il risultato è sempre `True` o `False`.
Gli operatori logici (chiamati anche operatori booleani) `not, and, or` sono usati per combinare valori di verità.

## Operatori Aritmetici
`+` e `-` sono usati per l'addizione e la sottrazione.

`2 + 3` restituisce `5`
`3 - 2` restituisce `1`

`*`, `/` e `//` sono usati per la moltiplicazione e la divisione.

`2 * 3` restituisce `6`
`5 / 2` restituisce `2.5`

`//` fa la stessa cosa di `/` ma il risultato viene arrotondato per difetto (all'intero successivo).

`5 // 2` restituisce `2`

`%` è l'operatore modulo, noto anche come operatore del resto. Essenzialmente divide i due numeri e poi restituisce il resto. Puoi anche pensarlo come la sottrazione ripetuta del numero di destra dal numero di sinistra finché il resto non è minore del numero di destra.

`4 % 2` restituisce `0`
`5 % 2` restituisce `1`
`6 % 2` restituisce `0`
`2 % 6` restituisce `2`
`1.5 % 1` restituisce `0.5`

`**` è l'operatore di potenza.

`2**2` restituisce `4`
`(-5)**3` restituisce `-125`

## Operatori di Confronto
`==` e `!=` sono usati per verificare se due valori sono "uguali" (`==`) o "non uguali" (`!=`). Possono essere usati su tutti i tipi di valori.

`2 == 2` restituisce `True`
`Entities.Bush != Entities.Bush` restituisce `False`
`3 != 3 + 1` restituisce `True`

`<=, >=, <, >` possono essere usati solo sui numeri. Verificano se il numero di sinistra è "minore o uguale" (`<=`), "maggiore o uguale" (`>=`), "minore" (`<`) o "maggiore" (`>`) del numero di destra.

`1 <= 1` restituisce `True`
`2 >= 3` restituisce `False`
`-2 < -1` restituisce `True`
`6 > 6` restituisce `False`

## Operatori Logici
`not` inverte semplicemente il valore:

`not False` restituisce `True`
`not True` restituisce `False`

`and` restituisce `True` solo se entrambi i valori sono `True`

`True and True` restituisce `True`
`True and False` restituisce `False`
`False and False` restituisce `False`

`or` restituisce `True` se almeno uno dei valori è `True`

`True or True` restituisce `True`
`True or False` restituisce `True`
`False or False` restituisce `False`