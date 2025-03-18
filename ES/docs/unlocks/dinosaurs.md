# Dinosaurios
Los dinosaurios son criaturas antiguas y majestuosas que pueden cultivarse para obtener huesos antiguos.

Desafortunadamente, los dinosaurios se extinguieron hace mucho tiempo, así que lo mejor que podemos hacer ahora es disfrazarnos como uno.
Para este propósito, has recibido el nuevo sombrero de dinosaurio.

El sombrero se puede equipar con
`change_hat(Hats.Dinosaur_Hat)`

Desafortunadamente, no se parece mucho al de la publicidad...

Si equipas el sombrero de dinosaurio y tienes suficientes calabazas, una [manzana](objects/apple) se comprará automáticamente y se colocará bajo el dron.
Cuando el dron está sobre una manzana y se mueve de nuevo, comerá la manzana y crecerá su cola en uno. Si puedes permitírtelo, se comprará una nueva manzana y se colocará en una ubicación aleatoria.
La manzana no puede aparecer si hay algo plantado donde quiere estar.

La cola del dinosaurio se arrastrará detrás del dron llenando las casillas previas por las que se movió el dron. Si un dron intenta moverse sobre la cola, `move()` fallará y devolverá `False`. 
El último segmento de la cola se moverá durante el movimiento, por lo que puedes moverte sobre él. Sin embargo, si la serpiente llena toda la granja, no podrás moverte más. Así que puedes comprobar si la serpiente está completamente crecida verificando si ya no puedes moverte.

Usar `measure()` en una manzana devolverá la posición de la próxima manzana como una tupla.

`next_x, next_y = measure()`

Cuando el sombrero se vuelve a desequipar al equipar un sombrero diferente, la cola será cosechada.
Recibirás huesos iguales al largo de la cola al cuadrado. Así que para una cola de longitud `n` recibirás `n**2` `Items.Bone`.
Por ejemplo:
longitud 1 => 1 hueso
longitud 2 => 4 huesos
longitud 3 => 9 huesos
longitud 4 => 16 huesos
longitud 16 => 256 huesos
longitud 100 => 10000 huesos

El Sombrero de Dinosaurio es muy pesado, así que si lo equipas, hará que `move()` tome 800 ticks en lugar de 200. Sin embargo, cada vez que recojas una manzana, el número de ticks utilizados por `move()` se reduce en un 3% (redondeado hacia abajo), porque una cola más larga puede ayudarte a moverte.

El siguiente bucle imprime el número de ticks utilizados por `move()` después de cualquier número de manzanas:

`ticks = 800
for i in range(100):
    print("ticks después de ", i, " manzanas: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=mostrar pista 1>Si sigues moviéndote a lo largo del mismo camino que cubre todo el campo, puedes conseguir fácilmente una serpiente que cubra todo el campo cada vez, porque cubrirás cada espacio libre antes de regresar a donde está tu cola. No es muy eficiente, pero funciona.
Los campos de tamaño impar pueden ser más difíciles. Si tienes `Unlocks.Debug2` desbloqueado, puedes cambiar el tamaño del campo a algo más conveniente.</spoiler>