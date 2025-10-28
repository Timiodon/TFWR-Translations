# Costs
Jakýkoli náklad může být reprezentován jako slovník, který mapuje předměty na číselné hodnoty.

Funkce `get_cost()` vrací takový slovník. Vrací cenu rostliny nebo odemknutí.

`get_cost(Entities.Pumpkin)`  
vrátí `{Items.Carrot:1}`

U odemykání lze volitelně předat druhý argument určující úroveň, pro kterou chceš získat cenu. Výchozí hodnota je aktuální úroveň odemknutí.

`get_cost(Unlocks.Loops, 0)`  
vrátí `{Items.Hay:5}`

U odemykání, které je již na maximální úrovni, vrátí `get_cost()` hodnotu `None`.

Lze ji použít například takto:  
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
