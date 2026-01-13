# Lists
Seznamy (lists) jsou jednoduchý způsob, jak uložit více hodnot do jedné proměnné.  
Nový seznam vytvoříš takto:

`list = [2, True, Items.Hay]`

Seznam nyní obsahuje hodnoty `2`, `True` a `Items.Hay`.  
Seznam může být i prázdný:

`empty_list = []`

K prvku seznamu se přistupuje pomocí indexu. Index `0` označuje první prvek, `1` druhý, `2` třetí atd.

zasadí mrkev
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Pomocí cyklu `for` můžeš procházet všechny prvky seznamu. Následující příklad sečte všechny hodnoty v seznamu.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` je nyní `18`

Následující metody seznamu umožňují přidávat a odebírat prvky:

`list.append(elem)` přidá prvek na konec seznamu:

`list = [2, 6, 12]
list.append(7)`
`list` je nyní `[2, 6, 12, 7]`

`list.remove(elem)` odstraní první výskyt daného prvku ze seznamu:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` je nyní `[1, 4, 2]`

`list.insert(index, elem)` vloží prvek na zadaný index:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` je nyní `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` odstraní prvek na zadaném indexu.  
Pokud index není uveden, odstraní se poslední prvek.

`list = [3, 5, 8, 25]
list.pop()`
`list` je nyní `[3, 5, 8]`
`list.pop(1)`
`list` je nyní `[3, 8]`

Funkce `len()` vrací délku seznamu.
`list = [3, 2, 1]
x = len(list)`
`x` je nyní `3`

Seznamy mají referenční sémantiku.  
To znamená, že přiřazení seznamu do jiné proměnné vytvoří odkaz na stejný objekt seznamu, nikoli jeho kopii. Pokud dvě proměnné odkazují na stejný seznam, změny seznamu se projeví v obou.

`a = [1,2]
b = a
b.pop()`
`a` i `b` jsou nyní `[1]`
