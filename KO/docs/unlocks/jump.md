[<- 석탄](docs/unlocks/coal.md)
---
# 점프

드론이 `jump()` 명령을 해금했습니다.

이 명령을 사용하면 특정 해금 항목이 있는 지점으로 바로 이동할 수 있습니다. 디버깅하거나 최근에 놓친 광맥으로 이동할 때 특히 유용합니다. `Unlocks.Iron`처럼 해금 항목을 인수로 전달해 사용합니다.

`jump()`는 `jump(Unlocks.Rice)` 또는 `jump(Unlocks.Iron)`처럼 지하에 나타나는 해금 항목에만 사용할 수 있습니다.

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
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

점프한다고 반드시 목표 해금 항목 바로 앞에 도착하는 것은 아니라서 주변을 조금 더 찾아야 할 수도 있습니다. 그래도 목표가 근처에 있다는 것은 보장되죠.

`jump()`는 프로그램 실행당 한 번만 사용할 수 있습니다.

---

[jump()](functions/jump)
