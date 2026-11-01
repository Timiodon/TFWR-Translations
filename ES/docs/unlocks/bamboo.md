[<- Arroz](docs/unlocks/rice.md) <right>[Bloques de colores ->](docs/unlocks/debug_place.md)
<right>[Pirámides ->](docs/unlocks/pyramid.md)
---
# Bambú
El bambú es una planta que crece hacia arriba. El dron tendrá que retirar sus frutos marrones con regularidad para que siga creciendo. Podemos hacerlo con el comando `hover` que acabas de desbloquear.

El bambú debe plantarse en terreno labrado (`Grounds.Soil`) y plantarlo cuesta arroz.

El siguiente código planta bambú y espera a que crezca hasta su primer fruto.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # apártate para que el bambú crezca
}}

## Frutos
El bambú crece exactamente 1 bloque por segundo.

El bambú produce frutos cada pocos bloques. Cuando esto ocurre, deja de crecer y tendrás que entrar en él con el dron para destruir el fruto. El bambú puede crecer hasta su tercer fruto. A partir de ahí no crecerá más alto, aunque lo retires.

Para retirar frutos, primero debes usar `hover` para situarte a la altura correcta. Después usa `move` para entrar en el fruto y retirarlo, y de nuevo `move` para apartarte y dejar que el bambú siga creciendo.

Puedes usar `measure()` sobre el bambú para comprobar a qué altura aparecerá el siguiente fruto. `measure()` empieza a contar desde `0`, así que `hover(measure())` llevará al dron a la altura del fruto.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # flota a la altura del fruto

move(East) # apártate y espera a que crezca
for i in range(3):
    do_a_flip()

move(West) # retira el fruto
move(East) # vuelve a apartarte
}}

## Flotar
El comando `hover` recibe un argumento: la altura a la que flotar, un número entre `0` y `18`. La altura de vuelo predeterminada del dron es `1`. `hover` no permite descender dentro de entidades sólidas: si el dron ya está sobre un bambú, no puedes introducirlo en él con `hover(0)`.

`hover` devuelve `True` si el dron alcanzó la altura indicada, y `False` en caso contrario.

También está el comando `get_hover`, que devuelve la altura de vuelo actual del dron.

Si usas `dig`, `harvest` o `plant` mientras flotas, el dron volverá a su altura de vuelo predeterminada (`1`).

Por último, la altura de vuelo no afecta a `get_pos_z()`. Siempre devuelve la posición z del bloque debajo del dron.

## Cosechar bambú
Aunque puedes usar `harvest()`, lo recomendable es entrar en el bambú con el dron a una altura de vuelo de `0` (`hover(0)`). Así cosecharás toda la planta de una vez.

Si quieres cosechar el bambú sin destruirlo, puedes entrar en él con `move` a cualquier altura, por ejemplo con `hover(3)`. Así cosecharás todos los segmentos desde esa altura hacia arriba, pero la planta seguirá viva. El bambú cosechado parcialmente vuelve a producir frutos, así que tendrás que retirarlos otra vez.

En ambos casos, el rendimiento equivale al cuadrado del número de segmentos de bambú destruidos: cuanto más alto sea el bambú, mayor será el rendimiento.

---

[Estadísticas](docs/stats.md)      [Bucle for](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funciones](docs/scripting/functions.md)      [Arroz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
