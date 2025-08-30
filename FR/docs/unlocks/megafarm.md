# Méga Ferme
Ce déblocage incroyablement puissant te donne accès à plusieurs drones.

Comme avant, tu commences avec un seul drone. Les drones supplémentaires doivent d'abord être créés et disparaîtront à la fin du programme.
Chaque drone exécute son propre programme. De nouveaux drones peuvent être créés en utilisant la fonction `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Cela fait apparaître un nouveau drone à la même position que celui qui a exécuté la commande `spawn_drone(function)`. Le nouveau drone se met alors à exécuter la fonction spécifiée. Une fois sa tâche terminée, il disparaît automatiquement.

Les drones n'entrent pas en collision les uns avec les autres.

Utilise `max_drones()` pour obtenir le nombre maximum de drones qui peuvent être créés.
Utilise `num_drones()` pour obtenir le nombre de drones déjà présents sur la ferme.


## Exemple :
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Cela fera en sorte que ton premier drone se déplace horizontalement et crée d'autres drones. Les drones créés se déplaceront ensuite verticalement et récolteront tout sur leur passage.

Si tous les drones disponibles ont déjà été créés, `spawn_drone()` ne fera rien et retournera `None`.

<spoiler=montrer l'indice>Jette un œil à cette fonction parallèle super utile `for_all`, qui prend n'importe quelle fonction et l'exécute sur chaque case de la ferme. Elle utilise tous les drones disponibles pour le faire.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

forall(harvest)`

Un modèle particulièrement utile est de créer un drone s'il y en a un de disponible, et sinon de faire le travail toi-même.

`if not spawn_drone(task):
	task()`
</spoiler>

## Attendre un autre drone
Utilise la fonction `wait_for(drone)` pour attendre qu'un autre drone ait terminé. Tu reçois le handle du `drone` lorsque tu le crées.
`wait_for(drone)` retourne la valeur de retour de la fonction que l'autre drone exécutait.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Note que la création de drones prend du temps, ce n'est donc pas une bonne idée de créer un nouveau drone pour chaque petite chose.

## Pas de mémoire partagée
Chaque drone a sa propre mémoire et ne peut pas lire ou écrire directement dans les variables globales d'un autre drone.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Cela affichera `0` car le nouveau drone a incrémenté sa propre copie de la variable globale `x`, ce qui n'affecte pas le `x` du premier drone.

## Race Conditions
Plusieurs drones peuvent interagir avec la même case de la ferme en même temps. Si deux drones interagissent avec la même case pendant le même tick, les deux interactions se produiront, mais les résultats peuvent différer en fonction de l'ordre des interactions.

Par exemple, imagine que les drones `0` et `1` sont tous les deux sur le même arbre qui est presque entièrement développé.
Le drone `0` appelle
`use_item(Items.Fertilizer)`
Le drone `1` appelle
`harvest()`

Si ces actions se produisent en même temps, l'arbre sera d'abord fertilisé puis récolté. Dans ce cas, tu en recevras du bois. Cependant, si le drone `1` est légèrement plus rapide, l'arbre sera récolté avant d'être fertilisé, et tu ne recevras pas le bois.
C'est ce qu'on appelle une "race condition". C'est un problème courant en programmation parallèle, où le résultat dépend de l'ordre dans lequel les opérations sont effectuées.

Voici une autre situation problématique qui peut se produire lorsque plusieurs drones exécutent le même code simultanément au même endroit.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si plusieurs drones l'exécutent simultanément, ils exécuteront tous la première ligne, ce qui les placera dans le bloc `if`. Ensuite, ils utiliseront tous de l'eau, en gaspillant une grande partie.
Au moment où un drone atteint la deuxième ligne, `get_water()` pourrait ne plus être inférieur à `0.5` car un autre drone a arrosé la case entre-temps.