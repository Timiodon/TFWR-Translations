# 感測
無人機現在看得見了！

函式 `get_pos_x()` 和 `get_pos_y()` 會回傳無人機目前的 x 和 y 位置。在起始位置時，兩者皆為 `0`。往 `East` 每移動一格，x 位置會增加 `1`，往 `North` 每移動一格，y 位置會增加 `1`。

`num_items(item)` 會回傳你擁有的某項物品數量。
舉例來說，`num_items(Items.Hay)` 會回傳你擁有的乾草數量。

`get_entity_type()` 和 `get_ground_type()` 會回傳無人機腳下的實體或地塊類型。

如果你在灌木上方則做翻轉：

```
if get_entity_type() == Entities.Bush:
	do_a_flip()
```

`None` 關鍵字也已解鎖！`None` 表示沒有值。
舉例來說，一個沒有 `return` 陳述式的函式實際上會回傳 `None`。

如果無人機腳下沒有任何實體，`get_entity_type()` 會回傳 `None`。

如果查詢某個解鎖項目的數量，可以使用 `num_unlocked(unlock)` 函式。

例如，`num_unlocked(Unlocks.Speed)` 會回傳你擁有的速度升級等級。

`num_unlocked(Unlocks.Senses)` 如果已解鎖感測會回傳 `1`，否則回傳 `0`。

你也可以對物品、實體或地塊使用 `num_unlocked()`。如果該項目已解鎖則回傳 `1`，否則回傳 `0`。

請小心，`num_unlocked(Unlocks.Carrots)` 會回傳該解鎖被解鎖或升級的次數。
`num_unlocked(Items.Carrot)` 則只會回傳 `0` 或 `1`。（其他植物亦然）