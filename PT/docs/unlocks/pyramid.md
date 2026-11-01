[<- Bambu](docs/unlocks/bamboo.md)
---
# Pirâmides

O subsolo agora contém antigas estruturas piramidais das quais você pode colher energia!

As pirâmides são feitas de blocos de areia (`Grounds.Sand`). Abaixo da pirâmide há uma camada de fundação de calcário (`Grounds.Limestone`). Como são antigas e erodidas, você as encontra parcialmente destruídas. A fundação está sempre presente, mas haverá buracos na areia. Veja como uma pirâmide fica ao ser escavada:

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

Os blocos acima da pirâmide são sempre terra. Você pode usar esse fato para escavar uma pirâmide de forma mais eficiente que no código acima.

Como pode ver, há vários buracos na areia que precisam ser preenchidos. Ao restaurar a pirâmide, ela se destrói e você recebe energia como recompensa.

Você pode restaurar uma pirâmide colocando blocos com `place(Grounds.Sand)`. A areia é um bloco especial que desmorona imediatamente sem apoio adequado. Cada bloco de areia deve ser colocado diretamente sobre calcário ou sobre uma área 3x3 de blocos de areia. Veja uma pequena pirâmide construída à mão. Construí-la você mesmo não rende energia:

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

Uma pirâmide restaurada corretamente tem uma fundação quadrada de calcário com lados de comprimento ímpar, por exemplo 5x5. Acima há uma camada de areia do mesmo tamanho (5x5), seguida de camadas progressivamente menores: 3x3 e depois 1x1.

Quando a pirâmide é concluída, ela desmorona e um grande girassol surge no centro. Colha-o para receber energia. Quanto maior a pirâmide, mais energia você recebe.

---

[Estatísticas](docs/stats.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)

