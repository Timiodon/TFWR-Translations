# 外部編輯器
遊戲內建的文字編輯器就可以用來玩這款遊戲，當然，它比不上像 Visual Studio Code 這樣更複雜的文字編輯器。

遊戲將所有程式碼檔案儲存為 .py 檔案，這樣很方便用 Python 編輯器來進行編輯。
請注意：這只是為了方便。實際上，遊戲內的語言並非 Python，只是語法與之相似，因此，可以正常使用 Python 的智慧提示（IntelliSense）。
你可以在[存檔資料夾](persistent_data_path/Saves)中找到這些檔案。

持久資料資料夾位於：

- Windows：`%USERPROFILE%\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced`
- macOS：`~/Library/Application Support/com.TheFarmerWasReplaced.TheFarmerWasReplaced`
- Linux（Steam/Proton）：`~/.steam/steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced`

每個存檔中還有一個 `__builtins__.py` 檔案，其中包含與遊戲內建函式相符的 Python 內建定義，讓 IntelliSense 生效。
VS Code 能夠自動檢測 `__builtins__.py` 檔案，但有些編輯器可能需要先新增 `from __builtins__ import *` 才能生效。

如果要在無需重新載入存檔的情況下，在遊戲內看到外部更改，則必須啟用「檔案監視器」選項。如果在外部建立或刪除檔案，則仍需重新載入存檔才能檢視。

## 使用 VS Code
Visual Studio Code 是《The Farmer Was Replaced》推薦使用的程式碼編輯器。

你可以[按一下此處](https://code.visualstudio.com/download)下載。

下載完成後，需要在 VS Code 中安裝 Python 擴充功能。

安裝完 Python 擴充功能後，在 VS Code 中開啟存放你的 `.py` 檔案的[資料夾](persistent_data_path/Saves)。必須開啟整個資料夾，而不只是單個檔案，否則 `__builtins__.py` 檔案將不起作用。

在遊戲中，確保你已經啟用了「檔案監視器」選項。現在，你只需要在 VS Code 中儲存，遊戲中也會同步修改。

做完這些，現在你可以在專業的程式碼編輯器中編寫你的程式碼了！

---

[第一個程式](docs/first_program.md)      [載入備份](docs/backup.md)
