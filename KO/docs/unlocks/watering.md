# 물 주기
식물은 물을 주면 더 빨리 자랍니다. 땅의 수위는 `0`에서 `1`까지 입니다. 함수 `get_water()`는 그 위의 땅의 수위를 반환합니다.

식물의 성장 속도는 수위 `0`일 때 1배 속도에서 수위 `1`일 때 5배 속도로 선형적으로 증가합니다.

땅은 시간이 지남에 따라 마릅니다: 평균적으로, 현재 수위의 1%가 초당 감소하지만, 약간의 무작위 변동이 있습니다. 높은 수위를 유지하는 것은 낮은 수위를 유지할 때보다 훨씬 더 많은 물이 필요합니다.

식물에게 물을 사용할 수 있습니다. 10초마다 자동으로 한 탱크의 물이 인벤토리에 추가됩니다. `Unlocks.Watering`를 업그레이드하면 10초마다 추가로 한 탱크의 물이 제공됩니다.

한 탱크는 `0.25`의 물을 담고 있습니다.

어떤 땅 위에서든 `use_item(Items.Water)`를 호출해 그 땅에 물을 주세요.