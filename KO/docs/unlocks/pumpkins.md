[<- 나무](docs/unlocks/trees.md) <right>[혼합 재배 ->](docs/unlocks/polyculture.md)
<right>[선인장 ->](docs/unlocks/cactus.md)
---
# 호박
[호박](objects/pumpkin)은 당근처럼 경작된 흙에서 자라요. 심는 데는 당근이 들어요.

사각형 안의 모든 호박이 다 자라면 함께 자라 거대한 호박을 형성해요. 불행히도 호박은 다 자라면 20% 확률로 죽기 때문에, 합쳐지게 하려면 죽은 호박을 다시 심어야 해요.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "carrot", "n": 11}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 5,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)
do_a_flip()
do_a_flip()
move(North)
move(North)
plant(Entities.Pumpkin)
do_a_flip()
plant(Entities.Pumpkin)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
harvest()
}}

호박이 죽으면 수확해도 아무것도 주지 않는 죽은 호박을 남겨요. 그 자리에 새 식물을 심으면 자동으로 죽은 호박이 제거되므로 수확할 필요가 없어요. `can_harvest()`는 죽은 호박에 대해 항상 `False`를 반환해요.

거대한 호박의 수확량은 호박의 크기에 따라 달라져요.

1x1 호박은 `1*1*1 = 1`개의 호박을 수확해요.
2x2 호박은 `4`개 대신 `2*2*2 = 8`개의 호박을 수확해요.
3x3 호박은 `9`개 대신 `3*3*3 = 27`개의 호박을 수확해요.
4x4 호박은 `16`개 대신 `4*4*4 = 64`개의 호박을 수확해요.
5x5 호박은 `25`개 대신 `5*5*5 = 125`개의 호박을 수확해요.
`n`x`n` 호박은 `n >= 6`일 때 `n*n*6`개의 호박을 수확해요.

최대 배율을 얻으려면 최소 6x6 크기의 호박을 기르는 것이 좋아요.

즉, 사각형의 모든 타일에 호박을 심어도 그중 하나가 죽어서 거대 호박이 자라지 못할 수 있어요.

---

[통계](docs/stats.md)      [연산자](docs/scripting/operators.md)      [변수](docs/scripting/variables.md)      [감각](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
