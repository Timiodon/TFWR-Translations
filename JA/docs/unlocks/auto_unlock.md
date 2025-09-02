# 自動アンロック
ゲームを完全に自動化するには、`unlock()` 関数を使用して機能を自動的にアンロックできます。
例えば、`unlock(Unlocks.Speed)` や `unlock(Unlocks.Expand)` を使用して、スピードや拡張機能をアンロックできます。

アンロックのコストを決定するには、植物やアイテムの場合と同様に `get_cost()` 関数を使用するだけです。
例:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}` を返します。
