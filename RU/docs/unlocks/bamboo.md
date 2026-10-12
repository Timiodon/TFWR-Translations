[<- Рис](docs/unlocks/rice.md) <right>[Цветные блоки ->](docs/unlocks/debug_place.md)
<right>[Пирамиды ->](docs/unlocks/pyramid.md)
---
# Бамбук

Бамбук — это растение, которое может вырастать до 6 блоков в высоту. Он не растет, пока над ним находится дрон, поэтому обязательно отведи дрон командой `move` после вызова `plant(Entities.Bamboo)`. Для посадки бамбука требуется рис.

Бамбук зацветает, когда достигает определенной случайной высоты. Используй `measure()`, чтобы узнать, на какой высоте он зацветет. Функция `measure()` начинает отсчёт с 0, поэтому, если бамбук зацветет на втором блоке, `measure()` вернет 1:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Ты добьешься максимального урожая бамбука, если вызовешь `harvest()`, когда дрон находится прямо над цветком. За каждый блок разницы урожай будет делиться на восемь.
Например, если цветок находится на высоте 3, а ты соберешь урожай на два блока выше, урожай разделится на 64.

Чтобы собирать цветы, расположенные выше, залетай в бамбук, когда дрон находится на нужной высоте. В этом поможет недавно разблокированная команда `place()`.

Используй `place(Grounds.Dirt)`, чтобы ставить блоки друг на друга рядом с бамбуком и подниматься выше. Затем используй `move()`, чтобы залететь в бамбук сбоку. При вызове `harvest()` дрон должен находиться прямо над цветком.

При использовании `place(Grounds.Dirt)` расходуется 1 блок! Также ты можешь размещать и другие типы земли, такие как `Grounds.Rock`, но не особые блоки, такие как `Grounds.Clay`.

Бамбук растет со скоростью ровно 1 блок в секунду.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # подождать немного
do_a_flip()
move(West)
harvest()
}}

---

[Статистика](docs/stats.md)      [Цикл For](docs/scripting/for.md)      [Переменные](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Функции](docs/scripting/functions.md)      [Рис](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
