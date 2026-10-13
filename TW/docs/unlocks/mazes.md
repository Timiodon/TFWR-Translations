[<- 肥料](docs/unlocks/fertilizer.md) <right>[巨型農場 ->](docs/unlocks/megafarm.md)
---
# 迷宮
`Items.Weird_Substance` 對灌木有奇怪的效果。如果在無人機位於灌木上方時呼叫 `use_item(Items.Weird_Substance, amount)`，灌木將長成一個樹籬迷宮。
迷宮的大小取決於使用的 `Items.Weird_Substance` 的數量（`use_item()` 呼叫的第二個參數）。
未升級迷宮時，使用 `n` 份 `Items.Weird_Substance` 將產生一個 `n`x`n` 的迷宮。每次迷宮升級都會使寶藏中的金幣數量翻倍，但所需的 `Items.Weird_Substance` 數量也會隨之翻倍。
所以若要產生一個全場迷宮：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


出於某種原因，無人機無法飛過樹籬，盡管樹籬看起來並沒有那麼高。

樹籬中隱藏著一份寶藏。對寶藏使用 `harvest()` 可以獲得等於迷宮面積的金幣。（例如，一個 5x5 的迷宮將產出 25 份金幣。）

如果在其他任何地方使用 `harvest()`，迷宮將直接消失。

如果無人機在寶藏上方，則 `get_entity_type()` 等於 `Entities.Treasure`，在迷宮的其他地方則等於 `Entities.Hedge`。

除非重複使用迷宮（關於如何重複使用迷宮，請見下文），否則迷宮不包含任何迴圈。因此，無人機不可能在不回頭的情況下再次到達相同的位置。

你可以透過嘗試穿過牆壁來檢查是否有牆。
`move()` 如果成功則回傳 `True`，否則回傳 `False`。

`can_move()` 可以用來在不移動的情況下檢查是否有牆。

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
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

如果不知道如何到達寶藏所在處，請看提示 1，其中說明了如何處理這樣的問題。

在迷宮中的任何地方使用 `measure()` 都會回傳寶藏的位置。
`x, y = measure()`

為了增加挑戰，你也可以透過在寶藏上再次使用相同數量的 `Items.Weird_Substance` 來重複使用迷宮。
這將收集寶藏，並在迷宮中的一個隨機位置產生一個新的寶藏。

每次寶藏被移動時，迷宮中的一些牆壁可能會被隨機移除。所以重複使用的迷宮可能包含迴圈。

請注意，迷宮中的迴圈會顯著提升難度，因為迴圈意味著你可以在不回頭的情況下再次到達相同的位置。
重複使用迷宮得到的金幣也並不會比直接收穫並產生一個新迷宮更多。
這百分百是一個可以直接跳過的額外挑戰。
只有當額外的資訊和捷徑能幫助你更快地破解迷宮時，才值得重複使用迷宮。

寶藏最多可以被重新定位 300 次。之後，在寶藏上使用奇異物質將不再增加其中的金幣，並且它將不再移動。

<spoiler=顯示提示 1>以下是解決這個問題的一種通用方法：

建立一個迷宮，並想像你是無人機。

思考一下如果你在迷宮中會如何嘗試找到寶藏。

一步步寫下你的策略，清晰到可以讓其他人不加思考地照辦。

現在嘗試將你的步驟翻譯成程式碼。
</spoiler>
<spoiler=顯示提示 2>只要沒有迴圈，所有牆壁就會形成一面相互連接的大牆。只要把左手貼在牆上並沿牆前進，就能走遍整個迷宮。
這種方法需要編寫的程式碼很少，而且不必記錄已經去過的地方。大約 10 行程式碼就足夠了。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=顯示提示 3>與其讓無人機朝東西南北這樣的絕對方向移動，朝相對方向（如「右轉」或「左轉」）移動可能更加實用。為此，你需要記錄無人機目前移動的方向。無人機實際上從不旋轉，但你仍然可以在程式碼中保持「虛擬」的旋轉。
下面的索引技巧對此很有幫助：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#右轉
index = (index + 1) % 4
move(directions[index])

#左轉
index = (index - 1) % 4
move(directions[index])
}}

使用 `% 4` 可讓方向在一個迴圈中輪轉。例如，`3 (West) + 1` 又回到了 `0 (North)`，因為 `4 % 4 == 0`，而且 `-1 % 4 == 3`。</spoiler>
<spoiler=顯示提示 4>如果無法破解也不必為難自己，你始終可以選擇效率更低的方式。
破解一個 `1`x`1` 的迷宮總歸是小菜一碟。</spoiler>

---

[統計資料](docs/stats.md)      [串列](docs/scripting/lists.md)      [字典](docs/scripting/dicts.md)      [元組](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
