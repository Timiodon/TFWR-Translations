# Operatory
operatory arytmetyczne: `+, -, *, /, //, %, **`
operatory porównania: `==, !=, <=, >=, <, >`
operatory logiczne: `not, and, or`

Uwaga: Wszystkie liczby w grze to liczby zmiennoprzecinkowe (floating point). Więc wszystkie operatory arytmetyczne są operatorami zmiennoprzecinkowymi.
`//` jest zdefiniowane tak, że po prostu zaokrągla liczbę w dół po dzieleniu.

Aby używać operatorów przypisania, musisz odblokować ulepszenie „Zmienne”.

## Wprowadzenie
Operatory pozwalają porównywać, modyfikować i łączyć wartości.
Operatory arytmetyczne `+, -, *, /, //, %, **` służą do wykonywania popularnych operacji matematycznych na liczbach.
Operatory porównania `==, !=, <=, >=, <, >` służą do porównywania wartości. Wynikiem jest zawsze `True` lub `False`.
Operatory logiczne (nazywane również operatorami boolean) `not, and, or` służą do łączenia wartości logicznych.

## Operatory arytmetyczne
`+` i `-` służą do dodawania i odejmowania.

`2 + 3` daje w wyniku `5`
`3 - 2` daje w wyniku `1`

`*`, `/` i `//` służą do mnożenia i dzielenia.

`2 * 3` daje w wyniku `6`
`5 / 2` daje w wyniku `2.5`

`//` robi to samo co `/`, ale wynik jest zaokrąglany w dół (do następnej liczby całkowitej).

`5 // 2` daje w wyniku `2`

`%` to operator modulo, znany również jako operator reszty z dzielenia. Zasadniczo dzieli dwie liczby, a następnie zwraca resztę. Można też o nim myśleć jako o wielokrotnym odejmowaniu prawej liczby od lewej, aż reszta będzie mniejsza od prawej liczby.

`4 % 2` daje w wyniku `0`
`5 % 2` daje w wyniku `1`
`6 % 2` daje w wyniku `0`
`2 % 6` daje w wyniku `2`
`1.5 % 1` daje w wyniku `0.5`

`**` to operator potęgowania.

`2**2` daje w wyniku `4`
`(-5)**3` daje w wyniku `-125`

## Operatory porównania
`==` i `!=` służą do sprawdzania, czy dwie wartości są „równe” (`==`) lub „nierówne” (`!=`). Mogą być używane na wszystkich typach wartości.

`2 == 2` daje w wyniku `True`
`Entities.Bush != Entities.Bush` daje w wyniku `False`
`3 != 3 + 1` daje w wyniku `True`

`<=, >=, <, >` mogą być używane tylko na liczbach. Sprawdzają, czy lewa liczba jest „mniejsza lub równa” (`<=`), „większa lub równa” (`>=`), „mniejsza” (`<`) lub „większa” (`>`) niż prawa liczba.

`1 <= 1` daje w wyniku `True`
`2 >= 3` daje w wyniku `False`
`-2 < -1` daje w wyniku `True`
`6 > 6` daje w wyniku `False`

## Operatory logiczne
`not` po prostu odwraca wartość:

`not False` daje w wyniku `True`
`not True` daje w wyniku `False`

`and` daje w wyniku `True` tylko wtedy, gdy obie wartości są `True`

`True and True` daje w wyniku `True`
`True and False` daje w wyniku `False`
`False and False` daje w wyniku `False`

`or` daje w wyniku `True`, jeśli co najmniej jedna z wartości jest `True`

`True or True` daje w wyniku `True`
`True or False` daje w wyniku `True`
`False or False` daje w wyniku `False`