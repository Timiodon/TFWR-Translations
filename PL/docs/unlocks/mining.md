[<- Ekspansja 1](docs/unlocks/expand_1.md) <right>[Podziemne zmysły ->](docs/unlocks/underground_senses.md)
<right>[Ryż ->](docs/unlocks/rice.md)
<right>[Węgiel ->](docs/unlocks/coal.md)
---
# Górnictwo
Twój dron otrzymał prymitywne wiertło, które pozwala mu szukać skarbów pod ziemią.

Za pomocą polecenia `dig()` możesz wkopać się w blok pod dronem.

Na razie zbierzmy trochę bloków:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Aby wrócić na powierzchnię, możesz w dowolnym momencie użyć `clear()`. Przywróci to również farmę.

Najechanie kursorem na blok pokazuje jego nazwę, stabilność i twardość.

# Wiertło
W miarę kopania w dół zauważysz, że bloki stają się twardsze, przez co kopanie zajmuje więcej czasu. Na szczęście możemy ulepszyć wiertło!

Aby dron orientował się pod ziemią, szybko odblokuj [Podziemne zmysły](docs/unlocks/underground_senses.md). Pozwolą sprawdzać pozycję z oraz rodzaj, twardość i stabilność podłoża.

Na przykład [Podziemne zmysły](docs/unlocks/underground_senses.md) pozwalają użyć `get_hardness()` do sprawdzenia twardości bloku pod dronem. Jeśli trafisz na obszar wyjątkowo twardych bloków, warto go ominąć, aby szybciej posuwać się naprzód:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Oczywiście im głębiej schodzisz, tym twardsze stają się bloki, więc ta strategia pomaga tylko do pewnego momentu.

## Zawały
Kopanie w dół powoduje zawał otaczających bloków. Cztery bloki obok drona są zawsze niszczone. Następnie zawał rozprzestrzenia się zależnie od stabilności podłoża. Blok o stabilności 1, taki jak teren trawiasty, wytrzymuje różnicę wysokości równą 1. Innymi słowy, jeśli jego sąsiad w pionie lub poziomie ma współrzędną z niższą o co najmniej 2 bloki, teren trawiasty zostanie zniszczony.

Stabilność bloku jest podana w jego podpowiedzi po najechaniu kursorem.

Gdy blok się zawali, wszystkie bloki nad nim również zostaną usunięte. Zasoby otrzymujesz tylko z bloków wykopanych bezpośrednio przez drona, więc bloki utracone w zawale zostają zniszczone bez żadnego plonu.

---

[Podziemne zmysły](docs/unlocks/underground_senses.md)      [Pętla While](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
