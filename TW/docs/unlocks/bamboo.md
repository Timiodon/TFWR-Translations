[<-水稻](docs/unlocks/rice.md) <right>[彩色地塊->](docs/unlocks/debug_place.md)
<right>[金字塔->](docs/unlocks/pyramid.md)
---
# 竹子
竹子是一種向上生長的植物。無人機需要定期摘除它的棕色果實，才能讓它繼續生長。新解鎖的 `hover` 指令可以幫我們做到這點。

竹子必須種在耕過的土壤（`Grounds.Soil`）上，種植需要消耗水稻。

以下程式碼種下竹子，並等待它長到第一個果實出現。
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # 移開，讓竹子繼續生長
}}

## 果實
竹子每秒長高 1 個地塊。

竹子每長幾格就會結出果實。這時竹子會停止生長，需要讓無人機飛入竹子破壞果實。竹子可以一直向上生長，直到結出第三個果實；此後即使摘除果實，也不會再長高。

要摘除果實，先用 `hover` 到達正確高度。接著用 `move` 飛入果實將其摘除，再用 `move` 移開，讓竹子繼續生長。

使用 `measure()` 測量竹子，可以查看下一個果實出現的高度。`measure()` 從 `0` 開始計數，因此 `hover(measure())` 會將無人機帶到果實所在的高度。

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # 懸停到果實旁邊的高度

move(East) # 移開並等待竹子生長
for i in range(3):
    do_a_flip()

move(West) # 摘除果實
move(East) # 再次移開
}}

## 懸停
`hover` 指令接受一個引數：懸停高度，數值為 `0` 到 `18`。無人機的預設懸停高度為 `1`。`hover` 不能向下進入實心實體內部。因此，如果無人機已位於竹子上方，就不能透過 `hover(0)` 進入竹子。

無人機成功到達指定高度時，`hover` 傳回 `True`，否則傳回 `False`。

此外，`get_hover` 指令可以傳回無人機目前的懸停高度。

懸停時使用 `dig`、`harvest` 或 `plant`，無人機會恢復預設懸停高度（`1`）。

最後，懸停高度不會影響 `get_pos_z()`。它始終傳回無人機下方地塊的 z 座標。

## 收穫竹子
雖然可以使用 `harvest()`，但建議將懸停高度設為 `0`（`hover(0)`），再讓無人機飛入竹子來收穫。這樣就能一次收穫整株竹子。

若想保留竹子，可以在任意高度用 `move` 飛入竹子，例如先呼叫 `hover(3)`。這會收穫該高度及以上的所有竹節，但竹子仍然存活。以這種方式部分收穫的竹子會重新長出果實，因此你還需要再次摘除。

無論採用哪種方式，產量都等於被破壞竹節數量的平方，因此竹子越高，產量越好。

---

[統計資料](docs/stats.md)      [For 迴圈](docs/scripting/for.md)      [變數](docs/scripting/variables.md)      [If 陳述式](docs/scripting/if.md)      [函式](docs/scripting/functions.md)      [水稻](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
