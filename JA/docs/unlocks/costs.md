# コスト
コストは、アイテムを数値にマッピングするdictionaryで表現できます。

`get_cost()`関数は、そのようなdictionaryを返します。それは植物やアンロックのコストを返します。

`get_cost(Entities.Pumpkin)`
は`{Items.Carrot:1}`を返します。

アンロックの場合、アンロックレベルのコストを取得するためにオプショナルで2番目のargumentを渡すことができます。デフォルトでは、現在のアンロックレベルです。

`get_cost(Unlocks.Loops, 0)`
は`{Items.Hay:5}`を返します。

すでに最大レベルのアンロックの場合、`get_cost()`は`None`を返します。

このように使うことができます：
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`