# Auto Unlocks
To fully automate the game, you can use the `unlock()` function to automatically unlock features.
For example, you can use `unlock(Unlocks.Speed)` and `unlock(Unlocks.Expand)` to unlock the speed and expansion features.

To determine the cost of an unlock, simply use the `get_cost()` function as you would for a plant or item.
Example:
`get_cost(Unlocks.Loops)`
returns `{Items.Hay:5}`

If you want to find out how many of a particular unlock you have, use the `num_unlocked(unlock)` function.

For example, `num_unlocked(Unlocks.Speed)` will return the number of speed upgrades you have.

`num_unlocked(Unlocks.Senses)` will return `1` if senses are unlocked and `0` if they are not.

You can also use `num_unlocked()` on Items, Entities or Grounds. This will return `1` if it's unlocked otherwise `0`.

Be careful `num_unlocked(Unlocks.Carrots)` will return the number of times it was unlocked/upgraded.
`num_unlocked(Items.Carrot)` will only return `0` or `1`. (Same for other plants)
