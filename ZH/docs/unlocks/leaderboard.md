# Leaderboard
如果你已经走到了这一步，你已经克服了许多挑战。但你是否高效地解决了它们？
你可以在各种 leaderboard 上与其他玩家竞争，争夺最有效的耕作方法。

你可以通过调用 `leaderboard_run(leaderboard, filename, speedup)` 来开始一次 leaderboard 挑战。
这将开始一个类似于 `simulate()` 的[模拟](docs/unlocks/simulation.md)，但起始条件是固定的。每个 leaderboard 类别都有不同的开始和成功条件。

如果模拟结束时成功条件为 `True`，则 leaderboard 挑战成功。模拟在达到目标时不会自动结束。你必须确保程序终止。
如果挑战成功，你的时间将被添加到 leaderboard。

为了减少方差，所有挑战都要求运行至少2小时（你可以加速，所以不会花那么长时间）。如果一个挑战提前完成，它将被重复，直到总时间达到2小时。然后所有挑战的平均值将作为你的分数上传。

这是一个能让你登上干草 leaderboard 的示例设置。
![](LeaderboardSetup400)

## 最快重置
最快重置是最负盛名的类别。从单一农田地块开始，完全自动化游戏，直到再次解锁 leaderboard。

你不必解锁所有东西，只需尽快解锁 `Unlocks.Leaderboard`。

记住，你可以使用 `num_unlocked(unlock) > 0` 来检查某样东西是否已解锁，你还可以在解锁项上使用 `get_cost()` 来查看它们的成本，以便自动种植正确的物品。

函数调用：
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

等效模拟：
`unlocks = {}
items = {}
globals = {}
#负的 seed 值意味着一个随机种子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷宫
从解锁所有东西开始，并尽快种出 `300000` 黄金。这正好是你通过解决一个迷宫 `300` 次所能获得的黄金数量。

函数调用：
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

等效模拟：
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_items(Items.Gold) >= 300000`

## 恐龙
从解锁所有东西开始，并尽快种出 `98010` 骨头。这正好是你用恐龙尾巴填满一个 10x10 区域所能获得的骨头数量。

函数调用：
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

等效模拟：
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_items(Items.Bone) >= 98010`

## 其他资源 Leaderboard
每种植物都有自己的 leaderboard，用于尽快种植该特定植物。你从所有解锁项、种植该植物所需的资源和大量能量开始。目标是种出 `100000` 份由该植物生产的资源。

函数调用：
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

成功条件：
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` 要求种出 `100000` 份所有三种混种资源。