# Continue
continue는 루프의 현재 반복을 멈추고 가장 안쪽 루프의 다음 반복으로 넘어갈 수 있게 해줘요.

`for i in range(10):
	continue
    print("this is never printed")`

이 코드는 루프의 모든 `10`번의 반복을 실행하지만, `continue` 뒤의 `print` 문은 항상 건너뛰어요.

`while` 루프에서도 작동해요.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

이 코드는 `can_harvest()`가 `True`일 때만 `harvest()`를 호출해요. 
이것은 다음과 같은 효과를 가져요.

`while True:
	if can_harvest():
		harvest()`

중첩된 루프에서 `continue`는 항상 가장 안쪽 루프에 영향을 줘요.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`