# Continue
continueを使うと、ループの現在のイテレーションを停止し、最も内側のループの次のイテレーションにジャンプできます。

`for i in range(10):
	continue
    print("これは決して表示されません")`

これはループの`10`回すべてのイテレーションを実行しますが、`continue`の後の`print`ステートメントは常にスキップされます。

`while`ループでも機能します。

`while True:
	if not can_harvest():
		continue
    
    harvest()`

このコードは`can_harvest()`が`True`のときにのみ`harvest()`を呼び出します。
これは以下と同じ効果があります。

`while True:
	if can_harvest():
		harvest()`

ネストされたループでは、`continue`は常に最も内側のループに影響します。

`for i in range(10):
	for j in range(10):
	    print("これは100回表示されます")
		continue
		print("これは決して表示されません")
	print("これは10回表示されます")`