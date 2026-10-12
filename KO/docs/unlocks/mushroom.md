[<- 석영](docs/unlocks/quartz.md) <right>[다이너마이트 ->](docs/unlocks/dynamite.md)
---
# 버섯

여러 종류의 버섯이 지하에 군락을 이루고 자라납니다. 굴착하며 `Grounds.Mushroom` 지층을 찾아보세요. 그런 다음 땅을 `measure()`하면 `0`부터 시작하는 숫자로 버섯 종류를 알 수 있습니다.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

같은 종류의 버섯들은 함께 자라나는 경향이 있지만, 서로의 위로 자라기엔 조금 부끄러워합니다. 버섯 블록 하나를 같은 종류의 다른 버섯 블록 위에 놓이도록 밀면 두 블록이 사라지고 보상으로 버섯을 획득할 수 있습니다.

`can_push(direction)`으로 드론 아래의 블록을 밀 수 있는지, 주어진 방향에 걸리는 것이 있는지 확인할 수 있습니다. `push(direction)`은 블록을 밀고 성공 여부를 반환합니다.

블록은 위쪽으로 밀 수 없고, 다른 블록이 길을 막고 있으면 밀 수 없습니다. 공중으로 밀린 블록은 아래로 낙하해 다음 블록 위에 놓입니다.

`place(Grounds.Dirt)`를 호출해 드론 아래에 블록을 배치할 수 있다는 걸 기억하세요. 구멍을 메워 그 위로 블록을 밀어야 할 때 유용한 방법이죠.

---

[통계](docs/stats.md)      [지하 감지](docs/unlocks/underground_senses.md)      [딕셔너리](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
