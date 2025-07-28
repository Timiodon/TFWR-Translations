# 당근
`plant(Entities.Carrot)`으로 당근을 심기 전에, 땅을 경작해야 합니다. 그러면 땅이 `Grounds.Soil`로 바뀝니다. 땅을 경작하려면 `till()`을 호출하면 됩니다. `till()`을 다시 호출하면 `Grounds.Grassland`로 돌아갑니다.

당근을 심는 데는 나무와 건초가 필요합니다. 이 아이템들은 `plant(Entities.Carrot)`를 호출할 때 자동으로 제거됩니다.

모든 식물의 비용은 [자체 페이지](objects/carrot)에서 확인할 수 있습니다.