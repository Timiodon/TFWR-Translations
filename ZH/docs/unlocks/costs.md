# 成本
任何成本都可以表示为一个将物品映射到数字的dictionary。

`get_cost()`函数返回这样一个dictionary。它返回植物或解锁项的成本。

`get_cost(Entities.Pumpkin)`
返回`{Items.Carrot:1}`

对于解锁项，可以传递一个可选的第二个argument，以获取相应解锁级别的成本。默认情况下，是当前的解锁级别。

`get_cost(Unlocks.Loops, 0)`
返回`{Items.Hay:5}`

对于已经达到最大级别的解锁项，`get_cost()`将返回`None`。

可以像这样使用它：
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`