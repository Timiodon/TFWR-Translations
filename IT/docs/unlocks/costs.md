# Costi
Qualsiasi costo può essere rappresentato come un dictionary che mappa gli oggetti a numeri.

La funzione `get_cost()` restituisce un dictionary del genere. Restituisce il costo di una pianta o di uno sblocco.

`get_cost(Entities.Pumpkin)`
restituisce `{Items.Carrot:1}`

Per gli sblocchi, può essere passato un secondo argumento opzionale per il livello di sblocco di cui vuoi ottenere il costo. Di default, è il livello di sblocco attuale.

`get_cost(Unlocks.Loops, 0)`
restituisce `{Items.Hay:5}`

Per gli sblocchi che sono già al livello massimo, `get_cost()` restituirà `None`.

Può essere usato così:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`