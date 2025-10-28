# Proměnné
Proměnné si můžeš představit jako pojmenované kontejnery, které uchovávají hodnotu.  
Operátor `=` se používá k deklaraci proměnné a uložení hodnoty do ní.

`variable_name = value`

Levá strana operátoru je název proměnné. Můžeš jí dát libovolné jméno.  
Pravá strana je výraz, jehož výsledná hodnota se uloží do proměnné.

Deklaruj proměnnou s názvem `a` a ulož do ní hodnotu `5`:  
`a = 5`  
Deklaruj proměnnou s názvem `b` a ulož do ní návratovou hodnotu funkce `can_harvest()`:  
`b = can_harvest()`

Nepleť si operátor `=` s operátorem `==`.  
Operátor `==` kontroluje, zda jsou dvě hodnoty stejné, a vrací `True` nebo `False`.  
Operátor `=` přiřazuje hodnotu na pravé straně názvu na levé straně.

Po přiřazení můžeš proměnnou v kódu použít pro získání uložené hodnoty.

`a = 5
for i in range(a):
	do_a_flip()`

Tento cyklus se provede 5×, protože `a` má hodnotu `5`.  
Proměnná `i` v cyklu `for` je také proměnná, které je při každé iteraci automaticky přiřazena aktuální hodnota z posloupnosti. (Nemusí se jmenovat `i`, může mít jakýkoli platný název.)

Proměnné můžeš použít i ve smyčce `while`:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Tento kód dělá totéž co cyklus `for` výše, jen zde musíme proměnnou `i` zvyšovat ručně.  
Abychom ji zvýšili, nastavíme ji na její současnou hodnotu plus `1`. Změna hodnoty proměnné na základě její předchozí hodnoty je běžná věc.  
Dá se zkrátit pomocí těchto operátorů: `+=, -=, *=, /=, %=`

`i = i + 1` je totéž jako `i += 1`  
`a = a / 3` je totéž jako `a /= 3`
