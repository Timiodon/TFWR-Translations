[<- 채광](docs/unlocks/mining.md) <right>[철 ->](docs/unlocks/iron.md)
<right>[점프 ->](docs/unlocks/jump.md)
---
# 석탄

지표 바로 아래의 땅은 석탄 매장층을 찾기에 좋은 곳이었군요.

석탄은 두께가 1블록인 수평 층으로 무작위 생성됩니다. 층의 크기는 세계 크기에 비례해 커지므로, 더 많은 석탄을 찾으려면 세계를 확장해 보세요!

다음 프로그램은 석탄을 찾는 좋은 시작점입니다. 석탄층을 찾아 아래로 굴착한 다음, 더 많은 석탄을 찾기 위해 동쪽과 서쪽으로 굴착합니다.

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
