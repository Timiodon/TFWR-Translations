# 메가 팜
이 엄청나게 강력한 해금은 여러 드론에 접근할 수 있게 해줘요.

이전처럼, 여전히 드론 하나로 시작해요. 추가 드론은 먼저 생성해야 하며 프로그램이 종료된 후 사라져요.
각 드론은 자신만의 별도 프로그램을 실행해요. 새 드론은 `spawn_drone(function)` 함수를 사용하여 생성할 수 있어요.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

이것은 `spawn_drone(function)` 명령을 실행한 드론과 같은 위치에 새 드론을 생성해요. 새 드론은 그런 다음 지정된 함수를 실행하기 시작해요. 끝나면 자동으로 사라져요.

드론들은 서로 충돌하지 않아요.

생성할 수 있는 최대 드론 수를 얻으려면 `max_drones()`를 사용하세요.
농장에 이미 있는 드론 수를 얻으려면 `num_drones()`를 사용하세요.


## 예시:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

이것은 첫 번째 드론이 수평으로 움직이면서 더 많은 드론을 생성하게 할 거예요. 생성된 드론들은 그런 다음 수직으로 움직이며 경로상의 모든 것을 수확할 거예요.

사용 가능한 모든 드론이 이미 생성되었다면, `spawn_drone()`은 아무것도 하지 않고 `None`을 반환할 거예요.

<spoiler=힌트 보기> 이 매우 유용한 병렬 `for_all` 함수를 확인해보세요. 어떤 함수든 받아서 모든 농장 타일에서 실행해요. 이를 위해 사용 가능한 모든 드론을 활용하죠.

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

특히 유용한 패턴 중 하나는 드론이 사용 가능하면 생성하고 그렇지 않으면 직접 하는 것이에요.

`if not spawn_drone(task):
	task()`
</spoiler>

## 다른 드론 기다리기
다른 드론이 끝날 때까지 기다리려면 `wait_for(drone)` 함수를 사용하세요. 드론을 생성할 때 `drone` 핸들을 받아요.
`wait_for(drone)`는 다른 드론이 실행하던 함수의 반환 값을 반환해요.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

드론을 생성하는 데는 시간이 걸리므로, 사소한 일마다 새 드론을 생성하는 것은 좋은 생각이 아니에요.

## 공유 메모리 없음
각 드론은 자신만의 메모리를 가지고 있으며 다른 드론의 전역 변수를 직접 읽거나 쓸 수 없어요.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

새 드론이 자신만의 전역 `x` 사본을 증가시켰고, 이것이 첫 번째 드론의 `x`에 영향을 주지 않기 때문에 `0`을 출력할 거예요.

## 경쟁 상태
여러 드론이 동시에 같은 농장 타일과 상호 작용할 수 있어요. 두 드론이 같은 tick 동안 같은 타일과 상호 작용하면, 두 상호 작용 모두 발생하지만 결과는 상호 작용 순서에 따라 달라질 수 있어요.

예를 들어, 드론 `0`과 `1`이 거의 다 자란 같은 나무 위에 있다고 상상해보세요.
드론 `0`은 다음을 호출해요
`use_item(Items.Fertilizer)`
드론 `1`은 다음을 호출해요
`harvest()`

이 동작들이 동시에 발생하면, 나무는 먼저 비료를 받고 그 다음에 수확될 거예요. 그 경우, 나무에서 목재를 얻게 될 거예요. 하지만, 드론 `1`이 약간 더 빠르다면, 나무는 비료를 받기 전에 수확될 것이고, 목재를 얻지 못할 거예요.
이것을 "경쟁 상태"라고 해요. 이것은 병렬 프로그래밍에서 흔한 문제이며, 결과가 작업이 수행되는 순서에 따라 달라지는 경우예요.

여러 드론이 동시에 같은 위치에서 같은 코드를 실행할 때 발생할 수 있는 또 다른 문제 상황이에요.
`if get_water() < 0.5:
    use_item(Items.Water)`

여러 드론이 이것을 동시에 실행하면, 모두 첫 번째 줄을 실행하여 `if` 블록으로 들어가게 돼요. 그런 다음, 모두 물을 사용하여 많이 낭비하게 될 거예요.
드론이 두 번째 줄에 도달할 때쯤이면, 다른 드론이 그 사이에 타일에 물을 주었기 때문에 `get_water()`가 더 이상 `0.5` 미만이 아닐 수도 있어요.