# Break
`break`는 루프를 일찍 멈출 수 있게 해줘요. `break` 문에 도달하면 즉시 가장 안쪽 루프를 빠져나와 루프 다음의 코드를 실행하기 시작해요.

`for i in range(10):
	break
print(i)`
이 코드는 `0`을 출력해요. 왜냐하면 루프의 첫 번째 반복에서 `i`가 `0`이고 그 다음에 break 문이 루프를 끝내기 때문이에요.

`while` 루프에서도 작동해요.

`while True:
	if can_harvest():
		break`

이 코드는 `can_harvest()`가 `True`가 될 때까지 `while` 루프를 실행해요. 
이것은 다음과 같은 효과를 가져요.

`while not can_harvest():
	pass`

중첩된 루프에서 `break`는 항상 가장 안쪽 루프를 빠져나와요.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`