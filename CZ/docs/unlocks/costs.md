# Náklady
Jakýkoli náklad lze reprezentovat jako slovník, který mapuje předměty na čísla.

Funkce `get_cost()` vrací takový slovník. Vrací cenu rostliny nebo odemčení.

`get_cost(Entities.Pumpkin)`
vrátí `{Items.Carrot:1}`

Pro odemčení lze předat volitelný druhý argument pro úroveň odemčení, pro kterou chcete získat cenu. Ve výchozím nastavení je to aktuální úroveň odemčení.

`get_cost(Unlocks.Loops, 0)`
vrátí `{Items.Hay:5}`

Pro odemčení, která jsou již na maximální úrovni, vrátí `get_cost()` hodnotu `None`.

Lze to použít takto:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
