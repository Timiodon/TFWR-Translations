[<- Górnictwo](docs/unlocks/mining.md) <right>[Bambus ->](docs/unlocks/bamboo.md)
<right>[Skamieniałe dynie ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlit i gleba próchnicza ->](docs/unlocks/special_soils.md)
---
# Ryż
Pod powierzchnią i warstwą `Grounds.Dirt` znajdziesz cienką warstwę `Grounds.Clay`. Okazuje się, że to żyzne, nasiąknięte wodą podłoże idealnie nadaje się do sadzenia ryżu.

Poniższy kod może pomóc ci kopać w dół, aż znajdziesz glinę, a następnie posadzić ryż:
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
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

Gdy dron jest nad blokiem `Grounds.Clay`, użyj `plant(Entities.Rice)`, aby posadzić ryż, `can_harvest()`, aby sprawdzić dojrzałość, a następnie `harvest()`, aby go zebrać.

## Tarasy
Po zasadzeniu ryżu podłoże zmienia się w `Grounds.Rice_Terrace`, zapewniając idealne warunki dojrzewania. Gdy ryż dojrzeje, podłoże wysycha i zmienia się w `Grounds.Dry_Rice_Terrace`, na którym nie można sadzić kolejnego ryżu. Na szczęście warstwa ma kilka bloków grubości: usuń blok przez `dig()` i posadź ryż na `Grounds.Clay` poniżej. Gdy warstwa się skończy, zawsze możesz odtworzyć świat przez `clear()` i dokopać się do nowej.

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Pętla for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
