# Set
Set은 [dictionaries](docs/scripting/dicts.md)와 같지만 value가 없습니다. 순서가 없는 key의 집합일 뿐입니다.

Dictionary처럼 만들어지지만 value가 없습니다.
`set = {North, East, West}`

빈 set을 만들려면 `set()`을 사용하세요. `{}`는 빈 dictionary를 만듭니다.

set에 새 요소를 추가하려면 `set.add(elem)`을 사용하세요.

set에서 요소를 제거하려면 `set.remove(elem)`을 사용하세요.

set에 요소가 포함되어 있는지 확인하려면 `if elem in set:`를 사용하세요.

set의 모든 요소를 반복하려면 `for elem in set:`를 사용하세요.
더 큰 set의 경우 `in` 연산자는 list에서보다 훨씬 빠르게 수행됩니다.

Dictionary와 마찬가지로 set은 순서가 없으므로 요소가 반복되는 순서에 대한 보장은 없습니다.

또한, set의 요소는 고유하므로 이미 set에 있는 요소를 추가해도 set이 변경되지 않습니다.