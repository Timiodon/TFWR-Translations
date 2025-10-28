# Import
Dávat veškerý kód do jednoho souboru se rychle stane nepřehledným.  
Příkaz `import` umožňuje importovat funkce a globální proměnné z jiného souboru.  
Jak to funguje na jednom obrázku:  
![](ImportsInOnePicture400)

Zde `import module2` spustí soubor s názvem `module2` a poskytne přístup ke všem jeho globálním proměnným.  
K proměnným a funkcím v importovaném modulu se pak dostaneš pomocí operátoru `.`  
V tomto příkladu tedy `module2.print_x()` volá funkci `print_x()` v souboru `module2`.

### Není nutné číst dál

Můžeš také přesunout globální proměnné z importovaného modulu do aktuálního prostoru, kde se příkaz `import` provádí, pomocí syntaxe `from`.

`from module2 import print_x
print_x()`
Importuje pouze zadané globální proměnné z `module2`.

nebo

`from module2 import *
print_x()`
Importuje všechny globální proměnné z `module2`.

Tím se také importuje soubor `module2`, ale místo přístupu přes proměnnou `module2` se jeho globální proměnné rozbalí a přiřadí přímo do lokálního prostoru.

Tento způsob importu se obvykle nedoporučuje, protože nefunguje dobře, když dva soubory importují navzájem, a může dojít k nechtěnému přepsání proměnných kvůli kolizi názvů. Pokud si nejsi jistý, je bezpečnější se vyhnout syntaxi `from`.

# Jak to ve skutečnosti funguje

## TLDR
Importy mohou být někdy neintuitivní, ale většinu problémů lze předejít tím, že se budeš držet syntaxe `import file` místo `from file import` a vše, co není globální definicí, obalíš do bloku  
`if __name__ == "__main__":`

## Vedlejší efekty importu
Při prvním importu souboru se provede celý jeho obsah a zpřístupní se všechny proměnné, které byly při tom vytvořeny.  
Při opětovném importu stejného souboru se vrátí uložený modul z prvního načtení.

To znamená, že import může mít vedlejší efekty. Pokud importuješ soubor, který volá `harvest()`, skutečně dojde ke sklizni už při importu. Při dalším importu se to už nestane, protože soubor se spustí pouze jednou.

Těmto efektům se dá předejít pomocí proměnné `__name__`. Tato proměnná se automaticky nastaví na `"__main__"`, pokud se soubor spouští přímo, a na název souboru, pokud se spouští přes `import`.  
Je považováno za dobrou praxi umístit jakýkoliv kód, který se nemá spustit při importu, do bloku `if __name__ == "__main__":`.

Běžná struktura souboru v Pythonu vypadá tak, že kód, který se má spustit při přímém spuštění, je vložen do funkce `main()`. Tím se oddělí lokální proměnné (definované uvnitř `main()`) od globálních proměnných, které lze importovat (definovaných mimo `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Cyklické importy
Co se stane, pokud soubor `a` importuje soubor `b` a soubor `b` importuje `a`?

file `a`:
`import b
x = 0`

file `b`:
`import a
def f():
    print(a.x)`

Toto bude fungovat správně. Předpokládejme, že žádný z těchto souborů ještě není načten, a někdo spustí `import a`.

- `a` se začne provádět až po řádek `import b`.  
- `b` se začne provádět až po řádek `import a`.  
- Modul `a` už existuje, ale zatím neobsahuje `x`, protože se dostal jen po řádek `import b`.  
- `b` uloží referenci na částečně načtený modul `a` do proměnné `a`.  
- `b` provede příkaz `def` a uloží funkci `f()`.  
- `a` pokračuje v provádění a inicializuje `x`.

Když někdo zavolá `b.f()`, správně se vypíše `0`, protože modul `a`, na který `b` odkazuje, je nyní plně načten.

Nyní si představ stejný kód se syntaxí `from`.

file `a`:
`from b import *
x = 0`

file `b`:
`from a import *
def f():
    print(x)`

- `a` se začne provádět po řádek `from b import *`.  
- `b` se začne provádět po řádek `from a import *`.  
- Modul `a` už existuje, ale ještě není plně proveden.  
- `b` rozbalí všechny aktuálně existující položky z `a` do svého globálního prostoru.  
  V této chvíli `a` ještě neobsahuje nic, protože se nedostal k řádku `x = 0`, takže se nic nenaimportuje.  
- `b` provede příkaz `def` a uloží funkci `f()`.  
- `a` pokračuje v provádění a inicializuje `x`.

Pokud teď někdo zavolá `b.f()`, dojde k chybě, že `x` neexistuje v aktuálním prostoru. Je to proto, že tentokrát `b` nemá referenci na modul `a`, který se stále načítá, a nevidí definice, které byly přidány až po importu.