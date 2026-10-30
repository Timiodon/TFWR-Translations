[<- Değişkenler](docs/scripting/variables.md) <right>[Dictionary'ler ->](docs/scripting/dicts.md)
---
# Listeler
Listeler, birden fazla değeri tek bir değişkende saklamanın kolay bir yoludur.
Yeni listeleri şöyle oluşturabilirsin:

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
some_list = [2, True, Items.Hay]
print(some_list)
}}

Liste artık `2`, `True` ve `Items.Hay` değerlerini içeriyor.
Bir liste boş da olabilir:

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
empty_list = []
print(empty_list)
}}

Bir listenin öğesine, o öğenin indeksiyle erişebilirsin. İndeks ilk öğe için `0`, ikinci öğe için `1`, üçüncü öğe için `2` olur ve böyle devam eder.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
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
till()
#CODE
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])
}}

Bir listedeki öğeleri `for` döngüsüyle tek tek dolaşabilirsin. Aşağıdaki örnek, listedeki tüm öğeleri toplar.

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
numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
print(sum)
}}

Aşağıdaki liste metotları öğe eklemeni ve kaldırmanı sağlar:

`elements.append(elem)` listenin sonuna bir öğe ekler:

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
numbers = [2, 6, 12]
numbers.append(7)
print(numbers)
}}

`elements.remove(elem)` bir öğenin listede ilk geçtiği yeri kaldırır:

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
numbers = [1, 2, 4, 2]
numbers.remove(2)
print(numbers)
}}

`elements.insert(index, elem)` verilen indekse bir öğe ekler:

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
some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
print(some_list)
}}

`elements.pop(index)` belirtilen indeksteki öğeyi kaldırır.
Hiç indeks belirtilmezse son öğe kaldırılır.

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
numbers = [3, 5, 8, 25]
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
}}

`len()` fonksiyonu listenin uzunluğunu döndürür.
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
numbers = [3, 5, 8, 25]
print(len(numbers))
}}

Listeler referans semantiğine sahiptir. Yani bir listeyi bir değişkene atadığında listenin bir kopyası oluşturulmaz; aynı liste nesnesi o değişkene atanır.
İki değişken aynı listeyi gösteriyorsa, listede yapılan değişiklikleri ikisi de görür.

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
a = [1, 2]
b = a
b.pop()
print(a)
print(b)
}}

---

[Değişkenler](docs/scripting/variables.md)      [For Döngüsü](docs/scripting/for.md)      [Tuple'lar](docs/scripting/tuples.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Set'ler](docs/scripting/sets.md)

[len()](functions/len)
