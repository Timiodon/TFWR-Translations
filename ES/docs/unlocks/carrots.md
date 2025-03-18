# Zanahorias
Antes de que puedas plantar zanahorias con `plant(Entities.Carrot)`, tienes que arar la tierra. Esto cambiará el suelo a `Grounds.Soil`. Para arar la tierra, simplemente llama a `till()`. Si llamas a `till()` nuevamente, volverá a cambiar a `Grounds.Grassland`.

Plantar zanahorias cuesta madera y heno. Estos elementos se eliminarán automáticamente al llamar a `plant(Entities.Carrot)`.

Puedes ver el costo de cualquier planta en su [página propia](objects/carrot).