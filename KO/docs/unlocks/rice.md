[<- 채광](docs/unlocks/mining.md) <right>[대나무 ->](docs/unlocks/bamboo.md)
<right>[화석화된 호박 ->](docs/unlocks/petrified_pumpkins.md)
<right>[진주암과 양토 ->](docs/unlocks/special_soils.md)
---
# 벼
지표와 `Grounds.Dirt`층 아래에는 얇은 `Grounds.Clay`층이 있습니다. 이 비옥하고 물기 많은 땅은 벼를 심기에 딱 좋습니다.

점토를 찾을 때까지 굴착하고 벼를 심는 데는 다음 코드가 유용합니다:
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

드론이 `Grounds.Clay` 위에 있으면 `plant(Entities.Rice)`로 벼를 심고, `can_harvest()`로 다 자랐는지 확인한 뒤 `harvest()`로 수확할 수 있습니다.

## 계단식 논
벼를 심으면 땅이 `Grounds.Rice_Terrace`로 바뀌어 벼가 자라기 좋은 환경이 됩니다. 벼가 다 자라면 땅이 말라 `Grounds.Dry_Rice_Terrace`가 되며 더는 벼를 심을 수 없습니다. 다행히 층이 몇 블록 두께이므로 `dig()`로 블록을 없애고 아래의 `Grounds.Clay`에 다시 벼를 심을 수 있습니다. 층을 다 쓰면 언제든 `clear()`로 세계를 복원하고 새 층까지 파면 됩니다.

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감지](docs/unlocks/underground_senses.md)      [If문](docs/scripting/if.md)      [for 루프](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
