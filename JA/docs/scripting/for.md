# Forループ
`for`ループはPythonと同じように動作します。（いくつかの言語ではforeachループと呼ばれ、Cスタイルのforループとは異なるものです）。

`for i in sequence:
	#do something with i`

`while`ループと同様に、`for`ループもコードブロックを繰り返し実行します。条件に基づいてループするのではなく、シーケンス内の各要素に対して一度ずつループ本体を実行します。

## 構文
forループは次のようになります：

`for variable_name in sequence:
	#code block`

`variable_name`は任意の名前にできます。これはシーケンス内の現在の要素を格納する変数です。`sequence`はrangeや数値のように反復可能な値である必要があります。コードブロックは、ループ変数がその要素に割り当てられているすべての要素に対して実行されます。

## シーケンス
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## 例
`for i in range(5):
    harvest()`

このループは、固定回数ループ本体を実行します。これは本質的に以下のコードを書くのと同じです：

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

つまり、`harvest()`を5回呼び出します。

[Break](docs/scripting/break.md)と[Continue](docs/scripting/continue.md)も参照してください。