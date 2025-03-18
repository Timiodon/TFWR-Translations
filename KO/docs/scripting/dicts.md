# Dictionaries
Dictionaries는 실제 사전이 단어를 정의로 매핑하는 방식과 동일하게 키를 값으로 매핑할 수 있는 데이터 구조입니다. 키 값을 빠르게 검색할 수 있습니다.

Dictionary는 다음과 같이 생성할 수 있습니다:
`rotation = {North:East, East:South, South:West, West:North}`

콜론 앞의 표현식은 키이고, 콜론 뒤의 표현식은 키가 매핑되는 값입니다. 위의 dictionary는 각 방향을 오른쪽 방향으로 매핑합니다.

드론의 위치를 그 아래에 있는 entity로 매핑한 또 다른 예제입니다.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

키에 매핑된 값을 접근하는 것은 리스트의 요소에 접근하는 것과 유사합니다:
`value = dict[key]`

예제:
`orientation = rotation[South]`
이는 `orientation`을 `West`로 설정합니다.

Dictionary에 새로운 키-값 쌍을 추가하려면 다음과 같이 할 수 있습니다:
`dict[key] = value`

예제:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
이는 현재 위치에 저장된 entity를 업데이트합니다.

키는 고유하므로 dictionary에 이미 존재하는 키를 추가하면 이전 값을 덮어씁니다.

`dict.pop(key)`을 사용하여 `dict`에서 키-값 쌍을 제거하세요.

`key in dict`는 `key`가 `dict`에 있는 경우 `True`로, 그렇지 않으면 `False`로 평가됩니다. 따라서 `if key in dict:`를 사용하여 `dict`가 키를 포함하는지 확인할 수 있습니다.

반복문에서 dictionary를 사용하면 모든 키를 반복할 수 있습니다:
`for key in dict:
	value = dict[key]`

키가 반복되는 순서에 대한 보장은 없습니다.

[Sets](docs/scripting/sets.md)도 참고하세요.