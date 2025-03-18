# If
`if`, `elif`, `else`를 사용하여 조건에 따라 코드를 실행할 수 있어.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntax
`if`는 특정 조건이 `True`일 때만 코드를 실행하도록 해 줘. 이건 반복되지 않는 `while` 루프랑 비슷해. `if`는 `while` 루프처럼 조건을 받아서, 그 조건이 `True`로 평가되면 if 코드 블록을 실행해:

`#조건이 True일 때 뒤집기
if condition:
	do_a_flip()`

또한, 조건이 `False`로 평가될 때 실행될 코드를 정의하기 위해 `else`를 if 뒤에 추가할 수도 있어.

조건이 True일 때 뒤집기, 그렇지 않으면 수확해.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`는 else if를 줄인 거야.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

이걸 줄이면 이렇게 돼:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`