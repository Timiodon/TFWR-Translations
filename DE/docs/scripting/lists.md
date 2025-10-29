# Listen
Listen sind eine einfache Möglichkeit, mehrere Werte in einer einzigen Variablen zu speichern.
Du kannst neue Listen so erstellen:

`some_list = [2, True, Items.Hay]`

Die Liste enthält jetzt die Werte `2`, `True` und `Items.Hay`.
Eine Liste kann auch leer sein:

`empty_list = []`

Du kannst auf ein Element einer Liste über seinen Index zugreifen. Der Index ist `0` für das erste Element, `1` für das zweite Element, `2` für das dritte...

_pflanzt Karotten_
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Du kannst mit einer for-Schleife über eine Liste iterieren. Das folgende Beispiel summiert alle Elemente in der Liste.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` ist jetzt `18`

Die folgenden Listenmethoden ermöglichen es dir, Elemente hinzuzufügen und zu entfernen:

`elements.append(elem)` fügt ein Element am Ende der Liste hinzu:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` ist jetzt `[2, 6, 12, 7]`

`elements.remove(elem)` entfernt das erste Vorkommen eines Elements aus einer Liste:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` ist jetzt `[1, 4, 2]`

`elements.insert(index, elem)` fügt ein Element am angegebenen Index ein:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` ist jetzt `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` entfernt das Element am angegebenen Index.
Wenn kein Index angegeben wird, wird das letzte Element entfernt.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` ist jetzt `[3, 5, 8]`
`numbers.pop(1)`
`numbers` ist jetzt `[3, 8]`

Die `len()`-Funktion gibt die Länge der Liste zurück.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` ist jetzt `3`

Listen haben Referenzsemantik. Das bedeutet, dass die Zuweisung einer Liste zu einer Variable dasselbe Listenobjekt dieser Variable zuweist, anstatt eine Kopie der Liste zu erstellen.
Wenn zwei Variablen auf dieselbe Liste verweisen, werden Änderungen an der Liste von beiden gesehen.

`a = [1, 2]
b = a
b.pop()`
`a` und `b` sind jetzt beide `[1]`
