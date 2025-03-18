# Цикл For
Цикл `for` работает как в Python. (В некоторых языках называется foreach-цикл, не путать с for-циклом в стиле C, который отличается).

`for i in sequence:
	#do something with i`

Подобно циклу `while`, цикл `for` также многократно вызывает блок кода. Вместо цикла, основанного на условии, он выполняет тело цикла один раз для каждого элемента в последовательности.

## Синтаксис
Цикл for выглядит так:

`for variable_name in sequence:
	#code block`

`variable_name` может быть любым названием, которое вы выберете. Это переменная, которая хранит текущий элемент в последовательности. `sequence` должна быть значением, по которому можно пройти, например, диапазон или числа. Код выполняется для каждого элемента, при этом переменной цикла присваивается этот элемент.

## Последовательности
[Ranges](functions/range)      <unlock=lists>[Списки](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежи](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Пример
`for i in range(5):
    harvest()`

Этот цикл выполняет тело фиксированное количество раз. По сути, это то же самое, что и написание

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Таким образом, он вызывает `harvest()` 5 раз.

Смотрите также [Break](docs/scripting/break.md) и [Continue](docs/scripting/continue.md)