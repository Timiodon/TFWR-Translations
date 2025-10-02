# 外部编辑器
游戏内置的文本编辑器通常足以用来玩这款游戏，但它当然比不上像 Visual Studio Code 这样更复杂的文本编辑器。

游戏将所有代码文件保存为 .py 文件，以便用 Python 编辑器来进行编辑。
请注意，这只是为了方便。游戏内的语言实际上并非 Python，只是足够相近，因而可正常使用 Python 的智能提示（IntelliSense）。
你可以在[存档文件夹](persistent_data_path/Saves)中找到这些文件。

每个存档中还有一个 `__builtins__.py` 文件，其中包含与游戏的内置函数匹配的 Python 内置定义，以启用 IntelliSense。
VS Code 能够自动检测 `__builtins__.py`，但有些编辑器可能需要先执行 `from __builtins__ import *` 才能工作。

若要在无需重新加载存档的情况下，于游戏内看到外部更改，则必须启用“文件监视器”选项。如果在外部创建或删除文件，则仍需重新加载存档才能查看。

## 使用 VS Code
Visual Studio Code 是《编程农场》推荐使用的代码编辑器。

你可以[点击此处](https://code.visualstudio.com/download)下载。

下载后，在 VS Code 中安装 Python 扩展。

完成后，在 VS Code 中打开存放你的 `.py` 文件的[文件夹](persistent_data_path/Saves)。请务必打开整个文件夹，而不仅仅是单个文件，否则 `__builtins__.py` 文件将不起作用。

在游戏中，确保你已经启用了“文件监视器”选项。现在，每次你在 VS Code 中保存时，更改都会自动显示在游戏中。

就是这样！现在你可以在专业的代码编辑器中编写你的代码了！