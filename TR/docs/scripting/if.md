# If
Kodu koşullu olarak çalıştırmak için if, elif ve else kullanabilirsin.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntax
`if`'ler, yalnızca bir koşul `True` ise kod çalıştırmana olanak tanır. Döngü yapmayan bir `while` döngüsü gibidirler.
`if`, `while` döngüsü gibi bir koşul alır ve koşul `True` olarak değerlendirilirse if kod bloğunu çalıştırır:

`#koşul True ise takla at
if condition:
	do_a_flip()`

Ayrıca, if'ten sonra koşul `False` olarak değerlendirilirse çalıştırılacak kodu tanımlayan bir `else` ekleyebilirsin.

Eğer `condition` True ise takla at, aksi halde hasat et.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif`, else if'in kısaltmasıdır.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

şöyle kısaltılabilir:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
