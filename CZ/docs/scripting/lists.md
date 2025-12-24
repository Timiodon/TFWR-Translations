# Seznamy
Seznamy jsou snadný způsob, jak uložit více hodnot do jedné proměnné.
Nové seznamy můžete vytvořit takto:

`list = [2, True, Items.Hay]`

Seznam nyní obsahuje hodnoty `2`, `True` a `Items.Hay`.
Seznam může být také prázdný:

`empty_list = []`

K prvku seznamu můžete přistupovat pomocí jeho indexu. Index je `0` pro první prvek, `1` pro druhý prvek, `2` pro třetí...

zasadí mrkve
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Seznam můžete procházet pomocí cyklu for. Následující příklad sečte všechny prvky v seznamu.

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

`list.remove(elem)` odstraní první výskyt prvku ze seznamu:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` je nyní `[1, 4, 2]`

`list.insert(index, elem)` vloží prvek na zadaný index:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` je nyní `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` odstraní prvek na zadaném indexu.
Pokud není zadán žádný index, odstraní se poslední položka.

`list = [3, 5, 8, 25]
list.pop()`
`list` je nyní `[3, 5, 8]`
`list.pop(1)`
`list` je nyní `[3, 8]`

Funkce `len()` vrací délku seznamu.
`list = [3, 2, 1]
x = len(list)`
`x` je nyní `3`

Seznamy mají referenční sémantiku. To znamená, že přiřazení seznamu do proměnné přiřadí této proměnné stejný objekt seznamu, místo aby se vytvořila kopie seznamu.
Pokud dvě proměnné odkazují na stejný seznam, změny v seznamu se projeví u obou.

`a = [1,2]
b = a
b.pop()`
`a` i `b` jsou nyní oba `[1]`
