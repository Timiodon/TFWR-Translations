# Amélioration de vitesse
La vitesse d'exécution a été doublée. Le problème est que le drone récolte maintenant plus vite que l'herbe ne peut pousser, ce qui n'entraîne aucune récolte. Pour gérer cela, les branchements [if](docs/scripting/if.md) et la fonction [can_harvest](functions/can_harvest) sont maintenant débloqués.

## Vérifier avant de récolter
Jusqu'à présent, on n'avait que `True` et `False` comme conditions, ce qui n'est bien sûr pas très utile avec `if`.

La nouvelle fonction can_harvest() fournit une meilleure condition. `can_harvest()` retourne `True` si la plante sous le drone peut être récoltée et `False` sinon.

`if can_harvest():
	#faire quelque chose`

La raison pour laquelle tu peux utiliser cette fonction comme condition est qu'elle retourne une valeur booléenne.

Une valeur de retour signifie essentiellement qu'après l'exécution de la fonctionnalité, l'expression d'appel de fonction s'évalue à la valeur retournée.

Voici ce qui se passe lorsque le code ci-dessus s'exécute :
	-le if s'exécute
	-`can_harvest()` est appelée
	-`can_harvest()` fait son travail
	-`can_harvest()` retourne `True` ou `False`
	-l'instruction est maintenant `if True:` ou `if False:`
	-le bloc de code n'est exécuté que si la récolte est possible

Maintenant, on peut utiliser `if` pour empêcher le drone de récolter trop tôt.