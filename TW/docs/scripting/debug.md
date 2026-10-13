[<- 種植](docs/unlocks/plant.md) <right>[偵錯 2 ->](docs/unlocks/debug2.md)
<right>[計時 ->](docs/unlocks/timing.md)
---
# 偵錯
有時候程式碼會無法正常執行，而你需要找出原因。有幾個工具可以在這方面派上用場。

第一個是逐步執行程式。
你可以使用執行按鈕旁邊的按鈕或設定斷點來進入逐步模式。

按一下程式碼左側區域可以新增斷點。
![|x227](Breakpoints)
當程式碼執行到斷點所在的行時，會自動切換到逐步模式。

將滑鼠移到某個變數上時，會顯示它目前的值。

`print()` 函式也非常有用。它會將傳遞給它的所有值直接列印到空中，形成文字狀的雲朵效果。

範例：

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

`print()` 函式會將值直接列印到空中和[輸出](docs/output.md)頁面。

如果你想列印大量的值，在空中書寫有時可能會有點慢。
在這種情況下，可以呼叫 `quick_print()` 函式，只列印到輸出視窗。

輸出視窗還會記錄警告和錯誤，所以如果執行結果有哪裡與預期不符，不妨檢查一下輸出視窗。

當程式停止執行時，輸出也會被寫入遊戲資料夾中的 [output.txt](persistent_data_path/output.txt) 檔案。

---

[輸出](docs/output.md)      [註解](docs/scripting/comments.md)      [偵錯 2](docs/unlocks/debug2.md)      [彩色地塊](docs/unlocks/debug_place.md)      [模擬](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
