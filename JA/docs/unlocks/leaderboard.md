# リーダーボード
ここまでたどり着いたなら、多くの課題を乗り越えてきたことでしょう。しかし、それらを効率的に解決しましたか？
さまざまなリーダーボードで他のプレイヤーと最も効率的な農業方法を競うことができます。

`leaderboard_run(leaderboard, filename, speedup)` を呼び出すことで、リーダーボードランを開始できます。
これは、`simulate()` に似た[シミュレーション](docs/unlocks/simulation.md)を開始しますが、開始条件は固定されています。各リーダーボードカテゴリには、異なる開始条件と成功条件があります。

シミュレーション終了時に成功条件が `True` であれば、リーダーボードランは成功します。

目標に到達してもシミュレーションは自動的に終了しません。プログラムが終了するようにする必要があります。
ランが成功した場合、あなたのタイムがリーダーボードに追加されます。

ばらつきを減らすため、すべてのランは少なくとも2時間実行する必要があります（スピードアップできるので、それほど長くはかかりません）。ランが早く完了した場合、合計時間が2時間に達するまで繰り返されます。すべてのランの平均がスコアとしてアップロードされます。

これは、干し草のリーダーボードに載るためのセットアップ例です。
![](LeaderboardSetup400)

## 最速リセット
最速リセットは最も名誉あるカテゴリです。単一の農地からリーダーボードを再びアンロックするまで、ゲームを完全に自動化します。

すべてをアンロックする必要はなく、できるだけ早く `Unlocks.Leaderboard` をアンロックするようにしてください。

`num_unlocked(unlock) > 0` を使って何かがアンロックされているかを確認でき、`get_cost()` をアンロックに使用してコストを確認できるので、適切なアイテムを自動的に栽培できます。

関数呼び出し:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

同等のシミュレーション:
`unlocks = {}
items = {}
globals = {}
#負のシード値はランダムシードを意味します
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷路
すべてがアンロックされた状態から始め、できるだけ早く `9863168` ゴールドを稼ぎます。これは、1つの32x32の迷路を `300` 回再利用することで得られるゴールドの量とまったく同じです。

関数呼び出し:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Gold) >= 9863168`

## 恐竜
すべてがアンロックされた状態から始め、できるだけ早く `33488928` 個の骨を稼ぎます。これは、32x32のエリアを恐竜の尻尾で埋めた場合に得られる骨の数とまったく同じです。

関数呼び出し:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Bone) >= 33488928`

## その他のリソースリーダーボード
各植物には、その特定の植物をできるだけ早く栽培するための独自のリーダーボードがあります。すべてのアンロック、植物を育てるために必要なリソース、そしてたくさんのパワーを持ってスタートします。目標は、植物によって生産されるリソースを一定量栽培することです。

これまでと同様に、目標に到達したらプログラムが終了するようにする必要があります。目標に到達しても、プログラムが終了するまでランは完了したことにはなりません。

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
成功条件: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
成功条件: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
成功条件: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
成功条件: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
成功条件: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
成功条件: `num_items(Items.Hay) >= 2000000000`

## シングルドローンリーダーボード
シングルドローンで農業を行うリーダーボードもあります。ドローンは1台、農場は8x8で、一定量のリソースをできるだけ早く獲得する必要があります。

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
成功条件: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
成功条件: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
成功条件: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
成功条件: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
成功条件: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
成功条件: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
成功条件: `num_items(Items.Hay) >= 100000000`