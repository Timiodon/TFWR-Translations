# If문
if, elif, else를 사용하여 코드를 조건부로 실행할 수 있어요.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 문법
`if`문은 어떤 조건이 `True`일 경우에만 코드를 실행할 수 있게 해줘요. 반복하지 않는 `while` 루프와 같아요.
`if`는 `while` 루프처럼 조건을 받고, 조건이 `True`로 평가되면 if 코드 블록을 실행해요:

`#condition이 True이면 재주넘기
if condition:
	do_a_flip()`

if 뒤에 `else`를 추가하여 조건이 `False`로 평가될 때 실행될 코드를 정의할 수도 있어요.

`condition`이 True이면 재주를 넘고, 그렇지 않으면 수확해요.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`는 else if의 줄임말이에요.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

는 다음과 같이 줄일 수 있어요:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`