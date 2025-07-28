# If
if, elif, else를 사용하여 코드를 조건부로 실행할 수 있습니다.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 구문
`if`는 어떤 조건이 `True`일 때만 코드를 실행할 수 있게 합니다. 이것들은 반복하지 않는 `while` 루프와 같습니다.
`if`는 `while` 루프와 마찬가지로 조건을 받아서, 조건이 `True`로 평가되면 if 코드 블록을 실행합니다:

`#condition이 True이면 공중제비를 합니다
if condition:
	do_a_flip()`

if 뒤에 `else`를 추가하여 조건이 `False`로 평가될 때 실행될 코드를 정의할 수도 있습니다.

`condition`이 True이면 공중제비를 하고, 그렇지 않으면 수확합니다.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`는 else if의 줄임말입니다.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

다음과 같이 줄일 수 있습니다:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
