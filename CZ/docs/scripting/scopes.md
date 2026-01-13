# Rozsahy názvů (Scopes)
Rozsahy určují, ke kterým proměnným lze odkud přistupovat. Rozsah je v podstatě mapování z názvů na hodnoty.
Fungují v podstatě stejně jako v Pythonu.

Existuje globální rozsah a každá funkce má lokální rozsah.
Když definujete proměnnou, přidá se do aktuálního rozsahu.
Cokoli mimo definici funkce je považováno za součást globálního rozsahu.

`x = 1`
Přiřadí hodnotu `1` názvu `x` v globálním rozsahu.

Tento příkaz `def` přiřadí funkci názvu `f` v globálním rozsahu.
`def f():
    `Přiřadí hodnotu `1` názvu `y` v lokálním rozsahu `f`.`
    y = 1

    `Přiřadí funkci názvu `g` v lokálním rozsahu `f`.`
    def g():
        pass`

`f()`
Získá funkci uloženou v `f` z globálního rozsahu a zavolá ji.

`print(y)`
Tento příkaz print v globálním rozsahu vyvolá chybu, protože `y` nebylo nikdy deklarováno v globálním rozsahu, takže ho zde nemůžeme číst.
Existovalo pouze v lokálním rozsahu `f`.

## Klíčové slovo global
Ve výchozím nastavení se všechny proměnné ve funkcích vážou k lokálnímu rozsahu, i když proměnná se stejným názvem existuje v globálním rozsahu.

`x = 0

def f():
    x = 1
f()
print(x)`

Tento kód vypíše `0`, protože lokální `x` uvnitř `f` není stejná proměnná jako globální `x`, takže globální `x` zůstává nezměněno. To je důležité, protože jinak by volání funkce mohlo omylem přepsat globální proměnnou, která má náhodou stejný název jako lokální proměnná této funkce.

Pokud chcete zapisovat do globální proměnné, musíte tak učinit explicitně pomocí klíčového slova `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

V tomto příkladu `global x` váže `x` ke globální proměnné `x` definované nad ní. Toto nyní vypíše `1`.
Pamatujte, že změna globálních proměnných je obvykle prvním krokem ke "špagetovému kódu", kde každá část programu ovlivňuje každou jinou část programu, takže to nepřehánějte.

## Cykly a větvení
Cykly a větvení nevytvářejí své vlastní rozsahy, takže cokoli deklarované v nich lze stále používat i vně.

`for i in range(3):
    pass
print(i)`

Toto vypíše `2`, protože poslední iterace cyklu `for` přiřadila `2` do `i`.