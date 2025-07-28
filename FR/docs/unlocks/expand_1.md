# Expansion 1
<unlock=for>Voir aussi [Expansion_2](docs/unlocks/expand_2.md)

</unlock>Votre ferme a grandi ! Cet espace n'est pas très utile si vous ne pouvez pas déplacer le drone, il y a donc une nouvelle fonction `move()` qui déplace le drone. `move()` nécessite que vous spécifiez la direction dans laquelle vous voulez que le drone se déplace. Il y a quatre nouvelles constantes pour cela : `North, East, South, West`

Par exemple, `move(North)` déplacera le drone d'une case vers le nord.

Si vous dépassez le bord de la ferme, le drone sera déplacé de l'autre côté de la ferme.
L'exemple de code suivant continuera de déplacer le drone vers le nord et reviendra au début lorsqu'il atteindra le bord de la ferme :

`while True:
	move(North)`