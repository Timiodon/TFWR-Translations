# 胡蘿蔔
在用 `plant(Entities.Carrot)` 種植胡蘿蔔之前，你需要先耕地。這會將地塊變更為 `Grounds.Soil`，只要呼叫 `till()`。再次呼叫 `till()` 則會將地塊變回 `Grounds.Grassland`。

種植胡蘿蔔需要木材和乾草。呼叫 `plant(Entities.Carrot)` 時會自動移除這些物品。

你可以在每個植物的[專屬頁面](objects/carrot)查看各自的花費。