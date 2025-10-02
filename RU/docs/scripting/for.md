# Цикл `for`
Цикл `for` работает в игре, как и в Python. (В некоторых языках называется он foreach. Не путать с циклом for в языке C, это другое).

`for i in sequence:
	#сделать что-то с i`

Подобно циклу `while`, `for` также многократно вызывает блок кода. Но вместо того, чтобы циклически выполнять его на основе условия, он выполняет тело цикла один раз для каждого элемента в последовательности.

## Синтаксис
Цикл for выглядит так:

`for variable_name in sequence:
	#блок кода`

Для `variable_name` можно задать любое имя. Это переменная, которая хранит текущий элемент в последовательности. `sequence` должно быть некоторым значением, которое можно перебирать, например, диапазоном или числами. Блок кода выполняется для каждого элемента, при этом переменная цикла присваивается этому элементу.

## Последовательности
[Диапазоны](functions/range)      <unlock=lists>[Списки](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежи](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Словари](docs/scripting/dicts.md)      </unlock><unlock=sets>[Множества](docs/scripting/sets.md)</unlock>

## Пример
`for i in range(5):
    harvest()`

Этот цикл выполняет тело определенное количество раз. По сути, это равносильно следующему:

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

Таким образом, цикл вызывает `harvest()` 5 раз.

См. также [Break](docs/scripting/break.md) и [Continue](docs/scripting/continue.md).