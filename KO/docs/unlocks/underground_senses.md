[<- 채광](docs/unlocks/mining.md)
---
# 지하 감지
드론이 지하에서 길을 찾을 수 있도록 센서를 몇 개 추가해 보죠.

## Z 위치
이제 `get_pos_z()`로 드론의 높이를 알 수 있습니다. 0에서 시작하며 드론이 내려갈수록 음수가 됩니다.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## 땅 종류
`get_ground_type()`은 드론 아래의 땅 종류를 반환합니다. `get_ground_type(North)` 같은 방향 인수를 전달하면 인접한 타일의 땅 종류를 알 수 있습니다.

드론 아래의 블록이 흙인지 확인하는 방법은 다음과 같습니다.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
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
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## 경도와 안정성
`get_hardness()`는 드론 아래 땅 타일의 경도를 반환합니다. `get_hardness(North)`처럼 방향 인수를 전달할 수 있습니다. 타일의 경도가 높을수록 굴착에 더 오랜 시간이 걸립니다.

`get_stability()`는 드론 아래 땅 타일의 안정성을 반환합니다. `get_stability(North)`처럼 방향 인수를 전달할 수 있습니다. 안정성이 1이라면 블록이 붕괴하기 전에 높이 차이 1까지 견딜 수 있다는 뜻입니다.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

드론이 아래로 굴착할 때 특수 기능이 있는 블록이 아니라면 드론 바로 옆의 네 블록은 안정성과 관계없이 제거됩니다. 예를 들어 점토, 철, 석영은 이 규칙에 따라 제거되지 않습니다. 하지만 블록 안정성이 부족해 일어나는 붕괴에는 여전히 영향을 받습니다.
---

[채광](docs/unlocks/mining.md)      [감각](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
