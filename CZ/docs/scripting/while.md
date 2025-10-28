# While Loop
Odemkl jsi smyčku `while` a hodnoty `True` a `False`. Smyčka `while` opakovaně provádí tělo smyčky tak dlouho, dokud je podmínka `True`.

`while condition:
	#loop body`

Nemusíš se bát vytvořit nekonečnou smyčku — zpoždění při provádění příkazů zabrání tomu, aby se program zasekl.

## Pro začátečníky
Možná jsi už zkusil napsat několik příkazů `harvest()` za sebou:

`harvest()
harvest()
harvest()`

To umožní sklidit několikrát v jednom běhu programu. 
Bylo by ale fajn sklízet víc než jen třikrát — a opakování stejného kódu několikrát za sebou je špatná praxe.
Řešením je smyčka.
Smyčka ti umožní spouštět stejný kód opakovaně.

Smyčka while používá podmínku, což je logická hodnota, která může mít pouze dva stavy: `True` nebo `False`. 
Taková hodnota se nazývá booleovská hodnota.

Smyčka pak provádí kód uvnitř sebe, dokud není podmínka False.
Smyčka while vypadá takto:

`while condition:
	#loop body
	#loop body
	#...`
	
Na místě slova condition musíš uvést booleovskou (logickou) podmínku, a na místě `#loop body` pak napsat příkazy, které se mají ve smyčce provádět.

Existují dvě konstantní booleovské hodnoty. Konstanty jsou hodnoty, které se během běhu programu nemění.

Pokud chceš vytvořit boolean hodnotu (tedy hodnotu typu pravda/nepravda), která je vždy `True`, jednoduše napiš `True`. Pokud chceš vytvořit hodnotu, která je vždy `False` napiš `False`.
Takže můžeš napsat například:

`while False:
	do_a_flip()`

nebo

`while True:
	do_a_flip()`

První příklad nikdy neudělá otočku, zatímco druhý bude dělat otočky neustále (nekonečná smyčka).

Normálně je vytvoření nekonečné smyčky špatný nápad, protože by program zamrzl.
Ale v této hře jsou mezi jednotlivými cykly smyčky malé prodlevy, takže dron bude pokračovat v otočkách, dokud program ručně nezastavíš opětovným stisknutím tlačítka pro spuštění.

Všimni si, že řádek za dvojtečkou je odsazený.
Takové odsazení se používá k oddělení bloků kódu.
Pro přidání odsazení stiskni Tab, a pro jeho odstranění Shift + Tab (nebo Backspace).

Smyčka zopakuje všechny příkazy s odsazením za dvojtečkou.
Příkazy, které následují až po skončení odsazeného bloku, se vykonají až po dokončení smyčky.
