# Carottes
Avant de pouvoir planter des carottes avec `plant(Entities.Carrot)`, tu dois labourer le sol. Cela changera le sol en `Grounds.Soil`. Pour labourer le sol, appelle simplement `till()`. Appeler `till()` à nouveau le retransformera en `Grounds.Grassland`.

Planter des carottes coûte du bois et du foin. Ces objets seront automatiquement retirés lors de l'appel de `plant(Entities.Carrot)`.

Tu peux voir le coût de n'importe quelle plante sur sa [propre page](objects/carrot).