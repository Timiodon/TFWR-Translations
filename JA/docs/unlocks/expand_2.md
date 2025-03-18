# Expand 2
あなたの農場がまた広がりました！ 今度はタイルがきれいに並んでいないので、正方形のグリッドを移動する方法を見つける必要があります。

`while`ループではセンサーとオペレーターを解放しない限り可能ではありません。
ここで`for`ループを紹介します。

[For Loop](docs/scripting/for.md)ページで`for`ループについて詳しく読むことができますが、今のところはコードを一定回数繰り返すためだけに使用します。

`#do n flips
for i in range(5):
	do_a_flip()`

`range(n)`は`0`から`n-1`までの`n`個の要素の範囲を作成します。`for`ループはそのシーケンスの各要素に対してループの本体を1回実行します。この例では`do_a_flip()`が`5`回呼び出されます。

`get_world_size()`関数も利用可能です。この関数は農場の辺の長さを返します。これにより、次の拡張アップグレードでコードが壊れないように対策できます。

`for i in range(get_world_size()):
	harvest()
	move(North)`

この例では、どんな農場サイズでも1列の収穫を行います。

農場でドローンを移動する方法がわからない場合は、以下のヒントを参照してください。
<spoiler=show hint>農場を移動する方法はいくつかあります。
私たちが探しているのは、農場がまた成長しても壊れない、体系的にすべての場所を訪れる方法です。
農場のすべての場所に到達するための体系的な方法は、次の2つの手順を永久に繰り返すことです：

1.`North`に移動し、元に戻るまで。
2.`East`に移動する。

`for i in range(get_world_size()):`を使用すると、このアイデアをコードに変えるのに役立つでしょう。
</spoiler>

<spoiler=show possible solution> 基本的な移動方法は次のようになります：

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#do a flip on every tile
		do_a_flip()
		move(North)
	move(East)`
</spoiler>