# Méga Ferme
Ce déblocage incroyablement puissant augmente considérablement la taille de la ferme et vous donne accès à plusieurs drones.

Pour faciliter la gestion, vous recevez toujours exactement 36 nouvelles parcelles pour chaque nouveau drone. Le ratio de drones à parcelles reste constant.

## Drones Multiples
Comme avant, vous commencez toujours avec un seul drone. Les drones supplémentaires doivent d'abord être créés et disparaîtront après la fin du programme.
Chaque drone exécute sa propre instance de programme. Les drones peuvent créer de nouveaux drones en utilisant
`new_drone_id = spawn_drone("filename")`

Cela crée un nouveau drone à la même position que le drone qui a exécuté la commande `spawn_drone("filename")`. Le nouveau drone commencera à exécuter le programme dans le fichier nommé `filename`, donc remplacez `"filename"` par le nom du fichier que vous souhaitez exécuter.

Vous pouvez envisager cela comme si vous disiez à votre drone d'aller dans le fichier nommé `filename` et de cliquer sur le bouton d'exécution pour le prochain drone.

Les drones ne se heurtent pas entre eux.

Utilisez `max_drones()` pour obtenir le nombre maximum de drones qui peuvent être créés.
Utilisez `num_drones()` pour obtenir le nombre de drones déjà présents sur la ferme.
Utilisez `get_drone_id()` pour savoir quel drone exécute le code.

Exemple:

Dans un fichier nommé `farming routine`:
`if get_drone_id() == 0:
    # Seul le premier drone exécutera ceci
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Cela provoquera le déplacement horizontal de votre premier drone et la création d'autres drones. Les drones créés se déplaceront alors verticalement et récolteront tout sur leur passage.

<spoiler=show hint>Le moyen le plus simple d'utiliser plusieurs drones est de diviser votre ferme entre eux. Les améliorations sont conçues pour que chaque drone puisse toujours avoir un champ de 6x6.
</spoiler>

### Tout ce qui se trouve ci-dessous est assez avancé et pas nécessaire pour l'agriculture de base

## Conditions de Course
Plusieurs drones peuvent interagir avec la même parcelle de terrain en même temps. Si deux drones interagissent avec la même parcelle au même moment, l'action du drone avec l'ID le plus bas se produira en premier.

Par exemple, imaginez que les drones `0` et `1` soient tous les deux au-dessus du même arbre presque complètement développé.
Le drone `0` appelle
`use_item(Items.Fertilizer)`
Le drone `1` appelle
`harvest()`

Si ces actions se produisent en même temps, l'arbre sera d'abord fertilisé puis récolté. Dans ce cas, vous recevrez du bois. Cependant, si le drone `1` est légèrement plus rapide, l'arbre sera récolté avant d'être fertilisé, et vous ne recevrez pas le bois.
Ceci est appelé une "condition de course". C'est un problème courant en programmation parallèle, où le résultat dépend de l'ordre dans lequel les opérations sont effectuées.

Voici une autre situation problématique qui peut survenir lorsque plusieurs drones exécutent le même code simultanément au même endroit.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si plusieurs drones exécutent cela en même temps, ils exécuteront tous la première ligne, ce qui les placera dans le bloc `if`. Ensuite, ils utiliseront tous de l'eau, gaspillant une grande quantité.
Au moment où un drone atteint la deuxième ligne, `get_water()` peut ne plus être inférieur à `0.5` car un autre drone a irrigué la parcelle entre-temps.

## Communication des Drones
Si vous êtes intéressé par des stratégies plus avancées, vous pouvez vouloir que vos drones communiquent entre eux en utilisant des fonctions de passage de messages.

Envoyez n'importe quelle valeur à un autre drone :
`send(data, receiver_drone_id)`

Recevez la prochaine valeur envoyée par n'importe quel drone :
`data = receive()`

Recevez la prochaine valeur envoyée par un drone spécifique :
`data = receive(sender_drone_id)`

Le temps d'exécution de `send()` dépend de la taille des données envoyées. Par exemple, envoyer un grand dictionnaire nécessite une copie, ce qui peut prendre un certain temps.

`receive()` n'attend pas qu'un message arrive. Si aucun message n'a encore été envoyé, il retournera `None`.

Vous pouvez créer une fonction qui attend un message de cette manière :
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Une application utile du passage de messages est d'avoir une fonction qui crée un drone et lui envoie une fonction à exécuter.
Dans un fichier nommé `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Envoyer des fonctions de cette manière peut être très lent car tout l'état capturé de la fonction, y compris toutes les variables globales, doit être copié.