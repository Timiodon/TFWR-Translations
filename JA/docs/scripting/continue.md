# Continue
continueは、ループの現在の反復を停止し、最も内側のループの次の反復にジャンプすることを可能にします。

`for i in range(10):
	continue
    print("this is never printed")`

これはループの全ての`10`回の反復を実行しますが、`continue`の後の`print`文は常にスキップされます。

これは`while`ループでも機能します。

`while True:
	if not can_harvest():
		continue
    
    harvest()`

このコードは`can_harvest()`が`True`のときだけ`harvest()`を呼び出します。 これは次のコードと同じ効果があります。

`while True:
	if can_harvest():
		harvest()`

ネストされたループでは、`continue`は常に最も内側のループに影響します。

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`