# Dictionaries
Dictionariesは、実際の辞書が言葉をその定義に紐づけるのと同じように、キーを値に紐づけることができるデータ構造です。これを使うと、情報を非常に素早く探せます。

辞書は以下のように作成できます：
`rotation = {North:East, East:South, South:West, West:North}`

コロンの前の表現がキーで、コロンの後の表現がキーが紐づけられる値です。
上の辞書は、それぞれの方角をその右側の方角に紐づけています。

ドローンの位置をその上にあるentityに紐づける別の例です：
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

キーに紐づけられた値にアクセスするのは、リスト要素にアクセスするのと同様です：
`value = dict[key]`

例：
`orientation = rotation[South]`
これにより、`orientation`は`West`になります。

新しいキー値ペアを辞書に追加するには、以下のようにします：
`dict[key] = value`

例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
これにより、現在の位置に保存されているentityが更新されます。

キーは一意ですので、辞書内にすでに存在するキーを追加すると、前の値が上書きされます。

`dict.pop(key)`を使って`dict`からキー値ペアを削除できます。

`key in dict`は`key`が`dict`内のキーであれば`True`、そうでなければ`False`を返します。
ですので、`if key in dict:`を使って、`dict`がキーを含んでいるか確認できます。

辞書をforループに入れると、すべてのキーを順に処理することができます：
`for key in dict:
	value = dict[key]`

キーが処理される順序に関しては、保証はありません。

また[Sets](docs/scripting/sets.md)も参照してください。