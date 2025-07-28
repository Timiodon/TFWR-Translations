# Import
모든 코드를 단일 파일에 넣으면 금방 관리하기 어려워집니다.
`import` 문은 다른 파일에서 함수와 전역 변수를 가져올 수 있게 합니다.

`import filename`

이것은 가장 간단한 형태의 import 문입니다. `filename`이라는 이름의 파일에 정의된 모든 것에 접근할 수 있게 해줍니다. 게임의 각 창은 파일이며, 파일 이름은 창 상단에 표시되는 이름입니다.

두 개의 파일이 있는 예시입니다:
helper라는 이름의 파일:
`x = 0

def say_hello():
    print("hello from helper")`

다른 파일:
`import helper
helper.say_hello()
helper.x += 1`

여기서 `import helper`는 `helper`라는 이름의 파일을 실행하고 그 안의 모든 전역 변수에 접근할 수 있게 해줍니다.
그 다음 `.` 연산자를 사용하여 import된 모듈 내의 변수와 함수에 접근할 수 있습니다.
그래서 이 예시에서, `helper.say_hello()`는 helper 안의 `say_hello()`를 호출하고 마지막 줄은 전역 변수 x를 증가시킵니다.

`from` 구문을 사용하여 import 문이 실행되는 현재 scope로 import된 모듈의 전역 변수를 가져올 수도 있습니다.

`from helper import *`
helper의 모든 전역 변수를 import합니다.

또는

`from helper import say_hello`
helper에서 지정된 전역 변수만 import합니다.

이것도 helper 파일을 import하지만, `helper`라는 이름의 변수를 통해 접근하는 대신, `helper`의 전역 변수를 언패킹하여 지역 scope에 직접 할당합니다.

`from helper import say_hello
say_hello()`

이 형태의 import는 두 파일이 서로를 import할 때 잘 작동하지 않고, 이름 충돌로 인해 import하는 파일의 변수를 실수로 덮어쓸 수 있기 때문에 보통 권장되지 않습니다.

# 실제 작동 방식

## 요약
Import는 꽤 직관적이지 않을 수 있지만, `from file import` 대신 `import file` 구문을 사용하고, 전역 정의가 아닌 모든 것을 다음과 같이 감싸면 대부분의 문제를 피할 수 있습니다:
`if __name__ == "__main__":`

## Import 부작용
파일을 처음 import하면, 전체 파일을 실행한 다음 실행 중에 정의된 모든 변수에 접근할 수 있게 해줍니다.
같은 파일을 다시 import하면, 처음의 캐시된 모듈을 다시 반환할 뿐입니다.

이것은 import 문에 부작용이 있을 수 있다는 것을 의미합니다. `harvest()`를 호출하는 파일을 import하면, import 중에 실제로 수확을 합니다. 하지만 다시 import할 때는 파일이 한 번만 실행되므로 다시 수확하지 않습니다.

`__name__` 변수를 사용하여 이러한 부작용을 피할 수 있는 방법이 있습니다. 이 변수는 파일이 직접 실행될 때 자동으로 `"__main__"`으로 설정되고, `import`를 통해 파일이 실행될 때 파일 이름으로 설정됩니다.
파일이 import될 때 실행하고 싶지 않은 코드는 `if __name__ == "__main__":` 블록 안에 넣는 것이 좋은 관행으로 간주됩니다.

파이썬의 일반적인 파일 구조는 파일이 실행될 때 실행되어야 하는 코드를 `main()` 함수 안에 넣는 것입니다. 이렇게 하면 지역 변수(`main()` 안에 정의됨)와 import될 수 있는 전역 변수(`main()` 밖에 정의됨)를 명확하게 구분할 수 있습니다.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # 할 일

if __name__ == "__main__":
    main()`

## Import 순환
만약 파일 `a`가 파일 `b`를 import하고 파일 `b`가 파일 `a`를 import하면 어떻게 될까요?

파일 `a`:
`import b
x = 0`

파일 `b`:
`import a
def f():
    print(a.x)`

이것은 잘 작동할 것입니다. 두 파일 모두 아직 로드되지 않았고, 다른 곳에서 `import a`를 실행한다고 가정해 봅시다.

-`a`는 `import b` 줄까지 실행됩니다.
-`b`는 `import a` 줄까지 실행됩니다.
-모듈 `a`는 이미 존재하지만, `import b` 줄까지만 도달했기 때문에 `x`를 포함하지 않습니다.
-`b`는 `a`라는 변수에 절반만 로드된 모듈 `a`에 대한 참조를 저장합니다.
-`b`는 `def` 문을 실행하고 함수 `f()`를 저장합니다.
-`a`는 계속 실행되어 `x`를 초기화합니다.

누군가 `b.f()`를 호출하면, `b`가 참조하는 모듈 `a`가 이제 완전히 로드되었으므로 `0`을 정확하게 출력합니다.

이제 `from` 구문을 사용한 같은 코드를 고려해 봅시다.

파일 `a`:
`from b import *
x = 0`

파일 `b`:
`from a import *
def f():
    print(x)`

-`a`는 `from b import *` 줄까지 실행됩니다.
-`b`는 `from a import *` 줄까지 실행됩니다.
-모듈 `a`는 이미 존재하지만, 아직 완전히 실행되지는 않았습니다.
-`b`는 현재 `a`에 있는 모든 것을 자신의 전역 scope로 언패킹합니다. 이 시점에서 `a`는 `x = 0` 줄에 도달하지 않았으므로 아무것도 포함하고 있지 않아 아무것도 import되지 않습니다.
-`b`는 `def` 문을 실행하고 함수 `f()`를 저장합니다.
-`a`는 계속 실행되어 `x`를 초기화합니다.

이제 누군가 `b.f()`를 호출하면, 현재 scope에 `x`가 존재하지 않는다는 error를 받게 됩니다. 이번에는 `b`가 아직 로딩 중인 `a`에 대한 참조를 가지고 있지 않으며, import 후에 추가된 정의를 보지 못하기 때문입니다.