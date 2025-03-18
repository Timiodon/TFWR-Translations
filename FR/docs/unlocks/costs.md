# Coûts
Un coût peut être représenté comme un dictionary qui associe des items à des nombres.

La fonction `get_cost()` renvoie un tel dictionary. Il renvoie le coût d'une plante ou d'un déblocage.

`get_cost(Entities.Pumpkin)`
renvoie `{Items.Carrot:1}`

Pour les déblocages, un second argument optionnel peut être passé pour le niveau de déblocage pour lequel vous souhaitez obtenir le coût. Par défaut, c'est le niveau de déblocage actuel.

`get_cost(Unlocks.Loops, 0)`
renvoie `{Items.Hay:5}`

Pour les déblocages qui sont déjà au niveau maximum, `get_cost()` renverra `None`.

Il peut être utilisé comme ceci :
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`