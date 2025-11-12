# 巨型農場
這個極其強大的解鎖項目讓你能使用多架無人機。

如同以往，你仍然從一架無人機開始。必須先生成額外的無人機，且這些無人機會在程式結束後消失。
每架無人機執行自己的獨立程式。可以使用 `spawn_drone(function)` 生成新無人機。

```
def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)
```

這會在執行 `spawn_drone(function)` 指令的無人機所在位置生成一架新無人機。新無人機隨即開始執行指定的函式。執行完畢後會自動消失。

無人機之間不會互相碰撞。

使用 `max_drones()` 取得同時存在的無人機數量上限。
使用 `num_drones()` 取得農場中已存在的無人機數量。

## 範例：
```
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
```

這會讓你的第一架無人機水平移動並生成更多無人機。被生成的無人機會垂直移動並採收它們路徑上的所有物件。

如果所有可用的無人機都已被生成，`spawn_drone()` 不會有任何操作並直接回傳 `None`。

這是另一個範例，會為每架無人機傳入不同方向：

```
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
```

## 所有無人機皆平等
沒有特別的「主要」無人機。所有無人機都可以生成其他無人機，且都計入無人機數量上限。所有無人機在終止時都會消失。如果第一架無人機較早完成其程式，系統會將畫面上顯示程式執行狀態切換到另一架正在執行的無人機。所有無人機都可以觸發中斷點，當某架無人機觸發中斷點時，程式碼的醒目標示會切換到該無人機。

<spoiler=顯示提示>看看這個超實用的平行 `for_all` 函式，它接受任意函式並在每個農場格子上執行該函式。它會善用所有可用的無人機：

```
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
```

一個特別有用的模式是：如果有可用無人機就生成，否則自己執行。

```
if not spawn_drone(task):
	task()
```
</spoiler>

## 等待另一架無人機
使用 `wait_for(drone)` 函式等待另一架無人機完成。當你生成無人機時會收到該無人機的 `drone` 控制代碼。
`wait_for(drone)` 會回傳該無人機所執行函式的回傳值。

```
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))
```

注意，生成無人機需要時間，所以不建議為每個小事都生成新無人機。

你可以使用 `has_finished(drone)` 在不等待的情況下檢查該無人機是否已完成。

## 無共用記憶體
每架無人機有自己的記憶體，無法直接讀寫其他無人機的全域變數。

```
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
```

上述程式會印出 `0`，因為新無人機只會遞增它自己副本的全域 `x`，並不會影響第一架無人機的 `x`。

## 競態條件
多架無人機可以同時對同一個農場格子操作。如果兩架無人機在同一個時間刻中互動同一格，兩個互動都會發生，但結果可能會依互動順序而不同。

例如，假設無人機 `0` 和 `1` 都在同一棵即將成熟的樹上。
無人機 `0` 呼叫
```
use_item(Items.Fertilizer)
```

無人機 `1` 呼叫
```
harvest()
```

如果兩個操作同時發生，樹會先被施肥再被採收，這種情況會得到木材。但如果無人機 `1` 稍快一些，樹會在被施肥前就被採收，則不會獲得木材。
這種情況稱為「競態條件」，在平行程式設計中很常見，結果會依操作發生的順序而異。

另一個可能的問題情境是多架無人機在相同位置同時執行相同程式碼：
```
if get_water() < 0.5:
    use_item(Items.Water)
```

如果多架無人機同時執行，皆會通過第一行的檢查並進入 `if` 區塊，接著都會使用水，造成大量浪費。
當某架無人機執行到第二行時，`get_water()` 可能已不再小於 `0.5`，因為其他無人機已在此期間澆水。