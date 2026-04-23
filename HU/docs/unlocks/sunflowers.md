# Sunflowers
[Sunflowers](objects/sunflower) collect the power of the sun. You can harvest that power. 

Planting them works exactly like planting carrots or pumpkins. 

Harvesting a grown sunflower yields power.
If there are at least 10 sunflowers on the farm and you harvest the one with the largest number of petals you get `8` times more power!
If you harvest a sunflower while there is another sunflower with more petals, the next sunflower you harvest will also only give you the normal amount of power (not the 8x bonus).

`measure()` returns the number of petals of the sunflower under the drone.
Sunflowers have at least `7` and at most `15` petals.
They can already be measured before they are fully grown.

Several sunflowers can have the same number of petals so there can also be several sunflowers with the largest number of petals. In this case, it doesn't matter which one of them you harvest.

As long as you have power the drone will use it to run twice as fast. 
It consumes 1 power every 30 actions (like moves, harvests, plants...)
Executing other code statements can also use power but a lot less than drone actions.

In general, everything that is sped up by speed upgrades is also sped up by power.
Anything sped up by power also uses power proportional to the time it takes to execute it, ignoring speed upgrades.
