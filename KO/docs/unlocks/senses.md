# 센서
드론이 이제 볼 수 있어요!

`get_pos_x()`와 `get_pos_y()` 함수는 드론의 현재 x와 y 위치를 반환해요. 시작 위치에서는 둘 다 `0`입니다. x 위치는 `East` 방향으로 타일 한 칸 이동할 때마다 `1`씩 증가하고, y 위치는 `North` 방향으로 타일 한 칸 이동할 때마다 `1`씩 증가해요.

`num_items(item)`은 여러분이 얼마나 많은 아이템을 가지고 있는지 반환해요.
예를 들어, `num_items(Items.Hay)`는 여러분이 얼마나 많은 건초를 가지고 있는지 반환합니다.

`get_entity_type()`과 `get_ground_type()`은 드론 아래에 있는 entity 또는 ground의 유형을 반환해요.

덤불 위에 있다면 회전을 해보세요:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 키워드도 이제 사용 가능해요! `None`은 값이 없음을 나타내는 값입니다.
예를 들어, `return` 문이 없는 함수는 실제로 `None`을 반환해요.

`get_entity_type()`은 드론 아래에 entity가 없을 때 `None`을 반환합니다.