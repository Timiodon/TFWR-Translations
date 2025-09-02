# 外部编辑器
游戏内置的文本编辑器通常足以玩这个游戏，但它当然无法与像 Visual Studio Code 这样更复杂的文本编辑器竞争。

游戏将所有代码文件保存为 .py 文件，所以你可以用 Python 编辑器来编辑它们。
请注意，这只是为了方便。游戏内的语言实际上不是 Python，但它足够接近，以至于 Python 的智能提示（IntelliSense）能很好地工作。
你可以在[存档文件夹](persistent_data_path/Saves)中找到这些文件。

每个存档还包含一个 `__builtins__.py` 文件，其中包含与游戏内内置函数匹配的 Python 内置定义，以启用智能提示。
VS Code 能够自动检测 `__builtins__.py`，但有些编辑器可能只有在你执行 `from __builtins__ import *` 时才能工作。

要在游戏中看到外部更改而无需重新加载存档，你必须启用“文件监视器”选项。如果你在外部创建或删除文件，你仍然需要重新加载存档才能看到它们。

## 使用 VS Code
Visual Studio Code 是与 The Farmer Was Replaced 一起使用的推荐代码编辑器。

你可以在[这里](https://code.visualstudio.com/download)安装它。

下载后，在 VS Code 中安装 Python 扩展。

完成后，在 VS Code 中打开存放你 `.py` 文件的[文件夹](persistent_data_path/Saves)。确保你打开的是整个文件夹，而不仅仅是单个文件，否则 `__builtins__.py` 文件将不起作用。

在游戏中，确保你已经打开了“文件监视器”选项。现在，每次你在 VS Code 中保存时，更改都会自动显示在游戏中。

就是这样！现在你可以在专业的代码编辑器中编写你的代码了！