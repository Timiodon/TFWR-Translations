# Pumpkins
[Pumpkins](objects/pumpkin) grow like carrots on tilled soil. Planting them costs carrots.

When all the pumpkins in a square are fully grown, they will grow together to form a giant pumpkin. Unfortunately, pumpkins have a 20% chance of dying once they are fully grown, so you will need to replant the dead ones if you want them to merge. 

When a pumpkin dies, it leaves behind a dead pumpkin that won't drop anything when harvested. Planting a new plant in its place automatically removes the dead pumpkin, so there is no need to harvest it. `can_harvest()` always returns `False` on dead pumpkins.

The yield of a giant pumpkin depends on the size of the pumpkin.

A 1x1 pumpkin yields `1*1*1 = 1` pumpkins.
A 2x2 pumpkin yields `2*2*2 = 8` pumpkins instead of `4`.
A 3x3 pumpkin yields `3*3*3 = 27` pumpkins instead of `9`.
A 4x4 pumpkin yields `4*4*4 = 64` pumpkins instead of `16`.
A 5x5 pumpkin yields `5*5*5 = 125` pumpkins instead of `25`.
A `n`x`n` pumpkin yields `n*n*6` pumpkins for `n >= 6`.

It's a good idea to get at least 6x6 size pumpkins to get the full multiplier. 

This means that even if you plant a pumpkin on every tile in a square, one of the pumpkins may die and prevent the mega pumpkin from growing.
