# Opérateurs
opérateurs arithmétiques : `+, -, *, /, //, %, **`
opérateurs de comparaison : `==, !=, <=, >=, <, >`
opérateurs booléens : `not, and, or`

Note : Tous les nombres dans le jeu sont des nombres à virgule flottante. Donc, tous les opérateurs arithmétiques sont des opérateurs à virgule flottante.
`//` est défini pour simplement arrondir à l'inférieur le nombre après la division.

Pour les opérateurs d'assignation, vous devez débloquer le déblocage "Variables".

## Introduction
Les opérateurs vous permettent de comparer, modifier et combiner des valeurs.
Les opérateurs arithmétiques `+, -, *, /, //, %, **` sont utilisés pour effectuer des opérations mathématiques courantes sur les nombres.
Les opérateurs de comparaison `==, !=, <=, >=, <, >` sont utilisés pour comparer des valeurs. Le résultat est toujours soit `True` soit `False`.
Les opérateurs logiques (aussi appelés opérateurs booléens) `not, and, or` sont utilisés pour combiner des valeurs de vérité.

## Opérateurs arithmétiques
`+` et `-` sont utilisés pour l'addition et la soustraction.

`2 + 3` s'évalue à `5`
`3 - 2` s'évalue à `1`

`*`, `/` et `//` sont utilisés pour la multiplication et la division.

`2 * 3` s'évalue à `6`
`5 / 2` s'évalue à `2.5`

`//` fait la même chose que `/` mais le résultat est arrondi à l'inférieur (arrondi à l'entier inférieur le plus proche).

`5 // 2` s'évalue à `2`

`%` est l'opérateur modulo, aussi connu comme l'opérateur de reste. Il divise essentiellement les deux nombres puis retourne le reste. Vous pouvez aussi y penser comme soustrayant répétitivement le nombre de droite du nombre de gauche jusqu'à ce que le reste soit inférieur au nombre de droite.

`4 % 2` s'évalue à `0`
`5 % 2` s'évalue à `1`
`6 % 2` s'évalue à `0`
`2 % 6` s'évalue à `2`
`1.5 % 1` s'évalue à `0.5`

`**` est l'opérateur de puissance.

`2**2` s'évalue à `4`
`(-5)**3` s'évalue à `-125`

## Opérateurs de comparaison
`==` et `!=` sont utilisés pour vérifier si deux valeurs sont "égales"(`==`) ou "non égales"(`!=`). Ils peuvent être utilisés sur tous les types de valeurs.

`2 == 2` s'évalue à `True`
`Entities.Bush != Entities.Bush` s'évalue à `False`
`3 != 3 + 1` s'évalue à `True`

`<=, >=, <, >` ne peuvent être utilisés que sur des nombres. Ils vérifient si le nombre de gauche est "plus petit ou égal"(`<=`), "plus grand ou égal"(`>=`), "plus petit" (`<`) ou "plus grand" (`>`) que le nombre de droite.

`1 <= 1` s'évalue à `True`
`2 >= 3` s'évalue à `False`
`-2 < -1` s'évalue à `True`
`6 > 6` s'évalue à `False`

## Opérateurs logiques
`not` inverse simplement la valeur :

`not False` s'évalue à `True`
`not True` s'évalue à `False`

`and` s'évalue à `True` seulement si les deux valeurs sont `True`

`True and True` s'évalue à `True`
`True and False` s'évalue à `False`
`False and False` s'évalue à `False`

`or` s'évalue à `True` si au moins une des valeurs est `True`

`True or True` s'évalue à `True`
`True or False` s'évalue à `True`
`False or False` s'évalue à `False`