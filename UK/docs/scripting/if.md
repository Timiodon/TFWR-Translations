# If (Умова)
Ви можете використовувати `if`, `elif` та `else`, щоб виконувати код за певних умов.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Синтаксис
`if` дозволяє запускати код лише у тому випадку, якщо певна умова `True` (є істинною). Вони схожі на цикл `while`, але не повторюється, а виконується одноразово.
`if` приймає умову, так само як і цикл `while`, і виконує блок коду, якщо умова оцінюється як `True`:

`#зробити сальто, якщо умова True
if condition:
	do_a_flip()`

Ви також можете додати `else` після `if`, щоб визначити код, який буде виконано, якщо умова оцінюється як `False` (хибна).

Зробити сальто, якщо `condition` є True, інакше — зібрати врожай.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` — це скорочення від «else if».

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

можна скоротити до:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
