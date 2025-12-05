# Break
`break` umožňuje předčasně ukončit cyklus. Když program narazí na příkaz `break`, okamžitě opustí nejvnitřnější cyklus a pokračuje kódem za ním.

`for i in range(10):
	break
print(i)`
Tento kód vypíše `0`, protože `i` má při první iteraci hodnotu `0` a poté se cyklus ukončí příkazem `break`.

Funguje to i pro cykly `while`.

`while True:
	if can_harvest():
		break`

Tento kód spouští cyklus `while`, dokud není `can_harvest()` rovno `True`.  
Má stejný efekt jako:

`while not can_harvest():
	pass`

U vnořených cyklů příkaz `break` vždy ukončí pouze ten nejvnitřnější cyklus.

`for i in range(10):
	for j in range(10):
		break
		print("tohle se nikdy nevypíše")
      	        print("tohle se vypíše 10×")`