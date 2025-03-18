# Functions
새로운 함수를 정의하려면 `def` 키워드를 사용하세요:
`def f(arg1, arg2 = False):
	#function code`

함수를 호출하려면 호출 연산자인 `()`를 사용할 수 있습니다:
`f(42)`

함수의 로컬 및 전역 변수에 대해 알아보려면 [Scopes](docs/scripting/scopes.md)를 참조하세요.

## Introduction
`harvest()`와 같은 내장 함수는 이미 보셨을 겁니다.
자신만의 함수를 정의할 수도 있으며, 이를 통해 코드를 모듈화된 방식으로 구조화할 수 있습니다. 기본적으로 코드 블록에 이름을 붙여 언제든지 호출할 수 있도록 합니다.

## Function Definitions
예를 들어, 드론을 여러 번 이동시키는 함수를 정의할 수 있습니다.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` 키워드는 이것이 함수 정의임을 나타냅니다. 
`move_n_dir`은 함수에 할당되는 이름입니다. 이는 유효한 변수 이름이어야 하며 함수 호출에 사용됩니다.
`n`과 `dir`은 매개변수입니다. 이들은 함수에 전달되는 값을 저장하는 변수입니다 (이 값들은 인수라고도 합니다). 함수 정의에 원하는 만큼의 매개변수를 추가할 수 있습니다.
`:` 다음에는 함수가 호출될 때 실행될 코드 블록이 나옵니다.

위의 정의를 통해 다음 코드는 드론을 `10` 타일 `North`로, `2` 타일 `West`로 이동시킵니다.

`move_n_dir(10, North)
move_n_dir(2, West)`

`def function():`를 보면 다음과 같은 변수 할당으로 생각해야 합니다:
`function = create_new_function_object()`
모든 할당과 마찬가지로, 할당되기 전에 변수를 사용할 수 없습니다!
함수 호출 전에 `def` 문이 실행되어야 합니다.
이 코드는 오류가 발생할 것입니다:

`func()
def func():
	pass`

## Return Values
값을 반환하도록 하려면 `return` 키워드를 사용하세요. 
예를 들어, 다음 함수는 베타적 OR 연산을 정의합니다. 베타적 OR 연산은 한 값이 `True`이고 다른 값이 `False`일 때 `True`를 반환합니다:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md)은 여러 값을 반환하는 것을 허용합니다.

## Default Arguments
인수를 전달하지 않았을 경우 사용할 기본값을 할당할 수도 있습니다.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

기본값이 있는 인수 뒤에는 기본값이 없는 인수를 사용할 수 없습니다.

## Advanced Function Usage
함수는 다른 값들과 마찬가지로 값이며, `def` 문은 단순히 함수에 이름을 할당하는 할당문처럼 동작합니다.
이렇게 함으로써 다음과 같은 작업들이 가능합니다:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

여기서 `f()`는 함수 `f`를 호출하고, 새로운 함수 `d`를 정의하고 반환합니다. 두 번째 `()`가 반환된 함수를 실행하고 flip을 수행합니다.
(이런 작업은 일반적으로 무슨 일이 벌어지는지 확인하기 어려우므로 좋지 않은 아이디어입니다)

다른 함수를 인수로 받는 함수는 당신이 정말 창의적으로 작업할 수 있게 합니다:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

이 코드는 드론을 `North` 방향으로 10번 이동시키고, 비료를 10번 사용합니다.