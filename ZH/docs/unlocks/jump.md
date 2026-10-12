[<-煤炭](docs/unlocks/coal.md)
---
# 跳转

无人机已解锁 `jump()` 命令。

此命令可以指定某些解锁项，让无人机直接跳转到它们附近。调试程序，或者回头寻找刚刚错过的矿脉时，这特别有用。使用时，传入一个解锁项作为参数，例如 `Unlocks.Iron`。

`jump()` 只能用于出现在地下的解锁项，例如 `jump(Unlocks.Rice)` 或 `jump(Unlocks.Iron)`。

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

跳转不一定能直接到达目标解锁项，因此你可能还得在附近找一找；但目标一定就在附近。

每次执行程序只能使用一次 `jump()`。

---

[jump()](functions/jump)
