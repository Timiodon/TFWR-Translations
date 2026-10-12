[<- 벼](docs/unlocks/rice.md) <right>[알록달록 블록 ->](docs/unlocks/debug_place.md)
<right>[피라미드 ->](docs/unlocks/pyramid.md)
---
# 대나무

대나무는 최대 6블록 높이까지 자라는 식물입니다. 위에 드론이 있으면 자라지 않으니 `plant(Entities.Bamboo)`를 사용한 후에는 드론을 반드시 `move`하세요. 대나무를 심으면 벼를 소모합니다.

대나무는 무작위로 선택된 특정 높이에 도달하면 꽃을 피웁니다. `measure()`로 어느 높이에서 꽃이 피는지 확인할 수 있습니다. `measure()`는 0부터 세므로 둘째 블록에 꽃이 피는 경우 `measure()`는 1을 반환합니다.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

드론이 꽃 바로 위에 있을 때 대나무를 `harvest()`하면 최대 수확량을 얻을 수 있습니다. 그 높이에서 한 블록씩 멀어질 때마다 수확량이 1/8로 줄어듭니다.
예를 들어 꽃이 높이 3에서 피고, 두 블록 위에서 수확하면 수확량은 1/64로 줄어듭니다.

더 높은 곳의 꽃을 수확하려면 드론을 원하는 높이에 놓고 대나무 안으로 날아가세요. 새로 해금된 `place()` 명령이 이때 유용합니다.

`place(Grounds.Dirt)`로 대나무 옆에 블록을 쌓아 올라가세요. 그런 다음 `move()`로 옆에서 대나무 안으로 날아가세요. `harvest()`를 호출할 때는 드론이 꽃 바로 위에 있어야 합니다.

`place(Grounds.Dirt)`를 사용하면 블록 1개를 소모합니다! `Grounds.Rock`과 같은 다른 땅도 배치할 수 있지만, `Grounds.Clay`와 같은 특수 블록은 배치할 수 없습니다.

대나무는 정확히 초당 1블록씩 자랍니다.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # 잠시 기다리기
do_a_flip()
move(West)
harvest()
}}

---

[통계](docs/stats.md)      [for 루프](docs/scripting/for.md)      [변수](docs/scripting/variables.md)      [If문](docs/scripting/if.md)      [함수](docs/scripting/functions.md)      [벼](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
