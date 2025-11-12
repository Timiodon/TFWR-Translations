# Name Scopes
Rozsahy (scopes) určují, odkud lze přistupovat k jednotlivým proměnným. Scope je v podstatě mapa, která přiřazuje názvy k hodnotám.  
Fungují v podstatě stejně jako v Pythonu.

Existuje globální scope a každý blok funkce má svůj lokální scope.  
Když definuješ proměnnou, přidá se do aktuálního scope.  
Vše mimo definici funkce je považováno za součást globálního scope.

`x = 1`
Přiřadí hodnotu `1` názvu `x` v globálním scope.

Tento příkaz `def` přiřadí funkci názvu `f` v globálním scope.  
`def f():
    `Přiřadí hodnotu `1` názvu `y` v lokálním scope funkce `f`.`
    y = 1

    `Přiřadí funkci názvu `g` v lokálním scope funkce `f`.`
    def g():
        pass`

`f()`
Získá funkci uloženou v `f` z globálního scope a zavolá ji.

`print(y)`
Tento příkaz `print` v globálním scope vyvolá chybu, protože `y` nebyla nikdy deklarována v globálním scope, takže k ní nelze přistoupit.  
Existovala pouze v lokálním scope funkce `f`.

## Klíčové slovo global
Ve výchozím nastavení se všechny proměnné ve funkcích vážou k lokálnímu scope, i když proměnná se stejným názvem existuje i v globálním scope.

`x = 0

def f():
    x = 1
f()
print(x)`

Tento kód vypíše `0`, protože lokální `x` uvnitř `f` není stejná proměnná jako globální `x`. Globální `x` tedy zůstane beze změny. To je důležité, protože jinak by funkce mohla omylem přepsat globální proměnnou, která má shodný název s lokální proměnnou.

Pokud chceš zapisovat do globální proměnné, musíš to udělat výslovně pomocí klíčového slova `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

V tomto příkladu `global x` sváže `x` s globální proměnnou `x` definovanou výše. Tento kód tedy vypíše `1`.  
Měj ale na paměti, že měnit globální proměnné bývá prvním krokem ke „špagetovému kódu“, kde každá část programu ovlivňuje všechny ostatní. Používej to s rozvahou.

## Smyčky a větvení
Smyčky a podmínky nevytvářejí vlastní scope, takže proměnné definované uvnitř lze použít i mimo ně.

`for i in range(3):
    pass
print(i)`

Tento kód vypíše `2`, protože poslední průchod cyklu `for` přiřadil `2` proměnné `i`.