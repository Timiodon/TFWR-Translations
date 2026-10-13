[<-煤炭](docs/unlocks/coal.md) <right>[石英->](docs/unlocks/quartz.md)
<right>[鐵礦探查->](docs/unlocks/prospecting.md)
<right>[藏寶圖->](docs/unlocks/treasure_map.md)
---
# 鐵礦

你在黏土下方的岩石層中發現了鐵礦脈。

鐵礦脈的礦頭很小，要找到還需要一點運氣。隨著此解鎖項等級提高，礦脈的最大規模也會增大。想更穩定地找到鐵礦，還可以看看礦石探查解鎖項。

鐵礦脈始終連成一片，不會斜著跨越地塊。如果找到一塊鐵礦，就檢查它的下方及相鄰地塊，確保採完整條礦脈。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [鐵礦探查](docs/unlocks/prospecting.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
