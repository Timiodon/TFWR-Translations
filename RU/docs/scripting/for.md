# Цикл For
Цикл `for` работает как в Python. (В некоторых языках называется циклом foreach, не путать с циклом for в стиле C, это другое).

`for i in sequence:
	#сделать что-то с i`

Подобно циклу `while`, цикл `for` также многократно вызывает блок кода. Вместо того, чтобы циклически выполняться на основе условия, он выполняет тело цикла один раз для каждого элемента в последовательности.

## Синтаксис
Цикл for выглядит так:

`for variable_name in sequence:
	#блок кода`

`variable_name` может быть любым именем, которое вы выберете. Это переменная, которая хранит текущий элемент в последовательности. `sequence` должно быть некоторым значением, которое можно перебирать, например, диапазон или числа. Блок кода выполняется для каждого элемента, при этом переменная цикла присваивается этому элементу.

## Последовательности
[Диапазоны](functions/range)      <unlock=lists>[Списки](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежи](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Словари](docs/scripting/dicts.md)      </unlock><unlock=sets>[Множества](docs/scripting/sets.md)</unlock>

## Пример
`for i in range(5):
    harvest()`

Этот цикл выполняет тело определённое количество раз. Это по сути то же самое, что написать

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

См. также [Break](docs/scripting/break.md) и [Continue](docs/scripting/continue.md)