[<- Удобрение](docs/unlocks/fertilizer.md) <right>[Мегаферма ->](docs/unlocks/megafarm.md)
---
# Лабиринты
`Items.Weird_Substance` странно действует на кусты. Если дрон находится над кустом и вызвать `use_item(Items.Weird_Substance, amount)`, куст превратится в лабиринт из живой изгороди.
Размер лабиринта зависит от количества использованного `Items.Weird_Substance` (второго аргумента вызова `use_item()`).
Без улучшений лабиринта использование `n` единиц `Items.Weird_Substance` создаст лабиринт размером `n`x`n`. Каждый уровень улучшения удваивает сокровище, но также удваивает необходимое количество `Items.Weird_Substance`.
Чтобы создать лабиринт размером со все поле:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


По какой-то причине дрон не может летать над изгородями, хотя они кажутся не такими уж высокими.

Где-то в лабиринте спрятан клад. Примени `harvest()` к кладу, чтобы получить золото в количестве, равном площади лабиринта. Например, лабиринт 5х5 принесет 25 золота.

Если ты используешь `harvest()` в любом другом месте, лабиринт пропадет.

`get_entity_type()` равно `Entities.Treasure`, если дрон находится над кладом, и `Entities.Hedge` — во всех остальных местах лабиринта.

Лабиринты не содержат циклов, если только ты не используешь лабиринт повторно (см. ниже, как это сделать). Следовательно, у дрона нет способа оказаться в той же позиции снова, не возвращаясь назад.

Чтобы проверить, есть ли на пути стена, можешь попытаться через нее переместиться.
`move()` возвращает `True`, если попытка удачная, в противном случае — `False`.

`can_move()` можно использовать для проверки наличия стены, не совершая движения.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Если ты не понимаешь, как добраться до клада, посмотри подсказку 1. Она объясняет, как подходить к решению такой задачи.

Использование `measure()` в любом месте лабиринта возвращает позицию клада.
`x, y = measure()`

Если хочешь усложнить задачу, можешь повторно использовать лабиринт, снова применив к кладу то же количество `Items.Weird_Substance`. 
Это действие соберет клад и создаст новый в случайном месте лабиринта.

Каждый раз, когда клад перемещается, некоторые стены лабиринта могут быть случайным образом удалены. Так что повторно используемые лабиринты могут содержать циклы.

Обрати внимание, что циклы делают лабиринт намного сложнее: ты можешь попадать в уже пройденное место, не возвращаясь назад.
Повторное использование лабиринта не дает больше золота, чем простой сбор в созданном заново лабиринте.
Это задачка со звездочкой, которую ты легко можешь пропустить.
Решай ее, только если знаешь дополнительную информацию и короткие пути, которые помогут пройти лабиринт быстрее.

Клад можно перемещать до 300 раз. После этого применение странного вещества к кладу больше не будет давать золото или перемещать клад.

<spoiler=показать подсказку 1>
Вот общий подход к решению задачи:

Создай лабиринт и представь, что ты дрон.

Подумай, как можно искать клад, если ты в лабиринте.

Опиши стратегию шаг за шагом, чтобы кто-то другой мог воспроизвести ее без раздумий.

Теперь попробуй перевести свои шаги в код.
</spoiler>
<spoiler=показать подсказку 2>
Пока в лабиринте нет циклов, все стены образуют одну большую связную стену. Если держаться левой рукой за стену и следовать вдоль нее, она проведет через весь лабиринт.
Для этого подхода нужно совсем немного кода и не требуется запоминать посещенные места. Достаточно примерно 10 строк.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=показать подсказку 3>
Вместо движения в абсолютных направлениях вроде востока и запада бывает удобно использовать относительные направления вроде «повернуть направо» и «повернуть налево». Для этого нужно отслеживать текущее направление движения дрона. Сам дрон не поворачивается, но в коде можно поддерживать «виртуальный» поворот.
Здесь пригодится следующий прием с индексами:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#повернуть направо
index = (index + 1) % 4
move(directions[index])

#повернуть налево
index = (index - 1) % 4
move(directions[index])
}}


`% 4` позволяет вращаться «по кругу»: `3 (West) + 1` снова дает `0 (North)`, потому что `4 % 4 == 0`, а `-1 % 4 == 3`.</spoiler>
<spoiler=показать подсказку 4>
Если решить задачу не получается, можно упростить ее, выбрав менее эффективный подход.
Лабиринт размером `1`x`1` решается элементарно.</spoiler>

---

[Статистика](docs/stats.md)      [Списки](docs/scripting/lists.md)      [Словари](docs/scripting/dicts.md)      [Кортежи](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
