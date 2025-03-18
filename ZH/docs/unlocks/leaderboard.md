# 排行榜

如果你已经走到这里，说明你克服了很多挑战。但是你解决这些挑战的效率如何？
你可以和其他玩家在不同的排行榜上竞争最有效的种植方法。

你可以通过调用 `leaderboard_run(leaderboard, filename, speedup)` 开始一场排行榜挑战。
这将启动一个类似于 `simulate()` 的 [模拟](docs/unlocks/simulation.md)，不同的是起始条件是固定的。每个排行榜类别都有不同的起点和成功条件。

如果成功条件在模拟结束时为 `True`，则排行榜挑战成功。模拟在达到目标时不会自动结束。你必须确保程序终止。
如果挑战成功，你的时间将被添加到排行榜上。

为了减少差异，所有挑战需要运行至少2小时（你可以加速，这样不会用太长时间）。如果挑战提前完成，将重复运行，直到达到2小时的总时间为止。所有运行的平均时间将被上传作为你的分数。

这是一个让你进入干草排行榜的示例设置。
![](LeaderboardSetup400)

## 最快重置

最快重置是最受欢迎的类别。从一个单独的农田地块完全自动化游戏，直到再次解锁排行榜。

你不必解锁所有内容，只需尽快解锁 `Unlocks.Leaderboard`。

记得你可以使用 `num_unlocked(unlock) > 0` 检查某物是否解锁，可以使用 `get_cost()` 查看解锁的成本，从而自动种植正确的物品。

函数调用：
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

等效模拟：
`unlocks = {}
items = {}
globals = {}
# 负数的种子值表示随机种子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷宫

从全部解锁开始，尽快获取 `300000` 金币。这正好是你通过解决一个迷宫 `300` 次获得的金币数量。

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

从全部解锁开始，尽快获得 `98010` 骨头。如果你用恐龙尾巴填满一个 10x10 的区域，这正是你将得到的骨头数量。

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

每种植物都有自己的排行榜，目标是尽快种植出特定植物。你开始时会拥有所有解锁内容、种植植物所需的资源以及大量能量。目标是种植出该植物产生的 `100000` 资源。

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

`Leaderboards.Polyculture` 需要同时种植出三个多种植资源的 `100000`。