[<- while 루프](docs/scripting/while.md)
---
# Continue
`continue`는 루프의 현재 반복을 멈추고 가장 안쪽 루프의 다음 반복으로 건너뛰어요.

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
for i in range(10):
	print("이 문장은 매번 출력됩니다")
	continue
	print("이것은 출력되지 않습니다")
}}

이 코드는 루프를 `10`번 모두 반복하지만, `continue` 다음의 `print` 문은 항상 건너뛰어요.

`while` 루프에서도 작동해요.

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Tree)
#CODE
while True:
	if not can_harvest():
		continue

	harvest()
}}

이 코드는 `can_harvest()`가 `True`일 때만 `harvest()`를 호출해요.
다음과 같은 효과가 있어요.

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Tree)
#CODE
while True:
	if can_harvest():
		harvest()
}}

중첩된 루프에서 `continue`는 항상 가장 안쪽의 루프에 영향을 줘요.

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
for i in range(2):
	for j in range(2):
		print("이 문장은 4번 출력됩니다")
		continue
		print("이것은 출력되지 않습니다")
	print("이 문장은 2번 출력됩니다")
}}

---

[while 루프](docs/scripting/while.md)      [for 루프](docs/scripting/for.md)      [Break](docs/scripting/break.md)
