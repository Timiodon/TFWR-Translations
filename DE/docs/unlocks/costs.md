# Kosten
Alle Kosten können als ein Dictionary dargestellt werden, das Items auf Zahlen abbildet.

Die `get_cost()`-Funktion gibt ein solches Dictionary zurück. Sie gibt die Kosten einer Pflanze oder einer Freischaltung zurück.

`get_cost(Entities.Pumpkin)`
gibt `{Items.Carrot:1}` zurück

Bei Freischaltungen kann optional ein zweites Argument für das Freischaltungslevel übergeben werden, für das du die Kosten erhalten möchtest. Standardmäßig ist es das aktuelle Freischaltungslevel.

`get_cost(Unlocks.Loops, 0)`
gibt `{Items.Hay:5}` zurück

Bei Freischaltungen, die bereits auf dem maximalen Level sind, gibt `get_cost()` `None` zurück.

Es kann so verwendet werden:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
