# Import
Mettre tout ton code dans un seul fichier devient vite ingérable.
Les instructions `import` te permettent d'importer des fonctions et des variables globales d'un autre fichier.

`import nom_de_fichier`

C'est la forme la plus simple d'instruction d'importation. Elle te donnera accès à tout ce qui est défini dans le fichier nommé `nom_de_fichier`. Chaque fenêtre du jeu est un fichier, et le nom du fichier est celui affiché en haut de la fenêtre.

Voici un exemple avec deux fichiers :
Fichier nommé helper :
`x = 0

def say_hello():
    print("hello from helper")`

Un autre fichier :
`import helper
helper.say_hello()
helper.x += 1`

Ici, `import helper` exécute le fichier nommé `helper` et te donne accès à toutes ses globales.
Tu peux ensuite accéder aux variables et fonctions du module importé en utilisant l'opérateur `.`.
Donc dans cet exemple, `helper.say_hello()` appelle `say_hello()` à l'intérieur de helper et la dernière ligne incrémente la variable globale x.

Tu peux aussi déplacer les globales du module importé dans la portée actuelle où l'instruction d'importation est exécutée en utilisant la syntaxe `from`.

`from helper import *`
Importe toutes les globales de helper.

ou

`from helper import say_hello`
Importe seulement les globales spécifiées de helper.

Cela importe aussi le fichier helper, mais au lieu d'y accéder via une variable nommée `helper`, il décompresse les globales de `helper` et les assigne directement dans la portée locale.

`from helper import say_hello
say_hello()`

Cette forme d'importation n'est généralement pas recommandée car elle ne fonctionne pas bien lorsque deux fichiers s'importent mutuellement, et tu pourrais accidentellement écraser des variables dans le fichier importateur en raison de collisions de noms.

# Comment ça marche vraiment

## TLDR
Les importations peuvent être assez contre-intuitives, mais la plupart des problèmes peuvent être évités en s'en tenant à la syntaxe `import file` au lieu de `from file import`, et en enveloppant tout ce qui n'est pas une définition globale dans
`if __name__ == "__main__":`

## Effets de Bord de l'Importation
La première fois que tu importes un fichier, il exécutera le fichier entier puis te donnera accès à toutes les variables qui ont été définies pendant l'exécution.
Si tu importes le même fichier à nouveau, il renverra simplement le module mis en cache de la première fois.

Cela signifie que les instructions d'importation peuvent avoir des effets de bord. Si tu importes un fichier qui appelle `harvest()`, il récoltera réellement pendant l'importation. Mais lorsque tu l'importeras à nouveau, il ne récoltera pas une seconde fois car le fichier n'est exécuté qu'une seule fois.

Il existe un moyen d'éviter de tels effets de bord en utilisant la variable `__name__`. C'est une variable qui est automatiquement définie à `"__main__"` lorsqu'un fichier est exécuté directement, et au nom du fichier lorsqu'un fichier est exécuté via `import`.
Il est considéré comme une bonne pratique de mettre tout code que tu ne veux pas exécuter lorsque le fichier est importé à l'intérieur d'un bloc `if __name__ == "__main__":`.

Une structure de fichier courante en Python consiste à mettre le code qui doit être exécuté lorsque le fichier est lancé dans une fonction `main()`. De cette façon, tu as une distinction claire entre les variables locales (définies à l'intérieur de `main()`) et les variables globales qui peuvent être importées (définies à l'extérieur de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # faire des choses

if __name__ == "__main__":
    main()`

## Cycles d'Importation
Que se passe-t-il si le fichier `a` importe le fichier `b` et que le fichier `b` importe le fichier `a` ?

Fichier `a` :
`import b
x = 0`

Fichier `b` :
`import a
def f():
    print(a.x)`

Cela fonctionnera bien. Disons qu'aucun des deux fichiers n'est encore chargé, et que quelqu'un d'autre exécute `import a`.

- `a` s'exécute jusqu'à la ligne `import b`.
- `b` s'exécute jusqu'à la ligne `import a`.
- Le module `a` existe déjà, mais ne contient pas `x` car il n'a atteint que la ligne `import b`.
- `b` stocke une référence au module `a` à moitié chargé dans une variable appelée `a`.
- `b` exécute l'instruction `def` et stocke la fonction `f()`.
- `a` continue de s'exécuter et initialise `x`.

Lorsque quelqu'un appelle `b.f()`, il affichera correctement `0` car le module `a` auquel `b` a une référence est maintenant entièrement chargé.

Considérons maintenant le même code en utilisant la syntaxe `from`.

Fichier `a` :
`from b import *
x = 0`

Fichier `b` :
`from a import *
def f():
    print(x)`

- `a` s'exécute jusqu'à la ligne `from b import *`.
- `b` s'exécute jusqu'à la ligne `from a import *`.
- Le module `a` existe déjà, mais n'a pas encore été entièrement exécuté.
- `b` décompresse tout ce qui se trouve actuellement dans `a` dans sa propre portée globale. À ce stade, `a` ne contient rien car il n'a pas encore atteint la ligne `x = 0`, donc rien n'est importé.
- `b` exécute l'instruction `def` et stocke la fonction `f()`.
- `a` continue de s'exécuter et initialise `x`.

Si quelqu'un appelle maintenant `b.f()`, il obtiendra une erreur indiquant que `x` n'existe pas dans la portée actuelle. C'est parce que cette fois `b` n'a pas de référence au `a` en cours de chargement et ne voit pas les définitions qui ont été ajoutées après l'importation.