# 排行榜
如果你走到了这一步，说明已经克服了许多挑战。但你的解决方法是否高效？
你可以在各种排行榜上与其他玩家竞争，看看谁的耕作方法效率最高。

调用 `leaderboard_run(leaderboard, filename, speedup)` 即可开始一次排行榜挑战。
这段代码会启动一次类似于 `simulate()` 的[模拟](docs/unlocks/simulation.md)，只不过起始条件是固定的。每个排行榜类别都有不同的开始和成功条件。

如果模拟结束时成功条件为 `True`，则排行榜挑战成功。

当目标达成时，模拟不会自动结束。你必须确保程序终止。
如果挑战成功，你的时间纪录将被添加到排行榜。

为了减少方差，所有挑战都要求运行至少 2 小时（你可以加速，所以实际不会花那么长时间）。如果挑战提前完成，则会重复运行，直到总时间达到 2 小时。随后，将所有运行过程的平均值作为你的分数上传。

以下是示例设置，可以让你登上干草排行榜。
![](LeaderboardSetup400)

## 最快重置
最快重置是最有声望的类别。从一块农田开始，实现游戏完全自动化，直到再次解锁排行榜。

不必解锁全部内容，只需尽快解锁 `Unlocks.Leaderboard`。

请记住，你可以使用 `num_unlocked(unlock) > 0` 来检查某项是否已解锁，也可以对解锁项使用 `get_cost()` 来查看其成本，以便自动耕种正确的物品。

函数调用：
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

等效模拟：
`unlocks = {}
items = {}
globals = {}
#负数种子值表示随机种子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷宫
从解锁全部内容开始，尽快收获 `9863168` 份金币。这正好是重复使用一个 32x32 的迷宫 `300` 次所能获得的金币数量。

函数调用：
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

等效模拟：
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_items(Items.Gold) >= 9863168`

## 恐龙
从解锁全部内容开始，尽快收获 `33488928` 根骨头。这正好是用恐龙尾巴填满一片 32x32 区域所能获得的骨头数量。

函数调用：
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

等效模拟：
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件：
`num_items(Items.Bone) >= 33488928`

## 其他资源排行榜
每种植物都有自己的排行榜，标准是尽快收获该特定植物。开局获得所有解锁项、种植该植物所需的资源，以及大量的能量。目标是收获该植物产出的特定数量的资源。

与之前一样，你需要确保程序在达到目标时终止。即使目标已达成，只要程序没有结束，挑战就不会完成。

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
成功条件：`num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
成功条件：`num_items(Items.Sunflower) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
成功条件：`num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
成功条件：`num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
成功条件：`num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
成功条件：`num_items(Items.Hay) >= 2000000000`

## 单无人机排行榜
也有单无人机耕作的排行榜。你只有一架无人机和一个 8x8 的农场，并且必须尽快收获特定数量的资源。

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
成功条件：`num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
成功条件：`num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
成功条件：`num_items(Items.Sunflower) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
成功条件：`num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
成功条件：`num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
成功条件：`num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
成功条件：`num_items(Items.Hay) >= 100000000`