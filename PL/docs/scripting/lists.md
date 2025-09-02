# Listy
Listy to łatwy sposób na przechowywanie wielu wartości w jednej zmiennej.
Możesz tworzyć nowe listy w ten sposób:

`lista = [2, True, Items.Hay]`

Lista zawiera teraz wartości `2`, `True` i `Items.Hay`.
Lista może być również pusta:

`pusta_lista = []`

Możesz uzyskać dostęp do elementu listy za pomocą jego indeksu. Indeks to `0` dla pierwszego elementu, `1` dla drugiego, `2` dla trzeciego...

sadzi marchewki
`lista = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(lista[1])`

Możesz iterować po liście za pomocą pętli for. Poniższy przykład sumuje wszystkie elementy na liście.

`lista = [4, 7, 2, 5]
suma = 0
for liczba in lista:
	suma += liczba`
`suma` wynosi teraz `18`

Poniższe metody list pozwalają na dodawanie i usuwanie elementów:

`list.append(elem)` dodaje element na koniec listy:

`lista = [2, 6, 12]
lista.append(7)`
`lista` to teraz `[2, 6, 12, 7]`

`list.remove(elem)` usuwa pierwsze wystąpienie elementu z listy:

`lista = [1, 2, 4, 2]
lista.remove(2)`
`lista` to teraz `[1, 4, 2]`

`list.insert(index, elem)` wstawia element na podanym indeksie:

`lista = [Entities.Tree, Items.Hay]
lista.insert(1, Items.Wood)`
`lista` to teraz `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` usuwa element na określonym indeksie.
Jeśli nie podano indeksu, usuwany jest ostatni element.

`lista = [3, 5, 8, 25]
lista.pop()`
`lista` to teraz `[3, 5, 8]`
`lista.pop(1)`
`lista` to teraz `[3, 8]`

Funkcja `len()` zwraca długość listy.
`lista = [3, 2, 1]
x = len(lista)`
`x` wynosi teraz `3`

Listy mają semantykę referencji. Oznacza to, że przypisanie listy do zmiennej przypisuje ten sam obiekt listy do tej zmiennej, zamiast tworzyć kopię listy.
Jeśli dwie zmienne odnoszą się do tej samej listy, zmiany na liście będą widoczne dla obu.

`a = [1,2]
b = a
b.pop()`
`a` i `b` to teraz obie `[1]`