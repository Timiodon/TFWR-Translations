[<- 연산자](docs/scripting/operators.md)
---
# 감각
이제 드론이 볼 수 있어요!

`get_pos_x()`와 `get_pos_y()` 함수는 드론의 현재 x, y 좌표를 반환해요. 시작 위치에서는 둘 다 `0`이에요. x 좌표는 `East` 방향으로 타일마다 `1`씩 증가하고, y 좌표는 `North` 방향으로 타일마다 `1`씩 증가해요.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)`은 해당 아이템을 몇 개 가지고 있는지 반환해요.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(num_items(Items.Hay))
}}

`get_entity_type()`와 `get_ground_type()`은 드론 아래에 있는 개체나 땅의 종류를 반환해요.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

`None` 키워드도 이제 해금되었어요! `None`은 값이 없음을 나타내는 값이에요.
예를 들어 `return` 문이 없는 함수는 실제로 `None`을 반환해요.

`get_entity_type()`은 드론 아래에 개체가 없으면 `None`을 반환해요.


특정 해금을 몇 개 가지고 있는지 알고 싶다면 `num_unlocked(unlock)` 함수를 사용하세요.

예를 들어 `num_unlocked(Unlocks.Speed)`는 가지고 있는 속도 업그레이드 수를 반환해요.

`num_unlocked(Unlocks.Senses)`는 감각이 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환해요.

아이템이나 개체에도 `num_unlocked()`를 사용할 수 있어요. 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환해요.

주의하세요. `num_unlocked(Unlocks.Carrots)`는 해당 해금이 해금되거나 업그레이드된 횟수를 반환해요.
`num_unlocked(Items.Carrot)`는 `0` 또는 `1`만 반환해요. 다른 식물도 마찬가지예요.

---

[If문](docs/scripting/if.md)      [연산자](docs/scripting/operators.md)      [변수](docs/scripting/variables.md)      [튜플](docs/scripting/tuples.md)      [딕셔너리](docs/scripting/dicts.md)      [지하 감지](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
