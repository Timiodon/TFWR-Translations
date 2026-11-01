# 地下排行榜
地下還有更大的挑戰。準備好最佳化你的採礦和種植程式了嗎？
這個解鎖項讓你能在地下競逐最有效率的方法。

呼叫 `leaderboard_run(leaderboard, filename, speedup)`，即可開始地下排行榜挑戰。
這段程式碼會啟動一次類似於 `simulate()` 的[模擬](docs/unlocks/simulation.md)，只不過起始條件是固定的。每個排行榜類別都有不同的開始和成功條件。

如果模擬結束時成功條件為 `True`，則排行榜挑戰成功。

當目標達成時，模擬不會自動結束。你必須確保程式終止。
如果挑戰成功，你的時間紀錄將被新增到排行榜。

為了減少變異數，所有挑戰都要求執行至少 2 小時（你可以加速，所以實際不會花那麼長時間）。如果挑戰提前完成，則會重複執行，直到總時間達到 2 小時。隨後，將所有執行過程的平均值作為你的分數上傳。

以下範例設定可以幫你進入 `Leaderboards.Rice_Single` 排行榜。

![|x400](UndergroundLeaderboardSetup)

## 最快地下重設
地下重設是最具聲望的項目。在此項目中，你要使採礦解鎖樹完全自動化，從一格農場開始，直到再次解鎖 `Unlocks.Underground_Leaderboard`。

不必解鎖所有內容，只需盡快解鎖 `Unlocks.Underground_Leaderboard`。

請記住，你可以使用 `num_unlocked(unlock) > 0` 來檢查某項是否已解鎖，也可以對解鎖項使用 `get_cost()` 來檢視其成本，以便自動耕種正確的物品。

`unlock()` 不受科技樹中的前置解鎖條件限制。例如，可以先解鎖 `Unlocks.Fertilizer`，再解鎖 `Unlocks.Water`。

函式呼叫：
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

等效模擬：
`unlocks = {}
items = {}
globals = {}
#負數種子值表示隨機種子
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## 礦石
這個排行榜考驗收集礦石的能力，尤其是石英。地面生成方式經過調整，各層依序提供煤炭、鐵礦和石英。

從全部解鎖的狀態開始，盡快收集 `20000` 石英。

函式呼叫：
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

等效模擬：
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_items(Items.Quartz) >= 20000`

## 藏寶圖
這個排行榜開始時已解鎖所有內容，並擁有大量能量。它會調整地面生成方式，讓藏寶圖大量出現。

它使用 8x8 的世界和單架無人機。目標是盡快收集 `115000` 金幣。

函式呼叫：
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

等效模擬：
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功條件：
`num_items(Items.Gold) >= 115000`

## 資源排行榜
這些排行榜著重於盡快收集特定資源。開始時已解鎖所有內容，並擁有大量能量。唯一的例外是金字塔排行榜，需要自行修復金字塔來生產能量。

目標是收集指定數量的資源。

與之前一樣，你需要確保程式在達到目標時終止。即使目標已達成，只要程式沒有結束，挑戰就不會完成。

這些排行榜會調整地面生成方式，讓目標資源不斷出現。因此不需要使用 `clear()`。例如，水稻排行榜只有黏土層。

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
成功條件： `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
竹子排行榜禁止挖掘。

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
成功條件： `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
成功條件： `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
成功條件： `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
成功條件： `num_items(Items.Power) >= 150000`

## 單架無人機地下排行榜
也有單無人機耕作的排行榜。你只有一架無人機和一個 8x8 的農場，並且必須盡快收穫特定數量的資源。

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
成功條件： `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
成功條件： `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
成功條件： `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
成功條件： `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
成功條件： `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
成功條件： `num_items(Items.Power) >= 30000`

