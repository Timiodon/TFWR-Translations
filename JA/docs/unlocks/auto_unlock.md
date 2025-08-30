# 自動アンロック
ゲームを完全に自動化するために、`unlock()`関数を使って機能を自動的にアンロックできます。
例えば、`unlock(Unlocks.Speed)`や`unlock(Unlocks.Expand)`を使って、スピードや拡張機能をアンロックできます。

アンロックのコストを調べるには、作物やアイテムの場合と同じように`get_cost()`関数を使います。
例:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}`を返します
