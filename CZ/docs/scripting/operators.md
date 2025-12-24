# Operátory
aritmetické operátory: `+, -, *, /, //, %, **`
porovnávací operátory: `==, !=, <=, >=, <, >`
booleovské operátory: `not, and, or`

Poznámka: Všechna čísla ve hře jsou čísla s plovoucí desetinnou čárkou. Takže všechny aritmetické operátory jsou operátory s plovoucí desetinnou čárkou.
`//` je definováno tak, že po dělení číslo zaokrouhlí dolů.

Pro operátory přiřazení musíte odemknout vylepšení "Proměnné".

## Úvod
Operátory umožňují porovnávat, upravovat a kombinovat hodnoty. 
Aritmetické operátory `+, -, *, /, //, %, **` se používají k provádění běžných matematických operací s čísly. 
Porovnávací operátory `==, !=, <=, >=, <, >` se používají k porovnávání hodnot. Výsledek je vždy buď `True` (pravda) nebo `False` (nepravda).
Logické operátory (také nazývané booleovské operátory) `not, and, or` se používají ke kombinování pravdivostních hodnot.

## Aritmetické operátory
`+` a `-` se používají pro sčítání a odčítání.

`2 + 3` se vyhodnotí jako `5`
`3 - 2` se vyhodnotí jako `1`

`*`, `/` a `//` se používají pro násobení a dělení.

`2 * 3` se vyhodnotí jako `6`
`5 / 2` se vyhodnotí jako `2.5`

`//` dělá totéž co `/`, ale výsledek je zaokrouhlen dolů (na nejbližší nižší celé číslo).

`5 // 2` se vyhodnotí jako `2`

`%` je operátor modulo, známý také jako operátor zbytku. V podstatě vydělí dvě čísla a poté vrátí zbytek. Můžete si to také představit jako opakované odečítání pravého čísla od levého, dokud není zbytek menší než pravé číslo.

`4 % 2` se vyhodnotí jako `0`
`5 % 2` se vyhodnotí jako `1`
`6 % 2` se vyhodnotí jako `0`
`2 % 6` se vyhodnotí jako `2`
`1.5 % 1` se vyhodnotí jako `0.5`

`**` je operátor mocnění.

`2**2` se vyhodnotí jako `4`
`(-5)**3` se vyhodnotí jako `-125`

## Porovnávací operátory
`==` a `!=` se používají ke kontrole, zda jsou dvě hodnoty "rovny" (`==`) nebo "nerovny" (`!=`). Lze je použít na všechny typy hodnot.

`2 == 2` se vyhodnotí jako `True`
`Entities.Bush != Entities.Bush` se vyhodnotí jako `False`
`3 != 3 + 1` se vyhodnotí jako `True`

`<=, >=, <, >` lze použít pouze na čísla. Kontrolují, zda je levé číslo "menší nebo rovno" (`<=`), "větší nebo rovno" (`>=`), "menší" (`<`) nebo "větší" (`>`) než pravé číslo.

`1 <= 1` se vyhodnotí jako `True`
`2 >= 3` se vyhodnotí jako `False`
`-2 < -1` se vyhodnotí jako `True`
`6 > 6` se vyhodnotí jako `False`

## Logické operátory
`not` jednoduše invertuje hodnotu:

`not False` se vyhodnotí jako `True`
`not True` se vyhodnotí jako `False`

`and` se vyhodnotí jako `True` pouze pokud jsou obě hodnoty `True`

`True and True` se vyhodnotí jako `True`
`True and False` se vyhodnotí jako `False`
`False and False` se vyhodnotí jako `False`

`or` se vyhodnotí jako `True`, pokud je alespoň jedna z hodnot `True`

`True or True` se vyhodnotí jako `True`
`True or False` se vyhodnotí jako `True`
`False or False` se vyhodnotí jako `False`