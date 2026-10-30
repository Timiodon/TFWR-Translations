# Harici Düzenleyici
Oyunu oynamak için oyun içi metin düzenleyici genellikle yeterlidir, ama elbette Visual Studio Code gibi daha gelişmiş metin düzenleyicilerle boy ölçüşemez.

Oyun tüm kod dosyalarını .py dosyaları olarak kaydeder, bu yüzden onları Python düzenleyicileriyle düzenleyebilirsin.
Bunun yalnızca kolaylık olsun diye sunulduğunu unutma. Oyun içi dil aslında Python değildir, ama Python IntelliSense'in üzerinde gayet iyi çalışacağı kadar ona yakındır.
Dosyaları [kayıt klasöründe](persistent_data_path/Saves) bulabilirsin.

Kalıcı veri klasörünün konumu:

- Windows: `%USERPROFILE%\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced`
- macOS: `~/Library/Application Support/com.TheFarmerWasReplaced.TheFarmerWasReplaced`
- Linux (Steam/Proton): `~/.steam/steam/steamapps/compatdata/2060160/pfx/drive_c/users/steamuser/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced`

Her kayıtta ayrıca bir `__builtins__.py` dosyası bulunur. Bu dosya, IntelliSense'i etkinleştirmek için oyun içi yerleşik öğelerle eşleşen yerleşik Python tanımlarını içerir.
VS Code `__builtins__.py` dosyasını otomatik olarak algılayabilir, ancak bazı düzenleyiciler yalnızca `from __builtins__ import *` satırını eklersen çalışabilir.

Kaydı yeniden yüklemek zorunda kalmadan harici değişiklikleri oyunda görmek için "Dosya İzleyici" seçeneğini etkinleştirmelisin. Dosyaları oyun dışında oluşturur veya silersen, onları görmek için yine de kaydı yeniden yüklemen gerekir.

## VS Code Kullanımı
The Farmer Was Replaced ile kullanmak için önerilen kod düzenleyici Visual Studio Code'dur.

[Buradan](https://code.visualstudio.com/download) yükleyebilirsin.

İndirdikten sonra VS Code'a Python eklentisini yükle.

Bunu yaptıktan sonra, `.py` dosyalarının bulunduğu [klasörü](persistent_data_path/Saves) VS Code'da aç. Tek tek dosyaları değil, klasörün tamamını açtığından emin ol; aksi takdirde `__builtins__.py` dosyası çalışmaz.

Oyunda "Dosya İzleyici" seçeneğinin açık olduğundan emin ol. Artık VS Code'da her kaydettiğinde değişiklikler otomatik olarak oyunda görünecek.

İşte bu kadar! Artık kodunu profesyonel bir kod düzenleyicide yazabilirsin!

---

[İlk Program](docs/first_program.md)      [Yedekleri Yükleme](docs/backup.md)
