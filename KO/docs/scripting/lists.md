# 리스트
리스트는 여러 값을 하나의 변수에 저장할 수 있는 쉬운 방법이에요.   
이렇게 새로운 리스트를 만들 수 있습니다:

`list = [2, True, Items.Hay]`

이제 리스트에는 `2`, `True` 그리고 `Items.Hay` 값들이 들어 있습니다.   
리스트는 비어 있을 수도 있어요: 

`empty_list = []`

리스트의 요소에 접근하려면 인덱스를 사용해야 합니다. 첫 번째 요소의 인덱스는 `0`, 두 번째 요소는 `1`, 세 번째 요소는 `2`...

당근 심기
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

리스트를 반복하려면 for 루프를 사용할 수 있습니다. 다음 예제는 리스트의 모든 요소를 더합니다.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum`은 이제 `18`입니다.

다음 리스트 메서드는 요소를 추가하거나 제거하는 데 사용할 수 있습니다:

`list.append(elem)`은 리스트의 끝에 요소를 추가합니다:

`list = [2, 6, 12]
list.append(7)`
`list`는 이제 `[2, 6, 12, 7]`입니다.

`list.remove(elem)`은 리스트에서 첫 번째로 발견되는 요소를 제거합니다:

`list = [1, 2, 4, 2]
list.remove(2)`
`list`는 이제 `[1, 4, 2]`입니다.

`list.insert(index, elem)`은 주어진 인덱스에 요소를 삽입합니다:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list`는 이제 `[Entities.Tree, Items.Wood, Items.Hay]`입니다.

`list.pop(index)`은 지정된 인덱스의 요소를 제거합니다.   
인덱스를 지정하지 않으면 마지막 항목이 제거됩니다.

`list = [3, 5, 8, 25]
list.pop()`
`list`는 이제 `[3, 5, 8]`입니다.
`list.pop(1)`
`list`는 이제 `[3, 8]`입니다.

`len()` 함수는 리스트의 길이를 반환합니다.   
`list = [3, 2, 1]
x = len(list)`
`x`는 이제 `3`입니다.

리스트는 참조 의미 체계를 가지고 있습니다.   
이는 리스트를 변수에 할당하면, 리스트의 복사본을 만드는 것이 아니라 같은 리스트 객체를 그 변수에 할당한다는 의미입니다.   
두 변수가 동일한 리스트를 참조하면, 리스트에 대한 변경 사항은 두 변수 모두에 반영됩니다.

`a = [1,2]
b = a
b.pop()`
`a`와 `b`는 이제 둘 다 `[1]`입니다.