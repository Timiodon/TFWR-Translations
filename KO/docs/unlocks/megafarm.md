# 메가 팜
이 엄청나게 강력한 해금은 여러 드론에 대한 접근 권한을 줍니다. 

이전과 마찬가지로, 여전히 한 대의 드론으로 시작합니다. 추가 드론은 먼저 생성되어야 하며, 프로그램이 종료된 후 사라집니다.
각 드론은 자신만의 별도 프로그램을 실행합니다. 새 드론은 `spawn_drone(function)` 함수를 사용하여 생성할 수 있습니다.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

`spawn_drone(function)` 명령을 실행한 드론과 같은 위치에 새 드론을 생성합니다. 그러면 새 드론은 지정된 함수를 실행하기 시작하고, 작업이 끝나면 자동으로 사라집니다.

드론은 서로 충돌하지 않습니다. 

`max_drones()`를 사용하여 생성할 수 있는 최대 드론 수를 가져옵니다.
`num_drones()`를 사용하여 농장에 이미 있는 드론 수를 가져옵니다.


## 예시:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

이렇게 하면 첫 번째 드론이 수평으로 움직이며 더 많은 드론을 생성합니다. 생성된 드론은 수직으로 움직이며 경로에 있는 모든 것을 수확합니다.

사용 가능한 모든 드론이 이미 생성된 경우, `spawn_drone()`은 아무것도 하지 않고 `None`을 반환합니다.

<spoiler=힌트 보기> 모든 농장 타일에서 주어진 함수를 실행하는 이 매우 유용한 병렬 `for_all` 함수를 확인해보세요. 이 함수는 사용 가능한 모든 드론을 활용합니다.

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

forall(harvest)`

특히 유용한 패턴 중 하나는 드론을 사용할 수 있을 때 생성하고, 그렇지 않으면 직접 수행하는 것입니다.

`if not spawn_drone(task):
	task()`
</spoiler>

## 다른 드론 기다리기
`wait_for(drone)` 함수를 사용하여 다른 드론이 끝날 때까지 기다립니다. 드론을 생성할 때 `drone` 핸들을 받습니다.
`wait_for(drone)`는 다른 드론이 실행하던 함수의 반환 값을 반환합니다.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

드론을 생성하는 데는 시간이 걸리므로, 사소한 일마다 새 드론을 생성하는 것은 좋지 않습니다.

## 공유 메모리 없음
각 드론은 자체 메모리를 가지고 있으며 다른 드론의 전역 변수를 직접 읽거나 쓸 수 없습니다.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

새 드론이 전역 `x`의 자체 복사본을 증가시켰기 때문에 이것은 `0`을 출력합니다. 이는 첫 번째 드론의 `x`에 영향을 미치지 않습니다.

## 경쟁 상태
여러 드론이 동시에 같은 농장 타일과 상호작용할 수 있습니다. 두 드론이 같은 tick 동안 같은 타일과 상호작용하면, 두 상호작용 모두 발생하지만, 상호작용 순서에 따라 결과가 달라질 수 있습니다.

예를 들어, 드론 `0`과 `1`이 거의 다 자란 같은 나무 위에 있다고 상상해보세요.
드론 `0`은 다음을 호출합니다.
`use_item(Items.Fertilizer)`
드론 `1`은 다음을 호출합니다.
`harvest()`

이러한 동작이 동시에 발생하면, 나무는 먼저 비료를 받고 그 다음에 수확됩니다. 이 경우 나무를 얻게 됩니다. 하지만 드론 `1`이 약간 더 빠르면, 나무는 비료를 받기 전에 수확되어 나무를 얻지 못할 것입니다.
이것을 "경쟁 상태(race condition)"라고 합니다. 이는 연산이 수행되는 순서에 따라 결과가 달라지는 병렬 프로그래밍에서 흔히 발생하는 문제입니다.

여러 드론이 같은 위치에서 동시에 같은 코드를 실행할 때 발생할 수 있는 또 다른 문제 상황은 다음과 같습니다.
`if get_water() < 0.5:
    use_item(Items.Water)`

여러 드론이 이것을 동시에 실행하면, 모두 첫 번째 줄을 실행하여 `if` 블록에 들어가게 됩니다. 그런 다음 모두 물을 사용하여 많은 양을 낭비하게 됩니다.
한 드론이 두 번째 줄에 도달할 때쯤에는 다른 드론이 그 사이에 타일에 물을 주었기 때문에 `get_water()`가 더 이상 `0.5`보다 작지 않을 수 있습니다.