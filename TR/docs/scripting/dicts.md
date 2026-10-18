[<- Listeler](docs/scripting/lists.md) <right>[Maliyetler ->](docs/unlocks/costs.md)
---
# Dictionary'ler
Dictionary (sözlük), anahtarları değerlerle eşleyen bir veri yapısıdır; tıpkı gerçek bir sözlüğün kelimeleri anlamlarıyla eşlemesi gibi. Bu değerleri çok hızlı bir şekilde bulmanı sağlar.

Bir dictionary şöyle oluşturulur:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

İki nokta üst üsteden önceki ifade anahtardır, sonraki ifade ise anahtarın eşlendiği değerdir.
Yukarıdaki dictionary, her yönü o yönün sağındaki yöne eşler.

İşte dronun konumunu, altındaki varlıkla eşleyen başka bir dictionary:
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Bir anahtara eşlenmiş değere erişmek, bir listedeki öğeye erişmeye benzer:
`value = dict[key]`

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Bir dictionary'ye yeni bir anahtar-değer çiftini şöyle ekleyebilirsin:
`dict[key] = value`

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
    "world_size": {"x": 3, "y": 1},
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
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Anahtarlar benzersizdir; bu yüzden dictionary'de zaten bulunan bir anahtarı eklersen önceki değerin üzerine yazılır.

`dict` içinden bir anahtar-değer çiftini kaldırmak için `dict.pop(key)` kullan.

`key in dict`, eğer `key` değeri `dict` içinde bir anahtarsa `True`, değilse `False` sonucunu verir.
Yani `dict` içinde bir anahtarın olup olmadığını kontrol etmek için `if key in dict:` kullanabilirsin.

Bir dictionary'yi `for` döngüsüne koyarsan tüm anahtarlarını tek tek dolaşabilirsin:
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Anahtarların hangi sırayla dolaşılacağı konusunda hiçbir garanti yoktur.

Ayrıca bkz. [Set'ler](docs/scripting/sets.md)

---

[Listeler](docs/scripting/lists.md)      [Set'ler](docs/scripting/sets.md)      [Tuple'lar](docs/scripting/tuples.md)      [Maliyetler](docs/unlocks/costs.md)

[len()](functions/len)
