# Watering
Plants grow faster when they are watered. The ground has a water level ranging from `0` to `1`.
The function `get_water()` returns the water level of the ground it is over.

The growth speed of a plant scales linearly from 1x speed at water level 0 to 5x speed at water level 1.

The ground dries up over time: On average, it loses 1% of its current water per second, but there is some random variance to this. Maintaining a high water level will consume much more water than maintaining a low water level.

You can use water on your plants. One tank of water is automatically added to your inventory every 10 seconds.
Upgrading `Unlocks.Watering` will double the amount of water you get every 10 seconds.

A tank holds `0.25` water.

Call `use_item(Items.Water)` over any ground to water the ground.
