# Krotki
Krotki to świetny sposób na połączenie wielu wartości w jedną. Aby stworzyć krotkę, wystarczy oddzielić wartości przecinkami:

`tuple = 1, 2`

Możesz je także rozpakować z powrotem do kilku zmiennych. W poniższym kodzie krotka `(1,2)` jest rozpakowywana do dwóch zmiennych `a` i `b`.

`a, b = 1, 2`

Krotki można indeksować jak listy, ale są niemutowalne i nie można ich zmieniać po stworzeniu.

`tuple = 1, 2`

`print(tuple[1])`
drukuje `2`

`tuple[0] = 3`
rzuca error
<unlock=dicts>
W przeciwieństwie do list, krotki mogą być używane jako klucze w dictionaries.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`drukuje` (4,5)</unlock>

Mogą być także przydatne przy zwracaniu wielu wartości z funkcji.

`def f():
    return 1, 2

a, b = f()`