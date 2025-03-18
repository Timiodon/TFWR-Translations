# Harici Editör
Oyun içindeki metin editörü genellikle bu oyunu oynamak için yeterlidir, ancak elbette Visual Studio Code gibi daha gelişmiş metin editörleriyle yarışamaz.

Oyun tüm kod dosyalarını .py dosyaları olarak kaydeder, bu yüzden bunları Python editörleri ile düzenleyebilirsiniz.
Bunun sadece bir kolaylık sağlamak için olduğunu unutmayın. Oyun içi dil aslında Python değil, ama yeterince yakındır ki Python IntelliSense'i üzerinde iyi çalışır.
Dosyaları [kayıt klasöründe](persistent_data_path/Saves) bulabilirsiniz.

Her kayıt ayrıca, oyun içi yerleşikleri etkinleştirmek için eşleşen yerleşik Python tanımlarını içeren bir `__builtins__.py` dosyasını da içerir.
VS Code `__builtins__.py`'yi otomatik olarak algılayabilir, ancak bazı editörler ancak `from __builtins__ import *` yaptığınızda çalışabilir.

Kaydı yeniden yüklemeden oyun içindeki dış değişiklikleri görmek için "File Watcher" seçeneğini etkinleştirmeniz gerekiyor. Dışarıdan dosya oluşturduğunuzda veya sildiğinizde, onları görebilmek için kaydı yine de yeniden yüklemeniz gerekecek.

## VS Code Kullanımı
The Farmer Was Replaced ile kullanılacak önerilen kod editörü Visual Studio Code'dur.

[Buradan](https://code.visualstudio.com/download) yükleyebilirsiniz.

İndirdikten sonra, VS Code içine Python uzantısını yükleyin.

Bunu yaptıktan sonra, `.py` dosyalarınızı tutan [klasörü](persistent_data_path/Saves) VS Code'da açın. Tüm klasörü açtığınızdan emin olun, sadece tekil dosyaları değil; aksi takdirde `__builtins__.py` dosyası çalışmaz.

Oyunda, "File Watcher" seçeneğinin açık olduğundan emin olun. Şimdi, her zaman VS Code'da kaydettiğinizde, değişiklikler otomatik olarak oyunda görünecek.

Hepsi bu! Artık kodunuzu profesyonel bir kod editöründe yazabilirsiniz!