# Kosten
Jede Kostenaufstellung kann als ein Dictionary dargestellt werden, das Items auf Zahlen abbildet.

Die `get_cost()`-Funktion gibt ein solches Dictionary zurück. Sie gibt die Kosten für eine Pflanze oder eine Freischaltung zurück.

`get_cost(Entities.Pumpkin)`
gibt `{Items.Carrot:1}` zurück

Bei Freischaltungen kann optional ein zweites Argument für die Freischalt-Stufe übergeben werden, für die du die Kosten erhalten möchtest. Standardmäßig ist es die aktuelle Freischalt-Stufe.

`get_cost(Unlocks.Loops, 0)`
gibt `{Items.Hay:5}` zurück

Für Freischaltungen, die bereits auf der maximalen Stufe sind, gibt `get_cost()` `None` zurück.

Es kann so verwendet werden:
`cost = get_cost(etwas)
for item in cost:
	amount_of_this_item_needed = cost[item]`
