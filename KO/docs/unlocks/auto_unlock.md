# 자동 잠금 해제
게임을 완전히 자동화하려면 `unlock()` 함수를 사용하여 기능을 자동으로 잠금 해제할 수 있어요.
예를 들어, `unlock(Unlocks.Speed)`와 `unlock(Unlocks.Expand)`를 사용하여 속도와 확장 기능을 잠금 해제할 수 있죠.

잠금 해제의 비용을 결정하려면 식물이나 아이템에 사용하는 것처럼 `get_cost()` 함수를 간단하게 사용하세요.
예시:
`get_cost(Unlocks.Loops)`
는 `{Items.Hay:5}`를 반환해요.

특정 잠금 해제를 몇 번 했는지 알아보고 싶다면 `num_unlocked(unlock)` 함수를 사용하세요.

예를 들어, `num_unlocked(Unlocks.Speed)`는 속도 업그레이드를 몇 번 했는지 반환해요.

`num_unlocked(Unlocks.Senses)`는 감지가 잠금 해제되면 `1`을, 그렇지 않으면 `0`을 반환해요.

`num_unlocked()`를 아이템, 엔티티 또는 필드에 사용할 수도 있어요. 잠금 해제되면 `1`을, 그렇지 않으면 `0`을 반환합니다.

주의하세요, `num_unlocked(Unlocks.Carrots)`는 잠금 해제/업그레이드된 횟수를 반환하고,
`num_unlocked(Items.Carrot)`는 `0` 또는 `1`만 반환해요. (다른 식물도 마찬가지입니다.)