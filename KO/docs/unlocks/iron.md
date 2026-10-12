[<- 석탄](docs/unlocks/coal.md) <right>[석영 ->](docs/unlocks/quartz.md)
<right>[철 탐사 ->](docs/unlocks/prospecting.md)
<right>[보물지도 ->](docs/unlocks/treasure_map.md)
---
# 철

점토 아래의 암석층에서 철 광맥을 발견했습니다.

철 광맥은 처음에는 작아서 찾으려면 약간의 운이 필요합니다. 이 해금 항목의 레벨이 올라가면 광맥의 최대 크기가 커집니다. 철을 더 안정적으로 찾고 싶다면 철 탐사 해금도 확인해 보세요.

철 광맥은 대각선으로 떨어져 이어지는 일 없이 항상 연속되어 있습니다. 철 조각을 찾았다면 아래쪽이나 옆쪽에 더 있는지 살펴 광맥 전체를 캐내세요.

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [철 탐사](docs/unlocks/prospecting.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
