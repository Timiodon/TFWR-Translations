# 外部编辑器
游戏内置的文本编辑器通常足够用于玩这个游戏，但当然无法与更复杂的文本编辑器如 Visual Studio Code 相媲美。

游戏会将所有代码文件保存为 .py 文件，所以你可以用 Python 编辑器编辑它们。请注意，这只是为了方便。游戏内的语言其实不是 Python，但它足够接近，以至于 Python IntelliSense 在它上面能够正常工作。你可以在 [保存文件夹](persistent_data_path/Saves) 找到这些文件。

每个存档还包含一个 `__builtins__.py` 文件，它包含与游戏内置函数匹配的 Python 内置定义，以启用 IntelliSense。VS Code 能够自动检测 `__builtins__.py`，但某些编辑器可能需要你执行 `from __builtins__ import *` 才能工作。

要在游戏中看到外部的更改而无需重新加载存档，你必须启用“File Watcher”选项。如果你在外部创建或删除文件，仍然需要重新加载存档才能查看它们。

## 使用 VS Code
Visual Studio Code 是推荐配合 The Farmer Was Replaced 使用的代码编辑器。

你可以在 [这里](https://code.visualstudio.com/download) 安装它。

下载后，在 VS Code 中安装 Python 插件。

安装完成后，在 VS Code 中打开保存 `.py` 文件的 [文件夹](persistent_data_path/Saves)。确保你是打开整个文件夹，而不是单独的文件，否则 `__builtins__.py` 文件将无法正常工作。

在游戏中，确保你已开启“File Watcher”选项。现在，每次你在 VS Code 中保存时，更改将自动显示在游戏中。

就是这样！现在你可以在专业的代码编辑器中编写你的代码了！