# Polyculture
You may have already noticed that sometimes plants yield more when planted together.
Grass, bushes, trees, and carrots yield more when they have the right plant companion. Companion preference is different for each individual plant and cannot be predicted. Fortunately, the companion preference of the plant under the drone can be measured using `get_companion()`. It returns a tuple where the first element is the type of plant it wants as its companion and the second element is the position where it wants its companion.

`plant_type, (x, y) = get_companion()`

For example if you plant a bush and then call `get_companion()` it will return something like `(Entities.Carrot, (3, 5))`. This means that this bush would like to have carrots at the position `(3,5)`. So if you plant carrots at `(3,5)` and then harvest the bush, it will yield more wood. The growth stage of the carrot doesn't matter.

A plant's companion preference can be either `Entities.Grass`, `Entities.Bush`, `Entities.Tree` or `Entities.Carrot`. Each plant chooses this randomly, but it will always choose a different plant than itself. The position can also be any position within 3 moves of the plant except the position of the plant itself.

If there is no plant under the drone that has a companion preference `get_companion()` will return `None`.

Before polyculture is unlocked, the yield multiplier is `5`. It doubles everytime you upgrade it.