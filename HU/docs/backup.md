# Biztonsági mentések betöltése
Sajnos néha a mentési fájl megsérülhet, vagy elveszíthetsz néhány kódfájlt. Ha ez veled történik, megpróbálhatsz betölteni egy biztonsági mentést. Ha ez rendszeresen megtörténik, próbáld kikapcsolni a Steam Cloud-ot.

Minden alkalommal készül egy biztonsági mentés, amikor a játék mentésre kerül, és néhány biztonsági mentés megmarad, arra az esetre, ha vissza kell állítanod valamit.
Ezek a biztonsági mentések megtalálhatók a [backup könyvtárban](persistent_data_path/Backup). A [mentési könyvtár](persistent_data_path/Saves) mentéseinek másolatai.
A biztonsági mentés betöltésének legegyszerűbb módja, ha a betölteni kívánt biztonsági mentés mappáját bemásolod a mentési könyvtárba.

Egy mentés egy mappa, ami egy `save.json` fájlt és egy csomó `.py` fájlt tartalmaz.
Ha csak néhány kódfájlt vesztettél el, vagy a kódfájlok még ott vannak, de a `save.json` fájl sérült, a sérült részeket a biztonsági mentés megfelelő fájljaival is kicserélheted.