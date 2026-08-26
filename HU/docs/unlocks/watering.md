# Öntözés
A növények gyorsabban nőnek, ha öntözik őket. A talaj vízszintje `0`-tól `1`-ig terjed.
A `get_water()` függvény a drón alatti talaj vízszintjét adja vissza.

A növény növekedési sebessége lineárisan skálázódik 1x sebességről 0 vízszinten 5x sebességre 1 vízszinten.

A talaj idővel kiszárad: Átlagosan másodpercenként az aktuális víz 1%-át veszti, de van némi random variancia ehhez. A magas vízszint fenntartása sokkal több vizet fogyaszt, mint az alacsony vízszint fenntartása.

Használhatsz vizet a növényeiden. Minden 10 másodpercben automatikusan hozzáadásra kerül egy tartály víz a leltárodhoz.
Az `Unlocks.Watering` fejlesztése megduplázza a kapott víz mennyiségét minden 10 másodpercben.

Egy tartály `0.25` vizet tartalmaz.

Hívd a `use_item(Items.Water)`-t bármely talaj felett a talaj öntözéséhez.