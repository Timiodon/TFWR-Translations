[<- 심기](docs/unlocks/plant.md) <right>[디버그 2 ->](docs/unlocks/debug2.md)
<right>[타이밍 ->](docs/unlocks/timing.md)
---
# 디버그
때때로 코드가 작동하지 않아서 왜 그런지 알아내야 할 때가 있어요. 이를 돕기 위한 몇 가지 도구가 있어요.

첫 번째는 프로그램을 단계별로 실행하는 거예요.
실행 버튼 옆에 있는 버튼을 사용하거나 중단점을 설정하여 단계별 모드로 들어갈 수 있어요.

중단점은 코드 왼쪽의 중단점 패널을 클릭하여 추가할 수 있어요.
![|x227](Breakpoints)
실행이 중단점이 있는 줄에 도달하면 자동으로 단계별 모드로 전환돼요.

변수 위에 마우스를 올리면 현재 값이 표시돼요.

`print()` 함수도 매우 유용할 수 있어요. 전달된 모든 값을 공중에 직접 써요.

예시:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(0.24)
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(can_harvest())
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_pos_x(), get_pos_y())
}}

`print()` 함수는 값을 공중에 직접 출력하고 [출력](docs/output.md) 페이지에도 출력해요.

많은 값을 출력하고 싶을 때 공중에 쓰는 것은 때때로 조금 느릴 수 있어요.
이 경우 출력 창에만 출력하는 `quick_print()` 함수를 사용할 수 있어요.

출력 창은 경고와 오류도 기록하므로, 무언가 예상대로 작동하지 않으면 확인하는 것이 유용할 수 있어요.

실행이 멈추면 출력은 게임 폴더의 [output.txt](persistent_data_path/output.txt) 파일에도 기록돼요.

---

[출력](docs/output.md)      [주석](docs/scripting/comments.md)      [디버그 2](docs/unlocks/debug2.md)      [알록달록 블록](docs/unlocks/debug_place.md)      [시뮬레이션](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
