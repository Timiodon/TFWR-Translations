# if 陳述式
你可以使用 if、elif 和 else 來有條件地執行程式碼。

```
if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
```

## 語法
`if` 可以讓程式碼僅在某個條件為 `True` 時執行。如同一個不會迭代的 `while` 迴圈。
`if` 與 `while` 迴圈一樣會接受一個條件，當該條件評估為 `True` 時，就會執行 `if` 的程式碼區塊：

```
# 如果 condition 為 True 則做翻轉
if condition:
	do_a_flip()
```

你也可以在 `if` 之後加上 `else`，定義當條件為 `False` 時要執行的程式碼。

```
# 如果 condition 為 True 則做翻轉，否則採收
if condition:
	do_a_flip()
else:
	harvest()
```

`elif` 是 else if 的縮寫。

```
if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c
```

可以簡化成：

```
if condition1:
	#a
elif condition2:
	#b
else:
	#c
```
