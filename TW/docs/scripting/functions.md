[<- 變數](docs/scripting/variables.md) <right>[匯入 ->](docs/scripting/import.md)
---
# 函式
使用 `def` 關鍵字來自訂一個新的函式：
`def f(arg1, arg2 = False):
	#函式程式碼`

使用 `()` 來呼叫某個函式：
`f(42)`

另請參閱[作用域](docs/scripting/scopes.md)來了解函式中的區域變數和全域變數。

## 介紹
你已經見過像 `harvest()` 這樣的內建函式。
你也可以自訂函式，從而以模組化的方式組織你的程式碼。簡單來說，你可以給一個程式碼區塊命名，之後可以從任何地方呼叫該程式碼區塊。

## 函式定義
例如，你可以定義一個多次移動無人機的函式。

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

`def` 關鍵字表示這定義了一個函式。
`move_n_dir` 是函式綁定的名稱。這是你自訂的變數名稱，用於呼叫該函式。
`n` 和 `dir` 是形式參數，用來接收傳入函式的值的變數，這些值也稱為引數。你可以根據需要定義多個（沒有數量限制）向函式傳入的形式參數。
`:` 後面是函式被呼叫時將執行的程式碼區塊。

根據上述定義，以下程式碼將無人機向 `North` 移動 `2` 格，向 `East` 移動 `2` 格。

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

看到 `def function():` 時，應該把它想像成一個這樣的變數指派：
`function = create_new_function_object()`
和其他指派一樣，在沒有給變數賦初值時，無法使用該變數！
`def` 陳述式必須在任何函式呼叫之前執行。
這段程式碼會拋出一個錯誤：

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
func()
def func():
	pass
}}

## 回傳值
使用 `return` 關鍵字可以讓函式回傳 1 個值。
例如，以下函式定義了異或運算。如果一個值為 `True` 而另一個為 `False`，異或運算回傳 `True`：

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[元組](docs/scripting/tuples.md)可以回傳多個值。

## 預設參數
你還可以新增預設值，在沒有傳遞參數的情況下，會使用預設值。

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

有預設值的參數後面不能跟沒有預設值的參數。

## 進階函式用法
和其他的值一樣，函式也是值，而 `def` 陳述式就像一個指派陳述式，將函式賦給你自訂的名稱。
因此，你可以這麼做：

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

這裡 `f()` 呼叫函式 `f`，它會定義並回傳一個新函式 `d`。第二個 `()` 則執行回傳的函式，並讓無人機翻轉。
(這種寫法不建議，因為很難看出這個函式到底在做什麼操作。)

將其他函式作為參數的函式可以讓你寫出很有創意的程式碼：

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
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
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[變數](docs/scripting/variables.md)      [名稱作用域](docs/scripting/scopes.md)      [元組](docs/scripting/tuples.md)      [匯入](docs/scripting/import.md)
