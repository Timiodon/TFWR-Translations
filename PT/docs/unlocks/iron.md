[<- Carvão](docs/unlocks/coal.md) <right>[Quartzo ->](docs/unlocks/quartz.md)
<right>[Prospecção de Ferro ->](docs/unlocks/prospecting.md)
<right>[Mapa do Tesouro ->](docs/unlocks/treasure_map.md)
---
# Ferro
Depois de encontrar carvão em `Grounds.Dirt`, escave além da camada de `Grounds.Clay` até `Grounds.Rock` para encontrar ferro.

Ao contrário do carvão, os veios de ferro também se estendem verticalmente. Todos os blocos de ferro de um veio ficam diretamente adjacentes; nunca se conectam apenas na diagonal.

Os veios de ferro começam pequenos, e você precisará de sorte para encontrá-los. Melhorar o ferro aumenta o tamanho máximo dos veios e facilita encontrá-los por acaso. Para encontrá-los com segurança, desbloqueie a [prospecção](docs/unlocks/prospecting.md).

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# Escave até aparecer um bloco de ferro
while get_ground_type() != Grounds.Iron:
    dig()

# Extraia o ferro
dig()
}}

---

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Prospecção de Ferro](docs/unlocks/prospecting.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
