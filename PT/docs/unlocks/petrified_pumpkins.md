[<- Arroz](docs/unlocks/rice.md)
---
# Abóboras Petrificadas
Aparentemente, é possível encontrar abóboras no subsolo. Elas endureceram e ficaram petrificadas, mas ainda servem para nossos propósitos. Use `dig()` nelas para obter abóboras.

Essa é uma alternativa para obter abóboras sem cultivá-las na superfície. Se preferir cultivá-las, você pode ignorar completamente as abóboras petrificadas.

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite", "quartz"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
}}

Abóboras petrificadas aparecem no subsolo em blocos de 3x3x3 ou 5x5x5. Não há uma forma garantida de encontrá-las; é preciso torcer para o drone atingir uma. Elas aparecem na terra dura abaixo da camada de pedra e ferro, aproximadamente na mesma altura do quartzo (se estiver desbloqueado).

---

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
