[<- Carbone](docs/unlocks/coal.md)
---
# Salto
Il tuo drone ha sbloccato il comando `jump()`. Per usarlo, passa uno sblocco come argomento, per esempio `Unlocks.Iron`.

Questo comando permette di puntare a determinate risorse nascoste nel terreno e saltare istantaneamente fino a esse. È particolarmente utile per il debug o per raggiungere una vena che hai appena mancato.

Dopo il salto, la risorsa cercata dovrebbe trovarsi entro 3 blocchi dalla superficie superiore. `jump()` può essere usato una sola volta per esecuzione del programma; ulteriori tentativi causano un errore.

L'esempio seguente salta fino al [riso](docs/unlocks/rice.md), trova l'argilla e pianta una fila di terrazze di riso:
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
# Salta vicino al riso
jump(Unlocks.Rice)

# Pianta una fila di terrazze di riso
for i in range(get_world_size()):
    # Il salto non è preciso: scava gli ultimi blocchi
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Sblocchi Compatibili
`jump()` funziona solo con i seguenti sblocchi minerari:
- Carbone
- Ferro
- Quarzo
- Riso
- Zucche Pietrificate
- Terreni Speciali
- Piramide
- Mappa del Tesoro
- Funghi
- Dinamite

---

[jump()](functions/jump)
