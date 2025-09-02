# 당근
`plant(Entities.Carrot)`으로 당근을 심기 전에, 땅을 갈아야 해요. 그러면 땅이 `Grounds.Soil`로 바뀔 거예요. 땅을 갈려면 `till()`을 호출하면 돼요. `till()`을 다시 호출하면 `Grounds.Grassland`로 다시 바뀌어요.

당근을 심는 데는 나무와 건초가 들어요. 이 아이템들은 `plant(Entities.Carrot)`을 호출할 때 자동으로 제거돼요.

어떤 식물이든 그 비용은 [자체 페이지](objects/carrot)에서 볼 수 있어요.