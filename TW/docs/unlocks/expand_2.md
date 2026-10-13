[<- 擴張 1](docs/unlocks/expand_1.md)
---
# 擴張 2
你的農場又擴張了！現在地塊不再是整齊的一行，所以你需要想辦法走訪整個方形網格。

在使用 `while` 迴圈的情況下，若尚未解鎖感官和運算子，則無法實現這一點。
那麼是時候介紹 `for` 迴圈了。

在 [For 迴圈](docs/scripting/for.md)頁面上可以閱讀所有有關 `for` 迴圈的內容，但目前你只需要用它在固定的次數來重複執行程式碼。

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
#CODE
for i in range(5):
	do_a_flip()
}}

`range(n)` 表示一個從 `0` 到 `n - 1` 的數字範圍，其中包含 `n` 個元素。`for` 迴圈對序列中的每個元素執行一次迴圈體。在這個例子中，`do_a_flip()` 將被呼叫 `5` 次。

現在也可以使用 `get_world_size()` 函式了。它會回傳你的農場的邊長，即使下次繼續擴張你的土地，你所編寫的程式碼也不會失效。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

在此範例中，無論農場多大，無人機都會收穫農場第一列的每一個格子。

如果想不出來該如何讓你的無人機飛遍整個農場，請看下面的提示。
<spoiler=顯示提示>當然，有多種方法都可以走訪農場。
我們要找的是一種普遍性的走訪方法，確保程式碼在農場再次擴大時不會失效。
如果想讓你的無人機飛遍整個農場，其中一種普遍性的方法就是永遠重複以下兩個步驟：

1.向 `North` 移動，直到繞回原點。
2.向 `East` 移動。

`for i in range(get_world_size()):` 可能有助於將這個想法轉化為程式碼。
</spoiler>
<spoiler=顯示可能的解決方案>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#在每個地塊上翻轉一次
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[For 迴圈](docs/scripting/for.md)      [While 迴圈](docs/scripting/while.md)      [變數](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
