# If文
if、elif、else を使って、条件付きでコードを実行できます。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 構文
`if` を使うと、ある条件が `True` の場合にのみコードを実行できます。これはループしない `while` ループのようなものです。
`if` は `while` ループと同じように条件を取り、条件が `True` に評価された場合にifコードブロックを実行します:

`#conditionがTrueの場合にフリップを実行
if condition:
	do_a_flip()`

ifの後に `else` を追加して、条件が `False` に評価された場合に実行されるコードを定義することもできます。

`condition` がTrueの場合はフリップを実行し、そうでない場合は収穫します。
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` は else if の短縮形です。

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
