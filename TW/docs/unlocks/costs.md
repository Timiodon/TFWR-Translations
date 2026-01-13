# 成本
任何成本皆可表示為一個將物品映射到數量的字典。

`get_cost()` 函式會回傳此類字典。它會回傳植物或解鎖項目的成本。

`get_cost(Entities.Pumpkin)`
會回傳 `{Items.Carrot:1}`

對於解鎖項目，你可以傳入第二個可選引數來指定想查詢的解鎖等級。預設為目前的解鎖等級。

`get_cost(Unlocks.Loops, 0)`
會回傳 `{Items.Hay:5}`

對於已達最高等級的解鎖， `get_cost()` 會回傳 `None`。

用法範例：
```
cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]
```