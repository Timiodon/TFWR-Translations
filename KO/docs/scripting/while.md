[<- 첫 번째 프로그램](docs/first_program.md) <right>[속도 업그레이드 ->](docs/unlocks/speed.md)
---
# While 루프
`while` 루프와 `True`, `False` 값을 해금했어요. `while` 루프는 조건이 `True`인 동안 루프 본문을 계속 실행해요.

`while condition:
	#루프 본문`

무한 루프를 만드는 것에 대해 걱정하지 마세요. 실행 지연이 프로그램이 멈추는 것을 방지할 거예요.

## 초보자를 위해
아마 이미 여러 `harvest()` 호출을 연달아 넣어 보셨을 거예요:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}

이렇게 하면 한 번의 프로그램 실행으로 여러 번 수확할 수 있어요.
하지만 세 번 이상 수확하고 싶을 텐데, 같은 코드를 여러 번 쓰는 것은 좋지 않은 습관이에요.
해결책은 루프예요.
루프를 사용하면 같은 코드를 여러 번 실행할 수 있어요.

while 루프는 조건을 받는데, 이것은 `True` 또는 `False` 두 가지 상태 중 하나만 가질 수 있는 논리값이에요.
이런 값을 불리언 값이라고 해요.

그런 다음 루프는 조건이 False가 될 때까지 루프 안의 코드를 실행해요.
while 루프는 다음과 같아요:

`while condition:
	#루프 본문
	#루프 본문
	#...`

여기서 "condition"을 불리언 값으로, `#루프 본문`을 루프에서 하고 싶은 일로 바꿔야 해요.

사용 가능한 상수 불리언 값은 두 가지가 있어요. 상수는 프로그램 동안 절대 변하지 않는 값이에요.

상수 불리언 값을 만들려면 `True` 또는 `False`라고 쓰면 돼요.
그래서 다음과 같이 쓸 수 있어요.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}

또는

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}

첫 번째는 절대 재주를 넘지 않고, 두 번째는 영원히 재주를 넘을 거예요 (무한 루프).

보통 무한 루프를 만드는 것은 프로그램이 멈추기 때문에 좋지 않은 생각이지만, 이 게임에서는 루프의 각 반복 사이에 지연이 있어서, 실행 버튼을 다시 눌러 수동으로 멈출 때까지 드론이 계속 재주를 넘게 할 거예요.

콜론 다음 줄이 어떻게 들여쓰기 되었는지 주목하세요. 이와 같은 들여쓰기는 코드 블록을 구분하는 데 사용돼요.
들여쓰기를 추가하려면 Tab 키를, 제거하려면 Shift + Tab(또는 Backspace)을 누르세요. 여러 줄을 선택하면 Tab과 Shift + Tab이 모든 줄에 적용돼요.

참고: Steam을 통해 게임을 플레이하는 경우 Shift + Tab을 누르면 Steam 오버레이가 열려요. 게임 옵션에서 내어쓰기 단축키를 다시 지정하거나 Steam 오버레이 옵션에서 오버레이 단축키를 다시 지정할 수 있어요.

여기서 `do_a_flip()`과 `pet_the_piggy()`는 들여쓰기된 `while` 블록 안에 있으므로 반복해 호출돼요. 하지만 `harvest()`는 그 블록 뒤에 있으므로 절대 실행되지 않아요.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[for 루프](docs/scripting/for.md)      [If문](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [외부 에디터](docs/external_editor.md)
