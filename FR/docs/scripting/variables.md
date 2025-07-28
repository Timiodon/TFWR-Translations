# Variables
Les variables peuvent être considérées comme des conteneurs nommés qui peuvent contenir une valeur.
L'opérateur `=` est utilisé pour déclarer une variable et y stocker une valeur.

`variable_name = value`

Le côté gauche de l'opérateur est le nom de la variable. Vous pouvez lui donner n'importe quel nom que vous voulez.
Le côté droit est une expression dont la valeur résultante sera stockée dans la variable.

Déclare une variable nommée `a` et y stocke la valeur `5` :
`a = 5`
Déclare une variable nommée `b` et y stocke la valeur de retour de `can_harvest()` :
`b = can_harvest()`

Ne confondez pas l'opérateur `=` avec l'opérateur `==`.
L'opérateur `==` vérifie si deux valeurs sont égales et retourne `True` ou `False`.
L'opérateur `=` assigne la valeur de droite au nom de gauche.

Après qu'une variable a été assignée, vous pouvez l'utiliser dans le code pour récupérer la valeur qu'elle contient

`a = 5
for i in range(a):
	do_a_flip()`

La boucle ci-dessus est exécutée 5 fois car `a` est défini sur `5`.
Le `i` dans la boucle `for` est également une variable qui est automatiquement assignée à la valeur actuelle de la séquence à chaque itération de la boucle. (Il n'est pas nécessaire de l'appeler `i`, vous pouvez lui donner n'importe quel nom de variable valide.)

Les variables vous permettent également de faire la même chose avec une boucle while :

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Cela fait la même chose que la boucle for ci-dessus. Nous devons juste incrémenter i manuellement.
Notez que pour incrémenter i, nous le définissons comme sa propre valeur plus `1`. Changer la valeur d'une variable en fonction de sa valeur précédente est quelque chose de très courant.
Cela peut être abrégé en utilisant ces opérateurs : `+=, -=, *=, /=, %=`

`i = i + 1` est la même chose que `i += 1`
`a = a / 3` est la même chose que `a /= 3`