# Sets
Setsは[dictionaries](docs/scripting/dicts.md)みたいなもので、値がないバージョンです。ただの順序のないキーの集まりです。

dictionariesと同じように、値を指定せずに作成します。
`set = {North, East, West}`

`set()`を使って空のセットを作れます。`{}`は空のdictionaryを作ることに注意してね。

`set.add(elem)`を使って、セットに新しい要素を追加できます。

`set.remove(elem)`を使って、セットから要素を削除できます。

`if elem in set:`を使って、そのセットに要素が含まれているかチェックできます。

`for elem in set:`を使って、セット内のすべての要素を順番に処理できます。
大きいセットでは、`in`というoperatorはリストよりもはるかに速く操作できます。

dictionariesと同じように、setsは順序がないので、要素がどの順番で処理されるかは保証されません。

また、sets内の要素はユニークなので、すでにセットにある要素を追加してもセットは変わりません。