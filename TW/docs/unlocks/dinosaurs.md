[<- 仙人掌](docs/unlocks/cactus.md)
---
# 恐龍
恐龍是古老而威風的生物，可以養殖以取得遠古骨頭。

不幸的是，恐龍很久以前就滅絕了，所以我們現在最多只能打扮成恐龍。
為此，你收到了新的恐龍帽。

帽子可以用以下方式裝備：
`change_hat(Hats.Dinosaur_Hat)`

很可惜，它看起來和廣告上的不太一樣……

如果裝備了恐龍帽且有足夠的仙人掌，則會自動購買一顆[蘋果](objects/apple)並將其放置在無人機下方。
當無人機在蘋果上方並再次移動時，便會吃掉蘋果，同時尾巴增長一節。如果你還有足夠的仙人掌，一顆新的蘋果將被購買並放置在一個隨機位置。
如果蘋果想產生的位置已經種植了其他東西，則無法產生。

恐龍的尾巴會拖在無人機後面，填滿無人機之前移動過的地塊。如果無人機試圖移動到尾巴上方，`move()` 將會失敗並回傳 `False`。
在移動過程中，尾巴的最後一節會移開，所以你可以移動到它原來的位置上。但是，如果尾巴填滿了整個農場，你將無法再移動。所以你可以透過檢查是否無法移動來判斷尾巴是否已經長到最大。
戴著恐龍帽時，無人機無法越過農場邊界到達另一邊。

在蘋果上使用 `measure()` 將回傳下一個蘋果的位置，形式為一個元組。

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

當透過裝備不同的帽子再次卸下這頂帽子時，便會收穫尾巴。
你將獲得等於尾巴長度平方數量的骨頭。因此，若尾巴長度為 `n`，則將獲得 `n**2` 根 `Items.Bone`。
例如：
長度 1 => 1 根骨頭
長度 2 => 4 根骨頭
長度 3 => 9 根骨頭
長度 4 => 16 根骨頭
長度 16 => 256 根骨頭
長度 100 => 10000 根骨頭

恐龍帽非常重，所以裝備後會使 `move()` 消耗 400 ticks 而不是 200。然而，每當你撿起一顆蘋果，`move()` 使用的 ticks 數量便會減少 3%（無條件捨去），因為尾巴變長可以幫助移動。

以下迴圈列印出吃掉任意數量蘋果後 `move()` 使用的 ticks 數量：

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
ticks = 400
for i in range(100):
    quick_print("吃掉 ", i, " 顆蘋果後的 ticks: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

你只有一頂恐龍帽，所以只有一架無人機可以佩戴它。

<spoiler=顯示提示 1>如果始終沿著覆蓋整個場地的同一路徑移動，那麼每次都能輕鬆地得到一條覆蓋整個場地的尾巴蛇。雖然效率不高，但確實可行。
完全走訪一個非常大的農場可能需要很長時間，而且你實際上可能並不需要那麼多骨頭。不妨使用 `set_world_size()` 將農場改為更方便覆蓋的大小。</spoiler>

---

[統計資料](docs/stats.md)      [元組](docs/scripting/tuples.md)      [串列](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
