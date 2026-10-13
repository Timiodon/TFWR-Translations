[<- 速度升級](docs/unlocks/speed.md) <right>[擴張 2 ->](docs/unlocks/expand_2.md)
<right>[採礦 ->](docs/unlocks/mining.md)
---
# 擴張 1
你的農場變大了！無人機現在可以移動了，呼叫新的函式 `move()` 來移動無人機。`move()` 可以指定無人機移動的方向，為此還引入了四個新的常數：`North, East, South, West`，分別是「向上」、「向右」、「向下」和「向左」。


例如，`move(North)` 會將無人機向上移動 1 格。

如果超過農場邊緣，無人機會繞回另一邊。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
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
while True:
	move(North)
}}

---

[While 迴圈](docs/scripting/while.md)      [運算子](docs/scripting/operators.md)      [擴張 2](docs/unlocks/expand_2.md)

[move()](functions/move)
