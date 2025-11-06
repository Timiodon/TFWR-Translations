# 擴張 2
你的農場再次擴張了！現在格子已不再整齊排列，因此你需要找到遍歷網格的方式。

使用 `while` 迴圈在未解鎖感知和運算子之前無法做到這件事。
現在是時候介紹 `for` 迴圈了。

你可以在 [for 迴圈](docs/scripting/for.md)頁面閱讀關於 `for` 迴圈的全部內容，但目前你只需要用它來重複執行固定次數的程式碼。

```
# 做 n 次翻轉
for i in range(5):
	do_a_flip()
```

`range(n)` 會建立從 `0` 到 `n-1` 的數列，包含 `n` 個元素。`for` 循迴圈會對序列中的每一個元素各執行一次迴圈主體。在這個範例中，`do_a_flip()` 會被呼叫 `5` 次。

現在也可以使用 `get_world_size()` 函式。它會回傳你農場的邊長。這樣你就可以撰寫在下次擴張後也不會壞掉的程式碼。

```
for i in range(get_world_size()):
	harvest()
	move(North)
```

此範例會對任意農場大小採收一整列。

如果你在思考如何讓無人機遍歷整個農場時卡住了，請參考下方提示。
<spoiler=顯示提示>當然，有多種方式可以在農場中移動。
但我們要尋找的是一種系統性的遍歷方法，能在農場再度擴張時仍然有效。
一種系統性到達農場每個格子的方式是無限重複下列兩個步驟：

1.向 `North` 移動，直到繞回起點。
2.向 `East` 移動。

`for i in range(get_world_size()):` 可能有助於將這個想法轉換成程式碼。
</spoiler>
<spoiler=顯示可能的解決方案>基本的遍歷可能如下所示：

```
for i in range(get_world_size()):
	for j in range(get_world_size()):
		# 在每個地塊翻轉一次
		do_a_flip()
		move(North)
	move(East)
```
</spoiler>