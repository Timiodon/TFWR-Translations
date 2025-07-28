# Debug
Bazen kodun çalışmaz ve nedenini bulman gerekir. Bunu yapmana yardımcı olacak birkaç araç var.

İlki, programı adım adım yürütmektir. 
Yürüt düğmesinin yanındaki düğmeyle veya bir breakpoint ayarlayarak adım adım moduna geçebilirsin.

Breakpoint'ler, kodun solundaki breakpoint paneline tıklanarak eklenebilir.
![](Breakpoints227)
Yürütme, breakpoint'in olduğu satıra ulaştığında, otomatik olarak adım adım moduna geçer.

Fareni bir değişkenin üzerine getirdiğinde, mevcut değeri görüntülenir.

`print()` fonksiyonu da çok yararlı olabilir. Kendisine geçirilen herhangi bir değeri doğrudan havaya yazdıracaktır.

Örnekler:

"0.24" yazdır.
`print(0.24)`

"True" veya "False" yazdır.
`print(can_harvest())`

Mevcut konumu yazdır.
`print(get_pos_x(), get_pos_y())`

Print fonksiyonu, değeri doğrudan havaya ve [Çıktı](docs/output.md) sayfasına yazdırır.

Çok sayıda değer yazdırmak istiyorsan havaya yazmak bazen biraz yavaş olabilir.
Bu durumda, yalnızca çıktı penceresine yazdıran `quick_print()` fonksiyonunu kullanabilirsin.

Çıktı penceresi ayrıca uyarıları ve error'ları da kaydeder, bu yüzden bir şey beklendiği gibi çalışmazsa orayı kontrol etmek faydalı olabilir.

Yürütme durduğunda, çıktı ayrıca oyun klasöründeki output.txt dosyasına da yazılır. [output.txt](persistent_data_path/output.txt).