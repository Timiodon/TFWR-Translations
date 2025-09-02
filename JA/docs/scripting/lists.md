# リスト
リストは、複数の値を1つの変数に簡単に格納する方法です。
次のように新しいリストを作成できます:

`list = [2, True, Items.Hay]`

これでリストには `2`、`True`、`Items.Hay` の値が含まれます。
リストは空にすることもできます:

`empty_list = []`

リストの要素にはインデックスでアクセスできます。インデックスは最初の要素が `0`、2番目の要素が `1`、3番目の要素が `2`...となります。

ニンジンを植える
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

forループを使ってリストを反復処理できます。次の例では、リスト内のすべての要素を合計します。

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` は `18` になります。

次のリストメソッドで要素を追加・削除できます:

`list.append(elem)` はリストの末尾に要素を追加します:

`list = [2, 6, 12]
list.append(7)`
`list` は `[2, 6, 12, 7]` になります。

`list.remove(elem)` はリストから最初に現れる要素を削除します:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` は `[1, 4, 2]` になります。

`list.insert(index, elem)` は指定されたインデックスに要素を挿入します:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` は `[Entities.Tree, Items.Wood, Items.Hay]` になります。

`list.pop(index)` は指定されたインデックスの要素を削除します。
インデックスが指定されていない場合、最後のアイテムが削除されます。

`list = [3, 5, 8, 25]
list.pop()`
`list` は `[3, 5, 8]` になります。
`list.pop(1)`
`list` は `[3, 8]` になります。

`len()` 関数はリストの長さを返します。
`list = [3, 2, 1]
x = len(list)`
`x` は `3` になります。

リストは参照セマンティクスを持ちます。これは、リストをコピーするのではなく、リストを同じリストオブジェクトに割り当てることを意味します。
2つの変数が同じリストを参照している場合、リストへの変更は両方から見えます。

`a = [1,2]
b = a
b.pop()`
`a` と `b` は両方とも `[1]` になります。
