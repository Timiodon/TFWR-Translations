# Fonctions
Utilisez le mot-clé `def` pour définir une nouvelle fonction :
`def f(arg1, arg2 = False):
	#code de la fonction`

Vous pouvez utiliser l'opérateur d'appel `()` pour appeler la fonction :
`f(42)`

Voir aussi [Portées (Scopes)](docs/scripting/scopes.md) pour en savoir plus sur les variables locales et globales dans les fonctions.

## Introduction
Vous avez déjà vu des fonctions intégrées comme `harvest()`.
Vous pouvez également définir vos propres fonctions, ce qui permet de structurer votre code de manière modulaire. Cela vous permet essentiellement de donner un nom à un bloc de code pour pouvoir l'appeler de n'importe où.

## Définitions de fonctions
Par exemple, vous pourriez définir une fonction qui déplace le drone plusieurs fois.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Le mot-clé `def` signale qu'il s'agit d'une définition de fonction.
`move_n_dir` est le nom auquel la fonction est liée. Ce peut être n'importe quel nom de variable valide et sera utilisé pour appeler la fonction.
`n` et `dir` sont des paramètres. Ce sont des variables qui contiennent les valeurs passées à la fonction (ces valeurs sont aussi appelées arguments). Vous pouvez ajouter autant de paramètres que vous le souhaitez à une définition de fonction.
Après le `:` vient le bloc de code qui s'exécutera lorsque la fonction sera appelée.

Avec la définition ci-dessus, le code suivant déplace alors le drone de `10` cases vers le `North` et de `2` cases vers l' `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quand vous voyez `def function():`, vous devriez vraiment y penser comme une assignation de variable comme ceci :
`function = create_new_function_object()`
Comme pour toutes les assignations, vous ne pouvez pas utiliser la variable avant qu'elle ait été assignée !
L'instruction `def` doit s'exécuter avant tout appel de fonction.
Ce code lèvera une erreur :

`func()
def func():
	pass`

## Valeurs de retour
Utilisez le mot-clé `return` pour qu'une fonction retourne une valeur.
Par exemple, la fonction suivante définit l'opération ou exclusif. Le ou exclusif retourne `True` si une valeur est `True` et l'autre est `False` :

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Les [Tuples](docs/scripting/tuples.md) permettent de retourner plusieurs valeurs.

## Arguments par défaut
Vous pouvez également assigner des valeurs par défaut qui seront utilisées si aucun argument n'est passé.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argument qui a une valeur par défaut ne peut pas être suivi par un argument qui n'a pas de valeur par défaut.

## Utilisation avancée des fonctions
Les fonctions sont des valeurs comme n'importe quelle autre valeur, et l'instruction `def` agit simplement comme une instruction d'assignation, assignant la fonction au nom que vous lui donnez.
Cela permet de faire des choses comme ça :

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Ici `f()` appelle la fonction `f` qui définit et retourne une nouvelle fonction `d`. Le second `()` exécute alors la fonction retournée et effectue un flip.
(Faire ce genre de choses n'est généralement pas une bonne idée car il est difficile de voir ce qui se passe)

Les fonctions qui prennent d'autres fonctions comme arguments vous permettent d'être vraiment créatif :

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ce code déplace le drone 10 fois vers le `North` puis utilise de l'engrais 10 fois.