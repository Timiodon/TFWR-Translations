# Portées des Noms (Scopes)
Les scopes déterminent quelles variables peuvent être accédées et d'où. Un scope est essentiellement une correspondance entre des noms et des valeurs.
Ils fonctionnent essentiellement de la même manière qu'en Python.

Il y a un scope global, et chaque fonction a un scope local.
Lorsque vous définissez une variable, elle est ajoutée au scope actuel.
Tout ce qui se trouve en dehors d'une définition de fonction est considéré comme faisant partie du scope global.

`x = 1`
Assigne une valeur de `1` au nom `x` dans le scope global.

Cette instruction `def` assigne une fonction au nom `f` dans le scope global.
`def f():
    `Assigne une valeur de `1` au nom `y` dans le scope local de `f`.`
    y = 1

    `Assigne une fonction au nom `g` dans le scope local de `f`.`
    def g():
        pass`

`f()`
Récupère la fonction stockée dans `f` depuis le scope global et l'appelle.

`print(y)`
Cette instruction print dans le scope global lève une erreur car `y` n'a jamais été déclaré dans le scope global, donc nous ne pouvons pas le lire ici.
Il n'existait que dans le scope local de `f`.

## Le mot-clé global
Par défaut, toutes les variables dans les fonctions se lient au scope local, même si une variable du même nom existe dans le scope global.

`x = 0

def f():
    x = 1
f()
print(x)`

Ce code affiche `0` car le `x` local à l'intérieur de `f` n'est pas la même variable que le `x` global, donc le `x` global reste inchangé. C'est important car sinon un appel de fonction pourrait accidentellement écraser une variable globale qui se trouve avoir le même nom qu'une variable locale de cette fonction.

Si vous voulez écrire dans une variable globale, vous devez le faire explicitement en utilisant le mot-clé `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Dans cet exemple, `global x` lie `x` à la variable globale `x` définie au-dessus. Cela affichera maintenant `1`.
Notez que changer les variables globales est généralement le premier pas vers du code spaghetti, où chaque partie du programme affecte toutes les autres parties du programme, donc n'en abusez pas.

## Boucles et branchements
Les boucles et les branchements ne créent pas leurs propres scopes, donc tout ce qui y est déclaré peut toujours être utilisé à l'extérieur.

`for i in range(3):
    pass
print(i)`

Ceci affichera `2` car la dernière itération de la boucle `for` a assigné `2` à `i`.