# 胡萝卜

在你能够用 `plant(Entities.Carrot)` 种植胡萝卜之前，你需要先犁地。这会将地面变成 `Grounds.Soil`。要犁地，只需简单调用 `till()`。再次调用 `till()` 会将地面变回 `Grounds.Grassland`。

种植胡萝卜需要消耗木材和干草。这些物品在调用 `plant(Entities.Carrot)` 时会被自动移除。

你可以在胡萝卜的 [专属页面](objects/carrot) 查看种植它的费用。