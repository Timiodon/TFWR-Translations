# If
Kodunuzu koşullu olarak çalıştırmak için if, elif ve else kullanabilirsiniz.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Söz Dizimi
`if`ler, kodunuzu sadece bazı koşullar `True` olduğunda çalıştırmanıza olanak tanır. Bir `while` döngüsü gibidirler ama döngü yapmazlar.
`if`, tıpkı bir `while` döngüsü gibi bir koşul alır ve koşul `True` olarak değerlendirilirse if kod bloğunu çalıştırır:

`# Koşul True ise do_a_flip yap
if condition:
	do_a_flip()`

Koşul `False` olarak değerlendirilirse çalışacak kodu tanımlayan bir `else` de if'in sonuna ekleyebilirsiniz.

Koşul `True` ise do_a_flip yap, aksi takdirde harvest.

`if condition:
	do_a_flip()
else:
	harvest()`

`elif` else if'in kısaltmasıdır.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

şu şekilde kısaltılabilir:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`