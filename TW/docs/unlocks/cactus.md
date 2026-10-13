[<- 南瓜](docs/unlocks/pumpkins.md) <right>[恐龍 ->](docs/unlocks/dinosaurs.md)
---
# 仙人掌
像其他植物一樣，[仙人掌](objects/cactus)可以種植在耕過的土地上並收穫。

然而，仙人掌大小不一，並有一種奇怪的秩序感。

如果收穫一株完全成熟的仙人掌，並且所有相鄰的仙人掌都已排序，則所有相鄰的仙人掌也會以遞迴方式收穫。

如果所有 `North`(上邊) 和 `East`(右邊) 方向的相鄰仙人掌都完全成熟且尺寸大於或等於自身，並且所有 `South`(下邊) 和 `West`(左邊) 方向的相鄰仙人掌都完全成熟且尺寸小於或等於自身，那麼這個仙人掌就被認為是處於已排序狀態。

當所有相鄰的仙人掌都完全成熟並處於已排序狀態時，可以觸發「連鎖收集」。
也就是說，如果一個方形區域的成熟仙人掌已經按大小排序，那麼收穫其中一株仙人掌時，會收穫整個方形區域。

一株完全成熟的仙人掌如果未排序，會顯示為棕色。一旦排序好，則會變回綠色。

你將獲得的仙人掌數量等於所收穫仙人掌數量的平方。因此，如果同時收穫 `n` 個仙人掌，則將獲得 `n**2` 個 `Items.Cactus`。

仙人掌的大小可以呼叫 `measure()` 函式取得。
取得的結果始終為以下數字之一：`0,1,2,3,4,5,6,7,8,9`。

你也可以向 `measure(direction)` 函式傳入 1 個方向參數來取得無人機對應方向上的相鄰地塊的仙人掌大小。

呼叫 `swap()` 函式可將 1 株仙人掌與其任何方向的鄰居交換位置。
`swap(direction)` 將無人機下方的物體與無人機 `direction` 方向 1 格處的物體交換位置。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "pumpkin", "n": 32}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## 數字範例
在這些網格中，所有的仙人掌都處於已排序狀態，可以連鎖收穫整片田地：
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

在下面網格中，只有左下角的仙人掌處於已排序狀態，這還無法觸發「連鎖收集」：
`1 5 3
4 9 7
3 3 2`

<spoiler=顯示提示 1>
如果行已經排序，對列進行排序時，不會打亂行的順序。
</spoiler>
<spoiler=顯示提示 2>
如果不熟悉排序演算法，不妨上網搜尋，看看有哪些演算法可以解決這個問題。當然，並不是所有演算法都有效，因為你只能交換相鄰的仙人掌。
</spoiler>
<spoiler=顯示提示 3>
「氣泡排序」或許是最簡單的排序演算法。它的做法是反覆走訪元素，將順序不對的相鄰元素交換，直到所有元素都排好序。

下面是用仙人掌演示的效果：
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
當然，這個策略還有很多改進空間！
當你成功排好一整行後，就可以利用提示 1 來對整片田地排序。
</spoiler>

---

[統計資料](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
