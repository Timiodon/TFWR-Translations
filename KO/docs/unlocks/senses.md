# 감각
이제 드론이 볼 수 있습니다!

`get_pos_x()`와 `get_pos_y()` 함수는 드론의 현재 x와 y 위치를 반환합니다. 시작 위치에서는 둘 다 `0`입니다. x 위치는 `East` 방향으로 타일마다 `1`씩 증가하고, y 위치는 `North` 방향으로 타일마다 `1`씩 증가합니다.

`num_items(item)`은 해당 아이템을 몇 개 가지고 있는지 반환합니다.
예를 들어 `num_items(Items.Hay)`는 가지고 있는 건초의 양을 반환합니다.

`get_entity_type()`과 `get_ground_type()`은 드론 아래에 있는 entity나 땅의 종류를 반환합니다.

덤불 위에 있다면 공중제비를 합니다:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 키워드도 이제 해금되었습니다! `None`은 값이 없음을 나타내는 값입니다.
예를 들어, `return` 문이 없는 함수는 실제로 `None`을 반환합니다.

`get_entity_type()`은 드론 아래에 entity가 없으면 `None`을 반환합니다.
