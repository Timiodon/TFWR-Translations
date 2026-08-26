# If
Az if, elif és else használatával feltételesen futtathatsz kódot.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Szintaxis
Az `if` lehetővé teszi, hogy kódot csak akkor futtass, ha valamilyen feltétel `True`. Úgy működik, mint egy `while` ciklus, csak nem ismétel.
Az `if` egy feltételt vesz, csakúgy, mint a `while` ciklus, és végrehajtja az if kód blokkját, ha a feltétel `True`-ra értékelődik:

`#flipet csinál, ha a feltétel True
if condition:
	do_a_flip()`

Hozzáadhatsz egy `else`-t is az if után, ami a feltétel `False`-ra értékelődése esetén végrehajtandó kódot definiál.

Flipet csinál, ha `condition` True, különben takaríts be.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` az "else if" rövidítése.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

Rövidíthető erre:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`