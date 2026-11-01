[<- Ferro](docs/unlocks/iron.md)
---
# Mapa do Tesouro
Lendas falam de um tesouro esquivo escondido por um pirata esquecido, morto há muito tempo — ou algo assim. E se ele anotou o caminho em um mapa e depois o perdeu? Talvez tenha deixado o mapa cair ao ser encurralado por um rio de lava, e ele ficou preservado sob uma camada de basalto.

Medir os blocos de basalto pode revelar algo!

<spoiler=conte mais>
Procure uma camada de `Grounds.Basalt`. Tente medir o basalto e veja o que ele informa. A pista pode levar ao mapa do tesouro, e medir o mapa certamente revelará o caminho até o tesouro — mas você consegue decifrar as instruções?
</spoiler>

<spoiler=só diga como>
Certo: encontre o estrato de `Grounds.Basalt` e o bloco `Grounds.Treasure_Map` diretamente abaixo. Use `measure()` no basalto para obter a posição `(x, y)` do bloco do mapa.

Chame `measure()` no bloco do mapa para obter o caminho como uma sequência de letras de direção. N, E, S e W representam `North`, `East`, `South` e `West`; D significa "Down" ou "Dig". Essas letras descrevem um caminho de blocos `Grounds.Treasure_Path` até o tesouro.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# Encontre a camada de basalto
while get_ground_type() != Grounds.Basalt:
    dig()

# Medir o basalto retorna a posição do mapa
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# Mapa encontrado: meça para obter o caminho
do_a_flip()
instructions = measure()
print("instruções: ", instructions)

# Escave o mapa para iniciar a caça ao tesouro
dig()
}}

Você pode percorrer a string com um laço `for` para processá-la letra por letra:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# As instruções do mapa retornam em uma única string
instructions = measure()
# Use for-in para processar a string letra por letra
for letter in instructions:
    print(letter)
}}

O drone precisa permanecer sobre blocos de `Grounds.Treasure_Path` o tempo todo. Se passar para outro solo, o caminho se romperá e o tesouro será perdido.

## Objetivo
No fim do caminho há um bloco `Grounds.Treasure_Goal`. Se o drone não tiver saído da trilha, um `Entities.Underground_Treasure` aparecerá sobre ele. O drone pode usar `harvest()` no baú para coletar o ouro.

## Recompensa
A quantidade de ouro é proporcional ao comprimento do caminho. Melhorar Mapa do Tesouro aumenta sua profundidade, enquanto melhorar Expandir dá mais espaço lateral. Ambas as melhorias aumentam o comprimento do caminho e a quantidade de ouro encontrada.

## Vários Drones
O drone que escava o bloco do mapa do tesouro deve encontrar o tesouro sem sair dos blocos do caminho.
</spoiler>

---

[Estatísticas](docs/stats.md)      [Loop For](docs/scripting/for.md)      [Tuplas](docs/scripting/tuples.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
