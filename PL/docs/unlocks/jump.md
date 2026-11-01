[<- Węgiel](docs/unlocks/coal.md)
---
# Skok
Twój dron odblokował polecenie `jump()`. Używa się go, przekazując odblokowanie jako argument, na przykład `Unlocks.Iron`.

To polecenie pozwala wskazać wybrane zasoby pod ziemią i natychmiast skoczyć w dół do nich. Jest szczególnie przydatne podczas debugowania lub do powrotu do niedawno pominiętej żyły rudy.

Po skoku cel powinien być najwyżej 3 bloki pod górną powierzchnią. `jump()` można użyć tylko raz podczas jednego wykonania programu. Kolejne próby wywołają błąd.

Poniższy przykład skacze do [ryżu](docs/unlocks/rice.md), znajduje warstwę gliny i sadzi rząd tarasów ryżowych:
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# Skocz w pobliże ryżu
jump(Unlocks.Rice)

# Posadź rząd tarasów ryżowych
for i in range(get_world_size()):
    # Skok jest niedokładny, wykop pozostałe bloki
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Obsługiwane odblokowania
`jump()` działa tylko z następującymi odblokowaniami górniczymi:
- Węgiel
- Żelazo
- Kwarc
- Ryż
- Skamieniałe dynie
- Specjalne gleby
- Piramida
- Mapa skarbów
- Grzyby
- Dynamit

---

[jump()](functions/jump)
