# コスト
どんなコストも、アイテムを数値にマッピングする辞書として表現できます。

`get_cost()` 関数は、そのような辞書を返します。植物やアンロックのコストを返します。

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}` を返します。

アンロックの場合、コストを知りたいアンロックレベルをオプションの第2引数として渡すことができます。デフォルトでは、現在のアンロックレベルです。

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}` を返します。

すでに最大レベルのアンロックの場合、`get_cost()` は `None` を返します。

次のように使用できます:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
