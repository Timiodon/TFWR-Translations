# Leaderboard
ここまでたどり着いたあなたは、多くの挑戦を乗り越えてきました。しかし、それらを効率的に解決しましたか？
最も効率的な農業方法を競う様々なleaderboardで、他のプレイヤーと競うことができます。

`leaderboard_run(leaderboard, filename, speedup)`を呼び出すことで、leaderboardの実行を開始できます。
これは`simulate()`と同様の[シミュレーション](docs/unlocks/simulation.md)を開始しますが、開始条件は固定されています。各leaderboardカテゴリには、異なる開始条件と成功条件があります。

シミュレーション終了時に成功条件が`True`であれば、leaderboardの実行は成功です。目標に到達してもシミュレーションは自動的に終了しません。プログラムが終了するように確認する必要があります。
実行が成功した場合、あなたのタイムがleaderboardに追加されます。

ばらつきを減らすため、すべての実行は少なくとも2時間実行する必要があります（高速化できるので、それほど時間はかかりません）。実行が早く完了した場合、合計時間が2時間に達するまで繰り返されます。その後、すべての実行の平均がスコアとしてアップロードされます。

これは、干し草のleaderboardに載るためのセットアップ例です。
![](LeaderboardSetup400)

## 最速リセット
最速リセットは最も名誉あるカテゴリです。単一の農地からleaderboardを再びアンロックするまで、ゲームを完全に自動化します。

すべてをアンロックする必要はありません。できるだけ早く`Unlocks.Leaderboard`をアンロックすることを目指してください。

`num_unlocked(unlock) > 0`を使って何かがアンロックされているかを確認でき、アンロックに対して`get_cost()`を使ってコストを確認できることを忘れないでください。そうすれば、適切なアイテムを自動的に栽培できます。

関数呼び出し:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

同等のシミュレーション:
`unlocks = {}
items = {}
globals = {}
#負のseed値はランダムなseedを意味します
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷路
すべてがアンロックされた状態で開始し、できるだけ早く`300000`ゴールドを稼ぎます。これは、1つの迷路を`300`回解くことで得られるゴールドの量とまったく同じです。

関数呼び出し:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Gold) >= 300000`

## 恐竜
すべてがアンロックされた状態で開始し、できるだけ早く`98010`個の骨を稼ぎます。これは、10x10のエリアを恐竜の尻尾で埋めた場合に得られる骨の数とまったく同じです。

関数呼び出し:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Bone) >= 98010`

## その他のリソースLeaderboard
各作物には、その特定の作物をできるだけ早く栽培するための独自のleaderboardがあります。すべてのアンロック、作物を育てるために必要なリソース、そしてたくさんのpowerを持ってスタートします。目標は、その作物が生産するリソースを`100000`個栽培することです。

関数呼び出し:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

成功条件:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture`は、3つすべての混作リソースを`100000`個栽培する必要があります。