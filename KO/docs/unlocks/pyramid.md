[<- 대나무](docs/unlocks/bamboo.md)
---
# 피라미드
이제 지하에는 드론을 빠르게 하는 파워를 수확할 수 있는 고대 피라미드 구조물이 출현합니다!

피라미드는 모래 블록(`Grounds.Sand`)으로 만들어집니다. 피라미드 아래에는 석회암 기반층(`Grounds.Limestone`)이 있습니다. 오래되어 침식되었기 때문에 일부가 파괴된 상태로만 발견되죠. 기반층은 항상 남아 있지만 모래에는 구멍이 있습니다.

피라미드 유적을 발굴하면 이런 모습입니다:
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
# 피라미드 기초를 찾을 때까지 굴착
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # 기초의 깊이 기억

# 피라미드가 아닌 부분을 모두 굴착
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## 피라미드 복원
보다시피 모래에는 메워야 하는 구멍이 여러 개 있습니다. 구멍을 메워 피라미드를 복원하면 피라미드가 무너지고 석회암 기초 중앙에 큰 해바라기가 생깁니다. 수확하면 `Items.Power`를 얻습니다. 완성한 피라미드가 클수록 더 많은 파워를 획득합니다.

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
# 모래를 놓을 석회암 기초가 필요
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# 석회암 위에 3x3 모래층 놓기
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# 3x3 층을 하나 더 놓아 보기
# 가운데 블록만 지지되어 남는 것을 확인
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

올바르게 복원된 피라미드는 각 변의 블록 수가 홀수인 정사각형 석회암 기반으로 이루어집니다. 예를 들어 기반이 5×5라면 그 위에는 같은 크기(5×5)의 모래 블록층이 있고, 이후에는 3×3, 1×1 순으로 점점 작은 층이 쌓이죠.

피라미드 위의 블록은 항상 흙입니다. 피라미드를 효율적으로 굴착하려면 이 사실을 활용하세요.

## 파워
파워가 있는 동안 드론은 파워를 사용해서 두 배 더 빠르게 움직여요. 
30번의 행동(이동, 수확, 심기 등)마다 1 파워를 소모해요.
다른 코드 문장을 실행할 때도 파워를 사용할 수 있지만, 드론 행동보다는 훨씬 적게 사용해요.

일반적으로, 속도 업그레이드로 빨라지는 모든 것은 파워로도 빨라져요.
파워로 빨라지는 모든 것은 속도 업그레이드를 무시하고 실행에 걸리는 시간에 비례하여 파워를 사용해요.

파워는 `dig()`에 영향을 주지 않습니다.

---

[통계](docs/stats.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
