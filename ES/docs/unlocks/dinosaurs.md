# Dinosaurios
Los dinosaurios son criaturas antiguas y majestuosas que se pueden criar para obtener huesos antiguos.

Desafortunadamente, los dinosaurios se extinguieron hace mucho tiempo, así que lo mejor que podemos hacer ahora es disfrazarnos de uno.
Para este propósito, has recibido el nuevo sombrero de dinosaurio.

El sombrero se puede equipar con
`change_hat(Hats.Dinosaur_Hat)`

Desafortunadamente, no se ve exactamente como en el anuncio...

Si equipas el sombrero de dinosaurio y tienes suficientes calabazas, se comprará y colocará automáticamente una [manzana](objects/apple) debajo del dron.
Cuando el dron esté sobre una manzana y se mueva de nuevo, se comerá la manzana y su cola crecerá en uno. Si puedes permitírtelo, se comprará una nueva manzana y se colocará en una ubicación aleatoria.
La manzana no puede aparecer si hay algo más plantado donde quiere estar.

La cola del dinosaurio será arrastrada detrás del dron, llenando las casillas anteriores por las que se movió. Si un dron intenta moverse sobre la cola, `move()` fallará y devolverá `False`. 
El último segmento de la cola se apartará durante el movimiento, por lo que puedes moverte sobre él. Sin embargo, si la serpiente llena toda la granja, ya no podrás moverte. Así que puedes comprobar si la serpiente ha crecido completamente verificando si ya no puedes moverte.

Usar `measure()` en una manzana devolverá la posición de la siguiente manzana como una tupla.

`next_x, next_y = measure()`

Cuando el sombrero se desequipa equipando un sombrero diferente, la cola será cosechada.
Recibirás huesos equivalentes a la longitud de la cola al cuadrado. Así que para una cola de longitud `n`, recibirás `n**2` `Items.Bone`. 
Por ejemplo:
longitud 1 => 1 hueso
longitud 2 => 4 huesos
longitud 3 => 9 huesos
longitud 4 => 16 huesos
longitud 16 => 256 huesos
longitud 100 => 10000 huesos

El Sombrero de Dinosaurio es muy pesado, así que si lo equipas, hará que `move()` tarde 400 ticks en lugar de 200. Sin embargo, cada vez que recoges una manzana, el número de ticks que usa `move()` se reduce en un 3% (redondeado hacia abajo), porque una cola más larga puede ayudarte a moverte.

El siguiente bucle imprime el número de ticks que usa `move()` después de cualquier número de manzanas:

`ticks = 400
for i in range(100):
    print("ticks después de ", i, " manzanas: ", ticks)
    ticks -= ticks * 0.03 // 1`

Solo tienes un sombrero de dinosaurio, así que solo un dron puede llevarlo.

<spoiler=mostrar pista 1>Si te mantienes moviendo por el mismo camino que cubre todo el campo, puedes conseguir fácilmente una serpiente que cubra todo el campo cada vez. No es muy eficiente, pero funciona.
Recorrer completamente una granja muy grande puede llevar mucho tiempo y es posible que no necesites tantos huesos. Siéntete libre de usar `set_farm_size()` para cambiar el tamaño de la granja a algo más conveniente.</spoiler>