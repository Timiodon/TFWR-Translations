# 自動アンロック
ゲームを完全に自動化するためには、`unlock()` 関数を使って機能を自動でアンロックすることができます。
例えば、`unlock(Unlocks.Speed)` や `unlock(Unlocks.Expand)` を使って、スピードと拡張機能をアンロックできます。

アンロックにかかるコストを知りたいときは、植物やアイテムと同じように `get_cost()` 関数を使います。
例:
`get_cost(Unlocks.Loops)`
は `{Items.Hay:5}` を返します。

特定のアンロックをいくつ持っているか知りたいときは、`num_unlocked(unlock)` 関数を使います。

例えば、`num_unlocked(Unlocks.Speed)` はスピードのアップグレード数を返します。

`num_unlocked(Unlocks.Senses)` は、センサーがアンロックされている場合は `1` を返し、されていない場合は `0` を返します。

アイテム、エンティティ、または地面でも `num_unlocked()` を使うことができ、アンロックされている場合は `1` を、そうでない場合は `0` を返します。

注意してください。`num_unlocked(Unlocks.Carrots)` はアンロック/アップグレードされた回数を返します。
`num_unlocked(Items.Carrot)` は `0` か `1` だけを返します。（他の植物も同じです）