[<- 第一個程式](docs/first_program.md) <right>[速度升級 ->](docs/unlocks/speed.md)
---
# While 迴圈
你已經解鎖了 `while` 迴圈和 `True`、`False` 這兩個值。`while` 迴圈會在條件為 `True` 的情況下一直執行迴圈體。

`while 條件:
	#迴圈體`

不用擔心建立無限迴圈。無人機可能會卡住，但整個遊戲不會當掉。只要停止執行中的程式，就能再試一次。

## 面向初學者
也許你已經試過連續寫好幾個 `harvest()` 函式：

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
這樣，你只需執行一次程式，即可收穫多次。
然而，如果能收穫超過 3 次就更好了，而多次出現重複程式碼會很快讓程式變得雜亂。
解決方法是使用迴圈。
迴圈能讓你多次執行相同的程式碼。

while 迴圈需要 1 個條件來判斷，條件比較的結果為邏輯值，只能是兩種狀態之一：`True` 或 `False`。
這樣的值被稱為布林值。

然後迴圈就會執行迴圈內的程式碼，直到條件變為 False。
while 迴圈的形式如下：

`while 條件:
	#迴圈體
	#迴圈體
	#...`

你需要將「條件」換成布林值，將 `#迴圈體` 換成迴圈中想做的事情。

有 2 個可用的常數布林值。常數是在程式執行期間永遠不會改變的值。

要建立布林常數，只需寫 `True` 或 `False`。
所以你可以寫

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
或者

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
第一個永遠不會翻轉，第二個會永遠重複翻轉（一個無限迴圈）。

建立無限迴圈通常不是個好主意，因為會導致程式卡死，但在這款遊戲中，迴圈的每次迭代之間都有延遲，所以它只會讓無人機一直翻轉，直到你再次按下執行按鈕手動讓它停下。

注意冒號後面的行是如何縮排的。這樣的縮排是用來分隔程式碼區塊的。
按 Tab 鍵即可新增縮排，按 Shift + Tab（或 Backspace）即可移除縮排。選取多行時，Tab 和 Shift + Tab 會對所有選取行生效。

注意：如果透過 Steam 遊玩，按 Shift + Tab 會開啟 Steam 介面。你可以在遊戲選項中重新綁定取消縮排快速鍵，或在 Steam 設定中更改介面快速鍵。

這裡，`do_a_flip()` 和 `pet_the_piggy()` 位於縮排的 `while` 程式碼區塊中，因此會被反覆呼叫。而 `harvest()` 在程式碼區塊之後，永遠不會執行。
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[For 迴圈](docs/scripting/for.md)      [If 陳述式](docs/scripting/if.md)      [Break 陳述式](docs/scripting/break.md)      [Continue 陳述式](docs/scripting/continue.md)      [外部編輯器](docs/external_editor.md)
