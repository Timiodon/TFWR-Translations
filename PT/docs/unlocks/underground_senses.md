[<- Mineração](docs/unlocks/mining.md)
---
# Sentidos Subterrâneos
Vamos adicionar alguns sensores para que o drone consiga se orientar no subsolo.

## Posição Z
Agora você pode usar `get_pos_z()` para obter a altura do drone (começa em 0 e fica negativa conforme ele desce).

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## Tipo de Solo
`get_ground_type()` retorna o tipo de solo sob o drone. Você pode passar uma direção, como `get_ground_type(North)`, para obter o tipo de solo de um bloco vizinho.

Veja como verificar se o bloco sob o drone é terra:

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
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
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## Dureza e Estabilidade
`get_hardness()` retorna a dureza do bloco de solo sob o drone. Você pode passar uma direção, como `get_hardness(North)`. Quanto maior a dureza, mais tempo leva para escavar.

`get_stability()` retorna a estabilidade do bloco de solo sob o drone. Você pode passar uma direção, como `get_stability(North)`. Estabilidade 1 significa que o bloco suporta uma diferença de altura de 1 antes de desmoronar.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

Observe que os quatro blocos diretamente ao lado do drone são removidos durante a escavação, independentemente da estabilidade, salvo se tiverem uma função especial. Argila, ferro e quartzo, por exemplo, não são removidos por essa regra, mas ainda podem desmoronar por falta de estabilidade.
---

[Mineração](docs/unlocks/mining.md)      [Sentidos](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
