# Break
`break`は、ループを早めに終了するために使います。`break`文に到達すると、すぐに最も内側のループを抜け、その後のコードを実行します。

`for i in range(10):
	break
print(i)`
これは`0`を出力します。なぜなら、`i`がループの最初の反復で`0`になり、break文がループを終了させるからです。

`while`ループでも同様に機能します。

`while True:
	if can_harvest():
		break`

このコードは、`can_harvest()`が`True`になるまで`while`ループを実行します。これは次のコードと同じ効果があります。

`while not can_harvest():
	pass`

ネストされたループでは、`break`は常に最も内側のループを終了します。

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`