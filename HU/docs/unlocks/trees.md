# Trees
[Trees](objects/tree) are a better way to get wood than bushes. They give 5 wood each. Like bushes, they can be planted on grass or soil.

Trees like to have some space and planting them right next to each other will slow down their growth. The growing time is doubled for each tree that is on a tile directly to the north, east, west or south of it. So if you plant trees on every tile, they will take `2*2*2*2 = 16` times longer to grow.

<spoiler=show> The `%` operator can be useful here. Remember that the `%` operator returns the remainder of the division. Even numbers divided by `2` have a remainder of `0` and odd numbers divided by `2` have a remainder of `1`.
So you can check if a number is even like this:

`def is_even(n):
	return n % 2 == 0`

This returns `True` if n is even and `False` if it isn't.
</spoiler>