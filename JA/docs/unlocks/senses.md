# 感覚
ドローンが見えるようになりました！

`get_pos_x()`と`get_pos_y()`関数は、ドローンの現在のxおよびy座標を返します。開始位置では、両方とも`0`です。x座標は`East`に向かってタイルごとに`1`増加し、y座標は`North`に向かってタイルごとに`1`増加します。

`num_items(item)`は、あなたが持っているアイテムの数を返します。
例えば、`num_items(Items.Hay)`はあなたが持っている干し草の量を返します。

`get_entity_type()`と`get_ground_type()`は、ドローンの下にあるentityまたは地面のタイプを返します。

茂みの上にいるなら、フリップします:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None`キーワードもアンロックされました！ `None`は値がないことを表す値です。
例えば、`return`ステートメントがない関数は、実際には`None`を返します。

`get_entity_type()`は、ドローンの下にentityがない場合、`None`を返します。


特定のアンロックをいくつ持っているかを知りたい場合は、`num_unlocked(unlock)`関数を使用します。

例えば、`num_unlocked(Unlocks.Speed)`はあなたが持っているスピードアップグレードの数を返します。

`num_unlocked(Unlocks.Senses)`は、感覚がアンロックされていれば`1`を、されていなければ`0`を返します。

`num_unlocked()`は、アイテム、エンティティ、地面に対しても使用できます。アンロックされていれば`1`を、そうでなければ`0`を返します。

注意してください、`num_unlocked(Unlocks.Carrots)`はアンロック/アップグレードされた回数を返します。
`num_unlocked(Items.Carrot)`は`0`か`1`しか返しません。（他の作物も同様です）