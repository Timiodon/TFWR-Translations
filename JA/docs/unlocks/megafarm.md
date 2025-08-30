# メガファーム
この信じられないほど強力なアンロックにより、複数のドローンにアクセスできるようになります。

以前と同様、最初は1体のドローンから始まります。追加のドローンはまずスポーンする必要があり、プログラムが終了すると消えます。
各ドローンは独自の別のプログラムを実行します。新しいドローンは`spawn_drone(function)`関数を使ってスポーンできます。

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

これは、`spawn_drone(function)`コマンドを実行したドローンと同じ位置に新しいドローンをスポーンします。新しいドローンは指定された関数の実行を開始し、完了すると自動的に消えます。

ドローンは互いに衝突しません。

`max_drones()`を使って、スポーンできるドローンの最大数を取得します。
`num_drones()`を使って、すでに農場にいるドローンの数を取得します。


## 例:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

これにより、最初のドローンが水平に移動し、より多くのドローンをスポーンするようになります。
スポーンされたドローンは垂直に移動し、進路上のすべてを収穫します。

利用可能なすべてのドローンがすでにスポーンされている場合、`spawn_drone()`は何もしないで`None`を返します。

<spoiler=show hint> この非常に便利な並列`for_all`関数をチェックしてみてください。これは任意の関数を取り、農場のすべてのタイルで実行します。そのために利用可能なすべてのドローンを使用します。

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

forall(harvest)`

特に便利なパターンの1つは、ドローンが利用可能であればスポーンし、そうでなければ自分で実行することです。

`if not spawn_drone(task):
	task()`
</spoiler>

## 他のドローンを待機
`wait_for(drone)`関数を使用して、他のドローンが終了するのを待ちます。ドローンをスポーンするときに`drone`ハンドルを受け取ります。
`wait_for(drone)`は、他のドローンが実行していた関数の戻り値を返します。

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

ドローンをスポーンするには時間がかかるため、些細なことのために新しいドローンをスポーンするのは良い考えではありません。

## 共有メモリなし
各ドローンは独自のメモリを持ち、他のドローンのグローバルを直接読み書きすることはできません。

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

新しいドローンはグローバル`x`の独自のコピーをインクリメントしたため、これは`0`を表示します。これは最初のドローンの`x`には影響しません。

## 競合状態
複数のドローンが同時に同じ農場のタイルと相互作用できます。2体のドローンが同じtick中に同じタイルと相互作用した場合、両方の相互作用が発生しますが、相互作用の順序によって結果が異なる場合があります。

例えば、ドローン`0`と`1`が両方とも、ほぼ完全に成長した同じ木の上にいると想像してください。
ドローン`0`は呼び出す
`use_item(Items.Fertilizer)`
ドローン`1`は呼び出す
`harvest()`

これらのアクションが同時に発生した場合、木はまず肥料を与えられ、次に収穫されます。その場合、木材を受け取ります。しかし、ドローン`1`がわずかに速い場合、木は肥料を与えられる前に収穫され、木材は受け取れません。
これは「競合状態」と呼ばれます。これは並列プログラミングでよくある問題で、結果が操作の実行順序に依存します。

複数のドローンが同じ位置で同時に同じコードを実行するときに発生する可能性のある、もう1つの問題のある状況です。
`if get_water() < 0.5:
    use_item(Items.Water)`

複数のドローンがこれを同時に実行すると、すべてが最初の行を実行し、`if`ブロックに入ります。その後、すべてが水を使い、多くの水を無駄にします。
あるドローンが2行目に到達する頃には、他のドローンがその間にタイルに水を与えたため、`get_water()`はもはや`0.5`未満ではないかもしれません。