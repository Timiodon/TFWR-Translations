# メガファーム
この信じられないほど強力なアンロックにより、複数のドローンにアクセスできるようになります。

以前と同様に、最初は1台のドローンから始まります。追加のドローンはまずスポーンさせる必要があり、プログラムが終了すると消えます。
各ドローンは独自の別のプログラムを実行します。新しいドローンは `spawn_drone(function)` 関数を使用してスポーンできます。

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

これにより、`spawn_drone(function)` コマンドを実行したドローンと同じ位置に新しいドローンがスポーンします。新しいドローンは指定された関数の実行を開始します。それが終わると、自動的に消えます。

ドローンは互いに衝突しません。

スポーンできるドローンの最大数を取得するには `max_drones()` を使用します。
農場にすでにいるドローンの数を取得するには `num_drones()` を使用します。


## 例:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

これにより、最初のドローンが水平に移動し、より多くのドローンをスポーンします。スポーンされたドローンは垂直に移動し、その経路にあるすべてを収穫します。

利用可能なすべてのドローンがすでにスポーンされている場合、`spawn_drone()` は何もしないで `None` を返します。

各ドローンに異なる方向を渡す、もう一つの例です。
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

<spoiler=show hint> この非常に便利な並列 `for_all` 関数をチェックしてください。これは任意の関数を受け取り、すべての農場のタイルで実行します。そのために利用可能なすべてのドローンを使用します。

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

特に便利なパターンの一つは、利用可能なドローンがいればスポーンし、そうでなければ自分でやることです。

`if not spawn_drone(task):
	task()`
</spoiler>

## 他のドローンを待つ
別のドローンが終了するのを待つには `wait_for(drone)` 関数を使用します。ドローンをスポーンするときに `drone` ハンドルを受け取ります。
`wait_for(drone)` は、他のドローンが実行していた関数の戻り値を返します。

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

ドローンのスポーンには時間がかかるため、些細なことごとに新しいドローンをスポーンするのは良い考えではありません。

`has_finished(drone)` を使えば、待たなくてもドローンが終わったかどうか確認できるよ。

## 共有メモリなし
各ドローンは独自のメモリを持ち、他のドローンのグローバル変数を直接読み書きすることはできません。

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

これは `0` を表示します。なぜなら、新しいドローンは自身のグローバル `x` のコピーをインクリメントし、これは最初のドローンの `x` に影響しないからです。

## 競合状態
複数のドローンが同時に同じ農場のタイルと対話することがあります。同じティック中に2つのドローンが同じタイルと対話すると、両方の対話が発生しますが、結果は対話の順序によって異なる場合があります。

例えば、ドローン `0` と `1` が両方ともほぼ完全に成長した同じ木の上にいると想像してください。
ドローン `0` は次を呼び出します
`use_item(Items.Fertilizer)`
ドローン `1` は次を呼び出します
`harvest()`

これらのアクションが同時に発生した場合、木はまず肥料を与えられ、次に収穫されます。その場合、木材を受け取ります。しかし、ドローン `1` がわずかに速い場合、木は肥料を与えられる前に収穫され、木材は受け取れません。
これは「競合状態」と呼ばれます。これは並列プログラミングでよくある問題で、結果は操作が実行される順序に依存します。

複数のドローンが同時に同じ位置で同じコードを実行すると、別の問題状況が発生する可能性があります。
`if get_water() < 0.5:
    use_item(Items.Water)`

複数のドローンがこれを同時に実行すると、それらはすべて最初の行を実行し、`if` ブロックに入ります。その後、それらはすべて水を使用し、多くの水を無駄にします。
ドローンが2行目に到達するまでに、他のドローンがその間にタイルに水をやったため、`get_water()` はもはや `0.5` 未満ではないかもしれません。