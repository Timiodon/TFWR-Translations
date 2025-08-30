# 감각
이제 드론이 볼 수 있습니다! 

`get_pos_x()`와 `get_pos_y()` 함수는 드론의 현재 x와 y 위치를 반환합니다. 시작 위치에서는 둘 다 `0`입니다. x 위치는 `East` 방향으로 타일마다 `1`씩 증가하고, y 위치는 `North` 방향으로 타일마다 `1`씩 증가합니다.

`num_items(item)`은 아이템을 몇 개 가지고 있는지 반환합니다.
예를 들어 `num_items(Items.Hay)`는 얼마나 많은 건초를 가지고 있는지 반환합니다.

`get_entity_type()`와 `get_ground_type()`은 드론 아래에 있는 entity 또는 땅의 종류를 반환합니다.

덤불 위에 있으면 공중제비를 합니다:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 키워드도 이제 해금되었습니다! `None`은 값이 없음을 나타내는 값입니다.
예를 들어 `return` 문이 없는 함수는 실제로는 `None`을 반환합니다.

드론 아래에 entity가 없으면 `get_entity_type()`는 `None`을 반환합니다.


특정 해금을 몇 개 가지고 있는지 알아보려면 `num_unlocked(unlock)` 함수를 사용하세요.

예를 들어, `num_unlocked(Unlocks.Speed)`는 가지고 있는 속도 업그레이드 수를 반환합니다.

`num_unlocked(Unlocks.Senses)`는 감각이 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환합니다.

아이템, Entity 또는 땅에도 `num_unlocked()`를 사용할 수 있습니다. 이 경우 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환합니다.

주의하세요. `num_unlocked(Unlocks.Carrots)`는 해금/업그레이드된 횟수를 반환합니다.
`num_unlocked(Items.Carrot)`는 `0` 또는 `1`만 반환합니다. (다른 식물도 마찬가지)