# Цикл For
Цикл `for` працює так само, як у Python. (У деяких мовах його називають циклом foreach, не плутайте його з циклом for у стилі C, який працює інакше).

`for i in sequence:
	#зробити щось із i`

Подібно до циклу `while`, цикл `for` також багаторазово викликає блок коду. Замість того, щоб виконувати цикл на основі умови, він виконує тіло циклу один раз для кожного елемента в послідовності.

## Синтаксис
Цикл for виглядає так:

`for variable_name in sequence:
	#блок коду`

`variable_name` може бути будь-яким ім'ям, яке ви оберете. Це змінна, яка зберігає поточний елемент у послідовності. `sequence` має бути певним значенням, яке можна ітерувати, наприклад, діапазоном чисел. Блок коду виконується для кожного елемента, при цьому змінній циклу присвоюється цей елемент.

## Послідовності
[Діапазони (Ranges)](functions/range)      <unlock=lists>[Списки (Lists)](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежі (Tuples)](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Словники (Dictionaries)](docs/scripting/dicts.md)      </unlock><unlock=sets>[Множини (Sets)](docs/scripting/sets.md)</unlock>

## Приклад
`for i in range(5):
	harvest()`

Цей цикл виконує тіло фіксовану кількість разів. Це по суті те саме, що написати:

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

Отже, він викликає `harvest()` 5 разів.

Дивіться також [Break](docs/scripting/break.md) та [Continue](docs/scripting/continue.md)