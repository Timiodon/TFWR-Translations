# 排行榜
如果你能走到這裡，表示已克服許多挑戰。但你是否以最高效率解決這些挑戰？
你可以參加各種排行榜，與其他玩家競爭最有效率的農耕方法。

你可以呼叫 `leaderboard_run(leaderboard, filename, speedup)` 開始一個排行榜挑戰。
這會啟動一個類似 `simulate()` 的[模擬](docs/unlocks/simulation.md)，但起始條件固定。每個排行榜類別有不同的起始與成功條件。

當模擬結束時，如果成功條件為 `True`，則該次排行榜挑戰算作成功。

模擬不會在達成目標時自動結束。你必須確保程式會正確終止。
如果該次執行成功，你的時間會被登錄到排行榜。

為了降低差異性，所有挑戰執行時間必須至少累計 2 小時（你可以加速模擬，因此實際耗時不必那麼長）。如果某次執行提早完成，系統會重複執行直到累計達到 2 小時為止。上傳的分數為所有執行的平均值。上傳的分數為所有執行的平均值。

下面是一個可讓你上到乾草排行榜的範例設定。
![](LeaderboardSetup400)

## 最快重置
最快重置是最具聲望的類別。從單一農地自動化到再次解鎖排行榜，盡可能快速完成。

你不必解鎖所有東西，只要盡快解鎖 `Unlocks.Leaderboard` 即可。

記住你可以用 `num_unlocked(unlock) > 0` 檢查某項是否已解鎖，也可以對解鎖項目使用 `get_cost()` 查詢其花費，以便自動取得所需資源。

函式呼叫：

```
leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)
```

等效模擬：

```
unlocks = {}
items = {}
globals = {}
# 負的亂數種子表示隨機種子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)
```

成功條件：

```
num_unlocked(Unlocks.Leaderboard) > 0
```

## 迷宮
從全部解鎖開始，盡快農出 `9863168` 個黃金。這正好是重複使用一個 32x32 迷宮 `300` 次所能獲得的黃金數量。

函式呼叫：

```
leaderboard_run(Leaderboards.Maze, filename, speedup)
```

等效模擬：

```
unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)
```

成功條件：

```
num_items(Items.Gold) >= 9863168
```

## 恐龍
從解鎖全部內容開始，盡快農出 `33488928` 個骨頭。這正好是將 32x32 區域填滿恐龍尾巴所能獲得的骨頭數量。

函式呼叫：

```
leaderboard_run(Leaderboards.Dinosaur, filename, speedup)
```

等效模擬：

```
unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)
```

成功條件：

```
num_items(Items.Bone) >= 33488928
```

## 其他資源排行榜
每種植物都有針對該植物的排行榜，目標是以最短時間生產指定數量的該資源。你從解鎖全部內容、擁有種植該植物所需的資源和大量能量開始。目標是快速農出該植物產出的指定數量資源。

一如既往，當你達成目標時必須確保程式會終止。程式結束前即便已達標，該次執行也不算完成。

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
成功條件：`num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
成功條件：`num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
成功條件：`num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
成功條件：`num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
成功條件：`num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
成功條件：`num_items(Items.Hay) >= 2000000000`

## 單一無人機排行榜
也有僅使用一台無人機的排行榜。你只會有一架無人機和 8x8 的農場，必須在最短時間內農出指定數量的資源。

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
成功條件：`num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
成功條件：`num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
成功條件：`num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
成功條件：`num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
成功條件：`num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
成功條件：`num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
成功條件：`num_items(Items.Hay) >= 100000000`