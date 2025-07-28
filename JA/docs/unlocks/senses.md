# 感覚
ドローンが見えるようになりました！

`get_pos_x()`と`get_pos_y()`関数は、ドローンの現在のxおよびy座標を返します。開始位置では両方とも`0`です。x座標は`East`に向かってタイルごとに`1`ずつ増加し、y座標は`North`に向かってタイルごとに`1`ずつ増加します。

`num_items(item)`は、アイテムをいくつ持っているかを返します。
例えば、`num_items(Items.Hay)`は持っている干し草の量を返します。

`get_entity_type()`と`get_ground_type()`は、ドローンの下にあるentityまたは地面の種類を返します。

茂みの上にいるならフリップします:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None`キーワードもアンロックされました！`None`は値がないことを表す値です。
例えば、`return`ステートメントがない関数は実際には`None`を返します。

`get_entity_type()`は、ドローンの下にentityがない場合に`None`を返します。
