# Operatory
operatory arytmetyczne: `+, -, *, /, //, %, **`
operatory porównania: `==, !=, <=, >=, <, >`
operatory logiczne: `not, and, or`

Notatka: Wszystkie liczby w grze to liczby zmiennoprzecinkowe. Więc wszystkie operatory arytmetyczne są operatorami zmiennoprzecinkowymi.
`//` jest zdefiniowany jako zaokrąglenie liczby w dół po podzieleniu.

Aby używać operatorów przypisania, musisz odblokować sekcję "Zmienne".

## Wprowadzenie
Operatory pozwalają porównywać, modyfikować i łączyć wartości.
Operatory arytmetyczne `+, -, *, /, //, %, **` są używane do wykonywania podstawowych operacji matematycznych na liczbach.
Operatory porównania `==, !=, <=, >=, <, >` są używane do porównywania wartości. Wynik jest zawsze albo `True` albo `False`.
Operatory logiczne (zwane również operatorami boolowskimi) `not, and, or` są używane do łączenia wartości logicznych.

## Operatory Arytmetyczne
`+` i `-` są używane do dodawania i odejmowania.

`2 + 3` daje `5`
`3 - 2` daje `1`

`*`, `/` i `//` są używane do mnożenia i dzielenia.

`2 * 3` daje `6`
`5 / 2` daje `2.5`

`//` robi to samo co `/`, ale wynik jest zaokrąglony w dół do najbliższej liczby całkowitej.

`5 // 2` daje `2`

`%` jest operatorem modulo, znanym również jako operator reszty. Tak naprawdę dzieli dwie liczby, a potem zwraca resztę. Możesz też myśleć o tym jako o powtarzalnym odejmowaniu prawej liczby od lewej, aż pozostanie mniej niż prawa liczba.

`4 % 2` daje `0`
`5 % 2` daje `1`
`6 % 2` daje `0`
`2 % 6` daje `2`
`1.5 % 1` daje `0.5`

`**` jest operatorem potęgowania.

`2**2` daje `4`
`(-5)**3` daje `-125`

## Operatory Porównania
`==` i `!=` są używane do sprawdzania, czy dwie wartości są "równe"(`==`) lub "nie są równe"(`!=`). Mogą być używane na wszystkich typach wartości.

`2 == 2` daje `True`
`Entities.Bush != Entities.Bush` daje `False`
`3 != 3 + 1` daje `True`

`<=, >=, <, >` mogą być używane tylko na liczbach. Sprawdzają, czy lewa liczba jest "mniejsza lub równa"(`<=`), "większa lub równa"(`>=`), "mniejsza" (`<`) lub "większa" (`>`) od prawej liczby.

`1 <= 1` daje `True`
`2 >= 3` daje `False`
`-2 < -1` daje `True`
`6 > 6` daje `False`

## Operatory Logiczne
`not` po prostu odwraca wartość:

`not False` daje `True`
`not True` daje `False`

`and` daje `True` tylko wtedy, gdy obie wartości są `True`

`True and True` daje `True`
`True and False` daje `False`
`False and False` daje `False`

`or` daje `True`, jeśli przynajmniej jedna z wartości jest `True`

`True or True` daje `True`
`True or False` daje `True`
`False or False` daje `False`