# Listen
Listen sind eine einfache Möglichkeit, mehrere Werte in einer einzigen Variablen zu speichern.
Du kannst neue Listen so erstellen:

`list = [2, True, Items.Hay]`

Die Liste enthält jetzt die Werte `2`, `True` und `Items.Hay`.
Eine Liste kann auch leer sein:

`empty_list = []`

Du kannst auf ein Element einer Liste über seinen Index zugreifen. Der Index ist `0` für das erste Element, `1` für das zweite Element, `2` für das dritte...

_pflanzt Karotten_
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Du kannst mit einer for-Schleife über eine Liste iterieren. Das folgende Beispiel summiert alle Elemente in der Liste.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` ist jetzt `18`

Die folgenden Listenmethoden ermöglichen es dir, Elemente hinzuzufügen und zu entfernen:

`list.append(elem)` fügt ein Element am Ende der Liste hinzu:

`list = [2, 6, 12]
list.append(7)`
`list` ist jetzt `[2, 6, 12, 7]`

`list.remove(elem)` entfernt das erste Vorkommen eines Elements aus einer Liste:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` ist jetzt `[1, 4, 2]`

`list.insert(index, elem)` fügt ein Element am angegebenen Index ein:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` ist jetzt `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` entfernt das Element am angegebenen Index.
Wenn kein Index angegeben wird, wird das letzte Element entfernt.

`list = [3, 5, 8, 25]
list.pop()`
`list` ist jetzt `[3, 5, 8]`
`list.pop(1)`
`list` ist jetzt `[3, 8]`

Die `len()`-Funktion gibt die Länge der Liste zurück.
`list = [3, 2, 1]
x = len(list)`
`x` ist jetzt `3`

Listen haben Referenzsemantik. Das bedeutet, dass die Zuweisung einer Liste zu einer Variable dasselbe Listenobjekt dieser Variable zuweist, anstatt eine Kopie der Liste zu erstellen.
Wenn zwei Variablen auf dieselbe Liste verweisen, werden Änderungen an der Liste von beiden gesehen.

`a = [1,2]
b = a
b.pop()`
`a` und `b` sind jetzt beide `[1]`
