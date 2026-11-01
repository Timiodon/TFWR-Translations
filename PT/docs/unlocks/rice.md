[<- Mineração](docs/unlocks/mining.md) <right>[Bambu ->](docs/unlocks/bamboo.md)
<right>[Abóboras Petrificadas ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlita e Solo Franco ->](docs/unlocks/special_soils.md)
---
# Arroz
Sob a superfície e a camada de `Grounds.Dirt`, há uma fina camada de `Grounds.Clay`. Acontece que esse solo fértil e encharcado é perfeito para plantar mudas de arroz.

O código a seguir pode ajudar você a escavar para baixo até encontrar argila e plantar arroz:
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
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

Enquanto o drone estiver sobre `Grounds.Clay`, use `plant(Entities.Rice)` para plantar arroz, `can_harvest()` para verificar se amadureceu e `harvest()` para colher.

## Terraços
Ao plantar arroz, o solo vira `Grounds.Rice_Terrace` para oferecer as condições ideais de maturação. Quando o arroz amadurece, o solo seca e vira `Grounds.Dry_Rice_Terrace`, onde não é possível plantar mais arroz. Felizmente a camada tem alguns blocos de espessura: remova o bloco com `dig()` e plante mais arroz na `Grounds.Clay` abaixo. Se a camada acabar, use `clear()` para restaurar o mundo e escave até uma nova camada.

---

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Loop For](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
