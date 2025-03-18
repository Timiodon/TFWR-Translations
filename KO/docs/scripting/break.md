# Break
`break`는 루프를 일찍 멈출 수 있게 해줘. `break` 문에 도달하면 즉시 가장 안쪽의 루프를 나가고 루프 이후의 코드를 실행하게 돼.

`for i in range(10):
	break
print(i)`
이건 `0`을 출력해, 왜냐면 루프의 첫 번째 반복에서 `i`는 `0`이고, 그다음 `break` 문이 끝내 버리기 때문이야.

`while` 루프에서도 작동해.

`while True:
	if can_harvest():
		break`

이 코드는 `while` 루프를 `can_harvest()`가 `True`일 때까지 실행해.
이것은 다음과 같은 효과가 있어

`while not can_harvest():
	pass`

중첩된 루프에서 `break`는 항상 가장 안쪽의 루프를 나가.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`