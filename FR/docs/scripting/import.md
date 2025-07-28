# Import
Mettre tout votre code dans un seul fichier devient vite ingérable.
Les instructions `import` vous permettent d'importer des fonctions et des variables globales d'un autre fichier.

`import filename`

C'est la forme la plus simple d'instruction d'importation. Elle vous donnera accès à tout ce qui est défini dans le fichier nommé `filename`. Chaque fenêtre du jeu est un fichier, et le nom du fichier est le nom affiché en haut de la fenêtre.

Voici un exemple avec deux fichiers :
Fichier nommé helper :
`x = 0

def say_hello():
    print("hello from helper")`

Un autre fichier :
`import helper
helper.say_hello()
helper.x += 1`

Ici, `import helper` exécute le fichier nommé `helper` et vous donne accès à toutes ses globales.
Vous pouvez ensuite accéder aux variables et fonctions du module importé en utilisant l'opérateur `.`.
Donc, dans cet exemple, `helper.say_hello()` appelle `say_hello()` à l'intérieur de helper et la dernière ligne incrémente la variable globale x.

Vous pouvez également déplacer les globales du module importé dans le scope actuel où l'instruction d'importation est exécutée en utilisant la syntaxe `from`.

`from helper import *`
Importe toutes les globales de helper.

ou

`from helper import say_hello`
Importe uniquement les globales spécifiées de helper.

Ceci importe également le fichier helper, mais au lieu d'y accéder via une variable nommée `helper`, il dépaquette les globales de `helper` et les assigne directement dans le scope local.

`from helper import say_hello
say_hello()`

Cette forme d'importation n'est généralement pas recommandée car elle ne fonctionne pas bien lorsque deux fichiers s'importent mutuellement, et vous pourriez accidentellement écraser des variables dans le fichier importateur en raison de collisions de noms.

# Comment ça marche vraiment

## TLDR
Les importations peuvent être assez peu intuitives, mais la plupart des problèmes peuvent être évités en s'en tenant à la syntaxe `import file` au lieu de `from file import`, et en enveloppant tout ce qui n'est pas une définition globale dans
`if __name__ == "__main__":`

## Effets de bord de l'importation
La première fois que vous importez un fichier, il exécutera le fichier entier puis vous donnera accès à toutes les variables qui ont été définies pendant l'exécution.
Si vous importez le même fichier à nouveau, il retournera simplement le module mis en cache la première fois.

Cela signifie que les instructions d'importation peuvent avoir des effets de bord. Si vous importez un fichier qui appelle `harvest()`, il récoltera réellement pendant l'importation. Mais lorsque vous l'importerez à nouveau, il ne récoltera pas à nouveau car le fichier n'est exécuté qu'une seule fois.

Il existe un moyen d'éviter de tels effets de bord en utilisant la variable `__name__`. C'est une variable qui est automatiquement définie sur `"__main__"` lorsqu'un fichier est exécuté directement, et sur le nom du fichier lorsqu'un fichier est exécuté via `import`.
Il est considéré comme une bonne pratique de mettre tout code que vous ne voulez pas exécuter lorsque le fichier est importé à l'intérieur d'un bloc `if __name__ == "__main__":`.

Une structure de fichier courante en Python consiste à mettre le code qui doit être exécuté lorsque le fichier est lancé dans une fonction `main()`. De cette façon, vous avez une distinction claire entre les variables locales (définies à l'intérieur de `main()`) et les variables globales qui peuvent être importées (définies à l'extérieur de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Cycles d'importation
Que se passe-t-il si le fichier `a` importe le fichier `b` et que le fichier `b` importe le fichier `a` ?

fichier `a` :
`import b
x = 0`

fichier `b` :
`import a
def f():
    print(a.x)`

Cela fonctionnera très bien. Disons qu'aucun des deux fichiers n'est encore chargé, et que quelqu'un d'autre exécute `import a`.

-`a` s'exécute jusqu'à la ligne `import b`.
-`b` s'exécute jusqu'à la ligne `import a`.
-Le module `a` existe déjà, mais ne contient pas `x` car il n'a atteint que la ligne `import b`.
-`b` stocke une référence au module `a` à moitié chargé dans une variable appelée `a`.
-`b` exécute l'instruction `def` et stocke la fonction `f()`.
-`a` continue de s'exécuter et initialise `x`.

Quand quelqu'un appelle `b.f()`, il affichera correctement `0` car le module `a` auquel `b` a une référence est maintenant entièrement chargé.

Considérons maintenant le même code en utilisant la syntaxe `from`.

fichier `a` :
`from b import *
x = 0`

fichier `b` :
`from a import *
def f():
    print(x)`

-`a` s'exécute jusqu'à la ligne `from b import *`.
-`b` s'exécute jusqu'à la ligne `from a import *`.
-Le module `a` existe déjà, mais n'a pas encore été entièrement exécuté.
-`b` dépaquette tout ce qui se trouve actuellement dans `a` dans son propre scope global. À ce stade, `a` ne contient rien car il n'a pas encore atteint la ligne `x = 0`, donc rien n'est importé.
-`b` exécute l'instruction `def` et stocke la fonction `f()`.
-`a` continue de s'exécuter et initialise `x`.

Si quelqu'un appelle maintenant `b.f()`, il obtiendra une erreur indiquant que `x` n'existe pas dans le scope actuel. C'est parce que cette fois, `b` n'a pas de référence à `a` qui est encore en cours de chargement et ne voit pas les définitions qui ont été ajoutées après l'importation.