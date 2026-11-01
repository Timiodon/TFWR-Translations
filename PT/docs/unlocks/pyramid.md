[<- Bambu](docs/unlocks/bamboo.md)
---
# Pirâmides
O subsolo agora contém antigas estruturas piramidais das quais você pode colher energia para acelerar o drone!

As pirâmides são feitas de blocos de areia (`Grounds.Sand`). Abaixo da pirâmide há uma camada de fundação de calcário (`Grounds.Limestone`). Como são antigas e erodidas, você as encontra parcialmente destruídas. A fundação está sempre presente, mas haverá buracos na areia.

Veja como ficam as ruínas de uma pirâmide ao serem desenterradas:
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
# Escave até encontrar a base de uma pirâmide
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # Lembre a profundidade da base

# Escave tudo que não faz parte da pirâmide
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## Restaurando a Pirâmide
Como pode ver, há vários buracos na areia que precisam ser preenchidos. Ao preencher os buracos e restaurar a pirâmide, ela se destrói e um grande girassol surge no centro da base de calcário. Colha-o para receber `Items.Power`. Quanto maior a pirâmide, mais energia você recebe.

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
# Precisamos de uma base de calcário para pôr areia
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# Coloque uma camada de areia 3x3 sobre o calcário
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# Tente colocar outra camada 3x3
# Só o bloco central tem apoio e permanece
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

Uma pirâmide restaurada corretamente tem uma fundação quadrada de calcário com lados de comprimento ímpar, por exemplo 5x5. Acima há uma camada de areia do mesmo tamanho (5x5), seguida de camadas progressivamente menores: 3x3 e depois 1x1.

Os blocos acima da pirâmide são sempre terra. Você pode usar esse fato para escavar uma pirâmide de forma eficiente.

## Energia
Enquanto você tiver energia, o drone a usará para funcionar duas vezes mais rápido.
Ele consome 1 de energia a cada 30 ações, como movimentos, colheitas ou plantios.
Executar outras instruções de código também pode consumir energia, mas muito menos do que as ações do drone.

Em geral, tudo que é acelerado por melhorias de velocidade também é acelerado por energia.
Qualquer coisa acelerada por energia também usa energia proporcional ao tempo que leva para executá-la, ignorando as melhorias de velocidade.

A energia não afeta `dig()`.

---

[Estatísticas](docs/stats.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
