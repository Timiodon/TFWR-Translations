# 胡萝卜
调用 `plant(Entities.Carrot)` 函数可以种植胡萝卜。在种植胡萝卜之前你必须先耕地，只需调用 `till()` 函数即可耕地，将地块变为 `Grounds.Soil` 。再次调用 `till()` 则会将地块变回 `Grounds.Grassland`。


种植胡萝卜所需的耗材是干草和木材。请注意：调用 `plant(Entities.Carrot)` 函数种植胡萝卜时，这些耗材（干草和木材）会被消耗一定数量。

你可以在所有植物的[专属页面](objects/carrot)上查看所需的耗材数量。