# List
List는 단일 변수에 여러 값을 저장하는 쉬운 방법입니다.
다음과 같이 새 list를 만들 수 있습니다:

`list = [2, True, Items.Hay]`

이제 list는 `2`, `True`, `Items.Hay` 값을 포함합니다.
List는 비어있을 수도 있습니다:

`empty_list = []`

인덱스를 사용하여 list의 요소에 접근할 수 있습니다. 인덱스는 첫 번째 요소에 대해 `0`, 두 번째 요소에 대해 `1`, 세 번째 요소에 대해 `2`... 입니다.

당근을 심습니다
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

for 루프를 사용하여 list를 반복할 수 있습니다. 다음 예시는 list의 모든 요소를 합산합니다.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
이제 `sum`은 `18`입니다

다음 list 메서드를 사용하면 요소를 추가하고 제거할 수 있습니다:

`list.append(elem)`는 list의 끝에 요소를 추가합니다:

`list = [2, 6, 12]
list.append(7)`
이제 `list`는 `[2, 6, 12, 7]`입니다

`list.remove(elem)`는 list에서 요소의 첫 번째 발생을 제거합니다:

`list = [1, 2, 4, 2]
list.remove(2)`
이제 `list`는 `[1, 4, 2]`입니다

`list.insert(index, elem)`는 주어진 인덱스에 요소를 삽입합니다:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
이제 `list`는 `[Entities.Tree, Items.Wood, Items.Hay]`입니다

`list.pop(index)`는 지정된 인덱스의 요소를 제거합니다.
인덱스가 지정되지 않으면 마지막 항목이 제거됩니다.

`list = [3, 5, 8, 25]
list.pop()`
이제 `list`는 `[3, 5, 8]`입니다
`list.pop(1)`
이제 `list`는 `[3, 8]`입니다

`len()` 함수는 list의 길이를 반환합니다.
`list = [3, 2, 1]
x = len(list)`
이제 `x`는 `3`입니다

List는 참조 의미론을 가집니다. 이것은 list를 변수에 할당하면 list의 복사본을 만드는 대신 동일한 list 객체를 해당 변수에 할당한다는 것을 의미합니다.
두 변수가 동일한 list를 참조하면, list에 대한 변경 사항은 둘 모두에게 보여집니다.

`a = [1,2]
b = a
b.pop()`
이제 `a`와 `b`는 모두 `[1]`입니다
