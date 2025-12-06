# 外部編輯器
遊戲內建的文字編輯器通常足以運行這款遊戲，但它當然無法與 Visual Studio Code 等更複雜的文字編輯器相媲美。

遊戲將所有程式碼檔案儲存為 .py 檔案，因此你可以使用 Python 編輯器進行編輯。
請注意，這只是為了方便起見。遊戲內建語言實際上並非 Python，但與 Python 非常接近，「Python 智慧型程式碼補全」可以很好地支援它。
你可以在[存檔資料夾](persistent_data_path/Saves)中找到這些檔案。

每個存檔還包含一個 `__builtins__.py` 檔案，其中包含與遊戲內建函式相符的內建 Python 定義，以便啟用智慧型程式碼補全。
VS Code 能夠自動偵測 `__builtins__.py`，但某些編輯器可能只有先加入 `from __builtins__ import *` 時才能運作。

要在遊戲中查看外部變更而無需重新載入存檔檔案，你必須開啟「檔案監視器」選項。如果你在外部建立或刪除檔案，則仍需要重新載入存檔才能查看。

## 使用 VS Code

推薦使用 Visual Studio Code 來寫《The Farmer Was Replaced》。

你可以在[此處](https://code.visualstudio.com/download)安裝。

下載後，在 VS Code 中安裝 Python 擴充功能。

完成後，在 VS Code 中開啟存放 `.py` 檔案的[資料夾](persistent_data_path/Saves)。請確保打開整個資料夾，而不是單一檔案，否則 `__builtins__.py` 檔案將不起作用。

在遊戲中，請確保你已開啟「檔案監視器」選項。現在，每次在 VS Code 中儲存時，變更都會自動顯示在遊戲中。

就這樣！現在你可以在專業的程式碼編輯器中編寫程式了！
