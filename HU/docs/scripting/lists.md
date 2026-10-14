# Listák
A listák egyszerű módja több érték tárolásának egyetlen változóban.
Így hozhatsz létre új listákat:

`some_list = [2, True, Items.Hay]`

A lista most a `2`, `True` és `Items.Hay` értékeket tartalmazza.
Egy lista üres is lehet:

`empty_list = []`

A listaelemeket az indexükön keresztül érheted el. Az index `0` az első elemhez, `1` a másodikhoz, `2` a harmadikhoz...

répa ültetése
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Egy listán for ciklussal iterálhatsz. A következő példa összeadja a lista összes elemét.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
A `sum` most `18`

A következő lista metódusok lehetővé teszik elemek hozzáadását és eltávolítását:

`elements.append(elem)` hozzáad egy elemet a lista végéhez:

`numbers = [2, 6, 12]
numbers.append(7)`
A `numbers` most `[2, 6, 12, 7]`

`elements.remove(elem)` eltávolítja egy elem első előfordulását a listából:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
A `numbers` most `[1, 4, 2]`

`elements.insert(index, elem)` beszúr egy elemet a megadott indexre:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
A `some_list` most `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` eltávolítja az elemet a megadott indexen.
Ha nincs megadva index, az utolsó elem kerül eltávolításra.

`numbers = [3, 5, 8, 25]
numbers.pop()`
A `numbers` most `[3, 5, 8]`
`numbers.pop(1)`
A `numbers` most `[3, 8]`

A `len()` függvény visszaadja a lista hosszát.
`numbers = [3, 2, 1]
x = len(numbers)`
Az `x` most `3`

A listák referencia szemantikájúak. Ez azt jelenti, hogy ha egy listát hozzárendelsz egy változóhoz, akkor ugyanazt a lista objektumot rendeled hozzá, nem másolatot készítesz.
Ha két változó ugyanarra a listára mutat, a lista változtatásait mindkettő látni fogja.

`a = [1, 2]
b = a
b.pop()`
Az `a` és `b` is most `[1]`