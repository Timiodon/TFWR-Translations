# 辞書
辞書は、実際の辞書が単語をその定義に対応付けるのと同じように、キーを値に対応付け、非常に迅速に検索できるデータ構造です。

辞書は次のように作成できます：
`right_of = {North:East, East:South, South:West, West:North}`

コロンの前の式がキーで、コロンの後の式がキーが対応する値です。
上記の辞書は、各方向をその右の方向にマッピングします。

これは、ドローンの位置をその上にあるエンティティにマッピングする別の例です。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

キーにマッピングされた値へのアクセスは、リスト内の要素へのアクセスに似ています：
`value = dict[key]`

例：
`orientation = right_of[South]`
これにより、`orientation` が `West` に設定されます。

辞書に新しいキーと値のペアを追加するには、次のようにします：
`dict[key] = value`

例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
これにより、現在の位置に保存されているエンティティが更新されます。

キーは一意なので、辞書にすでに存在するキーを追加すると、以前の値が上書きされます。

`dict` からキーと値のペアを削除するには、`dict.pop(key)` を使用します。

`key in dict` は、`key` が `dict` のキーである場合は `True`、そうでない場合は `False` に評価されます。
したがって、`if key in dict:` を使用して `dict` にキーが含まれているかどうかを確認できます。

forループで辞書を使用すると、すべてのキーを反復処理できます：
`for key in dict:
	value = dict[key]`

キーが反復される順序についての保証はありません。

参照：[セット](docs/scripting/sets.md)