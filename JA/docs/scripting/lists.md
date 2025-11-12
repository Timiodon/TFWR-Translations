# リスト
リストは、複数の値を1つの変数に簡単に格納する方法です。
次のように新しいリストを作成できます:

`some_list = [2, True, Items.Hay]`

これでリストには `2`、`True`、`Items.Hay` の値が含まれます。
リストは空にすることもできます:

`empty_list = []`

リストの要素にはインデックスでアクセスできます。インデックスは最初の要素が `0`、2番目の要素が `1`、3番目の要素が `2`...となります。

ニンジンを植える
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

forループを使ってリストを反復処理できます。次の例では、リスト内のすべての要素を合計します。

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` は `18` になります。

次のリストメソッドで要素を追加・削除できます:

`elements.append(elem)` はリストの末尾に要素を追加します:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` は `[2, 6, 12, 7]` になります。

`elements.remove(elem)` はリストから最初に現れる要素を削除します:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` は `[1, 4, 2]` になります。

`elements.insert(index, elem)` は指定されたインデックスに要素を挿入します:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` は `[Entities.Tree, Items.Wood, Items.Hay]` になります。

`elements.pop(index)` は指定されたインデックスの要素を削除します。
インデックスが指定されていない場合、最後のアイテムが削除されます。

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` は `[3, 5, 8]` になります。
`numbers.pop(1)`
`numbers` は `[3, 8]` になります。

`len()` 関数はリストの長さを返します。
`numbers = [3, 2, 1]
x = len(numbers)`
`x` は `3` になります。

リストは参照セマンティクスを持ちます。これは、リストをコピーするのではなく、リストを同じリストオブジェクトに割り当てることを意味します。
2つの変数が同じリストを参照している場合、リストへの変更は両方から見えます。

`a = [1, 2]
b = a
b.pop()`
`a` と `b` は両方とも `[1]` になります。
