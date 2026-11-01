[<- Hongo](docs/unlocks/mushroom.md) <right>[Taladro explosivo ->](docs/unlocks/explosive_drill.md)
---
# Dinamita
El explosivo revolucionario que dejaron atrás expediciones mineras anteriores. Por desgracia, tu taladro es perfecto para hacer explotar la dinamita y volar todos los bloques que te rodean. La dinamita recogida se puede usar con `use_item(Items.Dynamite)` y explota inmediatamente debajo del dron.

Para extraer dinamita de forma segura, tendrás que encontrar el estrato doble de `Grounds.Dynamite` y `Grounds.Soot`. La dinamita del estrato superior se ha quedado algo vieja y es seguro excavar algunos de sus bloques. Sin embargo, parte de la dinamita sigue activa y explotará al excavarla.

Este ejemplo excava dinamita y rodea el punto inicial, dejando al descubierto el estrato de hollín con sus números e imprimiendo la medición:
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# Excava hasta el hollín atravesando la dinamita de arriba
while get_ground_type() != Grounds.Soot:
    dig()

# Lista de direcciones para mover el dron en círculo
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # El número del bloque de hollín
}}

## Buscaminas de dinamita
¿Puedes encontrar y excavar todos los bloques inertes dejando solo los activos? Cada bloque activo que esté rodeado únicamente por otros bloques activos o bloques de hollín te dará dinamita adicional cuando desaparezca el estrato de dinamita.

Por suerte, los bloques de hollín inferiores te ayudarán: pueden detectar cuántos bloques de dinamita vecinos contienen dinamita activa. No te dirán exactamente cuáles están activos, solo el número total, así que tendrás que combinar las lecturas de varios bloques de hollín y deducirlo por tu cuenta.

Llamar a `measure()` sobre un bloque de hollín devuelve el número de minas que hay en las ocho casillas vecinas del estrato de dinamita superior. El número puede ir de `0` (ninguna mina activa) a `8` (cada bloque vecino contiene una mina activa).

La primera excavación en el estrato de dinamita siempre da con un bloque inerte. Cada bloque de dinamita extraído produce un poco de dinamita. Cuando se destruye el estrato, ya sea por haber excavado correctamente todos los bloques inertes o por excavar sin querer dinamita activa, también obtienes una cantidad de dinamita igual al cuadrado del número de bloques activos descubiertos por completo.

## Estructura de los estratos
El número de minas activas en el estrato de dinamita y, por tanto, la dificultad para encontrarlas aumentan con la profundidad. El número total de minas aumenta con el tamaño de la granja, al igual que el rendimiento máximo posible al despejar un estrato de dinamita.

Mejora la dinamita para aumentar el rendimiento de excavar bloques de dinamita y de descubrir por completo bloques activos. La mejora también aumenta un 30 % la energía de las explosiones de dinamita.

## Detectar el éxito y el fracaso
Si excavas dinamita activa, los dos estratos explotan. Puedes comprobarlo usando `get_ground_type()` después de excavar `Grounds.Dynamite`. Si el terreno no es `Grounds.Soot`, no has resuelto el puzle. En cambio, si excavas el último bloque de dinamita inerte, todos los bloques de dinamita desaparecen y obtienes el rendimiento máximo del puzle. El estrato de hollín permanece, pero `measure()` devuelve `None`, lo que indica que el puzle se ha resuelto correctamente.

`# Excava un bloque de dinamita y comprueba el estado del puzle
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Se excavó dinamita activa; el puzle ha fallado
        return False
    elif measure() == None:
        # Se excavó el último bloque inerte; puzle resuelto
        return True
    else:
        # La medición dio un número; el puzle sigue en curso
        return None
`

## Estrategia
<spoiler=pista>
El código siguiente excava en el estrato de dinamita y busca bloques de hollín cuya medición sea `0`. Por cada uno que encuentra, excava todos los bloques de dinamita que lo rodean:
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# Rodea el bloque que excavamos al principio
for dir in circle_directions:
    # Si la medición del hollín es 0,
    # sabemos que todos los bloques de dinamita que lo rodean están inertes
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # Da otra vuelta por los bloques de alrededor
        for dir2 in circle_directions:
            move(dir2)
            # Excava el bloque de dinamita inerte
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[Estadísticas](docs/stats.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [Diccionarios](docs/scripting/dicts.md)      [Conjuntos](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
