# If
`if`、`elif`、`else` を使って、特定の条件でコードを実行できます。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 構文
`if`を使うと、条件が`True`の場合にのみコードを実行できます。`while`ループに似ていますが、ループはしません。
`if`は`while`ループと同様に条件を取り、その条件が`True`に評価された場合にifコードブロックを実行します。

`# 条件がTrueならば回る
if condition:
	do_a_flip()`

また、`else`をifの後に追加して、条件が`False`に評価された場合に実行するコードを定義することもできます。

`condition`がTrueならば回り、そうでない場合は収穫します。
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`はelse ifの略です。

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

これを短縮すると次のようになります:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`