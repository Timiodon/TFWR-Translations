# Operátoři
Aritmetické operátory: `+, -, *, /, //, %, **`  
Porovnávací operátory: `==, !=, <=, >=, <, >`  
Logické (booleovské) operátory: `not, and, or`

Poznámka: Všechny číselné hodnoty ve hře jsou typu s plovoucí desetinnou čárkou. To znamená, že všechny aritmetické operace se provádějí v desetinné přesnosti.  
Operátor `//` jednoduše zaokrouhluje výsledek dolů po dělení.

Pro přiřazovací operátory je potřeba odemknout funkci „Variables“.

## Úvod
Operátory umožňují porovnávat, měnit a kombinovat hodnoty.  
Aritmetické operátory `+, -, *, /, //, %, **` provádějí běžné matematické operace s čísly.  
Porovnávací operátory `==, !=, <=, >=, <, >` porovnávají hodnoty. Výsledkem je vždy `True` nebo `False`.  
Logické (booleovské) operátory `not, and, or` se používají pro práci s pravdivostními hodnotami.

## Aritmetické operátory
`+` a `-` se používají pro sčítání a odčítání.

`2 + 3` vyhodnotí jako `5`  
`3 - 2` vyhodnotí jako `1`

`*`, `/` a `//` slouží pro násobení a dělení.

`2 * 3` vyhodnotí jako `6`  
`5 / 2` vyhodnotí jako `2.5`

`//` funguje stejně jako `/`, ale výsledek zaokrouhlí dolů (na celé číslo).

`5 // 2` vyhodnotí jako `2`

`%` je modulo operátor, známý také jako zbytek po dělení. Rozdělí dvě čísla a vrátí zbytek po dělení. Můžeš si to představit i jako opakované odečítání pravého čísla od levého, dokud zbytek není menší než pravé číslo.

`4 % 2` vyhodnotí jako `0`  
`5 % 2` vyhodnotí jako `1`  
`6 % 2` vyhodnotí jako `0`  
`2 % 6` vyhodnotí jako `2`  
`1.5 % 1` vyhodnotí jako `0.5`

`**` je operátor umocnění.

`2**2` vyhodnotí jako `4`  
`(-5)**3` vyhodnotí jako `-125`

## Porovnávací operátory
`==` a `!=` se používají ke kontrole, zda jsou dvě hodnoty „stejné“ (`==`) nebo „různé“ (`!=`). Lze je použít pro všechny typy hodnot.

`2 == 2` vyhodnotí jako `True`  
`Entities.Bush != Entities.Bush` vyhodnotí jako `False`  
`3 != 3 + 1` vyhodnotí jako `True`

`<=, >=, <, >` lze použít pouze na čísla. Kontrolují, zda je levé číslo „menší nebo rovno“ (`<=`), „větší nebo rovno“ (`>=`), „menší“ (`<`) nebo „větší“ (`>`) než pravé číslo.

`1 <= 1` vyhodnotí jako `True`  
`2 >= 3` vyhodnotí jako `False`  
`-2 < -1` vyhodnotí jako `True`  
`6 > 6` vyhodnotí jako `False`

## Logické operátory
`not` jednoduše obrátí hodnotu:

`not False` vyhodnotí jako `True`  
`not True` vyhodnotí jako `False`

`and` vrátí `True` pouze tehdy, pokud jsou obě hodnoty `True`.

`True and True` vyhodnotí jako `True`  
`True and False` vyhodnotí jako `False`  
`False and False` vyhodnotí jako `False`

`or` vrátí `True`, pokud je alespoň jedna z hodnot `True`.

`True or True` vyhodnotí jako `True`  
`True or False` vyhodnotí jako `True`  
`False or False` vyhodnotí jako `False`