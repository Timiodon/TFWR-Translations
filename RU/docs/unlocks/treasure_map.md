[<- Железо](docs/unlocks/iron.md)
---
# Карта сокровищ
Легенды рассказывают о неуловимом кладе, спрятанном давно погибшим забывчивым пиратом — или что-то в этом роде. Что, если он отметил путь к кладу на карте, а затем потерял ее? Вдруг карта выпала, когда пирата загнала в угол река лавы, и сохранилась под слоем базальта?

Измерение базальтовых блоков может что-то раскрыть!

<spoiler=Расскажи подробнее>
Ищи слой `Grounds.Basalt`. Попробуй измерить базальт и посмотри, что он сообщит. Подсказка может привести к карте сокровищ, а изучение карты наверняка откроет путь к самому кладу — но сможешь ли ты расшифровать ее указания?
</spoiler>

<spoiler=Просто скажи, как это сделать>
Ладно, вот что нужно сделать: найди слой `Grounds.Basalt` и блок `Grounds.Treasure_Map` прямо под ним. Вызови `measure()` на базальте, чтобы получить координаты `(x, y)` находящегося под ним блока карты.

Вызови `measure()` на блоке карты, чтобы получить путь к сокровищу в виде строки с буквами направлений. N, E, S и W означают соответственно `North`, `East`, `South` и `West`, а D — «вниз» или «копать». Эти буквы описывают путь из блоков `Grounds.Treasure_Path`, ведущий к кладу.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# Найди базальтовый пласт
while get_ground_type() != Grounds.Basalt:
    dig()

# Измерение базальта возвращает координаты карты
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# Карта найдена: измерь ее, чтобы получить путь
do_a_flip()
instructions = measure()
print("указания: ", instructions)

# Выкопай карту, чтобы начать поиск клада
dig()
}}

Цикл `for` позволяет обработать строку буква за буквой:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# Указания карты возвращаются одной строкой
instructions = measure()
# Используй for-in для обработки строки по буквам
for letter in instructions:
    print(letter)
}}

Дрону нужно все время оставаться над блоками `Grounds.Treasure_Path`. Если он собьется с пути, путь разрушится и клад будет потерян.

## Цель
В конце пути находится блок `Grounds.Treasure_Goal`. Если дрон не сходил с пути, над этим блоком появится `Entities.Underground_Treasure`. Дрон может забрать сундук командой `harvest()` и получить золото.

## Награда
Количество золота пропорционально длине пути к сокровищу. Улучшение технологии «Карта сокровищ» увеличивает глубину пути, а улучшение «Расширения» позволяет ему больше сдвигаться в стороны. Оба улучшения увеличивают длину пути и количество найденного золота.

## Несколько дронов
Искать клад должен дрон, раскопавший блок карты. При этом он не должен покидать блоки пути.
</spoiler>

---

[Статистика](docs/stats.md)      [Цикл For](docs/scripting/for.md)      [Кортежи](docs/scripting/tuples.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
