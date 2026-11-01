[<-铁矿](docs/unlocks/iron.md)
---
# 藏宝图
传说有位早已离世的健忘海盗将一份宝藏藏了起来——大概是这么回事吧。如果他把通往宝藏的路径画在地图上，后来又弄丢了呢？也许他被熔岩河逼到绝境时弄掉了地图，地图便保存在一层玄武岩下。

测量玄武岩地块或许能发现线索！

<spoiler=告诉我更多>
留意一层 `Grounds.Basalt`。试着测量玄武岩，看看能发现什么。线索或许会引你找到藏宝图；测量藏宝图一定能得到通往宝藏的路径——但你能解读地图给出的指示吗？
</spoiler>

<spoiler=直接告诉我怎么做>
好吧，方法是这样的：找到 `Grounds.Basalt` 层，以及正下方的 `Grounds.Treasure_Map` 地块。你可以对玄武岩使用 `measure()`，得到下方地图地块的 `(x, y)` 坐标。

在地图地块上调用 `measure()`，就能得到一串表示宝藏路径的方向字母。N、E、S、W 分别代表 `North`、`East`、`South`、`West`；D 代表“向下”或“挖掘”。这些字母描述了由 `Grounds.Treasure_Path` 地块组成、通向宝藏的路径。

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
# 寻找玄武岩层
while get_ground_type() != Grounds.Basalt:
    dig()

# 测量玄武岩会返回藏宝图的位置
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# 找到地图，测量以获得路径
do_a_flip()
instructions = measure()
print("指令： ", instructions)

# 挖入地图，开始寻宝
dig()
}}

可以对字符串使用 `for` 循环，逐个字母处理：
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
# 地图指令以一个字符串返回
instructions = measure()
# 用 for-in 将字符串逐字处理
for letter in instructions:
    print(letter)
}}

无人机必须一直待在 `Grounds.Treasure_Path` 地块上方。如果移动到其他地块，路径就会断开，宝藏也会丢失。

## 终点
路径尽头是一个 `Grounds.Treasure_Goal` 地块。如果无人机没有偏离路径，其上方就会出现 `Entities.Underground_Treasure`。无人机可以使用 `harvest()` 收获宝箱，获得黄金。

## 奖励
黄金数量与宝藏路径的长度成正比。升级藏宝图解锁项会增加路径的深度，升级扩张则能让路径有更多横向延伸的空间。两种升级都会延长宝藏路径，让你找到更多黄金。

## 多架无人机
宝藏必须由挖到藏宝图地块的那架无人机寻找，而且它不能离开路径地块。
</spoiler>

---

[统计数据](docs/stats.md)      [For 循环](docs/scripting/for.md)      [元组](docs/scripting/tuples.md)      [地下感官](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
