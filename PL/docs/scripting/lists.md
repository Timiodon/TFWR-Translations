# Listy
Listy to łatwy sposób na przechowywanie wielu wartości w jednej zmiennej.
Możesz tworzyć nowe listy w ten sposób:

`some_list = [2, True, Items.Hay]`

Lista zawiera teraz wartości `2`, `True` i `Items.Hay`.
Lista może być również pusta:

`empty_list = []`

Możesz uzyskać dostęp do elementu listy za pomocą jego indeksu. Indeks to `0` dla pierwszego elementu, `1` dla drugiego, `2` dla trzeciego...

sadzi marchewki
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Możesz iterować po liście za pomocą pętli for. Poniższy przykład sumuje wszystkie elementy na liście.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` wynosi teraz `18`

Poniższe metody list pozwalają na dodawanie i usuwanie elementów:

`elements.append(elem)` dodaje element na koniec listy:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` to teraz `[2, 6, 12, 7]`

`elements.remove(elem)` usuwa pierwsze wystąpienie elementu z listy:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` to teraz `[1, 4, 2]`

`elements.insert(index, elem)` wstawia element na podanym indeksie:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` to teraz `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` usuwa element na określonym indeksie.
Jeśli nie podano indeksu, usuwany jest ostatni element.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` to teraz `[3, 5, 8]`
`numbers.pop(1)`
`numbers` to teraz `[3, 8]`

Funkcja `len()` zwraca długość listy.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` wynosi teraz `3`

Listy mają semantykę referencji. Oznacza to, że przypisanie listy do zmiennej przypisuje ten sam obiekt listy do tej zmiennej, zamiast tworzyć kopię listy.
Jeśli dwie zmienne odnoszą się do tej samej listy, zmiany na liście będą widoczne dla obu.

`a = [1, 2]
b = a
b.pop()`
`a` i `b` to teraz obie `[1]`
