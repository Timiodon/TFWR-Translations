# Continue
`continue` umožňuje přeskočit aktuální iteraci cyklu a přejít rovnou na další průchod nejvnitřnějšího cyklu.

`for i in range(10):
	continue
    print("tohle se nikdy nevypíše")`

Tento kód provede všech `10` iterací cyklu, ale příkaz `print` za `continue` se vždy přeskočí.

Funguje to i u cyklů `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Tento kód volá `harvest()` pouze tehdy, když je `can_harvest()` rovno `True`.  
Má stejný efekt jako:

`while True:
	if can_harvest():
		harvest()`

U vnořených cyklů příkaz `continue` vždy ovlivňuje pouze ten nejvnitřnější cyklus.

`for i in range(10):
	for j in range(10):
	    print("tohle se vypíše 100×")
		continue
		print("tohle se nikdy nevypíše")
	print("tohle se vypíše 10×")`