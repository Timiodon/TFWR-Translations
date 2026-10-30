[<- Dictionary'ler](docs/scripting/dicts.md) <right>[Otomatik Kilit Açma ->](docs/unlocks/auto_unlock.md)
---
# Maliyetler
Her maliyet, eşyaları sayılarla eşleyen bir dictionary (sözlük) olarak gösterilebilir.

`get_cost()` fonksiyonu böyle bir dictionary döndürür. Bir bitkinin ya da bir kilit açmanın maliyetini döndürür.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Entities.Pumpkin))
}}

Kilit açmalar için, maliyetini öğrenmek istediğin kilit açma seviyesini isteğe bağlı ikinci bir argüman olarak verebilirsin. Varsayılan olarak mevcut kilit açma seviyesi kullanılır.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops, 0))
print(get_cost(Unlocks.Loops, 1))
}}

Zaten en yüksek seviyede olan kilit açmalar için `get_cost()` boş bir dictionary döndürür.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
cost = get_cost(Entities.Carrot)
for item in cost:
	if num_items(item) < cost[item]:
		print("missing", cost[item] - num_items(item), item)
}}

---

[Dictionary'ler](docs/scripting/dicts.md)      [Otomatik Kilit Açma](docs/unlocks/auto_unlock.md)      [Sıralama Tablosu](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
