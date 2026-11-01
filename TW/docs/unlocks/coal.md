[<-採礦](docs/unlocks/mining.md) <right>[鐵礦->](docs/unlocks/iron.md)
<right>[跳轉->](docs/unlocks/jump.md)
---
# 煤炭
地下隱藏著各種礦石，等著你去發現和開採。穿過地表挖入 `Grounds.Dirt` 後，最先找到的礦石是煤炭。

開採煤炭不需要特殊操作，只要無人機位於 `Grounds.Coal` 地塊正上方時執行 `dig()` 即可。用 `get_ground_type()` 檢查無人機下方，用 `get_ground_type(direction)` 檢查四個相鄰地塊。

下面的程式很適合用來尋找煤炭。它會向下挖掘尋找煤炭層。
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# 挖到出現煤炭地塊
while get_ground_type() != Grounds.Coal:
    dig()

# 開採煤炭
dig()
}}

## 關於崩塌
只有直接挖掘的煤炭地塊才會提供煤炭，無人機周圍崩塌的地塊不會。規劃採煤方式時請記住這點，盡量多挖出煤炭，減少崩塌損失。

## 礦脈結構
煤炭礦脈形成厚度為 1 格的水平薄層，需要在挖掘泥土時偶然發現。薄層內的煤炭大多直接相鄰，但也有只透過對角相連的地塊。

煤礦規模隨農場大小成比例增加，因此可以繼續升級[擴張](unlocks/expand)，增加可開採的煤炭。

## 策略
<spoiler=顯示提示>
一種簡單的策略，尤其適合小農場，就是挖掉發現煤炭時所在深度的所有地塊。要提高效率，可以用 `get_ground_type(direction)` 記錄看過煤炭的位置，避免在泥土地塊上移動浪費時間。只在煤炭上移動會漏掉對角連接，務必留意。
</spoiler>

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
