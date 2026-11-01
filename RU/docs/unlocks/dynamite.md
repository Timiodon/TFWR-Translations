[<- Грибы](docs/unlocks/mushroom.md) <right>[Взрывной бур ->](docs/unlocks/explosive_drill.md)
---
# Динамит
Революционная взрывчатка, оставленная предыдущими шахтерскими экспедициями. К сожалению, твой бур идеально подходит для подрыва динамита, уничтожающего все блоки вокруг. Собранный динамит можно применить командой `use_item(Items.Dynamite)`: он взорвется прямо под дроном.

Чтобы безопасно добывать динамит, найди двойной слой, состоящий из материалов `Grounds.Dynamite` и `Grounds.Soot`. Верхняя динамитная земля состарилась, поэтому некоторые ее блоки можно безопасно копать. Но часть зарядов все еще активна и взорвется при раскопке.

Этот пример копает динамит и блоки вокруг первого раскопа, открывает слой сажи с числами и выводит измерение:
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# Копай через динамит до слоя сажи
while get_ground_type() != Grounds.Soot:
    dig()

# Список направлений для движения дрона по кругу
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # Число на блоке сажи
}}

## Динамитный сапер
Сможешь ли ты найти и раскопать все блоки-пустышки, оставив только активные заряды? Когда динамитный слой исчезнет, каждый активный блок, окруженный только другими активными блоками или сажей, даст дополнительный динамит.

К счастью, помогут расположенные ниже блоки сажи: они способны опознавать соседние динамитные блоки с активными зарядами. Какие именно блоки активны, они не сообщат — только общее число, поэтому придется сопоставить показания нескольких блоков сажи.

Вызов `measure()` на блоке сажи возвращает количество зарядов в восьми соседних клетках динамитного слоя выше. Значение может быть от `0` (активных зарядов нет) до `8` (активный заряд есть у каждого соседа).

Первый раскопанный блок динамитного слоя всегда оказывается пустышкой. Каждый добытый блок дает немного динамита. Когда слой уничтожается — после успешной добычи всех пустышек или случайного попадания в активный заряд, — ты также получишь количество динамита, равное квадрату числа полностью открытых активных блоков.

## Строение пластов
Чем больше глубина, тем больше активных зарядов окажется в динамитном слое, а также выше сложность их поиска. Общее число мин увеличивается с размером фермы, как и максимальная награда за очистку пласта динамита.

Улучшай динамит, чтобы получать большее его количество при раскопках динамитных блоков и полном открытии активных зарядов. Каждое улучшение также повышает энергию взрыва динамита на 30%.

## Определение успеха и неудачи
Если прокопать активный динамит, оба слоя взорвутся. Проверить это можно, использовав `get_ground_type()` после раскопок `Grounds.Dynamite`. Если земля не `Grounds.Soot`, решить головоломку не удалось. Если же раскопать последний неактивный динамитный блок, все динамитные блоки исчезнут, а ты получишь максимальный урожай за головоломку. Слой сажи останется, но `measure()` вернет `None`, показывая, что головоломка успешно решена.

`# Раскопать динамитный блок и проверить состояние головоломки
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Раскопан активный динамит, головоломка провалена
        return False
    elif measure() == None:
        # Раскопан последний блок-пустышка, головоломка решена
        return True
    else:
        # При измерении получено число, головоломка не завершена
        return None
`

## Стратегия
<spoiler=подсказка>
Код ниже вкапывается в пласт динамита и ищет блоки сажи с измерением `0`. Для каждого из них он выкапывает весь окружающий динамит:
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# Обойди первый выкопанный блок
for dir in circle_directions:
    # Если измерение сажи равно 0,
    # все соседние блоки динамита — безопасные
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # Сделай еще один круг по соседним блокам
        for dir2 in circle_directions:
            move(dir2)
            # Выкопай безопасный блок динамита
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[Статистика](docs/stats.md)      [Подземные датчики](docs/unlocks/underground_senses.md)      [Словари](docs/scripting/dicts.md)      [Множества](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
