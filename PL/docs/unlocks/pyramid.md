[<- Bambus](docs/unlocks/bamboo.md)
---
# Piramidy

Pod ziemią znajdują się teraz starożytne piramidy, z których można pozyskiwać energię!

Piramidy są zbudowane z bloków piasku (`Grounds.Sand`). Pod samą piramidą znajduje się fundament z wapienia (`Grounds.Limestone`). Są stare i zerodowane, dlatego znajdziesz je tylko w częściowo zniszczonym stanie. Warstwa fundamentu jest zawsze kompletna, ale w piasku będą dziury. Tak wygląda odkopana piramida:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

Bloki nad piramidą są zawsze ziemią. Możesz wykorzystać ten fakt, aby odkopać piramidę wydajniej niż w powyższym kodzie.

Jak widać, w piasku znajduje się kilka dziur, które trzeba wypełnić. Gdy uzupełnisz braki i przywrócisz piramidę do pierwotnego stanu, konstrukcja rozpadnie się, a ty otrzymasz energię w nagrodę.

Piramidę można odnowić, umieszczając bloki poleceniem `place(Grounds.Sand)`. Piasek to specjalny blok, który natychmiast się zawali, jeśli nie ma odpowiedniego podparcia. Każdy blok piasku musi leżeć bezpośrednio na wapieniu albo na powierzchni 3x3 z bloków piasku. Oto mała ręcznie zbudowana piramida pokazowa. Oczywiście samodzielne zbudowanie jej nie daje energii:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

move(North)
move(East)
place(Grounds.Sand)
}}

Prawidłowo odnowiona piramida ma kwadratowy fundament z wapienia o nieparzystej długości boku, na przykład 5x5. Nad nim znajduje się warstwa bloków piasku tego samego rozmiaru (5x5), a następnie coraz mniejsze warstwy: 3x3 i 1x1.

Po ukończeniu piramida rozpada się, a pośrodku pojawia się duży słonecznik. Możesz go zebrać, aby otrzymać energię. Im większa ukończona piramida, tym więcej energii otrzymasz.

---

[Statystyki](docs/stats.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
