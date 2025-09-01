# 거대 농장
이 엄청나게 강력한 해금은 여러 드론에 접근할 수 있게 해줍니다.

이전과 마찬가지로, 여전히 드론 하나로 시작합니다. 추가 드론은 먼저 생성되어야 하며 프로그램이 종료된 후 사라집니다.
각 드론은 자신만의 별도 프로그램을 실행합니다. 새 드론은 `spawn_drone(function)` 함수를 사용하여 생성할 수 있습니다.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

이것은 `spawn_drone(function)` 명령을 실행한 드론과 같은 위치에 새 드론을 생성합니다. 그러면 새 드론은 지정된 함수를 실행하기 시작하고, 작업이 끝나면 자동으로 사라집니다.

드론은 서로 충돌하지 않습니다.

생성할 수 있는 최대 드론 수를 알아보려면 `max_drones()`를 사용하세요.
농장에 이미 있는 드론 수를 알아보려면 `num_drones()`를 사용하세요.


## 예시:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

이렇게 하면 첫 번째 드론이 수평으로 이동하며 더 많은 드론을 생성합니다. 생성된 드론들은 수직으로 이동하며 경로에 있는 모든 것을 수확합니다.

사용 가능한 모든 드론이 이미 생성되었다면, `spawn_drone()`은 아무것도 하지 않고 `None`을 반환합니다.

<spoiler=힌트 보기> 매우 유용한 병렬 `for_all` 함수를 확인해보세요. 이 함수는 어떤 함수든 인자로 받아서 농장의 모든 타일에서 실행합니다. 이를 위해 사용 가능한 모든 드론을 활용합니다.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

특히 유용한 패턴은 드론을 사용할 수 있으면 생성하고, 그렇지 않으면 직접 처리하는 것입니다.

`if not spawn_drone(task):
	task()`
</spoiler>

## 다른 드론 기다리기
`wait_for(drone)` 함수를 사용하여 다른 드론이 작업을 마칠 때까지 기다리세요. 드론을 생성할 때 `drone` 핸들을 받게 됩니다.
`wait_for(drone)`는 다른 드론이 실행하던 함수의 반환 값을 반환합니다.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

드론 생성에는 시간이 걸리므로, 사소한 일마다 새 드론을 생성하는 것은 좋은 생각이 아닙니다.

## 공유 메모리 없음
각 드론은 자신만의 메모리를 가지고 있으며 다른 드론의 전역 변수를 직접 읽거나 쓸 수 없습니다.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

이 코드는 `0`을 출력합니다. 새 드론이 전역 변수 `x`의 자신만의 복사본을 증가시켰고, 이는 첫 번째 드론의 `x`에 영향을 주지 않기 때문입니다.

## 경쟁 상태
여러 드론이 동시에 같은 농장 타일과 상호작용할 수 있습니다. 만약 두 드론이 같은 tick 동안 같은 타일과 상호작용하면 두 상호작용 모두 발생하지만, 상호작용 순서에 따라 결과가 달라질 수 있습니다.

예를 들어, 드론 `0`과 `1`이 거의 다 자란 같은 나무 위에 모두 있다고 상상해보세요.
드론 `0` 호출
`use_item(Items.Fertilizer)`
드론 `1` 호출
`harvest()`

이 동작들이 동시에 일어나면, 나무는 먼저 비료를 받고 그 다음에 수확됩니다. 이 경우에는 나무를 얻게 됩니다. 하지만 만약 드론 `1`이 약간 더 빠르다면, 나무는 비료를 받기 전에 수확되어 나무를 얻지 못할 것입니다.
이것을 "경쟁 상태(race condition)"라고 부릅니다. 이것은 병렬 프로그래밍에서 흔히 발생하는 문제로, 결과가 연산이 수행되는 순서에 따라 달라집니다.

여러 드론이 같은 위치에서 동시에 같은 코드를 실행할 때 발생할 수 있는 또 다른 문제 상황입니다.
`if get_water() < 0.5:
    use_item(Items.Water)`

만약 여러 드론이 이 코드를 동시에 실행하면, 모두 첫 번째 줄을 실행하여 `if` 블록으로 들어가게 됩니다. 그러면 모두 물을 사용하게 되어 많은 양을 낭비하게 됩니다.
한 드론이 두 번째 줄에 도달할 때쯤이면, 그 사이에 다른 드론이 타일에 물을 주었기 때문에 `get_water()`가 더 이상 `0.5`보다 작지 않을 수 있습니다.