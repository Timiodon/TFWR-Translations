[<- Hierro](docs/unlocks/iron.md)
---
# Prospección de hierro
Puede que hayas notado que a veces cuesta encontrar vetas de hierro. Podrías excavar por todas partes y confiar en encontrarlas por casualidad, pero hay una forma mejor: como el hierro es magnético, podemos detectarlo a distancia.

El comando `prospect_iron()` sirve precisamente para eso. `prospect_iron()` devuelve la dirección (`North`, `East`, `South` o `West`) en la que tendría que moverse el dron para dar un paso hacia el mineral de hierro más cercano.

Ejecutar el comando cuesta 1 carbón.

`prospect_iron()` devuelve `None` si el dron ya está justo encima del mineral de hierro más cercano, si no tienes suficiente carbón para ejecutar el comando o si no hay hierro dentro del alcance.

Puedes usar el siguiente código para acercarte un paso al siguiente mineral de hierro:

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
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# Comprueba que la prospección devuelve una dirección
if prospect_iron() != None:
    move(prospect_iron()) # Acércate a la veta de hierro
}}

Quizá te convenga optimizar este código con una variable, porque ahora llama dos veces a `prospect_iron()` y cuesta 2 de carbón.

## Cálculo de distancias
La distancia al mineral de hierro más cercano se calcula según el número de pasos que debe dar el dron. Si hay mineral de hierro 2 bloques al este y 3 bloques al norte del dron, se considera que está a una distancia de 5, porque el dron necesitaría cinco pasos para llegar hasta allí.

Excavar también cuenta como un paso. Así que, si además el hierro está enterrado 7 bloques bajo tierra, se considera que está a una distancia de 12, porque el dron necesitaría cinco pasos para colocarse encima del hierro y después siete excavaciones para alcanzarlo.

---

[Hierro](docs/unlocks/iron.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
