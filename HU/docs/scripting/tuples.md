# Tuple-ök
A tuple-ök nagyszerű módja több érték egyetlen értékké kombinálásának.
Tuple létrehozásához egyszerűen válaszd el az értékeket vesszővelel:

`tuple = 1, 2`

Vissza is csomagolhatod őket több változóba. Az alábbi kódban a `(1,2)` tuple-t két változóba, `a`-ba és `b`-be csomagoljuk vissza.

`a, b = 1, 2`

A tuple-ök indexelhetők, mint a listák, de megváltoztathatatlanok és nem változtathatók meg létrehozás után.

`tuple = 1, 2`

`print(tuple[1])`
kiírja a `2`-t

`tuple[0] = 3`
hibát dob
<unlock=dicts>
A listákkal ellentétben a tuple-ök szótárakban kulcsként használhatók.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
kiírja a `(4,5)`-t</unlock>

Hasznosak lehetnek több érték visszaadására egy függvényből.

`def f():
    return 1, 2

a, b = f()`