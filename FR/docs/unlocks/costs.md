# Coûts
Tout coût peut être représenté comme un dictionnaire qui mappe des objets à des nombres.

La fonction `get_cost()` retourne un tel dictionnaire. Elle retourne le coût d'une plante ou d'un déblocage.

`get_cost(Entities.Pumpkin)`
retourne `{Items.Carrot:1}`

Pour les déblocages, un deuxième argument optionnel peut être passé pour le niveau de déblocage dont vous voulez obtenir le coût. Par défaut, c'est le niveau de déblocage actuel.

`get_cost(Unlocks.Loops, 0)`
retourne `{Items.Hay:5}`

Pour les déblocages qui sont déjà au niveau maximum, `get_cost()` retournera `None`.

Il peut être utilisé comme ceci :
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`