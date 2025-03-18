# 비용
모든 비용은 아이템을 숫자에 매핑하는 dictionary로 나타낼 수 있어.

`get_cost()` 함수는 그런 dictionary를 반환해. 식물이나 언락의 비용을 반환해 주지.

`get_cost(Entities.Pumpkin)`
는 `{Items.Carrot:1}`를 반환해.

언락을 위한 경우, 원하는 언락 레벨에 대해 비용을 얻으려면 선택적 두 번째 인수를 전달할 수 있어. 기본값은 현재 언락 레벨이야.

`get_cost(Unlocks.Loops, 0)`
는 `{Items.Hay:5}`를 반환해.

이미 최대 레벨에 도달한 언락의 경우, `get_cost()`는 `None`을 반환해.

이렇게 사용할 수 있어:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`