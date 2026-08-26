# Függvények
A `def` kulcsszó használatával definiálhatsz új függvényt:
`def f(arg1, arg2 = False):
	#függvény kód`

A hívás operátorral `()` meghívhatod a függvényt:
`f(42)`

Lásd még: [Scopes](docs/scripting/scopes.md), hogy megismerd a lokális és globális változókat a függvényekben.

## Bevezetés
Már láttad a beépített függvényeket, mint a `harvest()`.
Saját függvényeket is definiálhatsz, ami lehetővé teszi a kód moduláris struktúrázását. Lényegében lehetővé teszi, hogy nevet adj egy kód blokknak, hogy bárhonnan meghívhasd.

## Függvény definíciók
Például definiálhatsz egy függvényt, ami a drónt többször mozgatja.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

A `def` kulcsszó jelzi, hogy ez egy függvény definíció.
A `move_n_dir` az a név, amihez a függvény kötődik. Ez bármilyen érvényes változónév lehet, és ez használatos a függvény meghívására.
A `n` és `dir` paraméterek. Ezek változók, amelyek a függvénybe átadott értékeket tárolják (ezeket az értékeket argumentumoknak is hívják). Annyi paramétert adhatsz egy függvény definícióhoz, amennyit akarsz.
A `:` után a kód blokk következik, ami a függvény meghívásakor fog futni.

A fenti definícióval a következő kód `10` csempével mozgatja a drónt `North` irányba és `2` csempével `West` irányba.

`move_n_dir(10, North)
move_n_dir(2, West)`

Amikor látod a `def function():`-t, gondolj igazából úgy rá, mint egy változó értékadásra:
`function = create_new_function_object()`
Mint minden értékadásnál, a változót sem használhatod, mielőtt értéket kapott volna!
A `def` utasításnak a függvényhívások előtt kell futnia!
Ez a kód hibát fog dobni:

`func()
def func():
	pass`

## Visszatérési értékek
A `return` kulcsszó használatával a függvény visszaadhat egy értéket.
Például a következő függvény az exclusive or műveletet definiálja. Az exclusive or `True`-t ad vissza, ha az egyik érték `True` és a másik `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

A [tuple-ök](docs/scripting/tuples.md) lehetővé teszik több érték visszaadását.

## Alapértelmezett argumentumok
Alapértelmezett értékeket is hozzárendelhetsz, amik akkor használatosak, ha nem adnak át argumentumot.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Egy argumentum, ami alapértelmezett értékkel rendelkezik, nem követheti argumentum, ami nem rendelkezik alapértelmezett értékkel.

## Haladó függvény használat
A függvények értékek, mint bármely más érték, és a `def` utasítás csak úgy viselkedik, mint egy értékadás, hozzárendelve a függvényt ahhoz a névhez, amit adsz neki.
Ez lehetővé teszi ilyesmiket:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Itt az `f()` meghívja a `f` függvényt, ami definiálja és visszaadja az új `d` függvényt. A második `()` aztán végrehajtja a visszaadott függvényt és flipet csinál.
( Az ilyesmi általában nem jó ötlet, mert nehéz látni, mi történik)

Függvények, amik más függvényeket argumentumként vesznek, igazán kreatív dolgokra képesek:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ez a kód a drónt `North` irányba mozgatja 10-szer, majd 10-szer használ műtrágyát.