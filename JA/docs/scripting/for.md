# Forループ
`for`ループはPythonのように機能します。（一部の言語ではforeachループと呼ばれ、Cスタイルのforループとは異なります）。

`for i in sequence:
	# iを使って何かをする`

`while`ループと同様に、`for`ループもコードのブロックを繰り返し呼び出します。条件に基づいてループする代わりに、シーケンス内の各要素に対してループ本体を一度実行します。

## 構文
forループは次のようになります：

`for variable_name in sequence:
	#コードブロック`

`variable_name`は自由に選べる名前です。これはシーケンス内の現在の要素を格納する変数です。`sequence`は、数値の範囲のように反復可能な値である必要があります。コードブロックは、ループ変数がその要素に割り当てられた状態で、すべての要素に対して実行されます。

## シーケンス
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## 例
`for i in range(5):
    harvest()`

このループは本体を固定回数実行します。これは本質的に次のように書くのと同じです。

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

したがって、`harvest()`を5回呼び出します。

[Break](docs/scripting/break.md)と[Continue](docs/scripting/continue.md)も参照してください