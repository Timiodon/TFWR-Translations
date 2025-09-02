# Fonctions
Utilise le mot-clé `def` pour définir une nouvelle fonction :
`def f(arg1, arg2 = False):
	#code de la fonction`

Tu peux utiliser l'opérateur d'appel `()` pour appeler la fonction :
`f(42)`

Voir aussi [Portées](docs/scripting/scopes.md) pour en apprendre davantage sur les variables locales et globales dans les fonctions.

## Introduction
Tu as déjà vu des fonctions intégrées comme `harvest()`.
Tu peux aussi définir tes propres fonctions, ce qui te permet de structurer ton code de manière modulaire. En gros, cela te permet de donner un nom à un bloc de code pour pouvoir l'appeler de n'importe où.

## Définitions de Fonctions
Par exemple, tu pourrais définir une fonction qui déplace le drone plusieurs fois.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Le mot-clé `def` signale qu'il s'agit d'une définition de fonction.
`move_n_dir` est le nom auquel la fonction est liée. Ce peut être n'importe quel nom de variable valide et sera utilisé pour appeler la fonction.
`n` et `dir` sont des paramètres. Ce sont des variables qui contiennent les valeurs passées à la fonction (ces valeurs sont aussi appelées arguments). Tu peux ajouter autant de paramètres que tu veux à une définition de fonction.
Après le `:`, vient le bloc de code qui s'exécutera lorsque la fonction est appelée.

Avec la définition ci-dessus, le code suivant déplace alors le drone de `10` cases vers le `North` et `2` cases vers l'`West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quand tu vois `def function():`, tu devrais vraiment y penser comme à une affectation de variable comme ceci :
`function = create_new_function_object()`
Comme pour toutes les affectations, tu ne peux pas utiliser la variable avant qu'elle n'ait été affectée !
L'instruction `def` doit être exécutée avant tout appel de fonction.
Ce code lèvera une erreur :

`func()
def func():
	pass`

## Valeurs de Retour
Utilise le mot-clé `return` pour qu'une fonction renvoie une valeur.
Par exemple, la fonction suivante définit l'opération "ou exclusif". Le "ou exclusif" renvoie `True` si une valeur est `True` et l'autre est `False` :

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Les [Tuples](docs/scripting/tuples.md) permettent de renvoyer plusieurs valeurs.

## Arguments par Défaut
Tu peux aussi assigner des valeurs par défaut qui seront utilisées si aucun argument n'est passé.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argument qui a une valeur par défaut ne peut pas être suivi d'un argument qui n'en a pas.

## Utilisation Avancée des Fonctions
Les fonctions sont des valeurs comme les autres, et l'instruction `def` agit simplement comme une instruction d'affectation, assignant la fonction au nom que tu lui donnes.
Cela permet de faire des choses comme ceci :

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Ici, `f()` appelle la fonction `f` qui définit et renvoie une nouvelle fonction `d`. Le second `()` exécute ensuite la fonction renvoyée et effectue un looping.
(Faire ce genre de choses n'est généralement pas une bonne idée car il est difficile de voir ce qui se passe)

Les fonctions qui prennent d'autres fonctions en arguments te permettent d'être vraiment créatif :

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ce code déplace le drone 10 fois vers le `North` puis utilise de l'engrais 10 fois.