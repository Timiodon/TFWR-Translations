[<-鐵礦](docs/unlocks/iron.md) <right>[蘑菇->](docs/unlocks/mushroom.md)
---
# 石英
沿著 `Grounds.Rock` 中的鐵礦脈繼續向下，在岩石層下部及其下方的硬 `Grounds.Dirt` 中可以找到石英（用[地下感官](docs/unlocks/underground_senses.md)解鎖的 `get_hardness()` 檢查硬度）。

以下程式碼穿過泥土，挖入岩石層。隨後邊挖掘邊持續探勘石英，直到距離小於 2。最後輸出到達位置的探勘距離。
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# 挖到岩石層
while get_ground_type() != Grounds.Rock:
    dig()

# 繼續挖掘，直到接近石英礦脈
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# 輸出最後到礦脈的距離
print(prospect_quartz())
}}

## 礦脈結構
石英礦脈呈針狀，形成垂直柱體，因此很難靠試誤找到。

## 探勘石英
好在我們可以把鐵礦加工成類似探礦杖的東西，更容易找到石英礦脈。對應的指令是 `prospect_quartz()`。

`prospect_quartz()` 的工作方式與 `prospect_iron()` 不同。它不像鐵礦探勘那樣傳回前往最近鐵礦石的方向，而是傳回最近石英地塊與無人機之間的精確三維距離（歐幾里得距離）。

執行 `prospect_quartz()` 指令需消耗 1 份鐵礦，最好省著用。

如果附近沒有石英，或者鐵礦不足以執行探查，`prospect_quartz()` 就會回傳 `None`。

## 策略
<spoiler=顯示提示>可以反覆探勘並移動，觀察距離如何變化。在平面上設法縮短距離，就能到達石英礦脈上方。可以採用類似二分搜尋的策略，減少 `prospect_quartz()` 的呼叫次數和鐵礦消耗。

更複雜的策略可以用二維幾何求兩個或多個圓的交點。也可以挑戰完整的三邊定位，求三個球面的交點，確定礦脈的精確三維位置。

可以用次方運算計算平方根，例如 `16**0.5` 就是 16 的平方根。遊戲沒有內建三角函數或向量運算函數，需要自行實作。

也要注意，附近可能有多條礦脈，因此相鄰位置的多次測量未必指向同一條礦脈。</spoiler>

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [變數](docs/scripting/variables.md)      [運算子](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
