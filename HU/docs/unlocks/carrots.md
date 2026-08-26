# Répák
Mielőtt répákat ültethetnél a `plant(Entities.Carrot)`-ral, felszántott talajra van szükség. Ez a talajt `Grounds.Soil`-ra változtatja. A talaj felszántásához egyszerűen hívd a `till()`-t. A `till()` újbóli meghívása visszaváltoztatja `Grounds.Grassland`-ra.

A répák ültetése fát és szénát igényel. Ezek az itemek automatikusan eltávolításra kerülnek a `plant(Entities.Carrot)` hívásakor.

A bármely növény költségét megtekintheted a [saját oldalán](objects/carrot).