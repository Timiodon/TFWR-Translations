# Listy
Listy to prosty sposób na przechowywanie wielu wartości w jednej zmiennej.
Możesz tworzyć nowe listy w ten sposób:

`list = [2, True, Items.Hay]`

Lista zawiera teraz wartości `2`, `True` i `Items.Hay`.
Lista może być także pusta:

`empty_list = []`

Możesz uzyskać dostęp do elementu listy za pomocą jego indeksu. Indeks to `0` dla pierwszego elementu, `1` dla drugiego, `2` dla trzeciego...

sadź marchewki
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Możesz iterować po liście przy użyciu pętli for. Poniższy przykład sumuje wszystkie elementy na liście.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` ma teraz wartość `18`

Następujące metody list pozwalają dodawać i usuwać elementy:

`list.append(elem)` dodaje element na końcu listy:

`list = [2, 6, 12]
list.append(7)`
`list` to teraz `[2, 6, 12, 7]`

`list.remove(elem)` usuwa pierwsze wystąpienie elementu z listy:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` to teraz `[1, 4, 2]`

`list.insert(index, elem)` wstawia element na podanym indeksie:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` to teraz `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` usuwa element na podanym indeksie.
Jeśli nie podasz indeksu, zostanie usunięty ostatni element.

`list = [3, 5, 8, 25]
list.pop()`
`list` to teraz `[3, 5, 8]`
`list.pop(1)`
`list` to teraz `[3, 8]`

Funkcja `len()` zwraca długość listy.
`list = [3, 2, 1]
x = len(list)`
`x` to teraz `3`

Listy mają semantykę referencji. Oznacza to, że przypisanie listy do zmiennej przypisuje ten sam obiekt listy do tej zmiennej, zamiast tworzyć kopię listy.
Jeśli dwie zmienne odnoszą się do tej samej listy, zmiany w liście będą widoczne dla obu.

`a = [1,2]
b = a
b.pop()`
`a` i `b` to teraz obie `[1]`