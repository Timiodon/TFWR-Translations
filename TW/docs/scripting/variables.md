[<- 運算子](docs/scripting/operators.md) <right>[串列 ->](docs/scripting/lists.md)
<right>[函式 ->](docs/scripting/functions.md)
---
# 變數
變數是用於存放 1 個值的容器，並且可以自訂變數的名字
`=` 運算子用於宣告 1 個變數並為其儲存 1 個值（指派）。

`variable_name = value`

運算子的左邊是變數名稱，你可以對變數名稱進行自訂。
右邊是一個運算式，其結果值將被儲存在變數中。

宣告 1 個名為 `a` 的變數，並在其中儲存值 `5`：
`a = 5`
宣告 1 個名為 `b` 的變數，並在其中儲存 `can_harvest()` 的回傳值：
`b = can_harvest()`

不要把 `=` 運算子和 `==` 運算子搞混了。
`==` 運算子是判斷兩個值是否相等，並回傳 `True` 或 `False`。
`=` 運算子將右邊的值賦給左邊的名稱。

給變數指派後，就可在程式碼中使用這個變數來代替它包含的值。

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
a = 5
for i in range(a):
	do_a_flip()
}}

上面的迴圈執行了 5 次，因為 `a` 被設定為了 `5`。
`for` 迴圈中的 `i` 也是一個變數，它在迴圈的每次迭代中被自動賦為序列的目前值。（它不一定非要叫 `i`，你可以給它取任何有效的變數名稱。）

變數也讓你能用 while 迴圈做同樣的事情：

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

這和上面的 `for` 迴圈做的是同樣的事情。我們只需要手動遞增 `i`。
注意，要遞增 `i`，我們把它設為它自己的值加上 `1`。根據變數的舊值來改變它的值是十分常見的操作。
這些運算子可以用來簡化過程：`+=, -=, *=, /=, %=`

`i = i + 1` 和 `i += 1` 是一樣的
`a = a / 3` 和 `a /= 3` 是一樣的

---

[運算子](docs/scripting/operators.md)      [While 迴圈](docs/scripting/while.md)      [For 迴圈](docs/scripting/for.md)      [函式](docs/scripting/functions.md)      [名稱作用域](docs/scripting/scopes.md)
