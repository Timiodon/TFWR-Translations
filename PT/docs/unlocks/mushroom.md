[<- Quartzo](docs/unlocks/quartz.md) <right>[Dinamite ->](docs/unlocks/dynamite.md)
---
# Cogumelo
Muitos tipos de cogumelo crescem em colônias no subsolo. Procure um estrato de `Grounds.Mushroom` ao escavar. Use `measure()` no solo para obter o tipo de cogumelo como um número de `0` a `5`.

O código abaixo encontra cogumelos e imprime o tipo:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# Processe uma fileira de cogumelos
for i in range(get_world_size()):
    # Escave até o bloco de cogumelo superior
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Imprima o número do tipo de cogumelo
    print(measure())

    move(East)
}}

## Coletando Cogumelos
Cogumelos do mesmo tipo gostam de ficar juntos, mas são tímidos demais para crescer uns sobre os outros. Empurre o bloco de cogumelo sob o drone com `push(direction)`.

Empilhe dois blocos de cogumelos do mesmo tipo e eles serão colhidos automaticamente.

O código abaixo abre espaço e empurra um cogumelo até combinar com o cogumelo abaixo:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Abra espaço para empurrar o cogumelo para leste
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Volte, empurre e siga o bloco empurrado
    move(West)
    push(East) # Empurre o cogumelo!
    move(East)
}}

# Empurrando Blocos
Use `can_push(direction)` para verificar se o bloco sob o drone pode ser empurrado e se há algo bloqueando a direção.

`push(direction)` empurra o bloco e informa se a ação foi bem-sucedida.

Só blocos de cogumelo podem ser empurrados. Blocos não podem ser empurrados para cima, e o empurrão falha se houver outro bloco no caminho. Quando empurrados para o ar, eles caem e pousam no próximo bloco abaixo.

# Estratégia
<spoiler=dica>
Lembre-se de que você pode chamar `place(Grounds.Dirt)` para colocar blocos sob o drone. Isso ajuda a preencher buracos e empurrar blocos por cima deles.
</spoiler>

---

[Estatísticas](docs/stats.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [Dicionários](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
