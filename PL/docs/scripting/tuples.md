# Krotki
Krotki to świetny sposób na połączenie wielu wartości w jedną.
Aby utworzyć krotkę, po prostu oddziel wartości przecinkami:

`krotka = 1, 2`

Można je również ponownie rozpakować do kilku zmiennych. W poniższym kodzie krotka `(1,2)` jest rozpakowywana do dwóch zmiennych `a` i `b`.

`a, b = 1, 2`

Krotki można indeksować jak listy, ale są one niemutowalne i nie można ich zmieniać po utworzeniu.

`krotka = 1, 2`

`print(krotka[1])`
wyświetla `2`

`krotka[0] = 3`
zgłasza błąd
<unlock=dicts>
W przeciwieństwie do list, krotki mogą być używane jako klucze w słownikach.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`wyświetla` (4,5)</unlock>

Mogą być również przydatne do zwracania wielu wartości w funkcji.

`def f():
    return 1, 2

a, b = f()`