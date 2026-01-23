# Externí Editory
Vestavěný textový editor ve hře obvykle stačí pro hraní, ale samozřejmě se nemůže rovnat pokročilým editorům, jako je Visual Studio Code.

Hra ukládá všechny soubory s kódem jako .py soubory, takže je můžeš upravovat v editorech pro Python.
Pamatuj však, že je to pouze pro usnadnění – jazyk ve hře není skutečný Python, ale je mu dost podobný, aby na něm Python IntelliSense fungoval poměrně dobře.
Soubory najdeš ve složce [save folder](persistent_data_path/Saves).

Každý save také obsahuje soubor `__builtins__.py` který obsahuje definice vestavěných funkcí Pythonu odpovídající těm herním, aby IntelliSense fungoval správně. 
VS Code dokáže soubor `__builtins__.py` rozpoznat automaticky, ale některé editory mohou vyžadovat, abys přidal příkaz `from __builtins__ import *`.

Chceš-li ve hře vidět změny provedené mimo ni bez nutnosti znovu načítat uloženou pozici, musíš zapnout možnost „File Watcher“. Pokud ale vytváříš nebo mažeš soubory mimo hru, bude i tak nutné uloženou hru znovu načíst, aby se změny projevily.

## Použití VS Code
Visual Studio Code je doporučený editor pro práci s hrou The Farmer Was Replaced.

Můžeš si jej stáhnout [zde](https://code.visualstudio.com/download).

Po instalaci do VS Code přidej rozšíření Python.

Poté otevři ve VS Code složku [folder](persistent_data_path/Saves) která obsahuje tvoje `.py` soubory. Ujisti se, že otevíráš celou složku, nikoliv jen jednotlivé soubory – jinak nebude fungovat soubor `__builtins__.py`.

Ve hře se ujisti, že máš zapnutou možnost „File Watcher“. Nyní se po každém uložení souboru ve VS Code změny automaticky projeví i ve hře.

A to je vše! Teď můžeš psát svůj kód v profesionálním editoru!