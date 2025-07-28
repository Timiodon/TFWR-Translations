# Break
`break`を使うと、ループを途中で停止できます。`break`ステートメントに到達すると、最も内側のループをすぐに抜け出し、ループの後のコードの実行を開始します。

`for i in range(10):
	break
print(i)`
これは`0`を表示します。なぜなら、ループの最初のイテレーションで`i`は`0`であり、その後breakステートメントがループを終了させるからです。

`while`ループでも機能します。

`while True:
	if can_harvest():
		break`

このコードは`can_harvest()`が`True`になるまで`while`ループを実行します。
これは以下と同じ効果があります。

`while not can_harvest():
	pass`

ネストされたループでは、`break`は常に最も内側のループを終了させます。

`for i in range(10):
	for j in range(10):
		break
		print("これは決して表示されません")
	print("これは10回表示されます")`