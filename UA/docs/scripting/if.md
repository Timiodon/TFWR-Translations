# If
Ви можете використовувати if, elif та else , щоб виконувати код за умовою:

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Синтаксис
`if` дозволяє виконувати код лише тоді, коли умова дорівнює `True`. Він схожий на цикл `while`, який не повторюється.
`if` приймає умову, так само, як і `while`, та виконує блок коду, якщо умова обчислюється як `True`:

`#зробити переворот, якщо умова є True
if condition:
	do_a_flip()`

Ви також можете додати `else`, який визначає код, що виконується, якщо умова дорівнює `False`.

Зробити переворот, якщо `condition` дорівнює True, інакше — зібрати врожай:

`if condition:
	do_a_flip()
else:
	harvest()`

`elif` — це скорочення від else if.

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
