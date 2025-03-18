# リスト
リストは、1つの変数に複数の値を簡単に保存する方法です。
新しいリストは次のように作成できます：

`list = [2, True, Items.Hay]`

このリストには、`2`、`True`、`Items.Hay` という値が含まれています。
リストは空にもできます：

`empty_list = []`

リストの要素には、そのインデックスを使ってアクセスできます。最初の要素のインデックスは `0` で、2番目の要素のインデックスは `1`、3番目の要素のインデックスは `2` です...

ニンジンを植える
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

for ループを使ってリストを反復処理できます。次の例では、リスト内の全ての要素を合計します。

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` は現在 `18` です

次のリストメソッドは、要素を追加および削除するためのものです：

`list.append(elem)` はリストの末尾に要素を追加します：

`list = [2, 6, 12]
list.append(7)`
`list` は現在 `[2, 6, 12, 7]` です

`list.remove(elem)` はリストから最初の指定した要素を削除します：

`list = [1, 2, 4, 2]
list.remove(2)`
`list` は現在 `[1, 4, 2]` です

`list.insert(index, elem)` は指定したインデックスに要素を挿入します：

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` は現在 `[Entities.Tree, Items.Wood, Items.Hay]` です

`list.pop(index)` は指定したインデックスの要素を削除します。
インデックスを指定しない場合、最後の要素が削除されます。

`list = [3, 5, 8, 25]
list.pop()`
`list` は現在 `[3, 5, 8]` です
`list.pop(1)`
`list` は現在 `[3, 8]` です

`len()` 関数はリストの長さを返します。
`list = [3, 2, 1]
x = len(list)`
`x` は現在 `3` です

リストは参照セマンティクスを持ちます。これは、リストを変数に代入すると、そのリストオブジェクト自体をその変数に代入することを意味し、リストのコピーを作成するわけではありません。
もし2つの変数が同じリストを参照している場合、そのリストへの変更は両方から観察できます。

`a = [1,2]
b = a
b.pop()`
`a` と `b` は現在両方 `[1]` です