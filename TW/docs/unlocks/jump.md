[<-煤炭](docs/unlocks/coal.md)
---
# 跳轉
無人機已解鎖 `jump()` 指令。使用時，傳入一個解鎖項作為參數，例如 `Unlocks.Iron`。

此指令可以指定地下的某些資源，並瞬間向下跳到它們附近。它特別適合偵錯，或直接跳到剛才錯過的礦脈附近。

跳躍後，目標資源應該位於最上方地塊表面以下 3 格以內。每次執行程式只能使用一次 `jump()`，再次嘗試會產生錯誤。

以下範例跳到[水稻](docs/unlocks/rice.md)附近，找到黏土層，再種下一排水稻梯田：
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# 跳到水稻資源附近
jump(Unlocks.Rice)

# 種下一排水稻梯田
for i in range(get_world_size()):
    # 跳躍不精確，挖掉剩餘地塊
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## 支援的解鎖項
`jump()` 只適用於以下採礦解鎖項：
- 煤炭
- 鐵礦
- 石英
- 水稻
- 石化南瓜
- 特殊土壤
- 金字塔
- 藏寶圖
- 蘑菇
- 炸藥

---

[jump()](functions/jump)
