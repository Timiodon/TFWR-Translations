# Externí editor
Vestavěný editor textu ve hře většinou stačí pro hraní, ale samozřejmě se nemůže rovnat pokročilejším editorům jako Visual Studio Code.

Hra ukládá všechny soubory s kódem jako `.py`, takže je můžete upravovat v Python editorech.
Upozornění: jde jen o pohodlí — vestavěný jazyk hry není přesně Python, ale je natolik podobný, že v něm funguje IntelliSense Pythonu docela dobře.
Soubory najdete ve [složce se savy](persistent_data_path/Saves).

Každé save obsahuje také soubor `__builtins__.py`, který obsahuje vestavěné definice odpovídající herním vestavěným funkcím, aby fungovalo IntelliSense.
VS Code `__builtins__.py` obvykle detekuje automaticky, některé editory však mohou vyžadovat `from __builtins__ import *`.

Abyste viděli změny provedené externě přímo ve hře bez načítání save, zapněte volbu „File Watcher“. Pokud externě vytvoříte nebo smažete soubory, budete i tak muset reloadovat save, aby se projevily v UI.

## Použití VS Code
Visual Studio Code je doporučený editor k používání s The Farmer Was Replaced.

Můžete si ho stáhnout [zde](https://code.visualstudio.com/download).

Po instalaci nainstalujte ve VS Code rozšíření Python.

Poté otevřete ve VS Code složku, která obsahuje vaše `.py` soubory (viz [persistent_data_path/Saves]). Ujistěte se, že otevřete celou složku, ne jen jednotlivé soubory; jinak `__builtins__.py` nebude fungovat správně.

Ve hře mějte zapnutou volbu „File Watcher“. Teď se při každém uložení ve VS Code změny automaticky projeví ve hře.

To je vše! Nyní můžete psát kód v profesionálním editoru.