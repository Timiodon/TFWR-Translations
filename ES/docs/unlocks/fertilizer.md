# Fertilizante
En algún momento, esperar a que las plantas crezcan ya no es lo suficientemente eficiente. 
Al igual que con el agua, recibirás automáticamente 1 fertilizante cada 10 segundos, más uno extra por cada mejora.

El fertilizante puede hacer que las plantas crezcan al instante. `use_item(Items.Fertilizer)` reduce el tiempo de crecimiento restante de la planta bajo el dron en 2 segundos.

Esto tiene algunos efectos secundarios.
Las plantas cultivadas con fertilizante estarán infectadas.

Cuando una planta está infectada, la mitad de su rendimiento se convierte en `Items.Weird_Substance` al cosecharla.
Weird Substance también se puede usar en plantas, lo que tiene el efecto de alternar el estado de infección de la planta y todas las plantas adyacentes.

Así que si llamas a `use_item(Items.Weird_Substance)` en una planta infectada, la curará, pero si la usas en una planta saludable, la infectará.

Si lo usas en una planta infectada que tiene vecinos saludables, curará la planta pero infectará a los vecinos y viceversa.