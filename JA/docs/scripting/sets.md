# set
setは[dictionary](docs/scripting/dicts.md)に似ていますが、値がありません。順序のないキーの集まりです。

-dictionaryのように作成されますが、値はありません。
`set = {North, East, West}`

空のsetを作成するには`set()`を使用します。`{}`は空のdictionaryを作成することに注意してください。

`set.add(elem)`を使用して、setに新しい要素を追加します。

`set.remove(elem)`を使用して、setから要素を削除します。

`if elem in set:`を使用して、setに要素が含まれているかを確認します。

`for elem in set:`を使用して、set内のすべての要素をイテレートします。
大きなsetの場合、`in`演算子はlistよりもはるかに高速に動作します。

dictionaryと同様に、setは順序付けられていないため、要素がイテレートされる順序についての保証はありません。

また、set内の要素は一意であるため、既にsetにある要素を追加してもsetは変更されません。