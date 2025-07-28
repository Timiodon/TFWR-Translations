# Krotki (Tuples)
Krotki (tuples) to świetny sposób na połączenie wielu wartości w jedną.
Aby utworzyć krotkę, po prostu oddziel wartości przecinkami:

`krotka = 1, 2`

Możesz je również ponownie rozpakować na kilka zmiennych. W poniższym kodzie krotka `(1,2)` jest rozpakowywana na dwie zmienne `a` i `b`.

`a, b = 1, 2`

Krotki można indeksować jak listy, ale są one niezmienne (immutable) i nie można ich zmieniać po utworzeniu.

`krotka = 1, 2`

`print(krotka[1])`
drukuje `2`

`krotka[0] = 3`
zgłasza error
<unlock=dicts>
W przeciwieństwie do list, krotki mogą być używane jako klucze w słownikach.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`drukuje` (4,5)</unlock>

Mogą być również przydatne do zwracania wielu wartości w funkcji.

`def f():
    return 1, 2

a, b = f()`