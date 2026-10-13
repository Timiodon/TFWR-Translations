[<- 成本](docs/unlocks/costs.md)
---
# 自動解鎖
你可以呼叫 `unlock()` 函式使科技樹中的項目進行自動解鎖，這可以實現完全自動化，解放雙手！
例如，你可以呼叫 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 函式來解鎖速度和擴張土地。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 300}, {"item": "wood", "n": 100000}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(6):
    harvest()
    unlock(Unlocks.Grass)
}}

對科技樹中的項目使用 `get_cost()` 函式，就可以取得該項目解鎖或者升級所需的耗材數量，就像對植物或物品使用函式那樣。
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "loops"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops))
}}

---

[成本](docs/unlocks/costs.md)      [字典](docs/scripting/dicts.md)      [If 陳述式](docs/scripting/if.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
