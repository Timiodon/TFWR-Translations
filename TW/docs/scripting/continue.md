# continue 陳述式
continue 允許中斷迴圈目前的迭代並跳到最內層迴圈的下一個迭代。

```
for i in range(10):
	continue
    print("這永遠不會印出")
```

這將運行迴圈的所有 `10` 次迭代，但 `continue` 之後的 `print` 陳述式總是會被跳過。

它也適用於 `while` 迴圈。

```
while True:
	if not can_harvest():
		continue

	harvest()
```

此程式碼僅在 `can_harvest()` 為 `True` 時呼叫 `harvest()`。
其效果與與以下程式碼相同：

```
while True:
	if can_harvest():
		harvest()
```

在巢狀迴圈中，`continue` 始終影響最內層迴圈。

```
for i in range(10):
	for j in range(10):
 		print("這句會印出 100 次")`
		continue
 		print("這句話永遠不會印出")
 	print("這句會印出 10 次")
```