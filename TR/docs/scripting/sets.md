[<- Dictionary'ler](docs/scripting/dicts.md)
---
# Set'ler
Set'ler (kümeler) [dictionary'ler](docs/scripting/dicts.md) gibidir, ama değerleri yoktur. Yalnızca anahtarlardan oluşan sırasız bir kümedir.

Dictionary'ler gibi oluşturulurlar, ama değerler olmadan.
`set = {North, East, West}`

Boş bir set oluşturmak için `set()` kullan. `{}` ifadesinin boş bir dictionary oluşturduğunu unutma.

Set'e yeni bir öğe eklemek için `set.add(elem)` kullan.

Set'ten bir öğe çıkarmak için `set.remove(elem)` kullan.

Set'in bir öğeyi içerip içermediğini kontrol etmek için `if elem in set:` kullan.

Set'teki tüm öğeleri tek tek dolaşmak için `for elem in set:` kullan.
Büyük set'lerde `in` operatörü, bir listede olduğundan çok daha hızlı çalışır.

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
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North is in set")
else:
    print("North is not in set")
for element in my_set:
    print(element)
}}

Tıpkı dictionary'ler gibi set'ler de sırasızdır, yani öğelerin hangi sırayla dolaşılacağının hiçbir garantisi yoktur.

Ayrıca set'teki öğeler benzersizdir; bu yüzden set'te zaten bulunan bir öğeyi eklemek set'i değiştirmez.

---

[Dictionary'ler](docs/scripting/dicts.md)      [Listeler](docs/scripting/lists.md)      [For Döngüsü](docs/scripting/for.md)

[len()](functions/len)
