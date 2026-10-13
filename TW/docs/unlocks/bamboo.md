[<-水稻](docs/unlocks/rice.md) <right>[彩色地塊->](docs/unlocks/debug_place.md)
<right>[金字塔->](docs/unlocks/pyramid.md)
---
# 竹子

竹子是一種最高可長到 6 個地塊的植物。如果上方有無人機，它就不會生長。因此，使用 `plant(Entities.Bamboo)` 後，記得用 `move` 移開無人機。種植竹子需要消耗水稻。

竹子長到隨機高度時會開花。使用 `measure()` 檢視開花高度。`measure()` 從 0 開始計數，因此竹子在第二個地塊開花時，`measure()` 會回傳 1：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
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
print(measure())
move(East)
}}

當無人機正好位於竹花上方時呼叫 `harvest()`，竹子的產量最高。每偏離一個地塊，產量就會變成原來的八分之一。
例如，如果開花高度為 3，而你在其上方兩個地塊的位置收穫，產量就會變成原來的六十四分之一。

要收穫更高處的竹花，先讓無人機升到所需高度，再從側面飛入竹子。新解鎖的 `place()` 指令能幫上忙。

用 `place(Grounds.Dirt)` 在竹子旁邊堆疊地塊，爬到高處。然後用 `move()` 從側面飛入竹子。呼叫 `harvest()` 時，無人機應正好位於竹花上方。

`place(Grounds.Dirt)` 會消耗 1 個地塊！你也可以放置 `Grounds.Rock` 等其他地塊，但不能放置 `Grounds.Clay` 這樣的特殊地塊。

竹子每秒長高 1 個地塊。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
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
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # 稍等片刻
do_a_flip()
move(West)
harvest()
}}

---

[統計資料](docs/stats.md)      [For 迴圈](docs/scripting/for.md)      [變數](docs/scripting/variables.md)      [If 陳述式](docs/scripting/if.md)      [函式](docs/scripting/functions.md)      [水稻](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
