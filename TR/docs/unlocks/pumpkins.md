# Balkabakları
[Balkabakları](objects/pumpkin) sürülmüş toprakta havuç gibi büyür. Onları ekmek havuç maliyetine sahiptir.

Bir karedeki tüm balkabakları tamamen büyüdüğünde, dev bir balkabağı oluşturmak için birleşirler. Maalesef, balkabaklarının tamamen büyüdükten sonra %20 ölme şansı vardır, bu yüzden birleşmelerini istiyorsan ölenleri yeniden ekmen gerekir. 

Bir balkabağı öldüğünde, arkasında hasat edildiğinde hiçbir şey düşürmeyecek ölü bir balkabağı bırakır. Yerine yeni bir bitki ekmek, ölü balkabağını otomatik olarak kaldırır, bu yüzden onu hasat etmeye gerek yoktur. `can_harvest()` ölü balkabaklarında her zaman `False` döndürür.

Dev bir balkabağının verimi, balkabağının boyutuna bağlıdır.

1x1 bir balkabağı `1*1*1 = 1` balkabağı verir.
2x2 bir balkabağı `4` yerine `2*2*2 = 8` balkabağı verir.
3x3 bir balkabağı `9` yerine `3*3*3 = 27` balkabağı verir.
4x4 bir balkabağı `16` yerine `4*4*4 = 64` balkabağı verir.
5x5 bir balkabağı `25` yerine `5*5*5 = 125` balkabağı verir.
Bir `n`x`n` balkabağı `n >= 6` için `n*n*6` balkabağı verir.

Tam çarpanı elde etmek için en az 6x6 boyutunda balkabakları elde etmek iyi bir fikirdir. 

Bu, bir karedeki her karoya bir balkabağı eksen bile, balkabaklarından birinin ölebileceği ve mega balkabağının büyümesini engelleyebileceği anlamına gelir.
