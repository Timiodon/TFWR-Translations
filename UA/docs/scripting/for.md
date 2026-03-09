# Цикл for
Цикл `for` працює як в Python. (У деяких мовах його називають foreach-циклом, не плутати з C-подібним for, який є зовсім іншим типом циклу).

`for i in sequence:
	#зробити щось з i`

Подібно до циклу `while`, цикл `for` також багаторазово виконує блок коду. Замість повторення за умовою він виконує тіло циклу один раз для кожного елемента послідовності.

## Синтаксис
Цикл for виглядає так:

`for variable_name in sequence:
	#блок коду`

`variable_name` може бути будь-яким ім'ям, яке ви оберете. Це змінна, яка зберігає поточний елемент послідовності. `sequence` має бути значенням, яке можна перебирати, наприклад, діапазоном чисел. Блок коду виконується для кожного елемента, при цьому змінна циклу отримує значення цього елемента.

## Послідовності
[Діапазони](functions/range)      <unlock=lists>[Списки](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежі](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Словники](docs/scripting/dicts.md)      </unlock><unlock=sets>[Множини](docs/scripting/sets.md)</unlock>

## Приклад
`for i in range(5):
    harvest()`

Цей цикл виконує тіло фіксовану кількість разів. По суті, це те саме, що написати:

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

Тобто `harvest()` буде викликано 5 разів.

Дивіться також [Break](docs/scripting/break.md) і [Continue](docs/scripting/continue.md)