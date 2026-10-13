[<- 蘑菇](docs/unlocks/mushroom.md) <right>[爆破鑽頭 ->](docs/unlocks/explosive_drill.md)
---
# 炸藥

這種革命性的爆炸物是以前的採礦隊留下的。（不）幸運的是，你的鑽頭正好能引爆炸藥，把周圍的地塊炸開。

想安全地開採炸藥，你得找到由 `Grounds.Dynamite` 和 `Grounds.Soot` 組成的雙層地層。上層的炸藥已經老化，其中一些地塊是啞彈，可以安全挖掘。不過，還有一些炸藥是實彈，會在挖掘時爆炸。

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

你能找出並挖掘所有啞彈地塊，只留下實彈炸藥地塊嗎？炸藥層消失時，每個周圍只剩實彈地塊或黑煙地塊的實彈地塊，都會給你產出額外的炸藥。

好在下方的黑煙地塊可以幫忙：它們能檢測相鄰的炸藥地塊中有多少是實彈炸藥。不過，它們只告訴你總數，不會指出具體是哪些地塊，因此你需要結合多個黑煙地塊的讀數自行推斷。

在黑煙地塊上呼叫 `measure()`，會回傳上方炸藥層中八個相鄰地塊中的炸藥數量。結果介於 `0`（沒有實彈炸藥）和 `8`（每個相鄰地塊都有實彈炸藥）之間。

炸藥層中第一次挖到的一定是啞彈。每挖掉一個炸藥地塊都會產出少量炸藥。炸藥層被摧毀時，無論是成功挖光啞彈，還是不慎挖中實彈炸藥，你都會獲得額外的炸藥，其數量等於完全顯露的實彈炸藥地塊數的平方。

如果挖到實彈炸藥，兩個地層都會爆炸。在挖入 `Grounds.Dynamite` 後，可以使用 `get_ground_type()` 檢查是否發生了爆炸。如果地塊不是 `Grounds.Soot`，說明解謎失敗。反之，如果挖掉最後一個啞彈地塊，所有炸藥地塊都會消失，你會獲得該謎題獎勵的最大產量。如果黑煙層保留，但 `measure()` 回傳 `None`，則表示謎題已成功解開。

`# 挖掘炸藥地塊並檢查謎題狀態
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # 挖到實彈炸藥，未能解開謎題
        return False
    elif measure() == None:
        # 挖掉最後一個啞彈地塊，成功解開謎題
        return True
    else:
        # 測量得到一個數字，謎題仍在進行中
        return None
`

炸藥層中的實彈炸藥數量會隨著深度增加，找出它們也會越來越難。

收集到的炸藥可以透過 `use_item(Items.Dynamite)` 使用，並立即在無人機下方爆炸。

升級炸藥後，挖掘炸藥地塊和完全顯露的實彈地塊時的產量會提高，還會使炸藥爆炸的能量提高 30%。

---

[統計資料](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)      [字典](docs/scripting/dicts.md)      [集合](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
