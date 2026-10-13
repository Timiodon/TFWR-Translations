[<- While 迴圈](docs/scripting/while.md) <right>[擴張 1 ->](docs/unlocks/expand_1.md)
<right>[種植 ->](docs/unlocks/plant.md)
---
# 速度升級
現在，無人機的執行速度翻倍了！但是無人機收穫的速度比草生長的速度還快，這會導致根本沒有收成。為了解決這個問題，現在解鎖了 [If 陳述式](docs/scripting/if.md) 分支和 [can_harvest()](functions/can_harvest) 函式。

## 在收穫前檢查
當給定條件為 `True` 時，`if` 陳述式會執行一次其程式碼區塊。

新的 `can_harvest()` 函式提供了一個實用的條件：如果無人機下方的植物可以收穫，它會回傳 `True`，否則回傳 `False`。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

你可以這樣理解回傳值：在判斷 `if` 條件時，函式呼叫運算式 `can_harvest()` 就像被回傳的 `True` 替換了一樣。

上面的程式碼執行時會發生以下過程：
- 執行 `if` 陳述式。
- 呼叫 `can_harvest()`。
- 草已經完全成熟，因此 `can_harvest()` 回傳 `True`。
- 陳述式現在變成 `if True:`。
- 值為 `True`，所以執行分支。

如果草尚未完全成熟，無人機就不會翻轉。

現在我們可以結合 `if` 陳述式和 `can_harvest()`，防止無人機在下方植物未成熟時提前收穫。

---

[If 陳述式](docs/scripting/if.md)      [While 迴圈](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
