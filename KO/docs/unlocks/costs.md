# 비용
모든 비용은 아이템을 숫자에 매핑하는 dictionary로 표현될 수 있습니다.

`get_cost()` 함수는 그러한 dictionary를 반환합니다. 식물이나 해금의 비용을 반환합니다.

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}`을 반환합니다

해금의 경우, 비용을 알고 싶은 해금 레벨을 두 번째 인자로 전달할 수 있습니다. 기본적으로는 현재 해금 레벨입니다.

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}`를 반환합니다

이미 최대 레벨인 해금의 경우, `get_cost()`는 `None`을 반환합니다.

다음과 같이 사용할 수 있습니다:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
