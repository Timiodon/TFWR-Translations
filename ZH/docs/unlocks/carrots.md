# 胡萝卜
在你用 `plant(Entities.Carrot)` 种植胡萝卜之前，你必须先耕地。这会将地面变为 `Grounds.Soil`。要耕地，只需调用 `till()`。再次调用 `till()` 会将其变回 `Grounds.Grassland`。

种植胡萝卜需要消耗木材和干草。调用 `plant(Entities.Carrot)` 时，这些物品会自动被移除。

你可以在任何植物的[专属页面](objects/carrot)上看到它的成本。