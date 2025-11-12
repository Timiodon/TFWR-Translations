@error_missing_default_parameter = 所有默认参数必须放在参数列表的末尾。
@error_invalid_name = {0} 非有效名称。名称必须以字母开头，只能包含字母、数字和下划线，且不属于保留关键字。
@error_reserved_keyword = {0} 属于保留关键字，不能用作名称。
@error_invalid_assign_expr = 不能给该表达式赋值。
@error_no_statements = 一个代码块必须至少包含一条语句。
语句可以是函数调用，如 `harvest()`，也可以是变量赋值。
如果想在代码块中什么都不做，请使用 `pass` 语句。
@error_not_enough_indentation = 这里的缩进不够。
在 `:` 之后必须有比之前更多的缩进，以分隔新的代码块。
使用 Tab 键来缩进代码。
@error_too_much_indentation = 这里的缩进过多。
一个代码块内所有语句的缩进必须相同。
@error_not_a_statement = 这不是一个有效的语句。
@error_not_a_statement2 = 这不是一个有效的语句。你是想写 {0} 吗？
@error_invalid_expression = 这不是一个有效的表达式。
@error_new_line_expected = 这里应该另起新行。
@error_unexpected_token = 这里应该插入 {0}。
@error_missing_colon = 每个代码块的开头都必须有一个冒号 `:`。
@error_unexpected_assign = 这里不能进行赋值。要检查是否相等，请改用 `==`。
@error_invalid_for_syntax = 这不是一个有效的 for 循环。for 循环的示例如下：
`for n in range(3):`
`for` 后面始终跟着循环变量、一个 `in` 和一个序列。在这个例子中，`n` 是变量名，但可以替换为任何其他名称。
@error_unknown_method = 这个方法不存在。
@error_bad_backslash = 反斜杠可以用来将表达式拆分到多行，但需要在后面添加新行。
@error_mixed_indentation = 制表符和空格不应混合使用。
@error_expected_close_token = 应为逗号或右括号。
@error_wrong_dict_literal = 应用 `:` 来分隔字典的键和值。
@error_assign_before_global = {0} 在全局声明之前被赋值。
@error_wildcard_imports_not_allowed_in_function = 形如 `from x import *` 的导入不允许在函数内部使用。
@error_invalid_import = 不能导入文件名不是有效标识符的文件。有效标识符只能包含字母、数字和下划线。如果文件名包含其他字符，则必须重命名。
@error_invalid_number_format = 这个数字格式无效。
@error_compared_item_with_number = {0} 不是一个数字，它是一个物品。将它与数字进行比较是没有意义的。

如果你想检查你拥有的该物品数量，请改用 `num_items(`{0}`)`。
@error_compared_entity_with_number = {0} 不是一个数字，它是一个实体。将它与数字进行比较是没有意义的。
@error_compared_unlock_with_number = {0} 不是一个数字，它是一个解锁项。将它与数字进行比较是没有意义的。

如果你想检查你解锁了它多少次，请改用 `num_unlocked(`{0}`)`。
@error_nonsensical_or = 在条件中使用 `or `{0} 是没有意义的，因为 {0} 是一个常量。
请注意，比较运算符的求值优先于 `or`。

示例：
`x == 5 or 6` 
等同于 
`(x == 5) or 6`
非零数字被视为 true，所以这等同于 
`(x == 5) or True`
这个表达式的结果永远是 true。

理论上这是有效的 Python 代码，但没有任何理由要这样写。
@error_item_condition = {0} 是一个物品，而不是布尔值。单独将它用作条件是没有意义的。
也许你是想检查某个值是否等于该物品？
`some_variable == `{0}
@error_unlock_condition = {0} 是一个解锁项，而不是布尔值。单独将它用作条件是没有意义的。
你可以这样检查该解锁项是否已解锁：
`num_unlocked(`{0}`) > 0`
@error_entity_condition = {0} 是一个实体，而不是布尔值。单独将它用作条件是没有意义的。
你可以这样检查无人机下方实体的类型：
`get_entity_type() == `{0}
@error_ground_condition = {0} 是一种地块类型，而不是布尔值。单独将它用作条件是没有意义的。
你可以这样检查无人机下方地块的类型：
`get_ground_type() == `{0}