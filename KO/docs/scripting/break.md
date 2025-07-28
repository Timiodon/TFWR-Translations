# Break
`break`는 루프를 일찍 멈추게 합니다. `break` 문에 도달하면 가장 안쪽 루프를 즉시 빠져나와 루프 다음의 코드를 실행하기 시작합니다.

`for i in range(10):
	break
print(i)`
이 코드는 `0`을 출력합니다. 루프의 첫 번째 반복에서 `i`가 `0`이고, 그 다음 break 문이 루프를 종료하기 때문입니다.

`while` 루프에서도 작동합니다.

`while True:
	if can_harvest():
		break`

이 코드는 `can_harvest()`가 `True`가 될 때까지 `while` 루프를 실행합니다. 
이것은 다음과 같은 효과를 가집니다.

`while not can_harvest():
	pass`

중첩 루프에서 `break`는 항상 가장 안쪽 루프를 빠져나갑니다.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`