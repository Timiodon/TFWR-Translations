[<- 벼](docs/unlocks/rice.md)
---
# 화석화된 호박

어쩐지 지하에서 호박을 찾을 수 있는 모양입니다. 단단하게 굳어 화석화되었지만, 우리가 쓰기에는 아직 충분하죠.

화석화된 호박은 지하에 3x3x3 또는 5x5x5 크기의 블록 뭉치로 나타납니다. 확실하게 찾는 방법은 없으니 드론이 운 좋게 하나 굴착해내길 바랄 수밖에 없죠. 화석화된 호박은 암석과 철층 아래의 단단한 흙에, 석영이 출현하는 곳과 대략 같은 높이에 생성됩니다(석영을 해금한 경우).

지상에서 재배하지 않고도 호박을 얻을 수 있는 또 다른 방법입니다. 재배하는 편이 더 좋다면 화석화된 호박은 그냥 무시해도 괜찮습니다.

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
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
