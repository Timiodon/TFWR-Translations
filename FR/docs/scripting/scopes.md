# Nommage des Scopes

Les scopes déterminent quelles variables peuvent être accédées depuis où. Un scope est en gros une association de noms à des valeurs. Ils fonctionnent de manière similaire à Python.

Il y a un scope global, et chaque fonction possède un scope local. Quand tu définis une variable, elle est ajoutée au scope actuel. Tout ce qui se trouve en dehors d'une définition de fonction est considéré comme faisant partie du scope global.

`x = 1` Attribue une valeur de `1` au nom `x` dans le scope global.

Cette déclaration `def` assigne une fonction au nom `f` dans le scope global. `def f(): ` Assigne une valeur de `1` au nom `y` dans le scope local de `f`.` y = 1 ` Assigne une fonction au nom `g` dans le scope local de `f`.` def g(): pass`

`f()` Récupère la fonction stockée dans `f` depuis le scope global et l'appelle.

`print(y)` Cette instruction print dans le scope global génère une erreur parce que `y` n'a jamais été déclarée dans le scope global donc on ne peut pas la lire ici. Elle existait seulement dans le scope local de `f`.

## Le mot-clé global

Par défaut, toutes les variables dans les fonctions se lient au scope local, même si une variable du même nom existe dans le scope global.

`x == 0

def f():
    x = 1
f()
print(x)`

Ce code affiche `0` car le `x` local à l'intérieur de `f` n'est pas la même variable que le `x` global, donc le `x` global reste inchangé. C'est important parce qu'autrement un appel de fonction pourrait accidentellement remplacer une variable globale qui aurait simplement le même nom qu'une variable locale de cette fonction.

Si tu veux écrire sur une variable globale, tu dois le faire explicitement en utilisant le mot-clé `global`.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

Dans cet exemple, `global x` lie `x` à la variable globale `x` définie au-dessus. Ceci affichera maintenant `1`. Note que changer les variables globales est généralement le premier pas vers du code spaghetti, où chaque partie du programme affecte toutes les autres parties du programme, donc ne l'utilise pas trop.

## Boucles et branches

Les boucles et les branches ne créent pas leurs propres scopes, donc tout ce qui est déclaré à l'intérieur peut toujours être utilisé en dehors.

`for i in range(3): pass print(i)`

Cela affichera `2` car la dernière itération de la boucle `for` a assigné `2` à `i`.