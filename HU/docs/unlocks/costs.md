# Költségek
Bármilyen költség szótárként reprezentálható, ami itemeket számokra képez le.

A `get_cost()` függvény ilyen szótárat ad vissza. Visszaadja egy növény vagy feloldás költségét.

`get_cost(Entities.Pumpkin)`
visszaadja `{Items.Carrot:1}`

A feloldásokhoz opcionális második argumentum adható át a kívánt feloldási szinthez, aminek a költségét meg akarod kapni. Alapértelmezetten az aktuális feloldási szint.

`get_cost(Unlocks.Loops, 0)`
visszaadja `{Items.Hay:5}`

A már maximum szinten lévő feloldásokhoz a `get_cost()` `None`-t ad vissza.

Használható így:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`