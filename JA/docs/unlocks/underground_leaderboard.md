# 地下ランキング
地下にはさらに大きな挑戦が待っています。採掘や農業のプログラムを最適化する準備はできましたか？
このアンロックで、地下での最も効率的な方法を競えるようになります。

`leaderboard_run(leaderboard, filename, speedup)`を呼ぶと、地下ランキングの挑戦を開始できます。
これは、`simulate()` に似た[シミュレーション](docs/unlocks/simulation.md)を開始しますが、開始条件は固定されています。各リーダーボードカテゴリには、異なる開始条件と成功条件があります。

シミュレーション終了時に成功条件が `True` であれば、リーダーボードランは成功します。

目標に到達してもシミュレーションは自動的に終了しません。プログラムが終了するようにする必要があります。
ランが成功した場合、あなたのタイムがリーダーボードに追加されます。

ばらつきを減らすため、すべてのランはシミュレーション内で合計2時間以上実行する必要があります。シミュレーションは加速できるので、現実の時間で2時間はかかりません。早く終了したランは、シミュレーション時間が合計2時間に達するまで繰り返されます。全ランの平均時間がスコアとしてアップロードされます。

`Leaderboards.Rice_Single`ランキングに参加するための設定例です。

![|x400](UndergroundLeaderboardSetup)

## 最速地下リセット
地下リセットは最も名誉ある種目です。1マスの農場から始め、`Unlocks.Underground_Leaderboard`を再度アンロックするまで、採掘のアンロックツリーを完全に自動化します。

すべてをアンロックする必要はありません。`Unlocks.Underground_Leaderboard`をできるだけ速くアンロックしてください。

`num_unlocked(unlock) > 0` を使って何かがアンロックされているかを確認でき、`get_cost()` をアンロックに使用してコストを確認できるので、適切なアイテムを自動的に栽培できます。

`unlock()` はアンロックツリーの依存関係を考慮しません。たとえば、`Unlocks.Water` より先に `Unlocks.Fertilizer` をアンロックできます。

関数呼び出し:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

同等のシミュレーション:
`unlocks = {}
items = {}
globals = {}
#負のシード値はランダムシードを意味します
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## 鉱石
このランキングでは、鉱石、特に石英を集める腕が試されます。地面の層が石炭、鉄、石英の順に現れるよう生成方法が変わります。

すべてをアンロックした状態から、できるだけ速く`20000`個の石英を集めます。

関数呼び出し:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Quartz) >= 20000`

## 宝物の地図
このランキングはすべてがアンロックされ、大量のパワーがある状態で始まります。宝物の地図がたくさん現れるよう、地面の生成方法が変わります。

8x8の世界で、ドローン1機を使って行います。目標は、できるだけ速く`115000`ゴールドを獲得することです。

関数呼び出し:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

同等のシミュレーション:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

成功条件:
`num_items(Items.Gold) >= 115000`

## 資源ランキング
これらのランキングでは、特定の資源をどれだけ速く集められるかを競います。すべてがアンロックされ、大量のパワーを持った状態から始まります。ただしピラミッドのランキングでは、ピラミッドを復元して自分でパワーを作る必要があります。

目標は決められた量の資源を獲得することです。

これまでと同様に、目標に到達したらプログラムが終了するようにする必要があります。目標に到達しても、プログラムが終了するまでランは完了したことにはなりません。

これらのランキングでは、目的の資源が繰り返し現れるよう地面の生成方法が変わります。そのため、`clear()`は必要ありません。たとえば稲のランキングでは、粘土の層だけが生成されます。

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
成功条件: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
竹のランキングでは掘削が禁止されています。

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
成功条件: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
成功条件: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
成功条件: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
成功条件: `num_items(Items.Power) >= 150000`

## ドローン1機の地下ランキング
シングルドローンで農業を行うリーダーボードもあります。ドローンは1台、農場は8x8で、一定量のリソースをできるだけ早く獲得する必要があります。

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
成功条件: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
成功条件: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
成功条件: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
成功条件: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
成功条件: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
成功条件: `num_items(Items.Power) >= 30000`

