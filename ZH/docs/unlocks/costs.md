# 耗材数量
所有的耗材数量都一个包含物品和数字的字典映射。

`get_cost()` 函数返回的值就是这样的一个字典：某种植物或某个科技树项目的耗材。

调用 `get_cost(Entities.Pumpkin)` 函数
会返回 `{Items.Carrot:1}`

向科技树中的各种项目添加第二个可选参数，就可以获取你想要的解锁等级对应的耗材数量。默认情况下为当前的解锁等级。

调用 `get_cost(Unlocks.Loops, 0)`
会返回 `{Items.Hay:5}`

如果科技树中的某些项目已经到达最高等级，调用 `get_cost()` 函数则返回 `None`。

使用示例如下：
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
