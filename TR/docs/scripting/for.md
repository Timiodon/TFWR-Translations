[<- Genişletme 2](docs/unlocks/expand_2.md)
---
# For Döngüsü
`for` döngüsü Python'daki gibi çalışır. Bazı dillerde foreach döngüsü olarak adlandırılır ve farklı çalışan C tarzı for döngüsüyle karıştırılmamalıdır.

`for i in sequence:
	#do something with i`

`while` döngüsüne benzer şekilde `for` döngüsü de bir kod bloğunu tekrar tekrar çalıştırır. Ancak bir koşula bağlı olarak dönmek yerine, döngü gövdesini bir dizideki her öğe için bir kez çalıştırır.

## Söz Dizimi
Bir for döngüsü şöyle görünür:

`for variable_name in sequence:
	#code block`

`variable_name` için istediğin herhangi bir adı seçebilirsin. Bu, dizideki o anki öğeyi tutan bir değişkendir. `sequence` ise üzerinde tek tek dolaşılabilen bir değer olmalıdır, örneğin bir sayı aralığı. Kod bloğu her öğe için bir kez çalıştırılır ve her seferinde döngü değişkenine o öğe atanır.

## Diziler
[Aralıklar](functions/range)      <unlock=lists>[Listeler](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuple'lar](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionary'ler](docs/scripting/dicts.md)      </unlock><unlock=sets>[Set'ler](docs/scripting/sets.md)</unlock>

## Örnek
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

Bu döngü, gövdesini sabit sayıda çalıştırır. Aslında şunu yazmakla temelde aynı şeydir:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[While Döngüsü](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
