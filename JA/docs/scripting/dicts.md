# Dictionaries
Dictionaryは、実際の辞書が単語をその定義に対応させるのと同じように、キーを値に対応させ、非常に迅速に検索できるデータ構造です。

Dictionaryは次のように作成できます：
`right_of = {North:East, East:South, South:West, West:North}`

コロンの前の式がキーで、コロンの後の式がキーがマッピングされる値です。
上記のdictionaryは、各方向をその右側の方向にマッピングします。

もう一つの例として、ドローンの位置をその上にあるentityに対応させるものがあります。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

キーに対応する値にアクセスするのは、リストの要素にアクセスするのと似ています：
`value = dict[key]`

例：
`orientation = right_of[South]`
これにより`orientation`が`West`に設定されます。

新しいキーと値のペアをdictionaryに追加するには、次のようにします：
`dict[key] = value`

例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
これにより、現在の位置に保存されているentityが更新されます。

キーは一意であるため、既にdictionaryに存在するキーを追加すると、前の値が上書きされます。

`dict`からキーと値のペアを削除するには`dict.pop(key)`を使用します。

`key in dict`は、`key`が`dict`のキーであれば`True`に、そうでなければ`False`に評価されます。
そのため、`if key in dict:`を使って`dict`にキーが含まれているかを確認できます。

forループでdictionaryを使用すると、すべてのキーを反復処理できます：
`for key in dict:
	value = dict[key]`

キーが反復される順序についての保証はありません。

[Sets](docs/scripting/sets.md)も参照してください