[<-鐵礦](docs/unlocks/iron.md)
---
# 鐵礦探查

你可能已經發現，鐵礦脈有時很難找。你可以四處挖掘碰碰運氣，但還有更好的辦法：鐵礦有磁性，因此可以從很遠的地方探測到它。

`prospect_iron()` 指令正是為此而設。`prospect_iron()` 會回傳一個基本方向（`North`、`East`、`South` 或 `West`），指示無人機該往哪邊走一步才能接近最近的鐵礦石。每次執行此指令需消耗 1 份煤炭。

如果無人機已在最近的鐵礦石正上方、煤炭不足以執行指令，或者探測範圍內沒有鐵礦，`prospect_iron()` 就會回傳 `None`。

你可以用下面的程式碼向下一塊鐵礦石靠近一步：

`if prospect_iron() != None:
    move(prospect_iron())
`

這段程式碼目前會呼叫兩次 `prospect_iron()`，消耗 2 份煤炭。你可以考慮用變數來最佳化它。

最近的鐵礦石按無人機必須行走的步數判斷。如果鐵礦石位於無人機以東 2 格、以北 3 格處，距離就算作 5，因為無人機需要走五步才能到達。

挖掘也算一步。因此，如果這塊鐵礦埋在地下 7 個地塊深處，距離就是 12：無人機需要先走五步到鐵礦上方，再向下挖七次。

---

[鐵礦](docs/unlocks/iron.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
