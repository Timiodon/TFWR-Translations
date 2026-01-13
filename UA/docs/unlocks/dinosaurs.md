# Dinosaurs
Dinosaurs are ancient, majestic creatures that can be farmed for ancient bones.

Unfortunately dinosaurs have gone extinct a long time ago, so the best we can do now is dressing up as one.
For this purpose you have received the new dinosaur hat.

The hat can be equipped with
`change_hat(Hats.Dinosaur_Hat)`

Unfortunately it doesn't quite look like on the advertisement...

If you equip the dinosaur hat and have enough cactus, an [apple](objects/apple) will automatically be purchased and placed under the drone.
When the drone is over an apple and moves again, it will eat the apple and grow its tail by one. If you can afford it, a new apple will be purchased and placed in a random location.
The apple cannot spawn if something else is planted where it wants to be.

The tail of the dinosaur will be dragged behind the drone filling the previous tiles the drone moved over. If a drone tries to move on top of the tail `move()` will fail and return `False`. 
The last segment of the tail will move out of the way during the move, so you can move onto it. However, if the snake fills out the whole farm, you will not be able to move anymore. So you can check if the snake is fully grown by checking if you can't move anymore.
While wearing the dinosaur hat, the drone can't move over the farm border to get to the other side.

Using `measure()` on an apple will return the position of the next apple as a tuple.

`next_x, next_y = measure()`

When the hat is unequipped again by equipping a different hat, the tail will be harvested.
You will receive bones equal to the tail length squared. So for a tail of length `n` you will receive `n**2` `Items.Bone`. 
For Example:
length 1 => 1 bone
length 2 => 4 bones
length 3 => 9 bones
length 4 => 16 bones
length 16 => 256 bones
length 100 => 10000 bones

The Dinosaur Hat is very heavy, so if you equip it, it will make `move()` take 400 ticks instead of 200. However, each time you pick up an apple, the number of ticks used by `move()` is reduced by 3% (rounded down), because a longer tail can help you move.

The following loop prints the number of ticks used by `move()` after any number of apples:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

You only have one dinosaur hat, so only one drone can wear it.

<spoiler=show hint 1>If you keep moving along the same path that covers the whole field, you can easily get a snake that covers the whole field every time. It's not very efficient, but it works.
Fully traversing a very large farm can take a long time and you might not actually need that many bones. Feel free to use `set_world_size()` to change the size of the farm to something more convenient.</spoiler>