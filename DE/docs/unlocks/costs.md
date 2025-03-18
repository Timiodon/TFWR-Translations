# Kosten
Jeder Kostenpunkt kann als ein Dictionary dargestellt werden, das Gegenstände mit Zahlen verknüpft.

Die `get_cost()` Funktion gibt ein solches Dictionary zurück. Sie liefert die Kosten einer Pflanze oder einer Freischaltung.

`get_cost(Entities.Pumpkin)`
gibt `{Items.Carrot:1}` zurück

Für Freischaltungen kann ein optionales zweites Argument übergeben werden, um das Freischaltungslevel anzugeben, für das man die Kosten haben möchte. Standardmäßig ist es das aktuelle Freischaltungslevel.

`get_cost(Unlocks.Loops, 0)`
gibt `{Items.Hay:5}` zurück

Für Freischaltungen, die bereits das maximale Level erreicht haben, wird `get_cost()` `None` zurückgeben.

Die Funktion kann so verwendet werden:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`