# 자동 해금
게임을 완전히 자동화하려면 `unlock()` 함수를 사용하여 기능을 자동으로 해금할 수 있습니다.
예를 들어, `unlock(Unlocks.Speed)`와 `unlock(Unlocks.Expand)`를 사용하여 속도 및 확장 기능을 해금할 수 있습니다.

해금 비용을 확인하려면 식물이나 아이템에 하던 것처럼 `get_cost()` 함수를 사용하면 됩니다.
예시:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}`를 반환합니다

특정 해금을 몇 개나 가지고 있는지 알고 싶다면 `num_unlocked(unlock)` 함수를 사용하세요.

예를 들어, `num_unlocked(Unlocks.Speed)`는 가지고 있는 속도 업그레이드 수를 반환합니다.

`num_unlocked(Unlocks.Senses)`는 감각이 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환합니다.

Items, Entities 또는 Grounds에도 `num_unlocked()`를 사용할 수 있습니다. 이것은 해금되었으면 `1`을, 그렇지 않으면 `0`을 반환합니다.

`num_unlocked(Unlocks.Carrots)`는 해금/업그레이드된 횟수를 반환하니 주의하세요.
`num_unlocked(Items.Carrot)`는 `0` 또는 `1`만 반환합니다. (다른 식물도 마찬가지)
