[<-鐵礦](docs/unlocks/iron.md)
---
# 藏寶圖
傳說有位早已離世的健忘海盜將一份寶藏藏了起來——大概是這麼回事吧。如果他把通往寶藏的路徑畫在地圖上，後來又弄丟了呢？也許他被熔岩河逼到絕境時弄掉了地圖，地圖便埋藏在一層玄武岩下。

測量玄武岩地塊或許能發現線索！

<spoiler=告訴我更多>
留意一層 `Grounds.Basalt`。試著測量玄武岩，看看能發現什麼。線索或許會引你找到藏寶圖；測量藏寶圖一定能得到通往寶藏的路徑——但你能解讀地圖給出的指示嗎？
</spoiler>

<spoiler=直接告訴我怎麼做>
好吧，方法是這樣的：找到 `Grounds.Basalt` 層，以及正下方的 `Grounds.Treasure_Map` 地塊。你可以對玄武岩使用 `measure()`，得到下方地圖地塊的 `(x, y)` 座標。

在地圖地塊上呼叫 `measure()`，就能得到一串表示寶藏路徑的方向字母。N、E、S、W 分別代表 `North`、`East`、`South`、`West`；D 代表「向下」或「挖掘」。這些字母描述了由 `Grounds.Treasure_Path` 地塊組成、通向寶藏的路徑。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# 尋找玄武岩層
while get_ground_type() != Grounds.Basalt:
    dig()

# 測量玄武岩會傳回藏寶圖的位置
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# 找到地圖，測量以取得路徑
do_a_flip()
instructions = measure()
print("指示： ", instructions)

# 挖入地圖，開始尋寶
dig()
}}

可以對字串使用 `for` 迴圈，逐個字母處理：
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# 地圖指示以一個字串傳回
instructions = measure()
# 用 for-in 將字串逐字處理
for letter in instructions:
    print(letter)
}}

它必須一直待在 `Grounds.Treasure_Path` 地塊上方。如果移動到其他地塊，路徑就會斷開，寶藏也會遺失。

## 終點
路徑盡頭是一個 `Grounds.Treasure_Goal` 地塊。如果無人機沒有偏離路徑，其上方就會出現 `Entities.Underground_Treasure`。無人機可以使用 `harvest()` 收穫寶箱，獲得黃金。

## 獎勵
黃金數量與寶藏路徑的長度成正比。升級藏寶圖解鎖項會增加路徑的深度，升級擴張則能讓路徑有更多橫向延伸的空間。兩種升級都會延長寶藏路徑，讓你找到更多黃金。

## 多架無人機
挖入藏寶圖地塊的無人機必須親自找到寶藏，而且不能離開路徑地塊。
</spoiler>

---

[統計資料](docs/stats.md)      [For 迴圈](docs/scripting/for.md)      [元組](docs/scripting/tuples.md)      [地下感官](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
