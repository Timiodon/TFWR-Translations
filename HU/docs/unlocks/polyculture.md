# Polikultura
Lehet, hogy már észrevetted, hogy néha a növények többet teremnek, ha együtt vannak ültetve.
A fű, a bokrok, a fák és a sárgarépa több termést ad, ha megfelelő „társ-növény” van mellettük. A társ preferencia minden egyes növénynél eltérő, és nem megjósolható. Szerencsére a drón alatt lévő növény társ-preferenciája a `get_companion()` függvénnyel lekérdezhető. A függvény egy tuple-t ad vissza, ahol az első elem a kívánt társ növény típusa, a második pedig az a pozíció, ahol ezt a társat szeretné.

`plant_type, (x, y) = get_companion()`

Például, ha elültetsz egy bokrot, majd meghívod a `get_companion()` függvényt, akkor valami ilyesmit kapsz: `(Entities.Carrot, (3, 5))`. Ez azt jelenti, hogy ennek a bokornak sárgarépára van szüksége a `(3,5)` pozícióban. Tehát ha sárgarépát ültetsz a `(3,5)` helyre, majd betakarítod a bokrot, több fa termést fog adni. A sárgarépa növekedési állapota nem számít.

Egy növény társ-preferenciája lehet Entities.Grass, Entities.Bush, Entities.Tree vagy Entities.Carrot. Minden növény véletlenszerűen választ, de soha nem saját magát választja társának. A pozíció is bármely hely lehet 3 lépésen belül a növénytől, kivéve magának a növénynek a helyét.

Ha a drón alatt nincs olyan növény, amelynek lenne társ-preferenciája, a `get_companion()` `None`-t ad vissza.

A polikultúra feloldása előtt a hozam szorzó értéke 5. Minden fejlesztésnél megduplázódik.