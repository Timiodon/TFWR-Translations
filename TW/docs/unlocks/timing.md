[<- 偵錯](docs/scripting/debug.md) <right>[模擬 ->](docs/unlocks/simulation.md)
---
# 計時
如果想要進一步最佳化你的方案，你需要了解這款遊戲中時間的計量方式，也就是這個科技樹的內容。

## 新函式
如果要考慮事情花費的時間，有兩個函式可用：

呼叫 `get_time()` 函式會回傳從遊戲開始以來的時間，單位是秒。

呼叫 `get_tick_count()` 函式會回傳該程式從開始到結束時所佔用的 tick 數。

這兩個函式以及 `quick_print()` 函式不佔用 tick，甚至連呼叫它們的操作也不佔用 tick。

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
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
}}

## 執行時詳情

### 注意
這是我們為這款遊戲制定的一個易於理解且一致的計時模型，這與現實世界中的執行方式是不一樣的。
你可能只有在想要極致最佳化程式碼時才會關心這個。


程式碼執行的基本時間單位稱為「tick」。在沒有速度升級和能量的情況下，每秒執行 `400` 個 tick。

通常，組合兩個值的操作（例如 `+, -, *, /, //, %, and, or, ...`）佔用 1 tick 來執行。
單值 `-` 和 `not` 是不佔用 tick 的。
單個 `if` 分支佔用 1 tick 來執行（不包括計算條件運算式所需的時間）。
函式呼叫以及變數的讀取和寫入不佔用 tick ，但函式的定義將佔用 1 tick。
`import` 不佔用 tick。
使用 `.` 運算子存取匯入的模組不佔用 tick。
如果一個函式或模組是透過參數或變數指派傳遞的，則使用時將佔用 1 tick 而非不佔用 tick。
`for` 和 `while` 迴圈開始時佔用 1 tick，但迭代自身不佔用 tick（不包含條件或者序列運算式所佔用的 tick ）。
`return`、`break` 和 `continue` 都不佔用 tick。
`pass` 佔用 1 tick，所以它可以用來創造精確的延遲。
使用索引運算子對資料結構進行索引佔用 1 tick，而在涉及字典或集合的情況下，還需要根據鍵的大小佔用額外的 tick。

執行內建函式所佔用的 tick 在每個函式的說明文件中都有單獨說明。

---

[偵錯](docs/scripting/debug.md)      [模擬](docs/unlocks/simulation.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_time()](functions/get_time)      [get_tick_count()](functions/get_tick_count)      [quick_print()](functions/quick_print)
