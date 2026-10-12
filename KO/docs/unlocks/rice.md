[<- 채광](docs/unlocks/mining.md) <right>[대나무 ->](docs/unlocks/bamboo.md)
<right>[화석화된 호박 ->](docs/unlocks/petrified_pumpkins.md)
<right>[진주암과 양토 ->](docs/unlocks/special_soils.md)
---
# 벼

지표 아래에 얇은 점토층이 있음을 발견하셨을 겁니다. 이 비옥한 땅은 벼 모를 심기에 안성맞춤이죠.

벼는 점토를 말리므로, 각 점토 블록은 한 번만 사용할 수 있습니다. 다행히 점토층은 몇 블록 두께입니다. 물론 언제든 `clear()`로 세계를 초기화해 점토층을 다시 생성할 수도 있습니다.

점토를 찾을 때까지 굴착하는 데는 다음 코드가 유용합니다.

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
move(North)
do_a_flip()
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감지](docs/unlocks/underground_senses.md)      [If문](docs/scripting/if.md)      [for 루프](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
