# Import
Vkládání veškerého kódu do jednoho souboru se rychle stane nezvladatelným. 
Příkazy `import` vám umožňují importovat funkce a globální proměnné z jiného souboru.
Jak to funguje na jednom obrázku:
![](ImportsInOnePicture400)

Zde `import module2` spustí soubor s názvem `module2` a zpřístupní vám všechny jeho globální proměnné.
K proměnným a funkcím v importovaném modulu pak můžete přistupovat pomocí operátoru `.`.
Takže v tomto příkladu `module2.print_x()` zavolá `print_x()` v `module2`.

### Není třeba číst dále

Globální proměnné z importovaného modulu můžete také přesunout do aktuálního rozsahu (scope), kde je příkaz importu spuštěn, pomocí syntaxe `from`.

`from module2 import print_x
print_x()`
Importuje pouze specifikované globální proměnné z `module2`.

nebo

`from module2 import *
print_x()`
Importuje všechny globální proměnné z `module2`.

Tím se také importuje soubor `module2`, ale místo přístupu k němu přes proměnnou s názvem `module2` se globální proměnné z `module2` rozbalí a přiřadí přímo do lokálního rozsahu.

Tato forma importu se obvykle nedoporučuje, protože nefunguje dobře, když se dva soubory importují navzájem, a můžete omylem přepsat proměnné v importujícím souboru kvůli kolizím názvů. Je bezpečnější se syntaxi `from` vyhnout, pokud nevíte přesně, co děláte.

# Jak to doopravdy funguje

## TLDR (Ve zkratce)
Importy mohou být docela neintuitivní, ale většině problémů se lze vyhnout tím, že se budete držet syntaxe `import file` místo `from file import` a zabalíte vše, co není definicí globální proměnné, do
`if __name__ == "__main__":`

## Vedlejší efekty importu
Při prvním importu souboru se provede celý soubor a poté získáte přístup ke všem proměnným, které byly během provádění definovány.
Pokud stejný soubor importujete znovu, vrátí se pouze uložený modul z prvního importu.

To znamená, že příkazy importu mohou mít vedlejší efekty. Pokud importujete soubor, který volá `harvest()`, skutečně se během importu provede sklizeň. Ale když jej importujete znovu, sklizeň se znovu neprovede, protože soubor se spouští pouze jednou.

Těmto vedlejším efektům se lze vyhnout pomocí proměnné `__name__`. Jedná se o proměnnou, která je automaticky nastavena na `"__main__"`, když je soubor spuštěn přímo, a na název souboru, když je soubor spuštěn přes `import`.
Považuje se za dobrou praxi umístit jakýkoli kód, který nechcete spouštět při importu souboru, do bloku `if __name__ == "__main__":`.

Běžnou strukturou souborů v Pythonu je umístit kód, který by se měl provést při spuštění souboru, do funkce `main()`. Tím získáte jasné rozlišení mezi lokálními proměnnými (definovanými uvnitř `main()`) a globálními proměnnými, které lze importovat (definovanými mimo `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Cyklické importy
Co se stane, když soubor `a` importuje soubor `b` a soubor `b` importuje soubor `a`?

soubor `a`:
`import b
x = 0`

soubor `b`:
`import a
def f():
    print(a.x)`

To bude fungovat v pořádku. Řekněme, že ani jeden ze dvou souborů ještě není načten a někdo jiný provede `import a`.

-`a` běží až k řádku `import b`.
-`b` běží až k řádku `import a`.
-Modul `a` již existuje, ale neobsahuje `x`, protože dosáhl pouze řádku `import b`.
-`b` uloží odkaz na napůl načtený modul `a` do proměnné s názvem `a`.
-`b` provede příkaz `def` a uloží funkci `f()`.
-`a` pokračuje v běhu a inicializuje `x`.

Když někdo zavolá `b.f()`, správně vypíše `0`, protože modul `a`, na který má `b` odkaz, je nyní plně načten.

Nyní zvažte stejný kód pomocí syntaxe `from`.

soubor `a`:
`from b import *
x = 0`

soubor `b`:
`from a import *
def f():
    print(x)`

-`a` běží až k řádku `from b import *`.
-`b` běží až k řádku `from a import *`.
-Modul `a` již existuje, ale ještě nebyl plně proveden.
-`b` rozbalí vše, co je aktuálně v `a`, do svého vlastního globálního rozsahu. V tomto okamžiku `a` neobsahuje nic, protože ještě nedosáhl řádku `x = 0`, takže se nic neimportuje.
-`b` provede příkaz `def` a uloží funkci `f()`.
-`a` pokračuje v běhu a inicializuje `x`.

Pokud nyní někdo zavolá `b.f()`, dostane chybu, že `x` v aktuálním rozsahu neexistuje. Je to proto, že tentokrát `b` nemá odkaz na stále se načítající `a` a nevidí definice, které byly přidány po importu.