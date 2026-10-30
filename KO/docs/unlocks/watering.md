[<- 당근](docs/unlocks/carrots.md) <right>[비료 ->](docs/unlocks/fertilizer.md)
<right>[해바라기 ->](docs/unlocks/sunflowers.md)
---
# 물주기
식물은 물을 주면 더 빨리 자라요. 땅은 `0`에서 `1` 범위의 물 수위를 가져요.
`get_water()` 함수는 드론이 위치한 땅의 물 수위를 반환해요.

식물의 성장 속도는 물 수위 0에서 1배 속도, 물 수위 1에서 5배 속도로 선형적으로 증가해요.

땅은 시간이 지나면서 말라요: 평균적으로 초당 현재 물의 1%를 잃지만, 여기에는 약간의 무작위 변동이 있어요. 높은 물 수위를 유지하는 것은 낮은 물 수위를 유지하는 것보다 훨씬 더 많은 물을 소비해요.

식물에 물을 사용할 수 있어요. 10초마다 물 한 탱크가 자동으로 인벤토리에 추가돼요.
`Unlocks.Watering`을 업그레이드하면 10초마다 얻는 물의 양이 두 배가 돼요.

한 탱크에는 `0.25`의 물이 들어있어요.

아무 땅 위에서나 `use_item(Items.Water)`를 호출하여 땅에 물을 주세요.
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
    move(East)
    move(East)
}}

---

[비료](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
