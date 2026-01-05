# Costs
Any cost can be represented as a dictionary that maps items to numbers.

The `get_cost()` function returns such a dictionary. It returns the cost of a plant or an unlock.

`get_cost(Entities.Pumpkin)`
returns `{Items.Carrot:1}`

For unlocks, an optional second argument can be passed for the unlock level you want to get the cost for. By default, it's the current unlock level.

`get_cost(Unlocks.Loops, 0)`
returns `{Items.Hay:5}`

For unlocks that are already at the max level, `get_cost()` will return `None`.

It can be used like this:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
