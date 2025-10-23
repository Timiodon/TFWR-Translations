# Funkce
Použij klíčové slovo `def` pro definici nové funkce:
`def f(arg1, arg2 = False):
	#function code`

Funkci můžeš zavolat pomocí závorek `()`:
`f(42)`

Viz také [Scopes](docs/scripting/scopes.md) pro vysvětlení lokálních a globálních proměnných ve funkcích.

## Úvod
Už jsi viděl vestavěné funkce jako `harvest()`.  
Můžeš si ale také definovat vlastní funkce, které ti umožní strukturovat kód modulárně. V podstatě tím pojmenuješ blok kódu, který můžeš volat odkudkoli.

## Definice funkcí
Například můžeš definovat funkci, která několikrát posune dron.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Klíčové slovo `def` říká, že jde o definici funkce.  
`move_n_dir` je název, pod kterým bude funkce uložena. Může to být libovolný platný název proměnné a bude se používat k volání funkce.  
`n` a `dir` jsou parametry – proměnné, které uchovávají hodnoty předané funkci (tyto hodnoty se také nazývají argumenty).  
Do definice funkce můžeš přidat libovolný počet parametrů. Za : následuje blok kódu, který se spustí při volání funkce.

Pomocí výše uvedené definice následující kód posune dron `10` polí `na sever` a `2` pole `na západ`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Když vidíš `def function():`, můžeš si to představit jako přiřazení proměnné:
`function = create_new_function_object()`
Stejně jako u každého přiřazení, nemůžeš proměnnou použít dřív, než je vytvořena!  
Příkaz `def` se musí vykonat dřív, než se funkce zavolá.  
Tento kód vyvolá chybu:

`func()
def func():
	pass`

## Návratové hodnoty
Pomocí klíčového slova `return` může funkce vracet hodnotu. Například následující funkce definuje operaci výlučného OR.  
Výsledek je `True`, pokud je jedna hodnota `True` a druhá `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) umožňují vracet více hodnot najednou.

## Výchozí argumenty
Můžeš také přiřadit výchozí hodnoty, které se použijí, pokud nejsou argumenty předány.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Argument s výchozí hodnotou nemůže být následován argumentem, který výchozí hodnotu nemá.

## Pokročilé použití funkcí
Funkce jsou hodnoty stejně jako jiné proměnné. Příkaz `def` funguje jako přiřazení – přiřadí funkci názvu, který jí dáš.  
To umožňuje dělat například toto:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Zde `f()` zavolá funkci `f`, která vytvoří a vrátí novou funkci `d`. Druhé `()` pak spustí tuto vrácenou funkci a provede přemet.  
(Tento styl psaní se obvykle nedoporučuje, protože se v něm těžko orientuje.)

Funkce, které přijímají jiné funkce jako argumenty, ti umožní být opravdu kreativní:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Tento kód posune dron `na sever` 10× a poté použije hnojivo 10×.