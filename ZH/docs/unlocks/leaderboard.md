# 排行榜
如果你已经走到了这一步，你已经克服了许多挑战。但你是否高效地解决了它们？
你可以在各种排行榜上与其他玩家竞争最有效的耕作方法。

你可以通过调用 `leaderboard_run(leaderboard, filename, speedup)` 来开始一次排行榜挑战。
这将开始一个类似于 `simulate()` 的[模拟](docs/unlocks/simulation.md)，但起始条件是固定的。每个排行榜类别都有不同的开始和成功条件。

如果模拟结束时成功条件为 `True`，则排行榜挑战成功。当目标达成时，模拟不会自动结束。你必须确保程序终止。
如果挑战成功，你的时间将被添加到排行榜。

为了减少方差，所有挑战都要求运行至少 2 小时（你可以加速，所以不会花那么长时间）。如果挑战提前完成，它将被重复，直到总时间达到 2 小时。所有运行的平均值将作为你的分数上传。

这里有一个示例设置，可以让你登上干草排行榜。
![](LeaderboardSetup400)

## 最快重置
最快重置是最负盛名的类别。从一个农田地块开始，完全自动化游戏，直到再次解锁排行榜。

你不必解锁所有东西，只需尽快解锁 `Unlocks.Leaderboard`。

请记住，你可以使用 `num_unlocked(unlock) > 0` 来检查某项是否已解锁，你也可以对解锁项使用 `get_cost()` 来查看它们的成本，以便自动耕种正确的物品。

函数调用：
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

等效模拟：
`unlocks = {}
items = {}
globals = {}
#负的种子值表示随机种子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷宫
从解锁所有东西开始，尽快农场 `300000` 黄金。这正好是解决一个迷宫 `300` 次所能获得的黄金数量。

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
从解锁所有东西开始，尽快农场 `98010` 骨头。这正好是你用恐龙尾巴填满一个 10x10 区域所能获得的骨头数量。

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

## 其他资源排行榜
每种植物都有自己的排行榜，用于尽快地耕种该特定植物。你从所有解锁项、种植该植物所需的资源和大量能量开始。目标是农场 `100000` 该植物生产的资源。

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

`Leaderboards.Polyculture` 需要农场 `100000` 所有三种复合种植资源。