# For 루프
`for` 루프는 파이썬에서처럼 작동합니다. (일부 언어에서는 foreach 루프라고 불리며, C 스타일 for 루프와는 다른 것입니다).

`for i in sequence:
	# i로 무언가를 하세요`

`while` 루프와 유사하게, `for` 루프도 코드 블록을 반복적으로 호출합니다. 조건에 따라 반복하는 대신, 시퀀스의 각 요소에 대해 한 번씩 루프 본문을 실행합니다.

## 구문
for 루프는 다음과 같습니다:

`for variable_name in sequence:
	#코드 블록`

`variable_name`은 원하는 어떤 이름이든 될 수 있습니다. 이것은 시퀀스의 현재 요소를 저장하는 변수입니다. `sequence`는 숫자 범위와 같이 반복할 수 있는 값이어야 합니다. 코드 블록은 루프 변수가 해당 요소에 할당된 상태로 모든 요소에 대해 실행됩니다.

## 시퀀스
[범위](functions/range)      <unlock=lists>[리스트](docs/scripting/lists.md)      </unlock><unlock=functions>[튜플](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## 예시
`for i in range(5):
    harvest()`

이 루프는 본문을 고정된 횟수만큼 실행합니다. 이것은 본질적으로 다음과 같이 쓰는 것과 같습니다.

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

따라서 `harvest()`를 5번 호출합니다.

참조: [Break](docs/scripting/break.md) 및 [Continue](docs/scripting/continue.md)