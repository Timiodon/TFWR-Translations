[<- 迷宮](docs/unlocks/mazes.md)
---
# 巨型農場
這個極其強大的解鎖項讓你能夠使用多架無人機。

{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

和以前一樣，一開始只有一架無人機。額外的無人機必須先被產生，且程式終止後便會消失。
每架無人機執行的都是自己獨立的程式。新無人機可以使用 `spawn_drone(function)` 函式產生。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

以上程式碼會在執行 `spawn_drone(function)` 指令的無人機所在位置產生一架新的無人機。新無人機隨後開始執行指定的函式，完成後便會自動消失。

無人機之間不會相互碰撞。

使用 `max_drones()` 取得可同時存在的無人機數量上限。
使用 `num_drones()` 取得農場上已有的無人機數量。


## 範例
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

這段程式碼會讓你的第一架無人機水平移動，並產生更多的無人機。產生的無人機將垂直移動並收穫其路徑上的一切資源。

如果產生的無人機數量已達上限，`spawn_drone()` 將什麼也不做並回傳 `None`。

以下是另一個為每架無人機傳遞不同方向的範例。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## 所有無人機都一樣
沒有所謂的「主」無人機。所有無人機都可以產生其他無人機，且都計入無人機數量上限。所有無人機在終止時都會消失。如果第一架無人機提前完成程式，另一架無人機將成為透過程式碼醒目顯示其執行過程的無人機。所有無人機都可以觸發斷點，當一架無人機觸發斷點時，程式碼醒目顯示會切換到該無人機。

<spoiler=顯示提示>這個並行 `for_all` 函式超級實用，可接受任何函式並在每個農場地塊上執行。它會利用所有可用的無人機來做到這一點。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
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
}}

一個特別有用的模式是，如果有可用的無人機就產生一架，沒有就自己執行。

`if not spawn_drone(task):
	task()`
</spoiler>

## 等待另一架無人機
使用 `wait_for(drone)` 函式來等待另一架無人機完成。你在產生無人機時會收到 `drone` 控制代碼。
`wait_for(drone)` 回傳另一架無人機正在執行的函式的回傳值。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
move(East)
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

請注意，產生無人機需要時間，所以不建議為每件小事都產生一架新的無人機。

你可以用 `has_finished(drone)` 來看看無人機是不是已經完成了，不用等。

## 無共享記憶體
每架無人機都有自己的記憶體，不能直接讀取或寫入另一架無人機的全域變數。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

這段程式碼將列印 `0`，因為新的無人機增加了它自己的全域 `x` 副本的值，但不影響第一架無人機的 `x`。

## 傳遞參數

`spawn_drone()` 還接受可選的額外參數，並會將它們傳遞給呼叫的函式：

注意，無共享記憶體規則仍然適用。這意味著被呼叫的函式處理的是參數的副本：

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def modify(list):
	list.append('綠色')
	print(list)

l = ['紅色']
wait_for(spawn_drone(modify, l))
print(l)
}}

## 競態條件
多架無人機可以同時與同一個農場地塊交互。如果兩架無人機在同一個 tick 內與同一個地塊交互，兩個交互都會發生，但結果可能會因交互的順序而異。

例如，想像無人機 `0` 和 `1` 都在同一棵即將完全成熟的樹上方。
無人機 `0` 呼叫
`use_item(Items.Fertilizer)`
無人機 `1` 呼叫
`harvest()`

如果兩個操作同時發生，樹將先被施肥再被收穫。在這種情況下，你將從中獲得木材。但是，如果無人機 `1` 稍微快一點，就會在給樹施肥前執行收穫，也因此不會得到木材。
這就是所謂的「競態條件」，屬於並行程式設計中的一個常見問題，結果取決於操作執行的順序。

多架無人機同時在同一位置執行相同程式碼時，還有可能發生以下問題。
`if get_water() < 0.5:
    use_item(Items.Water)`

如果多架無人機同時執行這段程式碼，則會都執行第一行，從而進入 `if` 塊，接著又都會使用水，導致浪費大量的水。
當一架無人機執行到第二行時，`get_water()` 可能不再小於 `0.5`，因為另一架無人機在此期間已經給地塊澆了水。

---

[函式](docs/scripting/functions.md)      [名稱作用域](docs/scripting/scopes.md)      [模擬](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
