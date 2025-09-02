# 리스트
리스트는 여러 값을 하나의 변수에 저장하는 쉬운 방법이에요.
다음과 같이 새 리스트를 만들 수 있어요:

`list = [2, True, Items.Hay]`

이제 리스트는 `2`, `True`, `Items.Hay` 값을 포함해요.
리스트는 비어 있을 수도 있어요:

`empty_list = []`

리스트의 요소는 인덱스로 접근할 수 있어요. 인덱스는 첫 번째 요소가 `0`, 두 번째 요소가 `1`, 세 번째 요소가 `2`... 이런 식이에요.

당근을 심어요
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

for 루프를 사용하여 리스트를 반복할 수 있어요. 다음 예시는 리스트의 모든 요소를 합산해요.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum`은 이제 `18`이 돼요

다음 리스트 메서드들을 사용하여 요소를 추가하고 제거할 수 있어요:

`list.append(elem)`는 리스트의 끝에 요소를 추가해요:

`list = [2, 6, 12]
list.append(7)`
`list`는 이제 `[2, 6, 12, 7]`이 돼요

`list.remove(elem)`는 리스트에서 요소의 첫 번째 항목을 제거해요:

`list = [1, 2, 4, 2]
list.remove(2)`
`list`는 이제 `[1, 4, 2]`가 돼요

`list.insert(index, elem)`는 주어진 인덱스에 요소를 삽입해요:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list`는 이제 `[Entities.Tree, Items.Wood, Items.Hay]`가 돼요

`list.pop(index)`는 지정된 인덱스의 요소를 제거해요.
인덱스가 지정되지 않으면 마지막 항목이 제거돼요.

`list = [3, 5, 8, 25]
list.pop()`
`list`는 이제 `[3, 5, 8]`이 돼요
`list.pop(1)`
`list`는 이제 `[3, 8]`이 돼요

`len()` 함수는 리스트의 길이를 반환해요.
`list = [3, 2, 1]
x = len(list)`
`x`는 이제 `3`이 돼요

리스트는 참조 의미론을 가져요. 이것은 리스트를 변수에 할당하면 리스트의 복사본을 만드는 대신 동일한 리스트 객체를 해당 변수에 할당한다는 의미예요.
두 변수가 동일한 리스트를 참조하면, 리스트에 대한 변경 사항이 두 변수 모두에 반영돼요.

`a = [1,2]
b = a
b.pop()`
`a`와 `b`는 이제 둘 다 `[1]`이 돼요