# Underground Leaderboard
The underground holds even greater challenges. Are you prepared to optimize your mining and farming programs?
With this unlock, you can compete for the most efficient methods in the depths.

You can start an underground leaderboard run by calling `leaderboard_run(leaderboard, filename, speedup)`.
This starts a [simulation](docs/unlocks/simulation.md) similar to `simulate()`, except that the starting conditions are fixed. Each leaderboard category has different starting and success conditions.

The leaderboard run succeeds if the success condition is `True` when the simulation ends. 

The simulation will NOT end automatically when the goal is reached. You must make sure that the program terminates.
If the run is successful, your time will be added to the leaderboard.

To reduce variance, all runs must cover at least 2 hours of simulated time. You can speed up the simulation, so it won't take that long in real time. If a run finishes earlier, it will be repeated until the total simulated time reaches 2 hours. The average time across all runs is then uploaded as your score.

Here's an example setup that will get you on the `Leaderboards.Rice_Single` leaderboard.

![|x400](UndergroundLeaderboardSetup)

## Fastest Underground Reset
The underground reset is the most prestigious category. In this category, you completely automate the mining unlock tree, starting with a single farm plot and ending when you unlock `Unlocks.Underground_Leaderboard` again.

You do not have to unlock everything, just try to unlock `Unlocks.Underground_Leaderboard` as fast as possible.

Remember that you can use `num_unlocked(unlock) > 0` to check whether something is unlocked. You can also use `get_cost()` on unlocks to see what they cost, allowing you to farm the right items automatically.

`unlock()` does not care about tech tree dependencies. For example, it is possible to unlock `Unlocks.Fertilizer` before `Unlocks.Water`.

Function Call:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Equivalent Simulation:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Ores
This leaderboard tests your skills in farming ores - particularly quartz. It modifies ground generation such that the ground layers will provide you with coal, then iron, then quartz in this order.

Start with everything unlocked and farm `20000` quartz as fast as you can.

Function Call:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Quartz) >= 20000`

## Treasure Map
This leaderboard starts with everything unlocked and lots of power. It modifies the ground generation such that there are lots of treasure maps.

It takes place on an 8x8 world size with a single drone. The goal is to farm `115000` gold as quickly as possible.

Function Call:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Gold) >= 115000`

## Resource Leaderboards
These leaderboards focus on farming specific resources as quickly as possible. You start with everything unlocked and lots of power. The only exception for this is the pyramids leaderboard, where you will need to produce power yourself by restoring pyramids.

The goal is to farm a set amount of resources.

As always, you need to make sure that your program terminates when you reach the goal. A run is not finished until the program ends, even if the goal is reached.

These leaderboards modify ground generation such that the desired resource can be found over and over. This means that there's no need to `clear()`. For example, the rice leaderboard consists of only clay layers.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Success Condition: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
Note that the bamboo leaderboard disallows digging.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Success Condition: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Success Condition: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Success Condition: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 150000`

## Single Drone Underground Leaderboards
There are also leaderboards for farming with a single drone. You get only one drone and an 8x8 farm, and you must farm a certain amount of resources as quickly as possible.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Success Condition: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Success Condition: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Success Condition: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Success Condition: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Success Condition: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 30000`

