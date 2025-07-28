# Costi
Qualsiasi costo può essere rappresentato come un dizionario che mappa item a numeri.

La funzione `get_cost()` restituisce un tale dizionario. Restituisce il costo di una pianta o di uno sblocco.

`get_cost(Entities.Pumpkin)`
restituisce `{Items.Carrot:1}`

Per gli sblocchi, può essere passato un secondo argomento opzionale per il livello di sblocco di cui si vuole ottenere il costo. Di default, è il livello di sblocco attuale.

`get_cost(Unlocks.Loops, 0)`
restituisce `{Items.Hay:5}`

Per gli sblocchi che sono già al livello massimo, `get_cost()` restituirà `None`.

Può essere usato in questo modo:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
