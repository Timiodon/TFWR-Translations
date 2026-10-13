[<-擴張 1](docs/unlocks/expand_1.md) <right>[地下感官->](docs/unlocks/underground_senses.md)
<right>[水稻->](docs/unlocks/rice.md)
<right>[煤炭->](docs/unlocks/coal.md)
---
# 採礦

無人機可以使用簡陋鑽頭了，可以用它到地下尋找寶藏。

使用 `dig()` 指令挖掘下方的地塊。

先來收集一些地塊吧：

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

如果想回到地表，隨時可以使用 `clear()`。這也會修復你的農場。

將滑鼠懸停在地塊上，可以看到它的名稱、穩定度和硬度。

# 鑽頭

越往下挖，地塊越堅硬，挖掘所需的時間也越長。好在可以升級鑽頭來應對！

使用 `get_hardness()` 可以檢查下方地塊的硬度。如果遇到特別堅硬的一片地塊，不妨繞過去，以便更快取得進展：

`while True:
        if get_hardness() < 5:
                dig()
        else:
                move(East)`

當然，越往下地塊越堅硬，所以這個策略雖然有用，也無法讓你一路暢通無阻。

## 塌方

向下挖掘會導致周圍地塊塌方。無人機四周的四個地塊總會被摧毀。之後，塌方如何擴散取決於地塊的穩定度。穩定度為 1 的地塊（如草地）能承受 1 格的高度差。換句話說，如果草地在垂直或水平方向上的相鄰地塊的 z 座標比它至少深 2 格，這塊草地就會被摧毀。

地塊的懸停提示框中會顯示其穩定度。

地塊塌方時，其上方的所有地塊也會被移除。只有無人機直接挖掘的地塊才會提供資源，因此塌方中損失的地塊會被直接摧毀，不會產出資源。

---

[地下感官](docs/unlocks/underground_senses.md)      [While 迴圈](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
