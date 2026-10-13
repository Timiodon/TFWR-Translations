[<- 模擬](docs/unlocks/simulation.md)
---
# 排行榜
如果你走到了這一步，說明已經克服了許多挑戰。但你的解決方法是否高效？
你可以在各種排行榜上與其他玩家競爭，看看誰的耕作方法效率最高。

呼叫 `leaderboard_run(leaderboard, filename, speedup)` 即可開始一次排行榜挑戰。
這段程式碼會啟動一次類似於 `simulate()` 的[模擬](docs/unlocks/simulation.md)，只不過起始條件是固定的。每個排行榜類別都有不同的開始和成功條件。

如果模擬結束時成功條件為 `True`，則排行榜挑戰成功。

當目標達成時，模擬不會自動結束。你必須確保程式終止。
如果挑戰成功，你的時間紀錄將被新增到排行榜。

為了減少變異數，所有挑戰都要求執行至少 2 小時（你可以加速，所以實際不會花那麼長時間）。如果挑戰提前完成，則會重複執行，直到總時間達到 2 小時。隨後，將所有執行過程的平均值作為你的分數上傳。

以下是範例設定，可以讓你登上乾草排行榜。
![|x400](LeaderboardSetup)

## 最快重設
最快重設是最有聲望的類別。從一塊農田開始，實現遊戲完全自動化，直到再次解鎖排行榜。

不必解鎖全部內容，只需盡快解鎖 `Unlocks.Leaderboard`。

請記住，你可以使用 `num_unlocked(unlock) > 0` 來檢查某項是否已解鎖，也可以對解鎖項使用 `get_cost()` 來檢視其成本，以便自動耕種正確的物品。

`unlock()` 不受科技樹中的前置解鎖條件限制。例如，可以先解鎖 `Unlocks.Fertilizer`，再解鎖 `Unlocks.Water`。

函式呼叫：
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

等效模擬：
`unlocks = {}
items = {}
globals = {}
#負數種子值表示隨機種子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷宮
從解鎖全部內容開始，盡快收穫 `9863168` 份金幣。這正好是重複使用一個 32x32 的迷宮 `300` 次所能獲得的金幣數量。

函式呼叫：
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

等效模擬：
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_items(Items.Gold) >= 9863168`

## 恐龍
從解鎖全部內容開始，盡快收穫 `33488928` 根骨頭。這正好是用恐龍尾巴填滿一片 32x32 區域所能獲得的骨頭數量。

函式呼叫：
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

等效模擬：
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_items(Items.Bone) >= 33488928`

## 其他資源排行榜
每種植物都有自己的排行榜，標準是盡快收穫該特定植物。開局獲得所有解鎖項、種植該植物所需的資源，以及大量的能量。目標是收穫該植物產出的特定數量的資源。

與之前一樣，你需要確保程式在達到目標時終止。即使目標已達成，只要程式沒有結束，挑戰就不會完成。

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

## 單無人機排行榜
也有單無人機耕作的排行榜。你只有一架無人機和一個 8x8 的農場，並且必須盡快收穫特定數量的資源。

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

---

[模擬](docs/unlocks/simulation.md)      [計時](docs/unlocks/timing.md)      [自動解鎖](docs/unlocks/auto_unlock.md)      [成本](docs/unlocks/costs.md)      [統計資料](docs/stats.md)

[get_cost()](functions/get_cost)      [num_unlocked()](functions/num_unlocked)      [leaderboard_run()](functions/leaderboard_run)
