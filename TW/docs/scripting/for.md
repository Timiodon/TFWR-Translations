# for 迴圈
`for` 迴圈的運作方式與 Python 相同（在某些語言中稱為 foreach 迴圈，但不要與 C 語言風格的 for 迴圈混淆，後者是不同的語法）。

```
for i in sequence:
	# 對 i 執行某些操作
```

與 `while` 迴圈類似，`for` 迴圈也會重複執行一段程式碼。不同之處在於它不是根據條件判斷來迴圈，而是對序列中的每一個元素各執行一次迴圈主體。

## 語法
for 迴圈的範例語法如下：

```
for variable_name in sequence:
	# 程式碼區塊
```

`variable_name` 可以是你選擇的任意名稱。它是一個，用來儲存序列中目前元素的變數。`sequence` 必須是可被迭代的值，例如數字範圍。程式碼區塊會對序列中的每一個元素執行一次，且迴圈變數在每次執行時會被指派為該元素。

## 序列
[範圍](functions/range)      <unlock=lists>[串列](docs/scripting/lists.md)      </unlock><unlock=functions>[元組](docs/scripting/tuples.md)      </unlock><unlock=dicts>[字典](docs/scripting/dicts.md)      </unlock><unlock=sets>[集合](docs/scripting/sets.md)</unlock>

## 範例

```
for i in range(5):
    harvest()
```

這個迴圈會執行固定次數的迴圈主體，基本上等同於寫成：

```
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
```

因此它會呼叫 `harvest()` 五次。

另請詳閱 [break 陳述式](docs/scripting/break.md)和 [continue 陳述式](docs/scripting/continue.md)。