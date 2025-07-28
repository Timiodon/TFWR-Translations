# 调试
有时你的代码就是不工作，你需要找出原因。有几种工具可以帮助你做到这一点。

第一种是逐行执行程序。
你可以通过执行按钮旁边的按钮或设置一个 breakpoint 进入逐行执行模式。

可以通过点击代码左侧的 breakpoint 面板来添加 breakpoint。
![](Breakpoints227)
当执行到达 breakpoint 所在行时，它会自动切换到逐行执行模式。

当你将鼠标移到一个变量上时，会显示它的当前值。

`print()` 函数也非常有用。它会将传递给它的任何值直接写到空中。

示例：

打印 “0.24”。
`print(0.24)`

打印 “True” 或 “False”。
`print(can_harvest())`

打印当前位置。
`print(get_pos_x(), get_pos_y())`

print 函数将值直接打印到空中和[输出](docs/output.md)页面。

如果你想打印大量的值，在空中书写有时可能会有点慢。
在这种情况下，你可以使用 `quick_print()` 函数，它只打印到输出窗口。

输出窗口还会记录警告和 error，所以如果有什么东西不像预期那样工作，检查一下会很有用。

当执行停止时，输出也会被写入游戏文件夹中的 output.txt 文件。[output.txt](persistent_data_path/output.txt)。