# 자동 해금
게임을 완전히 자동화하려면 `unlock()` 함수를 사용하여 기능을 자동으로 해금할 수 있습니다.
예를 들어 `unlock(Unlocks.Speed)`와 `unlock(Unlocks.Expand)`를 사용하여 속도 및 확장 기능을 해금할 수 있습니다.

해금 비용을 확인하려면, 식물이나 아이템에 하듯이 `get_cost()` 함수를 사용하면 됩니다.
예시:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}`를 반환합니다
