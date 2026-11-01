[<- 석탄](docs/unlocks/coal.md)
---
# 점프
드론이 `jump()` 명령을 해금했습니다. `Unlocks.Iron`처럼 해금 항목을 인수로 전달해 사용합니다.

이 명령은 땅속의 특정 자원을 목표로 즉시 아래로 점프할 수 있게 합니다. 디버깅하거나 방금 놓친 광맥 근처까지 건너뛸 때 특히 유용합니다.

점프 후 목표 자원은 가장 위쪽 블록 표면에서 3블록 이내에 있을 겁니다. `jump()`는 프로그램 실행당 한 번만 사용할 수 있습니다. 추가로 시도하면 오류가 납니다.

다음 예시는 [벼](docs/unlocks/rice.md) 근처로 점프하고 점토층을 찾아 계단식 논을 한 줄 심습니다:
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# 벼 자원 근처로 점프
jump(Unlocks.Rice)

# 벼 계단식 논을 한 줄 심기
for i in range(get_world_size()):
    # 점프는 정확하지 않으므로 남은 블록 파기
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## 지원하는 해금 항목
`jump()`는 다음 채광 해금 항목에만 사용할 수 있습니다:
- 석탄
- 철
- 석영
- 벼
- 화석화된 호박
- 특수 토양
- 피라미드
- 보물 지도
- 버섯
- 다이너마이트

---

[jump()](functions/jump)
