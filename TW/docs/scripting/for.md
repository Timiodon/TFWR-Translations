[<- 擴張 2](docs/unlocks/expand_2.md)
---
# For 迴圈
`for` 迴圈陳述式的執行方式與 Python 中類似。（在某些語言中稱為 foreach 迴圈，但不要與 C 語言風格的 for 迴圈混淆，那是不同的概念）。

`for i in sequence:
	#用 i 做點什麼`

與 `while` 迴圈類似，`for` 迴圈會重複呼叫某個程式碼區塊。但它不是根據條件迴圈的，而是儲存序列中每有 1 個元素就執行 1 次迴圈體。

## 語法
for 迴圈陳述式的格式如下：

`for variable_name in sequence:
	#程式碼區塊`

`variable_name` 可以是你選定的任意名稱。這個變數儲存序列中的目前元素。`sequence` 必須是可迭代的值，例如一段數字範圍。序列中的每個元素都會讓迴圈體執行一次，同時該元素會賦給迴圈變數。

## 序列
[範圍](functions/range)      <unlock=lists>[串列](docs/scripting/lists.md)      </unlock><unlock=functions>[元組](docs/scripting/tuples.md)      </unlock><unlock=dicts>[字典](docs/scripting/dicts.md)      </unlock><unlock=sets>[集合](docs/scripting/sets.md)</unlock>

## 範例
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
for i in range(5):
    harvest()
}}

這個迴圈會固定次數地執行迴圈體，基本上等同於如下程式碼：

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}

---

[While 迴圈](docs/scripting/while.md)      [Break 陳述式](docs/scripting/break.md)      [Continue 陳述式](docs/scripting/continue.md)

[range()](functions/range)
