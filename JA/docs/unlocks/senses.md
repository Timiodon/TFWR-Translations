# 感覚
ドローンの目が見えるようになりました！

関数 `get_pos_x()` と `get_pos_y()` は、ドローンの現在のx座標とy座標を返します。開始位置では両方とも `0` です。x座標は `East` に向かってタイルごとに `1` ずつ増加し、y座標は `North` に向かってタイルごとに `1` ずつ増加します。

`num_items(item)` は、持っているアイテムの数を返します。
例えば、`num_items(Items.Hay)` は持っている干し草の量を返します。

`get_entity_type()` と `get_ground_type()` は、ドローンの下にあるエンティティまたは地面の種類を返します。

茂みの上にいる場合はフリップを行います:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` キーワードもアンロックされました！ `None` は値がないことを表す値です。
例えば、`return` 文がない関数は実際には `None` を返します。

ドローンの下にエンティティがない場合、`get_entity_type()` は `None` を返します。


特定のアンロックをいくつ持っているかを知りたい場合は、`num_unlocked(unlock)` 関数を使用します。

例えば、`num_unlocked(Unlocks.Speed)` は持っているスピードアップグレードの数を返します。

`num_unlocked(Unlocks.Senses)` は、感覚がアンロックされていれば `1` を、そうでなければ `0` を返します。

`num_unlocked()` はアイテム、エンティティ、地面にも使用できます。これは、アンロックされていれば `1` を、そうでなければ `0` を返します。

`num_unlocked(Unlocks.Carrots)` は、それがアンロック/アップグレードされた回数を返すので注意してください。
`num_unlocked(Items.Carrot)` は `0` または `1` のみを返します。（他の植物も同様です）