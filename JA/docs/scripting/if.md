# If文
if、elif、elseを使って、条件に応じてコードを実行できます。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 構文
`if`を使うと、ある条件が`True`の場合にのみコードを実行できます。これはループしない`while`ループのようなものです。
`if`は`while`ループと同様に条件を取り、その条件が`True`と評価された場合にifのコードブロックを実行します:

`#conditionがTrueの場合にフリップを実行
if condition:
	do_a_flip()`

ifの後に`else`を追加することもでき、これは条件が`False`と評価された場合に実行されるコードを定義します。

`condition`がTrueの場合はフリップを行い、そうでなければ収穫します。
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`はelse ifの短縮形です。

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

は、次のように短縮できます:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
