# リーダーボード

ここまで来たあなたは多くのチャレンジを乗り越えましたね。でも、それを効率的に解決しましたか？ さまざまな農法で他のプレイヤーとリーダーボードで競争しましょう。

`leaderboard_run(leaderboard, filename, speedup)`を呼び出すことで、リーダーボードの実行を開始できます。これは、`simulate()` と似た[シミュレーション](docs/unlocks/simulation.md)を始めるもので、スタートの条件が固定されています。各リーダーボードのカテゴリは、異なるスタート条件と成功条件があります。

シミュレーションが終了したときに成功条件が `True` であれば、リーダーボードの実行は成功です。目標が達成されるとシミュレーションは自動で終了しません。プログラムが終了するようにしてください。成功すると、あなたのタイムがリーダーボードに追加されます。

ばらつきを減らすために、すべての実行は少なくとも2時間は行う必要があります（スピードアップできるので実際にはそんなに時間はかかりません）。もし早く完了した場合、それが合計2時間に達するまで繰り返されます。すべての実行の平均値があなたのスコアとしてアップロードされます。

これがあなたを干し草リーダーボードに載せるための例設定です。
![](LeaderboardSetup400)

## 最速リセット

最速リセットは最も名誉あるカテゴリです。1つの農場から完全に自動化して再びリーダーボードをアンロックすることを目指します。

すべてをアンロックする必要はありません。`Unlocks.Leaderboard`をできるだけ早くアンロックするようにしてください。

`num_unlocked(unlock) > 0` を使用して何かがアンロックされているか確認したり、`get_cost()` をアンロックに使用してコストを確認し、必要なアイテムを自動で収穫できるようにします。

関数呼び出し:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

同等のシミュレーション:
`unlocks = {}
items = {}
globals = {}
#負の seed 値はランダム seed を意味します
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 迷路

すべてのアンロックからスタートし、できるだけ早く `300000` ゴールドを収穫します。これは1つの迷路を `300` 回解くことで得られる正確なゴールド量です。

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

すべてのアンロックからスタートし、できるだけ早く `98010` 骨を収穫します。これは恐竜の尾で 10x10 のエリアを埋めることで正確に得られる骨の数です。

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

## その他のリソースリーダーボード

各植物には、その植物をできるだけ早く栽培するための専用リーダーボードがあります。すべてのアンロック、植物を育てるのに必要なリソース、大量のパワーからスタートします。目的はその植物が生産するリソースを `100000` 収穫することです。

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

`Leaderboards.Polyculture` はすべてのポリカルチャーリソースを `100000` 収穫する必要があります。