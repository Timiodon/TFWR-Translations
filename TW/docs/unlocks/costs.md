[<- 字典](docs/scripting/dicts.md) <right>[自動解鎖 ->](docs/unlocks/auto_unlock.md)
---
# 成本
所有成本都可以用一個將物品對應到數量的字典表示。

`get_cost()` 函式回傳的值就是這樣的一個字典：某種植物或某個科技樹項目的耗材。

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Entities.Pumpkin))
}}

向科技樹中的各種項目新增第二個可選參數，就可以取得你想要的解鎖等級對應的耗材數量。預設情況下為目前的解鎖等級。

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops, 0))
print(get_cost(Unlocks.Loops, 1))
}}

如果科技樹中的某些項目已經到達最高等級，呼叫 `get_cost()` 函式則回傳一個空字典。

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
cost = get_cost(Entities.Carrot)
for item in cost:
	if num_items(item) < cost[item]:
		print("缺少", cost[item] - num_items(item), item)
}}

---

[字典](docs/scripting/dicts.md)      [自動解鎖](docs/unlocks/auto_unlock.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
