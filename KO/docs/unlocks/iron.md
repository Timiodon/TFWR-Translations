[<- 석탄](docs/unlocks/coal.md) <right>[석영 ->](docs/unlocks/quartz.md)
<right>[철 탐사 ->](docs/unlocks/prospecting.md)
<right>[보물지도 ->](docs/unlocks/treasure_map.md)
---
# 철
`Grounds.Dirt`에서 석탄을 찾았다면 `Grounds.Clay`층을 지나 `Grounds.Rock`까지 더 파서 철을 찾을 수 있습니다.

석탄 광맥과 달리 철 광맥은 수직으로도 뻗습니다. 한 광맥의 철 블록은 항상 직접 맞닿으며 대각선으로만 연결되지는 않습니다.

철 광맥은 처음에는 작아서 찾으려면 약간의 운이 필요합니다. 철을 더 해금하면 최대 광맥 크기가 커져 우연히 발견하기 쉬워집니다. 확실히 찾으려면 [철 탐사](docs/unlocks/prospecting.md)를 해금하세요.

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# 철 블록이 나올 때까지 굴착
while get_ground_type() != Grounds.Iron:
    dig()

# 철 채굴
dig()
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [철 탐사](docs/unlocks/prospecting.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
