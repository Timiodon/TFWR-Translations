# 딕셔너리
딕셔너리는 실제 사전이 단어를 그 정의에 매핑하는 것처럼 키를 값에 매핑할 수 있게 해주는 자료 구조이며, 매우 빠르게 찾아볼 수 있어요.

딕셔너리는 다음과 같이 만들 수 있어요:
`right_of = {North:East, East:South, South:West, West:North}`

콜론 앞의 표현식은 키이고, 콜론 뒤의 표현식은 키가 매핑되는 값이에요.
위의 딕셔너리는 각 방향을 그 오른쪽 방향에 매핑해요.

다음은 드론의 위치를 그 위에 있는 개체에 매핑하는 또 다른 예시예요.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

키에 매핑된 값에 접근하는 것은 리스트의 요소에 접근하는 것과 유사해요:
`value = dict[key]`

예시:
`orientation = right_of[South]`
이것은 `orientation`을 `West`로 설정해요.

딕셔너리에 새 키-값 쌍을 추가하려면 다음과 같이 하세요:
`dict[key] = value`

예시:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
이것은 현재 위치에 저장된 개체를 업데이트해요.

키는 고유하므로, 딕셔너리에 이미 존재하는 키를 추가하면 이전 값을 덮어써요.

`dict`에서 키-값 쌍을 제거하려면 `dict.pop(key)`를 사용하세요.

`key in dict`는 `key`가 `dict`의 키이면 `True`로, 그렇지 않으면 `False`로 평가돼요.
따라서 `if key in dict:`를 사용하여 `dict`에 키가 포함되어 있는지 확인할 수 있어요.

딕셔너리를 for 루프에 넣으면 모든 키를 반복할 수 있어요:
`for key in dict:
	value = dict[key]`

키가 반복되는 순서는 보장되지 않아요.

참고: [세트](docs/scripting/sets.md)