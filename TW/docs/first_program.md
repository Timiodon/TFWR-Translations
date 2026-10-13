[<- 入門指南](docs/getting_started.md) <right>[While 迴圈 ->](docs/scripting/while.md)
---
# 第一個程式
## 文字編輯器

只需要在程式碼編輯視窗中編寫程式碼就可以完成 1 個程式的編寫。每個視窗都對應 1 個程式碼檔案，裡面的內容就是你正在編寫的程式碼。
你可以透過按一下視窗頂部的檔案名稱來重命名檔案。

程式停止執行時，就可以在視窗中編寫程式碼，像使用其他的文字編輯器一樣。
按一下視窗中的綠色執行按鈕可以直接執行程式。
![|x50](PlayButton)

按一下螢幕右上角的「+」按鈕可以建立新的程式碼檔案。
將一個視窗拖到另一個視窗上，兩個視窗可以有序地堆放在一起。

在視窗中編寫程式碼時，會彈出一個簡單的程式碼自動完成視窗。
按 Tab 鍵可以插入選取的自動完成內容。
使用方向鍵可以在自動完成選項之間切換。

如果你是第一次程式設計，新手也可以快速上手。這些功能是逐步解鎖的，相關知識不會一股腦地砸下來，讓你手忙腳亂。
這款遊戲中程式設計的語法也與 Python 相似，而 Python 是世界上使用最廣泛的程式設計語言之一，所以學習它並不是在浪費時間。

如果已經了解 Python，恭喜！你可以快速跳過遊戲的早期階段，進入更有趣的部分。

目前，有兩個函式可以用來操控無人機。

`harvest()`

和

`do_a_flip()`

這種寫法就是呼叫這個函式。函式可以看作是一個可執行的指令，使用 `()` 圓括號來執行。

在視窗中輸入這 2 個陳述式，然後按一下執行按鈕，就可以讓無人機動起來，你自己試試看吧！

你可以把程式碼看成一系列陳述式。把多個陳述式寫在不同行上，就能依次執行。
試著按一下下方嵌入式程式碼視窗中的執行按鈕，看看程式碼如何執行：

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## 科技樹
收集草可獲得乾草。乾草可以用來在科技樹中解鎖迴圈功能。按一下右上角的按鈕可開啟科技樹。

---

[外部編輯器](docs/external_editor.md)      [註解](docs/scripting/comments.md)      [While 迴圈](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
