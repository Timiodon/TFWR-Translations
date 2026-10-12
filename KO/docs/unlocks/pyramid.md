[<- 대나무](docs/unlocks/bamboo.md)
---
# 피라미드

이제 지하에는 에너지를 수확할 수 있는 고대 피라미드 구조물이 출현합니다!

피라미드는 모래 블록(`Grounds.Sand`)으로 만들어집니다. 피라미드 아래에는 석회암 기반층(`Grounds.Limestone`)이 있습니다. 오래되어 침식되었기 때문에 일부가 파괴된 상태로만 발견되죠. 기반층은 항상 남아 있지만 모래에는 구멍이 있습니다. 피라미드를 굴착할 때의 모습은 다음과 같습니다.

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

피라미드 위의 블록은 항상 흙입니다. 위 코드보다 효율적으로 피라미드를 굴착하려면 이 사실을 활용하세요.

보다시피 모래에는 메워야 하는 구멍이 여러 개 있습니다. 이러한 구멍을 메워 피라미드를 이전 상태로 복원하면 스스로 붕괴하며, 보상으로 파워를 얻을 수 있습니다.

`place(Grounds.Sand)` 명령으로 블록을 배치해 피라미드를 복원할 수 있습니다. 모래는 제대로 받쳐져 있지 않으면 즉시 붕괴하는 특수 블록입니다. 모래 블록을 배치할 때는 석회암 바로 위에 놓거나 3x3 모래 블록 위에 놓아야 합니다. 다음은 설명을 위해 직접 쌓은 작은 피라미드입니다. 물론 직접 지은 피라미드에서는 파워를 얻을 수 없습니다.

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)
    
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
    
move(North)
move(East)
place(Grounds.Sand)
}}

올바르게 복원된 피라미드는 각 변의 블록 수가 홀수인 정사각형 석회암 기반으로 이루어집니다. 예를 들어 기반이 5×5라면 그 위에는 같은 크기(5×5)의 모래 블록층이 있고, 이후에는 3×3, 1×1 순으로 점점 작은 층이 쌓이죠.

피라미드가 완성되면 부스러져 사라지고 중앙에 커다란 해바라기가 생성됩니다. 이 해바라기를 수확하면 파워를 얻습니다. 완성한 피라미드가 클수록 더 많은 파워를 획득합니다.

---

[통계](docs/stats.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
