# Proměnné
Proměnné si lze představit jako pojmenované kontejnery, které mohou uchovávat hodnotu.
Operátor `=` se používá k deklaraci proměnné a uložení hodnoty do ní.

`variable_name = value`

Levá strana operátoru je název proměnné. Můžete jí dát jakýkoli název chcete.
Pravá strana je výraz, jehož výsledná hodnota bude uložena v proměnné.

Deklarujte proměnnou s názvem `a` a uložte do ní hodnotu `5`:
`a = 5`
Deklarujte proměnnou s názvem `b` a uložte do ní návratovou hodnotu `can_harvest()`:
`b = can_harvest()`

Nepleťte si operátor `=` s operátorem `==`. 
Operátor `==` kontroluje, zda jsou dvě hodnoty stejné, a vrací `True` nebo `False`.
Operátor `=` přiřazuje hodnotu vpravo názvu vlevo.

Po přiřazení proměnné ji můžete použít v kódu k získání hodnoty, kterou obsahuje

`a = 5
for i in range(a):
	do_a_flip()`

Výše uvedený cyklus se provede 5krát, protože `a` je nastaveno na `5`.
`i` v cyklu `for` je také proměnná, které je automaticky přiřazena aktuální hodnota sekvence při každé iteraci cyklu. (Nemusí se jmenovat `i`, můžete jí dát jakýkoli platný název proměnné.)

Proměnné vám také umožňují dělat totéž s cyklem while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

To dělá totéž co cyklus for výše. Jen musíme i inkrementovat ručně.
Všimněte si, že pro inkrementaci i jej nastavíme na jeho vlastní hodnotu plus `1`. Změna hodnoty proměnné na základě její předchozí hodnoty je velmi běžná věc. 
Lze to zkrátit pomocí těchto operátorů: `+=, -=, *=, /=, %=`

`i = i + 1` je stejné jako `i += 1`
`a = a / 3` je stejné jako `a /= 3`
