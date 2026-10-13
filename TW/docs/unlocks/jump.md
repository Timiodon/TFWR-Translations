[<-煤炭](docs/unlocks/coal.md)
---
# 跳轉

無人機已解鎖 `jump()` 指令。

此指令可以指定某些解鎖項，讓無人機直接跳轉到它們附近。偵錯程式，或者回頭尋找剛剛錯過的礦脈時，這特別有用。使用時，傳入一個解鎖項作為參數，例如 `Unlocks.Iron`。

`jump()` 只能用於出現在地下的解鎖項，例如 `jump(Unlocks.Rice)` 或 `jump(Unlocks.Iron)`。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

跳轉不一定能直接到達目標解鎖項，因此你可能還得在附近找一找；但目標一定就在附近。

每次執行程式只能使用一次 `jump()`。

---

[jump()](functions/jump)
