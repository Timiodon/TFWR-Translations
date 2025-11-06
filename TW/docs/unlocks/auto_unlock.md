# 自動解鎖
要完全自動化遊戲，你可以使用 `unlock()` 函式自動解鎖功能。
例如，你可以使用 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 來解鎖速度和擴展功能。

要決定某個解鎖的花費，只要像查詢植物或物品花費一樣使用 `get_cost()` 函式。
範例：

```
get_cost(Unlocks.Loops)
```

回傳 `{Items.Hay:5}`