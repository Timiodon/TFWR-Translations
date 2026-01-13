# break 陳述式
`break` 允許提前停止迴圈。執行到 `break` 陳述式時，會立即退出最內層的迴圈，並開始執行該迴圈之後的程式碼。

```
for i in range(10):
	break
print(i)
```

這段程式碼會印出 `0`，因為在迴圈的第一次迭代中 `i` 是 `0`，然後 `break` 陳述式結束了迴圈。

該陳述式也適用於 `while` 迴圈。

```
while True:
 	if can_harvest():
 		break
```

這段程式碼會一直執行 `while` 迴圈，直到 `can_harvest()` 為 `True`。
其效果與以下程式碼相同：

```
while not can_harvest():
	pass
```

在巢狀迴圈中，`break` 總是會退出最內層的迴圈。

```
for i in range(10):
	for j in range(10):
		break
 		print("這句話永遠不會印出")
 	print("這句會印出 10 次")
```