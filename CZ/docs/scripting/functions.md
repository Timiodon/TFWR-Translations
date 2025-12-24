# Funkce
Použijte klíčové slovo `def` pro definici nové funkce:
`def f(arg1, arg2 = False):
    #kód funkce`

Funkci pak zavoláte pomocí závorek:
`f(42)`

Viz také [Prostory názvů](docs/scripting/scopes.md) pro informace o lokálních a globálních proměnných.

## Úvod
Vestavěné funkce jako `harvest()` už znáte. Můžete si také definovat vlastní funkce a strukturovat tak kód modulárně.

## Definice funkcí
Příklad funkce, která několikrát posune dron:

`def move_n_dir(n, dir):
    for i in range(n):
        move(dir)`

`def` označuje definici funkce. `move_n_dir` je jméno, pod kterým je funkce dostupná. `n` a `dir` jsou parametry — proměnné, které drží předané argumenty.
Po dvojtečce následuje blok kódu, který se vykoná při volání funkce.

S výše uvedenou definicí:
`move_n_dir(10, North)
move_n_dir(2, West)`

Definici funkce lze chápat jako přiřazení hodnoty funkce do proměnné:
`function = create_new_function_object()`
Proto nemůžete funkci použít dříve, než je přiřazena — `def` musí být provedeno před voláním.

## Návratové hodnoty
Pomocí `return` může funkce vrátit hodnotu.

`def xor(a, b):
    return a != b

if xor(True, False):
    do_a_flip()`

Více hodnot lze vrátit pomocí [N-tic](docs/scripting/tuples.md).

## Výchozí argumenty
Argumenty mohou mít výchozí hodnoty, které se použijí, pokud nejsou při volání poskytnuty.

`def f(a = False):
    if a:
        do_a_flip()

f()

f(True)`

Argument s výchozí hodnotou nesmí být následován argumentem bez výchozí hodnoty.

## Pokročilejší použití
Funkce jsou hodnoty jako jiné proměnné a `def` funguje jako přiřazení, takže můžete vracet a předávat funkce jako hodnoty.

`def f():
    def d():
        do_a_flip()
    return d

f()()`

Funkce mohou také jako argumenty přijímat jiné funkce:

`def f(g, arg):
    for _ in range(10):
        g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Tento kód posune dron 10× na sever a poté 10× použije hnojivo.