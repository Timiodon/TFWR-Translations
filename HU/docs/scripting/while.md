# While ciklus
Felhoztad a `while` ciklust és a `True` és `False` értékeket. A `while` ciklus mindaddig végrehajtja a ciklus törzsét, amíg a feltétel `True`.

`while condition:
	#ciklus törzse`

Ne aggódj a végtelen ciklusok miatt. A végrehajtás késleltetései megakadályozzák, hogy a program megfagyjon.

## Kezdőknek
Lehet, hogy már kipróbáltad több `harvest()` hívás egymás után rakását:

`harvest()
harvest()
harvest()`

Ez lehetővé teszi, hogy többször takaríts be egy program futás alatt.
Azonban jó lenne háromnál többször betakarítani, és ugyanazt a kódot többször írni rossz gyakorlat.
A megoldás a ciklus.
Egy ciklus lehetővé teszi, hogy ugyanazt a kódot többször futtatsd.

A while ciklus egy feltételt vesz, ami egy logikai érték, ami csak két állapot egyikében lehet: `True` vagy `False`.
Ilyen értéket Boolean értéknek nevezünk.

A ciklus aztán végrehajtja a cikluson belüli kódot, amíg a feltétel False.
A while ciklus így néz ki:

`while condition:
	#ciklus törzse
	#ciklus törzse
	#...`
	
Ahol a "condition" helyére egy boolean értéket, és a `#ciklus törzse` helyére azt kell írnod, amit a ciklusban akarsz csinálni.

Két állandó boolean érték érhető el. Az állandók olyan értékek, amelyek soha nem változnak a program futása alatt.

Állandó `True` boolean érték létrehozásához egyszerűen írd le a `True`-t. Írd le a `False`-t állandó boolean értékként, ami mindig `False` lesz.
Tehát írhatod

`while False:
	do_a_flip()`

vagy

`while True:
	do_a_flip()`

Az első soha nem csinál flipet, a második pedig örökké flipel (végtelen ciklus).

Általában a végtelen ciklus létrehozása rossz ötlet, mert megfagyasztja a programot, de ebben a játékban késleltetések vannak a ciklus minden iterációja között, így a drón folyamatosan flipelni fog, amíg kézzel le nem állítod a végrehajtás gomb újbóli megnyomásával.

Figyeld meg, hogy a kettőspont utáni sor behúzva van. Az ilyen behúzás a kód blokkok elválasztására szolgál.
Nyomd meg a Tab-ot a behúzás hozzáadásához és Shift + Tab-et (vagy Backspace-t) az eltávolításához.

A ciklus megismétli az összes behúzott utasítást a kettőspont után.
A behúzott blokk utáni utasítások a ciklus befejezése után kerülnek végrehajtásra.