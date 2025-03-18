# Fonctions
Utilisez le mot-clé `def` pour définir une nouvelle fonction :
`def f(arg1, arg2 = False):
	#code de la fonction`

Vous pouvez utiliser l'opérateur d'appel `()` pour appeler la fonction :
`f(42)`

Voir aussi [Scopes](docs/scripting/scopes.md) pour en savoir plus sur les variables locales et globales dans les fonctions.

## Introduction
Vous avez déjà vu des fonctions intégrées comme `harvest()`.
Vous pouvez aussi définir vos propres fonctions, ce qui permet de structurer votre code de manière modulaire. Ça vous permet en gros de donner un nom à un bloc de code pour l'appeler où vous le voulez.

## Définitions de Fonction
Par exemple, vous pouvez définir une fonction qui déplace le drone plusieurs fois.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Le mot-clé `def` indique qu'il s'agit d'une définition de fonction.
`move_n_dir` est le nom auquel la fonction est liée. Cela peut être n'importe quel nom de variable valide et sera utilisé pour appeler la fonction.
`n` et `dir` sont des paramètres. Ce sont des variables qui contiennent les valeurs passées à la fonction (Ces valeurs sont aussi appelées arguments). Vous pouvez ajouter autant de paramètres que vous le souhaitez à une définition de fonction.
Après le `:` vient le bloc de code qui sera exécuté lorsque la fonction est appelée.

Avec la définition ci-dessus, le code suivant déplace le drone de `10` cases vers le `North` et de `2` cases vers l' `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quand vous voyez `def function():` vous devriez vraiment le concevoir comme une affectation de variable comme ceci :
`function = create_new_function_object()`
Comme pour toutes les affectations, vous ne pouvez pas utiliser la variable avant qu'elle ne soit affectée !
L'instruction `def` doit être exécutée avant tout appel de fonction.
Ce code générera une erreur :

`func()
def func():
	pass`

## Valeurs de Retour
Utilisez le mot-clé `return` pour faire retourner une valeur par une fonction.
Par exemple, la fonction suivante définit l'opération ou exclusif. L'ou exclusif retourne `True` si une valeur est `True` et l'autre est `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) permettent de retourner plusieurs valeurs.

## Arguments par Défaut
Vous pouvez aussi assigner des valeurs par défaut qui seront utilisées si aucun argument n'est passé.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argument ayant une valeur par défaut ne peut pas être suivi par un argument qui n'a pas de valeur par défaut.

## Utilisation Avancée des Fonctions
Les fonctions sont des valeurs comme toutes les autres valeurs, et l'instruction `def` fonctionne simplement comme une instruction d'affectation, assignant la fonction au nom que vous lui donnez.
Cela permet de faire des choses comme ceci :

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Ici `f()` appelle la fonction `f` qui définit et retourne une nouvelle fonction `d`. Le second `()` exécute ensuite la fonction retournée et effectue un flip.
(Faire ce genre de choses n'est généralement pas une bonne idée car c'est difficile à suivre)

Les fonctions qui prennent d'autres fonctions comme arguments vous permettent d'être vraiment créatif :

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ce code déplace le drone vers le `North` 10 fois puis utilise le fertilisant 10 fois.