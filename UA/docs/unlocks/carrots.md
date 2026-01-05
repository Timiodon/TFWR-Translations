# Carrots
Before you can plant carrots with `plant(Entities.Carrot)`, you have to till the soil. This will change the ground to `Grounds.Soil`. To till the soil, simply call `till()`. Calling `till()` again will change it back to `Grounds.Grassland`.

Planting carrots costs wood and hay. These items will be automatically removed when calling `plant(Entities.Carrot)`.

You can see the cost of any plant on its [own page](objects/carrot).