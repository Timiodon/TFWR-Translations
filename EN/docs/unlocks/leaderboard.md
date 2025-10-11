# Leaderboard
If you have made it this far, you have overcome many challenges. But have you solved them efficiently? 
You can compete with other players on various leaderboards for the most efficient farming methods.

You can start a leaderboard run by calling `leaderboard_run(leaderboard, filename, speedup)`.
This starts a [simulation](docs/unlocks/simulation.md) similar to `simulate()` except that the starting conditions are fixed. Each leaderboard category has different start and success conditions.

The leaderboard run succeeds if the success condition is `True` when the simulation ends. 

The simulation will NOT end automatically when the goal is reached. You must make sure that the program terminates.
If the run is successful, your time will be added to the leaderboard.

To reduce variance, all runs are required to run for at least 2 hours (You can speed it up, so it won't take that long). If a run is completed earlier, it will be repeated until a total time of 2 hours is reached. The average of all runs is then uploaded as your score.

Here's an example setup that will get you on the hay leaderboard.
![](LeaderboardSetup400)

## Fastest Reset
The fastest reset is the most prestigious category. Completely automate the game from a single farm plot to unlocking the leaderboards again.

You do not have to unlock everything, just try to unlock `Unlocks.Leaderboard` as fast as possible.

Remember that you can use `num_unlocked(unlock) > 0` to check if something is unlocked and you can use `get_cost()` on unlocks to see what they cost so you can automatically farm the right items.

Function Call:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Equivalent Simulation:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Maze
Start with everything unlocked and farm `9863168` gold as fast as you can. This is exactly the amount of gold you will earn by reusing one 32x32 maze `300` times.

Function Call:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Gold) >= 9863168`

## Dinosaur
Start with everything unlocked and farm `33488928` bones as fast as you can. This is exactly the number of bones you will get if you fill a 32x32 area with the dinosaur tail.

Function Call:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Bone) >= 33488928`

## Other Resource Leaderboards
Each plant has its own leaderboard for farming that particular plant as quickly as possible. You start with all the unlocks, the resources you need to grow the plant, and lots of power. The goal is to farm a set amount of the resource produced by the plant.

As always, you need to make sure that your program terminates when you reach the goal. A run is not finished until the program ends, even if the goal is reached.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Success Condition: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Success Condition: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Success Condition: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Success Condition: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Success Condition: `num_items(Items.Hay) >= 2000000000`

## Single Drone Leaderboards
There are also Leaderboards for farming with a single drone. You only get one drone and an 8x8 farm and have to farm a certain amount of resources as quickly as possible.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Success Condition: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Success Condition: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Success Condition: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Success Condition: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Success Condition: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Success Condition: `num_items(Items.Hay) >= 100000000`