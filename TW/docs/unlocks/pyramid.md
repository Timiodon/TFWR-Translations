[<-竹子](docs/unlocks/bamboo.md)
---
# 金字塔

現在地下會出現古代金字塔，你可以從中收穫能量！

金字塔由沙地塊（`Grounds.Sand`）構成，下方是一層石灰岩（`Grounds.Limestone`）地基。由於年代久遠、遭受侵蝕，找到時總有一部分損壞。石灰岩地基始終完整，但沙層會出現坑洞。下面展示了一座金字塔挖出後的樣子：

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

金字塔上方的地塊總是泥土。你可以利用這一點，更加有效地挖掘金字塔，而不用照搬上方程式碼。

如你所見，沙層裡有幾個坑洞需要填補。填滿這些坑洞、將金字塔修復還原後，金字塔會自行崩塌，而你會獲得能量作為獎勵。

使用 `place(Grounds.Sand)` 指令放置地塊，就能修復金字塔。沙是特殊地塊，缺乏適當支撐時會立即塌方。每次放置沙地塊時，必須將其直接放在石灰岩上，或放在 3x3 的沙地塊上。下面是一座用於演示的手工建造小金字塔。當然，自己建造的金字塔不會提供能量：

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)
    
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
    
move(North)
move(East)
place(Grounds.Sand)
}}

正確修復的金字塔，底部是一塊邊長為奇數（如 5x5）的正方形石灰岩地基。其上是一層同樣規模的沙地塊（5x5），再向上逐層縮小：3x3，最後是 1x1。

金字塔建成後會崩塌，並在中央產生一株巨大的向日葵。收穫它即可獲得能量。修復的金字塔越大，獲得的能量越多。

---

[統計資料](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
