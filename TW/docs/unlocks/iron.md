[<-煤炭](docs/unlocks/coal.md) <right>[石英->](docs/unlocks/quartz.md)
<right>[鐵礦探查->](docs/unlocks/prospecting.md)
<right>[藏寶圖->](docs/unlocks/treasure_map.md)
---
# 鐵礦
在 `Grounds.Dirt` 中找到煤炭後，繼續向下穿過 `Grounds.Clay` 層，進入 `Grounds.Rock` 就能找到鐵礦。

與煤礦脈不同，鐵礦脈也會沿垂直方向延伸。礦脈內的鐵礦地塊始終直接相鄰，絕不會只有對角連接。

鐵礦脈的礦頭很小，要找到還需要一點運氣。繼續升級鐵礦可以增加礦脈的最大規模，讓你更容易偶然遇到。想穩定找到鐵礦，應該解鎖[鐵礦探查](docs/unlocks/prospecting.md)。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# 挖到出現鐵礦地塊
while get_ground_type() != Grounds.Iron:
    dig()

# 開採鐵礦
dig()
}}

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [鐵礦探查](docs/unlocks/prospecting.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
