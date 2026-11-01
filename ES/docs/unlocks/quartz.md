[<- Hierro](docs/unlocks/iron.md) <right>[Hongo ->](docs/unlocks/mushroom.md)
---
# Cuarzo
Después de las vetas de hierro en `Grounds.Rock`, encontrarás cuarzo en el fondo de la capa de roca y en la `Grounds.Dirt` dura de debajo (comprueba la dureza con `get_hardness()` de los [sentidos subterráneos](docs/unlocks/underground_senses.md)).

El siguiente fragmento excava más allá de la tierra y penetra en la capa de roca. Allí busca cuarzo continuamente mientras excava, hasta que la distancia sea menor que 2. Por último, imprime la distancia alcanzada.
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Excava hasta la capa de roca
while get_ground_type() != Grounds.Rock:
    dig()

# Sigue excavando hasta acercarte a una veta de cuarzo
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Imprime la distancia final hasta la veta
print(prospect_quartz())
}}

## Estructura de las vetas
El cuarzo crece en vetas con forma de aguja que forman columnas verticales, por lo que resulta bastante difícil encontrarlas por ensayo y error.

## Buscar cuarzo
Por suerte, podemos usar nuestro hierro y deformarlo hasta convertirlo en algo parecido a una vara de zahorí que nos permita localizar estas vetas de cuarzo más fácilmente. El comando para hacerlo es `prospect_quartz()`.

`prospect_quartz()` funciona de forma distinta a `prospect_iron()`. En vez de devolver la dirección en la que debe moverse el dron hacia el hierro más cercano, devuelve la distancia 3D exacta entre el bloque de cuarzo más próximo y el dron (distancia euclídea).

Ejecutar `prospect_quartz()` cuesta 1 hierro, así que conviene usar el comando con moderación.

Si `prospect_quartz()` no encuentra cuarzo cerca o no tienes suficiente hierro para realizar la búsqueda, devuelve `None`.

## Estrategia
<spoiler=mostrar pista>Puedes repetir la prospección y moverte para ver cómo cambia la distancia. En una superficie plana, minimizar la distancia puede situarte sobre una veta de cuarzo. Puedes usar una estrategia similar a la búsqueda binaria para minimizar las llamadas a `prospect_quartz()` y el hierro que consumen.

Las estrategias más elaboradas pueden usar geometría 2D para hallar la intersección de dos o más círculos. O puedes optar por la vía difícil: una trilateración completa, intersectando tres esferas para localizar la posición 3D exacta de la veta.

Para calcular una raíz cuadrada puedes usar el operador de potencia: por ejemplo, `16**0.5` obtiene la raíz cuadrada de 16. No hay funciones matemáticas integradas para trigonometría o vectores; tendrás que implementarlas.

Ten en cuenta que puede haber varias vetas cerca, por lo que distintas mediciones próximas podrían no señalar la misma veta.</spoiler>

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [Variables](docs/scripting/variables.md)      [Operadores](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
