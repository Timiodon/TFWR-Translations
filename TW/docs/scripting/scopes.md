[<- 函式](docs/scripting/functions.md)
---
# 名稱作用域
作用域決定了哪些變數可以從哪裡存取。簡單來說，作用域就是一個從名稱到值的對應。
其工作方式與 Python 中的基本相同。

首先存在 1 個全域作用域，其次每個函式都有 1 個區域作用域。
當定義一個變數時，它會被新增到目前作用域。
函式定義之外的所有內容被視為全域作用域的一部分。

`x = 1`
在全域作用域中將值 `1` 賦給名稱 `x`。

以下 `def` 陳述式在全域作用域中將一個函式賦給名稱 `f`。
`def f():
    `在 `f` 的區域作用域中將值 `1` 賦給名稱 `y`。`
    y = 1

    `在 `f` 的區域作用域中將一個函式賦給名稱 `g`。`
    def g():
        pass`

`f()`
從全域作用域中擷取儲存在 `f` 中的函式並呼叫它。

`print(y)`
這個在全域作用域中的 `print` 陳述式會拋出一個錯誤，因為 `y` 從未在全域作用域中宣告，所以無法在這裡讀取它。
它只存在於 `f` 的區域作用域中。

## global 關鍵字
預設情況下，函式中的所有變數都綁定到區域作用域，即使全域作用域中存在同名變數。

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
x = 0

def f():
    x = 1
f()
print(x)
}}

這段程式碼會列印 `0`，因為 `f` 內部的區域 `x` 與全域 `x` 不是同一個變數，所以全域 `x` 保持不變。這一點很重要，否則函式呼叫可能會意外覆蓋一個恰好與該函式區域變數同名的全域變數。

如果想寫入一個全域變數，則必須使用 `global` 關鍵字來明確表示。

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
x = 0

def f():
    global x
    x = 1
f()
print(x)
}}

在這個例子中，`global x` 將 `x` 綁定到上面定義的全域變數 `x`。現在列印的會是 `1`。
注意，改變全域變數通常是走向面條式程式碼（難以維護的程式碼）的第一步，導致程式的每個部分都會影響其他所有部分，所以請勿過度使用。

## 迴圈和分支
迴圈和分支不會建立自己的作用域，因此，在其內部宣告的一切都仍然可以在外部使用。

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
for i in range(3):
    pass
print(i)
}}

這將列印 `2`，因為 `for` 迴圈的最後一次迭代將 `2` 賦給了 `i`。

---

[變數](docs/scripting/variables.md)      [函式](docs/scripting/functions.md)      [匯入](docs/scripting/import.md)      [巨型農場](docs/unlocks/megafarm.md)
