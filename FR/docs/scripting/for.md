# Boucle For
La boucle `for` fonctionne comme en Python. (Appelée boucle foreach dans certains langages, à ne pas confondre avec la boucle for de style C, qui est une chose différente).

`for i in sequence:
	#faire quelque chose avec i`

Similaire à la boucle `while`, la boucle `for` appelle également à plusieurs reprises un bloc de code. Au lieu de boucler en fonction d'une condition, elle exécute le corps de la boucle une fois pour chaque élément d'une séquence.

## Syntaxe
Une boucle for ressemble à ceci :

`for nom_variable in sequence:
	#bloc de code`

`nom_variable` peut être n'importe quel nom que vous choisissez. C'est une variable qui stocke l'élément actuel de la séquence. `sequence` doit être une valeur qui peut être itérée comme une plage ou des nombres. Le bloc de code est exécuté pour chaque élément avec la variable de boucle assignée à cet élément.

## Séquences
[Plages](functions/range)      <unlock=lists>[Listes](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionnaires](docs/scripting/dicts.md)      </unlock><unlock=sets>[Ensembles](docs/scripting/sets.md)</unlock>

## Exemple
`for i in range(5):
    harvest()`

Cette boucle exécute le corps un nombre fixe de fois. C'est essentiellement la même chose que d'écrire

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Donc, elle appelle `harvest()` 5 fois.

Voir aussi [Break](docs/scripting/break.md) et [Continue](docs/scripting/continue.md)