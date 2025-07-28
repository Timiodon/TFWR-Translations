# Dictionaries
Dictionary는 실제 사전이 단어를 정의에 매핑하는 것과 같은 방식으로 key를 value에 매핑할 수 있게 해주는 데이터 구조이며, 매우 빠르게 찾아볼 수 있습니다.

A dictionary는 다음과 같이 만들 수 있습니다:
`right_of = {North:East, East:South, South:West, West:North}`

콜론 앞의 표현식은 key이고 콜론 뒤의 표현식은 key가 매핑되는 value입니다.
위의 dictionary는 각 방향을 그 오른쪽 방향에 매핑합니다.

드론의 위치를 그 위의 entity에 매핑하는 또 다른 예입니다.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

key에 매핑된 value에 접근하는 것은 list의 요소에 접근하는 것과 유사합니다:
`value = dict[key]`

예시:
`orientation = right_of[South]`
이것은 `orientation`을 `West`로 설정합니다.

dictionary에 새로운 key-value 쌍을 추가하려면 다음과 같이 합니다:
`dict[key] = value`

예시:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
이것은 현재 위치에 저장된 entity를 업데이트합니다.

Key는 고유하므로, dictionary에 이미 존재하는 key를 추가하면 이전 value를 덮어씁니다.

`dict`에서 key-value 쌍을 제거하려면 `dict.pop(key)`를 사용하세요.

`key in dict`는 `key`가 `dict`의 key이면 `True`로, 그렇지 않으면 `False`로 평가됩니다.
따라서 `if key in dict:`를 사용하여 `dict`에 key가 포함되어 있는지 확인할 수 있습니다.

for 루프에 dictionary를 넣으면 모든 key를 반복할 수 있습니다:
`for key in dict:
	value = dict[key]`

key가 반복되는 순서에 대한 보장은 없습니다.

참조: [Sets](docs/scripting/sets.md)