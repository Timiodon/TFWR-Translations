# Edytor zewnętrzny
Wbudowany edytor tekstu jest zazwyczaj wystarczający do gry, ale oczywiście nie może konkurować z bardziej zaawansowanymi edytorami tekstu, takimi jak Visual Studio Code.

Gra zapisuje wszystkie pliki z kodem jako pliki .py, więc możesz je edytować za pomocą edytorów Pythona.
Zauważ, że jest to tylko dla wygody. Język w grze nie jest w rzeczywistości Pythonem, ale jest na tyle bliski, że IntelliSense Pythona działa na nim całkiem dobrze.
Pliki można znaleźć w [folderze zapisu](persistent_data_path/Saves).

Każdy zapis zawiera również plik `__builtins__.py`, który zawiera wbudowane definicje Pythona pasujące do wbudowanych funkcji w grze, aby umożliwić działanie IntelliSense.
VS Code jest w stanie automatycznie wykryć `__builtins__.py`, ale niektóre edytory mogą działać tylko po wykonaniu `from __builtins__ import *`.

Aby zobaczyć zewnętrzne zmiany w grze bez konieczności ponownego wczytywania zapisu, musisz włączyć opcję „File Watcher”. Jeśli tworzysz lub usuwasz pliki zewnętrznie, nadal będziesz musiał ponownie wczytać zapis, aby je zobaczyć.

## Używanie VS Code
Visual Studio Code jest zalecanym edytorem kodu do użytku z The Farmer Was Replaced.

Możesz go zainstalować [tutaj](https://code.visualstudio.com/download).

Po pobraniu zainstaluj rozszerzenie Pythona w VS Code.

Gdy to zrobisz, otwórz [folder](persistent_data_path/Saves), w którym znajdują się twoje pliki `.py`, w VS Code. Upewnij się, że otwierasz cały folder, a nie tylko pojedyncze pliki, w przeciwnym razie plik `__builtins__.py` nie będzie działał.

W grze upewnij się, że masz włączoną opcję „File Watcher”. Teraz za każdym razem, gdy zapiszesz w VS Code, zmiany automatycznie pojawią się w grze.

To wszystko! Teraz możesz pisać swój kod w profesjonalnym edytorze kodu!