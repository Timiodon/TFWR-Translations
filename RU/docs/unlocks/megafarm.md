# Мега Ферма
Это невероятно мощное улучшение значительно увеличивает размер фермы и дает вам доступ к нескольким дронам.

Чтобы всё было проще, вы всегда получаете ровно 36 новых ячеек для каждого нового дрона. Соотношение дронов к ячейкам остается постоянным.

## Несколько Дронов
Как и раньше, вы начинаете только с одного дрона. Дополнительные дроны сначала нужно создать, и они исчезнут после завершения программы.
Каждый дрон запускает свою собственную отдельную программу. Дроны могут создавать новых дронов с помощью
`new_drone_id = spawn_drone("filename")`

Это создаёт нового дрона в той же позиции, где находился дрон, выполнивший команду `spawn_drone("filename")`. Новый дрон начнет выполнять программу из файла с именем `filename`, поэтому замените `"filename"` на имя файла, который вы хотите запустить.

Вы можете думать об этом как о ситуации, в которой вы говорите своему дрону перейти в файл с именем `filename` и нажать кнопку выполнения для следующего дрона.

Дроны не сталкиваются друг с другом.

Используйте `max_drones()`, чтобы узнать максимальное количество дронов, которых можно создать.
Используйте `num_drones()`, чтобы узнать количество дронов на ферме.
Используйте `get_drone_id()`, чтобы узнать, какой дрон выполняет код.

Пример:

В файле с именем `farming routine`:
`if get_drone_id() == 0:
    # Только первый дрон будет выполнять это
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Это заставит ваш первый дрон двигаться горизонтально и создавать больше дронов. Созданные дроны будут затем двигаться вертикально и собирать всё на своем пути.

<spoiler=показать подсказку>Самый простой способ использовать несколько дронов — это разделить вашу ферму между ними. Улучшения разработаны так, чтобы каждый дрон всегда имел поле 6x6.
</spoiler>

### Всё, что ниже, довольно продвинуто и не требуется для базового фермерства

## Гонки Состояний
Несколько дронов могут взаимодействовать с одной и той же ячейкой фермы одновременно. Если два дрона взаимодействуют с одной ячейкой в один и тот же тик, действие дрона с меньшим ID будет выполнено первым.

Например, предположим, что дроны `0` и `1` находятся на одном и том же дереве, которое почти полностью выросло.
Дрон `0` вызывает
`use_item(Items.Fertilizer)`
Дрон `1` вызывает
`harvest()`

Если эти действия происходят одновременно, дерево сначала будет удобрено, а затем собрано. В этом случае вы получите древесину. Однако, если дрон `1` немного быстрее, дерево будет собрано до того, как оно будет удобрено, и вы не получите древесину.
Это называется "гонкой состояний". Это распространенная проблема в параллельном программировании, когда результат зависит от порядка выполнения операций.

Вот ещё одна проблематичная ситуация, которая может произойти, когда несколько дронов одновременно выполняют один и тот же код в одной и той же позиции.
`if get_water() < 0.5:
    use_item(Items.Water)`

Если несколько дронов выполняют это одновременно, все они выполнят первую строку, что приведет их в блок `if`. Затем все они используют воду, тратя её впустую.
К тому времени, когда дрон достигнет второй строки, `get_water()` может уже не быть меньше `0.5`, потому что другой дрон полил ячейку за это время.

## Коммуникация Дронов
Если вы интересуетесь более продвинутыми стратегиями, возможно, вы захотите, чтобы ваши дроны обменивались сообщениями друг с другом с помощью функций передачи сообщений.

Отправка любого значения другому дрону:
`send(data, receiver_drone_id)`

Получение следующего значения, отправленного любым дроном:
`data = receive()`

Получение следующего значения, отправленного конкретным дроном:
`data = receive(sender_drone_id)`

Время выполнения `send()` зависит от размера отправляемых данных. Например, отправка большого dictionary требует копирования, что может занять некоторое время.

`receive()` не ожидает прибытия сообщения. Если сообщение ещё не отправлено, оно вернет `None`.

Вы можете создать функцию, ожидающую сообщение, так:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Одним из полезных приложений передачи сообщений является функция, которая создает дрона и отправляет ему функцию для выполнения.
В файле с именем `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Отправка функций таким образом может быть очень медленной, потому что всё состояние функции, включая все глобальные переменные, должно быть скопировано.