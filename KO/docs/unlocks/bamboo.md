[<- 벼](docs/unlocks/rice.md) <right>[알록달록 블록 ->](docs/unlocks/debug_place.md)
<right>[피라미드 ->](docs/unlocks/pyramid.md)
---
# 대나무
대나무는 위로 자라는 식물입니다. 계속 자라려면 드론이 갈색 열매를 주기적으로 따 줘야 합니다. 새로 해금한 `hover` 명령으로 할 수 있습니다.

대나무는 경작한 땅(`Grounds.Soil`)에 심어야 하며 벼가 필요합니다.

다음 코드는 대나무를 심고 첫 열매 높이까지 자라기를 기다립니다.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # 대나무가 자라도록 물러나기
}}

## 열매
대나무는 정확히 초당 1블록씩 자랍니다.

대나무는 몇 블록마다 열매를 맺습니다. 그러면 성장이 멈추므로 드론으로 열매에 부딪혀 없애야 합니다. 대나무는 세 번째 열매가 생길 때까지 위로 자라며, 그 뒤로는 열매를 따도 더 높이 자라지 않습니다.

열매를 따려면 먼저 `hover`로 알맞은 높이에 가야 합니다. 그런 다음 `move`로 열매 안에 들어가 따고, 다시 `move`로 물러나 대나무가 계속 자라게 하세요.

대나무에 `measure()`를 사용하면 다음 열매가 생길 높이를 확인할 수 있습니다. `measure()`는 `0`부터 세므로 `hover(measure())`로 열매가 생길 높이에 드론을 놓을 수 있습니다.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # 열매 옆에 오도록 높이 조절

move(East) # 물러나서 자랄 때까지 대기
for i in range(3):
    do_a_flip()

move(West) # 열매 따기
move(East) # 다시 물러나기
}}

## 부양
`hover` 명령은 부양 높이를 뜻하는 `0`부터 `18`까지의 숫자 하나를 인수로 받습니다. 드론의 기본 부양 높이는 `1`입니다. `hover`로 단단한 개체 안으로 내려갈 수는 없습니다. 드론이 이미 대나무 위에 있다면 `hover(0)`으로 그 안에 들어갈 수 없습니다.

`hover`는 지정한 높이에 도달하면 `True`를, 아니면 `False`를 반환합니다.

드론의 현재 부양 높이를 반환하는 `get_hover` 명령도 있습니다.

부양 중에 `dig`, `harvest`, `plant`를 사용하면 드론은 기본 부양 높이(`1`)로 돌아갑니다.

마지막으로, 부양 높이는 `get_pos_z()`에 영향을 주지 않습니다. 이 명령은 항상 드론 아래 블록의 z 위치를 반환합니다.

## 대나무 수확
`harvest()`도 쓸 수 있지만, 권장하는 수확 방법은 드론의 부양 높이를 `0`으로 맞추고(`hover(0)`) 대나무 안으로 이동하는 겁니다. 그러면 식물 전체를 한 번에 수확합니다.

대나무를 죽이지 않고 수확하려면 `hover(3)`처럼 원하는 높이에서 `move`로 대나무 안으로 들어가세요. 그 높이부터 위쪽 마디를 모두 수확하지만 대나무는 살아 있습니다. 이렇게 일부만 수확한 대나무는 열매를 다시 맺으므로 또 따 줘야 합니다.

어느 쪽이든 수확량은 파괴한 대나무 마디 수의 제곱이므로, 대나무가 높을수록 수확량이 많아집니다.

---

[통계](docs/stats.md)      [for 루프](docs/scripting/for.md)      [변수](docs/scripting/variables.md)      [If문](docs/scripting/if.md)      [함수](docs/scripting/functions.md)      [벼](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
