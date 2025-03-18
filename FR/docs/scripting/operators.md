# Opérateurs
opérateurs arithmétiques : `+, -, *, /, //, %, **`
opérateurs de comparaison : `==, !=, <=, >=, <, >`
opérateurs logiques : `not, and, or`

Note : Tous les nombres dans le jeu sont des nombres en virgule flottante. Donc tous les opérateurs arithmétiques sont des opérateurs en virgule flottante.
`//` est défini pour simplement tronquer le nombre après la division.

Pour les opérateurs d'affectation, tu dois débloquer le déblocage "Variables".

## Introduction
Les opérateurs te permettent de comparer, modifier et combiner des valeurs.
Les opérateurs arithmétiques `+, -, *, /, //, %, **` sont utilisés pour effectuer des opérations mathématiques courantes sur des nombres.
Les opérateurs de comparaison `==, !=, <=, >=, <, >` sont utilisés pour comparer des valeurs. Le résultat est toujours soit `True` soit `False`.
Les opérateurs logiques (aussi appelés opérateurs booléens) `not, and, or` sont utilisés pour combiner des valeurs de vérité.

## Opérateurs Arithmétiques
`+` et `-` sont utilisés pour l'addition et la soustraction.

`2 + 3` évalue à `5`
`3 - 2` évalue à `1`

`*`, `/` et `//` sont utilisés pour la multiplication et la division.

`2 * 3` évalue à `6`
`5 / 2` évalue à `2.5`

`//` fait la même chose que `/` mais le résultat est tronqué (arrondi à l'entier inférieur).

`5 // 2` évalue à `2`

`%` est l'opérateur modulo, aussi connu comme l'opérateur de reste. Il divise essentiellement les deux nombres puis renvoie le reste. On peut aussi le voir comme la soustraction répétée du nombre de droite au nombre de gauche jusqu'à ce que le reste soit inférieur au nombre de droite.

`4 % 2` évalue à `0`
`5 % 2` évalue à `1`
`6 % 2` évalue à `0`
`2 % 6` évalue à `2`
`1.5 % 1` évalue à `0.5`

`**` est l'opérateur puissance.

`2**2` évalue à `4`
`(-5)**3` évalue à `-125`

## Opérateurs de Comparaison
`==` et `!=` sont utilisés pour vérifier si deux valeurs sont "égales"(`==`) ou "différentes"(`!=`). Ils peuvent être utilisés sur tous types de valeurs.

`2 == 2` évalue à `True`
`Entities.Bush != Entities.Bush` évalue à `False`
`3 != 3 + 1` évalue à `True`

`<=, >=, <, >` peuvent seulement être utilisés sur des nombres. Ils vérifient si le nombre de gauche est "plus petit ou égal"(`<=`), "plus grand ou égal"(`>=`), "plus petit" (`<`) ou "plus grand" (`>`) que le nombre de droite.

`1 <= 1` évalue à `True`
`2 >= 3` évalue à `False`
`-2 < -1` évalue à `True`
`6 > 6` évalue à `False`

## Opérateurs Logiques
`not` inverse simplement la valeur :

`not False` évalue à `True`
`not True` évalue à `False`

`and` évalue à `True` seulement si les deux valeurs sont `True`

`True and True` évalue à `True`
`True and False` évalue à `False`
`False and False` évalue à `False`

`or` évalue à `True` si au moins une des valeurs est `True`

`True or True` évalue à `True`
`True or False` évalue à `True`
`False or False` évalue à `False`