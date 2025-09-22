# Importation
Mettre tout ton code dans un seul fichier devient vite ingérable.
Les instructions `import` te permettent d'importer des fonctions et des variables globales d'un autre fichier.
Comment ça marche en une capture d'écran :
![](ImportsInOnePicture400)

Ici, `import module2` exécute le fichier nommé `module2` et te donne accès à toutes ses variables globales.
Tu peux ensuite accéder aux variables et fonctions du module importé en utilisant l'opérateur `.`.
Donc, dans cet exemple, `module2.print_x()` appelle `print_x()` dans `module2`.

### Pour aller plus loin
Tu peux aussi déplacer les variables globales du module importé dans la portée actuelle où l'instruction d'importation est exécutée en utilisant la syntaxe `from`.

`from module2 import print_x
print_x()`
Importe uniquement les variables globales spécifiées de `module2`.

ou

`from module2 import *
print_x()`
Importe toutes les variables globales de `module2`.

Cela importe également le fichier `module2`, mais au lieu d'y accéder via une variable nommée `module2`, ça dépaquette les globales de `module2` et les assigne directement dans la portée locale.

Cette forme d'importation n'est généralement pas recommandée car elle ne fonctionne pas bien lorsque deux fichiers s'importent mutuellement, et tu pourrais accidentellement écraser des variables dans le fichier importateur à cause de collisions de noms. Il est plus sûr d'éviter la syntaxe `from` si tu ne sais pas ce que tu fais.

# Comment ça marche vraiment

## En bref
Les importations peuvent être assez peu intuitives, mais la plupart des problèmes peuvent être évités en s'en tenant à la syntaxe `import file` au lieu de `from file import`, et en enveloppant tout ce qui n'est pas une définition globale dans
`if __name__ == "__main__":`

## Effets de bord de l'importation
La première fois que tu importes un fichier, il exécutera le fichier entier et te donnera ensuite accès à toutes les variables qui ont été définies pendant l'exécution.
Si tu importes le même fichier à nouveau, il renverra simplement le module mis en cache de la première fois.

Cela signifie que les instructions d'importation peuvent avoir des effets de bord. Si tu importes un fichier qui appelle `harvest()`, il récoltera réellement pendant l'importation. Mais lorsque tu l'importeras à nouveau, il ne récoltera pas de nouveau car le fichier n'est exécuté qu'une seule fois.

Il y a un moyen d'éviter de tels effets de bord en utilisant la variable `__name__`. C'est une variable qui est automatiquement définie à `"__main__"` lorsqu'un fichier est exécuté directement, et au nom du fichier lorsqu'un fichier est exécuté via `import`.
Il est considéré comme une bonne pratique de mettre tout code que tu ne veux pas exécuter lorsque le fichier est importé à l'intérieur d'un bloc `if __name__ == "__main__":`.

Une structure de fichier courante en Python consiste à mettre le code qui doit être exécuté lorsque le fichier est lancé dans une fonction `main()`. De cette façon, tu as une distinction claire entre les variables locales (définies à l'intérieur de `main()`) et les variables globales qui peuvent être importées (définies à l'extérieur de `main()`).

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
-`a` continue son exécution et initialise `x`.

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
-`b` dépaquette tout ce qui se trouve actuellement dans `a` dans sa propre portée globale. À ce stade, `a` ne contient rien car il n'a pas encore atteint la ligne `x = 0`, donc rien n'est importé.
-`b` exécute l'instruction `def` et stocke la fonction `f()`.
-`a` continue son exécution et initialise `x`.

Si quelqu'un appelle maintenant `b.f()`, il obtiendra une erreur indiquant que `x` n'existe pas dans la portée actuelle. C'est parce que cette fois `b` n'a pas de référence au `a` qui est encore en cours de chargement et ne voit pas les définitions qui ont été ajoutées après l'importation.