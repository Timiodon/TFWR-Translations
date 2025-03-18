# Continue
continue는 현재 반복문의 반복을 멈추고 가장 안쪽 반복문의 다음 반복으로 넘어가게 해줘.

`for i in range(10):
	continue
    print("this is never printed")`

이 코드는 반복문을 `10`번 모두 실행하지만, `continue` 이후에 있는 `print` 문은 항상 건너뛰어져.

`while` 반복문에서도 동작해.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

이 코드는 `can_harvest()`가 `True`일 때만 `harvest()`를 호출해.
이는 다음과 같은 효과를 줘.

`while True:
	if can_harvest():
		harvest()`

중첩된 반복문에서는 `continue`가 항상 가장 안쪽의 반복문에 영향을 줘.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`