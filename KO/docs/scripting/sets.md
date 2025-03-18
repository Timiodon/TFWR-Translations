# Sets
Sets는 [dictionaries](docs/scripting/dicts.md)와 비슷하지만, 값이 없습니다. 그냥 순서가 없는 키들의 집합입니다.

Dictionaries처럼 생성하지만, 값이 없습니다.  
`set = {North, East, West}`

빈 set을 만들려면 `set()`을 사용하세요. 참고로 `{}`는 빈 dictionary를 만듭니다.

새로운 요소를 set에 추가하려면 `set.add(elem)`을 사용하세요.

set에서 요소를 제거하려면 `set.remove(elem)`을 사용하세요.

set이 요소를 포함하고 있는지 확인하려면 `if elem in set:`을 사용하세요.

set의 모든 요소를 반복하려면 `for elem in set:`을 사용하세요.  
더 큰 set일수록 `in` 연산자가 list보다 훨씬 빠르게 작동합니다.

Dictionaries처럼 Sets도 순서가 없으므로, 요소들이 반복되는 순서는 보장되지 않습니다.

또한, Sets의 요소들은 유일하기 때문에, 이미 있는 요소를 추가해도 set은 변하지 않습니다.