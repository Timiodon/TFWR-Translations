[<- Carottes](docs/unlocks/carrots.md) <right>[Engrais ->](docs/unlocks/fertilizer.md)
<right>[Tournesols ->](docs/unlocks/sunflowers.md)
---
# Arrosage
Les plantes poussent plus vite lorsqu'elles sont arrosées. Le sol a un niveau d'eau allant de `0` à `1`.
La fonction `get_water()` renvoie le niveau d'eau du sol sur lequel il se trouve.

La vitesse de croissance d'une plante évolue linéairement de 1x à un niveau d'eau de 0 à 5x à un niveau d'eau de 1.

Le sol s'assèche avec le temps : en moyenne, il perd 1% de son eau actuelle par seconde, mais il y a une certaine variance aléatoire. Maintenir un niveau d'eau élevé consommera beaucoup plus d'eau que de maintenir un niveau d'eau bas.

Tu peux utiliser de l'eau sur tes plantes. Un réservoir d'eau est automatiquement ajouté à ton inventaire toutes les 10 secondes.
Améliorer `Unlocks.Watering` doublera la quantité d'eau que tu obtiens toutes les 10 secondes.

Un réservoir contient `0.25` d'eau.

Appelle `use_item(Items.Water)` sur n'importe quel sol pour l'arroser.
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
    move(East)
    move(East)
}}

---

[Engrais](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
