[<-採礦](docs/unlocks/mining.md) <right>[竹子->](docs/unlocks/bamboo.md)
<right>[石化南瓜->](docs/unlocks/petrified_pumpkins.md)
<right>[珍珠岩與壤土->](docs/unlocks/special_soils.md)
---
# 水稻
地表和 `Grounds.Dirt` 層下方有一層薄薄的 `Grounds.Clay`。這片肥沃且浸滿水的地面非常適合種植水稻。

以下程式碼可以幫你挖到黏土並種下水稻：
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
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

只要無人機位於 `Grounds.Clay` 上方，就能用 `plant(Entities.Rice)` 種下水稻，再用 `can_harvest()` 檢查是否成熟，最後用 `harvest()` 收穫。

## 梯田
種下水稻後，地面會變成 `Grounds.Rice_Terrace`，為水稻成熟提供理想環境。水稻完全成熟後，地面會乾燥並變成 `Grounds.Dry_Rice_Terrace`，無法再次種植水稻。幸好薄層有幾格厚，因此可以用 `dig()` 挖掉地塊，在下方的 `Grounds.Clay` 上再種水稻。如果整層都用完了，隨時可以用 `clear()` 重設世界，再挖到新的黏土層。

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [If 陳述式](docs/scripting/if.md)      [For 迴圈](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
