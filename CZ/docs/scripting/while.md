# Smyčka `while`
Odemkli jste smyčku `while` a hodnoty `True` a `False`. Smyčka `while` opakuje tělo smyčky, dokud je podmínka `True`.

`while condition:
	#tělo smyčky`

Nebojte se vytvářet nekonečné smyčky — mezi iteracemi jsou pauzy, takže program nezamrzne.

## Pro začátečníky
Možná jste zkoušeli zavolat `harvest()` několikrát za sebou:

`harvest()
harvest()
harvest()`

To umožní sbírat vícekrát během jednoho spuštění. Nicméně je lepší použít smyčku, pokud chcete opakovat vícekrát.

Smyčka `while` bere podmínku, což je logická hodnota buď `True` nebo `False`.

Potom provádí kód uvnitř smyčky, dokud je podmínka `True`.

```
while condition:
	#tělo smyčky
	#tělo smyčky
	#...
```

Nahraďte `condition` logickou podmínkou a `#tělo smyčky` tím, co chcete provádět.

Jsou dostupné dvě konstantní booleovské hodnoty: `True` a `False`.

```
while False:
	do_a_flip()

while True:
	do_a_flip()
```

První smyčka nikdy nic nevykoná, druhá poběží navěky (nekonečná smyčka). Ve hře to způsobí, že dron bude opakovat činost, dokud manuálně stisknete Execute znovu.

Všimněte si odsazení za dvojtečkou — odsazení odděluje bloky kódu. Pro odsazení použijte `Tab`, pro odstranění `Shift+Tab` nebo `Backspace`.

Všechny odsazené příkazy budou opakovány; příkazy mimo odsazený blok se vykonají až po skončení smyčky.