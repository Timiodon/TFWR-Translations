# Zewnętrzny Edytor
Wbudowany edytor tekstu zazwyczaj wystarcza do gry, ale oczywiście nie może się równać z bardziej zaawansowanymi edytorami tekstu, jak Visual Studio Code.

Gra zapisuje wszystkie pliki kodu jako pliki .py, więc możesz je edytować za pomocą edytorów Pythona.
Zwróć uwagę, że jest to tylko dla wygody. Język w grze nie jest tak naprawdę Pythonem, ale jest na tyle podobny, że Python IntelliSense działa na nim przyzwoicie.
Możesz znaleźć pliki w [folderze z zapisami](persistent_data_path/Saves).

Każdy zapis zawiera także plik `__builtins__.py`, który zawiera wbudowane definicje Pythona odpowiadające wbudowanym w grze, aby umożliwić IntelliSense.
VS Code potrafi automatycznie wykryć `__builtins__.py`, ale niektóre edytory mogą działać tylko, jeśli zrobisz `from __builtins__ import *`.

Aby zobaczyć zewnętrzne zmiany w grze bez konieczności ponownego ładowania zapisu, musisz włączyć opcję "File Watcher". Jeśli utworzysz lub usuniesz pliki zewnętrznie, nadal będziesz musiał załadować zapis ponownie, aby je zobaczyć.

## Korzystanie z VS Code
Visual Studio Code to zalecany edytor kodu do używania z The Farmer Was Replaced.

Możesz go zainstalować [tutaj](https://code.visualstudio.com/download).

Po pobraniu zainstaluj rozszerzenie Python w VS Code.

Gdy już je masz, otwórz [folder](persistent_data_path/Saves), który zawiera twoje pliki `.py` w VS Code. Upewnij się, że otwierasz cały folder, a nie tylko pojedyncze pliki, inaczej plik `__builtins__.py` nie będzie działał.

W grze upewnij się, że masz włączoną opcję "File Watcher". Teraz za każdym razem, gdy zapiszesz w VS Code, zmiany automatycznie pojawią się w grze.

I to wszystko! Teraz możesz pisać swój kod w profesjonalnym edytorze kodu!