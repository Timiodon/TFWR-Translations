# For 루프
`for` 루프는 Python에서처럼 작동해. (몇몇 언어에서는 foreach 루프라고 부르고, C 스타일 for 루프와는 다르니 헷갈리지 마.)

`for i in sequence:
	#do something with i`

`while` 루프와 비슷하게, `for` 루프도 코드 블록을 반복 호출해. 조건에 기반한 루프 대신, 시퀀스의 각 요소에 대해 한 번씩 루프 본문을 실행해.

## 문법
for 루프는 이렇게 보이는데:

`for variable_name in sequence:
	#code block`

`variable_name`은 네가 선택할 수 있는 아무 이름이나 될 수 있어. 시퀀스의 현재 요소를 저장하는 변수야. `sequence`는 range나 숫자처럼 반복 가능한 값이어야 해. 모든 요소에 대해 루프 변수가 그 요소에 할당되면서 코드 블록이 실행돼.

## 시퀀스
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## 예제
`for i in range(5):
    harvest()`

이 루프는 본문을 고정된 횟수만큼 실행해. 이는 기본적으로 다음과 똑같아:

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

이렇게 `harvest()`를 5번 호출해.

또한 [Break](docs/scripting/break.md)와 [Continue](docs/scripting/continue.md)도 참고해봐.