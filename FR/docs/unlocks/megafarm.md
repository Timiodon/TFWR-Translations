# Méga Ferme
Ce déblocage incroyablement puissant augmente considérablement la taille de la ferme et vous donne accès à plusieurs drones.

Pour faciliter les choses, vous recevez toujours exactement 36 nouvelles cases pour chaque nouveau drone. Le ratio drones/cases reste constant.

## Plusieurs Drones
Comme avant, vous commencez toujours avec un seul drone. Les drones supplémentaires doivent d'abord être créés (spawned) et disparaîtront à la fin du programme.
Chaque drone exécute sa propre instance de programme séparée. Les drones peuvent créer de nouveaux drones en utilisant
`new_drone_id = spawn_drone("filename")`

Cela crée un nouveau drone à la même position que le drone qui a exécuté la commande `spawn_drone("filename")`. Le nouveau drone commencera à exécuter le programme dans le fichier nommé `filename`, donc remplacez `"filename"` par le nom du fichier que vous voulez exécuter.

Vous pouvez voir cela comme si vous aviez dit à votre drone d'aller au fichier nommé `filename` et d'appuyer sur le bouton d'exécution pour le prochain drone.

Les drones n'entrent pas en collision les uns avec les autres.

Utilisez `max_drones()` pour obtenir le nombre maximum de drones pouvant être créés.
Utilisez `num_drones()` pour obtenir le nombre de drones qui sont déjà dans la ferme.
Utilisez `get_drone_id()` pour savoir quel drone exécute le code.

Exemple :

Dans un fichier nommé `routine de culture` :
`if get_drone_id() == 0:
    # Seul le premier drone exécutera ceci
    while num_drones() < max_drones():
        spawn_drone("routine de culture")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Cela fera que votre premier drone se déplacera horizontalement et créera plus de drones. Les drones créés se déplaceront ensuite verticalement et récolteront tout sur leur passage.

<spoiler=montrer l'indice>
La manière la plus simple d'utiliser plusieurs drones est de diviser votre ferme entre eux. Les améliorations sont conçues pour que chaque drone puisse toujours avoir un champ de 6x6.
</spoiler>

Tout ce qui suit est assez avancé et n'est pas nécessaire pour la culture de base

## Conditions de course
Plusieurs drones peuvent interagir avec la même case de la ferme en même temps. Si deux drones interagissent avec la même case pendant le même tick, l'action du drone avec l'ID de drone le plus bas se produira en premier.

Par exemple, imaginez que les drones `0` et `1` sont tous les deux sur le même arbre qui est presque entièrement développé.
Le drone `0` appelle
`use_item(Items.Fertilizer)`
Le drone `1` appelle
`harvest()`

Si ces actions se produisent en même temps, l'arbre sera d'abord fertilisé puis récolté. Dans ce cas, vous en recevrez du bois. Cependant, si le Drone `1` est légèrement plus rapide, l'arbre sera récolté avant d'être fertilisé, et vous ne recevrez pas le bois.
C'est ce qu'on appelle une "condition de course". C'est un problème courant en programmation parallèle, où le résultat dépend de l'ordre dans lequel les opérations sont effectuées.

Voici une autre situation problématique qui peut se produire lorsque plusieurs drones exécutent le même code simultanément à la même position.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si plusieurs drones exécutent cela simultanément, ils exécuteront tous la première ligne, ce qui les mettra dans le bloc `if`. Ensuite, ils utiliseront tous de l'eau, en gaspillant beaucoup.
Au moment où un drone atteint la deuxième ligne, `get_water()` pourrait ne plus être inférieur à `0.5` car un autre drone a arrosé la case entre-temps.

## Communication entre drones
Si vous êtes intéressé par des stratégies plus avancées, vous voudrez peut-être que vos drones communiquent entre eux en utilisant des fonctions de passage de messages.

Envoyer n'importe quelle valeur à un autre drone :
`send(data, receiver_drone_id)`

Recevoir la prochaine valeur envoyée par n'importe quel drone :
`data = receive()`

Recevoir la prochaine valeur envoyée par un drone spécifique :
`data = receive(sender_drone_id)`

Le temps d'exécution de `send()` dépend de la taille des données envoyées. Par exemple, envoyer un grand dictionnaire nécessite une copie, ce qui peut prendre un certain temps.

`receive()` n'attend pas qu'un message arrive. Si aucun message n'a encore été envoyé, il retournera `None`.

Vous pouvez construire une fonction qui attend un message comme ceci :
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Une application utile du passage de messages est d'avoir une fonction qui crée un drone et lui envoie une fonction à exécuter.
Dans un fichier nommé `drone_spawning` :
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Envoyer des fonctions de cette manière peut être très lent car tout l'état capturé de la fonction, y compris toutes les variables globales, doit être copié.