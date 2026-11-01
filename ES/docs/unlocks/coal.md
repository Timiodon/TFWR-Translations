[<- Minería](docs/unlocks/mining.md) <right>[Hierro ->](docs/unlocks/iron.md)
<right>[Saltar ->](docs/unlocks/jump.md)
---
# Carbón
Bajo tierra hay distintos minerales esperando a que los encuentres y los extraigas. Si atraviesas la superficie y excavas en `Grounds.Dirt`, el primer mineral que encontrarás es carbón.

No hace falta nada especial para extraer carbón: ejecuta `dig()` cuando el dron esté justo encima de un bloque de `Grounds.Coal`. Usa `get_ground_type()` para comprobar qué hay debajo del dron y `get_ground_type(direction)` para comprobar los cuatro bloques adyacentes.

El siguiente programa es un buen punto de partida para encontrar carbón. Excava hacia abajo en busca de una capa de carbón.
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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Excava hasta que aparezca un bloque de carbón
while get_ground_type() != Grounds.Coal:
    dig()

# Extrae el carbón
dig()
}}

## Nota sobre los derrumbes
Solo obtienes carbón de los bloques que excavas directamente, no de los que se derrumban alrededor del dron. Tenlo en cuenta al planificar la extracción para excavar el máximo de carbón y perder el mínimo por derrumbes.

## Estructura de las vetas
Sus vetas forman capas horizontales de 1 bloque de grosor que debes encontrar por casualidad al excavar tierra. Los bloques de carbón de una capa suelen estar pegados unos a otros, pero algunos solo se conectan en diagonal.

Los depósitos de carbón crecen en proporción al tamaño de la granja; sigue mejorando [Expandir](unlocks/expand) para poder extraer más carbón.

## Estrategia
<spoiler=mostrar pista> 
Una estrategia sencilla, sobre todo en granjas pequeñas, es excavar todos los bloques a la profundidad donde encontraste carbón. Para mejorar la eficiencia, puedes registrar dónde has visto carbón con `get_ground_type(direction)` y evitar perder tiempo pasando sobre tierra. Ten cuidado de no pasar por alto las conexiones diagonales, que perderás si solo te mueves sobre bloques de carbón.
</spoiler>

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
