[<- 채광](docs/unlocks/mining.md) <right>[철 ->](docs/unlocks/iron.md)
<right>[점프 ->](docs/unlocks/jump.md)
---
# 석탄
지하에는 여러 광물이 발견되고 채굴되기를 기다리고 있습니다. 지표를 뚫고 `Grounds.Dirt`를 파면 처음 발견하는 광물은 석탄입니다.

석탄 채굴에 특별한 방법은 필요 없습니다. 드론이 `Grounds.Coal` 블록 바로 위에 있을 때 `dig()`를 실행하면 됩니다. `get_ground_type()`으로 드론 아래를, `get_ground_type(direction)`으로 인접한 네 블록을 확인하세요.

다음 프로그램은 석탄을 찾는 좋은 시작점입니다. 석탄층을 찾아 아래로 굴착합니다.
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
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# 석탄 블록이 나올 때까지 굴착
while get_ground_type() != Grounds.Coal:
    dig()

# 석탄 채굴
dig()
}}

## 붕괴에 관한 참고
석탄은 직접 파낸 블록에서만 얻으며 드론 주변에서 무너진 블록에서는 얻지 못합니다. 직접 캐는 석탄을 늘리고 붕괴로 잃는 석탄을 줄이도록 채굴 방법을 계획하세요.

## 광맥 구조
광맥은 두께 1블록의 수평층을 이루며, 흙을 파다가 우연히 찾아야 합니다. 한 층의 석탄 블록은 주로 직접 맞닿아 있지만 대각선으로만 연결되기도 합니다.

석탄 광상은 농장 크기에 비례해 커지므로 [확장](unlocks/expand)을 더 해금하면 더 많은 석탄을 얻을 수 있습니다.

## 전략
<spoiler=힌트 보기> 
특히 작은 농장에서는 석탄을 찾은 깊이의 모든 블록을 파는 것이 간단한 전략입니다. 효율을 높이려면 `get_ground_type(direction)`으로 석탄을 본 위치를 기록하고 흙 위를 이동하며 낭비하는 시간을 줄이세요. 석탄 블록 위로만 이동하면 대각선 연결을 놓치므로 주의하세요.
</spoiler>

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
