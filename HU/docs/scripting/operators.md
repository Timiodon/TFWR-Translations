# Operátorok
aritmetikai operátorok: `+, -, *, /, //, %, **`
összehasonlító operátorok: `==, !=, <=, >=, <, >`
logikai operátorok: `not, and, or`

Megjegyzés: A játékban minden szám lebegőpontos szám. Így minden aritmetikai operátor lebegőpontos operátor.
A `//` úgy van definiálva, hogy csak lefelé kerekíti a számot az osztás után.

Az értékadás operátorokhoz fel kell oldani a "Változók" feloldást.

## Bevezetés
Az operátorok lehetővé teszik az értékek összehasonlítását, módosítását és kombinálását.
Az aritmetikai operátorok `+, -, *, /, //, %, **` a számokon végzett gyakori matematikai műveletekhez használatosak.
Az összehasonlító operátorok `==, !=, <=, >=, <, >` értékek összehasonlítására használatosak. Az eredmény mindig `True` vagy `False`.
A logikai operátorok (boolean operátoroknak is hívják) `not, and, or` az igazságértékek kombinálására szolgálnak.

## Aritmetikai operátorok
A `+` és `-` összeadásra és kivonásra használatos.

`2 + 3` eredménye `5`
`3 - 2` eredménye `1`

A `*`, `/` és `//` szorzásra és osztásra használatos.

`2 * 3` eredménye `6`
`5 / 2` eredménye `2.5`

A `//` ugyanazt csinálja, mint a `/`, de az eredményt lefelé kerekíti (a következő egész számra).

`5 // 2` eredménye `2`

A `%` a maradék operátor, más néven maradék operátor. Lényegében elosztja a két számot, majd visszaadja a maradékot. Úgy is gondolhatsz rá, mint a jobb oldali szám ismételt kivonására a bal oldali számból, amíg a maradék kisebb nem lesz a jobb oldali számnál.

`4 % 2` eredménye `0`
`5 % 2` eredménye `1`
`6 % 2` eredménye `0`
`2 % 6` eredménye `2`
`1.5 % 1` eredménye `0.5`

A `**` a hatványozás operátor.

`2**2` eredménye `4`
`(-5)**3` eredménye `-125`

## Összehasonlító operátorok
A `==` és `!=` "egyenlő"(`==`) vagy "nem egyenlő"(`!=`) ellenőrzésére használatos. Minden értéktípuson használható.

`2 == 2` eredménye `True`
`Entities.Bush != Entities.Bush` eredménye `False`
`3 != 3 + 1` eredménye `True`

A `<=, >=, <, >` csak számokon használható. Ellenőrzi, hogy a bal oldali szám "kisebb vagy egyenlő"(`<=`), "nagyobb vagy egyenlő"(`>=`), "kisebb" (`<`) vagy "nagyobb" (`>`) mint a jobb oldali szám.

`1 <= 1` eredménye `True`
`2 >= 3` eredménye `False`
`-2 < -1` eredménye `True`
`6 > 6` eredménye `False`

## Logikai operátorok
A `not` egyszerűen megfordítja az értéket:

`not False` eredménye `True`
`not True` eredménye `False`

Az `and` csak akkor `True`, ha mindkét érték `True`

`True and True` eredménye `True`
`True and False` eredménye `False`
`False and False` eredménye `False`

Az `or` `True`, ha legalább az egyik érték `True`

`True or True` eredménye `True`
`True or False` eredménye `True`
`False or False` eredménye `False`