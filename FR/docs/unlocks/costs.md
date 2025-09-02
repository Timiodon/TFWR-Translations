# Coûts
Tout coût peut être représenté par un dictionnaire qui mappe des objets à des nombres.

La fonction `get_cost()` renvoie un tel dictionnaire. Elle renvoie le coût d'une plante ou d'un déblocage.

`get_cost(Entities.Pumpkin)`
renvoie `{Items.Carrot:1}`

Pour les déblocages, un deuxième argument optionnel peut être passé pour le niveau de déblocage dont tu veux obtenir le coût. Par défaut, c'est le niveau de déblocage actuel.

`get_cost(Unlocks.Loops, 0)`
renvoie `{Items.Hay:5}`

Pour les déblocages qui sont déjà au niveau maximum, `get_cost()` renverra `None`.

Il peut être utilisé comme ceci :
`cost = get_cost(quelque_chose)
for item in cost:
	quantite_de_cet_objet_necessaire = cost[item]`