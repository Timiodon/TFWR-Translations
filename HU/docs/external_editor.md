# Külső szerkesztő
A játékon belüli szövegszerkesztő általában elegendő a játékhoz, de persze nem versenyezhet komolyabb szövegszerkesztőkkel, mint a Visual Studio Code.

A játék minden kódfájlt .py fájlként ment, így Python szerkesztőkkel szerkesztheted őket.
Figyelj arra, hogy ez csak kényelmi célokat szolgál. A játékon belüli nyelv valójában nem Python, de elég közel van ahhoz, hogy a Python IntelliSensedecensen működjön rajta.
A fájlokat a [mentési mappában](persistent_data_path/Saves) találod.

Minden mentés tartalmaz egy `__builtins__.py` fájlt is, ami a beépített Python definíciókat tartalmazza, amelyek megfelelnek a játékon belüli beépítetteknek, hogy az IntelliSense működjön.
A VS Code képes automatikusan felismerni a `__builtins__.py`-t, de néhány szerkesztő csak akkor működik, ha `from __builtins__ import *`-ot írsz.

Ahhoz, hogy a külső változtatásokat a játékban lásd újratöltés nélkül, be kell kapcsolnod a "Fájl figyelő" opciót. Ha fájlokat hozol létre vagy törlöl kívülről, még mindig újra kell töltened a mentést, hogy lásd őket.

## VS Code használata
A Visual Studio Code az ajánlott kódszerkesztő a The Farmer Was Replaced-hez.

Telepítheted [itt](https://code.visualstudio.com/download).

Letöltés után telepítsd a Python bővítményt a VS Code-ban.

Ha ez megvan, nyisd meg a `.py` fájljaidat tartalmazó [mappát](persistent_data_path/Saves) a VS Code-ban. Ügyelj arra, hogy a teljes mappát nyisd meg, ne csak az egyes fájlokat, különben a `__builtins__.py` nem fog működni.

A játékban győződj meg róla, hogy a "Fájl figyelő" opció be van kapcsolva. Most, minden alkalommal, amikor a VS Code-ban mentessz, a változtatások automatikusan megjelennek a játékban.

Ennyi az egész! Most már professzionális kódszerkesztőben írhatod a kódod!