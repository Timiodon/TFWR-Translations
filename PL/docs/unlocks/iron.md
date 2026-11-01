[<- Węgiel](docs/unlocks/coal.md) <right>[Kwarc ->](docs/unlocks/quartz.md)
<right>[Poszukiwanie żelaza ->](docs/unlocks/prospecting.md)
<right>[Mapa skarbu ->](docs/unlocks/treasure_map.md)
---
# Żelazo
Po znalezieniu węgla w `Grounds.Dirt` kop dalej przez warstwę `Grounds.Clay` do `Grounds.Rock`, aby znaleźć żelazo.

W przeciwieństwie do węgla żyły żelaza rozciągają się także pionowo. Wszystkie bloki żelaza w żyle zawsze stykają się bezpośrednio; nigdy nie łączą się tylko po skosie.

Żyły żelaza są początkowo małe, a ich znalezienie wymaga odrobiny szczęścia. Dalsze ulepszanie żelaza zwiększa maksymalny rozmiar żył i ułatwia przypadkowe trafienie na nie. Aby znajdować je niezawodnie, odblokuj [poszukiwanie rud](docs/unlocks/prospecting.md).

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# Kop, aż pojawi się blok żelaza
while get_ground_type() != Grounds.Iron:
    dig()

# Wydobądź żelazo
dig()
}}

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Poszukiwanie żelaza](docs/unlocks/prospecting.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
