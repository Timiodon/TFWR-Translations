# Harici Düzenleyici
Oyun içi metin düzenleyici genellikle bu oyunu oynamak için yeterlidir, ancak elbette Visual Studio Code gibi daha gelişmiş metin düzenleyicileriyle rekabet edemez.

Oyun tüm kod dosyalarını .py dosyaları olarak kaydeder, böylece onları Python düzenleyicileriyle düzenleyebilirsin. 
Bunun sadece kolaylık sağlamak için olduğunu unutma. Oyun içi dil aslında Python değildir, ancak Python IntelliSense'in üzerinde iyi çalışacak kadar yakındır.
Dosyaları [kayıt klasöründe](persistent_data_path/Saves) bulabilirsin.

Her kayıt ayrıca, IntelliSense'i etkinleştirmek için oyun içi yerleşiklerle eşleşen yerleşik Python tanımlarını içeren bir `__builtins__.py` dosyası içerir. 
VS Code, `__builtins__.py`'yi otomatik olarak algılayabilir, ancak bazı düzenleyiciler yalnızca `from __builtins__ import *` yaparsan çalışabilir.

Harici değişiklikleri kaydı yeniden yüklemek zorunda kalmadan oyun içinde görmek için, "File Watcher" seçeneğini etkinleştirmen gerekir. Harici olarak dosya oluşturur veya silersen, onları görmek için yine de kaydı yeniden yüklemen gerekir.

## VS Code Kullanımı
Visual Studio Code, The Farmer Was Replaced ile kullanılması önerilen kod düzenleyicisidir.

[Buradan](https://code.visualstudio.com/download) yükleyebilirsin.

İndirdikten sonra, VS Code'a Python uzantısını yükle.

Bunu yaptıktan sonra, VS Code'da `.py` dosyalarını tutan [klasörü](persistent_data_path/Saves) aç. Sadece tek tek dosyaları değil, tüm klasörü açtığından emin ol, aksi takdirde `__builtins__.py` dosyası çalışmaz.

Oyunda, "File Watcher" seçeneğinin açık olduğundan emin ol. Şimdi, VS Code'da her kaydettiğinde, değişiklikler otomatik olarak oyunda görünecektir.

İşte bu kadar! Artık kodunu profesyonel bir kod düzenleyicide yazabilirsin!