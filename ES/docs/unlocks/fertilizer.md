# Fertilizante
En algún momento, esperar a que las plantas crezcan ya no es lo suficientemente eficiente. 
Similar al agua, recibirás automáticamente 1 fertilizante cada 10 segundos, y uno más con cada mejora.

El fertilizante puede hacer que las plantas crezcan instantáneamente. `use_item(Items.Fertilizer)` reduce el tiempo de crecimiento restante de la planta bajo el dron en 2 segundos.

Esto tiene algunos efectos secundarios.
Las plantas cultivadas con fertilizante se infectarán.

Cuando una planta está infectada, la mitad de su rendimiento se convierte en `Items.Weird_Substance` cuando se cosecha.
La Sustancia Rara también se puede usar en las plantas, lo que tiene el efecto de cambiar el estado de infección de la planta y de todas las plantas adyacentes.

Así que si llamas a `use_item(Items.Weird_Substance)` en una planta infectada, la curará, pero si la usas en una planta sana, la infectará.

Si la usas en una planta infectada que tiene vecinos sanos, curará la planta pero infectará a los vecinos y viceversa.