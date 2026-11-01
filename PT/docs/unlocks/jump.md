[<- Carvão](docs/unlocks/coal.md)
---
# Salto
Seu drone desbloqueou o comando `jump()`. Use-o passando um desbloqueio como argumento, como `Unlocks.Iron`.

Este comando permite escolher certos recursos escondidos no solo e saltar instantaneamente até eles. É especialmente útil para depuração ou para alcançar um veio que você acabou de deixar passar.

Após o salto, o recurso desejado deve estar a até 3 blocos da superfície superior. `jump()` só pode ser usado uma vez por execução do programa; novas tentativas causarão um erro.

O exemplo abaixo salta até o [arroz](docs/unlocks/rice.md), encontra a argila e planta uma fileira de terraços de arroz:
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
# Salte para perto do arroz
jump(Unlocks.Rice)

# Plante uma fileira de terraços de arroz
for i in range(get_world_size()):
    # O salto não é exato; escave os últimos blocos
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Desbloqueios Compatíveis
`jump()` funciona apenas com os seguintes desbloqueios de mineração:
- Carvão
- Ferro
- Quartzo
- Arroz
- Abóboras Petrificadas
- Solos Especiais
- Pirâmide
- Mapa do Tesouro
- Cogumelos
- Dinamite

---

[jump()](functions/jump)
