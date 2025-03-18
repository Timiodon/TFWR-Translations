# Hata Ayıklama
Bazen kodunuz çalışmaz ve nedenini bulmanız gerekir. Size yardımcı olacak birkaç araç var.

İlki, programı adım adım yürütmektir.  
Adım adım moda, Çalıştır butonunun yanındaki butonla veya bir breakpoint belirleyerek geçebilirsiniz.

Breakpoint'ler kodun solundaki breakpoint paneline tıklanarak eklenebilir.
![](Breakpoints227)
Yürütme, breakpoint'in bulunduğu satıra ulaştığında, otomatik olarak adım adım moda geçecektir.

Fareyi bir değişkenin üzerine getirdiğinizde, mevcut değeri görüntülenir.

`print()` fonksiyonu da çok faydalı olabilir. Kendisine iletilen herhangi bir değeri doğrudan havaya yazacaktır.

Örnekler:

"0.24" yazdır.
`print(0.24)`

"True" veya "False" yazdır.
`print(can_harvest())`

Mevcut konumu yazdır.
`print(get_pos_x(), get_pos_y())`

Print fonksiyonu, değeri doğrudan havaya ve [Çıktı](docs/output.md) sayfasına yazdırır.

Eğer çok sayıda değer yazdırmak istiyorsanız, havaya yazma biraz yavaş olabilir.  
Bu durumda sadece çıktı penceresine yazdıran `quick_print()` fonksiyonunu kullanabilirsiniz.

Çıktı penceresi ayrıca uyarıları ve hataları da kaydeder, bu yüzden bir şey beklenildiği gibi çalışmıyorsa, bunu kontrol etmek faydalı olabilir.

Yürütme durduğunda, çıktı aynı zamanda oyun klasöründeki output.txt dosyasına da yazılır. [output.txt](persistent_data_path/output.txt).