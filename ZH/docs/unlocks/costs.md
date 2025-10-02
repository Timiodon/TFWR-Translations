# 成本
任何成本都可以表示为一个将物品映射到数字的字典。

`get_cost()` 函数返回的就是这样一个字典：某种植物或某个解锁项的成本。

`get_cost(Entities.Pumpkin)`
返回 `{Items.Carrot:1}`

对于解锁项，若传递可选的第二个参数，则可获取你想要的解锁等级对应的成本。默认情况下为当前的解锁等级。

`get_cost(Unlocks.Loops, 0)`
返回 `{Items.Hay:5}`

对于已经达到最高等级的解锁项，`get_cost()` 将返回 `None`。

使用示例如下：
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
