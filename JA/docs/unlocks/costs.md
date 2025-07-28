# コスト
どんなコストも、アイテムを数値にマッピングするdictionaryとして表現できます。

`get_cost()`関数は、そのようなdictionaryを返します。これは、作物やアンロックのコストを返します。

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}`を返します

アンロックの場合、オプションで2番目の引数を渡して、コストを取得したいアンロックレベルを指定できます。デフォルトでは、現在のアンロックレベルです。

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}`を返します

すでに最大レベルにあるアンロックの場合、`get_cost()`は`None`を返します。

このように使用できます:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
