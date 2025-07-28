# 成本
任何成本都可以表示为一个将物品映射到数字的 dictionary。

`get_cost()` 函数返回这样一个 dictionary。它返回一种植物或一个解锁项的成本。

`get_cost(Entities.Pumpkin)`
返回 `{Items.Carrot:1}`

对于解锁项，可以传递一个可选的第二个参数，用于指定你想要获取成本的解锁等级。默认情况下，它是当前的解锁等级。

`get_cost(Unlocks.Loops, 0)`
返回 `{Items.Hay:5}`

对于已经达到最高等级的解锁项，`get_cost()` 将返回 `None`。

它可以这样使用：
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`